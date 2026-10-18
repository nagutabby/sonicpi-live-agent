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
         "notes": [[0, "eb4", 0.5], [1.5, "gb4", 1], [9, "bb4", 2]]},
    ],
}


def test_generate_is_valid_sonicpi(tmp_path):
    import subprocess
    import sys
    code = g.generate(PROJ)
    assert "live_loop :kick do grid_play voice_kick, pat_kick end" in code
    # 古い形式のグリッド(bass / chord)は、コード進行から音程つきの音に直る
    assert "notes_bass = [[0, :eb2, 4]" in code
    assert "notes_keys = [[0, :eb4, 0.75], [0, :fs4, 0.75]" in code
    assert "notes_lead = [[0, :eb4, 0.5], [1.5, :gb4, 1], [7.75, :bb4, 0.25]]" in code  # 曲の外の音は末尾に丸める
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
    assert pr["project"]["tracks"][0]["voice"]["name"] == "bd_haus" and pr["project"]["tracks"][0]["steps"].startswith("X...")
    assert pr["project"]["tracks"][3]["notes"] and not any(t["mute"] or t["solo"] for t in pr["project"]["tracks"])
    assert pr["project"]["prog"] == [["eb", "minor7"], ["bb", "dom7"]]
    for bad in ({"name": "", "project": PROJ}, {"name": "x", "project": {"tracks": [{"kind": "drum", "voice": {"name": "nope"}}]}}):
        with pytest.raises(ValueError):
            g.validate_preset(bad)


def test_no_velocity_all_hits_are_X():
    p = {**PROJ, "tracks": [{"id": "k", "kind": "drum", "voice": {"name": "bd_haus"}, "steps": "Xxo5 .-.. ...."}]}
    assert g.validate(p)["tracks"][0]["steps"].startswith("XXXX.-..")
    assert 'pat_k = "XXXX .-.. .... .... | ' in g.generate(p)


def test_stem_source_ai_is_kept_and_default_user():
    base = {"name": "S", "kind": "bass", "voice": {"name": "sine"}}
    assert g.validate_stem({**base, "source": "ai"})["source"] == "ai"
    assert g.validate_stem(base)["source"] == "user"
    assert g.validate_stem({**base, "source": "<script>"})["source"] == "user"


# ---- エフェクト(fx) ----
def fx_project(*fx):
    music = [{"id": "kick", "kind": "drum", "voice": {"name": "bd_haus"}, "steps": "X..." * 4},
             {"id": "bass", "kind": "bass", "voice": {"name": "sine"}, "notes": [[0, "c2", 1]]}]
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
