#!/usr/bin/env python3
"""DAW の画面を操作して曲を再生し、画面録画に mp3 の音をぴったり重ねた mp4 を作る。

  record_video.py [プロジェクト名] [--start-bar 0] [--bars N] [--size 1280x720] [--fps 30] [--out work/videos/名前.mp4] [--dry-run]

やること(スピーカーから、同じ区間の音が 2 回鳴る):
  1. 音: 同じ区間のコードを live_render.py で録音(Sonic Pi の音の頭 = 録音の 0 秒)→ mp3
  2. 映像: Chrome の専用ウィンドウで DAW を開き(?rec=1 で自動再生)、ffmpeg で画面を録画する
  3. 合わせる: 画面の左上に出る白い(マゼンタの)四角は、再生が始まる瞬間に消える。その消えたフレームを音の頭にして、
     映像をそこから切り出し、mp3 を重ねて mp4 にする(フレーム単位でそろう)

前提: 画面収録の許可(システム設定 → プライバシーとセキュリティ → 画面収録とシステムオーディオ録音 → ターミナルを許可)、
DAW サーバーの起動(daw_server.py)、Google Chrome、ffmpeg。録画中はウィンドウを動かさない・手前に何も出さない。
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path

import daw_codegen
import numpy as np
from common import ROOT, WORK

SERVER = "http://127.0.0.1:8765"
CHROME = "Google Chrome"
FLAG_WINDOW = (120, 80)   # ウィンドウの左上から、合図の四角を探す範囲(pt)
TITLEBAR_PT = 32         # Chrome のアプリウィンドウの題名の帯の高さ(pt)
SCHED_AHEAD = 0.5       # Sonic Pi が音を先行して予約する時間(秒)。画面の LEAD(index.html)と同じ値
MIN_FLAG_PIXELS = 12      # マゼンタの画素がこの数以上あれば「合図あり」


def flag_end_time(counts: list[int], times: list[float], min_pixels: int = MIN_FLAG_PIXELS) -> float:
    """合図(マゼンタ)が見えていたフレームの最後の、次のフレームの時刻 = 再生が始まった時刻。"""
    last = max((i for i, c in enumerate(counts) if c >= min_pixels), default=None)
    if last is None:
        raise ValueError("合図の四角が映像に見つかりません(ウィンドウが隠れた・画面収録の許可がない・別の画面を録っている可能性)")
    if last + 1 >= len(times):
        raise ValueError("合図が最後まで消えませんでした(再生が始まらなかった可能性)")
    return times[last + 1]


def run(cmd: list[str], **kw) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, text=True, capture_output=True, **kw)


def osa(script: str) -> str:
    r = run(["osascript", "-e", script])
    if r.returncode != 0:
        raise RuntimeError(f"osascript に失敗: {r.stderr.strip()}")
    return r.stdout.strip()


def numbers(s: str) -> list[float]:
    return [float(x) for x in re.findall(r"-?\d+(?:\.\d+)?", s)]


def screen_size_pt() -> tuple[int, int]:
    r = run(["osascript", "-l", "JavaScript", "-e", 'ObjC.import("AppKit"); var f = $.NSScreen.screens.objectAtIndex(0).frame; f.size.width + " " + f.size.height'])
    w, h = numbers(r.stdout)[:2]
    return int(w), int(h)


def screen_width_pt() -> float:
    """メイン画面の幅(pt)。画面収録の画素数との比から、Retina の倍率を出す。"""
    return numbers(osa('ObjC.import("AppKit"); $.NSScreen.screens.objectAtIndex(0).frame.size.width'.join(["", ""])) if False else
                   run(["osascript", "-l", "JavaScript", "-e", 'ObjC.import("AppKit"); $.NSScreen.screens.objectAtIndex(0).frame.size.width']).stdout)[0]


def newest_project() -> str:
    files = sorted((WORK / "daw").glob("*.json"), key=lambda p: p.stat().st_mtime)
    if not files:
        sys.exit("[エラー] work/daw/ にプロジェクトがありません")
    return files[-1].stem


def server_up() -> bool:
    try:
        urllib.request.urlopen(f"{SERVER}/api/version", timeout=2).read()
        return True
    except (urllib.error.URLError, OSError):
        return False


def finish(workdir: Path, keep_raw: bool) -> int:
    """--- 3. 合わせる(合図が消えたフレーム = 音の頭) ---"""
    meta = json.loads((workdir / "meta.json").read_text(encoding="utf-8"))
    raw, bounds, mp3, out = workdir / "raw.mkv", meta["bounds"], Path(meta["mp3"]), Path(meta["out"])
    seconds, fps = meta["seconds"], meta["fps"]
    print("[3/3] 音と映像をそろえます…", flush=True)
    vw, vh = (int(x) for x in run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height", "-of", "csv=p=0:s=x", str(raw)]).stdout.strip().split("x"))
    dur = float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(raw)]).stdout.strip() or 0)
    scale = vw / screen_width_pt()
    x, y = round(bounds[0] * scale), round(bounds[1] * scale)
    cw, ch = round((bounds[2] - bounds[0]) * scale) // 2 * 2, round((bounds[3] - bounds[1]) * scale) // 2 * 2
    bar = round(TITLEBAR_PT * scale) // 2 * 2   # ウィンドウの題名の帯(合図の文字が映る)は、最終の映像から切る
    vy, ch = y + bar, ch - bar
    fw, fh = round(FLAG_WINDOW[0] * scale), round(FLAG_WINDOW[1] * scale)
    log = Path(tempfile.mkdtemp(prefix="rec_")) / "showinfo.txt"
    with log.open("w") as lf:
        p = subprocess.run(["ffmpeg", "-loglevel", "info", "-i", str(raw), "-vf", f"crop={fw}:{fh}:{x}:{y},showinfo", "-f", "rawvideo", "-pix_fmt", "rgb24", "pipe:1"],
                           stdout=subprocess.PIPE, stderr=lf)
    frames = np.frombuffer(p.stdout, dtype=np.uint8).reshape(-1, fh, fw, 3).astype(np.int16)
    mag = (frames[..., 0] > 200) & (frames[..., 1] < 70) & (frames[..., 2] > 200)
    counts = mag.sum(axis=(1, 2)).tolist()
    times = [float(t) for t in re.findall(r"pts_time:\s*([0-9.]+)", log.read_text())]
    try:
        t0 = flag_end_time(counts, times[: len(counts)], MIN_FLAG_PIXELS * round(scale) ** 2)
    except ValueError as e:
        sys.exit(f"[エラー] {e}")
    if dur < t0 + seconds - 1.0:
        sys.exit(f"[エラー] 画面録画が途中で止まっています(録画 {dur:.1f} 秒 / 必要 {t0 + seconds:.1f} 秒)。画面が暗くなった・ロックされた・画面収録の許可が外れた可能性があります。"
                 f"録画のログ: {workdir / 'capture.log'}(中間フォルダは残してあります)")
    print(f"      再生の開始: 録画の {t0:.3f} 秒({counts.index(max(counts))} フレーム目付近に合図)")
    out.parent.mkdir(parents=True, exist_ok=True)
    mux = run(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{t0:.3f}", "-i", str(raw), "-i", str(mp3), "-t", f"{seconds:.3f}",
               "-vf", f"crop={cw}:{ch}:{x}:{vy}", "-r", str(fps), "-map", "0:v:0", "-map", "1:a:0", "-c:v", "libx264", "-preset", "medium", "-crf", "18",
               "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(out)])
    if mux.returncode != 0:
        sys.exit(f"[エラー] mp4 の作成に失敗: {mux.stderr[-400:]}")
    if keep_raw:
        shutil.copy(raw, out.with_suffix(".raw.mkv"))
    shutil.rmtree(raw.parent, ignore_errors=True)
    print(f"できました: {out}(映像 {cw}x{ch}、{seconds:.1f} 秒、音は {mp3.name})")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("project", nargs="?")
    ap.add_argument("--start-bar", type=int, default=0, help="開始小節(0 始まり)")
    ap.add_argument("--bars", type=int, help="小節数(省略 = 最後まで)")
    ap.add_argument("--size", default="screen", help="ウィンドウの大きさ(pt)。screen = 画面いっぱい(既定)、または 1280x720")
    ap.add_argument("--fps", type=int, default=30)
    ap.add_argument("--display", type=int, default=1, help="ffmpeg の画面番号(`ffmpeg -f avfoundation -list_devices true -i ''` の Capture screen)")
    ap.add_argument("--out")
    ap.add_argument("--resume", help="前回の中間フォルダ(raw.mkv と meta.json)から、後処理だけやり直す")
    ap.add_argument("--keep-raw", action="store_true", help="切り出す前の画面録画も残す")
    ap.add_argument("--dry-run", action="store_true", help="音を鳴らさず、計画と前提だけ確認する")
    a = ap.parse_args()

    if a.resume:   # 画面録画までは済んでいて、後処理(音と映像のそろえ)だけやり直す。音は鳴らない
        return finish(Path(a.resume), a.keep_raw)
    name = a.project or newest_project()
    pj = WORK / "daw" / f"{name}.json"
    if not pj.is_file():
        sys.exit(f"[エラー] プロジェクトがありません: {pj}")
    proj = daw_codegen.validate(json.loads(pj.read_text(encoding="utf-8")))
    cells_bar = proj["res"] * proj["meter"]
    bars = a.bars or proj["bars"] - a.start_bar
    if a.start_bar < 0 or bars < 1 or a.start_bar + bars > proj["bars"]:
        sys.exit(f"[エラー] 範囲が曲の外です(曲は {proj['bars']} 小節)")
    seconds = bars * proj["meter"] * 60 / proj["bpm"]
    out_dir = WORK / "videos"
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = f"{name}_{a.start_bar + 1}-{a.start_bar + bars}"
    out = Path(a.out) if a.out else out_dir / f"{stem}.mp4"
    if a.size == "screen":
        w, h = screen_size_pt()
    else:
        w, h = (int(x) for x in a.size.lower().split("x"))

    print(f"区間: {a.start_bar + 1}〜{a.start_bar + bars} 小節目({seconds:.1f} 秒)/ ウィンドウ {w}x{h} / {a.fps}fps → {out}")
    problems = []
    if not server_up():
        problems.append("DAW サーバーが動いていません(uv run scripts/daw_server.py)")
    for tool in ("ffmpeg", "ffprobe"):
        if not shutil.which(tool):
            problems.append(f"{tool} がありません")
    if not Path(f"/Applications/{CHROME}.app").exists():
        problems.append(f"{CHROME} がありません")
    if problems:
        print("[エラー] " + " / ".join(problems), file=sys.stderr)
        return 2
    if a.dry_run:
        print("前提 OK(--dry-run のため、音も録画もしていません)")
        return 0

    # --- 1. 音(区間のコードを録音して mp3 に) ---
    seg_rb = WORK / "daw" / f"_rec_{stem}.rb"
    seg = daw_codegen.slice_project(proj, a.start_bar * cells_bar, (a.start_bar + bars) * cells_bar)
    seg_rb.write_text(daw_codegen.generate(seg), encoding="utf-8")
    print(f"[1/3] 音を録音します(スピーカーから約 {seconds + 12:.0f} 秒、音が鳴ります)…", flush=True)
    # 曲が重いと先行時間 0 では間に合わない。DAW の ▶ と同じ先行 0.5 秒で録り、頭の 0.5 秒(無音)を切る
    r = subprocess.run([sys.executable, str(ROOT / "scripts" / "live_render.py"), f"daw/{seg_rb.name}", "--seconds", f"{seconds + 1.5:.1f}", "--name", f"rec_{stem}"],
                       text=True, capture_output=True, cwd=ROOT, env={**os.environ, "SONIC_PI_SCHED_AHEAD": str(SCHED_AHEAD)})
    sys.stdout.write(r.stdout[-400:])
    m = re.search(r"できました: (\S+\.wav)", r.stdout)
    if r.returncode not in (0, 1) or not m:
        print(r.stderr[-600:], file=sys.stderr)
        sys.exit("[エラー] 録音に失敗しました")
    wav = ROOT / m.group(1)
    mp3 = out.with_suffix(".mp3")
    cv = run(["ffmpeg", "-y", "-loglevel", "error", "-ss", str(SCHED_AHEAD), "-i", str(wav), "-t", f"{seconds:.3f}", "-codec:a", "libmp3lame", "-b:a", "256k", str(mp3)])
    if cv.returncode != 0:
        sys.exit(f"[エラー] mp3 への変換に失敗: {cv.stderr[-300:]}")
    print(f"      音: {mp3}")

    # --- 2. 映像(Chrome で DAW を開いて自動再生 + 画面録画) ---
    print("[2/3] 画面を録画します(Chrome の専用ウィンドウが開き、もう一度音が鳴ります)…", flush=True)
    raw = Path(tempfile.mkdtemp(prefix="rec_")) / "raw.mkv"
    profile = tempfile.mkdtemp(prefix="chrome_rec_")
    url = f"{SERVER}/?rec=1&project={name}&bar={a.start_bar}&bars={bars}"
    cap_log = raw.parent / "capture.log"
    awake = subprocess.Popen(["caffeinate", "-dimu", "-t", str(int(seconds + 180))])   # 録画中に画面が暗くなって、画面録画が止まるのを防ぐ
    cap = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "avfoundation", "-framerate", str(a.fps), "-pixel_format", "uyvy422",
                            "-capture_cursor", "0", "-i", f"{a.display}:none", "-c:v", "libx264", "-preset", "ultrafast", "-crf", "16", "-pix_fmt", "yuv420p", str(raw)],
                           stdin=subprocess.PIPE, stderr=cap_log.open("w"), text=True)
    time.sleep(1.5)
    if cap.poll() is not None:
        awake.terminate()
        sys.exit(f"[エラー] 画面録画を始められません: {cap_log.read_text()[-400:]}\n画面収録の許可(ターミナル)を確認してください")
    subprocess.Popen(["open", "-na", CHROME, "--args", f"--user-data-dir={profile}", f"--app={url}", f"--window-size={w},{h}", "--window-position=0,0",
                      "--no-first-run", "--no-default-browser-check"])
    status, bounds = "", None
    try:
        deadline = time.time() + seconds + 90
        while time.time() < deadline:
            time.sleep(0.5)
            try:
                status = osa(f'tell application "{CHROME}" to get title of active tab of front window')
                if bounds is None:
                    bounds = numbers(osa(f'tell application "{CHROME}" to get bounds of front window'))
            except RuntimeError:
                continue
            if status == "REC_END":
                break
        else:
            raise TimeoutError("再生が終わりませんでした")
        time.sleep(1.0)
    finally:
        try:
            cap.stdin.write("q")
            cap.stdin.flush()
        except (BrokenPipeError, ValueError):
            pass
        cap.wait(timeout=30)
        awake.terminate()
        run(["pkill", "-f", "--", f"--user-data-dir={profile}"])   # "--" がないと、-- で始まる模様が pkill のオプションに読まれて、ウィンドウが閉じない
        shutil.rmtree(profile, ignore_errors=True)
    if bounds is None or len(bounds) != 4:
        sys.exit("[エラー] ウィンドウの位置が取れませんでした")
    (raw.parent / "meta.json").write_text(json.dumps({"bounds": bounds, "mp3": str(mp3), "seconds": seconds, "out": str(out), "fps": a.fps}), encoding="utf-8")

    rc = finish(raw.parent, a.keep_raw)
    seg_rb.unlink(missing_ok=True)
    return rc


if __name__ == "__main__":
    sys.exit(main())
