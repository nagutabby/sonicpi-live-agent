# wav 音源(オーケストラなど)で stem を作る — AI エージェント向け資料

Sonic Pi 内蔵のシンセ・サンプルにない音(弦・金管・木管・ハープ・鐘など)は、**ユーザーが `work/samples/` に置いた wav** を `sample` で鳴らして使う。DAW(`scripts/daw_codegen.py`)が、wav のフォルダを「音程つきの楽器」として扱う。`work/` は git に入れないので、wav はリポジトリに含まれない(下の「入手元」から取り直す)。

## 使い方(stem・トラックに書く)

| 何を鳴らす | `kind` | `voice.name` | 書き方 |
|---|---|---|---|
| 音程つきの楽器(弦・管・ハープなど) | `bass` `chord` `melody` | `work/samples/<楽器フォルダ>`(リポジトリ直下からの相対パス。絶対パスでもよい) | `notes: [[拍, 音名, 長さ, ベロシティ], …]` |
| 1 つの音(ティンパニ・シンバルなど) | `drum` | `work/samples/<…>/<ファイル>.wav` | `hits: [[拍, ベロシティ], …]` |

- stem の例(`stems/ai_orch_violins_swell.json`): `{"name": "ヴァイオリン群(膨らむ和音)", "kind": "chord", "voice": {"name": "work/samples/violin_section", "amp": 1.06, "pan": -0.25, "cutoff": 110, "env": "swell"}, "description": "…", "source": "ai"}`
- **鳴らし方**: 音名ごとに、フォルダの中でいちばん近い音の wav を選び、`rate: 2**((音 - 基準音) / 12.0)` で音程をずらして鳴らす。長さは `sustain`(ノートの長さ)、`env`(`pluck stab pad swell`)は attack / release、`cutoff` は `sample` の `cutoff`、音量は `amp × ベロシティ ÷ 60`。
- **FX**: `fx` トラックの `targets` にそのトラックの id を書くと、リバーブなどがかかる(`with_fx` の中で鳴る)。
- **検証**: `uv run scripts/daw_codegen.py stems`(stem の検証。フォルダがないと、その stem は一覧に出ない)→ `check <曲>` → `export <曲>` → `live_check.py`。

## フォルダの条件(新しい楽器を足すとき)

- `work/samples/<楽器>/` の中(サブフォルダも可)に `.wav` を置く。**ファイル名を `_` で区切った 1 語が音名**になっていること(`A#3` `Bb2` `C4` のような、音名 + `#`/`b` + オクターブ)。例: `VlnEns_susVib_A2_v1.wav` → A2。`v1` `rr1` `sus` などは音名として読まれない。
- **1 つのフォルダには、1 つの奏法・1 つの強さだけ**を入れる(同じ音の wav が複数あると、名前順で最初の 1 つだけが使われる)。スタッカートとサステインは別フォルダにする。
- 音名がないファイル(ティンパニ・打楽器)はフォルダにせず、`drum` の `voice.name` に wav のパスを直接書く。
- 離れた音は `rate` でずらすので、基準音から遠いほど音色が変わる(ハープは 2〜3 半音おき、弦は 3 半音前後おきの wav がある)。極端な高音・低音は避ける。

## いま入れてある楽器(`work/samples/`。ユーザーの環境の一例)

| フォルダ | 音域 | 備考 | 入手元 |
|---|---|---|---|
| `violin_section` `viola_section` `cello_section` `contrabass` | g2〜d5 / c2〜d5 / c1〜f4 / fs0〜b2 | 弦(ビブラートあり。持続音) | VSCO 2 CE |
| `horn` `trumpet` `trombone` `tuba` | a0〜f4 / f2〜c5 / bb0〜f3 / f0〜d3 | 金管(持続音) | VSCO 2 CE |
| `flute` `oboe` `clarinet` | c3〜c6 / bb2〜f5 / d2〜fs5 | 木管(フルートとオーボエはビブラート。クラリネットは長い音) | VSCO 2 CE |
| `harp` | e1〜f7 | f と mf が混在(f が優先される) | VCSL |
| `glockenspiel` `tubular_bells` | g4〜c7 / c3〜e4 | 鐘・きらめき(グロッケンは medium、ベルは強さが混在) | VCSL |
| `pipe_organ` | c1〜c6 | 厚い持続音(Quiet の鍵盤) | VCSL |
| `timpani` | 音名なし | `Timpani1`〜`4` の打音 1 つずつ。`drum` で使う | VCSL |

この表は一例。実際の中身は `ls work/samples` と、`daw_codegen.sample_pitches("work/samples/<楽器>")`(音名と wav の一覧)で確かめる。

## 作ってある stem(`stems/ai_orch_*.json` と FX)

弦 `violins_swell` `violas_pad` `cellos_pad` `contrabass_pedal` `violin_lead` `cello_melody` / 木管 `flute` `oboe` `clarinet` / 金管 `horn_pad` `trombone_pad` `tuba_bass` `trumpet` / 色彩 `harp` `glockenspiel` `tubular_bells` `pipe_organ` / 打楽器 `timpani_a` `timpani_b` / FX `ai_fx_reverb_mist`(霧のリバーブ)`ai_fx_echo_ripple`(さざ波のエコー)`ai_fx_tremolo_shimmer`(トレモロ)。印象派・アートコア向けの使い方は、各 stem の `description` に書いてある。

## 入手元とライセンス(ユーザーが自分でダウンロードする。AI は取得しない)

| 素材 | 取得 | ライセンス | 中身 |
|---|---|---|---|
| **VCSL**(Versilian Community Sample Library) | `git clone --depth 1 https://github.com/sgossner/VCSL ~/vcsl`(約 9.5GB) | CC0 | ハープ・ピアノ・オルガン・鐘・ティンパニ・打楽器・民族楽器。弦・金管・フルート類はない |
| **VSCO 2 Community Edition**(Versilian Studios) | `git clone --depth 1 https://github.com/sgossner/VSCO-2-CE ~/vsco`(約 5GB) | CC0 | 弦・金管・木管・打楽器・鍵盤(`Strings/` `Brass/` `Woodwinds/` など) |

- 使う楽器だけを `work/samples/<名>/` にコピーする(全部は入れない。サイズが大きい)。1 奏法・1 強さに絞る(例: 弦は `susvib` の `v1` だけ)。
- 公開するときは、素材名(VCSL / VSCO 2 CE、Versilian Studios)をクレジットすると親切(CC0 なので必須ではない)。他の素材(Sonatina Symphonic Orchestra は CC Sampling Plus 1.0、Philharmonia Orchestra は MP3 で「そのまま」の再配布不可)を使うときは、ライセンスをユーザーと確認する。
- **AGENTS.md の守ること**: ユーザーが用意した wav だけを扱う。外部の音源を AI が勝手に取ってこない。他人の旋律・音声を複製しない。
