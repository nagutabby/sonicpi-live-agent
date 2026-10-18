#!/usr/bin/env python3
"""フレーズ仕様(JSON)の歌詞を、歌と同じタイミングで読み上げた wav を作る(歌声との比較用)。

  speak_phrase.py <phrase.json> [--voice Kyoko] [--lead-beats 4]

macOS の `say` で音節ごとに読み上げ、音符の頭に置く。長さは音符の長さで切る(伸ばさない)。
NEUTRINO の出力は譜面の前に 1 小節の無音を持つので、--lead-beats(既定 4)で同じ位置に揃える。
出力は work/vocals/<phrase名>_speak_vN.wav(48kHz/16bit/モノラル。既存は上書きしない)。
"""

import argparse
import json
import re
import subprocess
import sys
import tempfile
import wave
from pathlib import Path

import numpy as np
from common import WORK

SR = 48000
VOCALS = WORK / "vocals"


def say_syllable(text: str, voice: str, tmp: Path, rate: int = 0) -> np.ndarray:
    aiff, wav = tmp / "s.aiff", tmp / "s.wav"
    rate_opt = ["-r", str(rate)] if rate else []
    subprocess.run(["say", "-v", voice, *rate_opt, "-o", str(aiff), text], check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(aiff), "-ar", str(SR),
                    "-ac", "1", "-sample_fmt", "s16", str(wav)], check=True)
    with wave.open(str(wav)) as w:
        x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768
    loud = np.flatnonzero(np.abs(x) > 0.02 * max(np.abs(x).max(), 1e-6))
    return x[loud[0]:] if loud.size else x  # 頭の無音を捨てて、音符の頭に揃える


def next_version(stem: str) -> int:
    used = [int(m.group(1)) for p in VOCALS.glob(f"{stem}_speak_v*.wav")
            if (m := re.fullmatch(rf"{re.escape(stem)}_speak_v(\d+)\.wav", p.name))]
    return max(used, default=0) + 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("phrase", type=Path)
    ap.add_argument("--voice", default="Kyoko")
    ap.add_argument("--lead-beats", type=float, default=4.0)
    ap.add_argument("--by-bar", action="store_true",
                    help="1 小節ぶんの歌詞をまとめて普通に読み、その小節の長さに速さを合わせる")
    args = ap.parse_args()

    spec = json.loads(args.phrase.read_text(encoding="utf-8"))
    beat = 60.0 / spec["bpm"]
    total = sum(n[2] for n in spec["notes"]) + args.lead_beats + 4
    out = np.zeros(int(total * beat * SR), dtype=np.float32)
    with tempfile.TemporaryDirectory() as t:
        tmp, cache, pos = Path(t), {}, args.lead_beats
        if args.by_bar:
            bar, filled = [], 0.0  # [(開始拍, 歌詞, 拍数)]
            for lyric, pitch, beats in spec["notes"]:
                if lyric and pitch:
                    bar.append((pos + filled, lyric, beats))
                filled += beats
                if abs(filled - 4.0) < 1e-9:
                    if bar:
                        start = bar[0][0]
                        span = int((bar[-1][0] + bar[-1][2] - start) * beat * SR)
                        text, rate = "".join(b[1] for b in bar), 175
                        for _ in range(3):  # 長さが合うように読む速さを寄せる
                            x = say_syllable(text, args.voice, tmp, rate)
                            rate = int(min(400, max(80, rate * len(x) / span)))
                        x = x[:span].copy()
                        fade = min(len(x), int(0.02 * SR))
                        x[len(x) - fade:] *= np.linspace(1, 0, fade, dtype=np.float32)
                        i = int(start * beat * SR)
                        out[i:i + len(x)] += x
                    pos += 4.0
                    bar, filled = [], 0.0
            notes = []
        else:
            notes = spec["notes"]
        for lyric, pitch, beats in notes:
            if lyric and pitch:
                if lyric not in cache:
                    cache[lyric] = say_syllable(lyric, args.voice, tmp)
                x = cache[lyric][: int(beats * beat * SR)].copy()
                fade = min(len(x), int(0.02 * SR))
                x[len(x) - fade:] *= np.linspace(1, 0, fade, dtype=np.float32)
                i = int(pos * beat * SR)
                out[i:i + len(x)] += x
            pos += beats

    peak = np.abs(out).max()
    if peak > 0:
        out *= 0.79 / peak  # -2dBFS
    stem = args.phrase.stem
    path = VOCALS / f"{stem}_speak_v{next_version(stem)}.wav"
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((out * 32767).astype(np.int16).tobytes())
    print(f"出力: {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
