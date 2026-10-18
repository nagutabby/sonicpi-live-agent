import lyric_check as lc
import neutrino_sing as ns

BAR = [["あ", "C5", 1], ["い", "D5", 1], ["う", "E5", 1], ["え", "F5", 1]]


def spec(notes):
    return {"bpm": 120, "notes": notes}


def test_clean_phrase_has_no_findings():
    errors, warns, _ = lc.check(spec(BAR))
    assert errors == [] and warns == []


def test_two_moras_in_one_note_is_error_but_youon_is_ok():
    errors, _, _ = lc.check(spec([["きょ", "C5", 1], ["おお", "D5", 1], ["う", "E5", 2]]))
    assert len(errors) == 1 and "おお" in errors[0]


def test_particle_hint_and_crossing_bar():
    errors, warns, _ = lc.check(spec([["は", "C5", 3], ["あ", "D5", 2], ["", "", 3]]))
    assert any("わ" in w for w in warns)
    assert any("またぎ" in e for e in errors)


def test_tie_crosses_bar_and_needs_same_pitch():
    ok = spec([["あ", "C5", 2], ["い", "D5", 2, "tie"], ["", "D5", 4]])
    assert lc.check(ok)[0] == []
    bad = spec([["あ", "C5", 2], ["い", "D5", 2, "tie"], ["", "E5", 4]])
    assert any("tie" in e for e in lc.check(bad)[0])


def test_short_rest_inside_phrase_warns():
    _, warns, _ = lc.check(spec([["あ", "C5", 1.5], ["", "", 0.5], ["い", "D5", 1], ["う", "E5", 1]]))
    assert any("休符" in w for w in warns)


def test_long_phrase_without_breath_warns():
    notes = BAR * 5
    _, warns, _ = lc.check(spec(notes))
    assert any("息継ぎ" in w for w in warns)
    notes[7] = ["え", "F5", 1, "br"]
    assert not any("息継ぎ" in w for w in lc.check(spec(notes))[1])


def test_musicxml_has_breath_and_tie():
    xml = ns.build_musicxml(spec([["あ", "C5", 2, "br"], ["い", "D5", 2, "tie"], ["", "D5", 4]]), "t")
    assert "<breath-mark/>" in xml and xml.count('<tie type=') == 2
    assert xml.count("<lyric") == 2  # tie の後ろの音符には歌詞を付けない


def test_clip_wav_drops_lead_bar_and_keeps_length(tmp_path):
    import wave

    import numpy as np
    sr, bpm = 8000, 120  # 1 拍 = 0.5 秒
    x = np.concatenate([np.zeros(2 * sr), np.full(sr, 1000)]).astype("<i2")  # 4 拍の無音 + 2 拍の音
    src = tmp_path / "v.wav"
    with wave.open(str(src), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes(x.tobytes())
    out = ns.clip_wav(src, bpm, 4)
    with wave.open(str(out), "rb") as w:
        y = np.frombuffer(w.readframes(w.getnframes()), dtype="<i2")
    assert len(y) == 2 * sr and y[0] == 1000 and y[-1] == 0  # 4 拍ぶん(足りない分は無音)、末尾はフェード

