#!/usr/bin/env python3
"""フレーズ仕様(JSON)から MusicXML を作り、NEUTRINO で歌声(wav + f0)を合成する。

  neutrino_sing.py <phrase.json> [--model MERROW] [--support SOMA] [--style-shift 0] [--transpose 0] [--dry-run]
  neutrino_sing.py <phrase.json> --clip-from <wav>     (合成済みの wav を、頭の無音を捨てて拍数で切り出すだけ)

phrase.json の例(拍子は 4/4 固定。音符は小節をまたがない):
  {"bpm": 130, "notes": [["お", "C5", 1.5], ["な", "Bb4", 0.5, "br"], ["", "", 1.0], ["あ", "G4", 2, "tie"], ["", "G4", 2]]}
  各要素は [歌詞(かな1音), 音名, 長さ(拍), 印(省略可)]。音名が空なら休符。
  印: "br" = この音符のあとにブレス記号(NEUTRINO はブレスか休符で囲まれた区間を 1 フレーズとして生成する)。
      "tie" = 次の音符とタイで繋ぐ(次は同じ音名で、歌詞は空でよい)。小節をまたぐ長い音に使う。
  歌詞の記号: っ(促音)/ ー(直前の母音を伸ばす)/ '(母音脱落。「す'」は子音のみ)。発音どおりに書く(は→わ、へ→え、を→お)。

出力は work/vocals/<phrase名>_vN.{musicxml,wav,f0,...}(既存は上書きせず版を進める)。
同時に、頭の 1 小節の無音を捨てて譜面の拍数で切った <名>_vN_clip.wav も作る(Sonic Pi の `sample` を小節線に揃える用)。
~/neutrino(環境変数 NEUTRINO_DIR)は読み取り専用のまま使い、書き込みはしない。
"""

import argparse
import json
import os
import re
import subprocess
import sys
import wave
from pathlib import Path
from xml.sax.saxutils import escape

import numpy as np
from common import WORK, load_dotenv

VOCALS = WORK / "vocals"
DIVISIONS = 4  # 四分音符 = 4 → 16 分音符まで表せる
TYPES = {  # 拍数 -> (type, ドット)
    4.0: ("whole", 0), 3.0: ("half", 1), 2.0: ("half", 0), 1.5: ("quarter", 1),
    1.0: ("quarter", 0), 0.75: ("eighth", 1), 0.5: ("eighth", 0), 0.25: ("16th", 0),
}
STEPS = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}
LEAD_BEATS = 4.0  # NEUTRINO は譜面の前に 1 小節の無音を足す
FLAGS = {"br", "tie"}


def parse_pitch(name: str) -> tuple[str, int, int]:
    m = re.fullmatch(r"([A-G])([#b]?)(\d)", name)
    if not m:
        raise ValueError(f"音名が読めません: {name!r}(例: C5, Bb4, F#3)")
    return m.group(1), {"": 0, "#": 1, "b": -1}[m.group(2)], int(m.group(3))


def split_note(n: list) -> tuple[str, str, float, set[str]]:
    """[歌詞, 音名, 拍, 印(省略可)] → (歌詞, 音名, 拍, 印の集合)。印は "br" / "tie"(文字列または配列)。"""
    flags = n[3] if len(n) > 3 else []
    flags = {flags} if isinstance(flags, str) else set(flags)
    if flags - FLAGS:
        raise ValueError(f"対応していない印: {sorted(flags - FLAGS)}(使える印: {sorted(FLAGS)})")
    return n[0], n[1], float(n[2]), flags


def note_xml(lyric: str, pitch: str, beats: float, flags: frozenset[str] | set[str] = frozenset(),
             tie_stop: bool = False) -> str:
    if beats not in TYPES:
        raise ValueError(f"対応していない長さ: {beats} 拍(使える値: {sorted(TYPES)})")
    typ, dots = TYPES[beats]
    dur = int(beats * DIVISIONS)
    tie_tags = ("<tie type=\"stop\"/>" if tie_stop else "") + ("<tie type=\"start\"/>" if "tie" in flags else "")
    tail = f"<duration>{dur}</duration>{tie_tags}<voice>1</voice><type>{typ}</type>" + "<dot/>" * dots
    if not pitch:
        return f"<note><rest/>{tail}</note>"
    step, alter, octave = parse_pitch(pitch)
    alt = f"<alter>{alter}</alter>" if alter else ""
    ly = ("" if tie_stop else
          f"<lyric number=\"1\"><syllabic>single</syllabic><text>{escape(lyric)}</text></lyric>")
    marks = ("<tied type=\"stop\"/>" if tie_stop else "") + ("<tied type=\"start\"/>" if "tie" in flags else "")
    if "br" in flags:
        marks += "<articulations><breath-mark/></articulations>"
    notations = f"<notations>{marks}</notations>" if marks else ""
    return f"<note><pitch><step>{step}</step>{alt}<octave>{octave}</octave></pitch>{tail}{notations}{ly}</note>"


