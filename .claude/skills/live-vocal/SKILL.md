---
name: live-vocal
description: NEUTRINO(Tau)で歌詞つきの歌声を作り、必要なら調声して、Sonic Pi に載せるボーカルのステムを作る。『ボーカルを足して』『歌わせて』『歌詞を書いて』と言われたとき。
---

AGENTS.md「ボーカル」節、`docs/lyric-guide.md`(歌詞)、`docs/vocal-tuning.md`(調声)に従う。1回に1フレーズ(4〜8小節)。案を求められたら**5案**(別の歌詞/旋律/モデル・スタイルシフト/ハモリ/刻み方)。具体的な指示(「上ハモリを追加」「サポートモデルを SOMA に」)は、案を出さずに実行する。NEUTRINO は CPU を使うので、5案のうち実際に歌わせるのは、ユーザーが選んだ案(または違いの大きい案)に絞ってよい。ボコーダーなどで声を機械的にしない。

1. `work/current.rb` からキー・BPM・コード進行・展開(どこで鳴らすか)を読み取る(推測しない)。読み取れなければ聞く。歌詞のテーマや言葉があれば本人に聞く(なければ短い案を出す)。
2. 歌詞(ひらがな、発音どおり)とメロディを `work/vocals/NN_<label>.json` に書く(コードトーン中心、MIDI 55〜72、音符は小節をまたがず、またぐ音は `tie`、息継ぎは `br`、合計は小節数×4拍)。
3. `uv run scripts/lyric_check.py work/vocals/NN_<label>.json`。終了コード 2 は直す。警告(細かい休符・ブレスなしの長いフレーズなど)は結果をそのまま伝え、直すか聞く。
4. 実行前に「NEUTRINO を動かす(音は鳴らない・CPU を使う)」と一言伝える。`uv run scripts/neutrino_sing.py work/vocals/NN_<label>.json [--model M] [--support S] [--style-shift K]`。出力は `NN_<label>_vN.*` と `_clip.wav`。
5. 気になる箇所は、まず**リテイク**(同じコマンドをもう一度。版が進む)と `--style-shift`・`--support` の違いを聴き比べる。音程・子音だけ直すときは `uv run scripts/neutrino_tune.py work/vocals/NN_<label>_vN --preset natural`。数値(音高のずれ・4kHz 以上の比)を読み、足りなければパラメータを**1つだけ**動かして作り直す(版は進み、上書きしない)。
6. `proposals/NN_vocal_*.rb` に `live_loop`(`sample "<絶対パス>/..._clip.wav"` を拍数だけ `sleep`、`arr` や展開に合わせて鳴らす位置を決める)を書き、`live_check.py` を通す。重ねた録音は、録音前に一言断る。`wav_stats.py` でピークと長さを確認する。
7. 解説(歌詞のはまり・母音の響き・子音の位置・既存ステムとの帯域)、聴く箇所(秒)、試せる課題を1つ添える。採否を聞き、採用なら `work/notes.md` に追記し、`learning-log` スキルで学習ログに追記する(歌詞の工夫・ブレス・タイ・スタイルシフト・調声のパラメータなど)。
8. 歌詞は日本語(かな)のみ。英語の響きが欲しいときは、かな近似にして聴き比べる。
