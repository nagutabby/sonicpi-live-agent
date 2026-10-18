#!/usr/bin/env python3
"""NEUTRINO の f0(float32 / 10ms 刻み)を、音階の上で N 音ずらしてハモリ用の f0 を作る。

  vocal_harmony.py <in.f0> --key "Bb minor" --steps 2 [--out out.f0]

--steps 2 は音階の 2 つ上(= 3 度上)、-2 は 2 つ下(3 度下)。音階の外の音は、いちばん近い音階音を基準に同じ半音数だけずらす。
声(wav)はそのまま、ボコーダーのキャリアの音高(f0)だけを動かすので、母音は変わらない。ずらした f0 を vocode.py に渡す。
"""

from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path

import numpy as np

SCALES = {"major": (0, 2, 4, 5, 7, 9, 11), "minor": (0, 2, 3, 5, 7, 8, 10)}
ROOTS = {"c": 0, "db": 1, "c#": 1, "d": 2, "eb": 3, "d#": 3, "e": 4, "f": 5, "gb": 6, "f#": 6, "g": 7,
         "ab": 8, "g#": 8, "a": 9, "bb": 10, "a#": 10, "b": 11}


def scale_pcs(key: str) -> list[int]:
    root, _, mode = key.lower().partition(" ")
    if root not in ROOTS or (mode or "major") not in SCALES:
        raise ValueError(f"キーが読めません: {key!r}(例: 'Bb minor')")
    return sorted((ROOTS[root] + d) % 12 for d in SCALES[mode or "major"])


def shift_semitones(midi: int, pcs: list[int], steps: int) -> int:
    """音階上で steps 音ずらすときの半音数。音階の外の音は、いちばん近い音階音を基準にする。"""
    notes = sorted({o * 12 + pc for o in range(-1, 11) for pc in pcs})
    base = min(notes, key=lambda n: (abs(n - midi), n))
    i = notes.index(base)
    return notes[max(0, min(len(notes) - 1, i + steps))] - base


def harmonize(f0: np.ndarray, pcs: list[int], steps: int) -> np.ndarray:
    out = f0.astype(np.float64).copy()
    for i, f in enumerate(f0):
        if f <= 0:
            continue
        midi = 69 + 12 * math.log2(f / 440)
        out[i] = f * 2 ** (shift_semitones(round(midi), pcs, steps) / 12)
    return out.astype(np.float32)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("f0")
    ap.add_argument("--key", required=True)
    ap.add_argument("--steps", type=int, required=True)
    ap.add_argument("--out")
    a = ap.parse_args()
    src = Path(a.f0)
    out = Path(a.out) if a.out else src.with_name(f"{src.stem}_h{a.steps:+d}{src.suffix}")
    if out.exists():
        print(f"既存のファイルは上書きしません: {out}", file=sys.stderr)
        return 2
    try:
        pcs = scale_pcs(a.key)
    except ValueError as e:
        print(e, file=sys.stderr)
        return 2
    harmonize(np.fromfile(src, dtype="<f4"), pcs, a.steps).astype("<f4").tofile(out)
    print(f"出力: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