def build_musicxml(spec: dict, title: str) -> str:
    bpm = spec["bpm"]
    measures: list[list[str]] = [[]]
    filled = 0.0
    tie_next = ""  # タイで繋がる直前の音名(次の音符は同じ音名)
    for raw in spec["notes"]:
        lyric, pitch, beats, flags = split_note(raw)
        if filled + beats > 4.0 + 1e-9:
            raise ValueError(f"音符が小節をまたぎます(小節{len(measures)}、{filled}+{beats} 拍)。長い音は tie で繋ぐ")
        if tie_next and pitch != tie_next:
            raise ValueError(f"tie の次の音符は同じ音名にする(小節{len(measures)}: {tie_next} → {pitch or '休符'})")
        measures[-1].append(note_xml(lyric, pitch, beats, flags, tie_stop=bool(tie_next)))
        tie_next = pitch if "tie" in flags else ""
        filled += beats
        if abs(filled - 4.0) < 1e-9:
            measures.append([])
            filled = 0.0
    if filled:
        raise ValueError(f"最後の小節が 4 拍になっていません(あと {4.0 - filled} 拍)")
    measures = [m for m in measures if m]
    body = []
    for i, notes in enumerate(measures, 1):
        attrs = ""
        if i == 1:
            attrs = (
                f"<attributes><divisions>{DIVISIONS}</divisions><key><fifths>0</fifths></key>"
                "<time><beats>4</beats><beat-type>4</beat-type></time>"
                "<clef><sign>G</sign><line>2</line></clef></attributes>"
                f"<direction placement=\"above\"><direction-type><metronome>"
                f"<beat-unit>quarter</beat-unit><per-minute>{bpm}</per-minute></metronome>"
                f"</direction-type><sound tempo=\"{bpm}\"/></direction>"
            )
        body.append(f"<measure number=\"{i}\">{attrs}{''.join(notes)}</measure>")
    return (
        "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
        "<!DOCTYPE score-partwise PUBLIC \"-//Recordare//DTD MusicXML 3.1 Partwise//EN\" "
        "\"http://www.musicxml.org/dtds/partwise.dtd\">\n"
        "<score-partwise version=\"3.1\"><part-list><score-part id=\"P1\">"
        f"<part-name>{escape(title)}</part-name></score-part></part-list>"
        f"<part id=\"P1\">{''.join(body)}</part></score-partwise>\n"
    )


def next_version(stem: str) -> int:
    used = [int(m.group(1)) for p in VOCALS.glob(f"{stem}_v*.musicxml")
            if (m := re.fullmatch(rf"{re.escape(stem)}_v(\d+)\.musicxml", p.name))]
    return max(used, default=0) + 1


def phrase_beats(spec: dict) -> float:
    return sum(float(n[2]) for n in spec["notes"])


def clip_wav(wav: Path, bpm: float, beats: float, lead_beats: float = LEAD_BEATS) -> Path:
    """頭の無音(lead_beats)を捨て、beats 拍ぶんだけ切り出す。末尾に 20ms のフェードをかけて <名>_clip.wav に書く。"""
    with wave.open(str(wav), "rb") as w:
        sr, ch, sw = w.getframerate(), w.getnchannels(), w.getsampwidth()
        if sw != 2:
            raise ValueError(f"16bit の wav だけ対応しています: {wav}")
        x = np.frombuffer(w.readframes(w.getnframes()), dtype="<i2").reshape(-1, ch).astype(np.float64)
    spb = 60.0 / bpm
    start, n = round(lead_beats * spb * sr), round(beats * spb * sr)
    y = x[start:start + n].copy()
    if len(y) < n:
        y = np.vstack([y, np.zeros((n - len(y), ch))])  # 足りない分は無音で埋めて、拍数を保つ
    fade = min(len(y), round(0.02 * sr))
    y[len(y) - fade:] *= np.linspace(1, 0, fade)[:, None]
    out = wav.with_name(wav.stem + "_clip.wav")
    with wave.open(str(out), "wb") as w:
        w.setnchannels(ch)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes(np.clip(y, -32768, 32767).astype("<i2").tobytes())
    return out


