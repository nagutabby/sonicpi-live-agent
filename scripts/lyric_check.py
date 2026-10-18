#!/usr/bin/env python3
"""歌詞つきフレーズ JSON(neutrino_sing.py の入力)を検査する。

  lyric_check.py <phrase.json> [<phrase2.json> …]

誤り(終了コード 2): NEUTRINO に渡すと失敗する、または歌詞が崩れるもの。
  - 1 音符に 2 モーラ以上(NEUTRINO は 1 音符 = 1 かな。「きょ」のような拗音は 1 モーラ)
  - かな以外の文字 / 使えない長さ / 小節をまたぐ音符 / 合計が 4 拍の倍数でない / tie の音名違い
警告(終了コード 1): 歌い方が平坦・不自然になりやすいもの。
  - 「は」「へ」「を」(助詞なら わ・え・お と発音どおりに書く)
  - フレーズ中の細かい休符(0.5 拍以下)/ ブレスも休符もなく長く続くフレーズ(既定 16 拍超)
  - 16 分音符(0.25 拍)の連続が長い(4 つ超)
参考(終了コードには影響しない): 長い音符(2 拍以上)の母音。
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from neutrino_sing import TYPES, parse_pitch, split_note

MAX_PHRASE_BEATS = 16.0
SMALL = "ゃゅょぁぃぅぇぉゎャュョァィゥェォヮ"
MORA = re.compile(rf"^(?:[ぁ-ゖァ-ヺ](?![{SMALL}])|[ぁ-ゖァ-ヺ][{SMALL}]|っ|ッ|ん|ン|ー)'?$")
PARTICLES = {"は": "わ", "へ": "え", "を": "お"}
VOWEL_ROWS = {"あ": "あかさたなはまやらわがざだばぱ", "い": "いきしちにひみりぎじびぴ", "う": "うくすつぬふむゆるぐずぶぷ",
              "え": "えけせてねへめれげぜでべぺ", "お": "おこそとのほもよろをごぞどぼぽ"}


def vowel_of(ch: str) -> str:
    for v, row in VOWEL_ROWS.items():
        if ch in row:
            return v
    return ""


def check(spec: dict) -> tuple[list[str], list[str], list[str]]:
    errors: list[str] = []
    warns: list[str] = []
    infos: list[str] = []
    if not isinstance(spec.get("bpm"), (int, float)) or not spec["bpm"] > 0:
        errors.append("bpm が数値ではありません")
    filled, bar, tie_next = 0.0, 1, ""
    phrase_start, phrase_beats, pos = None, 0.0, 0.0
    small_run = 0
    notes = spec.get("notes", [])
    for i, raw in enumerate(notes):
        where = f"{i + 1}番目(小節{bar})"
        try:
            lyric, pitch, beats, flags = split_note(raw)
        except (ValueError, IndexError, TypeError) as e:
            errors.append(f"{where}: {e}")
            continue
        if beats not in TYPES:
            errors.append(f"{where}: 対応していない長さ {beats} 拍(使える値: {sorted(TYPES)})")
        if filled + beats > 4.0 + 1e-9:
            errors.append(f"{where}: 小節をまたぎます({filled:g}+{beats:g} 拍)。tie で繋ぐ")
        if pitch:
            try:
                parse_pitch(pitch)
            except ValueError as e:
                errors.append(f"{where}: {e}")
            if tie_next and pitch != tie_next:
                errors.append(f"{where}: tie の次は同じ音名にする({tie_next} → {pitch})")
            if lyric and not tie_next:
                if not MORA.match(lyric):
                    errors.append(f"{where}: 歌詞 {lyric!r} は 1 音符 1 モーラ(かな 1 字、拗音は 1 モーラ、っ・ん・ー)にする")
                if lyric in PARTICLES:
                    warns.append(f"{where}: 「{lyric}」は助詞なら「{PARTICLES[lyric]}」と発音どおりに書く")
                if beats >= 2 and (v := vowel_of(lyric[0])):
                    infos.append(f"{where}: 長い音符({beats:g} 拍)の母音は「{v}」。伸ばした先が聴きやすいかを聴いて確かめる")
            elif not lyric and not tie_next:
                errors.append(f"{where}: 音符に歌詞がありません(休符にするなら音名を空に)")
            if lyric == "ー" and i == 0:
                errors.append(f"{where}: 先頭に「ー」は置けません(伸ばす母音がない)")
        tie_next = pitch if "tie" in flags and pitch else ""
        # フレーズ(ブレスか休符で囲まれた区間)の長さ
        if pitch:
            if phrase_start is None:
                phrase_start, phrase_beats = pos, 0.0
            phrase_beats += beats
            small_run = small_run + 1 if beats == 0.25 else 0
            if small_run == 5:
                warns.append(f"{where}: 16 分音符が 5 つ以上続きます(歌詞が詰まって聞こえやすい)")
        else:
            if phrase_start is not None and 0 < beats <= 0.5 and i + 1 < len(notes) and notes[i + 1][1]:
                warns.append(f"{where}: フレーズ中の細かい休符({beats:g} 拍)。NEUTRINO は情報が減って平坦になりやすい(休符を音符に繋ぐ)")
            small_run = 0
        if (not pitch and beats >= 1) or "br" in flags or i == len(notes) - 1:
            if phrase_start is not None and phrase_beats > MAX_PHRASE_BEATS:
                warns.append(f"{where}: ブレスも休符もなく {phrase_beats:g} 拍続くフレーズ(息継ぎの位置に br か休符を)")
            if not pitch and beats >= 1 or "br" in flags:
                phrase_start = None
        pos += beats
        filled += beats
        if abs(filled - 4.0) < 1e-9:
            filled, bar = 0.0, bar + 1
    if filled > 1e-9:
        errors.append(f"最後の小節が 4 拍になっていません(あと {4.0 - filled:g} 拍)")
    if tie_next:
        errors.append("最後の音符に tie が付いています(次の音符がない)")
    return errors, warns, infos


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("phrases", nargs="+", type=Path)
    args = ap.parse_args()
    worst = 0
    for path in args.phrases:
        try:
            spec = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as e:
            print(f"{path}: 読めません({e})")
            worst = 2
            continue
        errors, warns, infos = check(spec)
        print(f"{path}: 誤り {len(errors)} / 警告 {len(warns)}")
        for lvl, msgs in (("誤り", errors), ("警告", warns), ("参考", infos)):
            for m in msgs:
                print(f"  [{lvl}] {m}")
        worst = max(worst, 2 if errors else 1 if warns else 0)
    return worst


if __name__ == "__main__":
    sys.exit(main())
