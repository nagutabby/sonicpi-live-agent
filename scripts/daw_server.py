#!/usr/bin/env python3
"""Sonic Pi のコードを DAW のように見て・直して・試聴するローカル専用 Web アプリ。

  daw_server.py [--port 8765] [--open]

http://127.0.0.1:<port>/ を開く。127.0.0.1 にしか待ち受けない(外部からは見えない)。標準ライブラリ + numpy のみ。
- 画面: トラックのタイムライン、ピアノロール、コード進行、stem・コード進行プリセットのライブラリ。
- ホットリロード: stems/・presets/・work/daw/ のファイルや画面(daw_static/index.html)が更新されると、画面が自動でリロードされる。サーバーのコード(scripts/daw_*.py)が更新されたら、サーバーが自分で再起動する。
- 試聴: ブラウザの簡易シンセ。本物の音は Sonic Pi で録音(live_render.py と同じ仕組み。録音中はスピーカーから鳴る)→ ブラウザで再生。
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
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse

import daw_codegen as codegen
import numpy as np
import sonicpi
import wav_stats
from common import ROOT, WORK

STATIC = Path(__file__).resolve().parent / "daw_static"
RENDERS = WORK / "renders"
PROJECTS = WORK / "daw"

JOB = {"state": "idle", "message": "", "wav": None, "stats": None, "started": 0.0}
JOB_LOCK = threading.Lock()


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


def wav_report(path: Path) -> dict:
    x, sr = wav_stats.load(str(path))
    mono = x.mean(axis=1)
    peak = float(np.abs(x).max())
    spec = np.abs(np.fft.rfft(mono)) ** 2
    freqs = np.fft.rfftfreq(len(mono), 1 / sr)
    tot = spec.sum() or 1.0
    bands = {n: round(float(spec[(freqs >= lo) & (freqs < hi)].sum() / tot * 100), 1) for n, lo, hi in wav_stats.BANDS}
    n = 900
    edge = np.linspace(0, len(mono), n + 1, dtype=int)
    wave_peaks = [round(float(np.abs(mono[a:b]).max()) if b > a else 0.0, 4) for a, b in zip(edge[:-1], edge[1:], strict=True)]
    step = sr  # 1 秒ごと
    rms = [round(wav_stats.db(float(np.sqrt((mono[i : i + step] ** 2).mean()))), 1) for i in range(0, max(len(mono) - step // 2, 1), step)]
    corr = None
    if x.shape[1] == 2 and x[:, 0].std() > 0 and x[:, 1].std() > 0:
        corr = round(float(np.corrcoef(x[:, 0], x[:, 1])[0, 1]), 2)
    return {"seconds": round(len(mono) / sr, 2), "peak_db": round(wav_stats.db(peak), 1), "clip": peak >= 0.999,
            "rms_db": round(wav_stats.db(float(np.sqrt((mono**2).mean()))), 1), "corr": corr, "bands": bands,
            "wave": wave_peaks, "rms_per_sec": rms}


def render_job(text: str, seconds: float) -> None:
    try:
        code = text + f"\n\nuse_bpm 60\nsleep {seconds}\n"
        RENDERS.mkdir(parents=True, exist_ok=True)
        vs = [int(m.group(1)) for f in RENDERS.glob("daw_v*.wav") if (m := re.fullmatch(r"daw_v(\d+)\.wav", f.name))]
        out = RENDERS / f"daw_v{max(vs, default=0) + 1}.wav"
        with tempfile.TemporaryDirectory() as td:
            raw = Path(td) / "raw.wav"
            try:
                sonicpi.record(code, seconds, raw)
            except SystemExit as e:  # sonicpi.record は失敗を sys.exit(メッセージ) で知らせる
                raise RuntimeError(str(e)) from None
            r = subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(raw), "-ar", "48000", "-c:a", "pcm_s16le", str(out)],
                               capture_output=True, text=True)
            if r.returncode != 0:
                raise RuntimeError("ffmpeg での変換に失敗: " + r.stderr[-300:])
        with JOB_LOCK:
            JOB.update(state="done", message="録音できました", wav=out.name, stats=wav_report(out))
    except Exception as e:  # 画面にそのまま見せる
        with JOB_LOCK:
            JOB.update(state="error", message=str(e), wav=None, stats=None)


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
            if u.path == "/api/job":
                with JOB_LOCK:
                    return self._json(dict(JOB))
            if u.path.startswith("/renders/"):
                return self._serve_wav(unquote(u.path[len("/renders/") :]))
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

    def _serve_wav(self, name: str) -> None:
        p = (RENDERS / name).resolve()
        if p.parent != RENDERS.resolve() or p.suffix != ".wav" or not p.is_file():
            return self._err("見つかりません", 404)
        data = p.read_bytes()
        rng = self.headers.get("Range")
        if rng and (m := re.fullmatch(r"bytes=(\d*)-(\d*)", rng)):
            start = int(m.group(1) or 0)
            end = int(m.group(2)) if m.group(2) else len(data) - 1
            end = min(end, len(data) - 1)
            return self._send(HTTPStatus.PARTIAL_CONTENT, data[start : end + 1], "audio/wav",
                              {"Content-Range": f"bytes {start}-{end}/{len(data)}", "Accept-Ranges": "bytes"})
        self._send(200, data, "audio/wav", {"Accept-Ranges": "bytes"})

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
            if path == "/api/render":
                return self._post_render(body)
            if path == "/api/project":
                proj = codegen.validate(body["project"])
                f = project_path(proj["name"])
                PROJECTS.mkdir(parents=True, exist_ok=True)
                f.write_text(json.dumps(body["project"], ensure_ascii=False, indent=1), encoding="utf-8")
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

    def _post_render(self, body: dict) -> None:
        text = codegen.generate(body["project"])  # GUI のプロジェクトから生成したコードを録音する(ミュート/ソロは生成時に反映)
        seconds = float(body.get("seconds", 8))
        if not 2 <= seconds <= 120:
            raise ValueError("seconds は 2〜120")
        with JOB_LOCK:
            if JOB["state"] == "running":
                return self._err("録音中です。終わるまでお待ちください", 409)
            JOB.update(state="running", message=f"{seconds:g} 秒を録音中(音が鳴ります)…", wav=None, stats=None, started=time.time())
        threading.Thread(target=render_job, args=(text, seconds), daemon=True).start()
        self._json({"version": version(), "ok": True})


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


def watch_code(srv) -> None:
    """サーバーのコード(scripts/daw_*.py)が更新されたら、自分で再起動する。録音中は終わるまで待つ。画面は version が変わるので自動でリロードされる。"""
    here = Path(__file__).resolve().parent
    files = sorted(here.glob("daw_*.py"))
    seen = {f: f.stat().st_mtime_ns for f in files}
    while True:
        time.sleep(1)
        if any(f.stat().st_mtime_ns != seen[f] for f in files if f.exists()) and JOB["state"] != "running":
            time.sleep(0.3)  # 書き込み途中を避ける
            print("[daw] コードが更新されたので再起動します", flush=True)
            srv.server_close()
            os.execv(sys.executable, [sys.executable, *sys.argv])


if __name__ == "__main__":
    main()
