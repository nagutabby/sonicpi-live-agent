"""DAW 風 GUI のプロジェクト(JSON)を、Sonic Pi のコードに変換する。標準ライブラリのみ。

プロジェクトは work/daw/<名前>.json。トラックの種類:
  drum   サンプルをグリッドで鳴らす(kick・snare・hat など)
  bass / chord / melody  シンセ。ピアノロールの音([拍の位置, 音名, 長さ(拍)])を鳴らす(役割の違いは音色・音域だけ)
  (古い形式の bass / chord = グリッド + コード進行 は、読み込むとき音程つきの音に直す)
  fx     エフェクト。ほかのトラック(targets。空なら全トラック)の live_loop を with_fx で包む。
         sidechain だけは、グリッド(steps)の X の位置で、対象の音量を一瞬下げて戻す(キックに合わせて息をする)
コード進行は、ピアノロールにコードトーンを見せるガイド。音そのものは持たない。
GUI から来る値はすべて検証して(名前・音名・コード種類・数値の範囲)、検証を通ったものだけをコードに書く。
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from common import ROOT

CHORD_TYPES = {  # 名前 -> 音程(半音)。GUI の試聴とコード選びに使う。名前は Sonic Pi の chord の名前
    "major": [0, 4, 7], "minor": [0, 3, 7], "major7": [0, 4, 7, 11], "minor7": [0, 3, 7, 10],
    "dom7": [0, 4, 7, 10], "sus2": [0, 2, 7], "sus4": [0, 5, 7], "diminished": [0, 3, 6],
    "m9": [0, 3, 7, 10, 14], "major9": [0, 4, 7, 11, 14], "add9": [0, 4, 7, 14],
}
KINDS = ("drum", "bass", "chord", "melody", "fx")
# エフェクト: 名前 -> (ラベル, 説明, mix の既定値, {パラメータ: (ラベル, 最小, 最大, 既定)})。Sonic Pi の with_fx の名前と引数に対応
FX_INFO = {
    "reverb": ("リバーブ", "残響で奥行きと広がりを足す", 0.4, {"room": ("部屋の広さ", 0, 1, 0.6), "damp": ("高域の吸収", 0, 1, 0.5)}),
    "echo": ("エコー", "やまびこのように音を繰り返す", 0.4, {"phase": ("間隔(拍)", 0.125, 2, 0.375), "decay": ("消えるまで(拍)", 0.5, 8, 2)}),
    "distortion": ("ディストーション", "音を歪ませて太く、荒くする", 0.5, {"distort": ("歪み量", 0, 0.99, 0.5)}),
    "lpf": ("ローパス", "高域を削って、こもった音にする", 1, {"cutoff": ("カットオフ", 30, 130, 80)}),
    "hpf": ("ハイパス", "低域を削って、薄く軽い音にする", 1, {"cutoff": ("カットオフ", 30, 130, 50)}),
    "flanger": ("フランジャー", "ジェット機のようなうねりを足す", 0.5, {"depth": ("深さ", 0, 15, 5), "decay": ("余韻(拍)", 0, 8, 2)}),
    "tremolo": ("トレモロ", "音量を細かく揺らす", 1, {"phase": ("周期(拍)", 0.125, 2, 0.5), "depth": ("深さ", 0, 1, 0.5)}),
    "slicer": ("スライサー", "音を刻んで断続的に切る", 1, {"phase": ("周期(拍)", 0.125, 1, 0.25), "pulse_width": ("音が鳴る割合", 0.1, 0.9, 0.5)}),
    "wobble": ("ワブル", "フィルターを往復させて、うねらせる", 1, {"phase": ("周期(拍)", 0.25, 4, 1), "cutoff_min": ("最小カットオフ", 30, 100, 60), "cutoff_max": ("最大カットオフ", 60, 130, 110)}),
    "bitcrusher": ("ビットクラッシャー", "解像度を落として、ざらざらしたデジタル音にする", 0.6, {"bits": ("ビット数", 4, 16, 8), "sample_rate": ("サンプルレート", 1000, 44100, 8000)}),
    "vowel": ("フォルマント(母音)", "声の母音の響き(フォルマント)を作り、声らしくする", 1, {"vowel_sound": ("母音(1あ 2え 3い 4お 5う)", 1, 5, 4), "voice": ("声の種類(0〜4 高い→低い)", 0, 4, 4)}),
    "sidechain": ("サイドチェイン", "グリッドの X の位置で対象の音量を下げ、すぐ戻す。キックに合わせて他の音が息をする", 1, {"depth": ("下げる深さ", 0, 1, 0.8), "release": ("戻る時間(拍)", 0.05, 1.5, 0.4)}),
}
MAX_NOTES = 4096   # 1 トラックの音の最大数(超えた分は末尾から捨てられる)
MAX_TRACKS = 40   # トラックの最大数(超えた分は末尾から捨てられる)
MAX_BARS = 128   # 曲の最大小節数
INT_PARAMS = {"bits", "sample_rate", "vowel_sound", "voice"}
ENVS = ("pluck", "stab", "pad", "swell")
PITCH = re.compile(r"^([a-g])([sb]?)(-?\d)$")
ROOTS = ("c", "cs", "d", "eb", "e", "f", "fs", "g", "ab", "a", "bb", "b")
GRID = re.compile(r"^[xXo1-9.\-]+$")
HELPERS = ROOT / "docs" / "live-grid.rb"
CATALOG = ROOT / "config" / "sonicpi_catalog.json"


# 音色の選択画面用: シンセの分類と一言説明(Sonic Pi 内蔵のシンセ名 -> [分類, 説明])
SYNTH_INFO = {
    "sine": ["基本の音", "純粋なサイン波。丸くて澄んだ音。サブベースやパッドの土台"],
    "saw": ["基本の音", "ノコギリ波。明るくて倍音が多い。リード・ベースの定番"],
    "square": ["基本の音", "矩形波。ファミコンのような中空の音"],
    "tri": ["基本の音", "三角波。サインより少し明るい、やわらかい音"],
    "pulse": ["基本の音", "パルス波。細い鼻にかかった音"],
    "dsaw": ["基本の音", "2 本のノコギリ波を少しずらして重ねた、厚い音"],
    "dtri": ["基本の音", "2 本の三角波を重ねた、ふわっと厚い音"],
    "dpulse": ["基本の音", "2 本のパルス波を重ねた、うねる音"],
    "supersaw": ["基本の音", "ノコギリ波をたくさん重ねた、幅広くきらびやかな音。Future Bass のコード向き"],
    "beep": ["基本の音", "単純なビープ音"],
    "mod_sine": ["基本の音", "サイン波にモジュレーション(揺れ)を付けた音"],
    "mod_saw": ["基本の音", "ノコギリ波にモジュレーションを付けた音"],
    "mod_dsaw": ["基本の音", "厚いノコギリ波にモジュレーションを付けた音"],
    "mod_tri": ["基本の音", "三角波にモジュレーションを付けた音"],
    "mod_pulse": ["基本の音", "パルス波にモジュレーションを付けた音"],
    "mod_fm": ["基本の音", "FM 合成にモジュレーションを付けた音"],
    "mod_beep": ["基本の音", "ビープ音にモジュレーションを付けた音"],
    "bass_foundation": ["ベース", "太く深い低音。ハーモニクスが多めで存在感がある"],
    "bass_highend": ["ベース", "高域の倍音が強いベース。小さいスピーカーでも聞こえる"],
    "subpulse": ["ベース", "丸いサブベース(パルス波ベース)。重く沈む"],
    "chipbass": ["ベース", "ファミコン風の 8bit ベース"],
    "tb303": ["ベース", "アシッドベース(TB-303 風)。cutoff を動かすとうねる"],
    "growl": ["ベース", "うなるようなベース。Dubstep・Phonk 向き"],
    "gabberkick": ["ベース", "ガバキック風の歪んだ低音の打撃"],
    "prophet": ["リード", "Prophet 風のアナログシンセ。温かみのあるリード・コード"],
    "blade": ["リード", "ブレードランナー風の、ゆらぐ哀愁のあるシンセ"],
    "hoover": ["リード", "レイヴの Hoover 音。ずり上がる分厚いリード"],
    "tech_saws": ["リード", "ノコギリ波の重なり。テクノ向けの鋭いリード"],
    "winwood_lead": ["リード", "70 年代風のオルガン系リード"],
    "zawa": ["リード", "ざわざわ揺れる、不思議な質感のリード"],
    "chiplead": ["リード", "ファミコン風の 8bit リード"],
    "rodeo": ["リード", "カントリー風のはじけるリード"],
    "fm": ["リード", "FM 合成。金属的・ベル的な音"],
    "hollow": ["パッド", "中空でかすれた、静かなパッド"],
    "dark_ambience": ["パッド", "暗く広がるアンビエント。リバーブ感がある"],
    "organ_tonewheel": ["パッド", "トーンホイールオルガン。温かく持続する"],
    "piano": ["鍵盤・ベル", "ピアノ。音量は低め(amp 0.2 前後から)に注意。DAW では amp に 0.2 を掛けて鳴らす"],
    "rhodey": ["鍵盤・ベル", "エレクトリックピアノ(Rhodes 風)。まるくて甘い"],
    "kalimba": ["鍵盤・ベル", "カリンバ(親指ピアノ)。素朴でかわいい"],
    "pretty_bell": ["鍵盤・ベル", "きらっとしたベル"],
    "dull_bell": ["鍵盤・ベル", "鈍く落ち着いたベル"],
    "pluck": ["鍵盤・ベル", "撥弦(はじいた弦)。短く立ち上がって減衰する"],
    "noise": ["ノイズ", "ホワイトノイズ。ライザーやスネアの飾りに"],
    "bnoise": ["ノイズ", "ブラウンノイズ。低域が重いノイズ"],
    "cnoise": ["ノイズ", "クリップノイズ。ざらついたノイズ"],
    "gnoise": ["ノイズ", "グレーノイズ。まるいノイズ"],
    "pnoise": ["ノイズ", "ピンクノイズ。自然な風のようなノイズ"],
    "chipnoise": ["ノイズ", "8bit 風のノイズ(ファミコンのドラム音)"],
}
for _n, _d in {"bassdrum": "808 のバスドラ。長くて丸いキック(低い音で鳴らすとサブベースにもなる)", "snare": "808 のスネア", "clap": "808 のクラップ",
               "closed_hihat": "808 のクローズハット", "open_hihat": "808 のオープンハット", "cymbal": "808 のシンバル",
               "rimshot": "808 のリムショット", "claves": "808 のクラベス(木の高い打音)", "cowbell": "808 のカウベル",
               "maracas": "808 のマラカス", "congahi": "808 のコンガ(高)", "congamid": "808 のコンガ(中)", "congalo": "808 のコンガ(低)",
               "tomhi": "808 のタム(高)", "tommid": "808 のタム(中)", "tomlo": "808 のタム(低)"}.items():
    SYNTH_INFO["sc808_" + _n] = ["808 の打楽器", _d + "。シンセとして鳴らせる"]
SAMPLE_GROUPS = {
    "bd": "キック", "sn": "スネア", "hat": "ハット", "drum": "ドラム", "elec": "エレクトロ", "perc": "打楽器・効果音",
    "ride": "ライド", "tabla": "タブラ", "bass": "ベース(サンプル)", "ambi": "アンビエント", "glitch": "グリッチ",
    "guit": "ギター", "loop": "ループ(長い)", "vinyl": "ビニール", "mehackit": "mehackit", "arovane": "arovane ビート",
    "tbd": "パッド・FX", "misc": "その他",
}
NOT_MUSICAL = {"sound_in", "sound_in_stereo"}  # マイク入力。作曲の音色には出さない


def catalog() -> dict:
    c = json.loads(CATALOG.read_text(encoding="utf-8"))
    samples = sorted({n for names in c["samples"].values() for n in names})
    group_of = {n: g for g, names in c["samples"].items() for n in names}
    synths = sorted(n for n in c["synths"] if n not in NOT_MUSICAL)
    return {"synths": synths, "samples": samples, "chords": CHORD_TYPES, "roots": ROOTS,
            "fx_info": {n: {"label": v[0], "desc": v[1], "mix": v[2], "params": {k: list(q) for k, q in v[3].items()}}
                        for n, v in FX_INFO.items()},
            "synth_info": {n: SYNTH_INFO.get(n, ["その他", ""]) for n in synths},
            "sample_group": {n: SAMPLE_GROUPS.get(group_of[n], group_of[n]) for n in samples}}


def ident(s: str, fallback: str) -> str:
    s = re.sub(r"[^a-z0-9_]", "_", str(s).lower()).strip("_")
    if not s or not s[0].isalpha():
        s = fallback
    return s[:24]


def num(v, lo: float, hi: float, default: float) -> float:
    try:
        f = float(v)
    except (TypeError, ValueError):
        return default
    return min(max(f, lo), hi)


def pitch_sym(p: str) -> str:
    m = PITCH.match(str(p).lower())
    if not m or not -1 <= int(m.group(3)) <= 8:
        raise ValueError(f"音名が不正です: {p}")
    return ":" + p.lower()


def name_midi(n: str) -> int:
    m = PITCH.match(n.lower())
    pc = {"c": 0, "d": 2, "e": 4, "f": 5, "g": 7, "a": 9, "b": 11}[m.group(1)] + {"": 0, "s": 1, "b": -1}[m.group(2)]
    return pc + 12 * (int(m.group(3)) + 1)  # gb4 や db5 のような異名同音も読める


def midi_name(m: int) -> str:
    return ROOTS[m % 12] + str(m // 12 - 1)


def legacy_notes(kind: str, steps: str, prog: list, res: int, cells_bar: int, octave: int) -> list:
    """古い形式(X と - のグリッド + コード進行)を [拍, 音名, 長さ] の並びに直す。bass は根音(E1〜の範囲)、chord は構成音。"""
    steps = re.sub(r"[ |\t]", "", steps)
    out, i = [], 0
    while i < len(steps):
        if steps[i] in "Xxo123456789":
            ln = 1
            while i + ln < len(steps) and steps[i + ln] == "-":
                ln += 1
            root, typ = prog[(i // cells_bar) % len(prog)]
            pc = ROOTS.index(root)
            if kind == "bass":
                m = pc + 24
                while m < 28:
                    m += 12
                midis = [m if m <= 39 else m - 12]
            else:
                midis = [pc + 12 * (octave + 1) + x for x in CHORD_TYPES[typ]]
            out += [[i / res, midi_name(m), ln / res] for m in midis]
            i += ln
        else:
            i += 1
    return out


def norm_steps(raw, want: int, tid: str) -> str:
    steps = re.sub(r"[ |\t]", "", str(raw or ""))
    steps = re.sub(r"[xo1-9]", "X", steps)  # 音の強さは使わない: 音はすべて X
    if steps and not GRID.match(steps):
        raise ValueError(f"{tid}: パターンに使えない文字があります")
    return (steps + "." * want)[:want]


def fx_track(t: dict, tid: str, v: dict, want: int) -> dict:
    name = v.get("name")
    if name not in FX_INFO:
        raise ValueError(f"{tid}: エフェクトが見つかりません: {name}")
    _, _, mix0, spec = FX_INFO[name]
    raw = v.get("params") if isinstance(v.get("params"), dict) else {}
    params = {}
    for k, (_, lo, hi, d) in spec.items():
        x = num(raw.get(k), lo, hi, d)
        params[k] = int(round(x)) if k in INT_PARAMS else round(x, 3)
    voice = {"name": name, "mix": round(num(v.get("mix"), 0, 1, mix0), 2), "params": params}
    ids = t.get("targets") if isinstance(t.get("targets"), list) else []
    out = {"id": tid, "name": str(t.get("name") or tid)[:24], "kind": "fx", "voice": voice,
           "targets": [ident(i, "x") for i in ids][:24], "mute": bool(t.get("mute")), "solo": False}
    if name == "sidechain":
        out["steps"] = norm_steps(t.get("steps"), want, tid)
    au = t.get("automation")   # {"param": "cutoff", "points": [[拍, 値], …]}: 値を時間で動かす(点の間は直線でなめらかに)
    if isinstance(au, dict) and (au.get("param") in spec or au.get("param") == "mix") and isinstance(au.get("points"), list):
        lo, hi = (0, 1) if au["param"] == "mix" else spec[au["param"]][1:3]
        pts = sorted({(round(num(x[0], 0, want, 0) * 4) / 4, round(num(x[1], lo, hi, lo), 3)) for x in au["points"][:64]})
        if len(pts) >= 2:
            out["automation"] = {"param": au["param"], "points": [list(x) for x in pts]}
    return out


def validate(project: dict) -> dict:
    """範囲外・不正な値は直すか、ValueError。戻り値は正規化したプロジェクト。"""
    cat = catalog()
    bpm = num(project.get("bpm"), 40, 240, 120)
    bars = int(num(project.get("bars"), 1, MAX_BARS, 4))
    res, meter = 4, int(num(project.get("meter"), 2, 7, 4))
    key = project.get("key") or {}
    key_root = key.get("root") if key.get("root") in ROOTS else "c"
    key_scale = key.get("scale") if key.get("scale") in ("major", "minor") else "major"
    prog = []
    for c in (project.get("prog") or [])[:bars]:
        if c is None:  # コードなしの小節(GUI で小節を増やした直後など)
            prog.append(None)
            continue
        root, typ = (c + [None, None])[:2] if isinstance(c, list) else (None, None)
        if root not in ROOTS or typ not in CHORD_TYPES:
            raise ValueError(f"コードが不正です: {c}")
        prog.append([root, typ])
    tonic = [key_root, "minor" if key_scale == "minor" else "major"]
    prog = prog or [tonic]
    cells_bar = res * meter
    tracks, seen = [], set()
    for i, t in enumerate((project.get("tracks") or [])[:MAX_TRACKS]):
        kind = t.get("kind")
        if kind not in KINDS:
            raise ValueError(f"トラックの種類が不正です: {kind}")
        tid = ident(t.get("id") or t.get("name"), f"track{i + 1}")
        while tid in seen:
            tid += "_"
        seen.add(tid)
        v = t.get("voice") or {}
        name = v.get("name")
        if kind == "fx":
            tracks.append(fx_track(t, tid, v, bars * cells_bar))
            continue
        pool = cat["samples"] if kind == "drum" else cat["synths"]
        if kind == "drum" and is_vocal_wav(name):   # ボコーダーで作った wav(work/vocals 内)は、サンプル名の代わりにパスで指せる
            pass
        elif name not in pool:
            raise ValueError(f"{tid}: 音色が見つかりません: {name}")
        voice = {"name": name, "amp": round(num(v.get("amp", v.get("velocity")), 0, 2, 0.8), 3), "pan": round(num(v.get("pan"), -1, 1, 0), 2)}
        if kind == "drum" and num(v.get("rate"), -2, 2, 1) not in (0, 1):   # サンプルの再生速度。-1 = 逆再生(リバース)
            voice["rate"] = round(num(v.get("rate"), -2, 2, 1), 2)
        if kind != "drum":
            voice["cutoff"] = int(num(v.get("cutoff"), 20, 130, 100))
            voice["env"] = v.get("env") if v.get("env") in ENVS else "stab"
            if num(v.get("glide"), 0, 2, 0) > 0:   # グライド(ポルタメント): 次の音に続くとき、音の最後の glide 拍で次の音程へ滑る
                voice["glide"] = round(num(v.get("glide"), 0, 2, 0), 2)
            if name.startswith("mod_"):   # mod_* は音程を周期的に揺らせる。ビブラート = 小さい mod_range をゆっくり揺らす
                voice["mod_range"] = round(num(v.get("mod_range"), 0, 12, 0.4), 2)    # 揺れの幅(半音)
                voice["mod_phase"] = round(num(v.get("mod_phase"), 0.05, 2, 0.35), 2)  # 揺れの周期(拍)
        if kind != "drum":  # bass / chord / melody はすべて音程つきの音(ピアノロール)
            beats_total = bars * meter
            raw = t.get("notes")
            if raw is None and t.get("steps"):  # 古い形式(コード進行に従うグリッド)は、音程つきの音に直す
                raw = legacy_notes(kind, str(t["steps"]), [c or tonic for c in prog], res, cells_bar, int(num(t.get("octave"), 2, 6, 4)))
            notes = []
            note_res = res * 2
            for n in (raw or [])[:MAX_NOTES]:
                beat = round(num(n[0], 0, beats_total - 0.125, 0) * note_res) / note_res   # 音の位置・長さは 0.125 拍刻み(溜めなどの微妙なずらし用)
                ln = max(round(num(n[2], 0.125, beats_total, 0.5) * note_res) / note_res, 1 / note_res)
                pitch_sym(n[1])
                item = [beat, str(n[1]).lower(), min(ln, beats_total - beat)]
                if len(n) > 3 and num(n[3], -24, 24, 0):   # ピッチベンド(半音): 音の長さをかけて、この分だけ音程が動く
                    item.append(round(num(n[3], -24, 24, 0), 2))
                notes.append(item)
            notes.sort(key=lambda x: (x[0], name_midi(x[1])))
            tracks.append({"id": tid, "name": str(t.get("name") or tid)[:24], "kind": kind, "voice": voice,
                           "notes": notes, "mute": bool(t.get("mute")), "solo": bool(t.get("solo"))})
            continue
        steps = norm_steps(t.get("steps"), bars * cells_bar, tid)
        out = {"id": tid, "name": str(t.get("name") or tid)[:24], "kind": kind, "voice": voice, "steps": steps,
               "mute": bool(t.get("mute")), "solo": bool(t.get("solo"))}
        tracks.append(out)
    for x, raw in zip(tracks, (project.get("tracks") or [])[:MAX_TRACKS], strict=True):  # 表示色(#rrggbb)だけ引き継ぐ
        c = raw.get("color")
        if isinstance(c, str) and re.fullmatch(r"#[0-9a-fA-F]{6}", c):
            x["color"] = c.lower()
    markers = []
    for m in (project.get("markers") or [])[:64]:  # セクション名(小節の位置 + 名前)
        if isinstance(m, dict) and isinstance(m.get("bar"), int) and 0 <= m["bar"] < bars and str(m.get("name") or "").strip():
            markers.append({"bar": m["bar"], "name": str(m["name"]).strip()[:16]})
    markers = sorted({m["bar"]: m for m in markers}.values(), key=lambda m: m["bar"])
    music = {x["id"] for x in tracks if x["kind"] != "fx"}
    for x in tracks:
        if x["kind"] == "fx":  # 存在しないトラックは外す。空 = 全トラック
            x["targets"] = [i for i in x["targets"] if i in music]
    return {"name": ident(project.get("name"), "song"), "bpm": bpm, "bars": bars, "meter": meter, "res": res,
            "key": {"root": key_root, "scale": key_scale}, "prog": prog, "markers": markers, "tracks": tracks}


def slice_project(project: dict, start_cell: int = 0, end_cell: int | None = None) -> dict:
    """曲の一部([start_cell, end_cell) マス = 16 分音符)だけを取り出した、先頭から始まるプロジェクト。途中から鳴らす用。"""
    p = validate(project)
    res, meter = p["res"], p["meter"]
    cb = res * meter
    total = p["bars"] * cb
    a = max(0, min(int(start_cell), total - 1))
    b = total if end_cell is None else max(a + 1, min(int(end_cell), total))
    bars = max(1, -(-(b - a) // cb))
    t0, t1 = a / res, b / res   # 拍
    tracks = []
    for t in p["tracks"]:
        x = {**t}
        if "steps" in x:
            x["steps"] = x["steps"][a:b]   # 足りない分は validate が休みで埋める
        if x.get("automation"):   # 範囲の頭の値から始める
            pts = x["automation"]["points"]

            def at(b, pts=pts):
                if b <= pts[0][0]:
                    return pts[0][1]
                for (b0, v0), (b1, v1) in zip(pts, pts[1:], strict=False):
                    if b0 <= b <= b1:
                        return v0 + (v1 - v0) * (b - b0) / (b1 - b0) if b1 > b0 else v1
                return pts[-1][1]
            q = [[0, at(t0)]] + [[b - t0, v] for b, v in pts if t0 < b < t1] + [[t1 - t0, at(t1)]]
            x["automation"] = {**x["automation"], "points": q}
        if "notes" in x:
            notes = []
            for n in x["notes"]:   # 範囲の前から鳴っている音は、範囲の頭から残りの長さで鳴らし直す
                s, e = max(n[0], t0), min(n[0] + n[2], t1)
                if e > s:
                    notes.append([s - t0, n[1], e - s] + (n[3:] if (s, e) == (n[0], n[0] + n[2]) else []))
            x["notes"] = notes
        tracks.append(x)
    first = a // cb
    return {**p, "bars": bars, "prog": p["prog"][first : first + bars] or [None], "markers": [], "tracks": tracks}


def bend_rows(notes: list, glide: float):
    """ピッチベンドかグライドがあるトラックの音を、[拍, 音名, 長さ, ベンド(半音), 滑り始めまでの拍, 滑る拍数] にする。なければ None。
    グライド: 次の音がちょうど続いて始まり(和音なら音程がいちばん近い音へ、7 半音以内)、音程が違うとき、最後の glide 拍で滑る。"""
    if not glide and not any(len(n) > 3 for n in notes):
        return None
    rows = []
    for n in notes:
        bd, gs, g = (n[3] if len(n) > 3 else 0), 0.0, max(n[2], 0.25)
        if len(n) > 3:
            gs, g = 0.0, n[2]
        elif glide:
            nxt = [m for m in notes if m is not n and abs(m[0] - (n[0] + n[2])) < 0.01]
            if nxt:
                d = min((name_midi(m[1]) - name_midi(n[1]) for m in nxt), key=abs)
                if 0 < abs(d) <= 7:
                    g = min(glide, n[2])
                    bd, gs = d, n[2] - g
        rows.append([n[0], n[1], n[2], bd, gs, g])
    return rows


def is_vocal_wav(name) -> bool:
    """work/vocals/ の中の、実在する .wav への絶対パスか(ボーカルの wav を DAW のドラム行で鳴らす用)。"""
    try:
        p = Path(str(name)).resolve()
        return p.suffix == ".wav" and p.is_file() and p.is_relative_to((ROOT / "work" / "vocals").resolve())
    except (OSError, ValueError):
        return False


def sample_ref(name: str) -> str:
    return json.dumps(name) if name.startswith("/") else f":{name}"


def fmt_pattern(steps: str, res: int, meter: int) -> str:
    bar = res * meter
    return " | ".join(" ".join(steps[k : k + res] for k in range(b, min(b + bar, len(steps)), res))
                      for b in range(0, len(steps), bar))


ENV_BEATS = {"pluck": (0, 0.03), "stab": (0.01, 0.15), "pad": (0.4, 1.0), "swell": (0.4, 0.03)}  # attack, release(拍)


PIANO_AMP = 0.2   # :piano は他のシンセよりかなり大きく鳴るので、amp に掛けて揃える(目安。録音で確かめる)


def opts_str(voice: dict, kind: str) -> str:
    if kind != "drum" and voice["name"] == "piano":
        # :piano は自然な減衰が音色。attack / cutoff は渡さない(attack は短くする向きにしか効かない)。
        # 音の長さ(sustain)は渡す: 渡さないと、既定の sustain 0 / release 1 で約 1 拍で切れてしまう。長い音ほど長く鳴る。
        # amp は音量と、打鍵の強さ(vel。強いほど明るく硬い音)の両方に効かせる
        parts = [f"amp: {voice['amp'] * PIANO_AMP:g}", f"vel: {min(voice['amp'], 1):g}"]
        if voice.get("pan"):
            parts.append(f"pan: {voice['pan']:g}")
        return ", ".join(parts)
    parts = [f"amp: {voice['amp']:g}"]
    if voice.get("pan"):
        parts.append(f"pan: {voice['pan']:g}")
    if voice.get("rate"):
        parts.append(f"rate: {voice['rate']:g}")
    if kind != "drum":
        att, rel = ENV_BEATS[voice["env"]]
        parts += [f"cutoff: {voice['cutoff']}", f"attack: {att:g}", f"release: {rel:g}"]
        if "mod_range" in voice:
            parts += [f"mod_range: {voice['mod_range']:g}", f"mod_phase: {voice['mod_phase']:g}", "mod_wave: 3"]   # 3 = サイン波
    return ", ".join(parts)


def active(tracks: list[dict]) -> list[dict]:
    """鳴らすトラック。ソロは音のトラックだけに効く(エフェクトはソロ中も、ミュートしていなければ効く)。"""
    music = [t for t in tracks if t["kind"] != "fx"]
    soloed = [t for t in music if t["solo"]]
    return (soloed or [t for t in music if not t["mute"]]) + [t for t in tracks if t["kind"] == "fx" and not t["mute"]]


def fx_opts(fx: dict) -> str:
    v = fx["voice"]
    vals = {"mix": v["mix"], **v["params"]}
    au = fx.get("automation")
    if au:   # オートメーションの最初の値から始める
        vals[au["param"]] = au["points"][0][1]
    return ", ".join(f"{k}: {x:g}" for k, x in vals.items())


def auto_loop(f: dict, sfx: str, pad: str, total: int) -> list[str]:
    """オートメーションの live_loop: 点と点の間を、<param>_slide でなめらかに動かす。"""
    au, fid = f["automation"], f["id"]
    pts, prm = au["points"], au["param"]
    segs = ", ".join(f"[{a[0]:g}, {b[0] - a[0]:g}, {b[1]:g}]" for a, b in zip(pts, pts[1:], strict=False))
    lines = [f"auto_{fid}{sfx} = [{segs}]   # {f['name']}: [開始の拍, かける拍数, 行き先の値]",
             f"live_loop :auto_{fid}{sfx} do", "  t = 0", f"  auto_{fid}{sfx}.each do |b, d, v|", "    sleep b - t",
             f"    control fx_{fid}{sfx}, {prm}_slide: d", f"    control fx_{fid}{sfx}, {prm}: v", "    t = b", "  end",
             f"  sleep {total} - t", "end"]
    return [pad + ln for ln in lines]


def generate(project: dict) -> str:
    p = validate(project)
    res, meter, bars = p["res"], p["meter"], p["bars"]
    out = [f"# {p['name']} / {p['bpm']:g} BPM / {bars} 小節 / key {p['key']['root']} {p['key']['scale']}",
           "# DAW 風 GUI(scripts/daw_server.py)が work/daw/ のプロジェクトから生成したコード。",
           HELPERS.read_text(encoding="utf-8").rstrip(), "",
           f"use_bpm {p['bpm']:g}", f"grid_res {res}", f"grid_meter {meter}",
           "# コード進行(ガイド。ピアノロールのコードトーン表示用): " + " / ".join(f"{c[0]} {c[1]}" if c else "なし" for c in p["prog"]), ""]
    play = active(p["tracks"])
    music = [t for t in play if t["kind"] != "fx"]
    fxs = [t for t in play if t["kind"] == "fx"]
    total = bars * meter
    loops: dict[str, list[str]] = {}   # トラック id -> live_loop の行
    for t in music:
        i, v = t["id"], t["voice"]
        if t["kind"] == "drum":
            out += [f"voice_{i} = grid_voice :sample, {sample_ref(v['name'])}, {opts_str(v, 'drum')}",
                    f"pat_{i} = \"{fmt_pattern(t['steps'], res, meter)}\""]
            loops[i] = [f"live_loop :{i} do grid_play voice_{i}, pat_{i} end"]
        else:
            rows = bend_rows(t["notes"], v.get("glide", 0))
            bent = rows is not None
            if bent:
                notes = ", ".join(f"[{r[0]:g}, {pitch_sym(r[1])}, {r[2]:g}, {r[3]:g}, {r[4]:g}, {r[5]:g}]" for r in rows)
                out.append(f"notes_{i} = [{notes}]   # [拍の位置, 音名, 長さ(拍), ピッチベンド(半音), 滑り始めまでの拍, 滑る拍数]")
                play = [f"    s = play n, {opts_str(v, 'note')}, sustain: l, note_slide: g",
                        "    if bd != 0", "      in_thread do", "        sleep gs", "        control s, note: note(n) + bd", "      end", "    end"]
            else:
                notes = ", ".join(f"[{n[0]:g}, {pitch_sym(n[1])}, {n[2]:g}]" for n in t["notes"])
                out.append(f"notes_{i} = [{notes}]   # [拍の位置, 音名, 長さ(拍)]")
                play = [f"    play n, {opts_str(v, 'note')}, sustain: l"]
            loops[i] = [f"live_loop :{i} do", f"  use_synth :{v['name']}", "  t = 0",
                        f"  notes_{i}.each do |b, n, l{', bd, gs, g' if bent else ''}|", "    sleep b - t",
                        *play, "    t = b", "  end",
                        f"  sleep {total} - t", "end"]
    for f in fxs:
        if f["voice"]["name"] == "sidechain":
            hits = ", ".join(f"{k / res:g}" for k, c in enumerate(f["steps"]) if c == "X")
            out.append(f"hits_{f['id']} = [{hits}]   # {f['name']}: 音量を下げる拍の位置")
    out.append("")
    # 同じエフェクトの組み合わせが掛かるトラックは、1 つの with_fx(同じエフェクトの実体)を共有する
    groups: dict[tuple, list[str]] = {}
    for t in music:
        chain = tuple(f["id"] for f in fxs if not f["targets"] or t["id"] in f["targets"])
        groups.setdefault(chain, []).append(t["id"])
    by_id = {f["id"]: f for f in fxs}
    for n, (chain, ids) in enumerate(groups.items(), 1):
        body: list[str] = []
        for i in ids:
            body += loops[i] + [""]
        pad = ""
        head: list[str] = []
        sfx = f"_g{n}" if len(groups) > 1 else ""
        # 先頭のエフェクトが最初に音を受ける(いちばん内側)。外側から順に開く
        for fid in reversed(chain):
            f = by_id[fid]
            if f["voice"]["name"] == "sidechain":
                head.append(f"{pad}with_fx :level, amp: 1, amp_slide: 0.02 do |lv_{fid}{sfx}|")
                pad += "  "
                head += duck_loop(f, sfx, pad, total)
            else:
                au = f.get("automation")
                var = f" |fx_{fid}{sfx}|" if au else ""
                head.append(f"{pad}with_fx :{f['voice']['name']}, {fx_opts(f)} do{var}")
                pad += "  "
                if au:
                    head += auto_loop(f, sfx, pad, total)
        block = head + [pad + ln if ln else "" for ln in body]
        for _ in chain:
            pad = pad[:-2]
            block.append(f"{pad}end")
        # グループごとに in_thread で並列に起動する。with_fx は 1 つずつ Sonic Pi の準備を待つので、続けて書くと待ち時間が足し算になり、
        # 最後のほうの live_loop が「thread got too far behind time」で止まる(途中から再生したとき、音が消える)
        out += ["in_thread do"] + [("  " + ln if ln else "") for ln in block] + ["end", ""]
    if not music:
        out += ["live_loop :silence do sleep 1 end", ""]
    return "\n".join(out)


def duck_loop(f: dict, sfx: str, pad: str, total: int) -> list[str]:
    """サイドチェインの live_loop: hits の位置で :level の amp を下げ、すぐ戻す。"""
    fid, p = f["id"], f["voice"]["params"]
    lv = f"lv_{fid}{sfx}"
    lines = [f"live_loop :duck_{fid}{sfx} do", "  t = 0", f"  hits_{fid}.each do |b|", "    sleep b - t",
             f"    control {lv}, amp_slide: 0.02", f"    control {lv}, amp: {1 - p['depth']:g}", "    sleep 0.04",
             f"    control {lv}, amp_slide: {p['release']:g}", f"    control {lv}, amp: 1", "    t = b + 0.04", "  end",
             f"  sleep {total} - t", "end"]
    return [pad + ln for ln in lines]


STEMS = ROOT / "stems"


def validate_stem(d: dict) -> dict:
    """stem(トラックの雛形)を検証して正規化する。stem は音色だけを持ち、パターン・音は持たない(追加すると必ず空のトラックになる)。"""
    kind = d.get("kind")
    t = {"id": "stem", "name": d.get("name"), "kind": kind, "voice": d.get("voice")}
    n = validate({"bars": 1, "meter": 4, "prog": [["c", "major"]], "tracks": [t]})["tracks"][0]
    return {"name": n["name"], "kind": kind, "voice": n["voice"], "description": str(d.get("description") or "")[:120],
            "source": "ai" if d.get("source") == "ai" else "user"}  # ai = AI(Claude)が作った stem


def list_stems() -> list[dict]:
    out = []
    for f in sorted(STEMS.glob("*.json")) if STEMS.is_dir() else []:
        try:
            out.append({"id": f.stem, **validate_stem(json.loads(f.read_text(encoding="utf-8")))})
        except (ValueError, json.JSONDecodeError):
            continue  # 壊れた stem は一覧に出さない(ファイルは触らない)
    return out


PRESETS_DIR = ROOT / "presets"


def validate_preset(d: dict) -> dict:
    """プリセット = 曲の状態まるごと(BPM・小節数・キー・コード進行・全トラックの音色とパターン/音)。検証して正規化する。"""
    name = str(d.get("name") or "").strip()[:40]
    if not name:
        raise ValueError("名前が空です")
    p = validate(d.get("project") or {})
    for t in p["tracks"]:
        t["mute"] = t["solo"] = False  # ミュート/ソロは保存しない
    return {"name": name, "description": str(d.get("description") or "")[:120], "project": p}


def list_presets() -> list[dict]:
    out = []
    for f in sorted(PRESETS_DIR.glob("*.json")) if PRESETS_DIR.is_dir() else []:
        try:
            out.append({"id": f.stem, **validate_preset(json.loads(f.read_text(encoding="utf-8")))})
        except (ValueError, json.JSONDecodeError):
            continue
    return out


def main() -> None:
    """CLI(AI が DAW のファイルを書いたあとの確認用)。
    stems          stems/ の全ファイルを検証して、誤りの理由を出す
    check <名前>   work/daw/<名前>.json を検証する(誤りはその理由を出す)
    export <名前> [出力先.rb]   プロジェクトから Sonic Pi のコードを書き出す(既定 work/daw/<名前>.rb)"""
    import sys
    args = sys.argv[1:]
    usage = "使い方: daw_codegen.py stems | check <名前> | export <名前> [出力先.rb]"
    if args == ["stems"]:
        bad = 0
        for f in sorted(STEMS.glob("*.json")):
            try:
                st = validate_stem(json.loads(f.read_text(encoding="utf-8")))
                print(f"OK   {f.name}: {st['name']}({st['kind']} / {st['voice']['name']})")
            except (ValueError, json.JSONDecodeError) as e:
                bad += 1
                print(f"誤り {f.name}: {e}")
        sys.exit(2 if bad else 0)
    if len(args) in (2, 3) and args[0] in ("check", "export") and (args[0] == "export" or len(args) == 2):
        src = ROOT / "work" / "daw" / f"{ident(args[1], 'song')}.json"
        try:
            proj = json.loads(src.read_text(encoding="utf-8"))
            p = validate(proj)
        except (OSError, ValueError) as e:  # JSONDecodeError は ValueError
            sys.exit(f"誤り {src.name}: {e}")
        if args[0] == "check":
            print(f"OK   {src.name}: {p['bpm']:g} BPM / {p['bars']} 小節 / " + " ".join(f"{t['id']}({t['kind']})" for t in p["tracks"]))
            return
        out = ROOT / args[2] if len(args) == 3 else src.with_suffix(".rb")
        out.write_text(generate(proj), encoding="utf-8")
        print(f"書き出しました: {out}(次に uv run scripts/live_check.py {out.relative_to(ROOT)})")
        return
    sys.exit(usage)


if __name__ == "__main__":
    main()
