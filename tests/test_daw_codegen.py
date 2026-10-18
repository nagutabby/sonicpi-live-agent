import daw_codegen as g
import pytest

PROJ = {
    "name": "t1", "bpm": 130, "bars": 2, "key": {"root": "eb", "scale": "minor"},
    "prog": [["eb", "minor7"], ["bb", "dom7"]],
    "tracks": [
        {"name": "Kick", "kind": "drum", "voice": {"name": "bd_haus", "amp": 1}, "steps": "X... .... X... ...."},
        {"name": "Bass", "kind": "bass", "voice": {"name": "sine", "amp": 0.8}, "steps": "X--- ---- ---- ----"},
        {"name": "Keys", "kind": "chord", "voice": {"name": "supersaw", "amp": 0.5}, "steps": "x--. ..x- .... ....", "octave": 4},
        {"name": "Lead", "kind": "melody", "voice": {"name": "saw", "amp": 0.4},
         "notes": [[0, "eb4", 0.5, 90], [1.5, "gb4", 1, 70], [9, "bb4", 2, 50]]},
    ],
}


def test_generate_is_valid_sonicpi(tmp_path):
    import subprocess
    import sys
    code = g.generate(PROJ)
    # 古い形式(トラックの音量 + X)は、ノート・1 マスごとのベロシティに引き継がれる(amp 1 → ベロシティ 42)
    assert "hits_kick = [[0, 44], [2, 44]]" in code and "hits_kick.each do |b, vel|" in code
    # 古い形式のグリッド(bass / chord)は、コード進行から音程つきの音に直る
    assert "notes_bass = [[0, :eb2, 4, 34]" in code
    assert "notes_keys = [[0, :eb4, 0.75, 21], [0, :fs4, 0.75, 21]" in code
    assert "notes_lead = [[0, :eb4, 0.5, 90], [1.5, :gb4, 1, 70], [7.875, :bb4, 0.125, 50]]" in code  # 曲の外の音は末尾に丸める(0.125 拍刻み)
    f = tmp_path / "gen.rb"
    f.write_text(code, encoding="utf-8")
    r = subprocess.run([sys.executable, str(g.ROOT / "scripts" / "live_check.py"), str(f)], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr


def test_mute_and_solo():
    p = {**PROJ, "tracks": [dict(t) for t in PROJ["tracks"]]}
    p["tracks"][0]["mute"] = True
    assert "live_loop :kick" not in g.generate(p)
    p["tracks"][3]["solo"] = True
    c = g.generate(p)
    assert "live_loop :lead" in c and "live_loop :bass" not in c


@pytest.mark.parametrize("bad", [
    {"tracks": [{"kind": "drum", "voice": {"name": "x; system 'ls'"}, "steps": "x"}]},
    {"tracks": [{"kind": "melody", "voice": {"name": "saw"}, "notes": [[0, "h9", 1]]}]},
    {"tracks": [{"kind": "drum", "voice": {"name": "bd_haus"}, "steps": "x\nputs 1"}]},
    {"prog": [["zz", "minor"]]},
])
def test_rejects_bad_input(bad):
    with pytest.raises(ValueError):
        g.generate({**PROJ, **bad})


def test_track_named_like_sonicpi_api_passes_live_check(tmp_path):
    import subprocess
    import sys
    p = {**PROJ, "tracks": [{"id": "chord4", "kind": "chord", "voice": {"name": "supersaw"}, "steps": "x---"},
                            {"id": "scale1", "kind": "bass", "voice": {"name": "sine"}, "steps": "X---"}]}
    f = tmp_path / "gen.rb"
    f.write_text(g.generate(p), encoding="utf-8")
    r = subprocess.run([sys.executable, str(g.ROOT / "scripts" / "live_check.py"), str(f)], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout


def test_stem_holds_voice_only():
    st = g.validate_stem({"name": "K", "kind": "drum", "voice": {"name": "bd_haus", "amp": 1}, "steps": "X...X...", "notes": [[0, "c4", 1]]})
    assert "steps" not in st and "notes" not in st and st["voice"]["name"] == "bd_haus"
    with pytest.raises(ValueError):
        g.validate_stem({"name": "x", "kind": "drum", "voice": {"name": "nope"}})


def test_catalog_has_sound_info_for_every_sound():
    c = g.catalog()
    assert "sound_in" not in c["synths"]
    assert all(c["synth_info"][n][0] != "その他" and c["synth_info"][n][1] for n in c["synths"])
    assert set(c["sample_group"]) == set(c["samples"])


def test_shipped_stems_are_valid_and_generate():
    stems = g.list_stems()
    assert {s["id"] for s in stems} >= {"kick", "snare", "hat_8th", "bass_root", "chord_pad", "melody"}
    assert all("steps" not in s and "notes" not in s for s in stems)
    for st in stems:  # 1 つずつ曲に入れても、Sonic Pi のコードとして生成できる
        track = {"id": st["id"], "kind": st["kind"], "voice": st["voice"]}
        if st["kind"] == "fx":  # エフェクトは音のトラックに掛けて確かめる
            code = g.generate({**PROJ, "tracks": [PROJ["tracks"][0], track]})
            assert "with_fx" in code and "live_loop :kick" in code, st["id"]
            continue
        assert f"live_loop :{st['id']}" in g.generate({**PROJ, "tracks": [track]}), st["id"]
    assert sum(1 for st in stems if st["source"] == "ai") >= 40


def test_preset_keeps_tracks_and_voices_and_clears_mute():
    proj = {**PROJ, "tracks": [dict(t) for t in PROJ["tracks"]]}
    proj["tracks"][0]["mute"] = True
    pr = g.validate_preset({"name": " 曲A ", "project": proj})
    assert pr["name"] == "曲A" and len(pr["project"]["tracks"]) == 4
    assert pr["project"]["tracks"][0]["voice"]["name"] == "bd_haus" and pr["project"]["tracks"][0]["steps"].startswith(g.vel_level(42) + "...")
    assert pr["project"]["tracks"][3]["notes"] and not any(t["mute"] or t["solo"] for t in pr["project"]["tracks"])
    assert pr["project"]["prog"] == [["eb", "minor7"], ["bb", "dom7"]]
    for bad in ({"name": "", "project": PROJ}, {"name": "x", "project": {"tracks": [{"kind": "drum", "voice": {"name": "nope"}}]}}):
        with pytest.raises(ValueError):
            g.validate_preset(bad)


def test_drum_hits_carry_their_own_velocity():
    p = {**PROJ, "tracks": [{"id": "k", "kind": "drum", "voice": {"name": "bd_haus"}, "steps": "z1o5 .-.. ...."}]}
    assert g.validate(p)["tracks"][0]["steps"].startswith("z1o5.-..")   # 1 マスごとのベロシティ(1 = 最弱 … z = 最強)
    assert "hits_k = [[0, 127], [0.25, 4], [0.5, 87], [0.75, 18]]" in g.generate(p)


def test_velocity_is_required_per_note_and_per_hit():
    for bad in ({"kind": "melody", "voice": {"name": "saw"}, "notes": [[0, "c4", 1]]},   # ノートにベロシティがない
                {"kind": "drum", "voice": {"name": "bd_haus"}, "steps": "X..."}):        # X にはベロシティがない
        with pytest.raises(ValueError):
            g.validate({"bars": 1, "tracks": [bad]})
    v = g.validate({"bars": 1, "tracks": [{"kind": "melody", "voice": {"name": "saw"}, "notes": [[0, "c4", 1, 300]]}]})
    assert v["tracks"][0]["notes"] == [[0, "c4", 1, 127]] and "velocity" not in v["tracks"][0]["voice"]   # 範囲外は直す。トラックの音量は持たない


def test_stem_source_ai_is_kept_and_default_user():
    base = {"name": "S", "kind": "bass", "voice": {"name": "sine"}}
    assert g.validate_stem({**base, "source": "ai"})["source"] == "ai"
    assert g.validate_stem(base)["source"] == "user"
    assert g.validate_stem({**base, "source": "<script>"})["source"] == "user"


# ---- エフェクト(fx) ----
def fx_project(*fx):
    music = [{"id": "kick", "kind": "drum", "voice": {"name": "bd_haus"}, "steps": "h..." * 4},
             {"id": "bass", "kind": "bass", "voice": {"name": "sine"}, "notes": [[0, "c2", 1, 64]]}]
    return {"bars": 1, "tracks": music + list(fx)}


def test_fx_validate_clamps_and_cleans_targets():
    p = g.validate(fx_project({"id": "rv", "kind": "fx", "voice": {"name": "reverb", "mix": 5, "params": {"room": 9, "x": 1}},
                                     "targets": ["bass", "ghost"]}))
    fx = p["tracks"][2]
    assert fx["voice"] == {"name": "reverb", "mix": 1.0, "params": {"room": 1.0, "damp": 0.5}}
    assert fx["targets"] == ["bass"] and "steps" not in fx


def test_fx_unknown_name_rejected():
    with pytest.raises(ValueError):
        g.validate(fx_project({"id": "f", "kind": "fx", "voice": {"name": "nope"}}))


def test_fx_wraps_targets_only():
    code = g.generate(fx_project({"id": "rv", "kind": "fx", "voice": {"name": "reverb"}, "targets": ["bass"]}))
    body = code.split("use_bpm", 1)[1]
    i = body.index("with_fx :reverb")
    assert "live_loop :bass" in body[i:] and "live_loop :kick" not in body[i:]


def test_sidechain_ducks_on_steps():
    code = g.generate(fx_project({"id": "sc", "kind": "fx", "voice": {"name": "sidechain"}, "steps": "X...X...X...X..." , "targets": []}))
    assert "hits_sc = [0, 1, 2, 3]" in code and "with_fx :level" in code and "control lv_sc" in code


def test_solo_keeps_fx_and_mute_removes_it():
    fx = {"id": "rv", "kind": "fx", "voice": {"name": "reverb"}}
    pr = fx_project(fx)
    pr["tracks"][1]["solo"] = True
    assert "with_fx :reverb" in g.generate(pr) and "live_loop :kick" not in g.generate(pr)
    pr["tracks"][2]["mute"] = True
    assert "with_fx" not in g.generate(pr)


def test_fx_stem_valid():
    st = g.validate_stem({"name": "SC", "kind": "fx", "voice": {"name": "sidechain"}})
    assert st["kind"] == "fx" and st["voice"]["params"]["depth"] == 0.8


def test_empty_chord_bar_allowed():
    pr = {**PROJ, "prog": [["eb", "minor7"], None]}
    p = g.validate(pr)
    assert p["prog"] == [["eb", "minor7"], None]
    assert "eb minor7 / なし" in g.generate(pr)


def test_track_color_and_markers_kept():
    pr = {**PROJ, "markers": [{"bar": 1, "name": " サビ "}, {"bar": 9, "name": "x"}, {"bar": 0, "name": ""}]}
    pr = {**pr, "tracks": [{**pr["tracks"][0], "color": "#FF0000"}, {**pr["tracks"][1], "color": "red"}]}
    p = g.validate(pr)
    assert p["markers"] == [{"bar": 1, "name": "サビ"}]
    assert p["tracks"][0]["color"] == "#ff0000" and "color" not in p["tracks"][1]


def test_piano_keeps_natural_envelope():
    p = {"name": "p", "bpm": 130, "bars": 1, "key": {"root": "c", "scale": "minor"}, "prog": [None],
         "tracks": [{"name": "P", "kind": "melody", "voice": {"name": "piano", "env": "pad", "cutoff": 90},
                     "notes": [[0, "c5", 1, 64]]}]}
    line = [x for x in g.generate(p).splitlines() if "play n" in x and "piano" not in x][-1]
    assert "vel: vel / 127.0" in line and "amp: vel / 127.0 * 3 * 0.2" in line   # ベロシティは音量と打鍵の強さの両方に効く
    assert "sustain: l" in line   # 音の長さで鳴らす(渡さないと約 1 拍で切れる)
    assert not any(k in line for k in ("attack", "release", "cutoff"))


def test_slice_project_plays_from_the_middle():
    p = {"name": "s", "bpm": 120, "bars": 4, "key": {"root": "c", "scale": "minor"}, "prog": [None] * 4,
         "tracks": [{"name": "K", "kind": "drum", "voice": {"name": "bd_haus"}, "steps": "h... .... .... .... | " * 3 + "h... .... .... ...."},
                    {"name": "L", "kind": "melody", "voice": {"name": "saw"}, "notes": [[0, "c4", 8, 64], [9, "d4", 1, 64], [15, "e4", 1, 64]]}]}
    s = g.slice_project(p, 2 * 16, 4 * 16 - 16 + 8)   # 3 小節目の頭から、4 小節目の途中まで
    assert s["bars"] == 2
    assert s["tracks"][0]["steps"].startswith("h...........")
    assert s["tracks"][1]["notes"][0] == [1, "d4", 1, 64]   # 8 拍 = 3 小節目の頭(拍 8)より前の c4 は消え、拍 9 の d4 は 1 拍目へ
    assert "use_bpm 120" in g.generate(s)


def test_drum_rate_reverses_sample():
    p = {"name": "r", "bpm": 130, "bars": 1, "key": {"root": "c", "scale": "minor"}, "prog": [None],
         "tracks": [{"name": "Rev", "kind": "drum", "voice": {"name": "drum_cymbal_open", "rate": -1}, "steps": "h..."},
                    {"name": "K", "kind": "drum", "voice": {"name": "bd_haus", "rate": 1}, "steps": "h..."}]}
    code = g.generate(p)
    assert "sample :drum_cymbal_open, amp: vel / 127.0 * 3, rate: -1" in code
    assert "sample :bd_haus, amp: vel / 127.0 * 3\n" in code   # rate 1 は出さない


def test_pitch_bend_note_is_kept_and_generated():
    proj = {"bpm": 120, "bars": 2, "tracks": [
        {"id": "ld", "name": "ld", "kind": "melody", "voice": {"name": "saw"}, "notes": [[0, "c5", 2, 100, -12], [2, "c5", 2, 100]]}]}
    p = g.validate(proj)
    assert p["tracks"][0]["notes"][0] == [0, "c5", 2, 100, -12]
    code = g.generate(proj)
    assert "note_slide: g" in code and "control s, note: note(n) + bd" in code and "in_thread" in code


def test_fx_automation_generates_control_loop_and_slices():
    proj = {"bpm": 120, "bars": 4, "tracks": [
        {"id": "a", "name": "a", "kind": "melody", "voice": {"name": "saw"}, "notes": [[0, "c4", 1, 64]]},
        {"id": "f", "name": "f", "kind": "fx", "voice": {"name": "lpf"}, "targets": ["a"],
         "automation": {"param": "cutoff", "points": [[0, 50], [8, 130]]}}]}
    code = g.generate(proj)
    assert "cutoff: 50" in code and "cutoff_slide: d" in code and "|fx_f|" in code
    part = g.slice_project(proj, start_cell=16)   # 4 拍目(1 拍 = 4 マス)から
    assert part["tracks"][1]["automation"]["points"][0] == [0, 90]


def test_glide_slides_into_the_next_note():
    proj = {"bpm": 120, "bars": 2, "tracks": [
        {"id": "ld", "name": "ld", "kind": "melody", "voice": {"name": "prophet", "glide": 0.5},
         "notes": [[0, "c5", 2, 64], [2, "g5", 2, 64], [4, "g5", 1, 64]]}]}
    rows = g.bend_rows(g.validate(proj)["tracks"][0]["notes"], 0.5)
    assert rows[0][4:] == [7, 1.5, 0.5]   # c5 → g5 (+7)、最後の 0.5 拍で滑る
    assert rows[1][4] == 0 and rows[2][4] == 0   # 同じ音程の続き / 次がない音は滑らない


def test_record_video_flag_end_time():
    import record_video as rv
    times = [i / 30 for i in range(10)]
    counts = [0, 0, 80, 80, 80, 0, 0, 0, 0, 0]
    assert abs(rv.flag_end_time(counts, times) - 5 / 30) < 1e-9     # 最後に合図が見えたフレーム(4)の次
    with pytest.raises(ValueError):
        rv.flag_end_time([0] * 10, times)                             # 合図が一度も見えない
    with pytest.raises(ValueError):
        rv.flag_end_time([80] * 10, times)                            # 合図が消えない


def test_note_positions_keep_eighth_beat_resolution():
    proj = {"bpm": 120, "bars": 1, "tracks": [
        {"id": "p", "name": "p", "kind": "melody", "voice": {"name": "piano"}, "notes": [[2.125, "c5", 1.875, 64]]}]}
    assert g.validate(proj)["tracks"][0]["notes"][0] == [2.125, "c5", 1.875, 64]


def test_legacy_track_volume_migrates_to_notes_and_hits():
    def tr(kind, **kw):
        return g.validate({"bars": 1, "tracks": [{"id": "t", "kind": kind, "name": "t", **kw}]})["tracks"][0]
    t = tr("melody", voice={"name": "saw", "amp": 0.8}, notes=[[0, "c4", 1]])
    assert t["notes"] == [[0, "c4", 1, 34]] and "amp" not in t["voice"]     # 古い amp(0.8 ÷ 3 × 127)がノートに入る
    t = tr("melody", voice={"name": "saw", "velocity": 90}, notes=[[0, "c4", 1], [1, "d4", 1, 20]])
    assert [n[3] for n in t["notes"]] == [90, 20]                           # ノート自身のベロシティが優先
    assert g.vel_to_amp(127) == 3.0 and g.level_vel(g.vel_level(100)) in range(98, 103)