def neutrino_options(neutrino: Path, style_shift: int, transpose: int, support: str | None) -> list[str]:
    """neutrino 本体に渡す -k(スタイルシフト)/ -f(トランスポーズ)/ -S(サポートモデル)。"""
    opts = ["-k", str(style_shift), "-f", str(transpose)]
    if support:
        sm = neutrino / "model" / support
        if not sm.exists():
            sys.exit(f"サポートモデルが見つかりません: {sm}")
        opts += ["-S", f"{sm}/"]
    return opts


def add_neutrino_args(ap: argparse.ArgumentParser) -> None:
    ap.add_argument("--model", default="MERROW", help="声のモデル(MERROW/NAKUMO/REINA/RUNO/SOMA)")
    ap.add_argument("--support", help="サポートモデル(主モデルの声質のまま、別モデルの歌い方を混ぜる)")
    ap.add_argument("--style-shift", type=int, default=0, help="スタイルシフト -5〜5(2 なら 2 つ上のキーの歌い方)")
    ap.add_argument("--transpose", type=int, default=0, help="トランスポーズ(半音)")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("phrase", type=Path)
    add_neutrino_args(ap)
    ap.add_argument("--clip-from", type=Path, help="合成済みの wav を切り出すだけ(NEUTRINO は動かさない)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    load_dotenv()

    spec = json.loads(args.phrase.read_text(encoding="utf-8"))
    if args.clip_from:
        out = clip_wav(args.clip_from, spec["bpm"], phrase_beats(spec))
        print(f"出力: {out}({phrase_beats(spec):g} 拍 @ {spec['bpm']} BPM)")
        return 0

    neutrino = Path(os.environ.get("NEUTRINO_DIR", "~/neutrino")).expanduser()
    mxl2lab, nbin = neutrino / "bin/musicXMLtoLabel", neutrino / "bin/neutrino"
    model = neutrino / "model" / args.model
    for p in (mxl2lab, nbin, model):
        if not p.exists():
            sys.exit(f"見つかりません: {p}(NEUTRINO_DIR を確認)")

    VOCALS.mkdir(parents=True, exist_ok=True)
    stem = args.phrase.stem
    base = VOCALS / f"{stem}_v{next_version(stem)}"
    xml_path = base.with_suffix(".musicxml")
    xml_path.write_text(build_musicxml(spec, stem), encoding="utf-8")
    paths = {k: base.with_suffix(f".{k}") for k in
             ("full.lab", "mono.lab", "timing.lab", "f0", "melspec", "wav")}
    cmds = [
        [str(mxl2lab), str(xml_path), str(paths["full.lab"]), str(paths["mono.lab"])],
        [str(nbin), str(paths["full.lab"]), str(paths["timing.lab"]), str(paths["f0"]),
         str(paths["melspec"]), str(paths["wav"]), f"{model}/",
         "-n", "4", *neutrino_options(neutrino, args.style_shift, args.transpose, args.support),
         "-s", "48000", "-b", "16", "-t"],
    ]
    env = {**os.environ, "DYLD_LIBRARY_PATH": f"{neutrino / 'bin'}:{os.environ.get('DYLD_LIBRARY_PATH', '')}"}
    for cmd in cmds:
        print("+", " ".join(cmd))
        if not args.dry_run:
            r = subprocess.run(cmd, env=env, cwd=neutrino)  # settings/ を相対で読むため
            if r.returncode != 0:
                sys.exit(f"失敗しました(終了コード {r.returncode}): {Path(cmd[0]).name}")
    if args.dry_run:
        print("(dry-run)")
        return 0
    clip = clip_wav(paths["wav"], spec["bpm"], phrase_beats(spec))
    print(f"出力: {paths['wav']}\n切り出し(Sonic Pi 用): {clip}({phrase_beats(spec):g} 拍)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
