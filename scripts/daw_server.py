#!/usr/bin/env python3
"""Sonic Pi のコードを DAW のように見て・直して・試聴するローカル専用 Web アプリ。

  daw_server.py [--port 8765] [--open]

http://127.0.0.1:<port>/ を開く。127.0.0.1 にしか待ち受けない(外部からは見えない)。標準ライブラリのみ。
- 画面: トラックのタイムライン、ピアノロール、コード進行、stem・コード進行プリセットのライブラリ。
- ホットリロード: stems/・presets/・work/daw/ のファイルや画面(daw_static/index.html)が更新されると、画面が自動でリロードされる。サーバーのコード(scripts/daw_*.py)が更新されたら、サーバーが自分で再起動する。
- 再生: ▶ は Sonic Pi の本物の音(ヘッドレスで常駐させた Sonic Pi に、再生位置から先のコードを送る。スピーカーから鳴る)。stem の試聴だけはブラウザの簡易音。
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import webbrowser
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse

import daw_codegen as codegen
import sonicpi
from common import ROOT, WORK

STATIC = Path(__file__).resolve().parent / "daw_static"
PROJECTS = WORK / "daw"



PLAYER_RB = ROOT / "scripts" / "sonicpi_player.rb"
PLAY_TMP = Path(tempfile.mkdtemp(prefix="daw_play_"))


class Player:
    """常駐の Sonic Pi(sonicpi_player.rb)に、再生位置から先のコードを送って鳴らす。最初の起動に十数秒かかる。"""

    def __init__(self) -> None:
        self.proc: subprocess.Popen | None = None
        self.ready = threading.Event()
        self.lock = threading.Lock()
        self.errors: list[str] = []
        self.replies: list[str] = []
        self.stopper: threading.Timer | None = None
        self.seq = 0

    def start(self) -> None:
        with self.lock:
            if self.proc and self.proc.poll() is None:
                return
            ruby, app = sonicpi.find_ruby(), sonicpi.find_app()
            if not (ruby and app):
                raise ValueError("Sonic Pi と ruby が見つかりません(brew install --cask sonic-pi)")
            self.ready.clear()
            self.proc = subprocess.Popen([ruby, str(PLAYER_RB)], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                         stderr=subprocess.STDOUT, text=True, env={**os.environ, "SONIC_PI_APP": str(app)},
                                         start_new_session=True)
            threading.Thread(target=self._read, args=(self.proc,), daemon=True).start()

    def _read(self, proc) -> None:
        for line in proc.stdout:
            line = line.rstrip()
            if line == "READY":
                self.ready.set()
            elif line.startswith("ERRORS") or "ERROR" in line:
                self.errors.append(line)
            elif line in ("PLAYING", "STOPPED"):
                self.replies.append(line)
        self.ready.clear()

    def status(self) -> dict:
        return {"ready": self.ready.is_set(), "running": bool(self.proc and self.proc.poll() is None), "errors": self.errors[-8:]}

    def _send(self, text: str) -> None:
        assert self.proc and self.proc.stdin
        self.proc.stdin.write(text + "\n")
        self.proc.stdin.flush()

    def play(self, body: dict) -> dict:
        """body: project, start_cell, end_cell(省略 = 最後まで), loop。範囲を鳴らす。loop でなければ、終わったら止める。"""
        sliced = codegen.slice_project(body["project"], int(body.get("start_cell", 0)), body.get("end_cell"))
        code = codegen.generate(sliced)
        check = check_code(code)
        if check["code"] == 2:
            raise ValueError("生成コードに誤りがあります: " + check["output"][-300:])
        self.start()
        if not self.ready.wait(60):
            raise ValueError("Sonic Pi の起動が終わりません(別の Sonic Pi が動いていないか確認)")
        with self.lock:
            if self.stopper:
                self.stopper.cancel()
            self.seq += 1
            f = PLAY_TMP / f"play_{self.seq}.rb"
            f.write_text(code, encoding="utf-8")
            self.errors.clear()
            self._send(f"PLAY {f}")
            beats = sliced["bars"] * sliced["meter"]
            seconds = beats * 60 / sliced["bpm"]
            if not body.get("loop"):
                self.stopper = threading.Timer(seconds + 2.5, self.stop)   # 最後の余韻(リバーブなど)を待ってから止める
                self.stopper.daemon = True
                self.stopper.start()
        return {"ok": True, "seconds": round(seconds, 2), "check": check["output"] if check["code"] else ""}

    def stop(self) -> None:
        with self.lock:
            if self.stopper:
                self.stopper.cancel()
                self.stopper = None
            if self.proc and self.proc.poll() is None:
                try:
                    self._send("STOP")
                except OSError:
                    pass

    def quit(self) -> None:
        if self.proc and self.proc.poll() is None:
            try:
                self._send("QUIT")
                self.proc.wait(5)
            except (OSError, subprocess.TimeoutExpired):
                os.killpg(self.proc.pid, 15)


PLAYER = Player()


BOOT = str(time.time())  # 起動のたびに変わる(サーバーのコードが更新されて再起動したら、画面もリロードさせる)


def version() -> str:
    """画面のホットリロード用。画面・stem・プリセット・曲のファイルの更新時刻と、サーバーの起動時刻から決まる文字列。"""
    h = hashlib.sha1(BOOT.encode())
    files = [STATIC / "index.html", *sorted(codegen.STEMS.glob("*.json")), *sorted(codegen.PRESETS_DIR.glob("*.json")),
             *(sorted(PROJECTS.glob("*.json")) if PROJECTS.is_dir() else [])]
    for f in files:
        try:
            h.update(f"{f.name}:{f.stat().st_mtime_ns}".encode())
        except OSError:
            pass
    return h.hexdigest()[:12]


def project_path(name: str) -> Path:
    if not re.fullmatch(r"[A-Za-z0-9_-]{1,40}", name or ""):
        raise ValueError("プロジェクト名は英数字・_・- のみ(40 字まで)")
    return PROJECTS / f"{name}.json"


def check_code(code: str) -> dict:
    with tempfile.TemporaryDirectory() as td:
        f = Path(td) / "gen.rb"
        f.write_text(code, encoding="utf-8")
        r = subprocess.run([sys.executable, str(Path(__file__).with_name("live_check.py")), str(f)],
                           capture_output=True, text=True, timeout=60)
    return {"code": r.returncode, "output": (r.stdout + r.stderr).replace(td, "").strip()}


def backup_and_write(path: Path, new: str) -> None:
    hist = WORK / "history"
    hist.mkdir(parents=True, exist_ok=True)
    shutil.copy2(path, hist / f"{path.stem}_{datetime.now():%Y%m%d_%H%M%S}.rb")
    path.write_text(new, encoding="utf-8")


class Handler(BaseHTTPRequestHandler):
    server_version = "SonicPiDAW/1"

    def log_message(self, fmt, *args):
        sys.stderr.write("[daw] " + fmt % args + "\n")

    def _host_ok(self) -> bool:
        port = self.server.server_address[1]
        return self.headers.get("Host", "") in (f"127.0.0.1:{port}", f"localhost:{port}")

    def _send(self, code: int, body: bytes, ctype: str, extra: dict | None = None) -> None:
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        for k, v in (extra or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(body)

    def _json(self, obj, code: int = 200) -> None:
        self._send(code, json.dumps(obj, ensure_ascii=False).encode(), "application/json; charset=utf-8")

    def _err(self, msg: str, code: int = 400) -> None:
        self._json({"error": msg}, code)

    def do_GET(self) -> None:
        if not self._host_ok():
            return self._err("Host が不正です", 403)
        u = urlparse(self.path)
        q = {k: v[0] for k, v in parse_qs(u.query).items()}
        try:
            if u.path in ("/", "/index.html"):
                return self._send(200, (STATIC / "index.html").read_bytes(), "text/html; charset=utf-8")
            if u.path == "/api/catalog":
                return self._json(codegen.catalog())
            if u.path.startswith("/api/sample/"):
                return self._serve_sample(unquote(u.path[len("/api/sample/") :]))
            if u.path == "/api/stems":
                return self._json({"stems": codegen.list_stems()})
            if u.path == "/api/presets":
                return self._json({"presets": codegen.list_presets()})
            if u.path == "/api/projects":
                files = sorted(PROJECTS.glob("*.json"), key=lambda f: f.stat().st_mtime, reverse=True) if PROJECTS.is_dir() else []
                return self._json({"projects": [f.stem for f in files]})   # 新しく更新した順(開くのは先頭)
            if u.path == "/api/version":
                return self._json({"version": version()})
            if u.path == "/api/project":
                return self._json(codegen.validate(json.loads(project_path(q.get("name", "")).read_text(encoding="utf-8"))))
        except (ValueError, FileNotFoundError) as e:
            return self._err(str(e))
        self._err("見つかりません", 404)

    def _serve_sample(self, name: str) -> None:
        """Sonic Pi 内蔵のサンプル(試聴用)。カタログにある名前だけ。"""
        if not re.fullmatch(r"[a-z0-9_]+", name) or name not in codegen.catalog()["samples"]:
            return self._err("見つかりません", 404)
        p = sonicpi.APP / "Contents/Resources/etc/samples" / f"{name}.flac"
        if not p.is_file():
            return self._err("サンプルのファイルが見つかりません", 404)
        self._send(200, p.read_bytes(), "audio/flac", {"Cache-Control": "max-age=3600"})

    def do_POST(self) -> None:
        if not self._host_ok():
            return self._err("Host が不正です", 403)
        origin = self.headers.get("Origin")
        if origin is not None and origin.split("://", 1)[-1] not in (f"127.0.0.1:{self.server.server_address[1]}",
                                                                    f"localhost:{self.server.server_address[1]}"):
            return self._err("Origin が不正です", 403)
        if "application/json" not in self.headers.get("Content-Type", ""):
            return self._err("Content-Type は application/json", 415)
        try:
            body = json.loads(self.rfile.read(min(int(self.headers.get("Content-Length", 0)), 1_000_000)) or b"{}")
            path = urlparse(self.path).path
            if path == "/api/play":
                return self._json({"version": version(), **PLAYER.play(body)})
            if path == "/api/stop":
                PLAYER.stop()
                return self._json({"ok": True})
            if path == "/api/player":
                PLAYER.start()
                return self._json({"ok": True, **PLAYER.status()})
            if path == "/api/project":
                proj = codegen.validate(body["project"])
                f = project_path(proj["name"])
                PROJECTS.mkdir(parents=True, exist_ok=True)
                f.write_text(json.dumps(body["project"], ensure_ascii=False, indent=1), encoding="utf-8")
                f.with_suffix(".rb").write_text(codegen.generate(body["project"]), encoding="utf-8")  # 生成コードも常に最新にする(古い .rb を Sonic Pi で鳴らして「反映されない」を防ぐ)
                return self._json({"version": version(), "ok": True, "name": proj["name"]})
            if path == "/api/preset":
                pr = codegen.validate_preset(body["preset"])
                pid = codegen.ident(body.get("id") or pr["name"], "") or "preset_" + hashlib.md5(pr["name"].encode()).hexdigest()[:6]
                f = codegen.PRESETS_DIR / f"{pid}.json"
                if f.exists() and not body.get("overwrite"):
                    return self._err(f"プリセット「{pr['name']}」は登録済みです(上書きするときは確認が出ます)", 409)
                codegen.PRESETS_DIR.mkdir(parents=True, exist_ok=True)
                f.write_text(json.dumps(pr, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
                return self._json({"version": version(), "ok": True, "id": pid})
            if path == "/api/preset/delete":
                pid = str(body.get("id", ""))
                f = codegen.PRESETS_DIR / f"{pid}.json"
                if not re.fullmatch(r"[a-z][a-z0-9_]{0,31}", pid) or not f.is_file():
                    raise ValueError("プリセットが見つかりません")
                f.unlink()
                return self._json({"version": version(), "ok": True})
            if path == "/api/stem":
                stem = codegen.validate_stem(body["stem"])
                sid = codegen.ident(body.get("id") or stem["name"], "") or "stem_" + hashlib.md5(stem["name"].encode()).hexdigest()[:6]  # 日本語名は名前から決まる ID にする
                f = codegen.STEMS / f"{sid}.json"
                if f.exists() and not body.get("overwrite"):
                    return self._err(f"stem「{sid}」は登録済みです(上書きするときは確認が出ます)", 409)
                codegen.STEMS.mkdir(parents=True, exist_ok=True)
                f.write_text(json.dumps(stem, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
                return self._json({"version": version(), "ok": True, "id": sid})
            if path == "/api/stem/delete":
                sid = str(body.get("id", ""))
                f = codegen.STEMS / f"{sid}.json"
                if not re.fullmatch(r"[a-z][a-z0-9_]{0,23}", sid) or not f.is_file():
                    raise ValueError("stem が見つかりません")
                f.unlink()
                return self._json({"version": version(), "ok": True})
            if path == "/api/code":
                code = codegen.generate(body["project"])
                return self._json({"code": code, "check": check_code(code)})
            if path == "/api/export":
                proj = codegen.validate(body["project"])
                code = codegen.generate(body["project"])
                if body.get("target") == "current":
                    target = WORK / "current.rb"
                    if target.is_file():
                        backup_and_write(target, code)
                    else:
                        target.write_text(code, encoding="utf-8")
                else:
                    PROJECTS.mkdir(parents=True, exist_ok=True)
                    target = PROJECTS / f"{proj['name']}.rb"
                    target.write_text(code, encoding="utf-8")
                return self._json({"version": version(), "ok": True, "path": str(target.relative_to(ROOT)), "check": check_code(code)})
            return self._err("見つかりません", 404)
        except (ValueError, KeyError, TypeError, json.JSONDecodeError) as e:
            return self._err(f"{type(e).__name__}: {e}")

def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("--port", type=int, default=8765)
    ap.add_argument("--open", action="store_true", help="ブラウザを開く")
    a = ap.parse_args()
    srv = ThreadingHTTPServer(("127.0.0.1", a.port), Handler)
    url = f"http://127.0.0.1:{a.port}/"
    print(f"DAW ビューを起動しました: {url}(Ctrl+C で終了。このPCからだけ見えます)", flush=True)
    if a.open:
        webbrowser.open(url)
    threading.Thread(target=watch_code, args=(srv,), daemon=True).start()
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        PLAYER.quit()


def watch_code(srv) -> None:
    """サーバーのコード(scripts/daw_*.py)が更新されたら、自分で再起動する。画面は version が変わるので自動でリロードされる。"""
    here = Path(__file__).resolve().parent
    files = sorted(here.glob("daw_*.py"))
    seen = {f: f.stat().st_mtime_ns for f in files}
    while True:
        time.sleep(1)
        if any(f.stat().st_mtime_ns != seen[f] for f in files if f.exists()):
            time.sleep(0.3)  # 書き込み途中を避ける
            print("[daw] コードが更新されたので再起動します", flush=True)
            srv.server_close()
            PLAYER.quit()
            os.execv(sys.executable, [sys.executable, *sys.argv])


if __name__ == "__main__":
    main()
