# 学習ログ

案を採用したあと、**音楽理論に基づく意味と、使った技法・用語**を1案ごとに残す記録。曲(`work/`)を入れ替えても残り、後から検索できる。

- 探す: `uv run scripts/learning_log.py search サイドチェイン`(または `grep -n '#sidechain' docs/learning-log.md`)。タグは日本語名と英語名の両方を付けてある。
- 追記する人: エージェント(スキル `learning-log`)。「決めた人」と「関連」も必ず書く。ユーザーが案を採用したとき、最終レビューのとき。スタイル②(AI が書く)では、AI が書いたコードに使った全技法・用語を書く。
- 追記したら `uv run scripts/learning_log.py index` で、下の索引を作り直す。
- 理論の辞書は [music-theory.md](music-theory.md)、技法は [live-coding.md](live-coding.md)、基本用語は [glossary.md](glossary.md)。

## エントリの書式
```markdown
### L0xx 短い題
- タグ: #日本語名 #english-name …
- 日付 / 曲: YYYY-MM-DD / 曲名(`songs/….rb` の `live_loop :名前` など)
- 決めた人: 誰がこの選択をしたか(下の凡例)
- 選んだ案: 何を選んだか(選ばなかった案との違いを1行)
- コード: 該当部分の抜粋(数行)
- 意味(理論): なぜそう聞こえるか。度数・コード機能・リズムの位置・音域・倍音・帯域
- 数値: `amp`・`cutoff`・`sleep`・測った値(未確認のことは「未確認」)
- 聴きどころ: 何秒付近で何を聴くか
- 課題: 自分で試せること(1つ)
- 関連: 関連するエントリ(L0xx)
```

**「決めた人」の凡例**(後から、人の判断と AI の判断を区別するため。公開時の説明にも使える)
| 表記 | 意味 |
|---|---|
| ユーザーが選んだ | AI の5案(または3案)から、ユーザーが選んだ |
| ユーザーの指示 | ユーザーが「〜して」と具体的に指示し、AI が実装した |
| AI が決めた | ユーザーの指示のない部分を、AI が判断した(ユーザーは未確認) |

## 索引
<!-- INDEX:START -->
**エントリ一覧**

| 番号 | 題 | タグ |
|---|---|---|
| L001 | ハーフタイムのドラム | #ハーフタイム #half-time #バックビート #backbeat #16分グリッド #キック #kick #スネア #snare |
| L002 | ハットの強弱と3連ロール | #ハイハット #hi-hat #ベロシティ #velocity #amp #強弱 #3連符 #triplet #ロール #roll |
| L003 | 単音のサブベースリフ(グルーヴ先行) | #サブベース #sub-bass #ベースリフ #bass-riff #グルーヴ先行 #groove-first #キックとベースの位置 #sine |
| L004 | サイドチェイン風の沈み(ダッキング) | #サイドチェイン #sidechain #ダッキング #ducking #control #amp_slide #キックからの距離 |
| L005 | ワブル(cutoff の LFO) | #ワブル #wobble #LFO #cutoff #supersaw #detune #res #ローパスフィルター |
| L006 | シンコペーション(3-3-2、付点8分) | #シンコペーション #syncopation #付点8分 #dotted-eighth #3-3-2 #拍の裏 #ノリ |
| L007 | 区間ごとのコード進行(ローマ数字・機能) | #コード進行 #chord-progression #ローマ数字 #roman-numeral #i-VI-III-VII #V7 #ドミナント #dominant #解決 #resolution #平行調 #セクション #トニック #サブドミナント |
| L008 | ワブルをメロディにする(1音を伸ばす・グライド・導音) | #メロディ #melody #コードトーン #chord-tone #導音 #leading-tone #note_slide #グライド #glide #ポルタメント #portamento |
| L009 | オクターブ重ね(レイヤー)とステレオ幅 | #オクターブ重ね #layering #レイヤー #pan #ステレオ幅 #stereo-width #左右相関 #パッド #dsaw |
| L010 | ビルドアップ(riser・ロールの加速・4つ打ち) | #ビルドアップ #build-up #riser #ライザー #スネアロール #snare-roll #ハイパスフィルター #cutoff_slide #クラッシュ #crash #4つ打ち |
| L011 | ドロップ前の無音(間) | #間 #無音 #休符 #rest #落差 #コントラスト #contrast #音を引く |
| L012 | ピアノを低音で支える(音域の住み分け・ローパス) | #音域の住み分け #range-separation #ローパス #lpf #ピアノ #piano #vel #hard #背後から支える |
| L013 | イントロのピアノ:トップノートから昇格(段階的な展開) | #段階的な展開 #トップノート #top-note #密度 #density #メロディ昇格 #イントロ |
| L014 | ビブラフォン風(pretty_bell + tremolo) | #ビブラフォン #vibraphone #tremolo #トレモロ #pretty_bell #reverb #リバーブ |
| L015 | clap の合成と帯域設計 | #clap #クラップ #ノイズ #noise #バンドパス #bandpass #rbpf #pnoise #帯域設計 #リバーブ #胴鳴り |
| L016 | EQ で重みを出す・声との被りを削る | #EQ #イコライザー #equalizer #low_shelf #high_shelf #マスキング #masking #帯域 #試験録音 |
| L017 | ボコーダーの声(NEUTRINO + 調声 + DSP ボコーダー) | #ボコーダー #vocoder #フォルマント #formant #母音 #vowel #NEUTRINO #調声 #pitch-lock #smooth #glide-ms #歌声合成 |
| L018 | ハモリ(3度上・3度下) | #ハモリ #harmony #3度 #third #コードトーン #上ハモリ #下ハモリ |
| L019 | 声を刻む・全員で刻む(tutti) | #刻み #chop #tutti #ユニゾン #unison #アクセント #accent #start-finish #スライス |
| L020 | 区間の管理(on_air・小節の表・plan) | #on_air #小節の表 #構成管理 #live_loop #sleep #plan #区間 #define |
| L021 | 音量管理と試験録音(drop_gain・ピーク) | #ゲインステージング #gain-staging #peak #ピーク #RMS #drop_gain #試験録音 #wav_stats #ヘッドルーム |
| L022 | 権利と配布(CC0・NEUTRINO・MIT / CC BY) | #ライセンス #license #CC0 #NEUTRINO規約 #CC-BY #MIT #配布 |
| L023 | 付点で跳ねるキック(ハーフタイムの土台) | #キック #kick #付点8分 #dotted-eighth #シンコペーション #syncopation #ハーフタイム #half-time #bd_tek #16分グリッド #3-3-2 |
| L024 | Pad と借用和音 IV(近接転回・supersaw・ロングテイル) | #パッド #pad #supersaw #借用和音 #borrowed-chord #近接転回 #voice-leading #ナチュラルマイナー #natural-minor #コード進行 #chord-progression #リバーブ #reverb #ロングテイル #long-tail #env-pad #cutoff #detune |
| L025 | ロングテイルのスネア(ハーフタイムの3拍目 + 深いリバーブ) | #スネア #snare #ハーフタイム #half-time #バックビート #backbeat #リバーブ #reverb #ロングテイル #long-tail #damp #hpf #sn_dolf |
| L026 | キックに揃えた saw ベース(bass b) | #ベース #bass #saw #キックとベースの位置 #キックロック #kick-lock #env-stab #cutoff #res #fold #grid_prog #根音 #root |
| L027 | サイン波のサブベース(根音ロング) | #サブベース #sub-bass #sine #サイン波 #根音 #root #fold #低域 #音域の住み分け #range-separation #ヘッドルーム |
| L028 | サイドチェイン風の沈み(Pad と sub、キック引き金) | #サイドチェイン #sidechain #ダッキング #ducking #level #control #amp_slide #in_thread #キックからの距離 #キックとベースの位置 #ゲインステージング |
| L029 | イントロ:Pad だけ・拍を一部無音・少しずつ強く | #イントロ #intro #パッド #pad #間 #無音 #休符 #rest #フェードイン #fade-in #段階的な展開 #近接転回 #voice-leading #cutoff #コード進行 #chord-progression #セクション |
| L030 | ビルド:目覚め・リードのパワーコード・ピッチドロップと無音の拍 | #ビルドアップ #build-up #ピッチドロップ #pitch-drop #間 #無音 #rest #パワーコード #power-chord #リード #lead #dsaw #attack #time_warp #キックの重ね #kick-layer #ロー・タム #low-tom #cutoff #近接転回 #voice-leading #ゲインステージング |
| L031 | ハイハット:16分の強弱(x・o) | #ハイハット #hi-hat #ベロシティ #velocity #amp #強弱 #16分グリッド #ノリ #hat_snap #hpf #pan #音域の住み分け |
| L032 | 低音ピアノ:キックに揃えたスタブ | #ピアノ #piano #低音ピアノ #伴奏 #スタブ #stab #キックロック #kick-lock #vel #hard #音域の住み分け #range-separation #ゲインステージング |
| L033 | 弦楽器のグライド + supersaw の伸ばし(コール&レスポンス) | #弦楽器 #strings #グライド #glide #ポルタメント #portamento #レガート #legato #コール&レスポンス #call-and-response #supersaw #blade #note_slide #control #サイドチェイン #sidechain #ビブラート #vibrato #メロディ #melody |
| L034 | グリッチのスタッター(フィル) | #フィル #fill #グリッチ #glitch #スタッター #stutter #rate #finish #hat_snap #アクセント #つなぎ |
| L035 | Solo Violin + Cello のハモリ(強弱・swell・深いリバーブ) | #ヴァイオリン #violin #チェロ #cello #ハモリ #harmony #3度 #third #強弱 #ダイナミクス #dynamics #swell #クレッシェンド #crescendo #ビブラート #vibrato #vibrato_delay #リバーブ #reverb #blade #音域の住み分け #range-separation |
| L036 | ブレイク:静かに浮く・期待を作る・リバースキックと無音の拍 | #ブレイク #breakdown #セクション #間 #無音 #rest #リバースキック #reverse-kick #riser #ライザー #クレッシェンド #crescendo #期待 #低音ピアノ #piano #近接転回 #voice-leading #コード進行 #chord-progression #コントラスト |
| L037 | 低いタムのゴースト(パーカッション、ドロップB) | #パーカッション #percussion #ゴーストノート #ghost-note #タム #tom #コンガ #rate #隠し味 #ドロップB #ベロシティ #velocity |
| L038 | glitch のアクセント(4小節の終わりの3連打) | #グリッチ #glitch #アクセント #accent #rate #32分音符 #連打 #FX #ドロップB #引き算 #少なさ |
| L039 | 音をリズミカルに刻んでドロップへ向かう(ピッチドロップの置き換え) | #リズミカルな刻み #rhythmic-chop #ビルドアップ #build-up #加速 #acceleration #16分 #supersaw #stab #つなぎ #ドロップ前 #クレッシェンド #crescendo |
| L040 | 曲全体のチョップ(スライサー)+ 直前の glitch アクセント | #チョップ #chop #スライサー #slicer #ゲート #gate #with_fx #phase #加速 #acceleration #glitch #アクセント #accent #ビルドアップ #build-up #ドロップ前 #in_thread #control |
| L041 | 9度のテンション(長い音の最高音として足す) | #9度 #ninth #テンション #tension #ナインス #9th #トップノート #top-note #コードトーン #chord-tone #ダブルストップ #double-stop |
| L042 | ビルドアップ:stem を2小節ごとに増やす・ライザー・弦の段階的な増音 | #ビルドアップ #build-up #ライザー #riser #ノイズ #noise #rlpf #cutoff_slide #stem追加 #段階的な展開 #クレッシェンド #crescendo #チョップ #slicer #glitch |
| L043 | チップ系リード + アルペジオ(glitch との相性) | #チップチューン #chiptune #chiplead #矩形波 #square-wave #アルペジオ #arpeggio #スタッカート #staccato #glitch #パン #pan #散りばめる |
| L044 | 曲全体の組み立て(define と in_thread)と、最後の音を伸ばし切る | #曲全体の組み立て #song-assembly #define #in_thread #set #get #time-state #変数のスコープ #sustain #release #伸ばし切る #録音スクリプト |
| L045 | ボーカルチョップ(NEUTRINO → 調声 → ボコーダー → 16分チョップ) | #ボーカルチョップ #vocal-chop #ボコーダー #vocoder #NEUTRINO #調声 #pitch-lock #grid_chop #from #16分 #フォルマント #formant #母音 #vowel #歌声合成 #アルペジオに重ねる |
| L046 | chiptune の高音を EQ で削る・音量とリバーブの微調整 | #EQ #イコライザー #equalizer #high_shelf #ハイシェルフ #chiptune #帯域 #reverb #amp #微調整 #試験録音 |
| L047 | Dark Bass へ: 低音管楽器のスタッカート・1オクターブ上の pad・9度つきの pluck | #低音管楽器 #brass #スタッカート #staccato #gate #オクターブ上のpad #pluck #9th #ナインス #EQ #high_shelf #bass-extension #サイドチェイン #amp #cutoff |
| L048 | ドロップのリードシンセ: 音階を1〜2度ずつ進み、音が短くなって、サブドミナントで終わる | #リードシンセ #dsaw #パワーコード #音階 #scale #ナチュラルマイナー #サブドミナント #subdominant #緊張感 #音価 #note-length #トップノート |
| L049 | 808 キックの 3-3-2(Dark Future Bass x Phonk のステップ1) | #808 #bd_808 #キック #kick #3-3-2 #シンコペーション #syncopation #ローパス #lpf #ハーフタイム #half-time #サブ低音 #sub-bass |
| L050 | フィンガースナップのスネア: 3拍目だけ + 弱い EQ で低域寄りに | #スネア #snare #フィンガースナップ #finger-snap #perc_snap #EQ #eq #low_shelf #high_shelf #ハーフタイム #half-time #音色の置き換え |
| L051 | 8分のハット: 強弱だけで刻む（x.o.） | #ハイハット #hi-hat #8分音符 #eighth-notes #ベロシティ #velocity #強弱 #hat_snap #lpf #ローパス |
| L052 | ベース: サブ + 鋸波の2層で、i - bVI - bIII - bVII の根音を弾く | #ベース #bass #サブベース #sub-bass #サイン波 #sine #鋸波 #saw #コード進行 #chord-progression #ナチュラルマイナー #natural-minor #アタックとリリース #attack-release #キックとベースの位置 #fold |
| L053 | コード: スタブ + セカンダリードミナント(Db7)+ 4小節目をマイナー化(Dbm7) | #コード #chords #supersaw #スタブ #stab #セカンダリードミナント #secondary-dominant #共通音保持 #common-tone #マイナー化 #minor #借用和音 #borrowed-chord #モーダルミクスチャー #7th #9th |
| L053 | コードのスタブ: Ebm9 → Cbmaj7 → Gbmaj7 → Dbm7 と、2小節目後半の Db7 | #コード #chords #スタブ #stab #supersaw #スーパーソウ #共通音保持 #common-tone #セカンダリードミナント #secondary-dominant #属七 #Db7 #9th #ナインス #grid_prog #chord_true |
| L054 | メロディ: 山なりの2小節フレーズを繰り返し、最後の1音だけ変える(grid_repeat_phrase) | #メロディ #melody #山なり #arch #反復 #repetition #変化 #variation #カウンターメロディ #counter-melody #溜め #tame #跳ね #swing #付点 #dotted #息継ぎ #breath #疲労度 #fatigue-score #supersaw #grid_repeat_phrase |
| L055 | ベース進行: i – bVI – iv – V7(Eb – Cb – Ab – Bb)で暗くし、ベースを -6dB | #コード進行 #chord-progression #属七 #dominant #V7 #ハーモニックマイナー #harmonic-minor #セカンダリードミナント #secondary-dominant #音量バランス #mix-balance |
| L056 | メロディ: 同じ音の連打 + 一部を削るシンコペーション + クリシェ(Eb → D → Db → C) | #メロディ #melody #クリシェ #cliche #シンコペーション #syncopation #連打 #repetition #phonk #dsaw #溜め #tame #grid_dotted #grid_repeat_phrase #疲労度 #fatigue-score |
| L057 | glitch: 小節の最後の1拍で和音を16分にこま切れ | #glitch #グリッチ #スタッター #stutter #コード #chords #supersaw #cut #深み |
| L058 | カウンターメロディ(ロングトーン)+ メロディを4音に + リバーブ + サブベース・EQ | #カウンターメロディ #counter-melody #ロングトーン #long-tone #リバーブ #reverb #EQ #eq #サブベース #sub-bass #音量バランス #mix-balance #シンコペーション #syncopation |
| L059 | 808 スライド(5度の跳ね)+ メロディのオクターブ重ね | #808 #スライド #slide #ポルタメント #portamento #note_slide #control #オクターブ重ね #octave-doubling #ベース #bass #メロディ #melody |
| L060 | メロディの試行と撤去: 9th の追加と削除・全音の山・問いと答えの削除・高音ピアノ → 低音ピアノのリフへ | #メロディ #melody #9th #ナインス #テンション #tension #半音 #semitone #全音 #whole-tone #トリル #trill #call-and-response #問いと答え #サブドミナント #subdominant #カウベル #cowbell #ピアノ #piano |
| L061 | 低音ピアノのリフ + 1オクターブ上のピアノ + ベロシティ・リバーブ | #ピアノ #piano #リフ #riff #ベロシティ #velocity #リバーブ #reverb #オクターブ重ね #octave-doubling #パワーコード風 #5度 #fifth #グリッド #grid_each #溜め #tame |
| L062 | キック: 3層(bd_klub + bd_haus + bd_boom)+ リバースキック | #キック #kick #強いキック #bd_klub #bd_haus #bd_boom #リバースキック #reverse-kick #逆再生 #rate #sample_duration #ヘッドルーム #headroom #音量バランス #mix-balance |
| L063 | vox(ボーカルチョップ風)+ ディストーション + EQ | #vox #ボーカルチョップ #vocal-chop #フォルマント #formant #grid_vsing #ディストーション #distortion #EQ #eq #リバーブ #reverb #パン #pan #16分 #配置 |
| L064 | ベースと glitch のディストーション | #ディストーション #distortion #ベース #bass #サブベース #sub-bass #サイン波 #sine #倍音 #harmonics #glitch #グリッチ #amp #distort |
| L065 | パワーコードのペダルポイント | #パワーコード #power-chord #ペダルポイント #pedal-point #ディストーション #distortion #dsaw #ブリッジミュート #palm-mute #5度 #オクターブ |
| L066 | 疑似サイドチェイン + 先読みの調整 | #サイドチェイン #sidechain #level #amp_slide #control #ダッキング #ducking #set_sched_ahead_time #timing #キック #kick |
| L067 | 曲の構成: セクションごとにステムを切り替える(grid_gate)と 64小節の並び | #構成 #structure #セクション #section #イントロ #intro #ビルドアップ #build-up #ドロップ #drop #ブレイク #break #アウトロ #outro #grid_gate #tick #コード進行 #chord-progression |
| L068 | 土台と上モノ + ドロップ内で音を止める(4・8小節ごと) | #土台 #foundation #上モノ #top-layer #レイヤー #layer #無音 #silence #ブレイク #break #インパクト #impact #with_fx #level #control |
| L069 | ドロップ前: ライザーなしの静寂 + ハットの 16分への盛り上げ | #ドロップ前 #pre-drop #静寂 #silence #ハイハット #hi-hat #16分 #sixteenth #ロール #roll #クレッシェンド #crescendo #逆再生キック #reverse-kick |
| L070 | ピアノのリフ 16小節ループ(A → A' → B → C) | #ピアノ #piano #リフ #riff #16小節 #phrase #フレーズ #反復と変化 #variation #grid_song_rel |
| L071 | ドロップの2周と、楽器を少しずつ足す(32小節の山) | #ドロップ #drop #段階的な展開 #layering #レイヤー #密度 #density #繰り返しと変化 #variation |
| L072 | ドロップ前の「波打つローパス」と無音の1拍・riser・リバース | #ローパスフィルター #lpf #オートメーション #automation #riser #ライザー #リバースシンバル #reverse-cymbal #リバースキック #間 #無音 #フィル #fill |
| L073 | ゴーストノートとキックの細分化(シンコペーションの勢い) | #ゴーストノート #ghost-note #シンコペーション #syncopation #キック #kick #スネア #snare #ハイハット #hi-hat #ベロシティ #amp #16分グリッド |
| L074 | ピアノの9thと、高音のアルペジオ | #9th #テンション #tension #4和音 #アルペジオ #arpeggio #ピアノ #piano #コードトーン #chord-tone #音域の住み分け #オクターブ重ね |
| L075 | グライド・ピッチベンド・パラメータのオートメーション | #グライド #glide #ポルタメント #portamento #ピッチベンド #pitch-bend #オートメーション #automation #control #slide |
| L076 | prophet の3度下ハモリ | #ハモリ #harmony #3度 #third #下ハモリ #コードトーン #chord-tone #prophet #音階 #scale |
| L077 | パワーコードを最後のドロップだけで(重ならない・長さをそろえる) | #パワーコード #power-chord #ディストーション #distortion #シンコペーション #syncopation #重なり #tri #音を引く |
| L078 | 海と空の glitch(ノイズ + ビットクラッシャー) | #グリッチ #glitch #ノイズ #noise #bnoise #cnoise #ビットクラッシャー #bitcrusher #テクスチャ |
| L079 | イントロのローパスと低音ピアノ・アウトロの閉じ方 | #ローパスフィルター #lpf #オートメーション #automation #イントロ #アウトロ #outro #フェードアウト #音域の住み分け #ピアノ #piano |
| L080 | 同時に読み込めないとき: with_fx を in_thread で包む(技術メモ) | #in_thread #too-far-behind #sched_ahead #スレッド #with_fx #再生トラブル |
| L081 | ハーフタイムのキック(0・2拍。暗い artcore の土台) | #ハーフタイム #half-time #キック #kick #ベロシティ #velocity #隙間 #space |
| L082 | スネアとゴーストスネアを別トラックに分ける | #ゴーストノート #ghost-note #スネア #snare #ハーフタイム #half-time #トラック分け #ベロシティ #velocity |
| L083 | キックを軽く固い音に替える(bd_pure → bd_tek) | #キック #kick #音色選び #帯域 #low-end #アタック #attack #サンプル測定 |
| L084 | 3-3-2 のハット(跳ねるシンコペーション) | #3-3-2 #シンコペーション #syncopation #ハイハット #hi-hat #ベロシティ #velocity #グルーヴ #groove #ゴーストノート |
| L085 | ペダルポイントのイントロ + フリジアンのドロップ(低音ピアノのベタ打ち) | #ペダルポイント #pedal-point #フリジアン #phrygian #半音 #借用和音 #セクション構成 #導音 #leading-tone #低音ピアノ |
| L086 | ドロップの主旋律: 長い音のピアノ(余白で暗さを作る) | #主旋律 #melody #ロングトーン #long-tone #余白 #space #フリジアン #phrygian #導音 #leading-tone #ピアノ #piano |
| L087 | ヴァイオリンのメロディ2: ロングトーンとスタッカートの混合 | #ロングトーン #long-tone #スタッカート #staccato #対旋律 #counter-melody #3-3-2 #半音 #ヴァイオリン #violin #ベロシティ #velocity #コール&レスポンス |
| L088 | 低音ピアノを強音・弱音の2トラックに分け、スタッカートで細かく刻む | #スタッカート #staccato #強弱 #dynamics #ゴーストノート #ghost-note #アルペジオ #arpeggio #ベロシティ #velocity #トラック分け #16分 #ピアノ #piano |
| L089 | フルートのソロイントロ: 明るい機能和声から、マイナーとサスで暗くする | #ソロ #solo #レガート #legato #機能和声 #functional-harmony #sus4 #sus-to-tonic #マイナーの増加 #休符 #rest #リリース #release #分散和音 #arpeggio |
| L090 | つなぎ: 減七の橋とティンパニの心拍(イントロ → ビルドアップ) | #つなぎ #transition #減七和音 #diminished-seventh #ティンパニ #timpani #裏打ち #offbeat #クレッシェンド #crescendo #アウフタクト #anacrusis |
| L091 | コントラバスと sus・add9・m9 の曖昧な和声(声部づくり) | #コントラバス #contrabass #sus和音 #suspended #add9 #m9 #声部 #voicing #浮遊感 #floating #wav音源 #sampled-instrument |
| L092 | ストリングスのロングトーンの置き方(前方を長く、後ろは休符) | #ロングトーン #long-tone #休符 #rest #リリース #release #ヴィオラ #viola #sustain #wav-sustain |
| L093 | パッド(supersaw)とトレモロ、オクターブ下を重ねない深み | #パッド #pad #supersaw #ノコギリ波 #saw #ギザギザ #aliasing #トレモロ #tremolo #サイドチェイン #sidechain #attack |
| L094 | キックの跳ね(0・2.5・3.5)とキック・ティンパニの重ね | #キック #kick #シンコペーション #syncopation #レイヤー #layer #イコライザー #eq #lpf #ローパス #ティンパニ #timpani |
| L095 | ハットの駆け抜け・スネアの連打とシンコペーション | #ハイハット #hi-hat #16分音符 #sixteenth #シンコペーション #syncopation #スネアロール #snare-roll #3つ打ち #triple-hit |
| L096 | フルートの風(対旋律・スタッカートへの応答・下降) | #対旋律 #counter-melody #フルート #flute #コールアンドレスポンス #call-and-response #スタッカート #staccato #グライド #glide #ベンド #bend |
| L097 | 後半の構成: ドロップ2周目・ブレイク・ドロップ前半・最後のドロップ | #構成 #structure #ブレイク #break #ドロップ #drop #dim7 #diminished-seventh #導音 #leading-tone #ドミナント #dominant #ベロシティ #velocity #コードの置換 #chord-mapping |
| L098 | riser: ノイズのスウィープと弦のトレモロ、無音の拍 | #riser #ライザー #ノイズ #noise #ハイパス #hpf #オートメーション #automation #トレモロ奏法 #tremolo-strings #休符 #rest #リバーブ #reverb |
| L099 | アウトロ: コーラス風の進行から減らす(Dsus2・lpf 沈め) | #アウトロ #outro #サブドミナント #subdominant #sus2 #ローパス #lpf #オートメーション #automation #引き算 #subtractive-arrangement #A-フリジアン #phrygian |
| L100 | glitch の自作サンプルと、スライサー + スタッター | #グリッチ #glitch #ビットクラッシャー #bitcrusher #スライサー #slicer #スタッター #stutter #タイムストレッチ #time-stretch #atempo #自作サンプル #synthesized-sample |
| L101 | ピアノを wav(Knight)に替える、イントロのピアノ(3和音 + トップノートをなぞる + 9th) | #ピアノ #piano #wav音源 #sampled-instrument #アップライト #upright #9th #ninth #トップノート #top-note #追従 #follow #声部 #voicing |
| L102 | イントロの「暗闇に向かう」オートメーション(lpf と reverb の mix) | #オートメーション #automation #ローパス #lpf #リバーブ #reverb #mix #room #音色変化 #timbre-automation |

**タグ索引**(五十音・アルファベット順)

| タグ | エントリ |
|---|---|
| #16分 | L039, L045, L063, L069, L088 |
| #16分グリッド | L001, L023, L031, L073 |
| #16分音符 | L095 |
| #16小節 | L070 |
| #3-3-2 | L006, L023, L049, L084, L087 |
| #32分音符 | L038 |
| #3つ打ち | L095 |
| #3度 | L018, L035, L076 |
| #3連符 | L002 |
| #4つ打ち | L010 |
| #4和音 | L074 |
| #5度 | L061, L065 |
| #7th | L053 |
| #808 | L049, L059 |
| #8分音符 | L051 |
| #9th | L041, L047, L053, L053, L060, L074, L101 |
| #9度 | L041 |
| #A-フリジアン | L099 |
| #acceleration | L039, L040 |
| #accent | L019, L038, L040 |
| #add9 | L091 |
| #aliasing | L093 |
| #amp | L002, L031, L046, L047, L064, L073 |
| #amp_slide | L004, L028, L066 |
| #anacrusis | L090 |
| #arch | L054 |
| #arpeggio | L043, L074, L088, L089 |
| #atempo | L100 |
| #attack | L030, L083, L093 |
| #attack-release | L052 |
| #automation | L072, L075, L079, L098, L099, L102 |
| #backbeat | L001, L025 |
| #bandpass | L015 |
| #bass | L026, L052, L059, L064 |
| #bass-extension | L047 |
| #bass-riff | L003 |
| #bd_808 | L049 |
| #bd_boom | L062 |
| #bd_haus | L062 |
| #bd_klub | L062 |
| #bd_tek | L023 |
| #bend | L096 |
| #bitcrusher | L078, L100 |
| #blade | L033, L035 |
| #bnoise | L078 |
| #borrowed-chord | L024, L053 |
| #brass | L047 |
| #break | L067, L068, L097 |
| #breakdown | L036 |
| #breath | L054 |
| #build-up | L010, L030, L039, L040, L042, L067 |
| #call-and-response | L033, L060, L096 |
| #CC-BY | L022 |
| #CC0 | L022 |
| #cello | L035 |
| #chiplead | L043 |
| #chiptune | L043, L046 |
| #chop | L019, L040 |
| #chord-mapping | L097 |
| #chord-progression | L007, L024, L029, L036, L052, L055, L067 |
| #chord-tone | L008, L041, L074, L076 |
| #chord_true | L053 |
| #chords | L053, L053, L057 |
| #clap | L015 |
| #cliche | L056 |
| #cnoise | L078 |
| #common-tone | L053, L053 |
| #contrabass | L091 |
| #contrast | L011 |
| #control | L004, L028, L033, L040, L059, L066, L068, L075 |
| #counter-melody | L054, L058, L087, L096 |
| #cowbell | L060 |
| #crash | L010 |
| #crescendo | L035, L036, L039, L042, L069, L090 |
| #cut | L057 |
| #cutoff | L005, L024, L026, L029, L030, L047 |
| #cutoff_slide | L010, L042 |
| #damp | L025 |
| #Db7 | L053 |
| #define | L020, L044 |
| #density | L013, L071 |
| #detune | L005, L024 |
| #dim7 | L097 |
| #diminished-seventh | L090, L097 |
| #distort | L064 |
| #distortion | L063, L064, L065, L077 |
| #dominant | L007, L055, L097 |
| #dotted | L054 |
| #dotted-eighth | L006, L023 |
| #double-stop | L041 |
| #drop | L067, L071, L097 |
| #drop_gain | L021 |
| #dsaw | L009, L030, L048, L056, L065 |
| #ducking | L004, L028, L066 |
| #dynamics | L035, L088 |
| #eighth-notes | L051 |
| #env-pad | L024 |
| #env-stab | L026 |
| #EQ | L016, L046, L047, L050, L058, L063 |
| #eq | L050, L058, L063, L094 |
| #equalizer | L016, L046 |
| #fade-in | L029 |
| #fatigue-score | L054, L056 |
| #fifth | L061 |
| #fill | L034, L072 |
| #finger-snap | L050 |
| #finish | L034 |
| #floating | L091 |
| #flute | L096 |
| #fold | L026, L027, L052 |
| #follow | L101 |
| #formant | L017, L045, L063 |
| #foundation | L068 |
| #from | L045 |
| #functional-harmony | L089 |
| #FX | L038 |
| #gain-staging | L021 |
| #gate | L040, L047 |
| #get | L044 |
| #ghost-note | L037, L073, L082, L088 |
| #glide | L008, L033, L075, L096 |
| #glide-ms | L017 |
| #glitch | L034, L038, L040, L042, L043, L057, L064, L078, L100 |
| #grid_chop | L045 |
| #grid_dotted | L056 |
| #grid_each | L061 |
| #grid_gate | L067 |
| #grid_prog | L026, L053 |
| #grid_repeat_phrase | L054, L056 |
| #grid_song_rel | L070 |
| #grid_vsing | L063 |
| #groove | L084 |
| #groove-first | L003 |
| #half-time | L001, L023, L025, L049, L050, L081, L082 |
| #hard | L012, L032 |
| #harmonic-minor | L055 |
| #harmonics | L064 |
| #harmony | L018, L035, L076 |
| #hat_snap | L031, L034, L051 |
| #headroom | L062 |
| #hi-hat | L002, L031, L051, L069, L073, L084, L095 |
| #high_shelf | L016, L046, L047, L050 |
| #hpf | L025, L031, L098 |
| #i-VI-III-VII | L007 |
| #impact | L068 |
| #in_thread | L028, L040, L044, L080 |
| #intro | L029, L067 |
| #kick | L001, L023, L049, L062, L066, L073, L081, L083, L094 |
| #kick-layer | L030 |
| #kick-lock | L026, L032 |
| #layer | L068, L094 |
| #layering | L009, L071 |
| #lead | L030 |
| #leading-tone | L008, L085, L086, L097 |
| #legato | L033, L089 |
| #level | L028, L066, L068 |
| #LFO | L005 |
| #license | L022 |
| #live_loop | L020 |
| #long-tail | L024, L025 |
| #long-tone | L058, L086, L087, L092 |
| #low-end | L083 |
| #low-tom | L030 |
| #low_shelf | L016, L050 |
| #lpf | L012, L049, L051, L072, L079, L094, L099, L102 |
| #m9 | L091 |
| #masking | L016 |
| #melody | L008, L033, L054, L056, L059, L060, L086 |
| #minor | L053 |
| #MIT | L022 |
| #mix | L102 |
| #mix-balance | L055, L058, L062 |
| #natural-minor | L024, L052 |
| #NEUTRINO | L017, L045 |
| #NEUTRINO規約 | L022 |
| #ninth | L041, L101 |
| #noise | L015, L042, L078, L098 |
| #note-length | L048 |
| #note_slide | L008, L033, L059 |
| #octave-doubling | L059, L061 |
| #offbeat | L090 |
| #on_air | L020 |
| #outro | L067, L079, L099 |
| #pad | L024, L029, L093 |
| #palm-mute | L065 |
| #pan | L009, L031, L043, L063 |
| #peak | L021 |
| #pedal-point | L065, L085 |
| #perc_snap | L050 |
| #percussion | L037 |
| #phase | L040 |
| #phonk | L056 |
| #phrase | L070 |
| #phrygian | L085, L086, L099 |
| #piano | L012, L032, L036, L060, L061, L070, L074, L079, L086, L088, L101 |
| #pitch-bend | L075 |
| #pitch-drop | L030 |
| #pitch-lock | L017, L045 |
| #plan | L020 |
| #pluck | L047 |
| #pnoise | L015 |
| #portamento | L008, L033, L059, L075 |
| #power-chord | L030, L065, L077 |
| #pre-drop | L069 |
| #pretty_bell | L014 |
| #prophet | L076 |
| #range-separation | L012, L027, L032, L035 |
| #rate | L034, L037, L038, L062 |
| #rbpf | L015 |
| #release | L044, L089, L092 |
| #repetition | L054, L056 |
| #res | L005, L026 |
| #resolution | L007 |
| #rest | L011, L029, L030, L036, L089, L092, L098 |
| #reverb | L014, L024, L025, L035, L046, L058, L061, L063, L098, L102 |
| #reverse-cymbal | L072 |
| #reverse-kick | L036, L062, L069 |
| #rhythmic-chop | L039 |
| #riff | L061, L070 |
| #riser | L010, L036, L042, L072, L098 |
| #rlpf | L042 |
| #RMS | L021 |
| #roll | L002, L069 |
| #roman-numeral | L007 |
| #room | L102 |
| #root | L026, L027 |
| #sample_duration | L062 |
| #sampled-instrument | L091, L101 |
| #saw | L026, L052, L093 |
| #scale | L048, L076 |
| #sched_ahead | L080 |
| #secondary-dominant | L053, L053, L055 |
| #section | L067 |
| #semitone | L060 |
| #set | L044 |
| #set_sched_ahead_time | L066 |
| #sidechain | L004, L028, L033, L066, L093 |
| #silence | L068, L069 |
| #sine | L003, L027, L052, L064 |
| #sixteenth | L069, L095 |
| #sleep | L020 |
| #slicer | L040, L042, L100 |
| #slide | L059, L075 |
| #smooth | L017 |
| #sn_dolf | L025 |
| #snare | L001, L025, L050, L073, L082 |
| #snare-roll | L010, L095 |
| #solo | L089 |
| #song-assembly | L044 |
| #space | L081, L086 |
| #square-wave | L043 |
| #stab | L032, L039, L053, L053 |
| #staccato | L043, L047, L087, L088, L096 |
| #start-finish | L019 |
| #stem追加 | L042 |
| #stereo-width | L009 |
| #strings | L033 |
| #structure | L067, L097 |
| #stutter | L034, L057, L100 |
| #sub-bass | L003, L027, L049, L052, L058, L064 |
| #subdominant | L048, L060, L099 |
| #subtractive-arrangement | L099 |
| #supersaw | L005, L024, L033, L039, L053, L053, L054, L057, L093 |
| #sus-to-tonic | L089 |
| #sus2 | L099 |
| #sus4 | L089 |
| #suspended | L091 |
| #sustain | L044, L092 |
| #sus和音 | L091 |
| #swell | L035 |
| #swing | L054 |
| #syncopation | L006, L023, L049, L056, L058, L073, L077, L084, L094, L095 |
| #synthesized-sample | L100 |
| #tame | L054, L056, L061 |
| #tension | L041, L060, L074 |
| #third | L018, L035, L076 |
| #tick | L067 |
| #timbre-automation | L102 |
| #time-state | L044 |
| #time-stretch | L100 |
| #time_warp | L030 |
| #timing | L066 |
| #timpani | L090, L094 |
| #tom | L037 |
| #too-far-behind | L080 |
| #top-layer | L068 |
| #top-note | L013, L041, L101 |
| #transition | L090 |
| #tremolo | L014, L093 |
| #tremolo-strings | L098 |
| #tri | L077 |
| #trill | L060 |
| #triple-hit | L095 |
| #triplet | L002 |
| #tutti | L019 |
| #unison | L019 |
| #upright | L101 |
| #V7 | L007, L055 |
| #variation | L054, L070, L071 |
| #vel | L012, L032 |
| #velocity | L002, L031, L037, L051, L061, L081, L082, L084, L087, L088, L097 |
| #vibraphone | L014 |
| #vibrato | L033, L035 |
| #vibrato_delay | L035 |
| #viola | L092 |
| #violin | L035, L087 |
| #vocal-chop | L045, L063 |
| #vocoder | L017, L045 |
| #voice-leading | L024, L029, L030, L036 |
| #voicing | L091, L101 |
| #vowel | L017, L045 |
| #vox | L063 |
| #wav-sustain | L092 |
| #wav_stats | L021 |
| #wav音源 | L091, L101 |
| #whole-tone | L060 |
| #with_fx | L040, L068, L080 |
| #wobble | L005 |
| #つなぎ | L034, L039, L090 |
| #アウトロ | L067, L079, L099 |
| #アウフタクト | L090 |
| #アクセント | L019, L034, L038, L040 |
| #アタック | L083 |
| #アタックとリリース | L052 |
| #アップライト | L101 |
| #アルペジオ | L043, L074, L088 |
| #アルペジオに重ねる | L045 |
| #イコライザー | L016, L046, L094 |
| #イントロ | L013, L029, L067, L079 |
| #インパクト | L068 |
| #オクターブ | L065 |
| #オクターブ上のpad | L047 |
| #オクターブ重ね | L009, L059, L061, L074 |
| #オートメーション | L072, L075, L079, L098, L099, L102 |
| #カウベル | L060 |
| #カウンターメロディ | L054, L058 |
| #キック | L001, L023, L049, L062, L066, L073, L081, L083, L094 |
| #キックからの距離 | L004, L028 |
| #キックとベースの位置 | L003, L026, L028, L052 |
| #キックの重ね | L030 |
| #キックロック | L026, L032 |
| #ギザギザ | L093 |
| #クラッシュ | L010 |
| #クラップ | L015 |
| #クリシェ | L056 |
| #クレッシェンド | L035, L036, L039, L042, L069, L090 |
| #グライド | L008, L033, L075, L096 |
| #グリッチ | L034, L038, L057, L064, L078, L100 |
| #グリッド | L061 |
| #グルーヴ | L084 |
| #グルーヴ先行 | L003 |
| #ゲインステージング | L021, L028, L030, L032 |
| #ゲート | L040 |
| #コンガ | L037 |
| #コントラスト | L011, L036 |
| #コントラバス | L091 |
| #コード | L053, L053, L057 |
| #コードの置換 | L097 |
| #コードトーン | L008, L018, L041, L074, L076 |
| #コード進行 | L007, L024, L029, L036, L052, L055, L067 |
| #コール&レスポンス | L033, L087 |
| #コールアンドレスポンス | L096 |
| #ゴーストノート | L037, L073, L082, L084, L088 |
| #サイドチェイン | L004, L028, L033, L047, L066, L093 |
| #サイン波 | L027, L052, L064 |
| #サブドミナント | L007, L048, L060, L099 |
| #サブベース | L003, L027, L052, L058, L064 |
| #サブ低音 | L049 |
| #サンプル測定 | L083 |
| #シンコペーション | L006, L023, L049, L056, L058, L073, L077, L084, L094, L095 |
| #スタッカート | L043, L047, L087, L088, L096 |
| #スタッター | L034, L057, L100 |
| #スタブ | L032, L053, L053 |
| #ステレオ幅 | L009 |
| #スネア | L001, L025, L050, L073, L082 |
| #スネアロール | L010, L095 |
| #スライサー | L040, L100 |
| #スライス | L019 |
| #スライド | L059 |
| #スレッド | L080 |
| #スーパーソウ | L053 |
| #セカンダリードミナント | L053, L053, L055 |
| #セクション | L007, L029, L036, L067 |
| #セクション構成 | L085 |
| #ソロ | L089 |
| #タイムストレッチ | L100 |
| #タム | L037 |
| #ダイナミクス | L035 |
| #ダッキング | L004, L028, L066 |
| #ダブルストップ | L041 |
| #チェロ | L035 |
| #チップチューン | L043 |
| #チョップ | L040, L042 |
| #ティンパニ | L090, L094 |
| #テクスチャ | L078 |
| #テンション | L041, L060, L074 |
| #ディストーション | L063, L064, L065, L077 |
| #トップノート | L013, L041, L048, L101 |
| #トニック | L007 |
| #トラック分け | L082, L088 |
| #トリル | L060 |
| #トレモロ | L014, L093 |
| #トレモロ奏法 | L098 |
| #ドミナント | L007, L097 |
| #ドロップ | L067, L071, L097 |
| #ドロップB | L037, L038 |
| #ドロップ前 | L039, L040, L069 |
| #ナインス | L041, L047, L053, L060 |
| #ナチュラルマイナー | L024, L048, L052 |
| #ノイズ | L015, L042, L078, L098 |
| #ノコギリ波 | L093 |
| #ノリ | L006, L031 |
| #ハイシェルフ | L046 |
| #ハイハット | L002, L031, L051, L069, L073, L084, L095 |
| #ハイパス | L098 |
| #ハイパスフィルター | L010 |
| #ハモリ | L018, L035, L076 |
| #ハーフタイム | L001, L023, L025, L049, L050, L081, L082 |
| #ハーモニックマイナー | L055 |
| #バックビート | L001, L025 |
| #バンドパス | L015 |
| #パッド | L009, L024, L029, L093 |
| #パワーコード | L030, L048, L065, L077 |
| #パワーコード風 | L061 |
| #パン | L043, L063 |
| #パーカッション | L037 |
| #ビットクラッシャー | L078, L100 |
| #ビブラフォン | L014 |
| #ビブラート | L033, L035 |
| #ビルドアップ | L010, L030, L039, L040, L042, L067 |
| #ピアノ | L012, L032, L060, L061, L070, L074, L079, L086, L088, L101 |
| #ピッチドロップ | L030 |
| #ピッチベンド | L075 |
| #ピーク | L021 |
| #フィル | L034, L072 |
| #フィンガースナップ | L050 |
| #フェードアウト | L079 |
| #フェードイン | L029 |
| #フォルマント | L017, L045, L063 |
| #フリジアン | L085, L086 |
| #フルート | L096 |
| #フレーズ | L070 |
| #ブリッジミュート | L065 |
| #ブレイク | L036, L067, L068, L097 |
| #ヘッドルーム | L021, L027, L062 |
| #ベロシティ | L002, L031, L037, L051, L061, L073, L081, L082, L084, L087, L088, L097 |
| #ベンド | L096 |
| #ベース | L026, L052, L059, L064 |
| #ベースリフ | L003 |
| #ペダルポイント | L065, L085 |
| #ボコーダー | L017, L045 |
| #ボーカルチョップ | L045, L063 |
| #ポルタメント | L008, L033, L059, L075 |
| #マイナーの増加 | L089 |
| #マイナー化 | L053 |
| #マスキング | L016 |
| #メロディ | L008, L033, L054, L056, L059, L060 |
| #メロディ昇格 | L013 |
| #モーダルミクスチャー | L053 |
| #ユニゾン | L019 |
| #ライザー | L010, L036, L042, L072, L098 |
| #ライセンス | L022 |
| #リズミカルな刻み | L039 |
| #リバースキック | L036, L062, L072 |
| #リバースシンバル | L072 |
| #リバーブ | L014, L015, L024, L025, L035, L058, L061, L063, L098, L102 |
| #リフ | L061, L070 |
| #リリース | L089, L092 |
| #リード | L030 |
| #リードシンセ | L048 |
| #レイヤー | L009, L068, L071, L094 |
| #レガート | L033, L089 |
| #ロングテイル | L024, L025 |
| #ロングトーン | L058, L086, L087, L092 |
| #ローパス | L012, L049, L051, L094, L099, L102 |
| #ローパスフィルター | L005, L072, L079 |
| #ローマ数字 | L007 |
| #ロール | L002, L069 |
| #ロー・タム | L030 |
| #ワブル | L005 |
| #ヴァイオリン | L035, L087 |
| #ヴィオラ | L092 |
| #上ハモリ | L018 |
| #上モノ | L068 |
| #下ハモリ | L018, L076 |
| #主旋律 | L086 |
| #付点 | L054 |
| #付点8分 | L006, L023 |
| #休符 | L011, L029, L089, L092, L098 |
| #伴奏 | L032 |
| #伸ばし切る | L044 |
| #低域 | L027 |
| #低音ピアノ | L032, L036, L085 |
| #低音管楽器 | L047 |
| #余白 | L086 |
| #倍音 | L064 |
| #借用和音 | L024, L053, L085 |
| #全音 | L060 |
| #共通音保持 | L053, L053 |
| #再生トラブル | L080 |
| #分散和音 | L089 |
| #刻み | L019 |
| #加速 | L039, L040 |
| #区間 | L020 |
| #半音 | L060, L085, L087 |
| #反復 | L054 |
| #反復と変化 | L070 |
| #問いと答え | L060 |
| #土台 | L068 |
| #声部 | L091, L101 |
| #変化 | L054 |
| #変数のスコープ | L044 |
| #密度 | L013, L071 |
| #対旋律 | L087, L096 |
| #導音 | L008, L085, L086, L097 |
| #小節の表 | L020 |
| #少なさ | L038 |
| #属七 | L053, L055 |
| #山なり | L054 |
| #左右相関 | L009 |
| #帯域 | L016, L046, L083 |
| #帯域設計 | L015 |
| #平行調 | L007 |
| #引き算 | L038, L099 |
| #弦楽器 | L033 |
| #強いキック | L062 |
| #強弱 | L002, L031, L035, L051, L088 |
| #微調整 | L046 |
| #息継ぎ | L054 |
| #拍の裏 | L006 |
| #散りばめる | L043 |
| #曲全体の組み立て | L044 |
| #期待 | L036 |
| #根音 | L026, L027 |
| #構成 | L067, L097 |
| #構成管理 | L020 |
| #機能和声 | L089 |
| #歌声合成 | L017, L045 |
| #段階的な展開 | L013, L029, L042, L071 |
| #母音 | L017, L045 |
| #浮遊感 | L091 |
| #深み | L057 |
| #減七和音 | L090 |
| #溜め | L054, L056, L061 |
| #無音 | L011, L029, L030, L036, L068, L072 |
| #疲労度 | L054, L056 |
| #矩形波 | L043 |
| #緊張感 | L048 |
| #繰り返しと変化 | L071 |
| #背後から支える | L012 |
| #胴鳴り | L015 |
| #自作サンプル | L100 |
| #落差 | L011 |
| #裏打ち | L090 |
| #解決 | L007 |
| #試験録音 | L016, L021, L046 |
| #調声 | L017, L045 |
| #跳ね | L054 |
| #近接転回 | L024, L029, L030, L036 |
| #追従 | L101 |
| #逆再生 | L062 |
| #逆再生キック | L069 |
| #連打 | L038, L056 |
| #配布 | L022 |
| #配置 | L063 |
| #重なり | L077 |
| #鋸波 | L052 |
| #録音スクリプト | L044 |
| #間 | L011, L029, L030, L036, L072 |
| #隙間 | L081 |
| #隠し味 | L037 |
| #静寂 | L069 |
| #音を引く | L011, L077 |
| #音価 | L048 |
| #音域の住み分け | L012, L027, L031, L032, L035, L074, L079 |
| #音色の置き換え | L050 |
| #音色変化 | L102 |
| #音色選び | L083 |
| #音量バランス | L055, L058, L062 |
| #音階 | L048, L076 |
<!-- INDEX:END -->

## エントリ
(2026-10-12 の曲「Dark Kawaii Future Bass」 = `songs/73_section.rb`。スタイル②(AI がコードを書き、ユーザーが聴いて方向を決めた)。進行と構成は AI が決めたもので、ユーザーの確認は未実施。)

### L001 ハーフタイムのドラム
- タグ: #ハーフタイム #half-time #バックビート #backbeat #16分グリッド #キック #kick #スネア #snare
- 日付 / 曲: 2026-10-12 / Dark Kawaii Future Bass(`live_loop :kick` `:snare`)
- 決めた人: ユーザーが選んだ(ドラム A)
- 選んだ案: ドラム A(王道ハーフタイム)。B は 16分ハットの揺れと3連ロール、C はスカスカのミニマル
- コード: `"x.....x.....x.x.".each_char { |c| sample :bd_haus if c == "x"; sleep 0.25 }`(16分グリッドの文字列。スネアは `"........x......."`)
- 意味(理論): 4/4 の1小節を16分で数えると 16 マス。スネアを3拍目(8 番目)だけに置くと、2拍ぶんの間が1つの大きな拍になり、体感のテンポが半分(145 → 約 72)に感じる(ハーフタイム)。キックは 1 拍目(0)と、拍を外した 6・12・14 番目に置いて「ドッ……パーン」の重さと推進力を両立する。
- 数値: BPM 145、16分1つ = 0.25 拍 ≒ 0.103 秒。キック 0,6,12,14 / スネア 8。ドラム単体のピーク -6.6 dBFS、低域(<200Hz)91%
- 聴きどころ: 3拍目のスネアで「間」が引き延ばされる感じ
- 課題: キックの最後の `x`(14 番目)を消す、または前へずらして、ノリの変化を聴き比べる
- 関連: L002

### L002 ハットの強弱と3連ロール
- タグ: #ハイハット #hi-hat #ベロシティ #velocity #amp #強弱 #3連符 #triplet #ロール #roll
- 日付 / 曲: 2026-10-12 / Dark Kawaii Future Bass(`live_loop :hat`)
- 決めた人: AI が決めた(ユーザーが選んだドラム A に、AI が 16分ハットの強弱と3連ロールを足した)
- 選んだ案: 16分ハットを、表拍が強く・裏が弱い配列で鳴らす。4小節ごとの最後の拍だけ3連ロール
- コード: `amps = [0.45, 0.15, 0.3, 0.15]` を `amps[i % 4]` で使う。3連は `6.times { …; sleep 1.0 / 6 }`
- 意味(理論): 同じ音を同じ強さで並べると機械的に聞こえる。拍の頭を強く、裏を弱くすると拍の構造(強・弱・中・弱)が聞こえて人間味が出る。1拍を4分割(16分)から6分割(3連)に切り替えると、そこだけ急に流れが変わり、フレーズの区切りの合図になる。
- 数値: amp 0.45 / 0.15 / 0.3 / 0.15。3連の amp は 0.2 → 0.45(1つごとに +0.05)で勢いを付ける
- 聴きどころ: 4小節ごとの最後の拍(ドロップなら 28・32 小節目の4拍目)
- 課題: `amps` の並びを `[0.3, 0.3, 0.3, 0.3]` にして、抑揚がないとどう聞こえるか確かめる
- 関連: L001

### L003 単音のサブベースリフ(グルーヴ先行)
- タグ: #サブベース #sub-bass #ベースリフ #bass-riff #グルーヴ先行 #groove-first #キックとベースの位置 #sine
- 日付 / 曲: 2026-10-12 / Dark Kawaii Future Bass(`live_loop :sub`)
- 決めた人: ユーザーが選んだ(ベース A)
- 選んだ案: ベース A(サブ中心、休符が多い)。B は歪ませた saw を重ねる案、C は2小節目の後半を無音にする案
- コード: `riff = { 1 => [root, 3], 8 => [root, 2], 10 => [root + 7, 2], 15 => [root + 12, 1] }`(位置 => [音, 長さ(16分)])を `use_synth :sine` で鳴らす
- 意味(理論): コード進行より先に、ビートとベース1本のノリを作る(グルーヴ先行)。ベースはキック(0,6,12,14)の直後(1)や間(8,10,15)に置き、同じ位置に重ねない。低域は2つの音が同じ位置で鳴ると渋滞して濁るため、位置をずらして住み分ける。音は根音・根音・5度・オクターブの3種で、リズムで聞かせる。
- 数値: sine、F1〜E2(MIDI 29〜40 ≒ 44〜83Hz)。amp 1.5 × drop_gain
- 聴きどころ: キックの直後(1 番目)にベースが続いて入る所
- 課題: 1 番目のベースを 0 番目(キックと同時)にして、低域の濁りを聴き比べる
- 関連: L001, L016

### L004 サイドチェイン風の沈み(ダッキング)
- タグ: #サイドチェイン #sidechain #ダッキング #ducking #control #amp_slide #キックからの距離
- 日付 / 曲: 2026-10-12 / Dark Kawaii Future Bass(`live_loop :wobble`)
- 決めた人: ユーザーが選んだ(コード案 B)
- 選んだ案: コード案 B(伸ばしたコードをキックのたびに沈める)。C は cutoff のウーブル、A は短いスタブ
- コード: `duck = [0.1, 0.4, 0.7, 1.0]`、`control s, amp: 0.9 * duck[[i - last, 3].min]`(`last` = 直前のキックの位置)
- 意味(理論): サイドチェインは、キックが鳴る瞬間に他の音の音量を下げ、キックの低域を聴こえやすくする手法。DAW ではコンプレッサーで作るが、Sonic Pi ではキックの位置から音量を計算して `control` で動かして真似る。キックの直後は 0.1、そこから 0.4 → 0.7 → 1.0 と戻るので、「ウワッ・ウワッ」と呼吸するように聞こえる(future bass の特徴)。
- 数値: 沈みの深さ 0.1、戻りは 16分3つぶん(約 0.3 秒)。`amp_slide: 0.06` で変化をなめらかにする
- 聴きどころ: キックが鳴るたびにワブルが引っ込み、戻る所(ドロップの頭)
- 課題: `duck` を `[0.5, 0.7, 0.85, 1.0]` にして、沈みを浅くして聴き比べる(刻む小節ではこの値を使った)
- 関連: L005, L009

### L005 ワブル(cutoff の LFO)
- タグ: #ワブル #wobble #LFO #cutoff #supersaw #detune #res #ローパスフィルター
- 日付 / 曲: 2026-10-12 / Dark Kawaii Future Bass(`live_loop :wobble`)
- 決めた人: ユーザーが選んだ(コード案 A)。振れ幅 ±13 → ±7 は、ユーザーの指示
- 選んだ案: ワブル A(8分のウーブル)。B は2小節かけて cutoff が開く案、C は8分から16分に加速する案
- コード: `control s, cutoff: 82 + 7 * Math.sin(j * Math::PI / 4)`(`j` は 1/8 拍刻み)
- 意味(理論): cutoff はローパスフィルターが通す上限の高さ。低いと暗く、高いと明るい。これを正弦波(LFO = 低周波発振器)で周期的に開け閉めすると「ウワウワ」(ワブル)になる。`supersaw` は7本の鋸歯波を少しずらした(`detune`)厚い音で、倍音が多いのでフィルターの効きが目立つ。
- 数値: 中心 82、振れ幅 ±7(最初は ±13。揺らぎが強いと言われて下げた)、周期は1拍(`sin(j*PI/4)`)。`detune: 0.3`、`res: 0.2`
- 聴きどころ: 伸ばした音の明るさが1拍ごとに上下する所
- 課題: 振れ幅の `7` を 3 と 15 にして、揺らぎの強さを聴き比べる
- 関連: L004, L016

### L006 シンコペーション(3-3-2、付点8分)
- タグ: #シンコペーション #syncopation #付点8分 #dotted-eighth #3-3-2 #拍の裏 #ノリ
- 日付 / 曲: 2026-10-12 / Dark Kawaii Future Bass(`chop_a` / `chop_b`、ボーカルの刻み)
- 決めた人: ユーザーの指示(「刻んでシンコペーションで抑揚を」)。位置とアクセントの数値は AI が設計
- 選んだ案: コード案 A(8分ゲート)と B(付点の長短)を混ぜた「刻み」
- コード: `chop_a = [[0, 3, 1.0], [3, 3, 0.75], [6, 2, 0.9], [10, 3, 1.0], [13, 3, 0.7]]`([16分の位置, 長さ, アクセント])
- 意味(理論): シンコペーションは、拍の頭(0・4・8・12)を外した位置から音が始まり、次の拍の頭をまたぐリズム。16分を 3+3+2 に区切ると、2拍(8つ)の中に、4分音符の格子とずれた3つの区切りができ、「跳ねる」感じになる。3つ分 = 付点8分(0.75 拍)。
- 数値: 位置 0,3,6,10,13。アクセント 1.0 / 0.75 / 0.9 / 1.0 / 0.7(強い音と弱い音の差は約 3dB)
- 聴きどころ: 3 番目と 13 番目(拍の裏)から始まる音
- 課題: 位置を全部 4 の倍数(0,4,8,12)にして、シンコペーションがない場合の硬さを聴き比べる
- 関連: L019

### L007 区間ごとのコード進行(ローマ数字・機能)
- タグ: #コード進行 #chord-progression #ローマ数字 #roman-numeral #i-VI-III-VII #V7 #ドミナント #dominant #解決 #resolution #平行調 #セクション #トニック #サブドミナント
- 日付 / 曲: 2026-10-12 / Dark Kawaii Future Bass(`intro_p` `build_p` `drop_a_p` `brk_p` `drop_b_p`)
- 決めた人: AI が決めた(ユーザーの指示は「区間ごとに進行を変えて」だけで、進行の中身は AI。ユーザーは未確認)
- 選んだ案: 区間ごとに進行を変える(静 → 緊張 → 開放 → 浮遊 → 締め)。※ 進行は AI が決めたもの
- コード: `build_p = [[:bb2, :minor7], [:db3, :major7], [:eb3, :major7], [:c3, '7']]` などの表を `prog[小節]` に展開する
- 意味(理論): F マイナーのローマ数字は i = Fm、III = Ab、iv = Bbm、VI = Db、VII = Eb。
  - イントロ(i – VI): 動きが少なく静か。
  - ビルド(iv – VI – VII – V7): 上へ登り、最後の C7 は E(F への導音 = 半音下から主音を呼ぶ音)を含むドミナント(V7)で、F マイナーへの解決を強く呼ぶ(緊張)。
  - ドロップA(i – VI – III – VII): 平行調 Ab(III)を通るので明るく開ける(future bass の定番)。
  - ブレイク(III – VII – iv – V7): Ab 長調寄りで浮き、V7 でドロップBへ。
  - ドロップB(i – VI – iv – V7): 最後は V7 → i(最終小節の Fm)で解決して終わる。
- 数値: 1小節に1コード。ワブル・ピアノ・ビブラフォン・ベースの根音が、すべて `prog[小節]` に従う
- 聴きどころ: ビルド最後の C7(24 小節目、約 38〜39.7 秒)の緊張と、ドロップの頭(25 小節目、約 39.7 秒)の開放感の落差
- 課題: `[:c3, '7']` を `[:c3, :minor7]` にして、V7(E ナチュラル)と、導音のない Cm7 の緊張感の違いを聴き比べる
- 関連: L008, L010

### L008 ワブルをメロディにする(1音を伸ばす・グライド・導音)
- タグ: #メロディ #melody #コードトーン #chord-tone #導音 #leading-tone #note_slide #グライド #glide #ポルタメント #portamento
- 日付 / 曲: 2026-10-12 / Dark Kawaii Future Bass(`drop_a_m` `drop_b_m`、`live_loop :wobble`)
- 決めた人: ユーザーの指示(「ワブルをメロディの主役に。1音を伸ばして引く」)。旋律の音は AI が決めた
- 選んだ案: リードのピコピコ音をやめ、ワブルシンセ(supersaw)が1小節に1音を伸ばして、メロディの主役になる
- コード: `s = play prev, note_slide: 0.2, …` → `control s, note: m`(前の音から 0.2 拍かけて次の音へすべる)
- 意味(理論): メロディの各音は、その小節のコードの構成音(コードトーン)から選ぶと、コード進行となじむ。ドロップAの 1周目は C5 → Db5 → Eb5 → D5(D は Ebmaj7 の長7度で、次の Fm へ落ち着きたがる音)。ドロップBは最後を C7 の3度 E5 にして、次の F5 へ半音上行する導音の動きで、解決を呼ぶ。`note_slide` で前の音から滑らせると、跳ねずに「引く」感じ(ポルタメント)になる。
- 数値: `note_slide: 0.2`(拍)、1小節(4拍)に1音。周回ごとに2種類のメロディを交互に使う(`(k/4) % 2`)
- 聴きどころ: 小節の頭の 0.2 拍で音がすべる所と、ドロップB最後の E5 → F5
- 課題: `note_slide: 0.2` を 0.05 と 0.5 にして、音程の切り替わりの違いを聴き比べる
- 関連: L005, L007

### L009 オクターブ重ね(レイヤー)とステレオ幅
- タグ: #オクターブ重ね #layering #レイヤー #pan #ステレオ幅 #stereo-width #左右相関 #パッド #dsaw
- 日付 / 曲: 2026-10-12 / Dark Kawaii Future Bass(`layers`、`pad_on`)
- 決めた人: ユーザーが選んだ(提案 C)。「部分的に重ねて」はユーザーの指示
- 選んだ案: 提案「厚みと広がり」(C)。主音に1オクターブ下・上を重ね、左右に振る。コードのパッド(dsaw)を左右に重ねる
- コード: `layers = [[0, 0.9, 0]]; layers << [-12, 0.55, -0.35]; layers << [12, 0.3, 0.35]`([オクターブのずれ, 音量, pan])
- 意味(理論): 同じ音を1オクターブ離して重ねると、音が太くなり(下)、きらびやかになる(上)。左右に振る(pan)と、音の幅が広がる。ただし音量と pan は、重ねるほど他の音とぶつかるので、必要な小節にだけ重ねる(部分的に重ねる)。
- 数値: 下 -12(amp 0.55、pan -0.35)、上 +12(amp 0.3、pan +0.35)。重ねた全体の左右の相関は 0.98〜0.99(まだほぼモノラル寄り)
- 聴きどころ: 下のオクターブが入る小節(ドロップAの2周目、29 小節目)と、上が加わる小節(ドロップBの2周目、49 小節目)
- 課題: `0.35` を 0.8 にして、左右の振りを大きくした場合の聞こえ方を確かめる
- 関連: L004, L008

### L010 ビルドアップ(riser・ロールの加速・4つ打ち)
- タグ: #ビルドアップ #build-up #riser #ライザー #スネアロール #snare-roll #ハイパスフィルター #cutoff_slide #クラッシュ #crash #4つ打ち
- 日付 / 曲: 2026-10-12 / Dark Kawaii Future Bass(`live_loop :riser` `:kick` `:snare`)
- 決めた人: ユーザーの指示(riser の追加)。ロールの加速や4つ打ちは AI が設計
- 選んだ案: ドロップ前の8小節に、riser・4つ打ちキック・加速するスネアロール・ハットの増加を積む
- コード: `with_fx :rhpf, cutoff: 50, cutoff_slide: len do |f| control f, cutoff: 125 …`(ノイズの高域だけが残っていく)。`synth :saw, note: :f3, note_slide: len` → `control p, note: :f5`
- 意味(理論): ビルドアップは「期待」を作る区間。ノイズのハイパス(低い音から削る)を上げ、saw の音程を上げ、音量(amp)も上げていくと、「上へ登る」感じになる。スネアロールは 8分 → 16分 → 32分(`sleep` 0.5 → 0.25 → 0.125)と細かくして加速感を出す。キックを4つ打ちにして(1拍ごと)、ドロップの半拍子(ハーフタイム)との対比にする。
- 数値: cutoff 50 → 125、saw F3 → F5(2オクターブ上)、キックの amp は小節ごとに +0.06
- 聴きどころ: 21〜24 小節目(約 33〜39.7 秒)のスネアロールの加速
- 課題: ロールの `sleep 0.125` を `0.25` のままにして(加速しない)、盛り上がりの違いを聴き比べる
- 関連: L011, L007

### L011 ドロップ前の無音(間)
- タグ: #間 #無音 #休符 #rest #落差 #コントラスト #contrast #音を引く
- 日付 / 曲: 2026-10-12 / Dark Kawaii Future Bass(`gap_bars`)
- 決めた人: ユーザーの指示(「ドロップ前に少し無音を入れて」)
- 選んだ案: 提案「頭の衝撃」のうち、直前の無音の部分だけを採用
- コード: `gap_bars = [drop_a.first - 1, drop_b.first - 1]`、`pat = pat[0, 12] + "...." if gap_bars.include?(bar)`(最後の1拍を無音に)。riser も 1 拍早く止める(`sustain: len - 1`)
- 意味(理論): 音を引いた直後は、次の音が実際より大きく感じる(コントラスト)。ドロップの頭の1拍目に向けて、直前の1拍だけを無音にすると、「落とし」の衝撃が強まる。「バサッ」と音が消える隙間は、future bass のリズムを際立たせる技法。
- 数値: 無音は1拍(約 0.41 秒)。キック・ハット・ピアノ・riser を止める(リバーブの余韻は残る)
- 聴きどころ: ドロップAの直前(24 小節目の4拍目、約 39.3 秒付近。次の頭は約 39.7 秒)
- 課題: `pat[0, 12]` を `pat[0, 8]` にして、無音を2拍に伸ばして聴き比べる
- 関連: L010

### L012 ピアノを低音で支える(音域の住み分け・ローパス)
- タグ: #音域の住み分け #range-separation #ローパス #lpf #ピアノ #piano #vel #hard #背後から支える
- 日付 / 曲: 2026-10-12 / Dark Kawaii Future Bass(`live_loop :piano`)
- 決めた人: ユーザーの指示(「低音で背後から支える。ドロップでも」)
- 選んだ案: ピアノを主役にせず、低音域で背後から支える役にする
- コード: `b = win.call(r - 12, 36)`(36〜47 の範囲に根音を収める)、`with_fx :lpf, cutoff: 90`、ドロップは `low = [cs[0], cs[2], cs[1] + 12]` を1拍目と3拍目に打つ
- 意味(理論): 同じ音域に音が重なると、聞き分けられなくなる(マスキング)。ベース F1〜E2、ピアノ F2〜G3、ワブル F4〜、声 F4〜Bb4 と、音域を分けると、重ねても各パートが聞こえる。ローパス(cutoff 90 = 約 1.5kHz)で高い倍音を削ると、こもった柔らかい音になり、前に出なくなる。`vel`(打鍵の強さ)と `hard`(ハンマーの硬さ)を下げると、さらに柔らかい。
- 数値: アルペジオ amp 0.32、ドロップの和音 amp 0.28 × drop_gain、トップノート amp 0.12(vel 0.4、hard 0.7)
- 聴きどころ: ドロップに入ってもピアノの低い和音が続き、つながりが保たれる所
- 課題: `cutoff: 90` を 110 にして、ピアノが明るく前に出る様子を聴き比べる
- 関連: L013, L016

### L013 イントロのピアノ:トップノートから昇格(段階的な展開)
- タグ: #段階的な展開 #トップノート #top-note #密度 #density #メロディ昇格 #イントロ
- 日付 / 曲: 2026-10-12 / Dark Kawaii Future Bass(`lvl`、`live_loop :piano`)
- 決めた人: ユーザーの指示(「トップノートから少ない音で、徐々にメロディに昇格」)
- 選んだ案: 1音から始めて、少しずつ音を増やし、メロディになるイントロ
- コード: `lvl = (bar - intro.first) * 4 / intro.size`(0〜3)。lvl0 = トップノート1音、lvl1 = 2音、lvl2 = 4分で4音、lvl3 = 低いアルペジオ+トップのメロディ
- 意味(理論): 一番高い音(トップノート)は、和音の中で最も耳に残り、メロディとして聞こえる。トップノートを1音だけ伸ばし、2音、4音と音の数(密度)を増やすと、聴き手は自然に「これが旋律だ」と気づく。イントロを「無音からいきなり全開」にせず、段階的に展開すると、曲の始まりが自然になる。
- 数値: イントロ8小節なら2小節ごとに1段階。4小節なら1小節ごと。トップノートは和音の7度(`tones[3]`)
- 聴きどころ: 1〜2 小節の1音から、7〜8 小節のメロディへの変化
- 課題: `* 4 / intro.size` を `* 2 /` にして、昇格が2段階だけの場合に、どう聞こえるか確かめる
- 関連: L012

### L014 ビブラフォン風(pretty_bell + tremolo)
- タグ: #ビブラフォン #vibraphone #tremolo #トレモロ #pretty_bell #reverb #リバーブ
- 日付 / 曲: 2026-10-12 / Dark Kawaii Future Bass(`live_loop :vibes`)
- 決めた人: ユーザーの指示(ビブラフォンの追加、「小さく硬く」)
- 選んだ案: Sonic Pi にビブラフォンは無いので、`pretty_bell` に tremolo と reverb を掛けて近似。小さく硬くする調整
- コード: `with_fx :tremolo, phase: 0.5, depth: 0.25 do … play tones[k], sustain: 0.25, release: 0.45, amp: 0.5`
- 意味(理論): ビブラフォンは金属の鍵盤に、共鳴管の中のモーターで羽根が回り、音量が周期的に揺れる(約 5Hz)のが特徴。`tremolo` の phase 0.5 拍は 145 BPM で約 0.21 秒 = 約 4.8Hz で、その揺れに近い。音を短く(`sustain` 0.25)、リバーブを減らす(mix 0.12)と、硬く小さな音になる。
- 数値: amp 0.9 → 0.5、sustain 0.8 → 0.25、release 1.0 → 0.45、tremolo の depth 0.5 → 0.25
- 聴きどころ: ヴァース(9〜16 小節)の、2拍ごとの音の揺れ
- 課題: `phase: 0.5` を 0.25 にして、揺れが速くなると、どう聞こえるか確かめる
- 関連: L012

### L015 clap の合成と帯域設計
- タグ: #clap #クラップ #ノイズ #noise #バンドパス #bandpass #rbpf #pnoise #帯域設計 #リバーブ #胴鳴り
- 日付 / 曲: 2026-10-12 / Dark Kawaii Future Bass(`clap = lambda …`、`live_loop :clap`)
- 決めた人: ユーザーの指示(clap の追加、「低音を強く、高音を弱く、リバーブで伸びを」)
- 選んだ案: Sonic Pi の同梱サンプルに clap は無いので、ノイズで合成。重みを出すため、低域を足して高域を弱め、リバーブで伸ばした
- コード: ノイズのバースト3回(間隔 0.03 拍)を `with_fx :rbpf, centre: 86`、低い胴鳴りを `synth :pnoise` + `with_fx :lpf, cutoff: 84`、全体を `with_fx :reverb, room: 0.85, mix: 0.4`
- 意味(理論): clap は、複数の手がわずかにずれて鳴る音(約 10 ms 間隔の3連の短いバースト)。帯域は 1〜2kHz が中心。中心を下げ(2.1kHz → 約 1.2kHz)、低い成分(約 650Hz 以下)を足すと、「パッ」より「ボフッ」とした重い音になる。茶色ノイズ(`bnoise`)は低域に偏りすぎ(200Hz 以下が 59%)で、clap ではなく「ドン」に近くなったので、ピンクノイズ(`pnoise`)にした。
- 数値(clap だけを録音して比較): 旧 低 0% / 低中 1% / 中高 94% / 高 6%、新 低 37% / 低中 30% / 中高 32% / 高 1%。ピークは -19.3 → -20.3 dBFS でほぼ同じ
- 聴きどころ: 3拍目の clap の重さと、リバーブの余韻
- 課題: `centre: 86` を 80 と 92 に変えて、低くこもった音と明るい音を聴き比べる
- 関連: L016

### L016 EQ で重みを出す・声との被りを削る
- タグ: #EQ #イコライザー #equalizer #low_shelf #high_shelf #マスキング #masking #帯域 #試験録音
- 日付 / 曲: 2026-10-12 / Dark Kawaii Future Bass(`live_loop :sub` `:bass` `:wobble` の `with_fx :eq`)
- 決めた人: ユーザーの指示(ベースの重み、声との被りを EQ で調整)。EQ の値は試験録音で AI が決めた
- 選んだ案: ベースの重みを EQ で出す。ワブルの 1〜3kHz 付近を削って、声(ボコーダー)を前に出す
- コード: `with_fx :eq, low_shelf: 0.08, low_shelf_note: 45, low: 0.1, low_note: 36, low_q: 0.8`(サブ)、`with_fx :eq, mid: -0.2, mid_note: 90, mid_q: 0.6, high_shelf: -0.3, high_shelf_note: 100`(ワブル)
- 意味(理論): EQ は、周波数ごとに音量を持ち上げたり削ったりする。低域を持ち上げると重みが出る。別の2つの音が同じ周波数帯にあると、一方が他方を隠す(マスキング)。声の中心(約 0.8〜3kHz)と重なる帯域を、ワブルのほうで削ると、声が聞こえやすくなる。`low_note` などは MIDI 番号で周波数を指定する(36 = 約 65Hz、90 = 約 1.5kHz)。
- 数値(短い試験録音で決めた): ベースの低域ブースト 0.25〜0.3 は RMS +5.5dB・ピーク -0.1 dBFS で強すぎ。0.08〜0.1 で RMS +1.6dB・ピーク -2.3 dBFS。ワブルのカットは中高域(0.8〜4kHz)が 30% → 22%、RMS -1.8dB
- 聴きどころ: ドロップで声の言葉(母音)がワブルに隠れず聞こえるか(声との被りの減少は、聴いて確認が必要)
- 課題: `mid: -0.2` を -0.1 と -0.35 にして、ワブルの明るさと声の聞こえやすさの違いを聴き比べる
- 関連: L003, L015, L017

### L017 ボコーダーの声(NEUTRINO + 調声 + DSP ボコーダー)
- タグ: #ボコーダー #vocoder #フォルマント #formant #母音 #vowel #NEUTRINO #調声 #pitch-lock #smooth #glide-ms #歌声合成
- 日付 / 曲: 2026-10-12 / Dark Kawaii Future Bass(`work/vocals/` の「う」「あ」だけの声、`live_loop :vocal`)
- 決めた人: ユーザーの指示(ドロップに声、「ウーアー」、滑らかに)。調声パラメータは AI が決めた
- 選んだ案: 歌詞は意味のない母音「う」「あ」だけ。ギザギザしないよう滑らかに調声した
- コード: `neutrino_tune.py … --preset vocoder --smooth 7 --glide-ms 90 --hf-boost 0.2 --cons-boost 0.3`、`vocode.py … --dynamics --attack-beats 1`
- 意味(理論): 声の「う」と「あ」は、口の中の共鳴の山(フォルマント)の位置の違いで決まる。ボコーダーは、その形(包絡)を、鋸波などのシンセ音に載せて、機械的に歌わせる。音程は NEUTRINO の f0 が決めるので、f0 の揺れが大きいとギザギザに聞こえる。`--smooth`(移動平均を長く)と `--glide-ms`(音符の頭の滑らかな入りを長く)で滑らかにし、高域の持ち上げ(`--hf-boost`)を弱めると、シャリつきが減る。
- 数値: 音高のずれ 11 → 16 セント(100 セント = 半音)、4kHz 以上 3.6% → 0.8%。音の立ち上がりを 0.5 → 1 拍に
- 聴きどころ: 長い「う」の音程の安定と、音の頭のなめらかさ
- 課題: `--smooth` を 7 から 12 にして作り直し、滑らかさと音の頭の鈍さのバランスを聴き比べる
- 関連: L018, L019

### L018 ハモリ(3度上・3度下)
- タグ: #ハモリ #harmony #3度 #third #コードトーン #上ハモリ #下ハモリ
- 日付 / 曲: 2026-10-12 / Dark Kawaii Future Bass(`05_ua_a_low` `07_ua_a_high` など)
- 決めた人: ユーザーの指示(下ハモリ、上ハモリ)。各音は AI が決めた
- 選んだ案: 主旋律のほぼ3度下と3度上を、別の歌声として作る
- コード: 例(ドロップA): 主旋律 Ab4 → 下 F4 / 上 C5。`sample high, start: s0, finish: s1, amp: 0.55 * acc, pan: 0.3`
- 意味(理論): ハモリは、主旋律の上や下に、3度離れた音を重ねる。3度は長3度(4半音)か短3度(3半音)で、キー(ダイアトニック)の音から選ぶと、濁らない。コードの構成音の中から選ぶと、さらにコードとなじむ。下のハモリは厚みを、上のハモリは明るさを足す。
- 数値: 音高のずれ 16 / 14 セント。音量は主旋律 1.35、下 0.85、上 0.55(上は明るく目立つので小さく)。pan は 0 / -0.3 / +0.3
- 聴きどころ: 声が3つの層になって、厚みが増す所。最高音 D5(MIDI 74)は、ボーカル既定の音域(55〜72)を少し超えているので、音程の安定を確認
- 課題: 上ハモリの `amp: 0.55` を 0.8 にして、声の明るさと濁りを聴き比べる
- 関連: L017, L019

### L019 声を刻む・全員で刻む(tutti)
- タグ: #刻み #chop #tutti #ユニゾン #unison #アクセント #accent #start-finish #スライス
- 日付 / 曲: 2026-10-12 / Dark Kawaii Future Bass(`vocal_chop`、`tutti`)
- 決めた人: ユーザーの指示(声を刻む、全体を刻む箇所)。パターンは AI が設計
- 選んだ案: 声を元の位置から切り出して、シンコペーションで刻む。ドロップの 8 小節ごとの最後の2小節は、全パートが同じリズムで刻む
- コード: `sample main, start: s0, finish: s1, amp: 1.35 * acc, attack: 0.008, release: 0.06`(`s0 = (k*16 + st) / 64.0` で声の中の位置)、`tutti[b] = ((b - r.first) % 8 >= 6)`
- 意味(理論): 長い声を一定の長さで切り出して鳴らすと、リズム楽器のようになる。複数のパートが同じ位置で一斉に鳴ると(ユニゾンヒット = tutti)、リズムが強く揃い、盛り上がる。小節ごとに、鳴らす・止める、刻む・伸ばす、を変えると、同じ4小節ループでも「抑揚」がつく。
- 数値: tutti の小節では、ワブルに ×1.15、声に ×1.1(強調)。プランaでは 31・32、39・40、51・52、59 小節目
- 聴きどころ: 約 49.7 秒(31 小節目)で、ワブル・声・ピアノが一斉に跳ねる所
- 課題: `% 8 >= 6` を `% 8 >= 4` にして、全員で刻む小節を2倍に増やして聴き比べる
- 関連: L006, L017, L018

### L020 区間の管理(on_air・小節の表・plan)
- タグ: #on_air #小節の表 #構成管理 #live_loop #sleep #plan #区間 #define
- 日付 / 曲: 2026-10-12 / Dark Kawaii Future Bass(`plan = :a`、`on_air`、`prog`、`mel`)
- 決めた人: AI が決めた(コードの構造)
- 選んだ案: 60 小節の曲を、各パートが `60.times |bar|` で1回ずつ鳴らし、`on_air(bar, 範囲)` で区間ごとに出し入れする。小節ごとの情報(進行・メロディ・刻む小節)は配列に先に作る
- コード: `define :on_air do |bar, *ranges| ranges.any? { |r| r.include?(bar) } end`
- 意味(技法): すべてのパートは同じ長さ(4拍)ずつ `sleep` するので、別々の `live_loop` でも、ずれずに揃う。区間の表を1か所(`case plan`)に集めると、構成の変更が1か所で済む。注意: `define :at` は Sonic Pi のコア API の名前と衝突してエラーになる(`live_check.py` では検出できない)。固有の名前(`on_air`)にする。
- 数値: 3プラン(a: 王道 / b: ドロップ先出し / c: 長いブレイク)。すべて 60 小節 ≒ 99.3 秒
- 聴きどころ: (技法の項目。聴感ではなくコードの構造)
- 課題: `plan = :b` に変えて、ドロップ先出しの構成の違いを聴き比べる
- 関連: L007, L021

### L021 音量管理と試験録音(drop_gain・ピーク)
- タグ: #ゲインステージング #gain-staging #peak #ピーク #RMS #drop_gain #試験録音 #wav_stats #ヘッドルーム
- 日付 / 曲: 2026-10-12 / Dark Kawaii Future Bass(`drop_gain = 1.25`)
- 決めた人: ユーザーの指示(ドロップを大きく)。倍率 1.25 は AI が決めた(未確認)
- 選んだ案: ドロップの音量を1つの倍率(`drop_gain`)で、まとめて調整できるようにする
- コード: `amp: 1.4 * drop_gain`(キック)、`0.9 * drop_gain`(ワブルの主音)など
- 意味(理論): 全体のピーク(最大の音量)が 0 dBFS を超えると歪む。ミックスでは、ピークに余裕(ヘッドルーム)を残す。倍率 1.25 ≒ +1.9 dB。短い音(`supersaw` の刻み)は、同じ amp でも伸ばした音よりピークが低くなる(amp 0.9 でピーク -15.7 dBFS、伸ばした amp 0.7 で -6.5 dBFS)ので、音の長さを変えたら amp も確かめる。EQ のような値の決めにくい調整は、数秒の試験録音で数値(RMS・帯域比)を比べてから決めると、失敗が少ない。
- 数値: 完成版(73)のピーク -0.1 dBFS、RMS -13.2 dBFS、最初の 10 秒は -30 dBFS(ピアノだけのイントロ)
- 聴きどころ: ドロップの頭で音量が割れていないか(聴いて確認が必要)
- 課題: `drop_gain` を 1.0 と 1.4 にして録音し、`wav_stats.py` のピークの違いを比べる
- 関連: L016, L020

### L022 権利と配布(CC0・NEUTRINO・MIT / CC BY)
- タグ: #ライセンス #license #CC0 #NEUTRINO規約 #CC-BY #MIT #配布
- 日付 / 曲: 2026-10-12 / Dark Kawaii Future Bass(`LICENSE-MIT`、`LICENSE-CC-BY-4.0`)
- 決めた人: ユーザーの指示(MIT と CC BY 4.0)
- 選んだ案: コードは MIT、曲の録音(mp3)は CC BY 4.0。声の素材(wav)は配布しない
- 意味(運用): Sonic Pi の同梱サンプルは CC0(クレジット不要)。NEUTRINO の声は、作った音声を音楽に使えるが、音源・サンプルライブラリとしての利用や、AI・機械学習の学習データ・変換元としての利用は禁止。ボコーダー(DSP)は機械学習を使わないので該当しない。CC BY は他の制限を足せないので、声の注意書きは「第三者の素材の注意」として README に書いた。
- 数値: (なし)
- 聴きどころ: (なし。運用の項目)
- 課題: 自分の曲をアップロードする前に、最新の NEUTRINO の `license.pdf` と、公開先の規約を読み直す
- 関連: L017

### L023 付点で跳ねるキック(ハーフタイムの土台)
- タグ: #キック #kick #付点8分 #dotted-eighth #シンコペーション #syncopation #ハーフタイム #half-time #bd_tek #16分グリッド #3-3-2
- 日付 / 曲: 2026-10-13 / Dark Future Bass(`work/current.rb` の `live_loop :kick`、BPM140)
- 決めた人: ユーザーが選んだ(`02_kick_` の5案から c)。3拍目を空ける配置と音色(`bd_tek`、amp 1.3)は AI が決めた
- 選んだ案: 毎小節の頭 `X`、3マス後 `x`(0.75拍)、6マス後 `x`(1.5拍)と、付点8分で跳ねる。a(1拍目だけ)、b(裏拍)、d(808)、e(逆再生)との違いは、跳ねる位置が拍の頭から 3 マスずつずれること
- コード: `kick_p = "X..x ..x. .... .... | …"` / `kick = grid_voice :sample, :bd_tek, amp: 1.3` / `grid_play kick, kick_p`
- 意味(理論): 1マス = 16分音符(0.25拍)。頭の `X` から 3 マス後は付点8分(0.75拍)、さらに 3 マス後は 1.5 拍。「3-3-2」の最初の 3-3 に当たり、拍の頭にない位置を叩くので、拍子を崩さずに前へ押される(シンコペーション)。3拍目(8マス目)は空けてあり、スネアが入る場所になる(ハーフタイムのバックビート)。`bd_tek` は `bd_boom` より硬い音で、跳ねた位置が聞き取りやすい
- 数値: 付点の位置 0.75 拍 = BPM140 で約 0.32 秒。キック単体のピークは未録音(`02_kick_b/d/e` の録音は -6.6〜-8.4 dBFS。c は未録音)
- 聴きどころ: 各小節の頭から約 0.3 秒後と約 0.6 秒後に、2発目・3発目が来る。4小節目の最後(`x.o.`)が次の頭に向かうか(聴いて確認)
- 課題: `kick_p` の最初の小節の `x` を 1 マスずらして(`X.x.`)、跳ね方がどう変わるか聴き比べる
- 関連: L001, L006

### L024 Pad と借用和音 IV(近接転回・supersaw・ロングテイル)
- タグ: #パッド #pad #supersaw #借用和音 #borrowed-chord #近接転回 #voice-leading #ナチュラルマイナー #natural-minor #コード進行 #chord-progression #リバーブ #reverb #ロングテイル #long-tail #env-pad #cutoff #detune
- 日付 / 曲: 2026-10-13 / Dark Future Bass(`work/current.rb` の `live_loop :pad`、BPM140、F ナチュラルマイナー)
- 決めた人: ユーザーが選んだ(`03_pad_` の5案から b)。音色(supersaw、cutoff 78、detune 0.2、amp 0.4)、ボイシング、リバーブの値は AI が決めた
- 選んだ案: Fm7 → Dbmaj7 → Abmaj7 → Bb。4小節目の Bb メジャーを F メジャーから借りる(借用 IV)。a(ナチュラルマイナーだけ)、c(Bbm7 で沈む)、d(Bb7)、e(Fmaj7)との違いは、借用が4小節目に1回、メジャー三和音で出ること
- コード: `pad_p = [[:f3,:ab3,:c4,:eb4], [:f3,:ab3,:c4,:db4], [:g3,:ab3,:c4,:eb4], [:f3,:bb3,:d4,:f4]]` / `pad = grid_voice :synth, :supersaw, cutoff: 78, detune: 0.2, env: :pad, amp: 0.4` / `with_fx :reverb, room: 0.9, mix: 0.5, damp: 0.6`
- 意味(理論): F マイナーの IV は本来 Bbm(B♭・D♭・F)。同主長調の F メジャーの IV である Bb メジャー(B♭・D・F)を借りると、3度が D♭ から D(♮6)に半音上がり、暗い響きに一瞬だけ明るさが差す(借用和音)。直前の Abmaj7 [G A♭ C E♭] から Bb [F B♭ D F] へは、G→F(-2)、A♭→B♭(+2)、C→D(+2)、E♭→F(+2) と全音ずつで、1小節目の Fm7 へも B♭→A♭、D→C、F→E♭ と全音で戻る(近接転回)。supersaw は鋸波を `detune` でずらして重ねた厚い音で、`cutoff 78` が高域を丸めて暗くする。`env: :pad` は立ち上がり 0.4 拍、余韻 1 拍で、和音が次の小節へ滑る。`reverb` の `room 0.9` / `mix 0.5` / `damp 0.6` が長い残響(ロングテイル)を作る
- 数値: キックと重ねて 28 秒録音で、ピーク -10.2 dBFS、RMS -23.4 dBFS、低 <200Hz 91% / 低中 8%(キックが帯域の比を支配する)。Pad 単体のピークは未録音
- 聴きどころ: 約 20〜27 秒(4小節目)の Bb で明るさが差し、次の Fm7 へ戻って暗く閉じるか(聴いて確認)
- 課題: `cutoff` を 78→110 にして、Pad が前に出るか聴き比べる
- 関連: L009, L007, L023

### L025 ロングテイルのスネア(ハーフタイムの3拍目 + 深いリバーブ)
- タグ: #スネア #snare #ハーフタイム #half-time #バックビート #backbeat #リバーブ #reverb #ロングテイル #long-tail #damp #hpf #sn_dolf
- 日付 / 曲: 2026-10-13 / Dark Future Bass(`work/current.rb` の `live_loop :snare`、BPM140)
- 決めた人: ユーザーが選んだ(`04_snare_` の5案から b)。音色(`sn_dolf`、amp 0.85、hpf 110)とリバーブの値は AI が決めた
- 選んだ案: 各小節の3拍目(8 マス目)に1発。リバーブを深く(room 1、mix 0.55、damp 0.7)して暗い余韻を作る。a(薄いリバーブ)、c(レイヤー)、d(ゴースト)、e(ロール)との違いは、足すものがなく、残響だけを長くしたこと
- コード: `snare_p = ".... .... X... .... | …"` / `snare = grid_voice :sample, :sn_dolf, amp: 0.85, hpf: 110` / `with_fx :reverb, room: 1, mix: 0.55, damp: 0.7 do grid_play snare, snare_p end`
- 意味(理論): 4/4 を半分の速さで感じるハーフタイムは、バックビート(通常の2・4拍目)を3拍目だけに置くので、1小節が広く、重く聞こえる。`room 1` は最大の部屋、`mix 0.55` は原音と残響をほぼ半々にし、`damp 0.7` は残響の高域を減衰させて暗くする。`hpf 110` で 110Hz 以下を切り、キックの低域と分ける。キックは 0・3・6 マス目で、スネアの 8 マス目とは重ならない
- 数値: キック + Pad + スネア b を重ねて 28 秒録音で、ピーク -10.3 dBFS、RMS -23.4 dBFS(Pad だけと同じ)、高域 >4kHz 1%。スネアは小さめ(聴いて足りなければ amp を上げる)
- 聴きどころ: 各小節の3拍目(約 1.7・5.1・8.6 秒…)で、スネアと残響が Pad に埋もれず、次のキックの頭の前に消えていくか(聴いて確認)
- 課題: `damp` を 0.7→0.3 にして、残響の高域が増えて明るくなるか聴き比べる
- 関連: L001, L024

### L026 キックに揃えた saw ベース(bass b)
- タグ: #ベース #bass #saw #キックとベースの位置 #キックロック #kick-lock #env-stab #cutoff #res #fold #grid_prog #根音 #root
- 日付 / 曲: 2026-10-13 / Dark Future Bass(`work/current.rb` の `live_loop :bass`、BPM140)
- 決めた人: ユーザーが選んだ(`05_bass_` の5案から b)。音色(saw、cutoff 78、res 0.25、env :stab、amp 0.6)、音域(fold 36)、根音の進行は AI が決めた(進行は Pad に合わせた)
- 選んだ案: キックと同じ 0・3・6 マス目で短く切って鳴らす。a(根音ロング)、c(裏で動く)、d(オクターブ跳び)、e(グライド)との違いは、リズムをキックにそのまま揃えたこと
- コード: `bass_p = grid_prog [:f2,:minor7],[:db2,:major7],[:ab2,:major7],[:bb2,:major]` / `bass_r = "X..x ..x. .... .... | …"` / `grid_play bass, bass_r, on: bass_p, fold: 36`
- 意味(理論): 根音(F・D♭・A♭・B♭)だけを鳴らして、Pad の和音の下を支える。キックと同じ位置に置くと、2つの低音が1つの太い「ドン」として聞こえ、ノリが揃う(キックロック)。`saw` は倍音が豊富で、`cutoff 78` が高域を丸め、`res 0.25` で少し鋭さを残す。`env: :stab` は急に立ち上がって短く切る。`fold: 36` は音域を C2〜B2 に収める
- 数値: 全部重ねて 28 秒録音で、ピーク -7.4 dBFS、RMS -23.0 dBFS、低 <200Hz 89% / 低中 9%
- 聴きどころ: 各小節の頭で、キックと bass が1つの塊に聞こえるか。低域が濁らないか(聴いて確認)
- 課題: `cutoff` を 78→55 に下げて、こもる代わりに暗く沈むか聴き比べる
- 関連: L003, L023, L024

### L027 サイン波のサブベース(根音ロング)
- タグ: #サブベース #sub-bass #sine #サイン波 #根音 #root #fold #低域 #音域の住み分け #range-separation #ヘッドルーム
- 日付 / 曲: 2026-10-13 / Dark Future Bass(`work/current.rb` の `live_loop :sub`、BPM140)
- 決めた人: ユーザーが選んだ(`06_sub_` の5案から a)。sine、amp 0.7、fold 25 は AI が決めた
- 選んだ案: 毎小節の頭から1小節、根音を `sine` で伸ばす。b(3拍目まで)、c(808 風)、d(キック位置)、e(倍音付与)との違いは、途切れず、飾りもないこと
- コード: `sub_r = "X--- ---- ---- ---- | …"` / `sub = grid_voice :synth, :sine, attack: 0.02, release: 0.3, amp: 0.7` / `grid_play sub, sub_r, on: bass_p, fold: 25`
- 意味(理論): `sine` は倍音を持たない純音で、F1 は約 43.7Hz。bass(saw、F2 は約 87Hz)の1オクターブ下に置くと、同じ根音が2つの高さで重なり、キックの下の帯域を埋める(音域の住み分け)。`fold: 25` は音域を D♭1〜C2 に収めるので、進行が変わっても低音が上がりすぎない。1小節伸ばすので、キック・bass の跳ねた位置の下に途切れない土台ができる
- 数値: 全部重ねて 28 秒録音で、ピーク -5.1 dBFS、RMS -19.7 dBFS(bass まで重ねたときの約 -23 より約 3dB 上がった)。低 <200Hz 95%
- 聴きどころ: 各小節の頭で、キック・bass・sub が太い塊になり、濁らないか。小さなスピーカーで sub が聞こえにくい場合は倍音の追加(e 案)が必要(聴いて確認)
- 課題: `amp` を 0.7→0.4 にして、全体の RMS と低域の濁りがどう変わるか比べる
- 関連: L003, L026

### L028 サイドチェイン風の沈み(Pad と sub、キック引き金)
- タグ: #サイドチェイン #sidechain #ダッキング #ducking #level #control #amp_slide #in_thread #キックからの距離 #キックとベースの位置 #ゲインステージング
- 日付 / 曲: 2026-10-13 / Dark Future Bass(`work/current.rb` の `define :grid_duck`、`live_loop :pad` と `:sub`)
- 決めた人: ユーザーが選んだ(`07_sidechain_` の5案から b)。bass を沈めない判断、depth 0.35、戻り 4 マス、`amp_slide 0.04` は AI が決めた
- 選んだ案: キックが鳴る位置(0・3・6 マス目)から、Pad と sub の音量を 0.35 まで下げ、4 マス(1拍)かけて 1 に戻す。a(Pad だけ浅く)、c(深く長く)、d(sub だけ深く)、e(スネアでも)との違いは、中くらいの深さで、低域の2本(sub と Pad の低い声)を同時に空けること
- コード: `define :grid_duck do |fx, pattern, depth, rel| … control fx, amp: depth + (1 - depth) * t … end` / `with_fx :level, amp: 1, amp_slide: 0.04 do |duck_fx| in_thread { grid_duck duck_fx, kick_p, 0.35, 4 } … end`
- 意味(理論): サイドチェインは、キックが鳴る瞬間に他の音を下げ、キックの低域を聞こえやすくする手法。DAW ではコンプレッサーの外部入力で作るが、Sonic Pi ではキックの位置から音量を計算して `control` で動かして真似る。沈む深さ 0.35 は約 -9dB。戻りの 4 マスは 1 拍(BPM140 で約 0.43 秒)で、ハーフタイムの間延びを呼吸の感じで埋める。bass はキックと同じ位置で鳴るので、沈めると bass の頭が消える。そのため沈めない
- 数値: 沈めない sub a(ピーク -5.1、RMS -19.7 dBFS)に対し、b はピーク -6.4、RMS -21.0 dBFS(それぞれ 1.3dB・1.3dB 下がった)
- 聴きどころ: 各小節の頭(約 0・1.7・3.4 秒…)で Pad が引き、約 0.4 秒かけて膨らんで戻るか(聴いて確認)
- 課題: `0.35` を 0.1 に変えて、深い沈みの「ウワッ」とした呼吸を聴き比べる
- 関連: L004, L024, L027

### L029 イントロ:Pad だけ・拍を一部無音・少しずつ強く
- タグ: #イントロ #intro #パッド #pad #間 #無音 #休符 #rest #フェードイン #fade-in #段階的な展開 #近接転回 #voice-leading #cutoff #コード進行 #chord-progression #セクション
- 日付 / 曲: 2026-10-13 / Dark Future Bass(1-8小節、`work/proposals/08_intro.rb`)
- 決めた人: ユーザーが選んだ(コード進行 A、Pad のみ、拍を一部無音)。強さの数字(5→9)、無音の置き方、cutoff 60、amp 0.4 は AI が決めた
- 選んだ案: Fm7→Fm7→Dbmaj7→Dbmaj7 を2回。音は Pad だけで、後から足す。B(Fm7→Dbmaj7→Fm7→Ebmaj7)、C(i と iv の往復)、D(借用 I)との違いは、動きが最小で、ドロップとの落差が最大になること
- コード: `pad_r = "5--- ---- .... .... | 6--- ---- ---- .... | … | 9--- ---- .... ...."` / `pad_p` の Fm7 と Dbmaj7 を2つずつ / `pad = grid_voice :synth, :supersaw, cutoff: 60, detune: 0.2, env: :pad, amp: 0.4`
- 意味(理論): i(Fm7)と♭VI(D♭maj7)は、F・A♭・C の3音を共有する。E♭ が D♭ に半音下がるだけで、動きが最小になる(近接転回)。動きが少ないほど、静かで漂う。音の強さを 5→9 に少しずつ上げると、いきなり鳴らずに自然に入ってくる(フェードイン)。小節の最後の拍を休むと、リバーブの余韻だけが残り、呼吸の間ができる。8小節目の最後の2拍は、次のセクション(ビルド)への息継ぎになる。cutoff 60 は高域を落とし、ドロップの Pad(cutoff 78)より暗い。開いたときに落差が出る
- 数値: 15秒録音で、ピーク -23.0 dBFS、RMS -37.3 dBFS(ドロップの全体 RMS 約 -21 より約 16dB 小さい)。低中域(200〜800Hz)78%、左右の相関 0.82
- 聴きどころ: 1小節目の前半だけの音、各小節の最後の拍の余韻、8小節目の最後の2拍の無音(ユーザーが試聴し、「このままでいい」と了承)
- 課題: `5---` を `3---` に変えて、入りがさらに静かになるか聴き比べる
- 関連: L011, L013, L024

### L030 ビルド:目覚め・リードのパワーコード・ピッチドロップと無音の拍
- タグ: #ビルドアップ #build-up #ピッチドロップ #pitch-drop #間 #無音 #rest #パワーコード #power-chord #リード #lead #dsaw #attack #time_warp #キックの重ね #kick-layer #ロー・タム #low-tom #cutoff #近接転回 #voice-leading #ゲインステージング
- 日付 / 曲: 2026-10-13 / Dark Future Bass(9-16小節、`work/proposals/09_build.rb`)
- 決めた人: ユーザーが選んだ(進行 A、雰囲気「目覚めて緊張」、Pad + キック + 低いドラム、パワーコードのリード、ピッチドロップと無音の拍)。「次に進む」を了承として扱った。音量・タイミング・cutoff の値、F ナチュラルマイナーに収める判断は AI が決めた
- 選んだ案: Fm7→Bbm7→Dbmaj7→Ebmaj7 を2回。Pad の cutoff を 60→78 に開き、強さを 6→9 に上げ、キックは前半が頭だけ、後半が付点で跳ねる形。13-16小節に dsaw のリード(パワーコード + 1オクターブ下の単音 + bass)、15-16小節に低いタム、16小節目の3拍目にピッチドロップ、4拍目は無音
- コード: `pad = grid_voice :synth, :supersaw, cutoff: 60, …` / `[low, top]`(`grid_power`)/ `time_warp 0.1 do … end` / `synth :dsaw, note: :eb5, note_slide: 1 … control s, note: :eb3` / `opts.merge(release: 0.08) if bar == 7`
- 意味(理論): ビルドは、Pad の cutoff を開き、音を少しずつ強くして緊張を溜める。進行は i→iv→♭VI→♭VII で上へ登り、最後の E♭ から次の Fm7(♭VII→i)で解決してドロップが強く落ちる。パワーコード(根音 + 5度)は3度を含まず、長調・短調をあいまいにして硬く力強い。リードは、遅い立ち上がり(0.5 拍)と短いリバーブで、パッドのように伸びる。低音パートを 0.1 拍(約43ms)遅らせると、高い音が先、低い音が後から支える形になる。キックを2種類重ねると、硬い立ち上がり(bd_tek)と太い胴鳴り(drum_heavy_kick)が合わさってインパクトが増す。ピッチドロップ(音程が滑り下りる音)は、直後の無音の拍(間)の落差を強める。無音にするため、Pad・リードの余韻(release)を短く切った
- 数値: ビルドのピーク -4.8 dBFS。16小節目の拍ごとの RMS は -17.0 → -19.4 → -21.0(ピッチドロップ)→ -30.5(4拍目、後半は -38.0)。リード EQ ありの試験で、中高域 11% → 2%(EQ は最終的に外した)
- 聴きどころ: 16小節目の3拍目の滑り下りと、4拍目の間。13-16小節のリードがパッドのように入るか(ユーザーが試聴して了承)
- 課題: `pitch_drop` の `note: :eb3` を `:eb2` にして、落ち方の深さを聴き比べる
- 関連: L010, L011, L024, L026
- 後日の変更: ユーザーの指示でピッチドロップ(と最後の1拍の無音)は削除し、「音をリズミカルに刻んでドロップへ向かう」形に置き換えた(L039)。この項の `pitch_drop` の記述は、当時の記録として残す

### L031 ハイハット:16分の強弱(x・o)
- タグ: #ハイハット #hi-hat #ベロシティ #velocity #amp #強弱 #16分グリッド #ノリ #hat_snap #hpf #pan #音域の住み分け
- 日付 / 曲: 2026-10-13 / Dark Future Bass(`work/current.rb` の `live_loop :hat`、ドロップA 17-32小節)
- 決めた人: ユーザーが選んだ(`10_hat_` の5案から b)。`hat_snap`、amp 0.45、hpf 100、pan 0.2 は AI が決めた
- 選んだ案: 16分のハットに、ふつう(x)と弱(o)を並べて強弱を付ける。4小節目の最後を oxox と詰める。a(裏拍だけ)、c(ロール)、d(オープンハット)、e(付点)との違いは、細かく刻んで動きを出すこと
- コード: `hat_p = "x.ox .oxo x.ox .oxo | … | x.ox .oxo x.ox oxox"` / `hat = grid_voice :sample, :hat_snap, amp: 0.45, hpf: 100, pan: 0.2` / `grid_play hat, hat_p`
- 意味(理論): 1マス = 16分音符(0.25拍)。x(0.75)と o(0.4)の強弱が、機械的にならない揺れを作る。ハーフタイムは間が広いので、16分の細かい刻みで動きを足すと、重さを保ったまま推進力が出る。`hpf 100` は 100Hz 以下を切り、キックと bass の低域と分ける。右(pan 0.2)に少し寄せ、中央のスネアや Pad と位置を分ける
- 数値: ドロップ全体 28秒録音で、ピーク -6.2 dBFS(ハットなし -7.5)、RMS -21.0 dBFS(変わらず)。高域 >4kHz 1%(ハットは小さめ。聴いて足りなければ amp を上げる)
- 聴きどころ: 約 1.7 秒付近から、16分の強弱がグルーヴに聞こえるか。スネアの3拍目・キックと混んでいないか(聴いて確認)
- 課題: `o` を `.` に変えて、弱い音がないときのグルーヴの違いを聴き比べる
- 関連: L002, L006

### L032 低音ピアノ:キックに揃えたスタブ
- タグ: #ピアノ #piano #低音ピアノ #伴奏 #スタブ #stab #キックロック #kick-lock #vel #hard #音域の住み分け #range-separation #ゲインステージング
- 日付 / 曲: 2026-10-13 / Dark Future Bass(`work/current.rb` の `live_loop :keys`、ドロップA)
- 決めた人: ユーザーが選んだ(`11_keys_` の5案から c)。`:piano`、`vel 0.25`、`hard 0.8`、`release 0.3`、fold 48、`amp 0.5` は、`amp` と `vel` をユーザーの指示で調整した結果
- 選んだ案: キックの位置(0・3・6 マス目)で、和音を短く(`release 0.3`)鳴らす。a(ロングコード)、b(アルペジオ)、d(シンコペ)、e(根音 + 5度)との違いは、キックと同じ位置に揃えたこと
- コード: `keys_r = "X..x ..x. .... .... | …"` / `keys = grid_voice :synth, :piano, vel: 0.25, hard: 0.8, release: 0.3, amp: 0.5, pan: -0.2` / `grid_play keys, keys_r, on: bass_p, fold: 48, chord: true`
- 意味(理論): キック・bass と同じ位置で和音を叩くと、低域の3つが1つの塊として聞こえ、ノリが揃う(キックロック)。`fold: 48` は和音の根音を C3〜B3 に収め、bass(F2〜)と Pad(F3〜E♭4)の間に入れる。`vel` は鍵盤を叩く強さで、下げると音が小さくなるだけでなく、打鍵が弱くなって高域も減る。`hard` は打鍵の硬さ。`:piano` は他のシンセよりずっと大きい音源なので、`amp` を低めに調整する必要があった
- 数値: 14秒録音で、ピーク -5.8 dBFS、RMS -20.9 dBFS(ピアノなしの基準 -6.0 / -21.0)。調整の経緯: `amp 0.7`・`vel 0.6` でピーク -0.1 dBFS(割れる寸前)
- 聴きどころ: 各小節の頭で、キック・bass・ピアノが1つの塊に聞こえるか。ピアノが Pad の下で、存在感を保っているか(聴いて確認)
- 課題: `vel` を 0.25 から 0.5 に上げて、打鍵の強さで音色がどう変わるか聴き比べる
- 関連: L026, L027, L031

### L033 弦楽器のグライド + supersaw の伸ばし(コール&レスポンス)
- タグ: #弦楽器 #strings #グライド #glide #ポルタメント #portamento #レガート #legato #コール&レスポンス #call-and-response #supersaw #blade #note_slide #control #サイドチェイン #sidechain #ビブラート #vibrato #メロディ #melody
- 日付 / 曲: 2026-10-13 / Dark Future Bass(`work/current.rb` の `live_loop :sup_chord` と `:strings`、ドロップA)
- 決めた人: ユーザーの指示(「ベースやキックが強く打ち込まれるときはスーパーソーを伸ばし、ベースが落ち着くときにメロディが応答するように細かく弾いて」「スーパーソーではなく弦楽器でグライドで滑らかに弾いて。メロディーをなぞる感じで」「応答だけでなくdropの全体を弾いて」)。フレーズの音、`blade` の選択、cutoff 90、ビブラートの値は AI が決めた
- 選んだ案: 前半(0〜7マス目)は supersaw の和音を伸ばし、弦楽器は和音の音(F5・C5・E♭5・D5)を長く鳴らす。後半(8〜15マス目)は、弦楽器が6音の細かいフレーズで応答する。弦楽器は 4小節(16拍)で1つの音を鳴らし続け、音程を `control` で滑らせる。supersaw の細かい応答や、フレーズだけの弦楽器との違いは、小節の境目でも途切れないこと
- コード: `str_hold = [:f5, :c5, :eb5, :d5]` / `str_n = str_phrase.each_with_index.map { |ph, b| [str_hold[b]] + ph }` / `s = synth :blade, … sustain: 4 * 4 - attack` / `control s, note: n, amp: …`(`note_slide: 0.12`)
- 意味(理論): 強く打つ位置(キック・bass)で音を伸ばし、落ち着く位置で細かく動くと、リズムの密度が交互になり、会話のような呼応(コール&レスポンス)になる。弦楽器は、1つの音を `control` で動かすと、音が途切れず滑るグライド(ポルタメント)になる。`note_slide 0.12` 拍は約 51ms で、音程がにじまない短い滑り。長い音を和音の7度(C)・5度(E♭)・3度(D)にして、前の小節の終わりから全音で上がるようにつなぐ。最後の F5 が次の小節の根音 F5 とつながり、4小節がループしても切れない。フレーズの D(♮6)は借用 IV(B♭ メジャー)の音。`blade` はビブラート付きの弦のような音
- 数値: 28秒録音で、ピーク -4.6 dBFS、RMS -20.2 dBFS、中高域 2%。supersaw のコード単体は、最初 amp 0.45 でピーク -21.2 dBFS と小さすぎ(重ねても聞こえない)、1.5 に上げた
- 聴きどころ: 各小節の前半の長い音と、後半の滑る細かい音の対比。4小節目の F への着地(ユーザーが試聴し、「これでいい」と了承)
- 課題: `note_slide: 0.12` を 0.25 にして、さらににじむ滑らかさを聴き比べる
- 関連: L009, L028, L032

### L034 グリッチのスタッター(フィル)
- タグ: #フィル #fill #グリッチ #glitch #スタッター #stutter #rate #finish #hat_snap #アクセント #つなぎ
- 日付 / 曲: 2026-10-13 / Dark Future Bass(`work/current.rb` の `live_loop :fill`、ドロップAのつなぎ)
- 決めた人: ユーザーが選んだ(`16_fill_` の5案から d)。`hat_snap`、`finish 0.15`、rate の上げ幅、amp の上げ幅は AI が決めた
- 選んだ案: 4小節ループの最後の1拍に、`hat_snap` の短い音を 32分音符(0.125拍)で8回繰り返し、rate を 1.0 → 1.7 に上げる。a(スネアロール)、b(タムの下降)、c(逆再生キック)、e(リバースシンバル)との違いは、低音ではなく高音の質感で区切ること
- コード: `live_loop :fill do sleep 15; 8.times do |k| sample :hat_snap, rate: 1.0 + 0.1 * k, amp: 0.5 + 0.05 * k, finish: 0.15; sleep 0.125 end end`
- 意味(理論): スタッター(同じ音の短い繰り返し)は、一瞬だけ時間が引っかかったような効果を作り、デジタルな質感(グリッチ)が出る。rate を上げると音程も速さも上がるので、1拍の中で緊張が高まる。`finish: 0.15` は音の最初の15%だけを鳴らし、アタックだけを切り出す。8回 × 0.125 拍 = 1拍で、ループの長さ(16拍)を保つ
- 数値: 14秒録音で、ピーク -5.8 dBFS、RMS -20.3 dBFS(フィルなしの基準 -4.6 / -20.2)。ほかの案(b)はピーク -3.4 dBFS
- 聴きどころ: 4小節目の最後の1拍(約 6.4〜6.9 秒、12.3〜13.7 秒)で、短い高音が高くなりながら繰り返されるか(聴いて確認)
- 課題: `0.1 * k` を `0.2 * k` にして、rate の上がり方が大きくなったときの緊張を聴き比べる
- 関連: L010

### L035 Solo Violin + Cello のハモリ(強弱・swell・深いリバーブ)
- タグ: #ヴァイオリン #violin #チェロ #cello #ハモリ #harmony #3度 #third #強弱 #ダイナミクス #dynamics #swell #クレッシェンド #crescendo #ビブラート #vibrato #vibrato_delay #リバーブ #reverb #blade #音域の住み分け #range-separation
- 日付 / 曲: 2026-10-13 / Dark Future Bass(`work/current.rb` の `live_loop :solo_violin` と `:cello`、ドロップA)
- 決めた人: ユーザーの指示(弦の編成を、グライド → ヴァイオリン + ヴィオラ + チェロ → ヴィオラ + チェロ → ヴァイオリン + ヴィオラ → Solo Violin + Ensemble → ヴァイオリン + ギター → ヴァイオリン + チェロ と、順に選んだ。「リバーブを追加」「強弱をつけて」「eq は消して」も指示)。チェロを「3度下を1オクターブ低く」にしたこと、`cutoff`、強弱の値は AI が決めた。「次に進む」を了承として扱った
- 選んだ案: Solo Violin が、メロディをそのままの高さで弾く。Cello が、その3度下を1オクターブ低くハモる。どちらも `blade`(ビブラート付き)。長い音は 1拍かけて膨らみ(swell)、強弱は小節ごとの大きさ × フレーズ内の山 × `x`・`o` の強さ。深いリバーブ(room 0.9、mix 0.45、damp 0.5)。supersaw の和音は前半に残す
- コード: `dyn_bar = [0.75, 0.88, 1.0, 0.9]` / `dyn_note[bar][k]`(山で 1.0) / `s = synth …, amp: loud * 0.35, amp_slide: 1.0; control s, amp: loud` / `define :grid_third_below do |n| harm_scale.include?((n - 4) % 12) ? n - 4 : n - 3 end` / `vibrato_delay: 0.3`
- 意味(理論): 3度のハモリ(旋律の3度下)は、2つの声が同じリズムで寄り添い、甘く安定した響きになる。3度は、音階の音のうち、全音+全音(長3度、4半音)か、全音+半音(短3度、3半音)の、音階内に収まる方を選ぶ。強弱(ダイナミクス)は、フレーズの山(最も高い音)で最大にし、終わりで着地させると、歌うように聞こえる。swell(小さく始まって膨らむ)は弦の自然な立ち上がりに近い。ビブラートを少し遅らせると、音の出だしが静かで、後で揺れる、弦らしい表情になる。チェロは `cutoff 70` で暗くして、ヴァイオリン(cutoff 98)との音色の差を作り、F3〜F4 に収めて bass(F2〜)との帯域の重なりを避ける
- 数値: 28秒録音で、ピーク -6.2 dBFS、RMS -20.4 dBFS、低中域 15%、中高域 2%。編成の比較: ヴァイオリン + ヴィオラ -6.1、Solo + Ensemble -5.6(相関 0.92)、ヴァイオリン + ギター -5.2
- 聴きどころ: 各小節の前半の長い音の膨らみ、後半の細かいフレーズの山(1小節目 F5、2・3小節目 A♭5)、4小節目の D と B♭ のハモりから F への着地(ユーザーが試聴し、「次に進む」で了承)
- 課題: チェロの `amp: 0.8` を 1.2 にして、ヴァイオリンとの主従を聴き比べる
- 関連: L033, L028

### L036 ブレイク:静かに浮く・期待を作る・リバースキックと無音の拍
- タグ: #ブレイク #breakdown #セクション #間 #無音 #rest #リバースキック #reverse-kick #riser #ライザー #クレッシェンド #crescendo #期待 #低音ピアノ #piano #近接転回 #voice-leading #コード進行 #chord-progression #コントラスト
- 日付 / 曲: 2026-10-13 / Dark Future Bass(33-44小節、`work/proposals/23_break.rb`)
- 決めた人: ユーザーが選んだ(進行 A、「静かに浮く。期待を作る」、Solo Violin + Cello + 低音ピアノ、リバースキックの riser + 最後の1拍を無音)。メロディの音、強弱の値、riser の開始位置は AI が決めた。「はい。次は」を了承として扱った
- 選んだ案: D♭maj7→A♭maj7→E♭maj7→Fm7 を3回(12小節)。キック・スネア・bass・sub・ハット・Pad・supersaw を抜き、低音ピアノ(小節の頭と3拍目)+ Solo Violin + Cello の長い音(1小節2音)だけにする。繰り返しごとに大きさを 0.5→0.75→1.0 と上げ、最後の小節の 40.2 拍目から逆再生キックを鳴らして、47拍目で止め、最後の1拍を無音にする
- コード: `break_prog = grid_prog [:db3, :major7], [:ab3, :major7], [:eb3, :major7], [:f3, :minor7]` / `br_rep = [0.5, 0.75, 1.0]` / `sample :bd_boom, rate: -0.6`(40.2拍目、`sleep 40.2`)
- 意味(理論): ブレイクは、リズムと低域を抜いて音の密度を急に下げ、次のドロップの落差を大きく見せる(音を引く)。進行は♭VI(D♭)から入り、ドロップの主和音 Fm7 を最後の4小節目まで避けるので、「戻ってくる」感じがドロップBの頭で再び来る。メロディは各コードのコードトーンの長い音(3拍)で、浮く感じを作る。繰り返しごとの強弱の上昇(クレッシェンド)は、期待を高める。`bd_boom` は 1.714秒(BPM140 で4拍)で、`rate -0.6` の逆再生は約 2.86秒(6.67拍)。逆再生キックは音が最後に最大になるので、47拍目に頂点が来るよう 40.2拍目から鳴らす。最後の1拍に全員を止めると、直後のドロップBの頭が際立つ
- 数値: 22秒録音で、ピーク -13.8 dBFS、RMS -29.0 dBFS(ドロップAの約 -20 より 8〜17dB 小さい)。拍ごとの RMS は 1小節目 -37.3 → 5小節目 -33.1 → 9小節目 -30.6 → riser -24.7 → 3拍目 -21.7 → 4拍目(無音)-40.1
- 聴きどころ: ブレイクの頭の静けさ、3回目の繰り返しの強まり、最後の小節の riser と、その後の1拍の沈黙(ユーザーが試聴し、「はい。次は」で了承)
- 課題: `br_rep` を `[0.7, 0.85, 1.0]` にして、頭の静けさが減ったときの、ドロップAからのつながりを聴き比べる
- 関連: L011, L030, L035

### L037 低いタムのゴースト(パーカッション、ドロップB)
- タグ: #パーカッション #percussion #ゴーストノート #ghost-note #タム #tom #コンガ #rate #隠し味 #ドロップB #ベロシティ #velocity
- 日付 / 曲: 2026-10-13 / Dark Future Bass(`work/proposals/24_perc_c.rb`、ドロップB 45-60小節で使う)
- 決めた人: ユーザーが選んだ(`24_perc_` の5案から c)。`drum_tom_mid_soft`、`rate 1.2`、amp 0.6、置く位置は AI が決めた
- 選んだ案: 3拍目のスネアの前後(11・14・15 マス目)に、弱い(o)タムを置く。a(シェイカー)、b(ウッド)、d(タンバリン)、e(glitch)との違いは、高音ではなく中低音で、スネアの前後を飾ること
- コード: `perc_p = ".... .... .... .o.. | .... .... .... ..o. | .... .... .... .o.. | .... .... .... o.o."` / `perc = grid_voice :sample, :drum_tom_mid_soft, amp: 0.6, pan: -0.3, rate: 1.2`
- 意味(理論): ゴーストノート(幽霊音)は、主役のリズムの合間に、とても弱く入れる装飾の音で、グルーヴに奥行きを足す。位置は、3拍目のスネア(8 マス目)の後(11・14・15 マス目)で、スネアの余韻を埋める。`rate 1.2` は再生速度が 1.2 倍で、音は元より約 3.2 半音(12 × log2(1.2))高くなり、胴が軽く聞こえる。左寄り(pan -0.3)で、ハット(右寄り)と左右で分かれる。ドロップBだけに入れると、ドロップAとの違いが生まれ、曲の頂点が厚く見える
- 数値: 14秒録音で、ピーク -6.1 dBFS、RMS -20.3 dBFS(基準と同じ。小さい音なので数値に出ない)
- 聴きどころ: 3拍目のスネアのすぐ後で、低いタムが弱く返しているか(聴いて確認)
- 課題: `drum_tom_mid_soft` を `drum_tom_lo_soft` に変えて、胴の低さが増したときの印象を聴き比べる
- 関連: L001, L031

### L038 glitch のアクセント(4小節の終わりの3連打)
- タグ: #グリッチ #glitch #アクセント #accent #rate #32分音符 #連打 #FX #ドロップB #引き算 #少なさ
- 日付 / 曲: 2026-10-13 / Dark Future Bass(`work/proposals/25_glitch_a.rb`、ドロップB 45-60小節で使う)
- 決めた人: ユーザーが選んだ(`25_glitch_` の5案から a)。`glitch_perc2`、rate の上げ幅(0.3 ずつ)、amp 0.7、置く位置は AI が決めた
- 選んだ案: 4小節(16拍)の終わりの 15.25 拍目から、`glitch_perc2` を 16分(0.25拍)で3発、`rate` を 1.0 → 1.3 → 1.6 と上げる。b(裏拍の一発)、c(ロボット声の逆再生)、d(低いグリッチベース)、e(ランダム)との違いは、短い連打が高くなって、次の頭に向かうこと
- コード: `live_loop :glitch do sleep 15.25; 3.times do |k| sample :glitch_perc2, rate: 1.0 + 0.3 * k, amp: 0.7; sleep 0.25 end end`
- 意味(理論): アクセントは、数の少なさで効く。4小節に1回、最後の0.75拍にだけ置くと、他のところが静かに感じ、聞き手の耳が一瞬そこに向く。`rate` を上げると、速さと音程が同時に上がるので、短い間に緊張が高まる。sleep の合計(15.25 + 3 × 0.25 = 16)で、4小節ループの長さを保つ。ドロップAのフィル(スタッター)が `hat_snap` の高音だったのに対し、こちらは glitch 系の音色で、ドロップBの質感を変える
- 数値: 14秒録音で、ピーク -4.7 dBFS、RMS -20.3 dBFS(基準のパーカッションまで -6.1 / -20.3。連打が高いので、ピークが 1.4dB 上がった)
- 聴きどころ: 4小節の最後(約 5.7〜6.9 秒、12.5〜13.7 秒)で、短い高音が3回、高くなりながら次の頭に向かうか(聴いて確認)
- 課題: `0.3 * k` を `0.5 * k` にして、rate の上がり方が大きくなったときの緊張を聴き比べる
- 関連: L034, L037

### L039 音をリズミカルに刻んでドロップへ向かう(ピッチドロップの置き換え)
- タグ: #リズミカルな刻み #rhythmic-chop #ビルドアップ #build-up #加速 #acceleration #16分 #supersaw #stab #つなぎ #ドロップ前 #クレッシェンド #crescendo
- 日付 / 曲: 2026-10-13 / Dark Future Bass(`work/proposals/09_build.rb` の `live_loop :chop`、ビルド 15-16小節)
- 決めた人: ユーザーの指示(「ピッチドロップをすべての箇所から削除して。音をリズミカルに刻んでdropに向かう方法に置き換えて」)。刻みのリズム、音色、強さの上げ方は AI が決めた
- 選んだ案: 最後の2小節に、supersaw の和音(15小節目 D♭maj7、16小節目 E♭maj7。Pad の声部を1オクターブ上げたもの)を、4分 → 8分 → 16分と詰めて刻み、強さを 5 → 9 へ上げる。低いタムも、16分で最後まで鳴らす。最後の1拍の無音は置かない。ピッチドロップとの違いは、音程を滑らせずに、拍の細分化(密度)で緊張を作ること
- コード: `chop_r = "5... 5... 6.6. 6.6. | 7.7. 7.7. 8888 9999"` / `chop = grid_voice :synth, :supersaw, cutoff: 110, detune: 0.3, env: :stab, amp: 1.2` / `play pad_p[bar].map { |n| note(n) + 12 }`
- 意味(理論): 同じ和音を刻む間隔を、1拍 → 半拍 → 1/4拍 と詰めていくと、打つ頻度が倍々に増え、「加速している」と感じる。強さも同時に上げると、クレッシェンド(だんだん強く)になる。最後の16分の直後がドロップの頭になるので、無音を置かなくても、切れ目の落差(密度の頂点から一気に開放)が生まれる。`env: :stab` は急に立ち上がって短く切る型なので、長さが16分でも音の輪郭が保てる
- 数値: ビルド15秒録音で、ピーク -4.6 dBFS(ビルド部分)。拍ごとの RMS は 15小節目 -17.3 → -19.6 → -23.3 → -21.7、16小節目 -16.9 → -19.1 → -21.3 → -20.1(各小節の1拍目が最大で、後ろへ下がる。刻みの密度は増える一方、音は小さくなる)。最後の1拍は -20.1 dBFS で、無音ではない
- 聴きどころ: 16小節目の後半(16分の刻み)から、ドロップの頭へ入る瞬間(聴いて確認)
- 課題: `chop_r` の最後の `9999` を `9.9.` にして、最後の刻みが粗くなったときの、ドロップの頭への入りの違いを聴き比べる
- 関連: L030, L034
- 後日の変更: ユーザーの指示で、supersaw の和音の刻みは削除し、曲全体をスライサーで区切る形に置き換えた(L040)。この項は当時の記録として残す

### L040 曲全体のチョップ(スライサー)+ 直前の glitch アクセント
- タグ: #チョップ #chop #スライサー #slicer #ゲート #gate #with_fx #phase #加速 #acceleration #glitch #アクセント #accent #ビルドアップ #build-up #ドロップ前 #in_thread #control
- 日付 / 曲: 2026-10-13 / Dark Future Bass(`work/proposals/09_build.rb` の `define :grid_gate` と `live_loop :glitch_pre`、ビルド 15-16小節)
- 決めた人: ユーザーの指示(「supersawを入れないで。曲全体をチョップで区切ってdropに入り、直前でglitch fxでアクセントを加えて」)。区切りの細かさ(8分→16分→32分)、始める拍(24拍)、glitch の音と回数は AI が決めた
- 選んだ案: ビルドの最後の2小節(24〜32拍)で、Pad・キック(2種)・メロディ(リードと bass)・低いタムを、`with_fx :slicer`(矩形波)で同じ時刻に区切る。24〜28拍は8分(`phase 0.5`)、28〜30拍は16分(0.25)、30〜32拍は32分(0.125)。最後の1拍(31拍目)に、`glitch_perc2` を16分で3発、`rate` を 1.0 → 1.6 に上げる。supersaw の和音の刻み(L039)との違いは、新しい音を足さずに、すでに鳴っている全部の音を区切ること
- コード: `define :grid_gate do |&blk| with_fx :slicer, phase: 0.5, wave: 1, mix: 0 do |sl| in_thread { sleep 24; control sl, mix: 1, phase: 0.5; sleep 4; control sl, phase: 0.25; sleep 2; control sl, phase: 0.125 }; blk.call end end` / `live_loop :pad do grid_gate do … end end`
- 意味(理論): スライサーは、音をリズムに合わせて「鳴る・止まる」に切る FX(ゲート)。`phase` は1周期の長さ(拍)で、小さいほど細かい。8分 → 16分 → 32分と半分ずつ詰めると、倍々に加速して聞こえる。曲全体を同じ時刻で区切るので、バラバラの楽器がひとつの塊になって加速する。`mix: 0` の間は素通りなので、24拍目までは通常の音のまま、途中から `control` で区切りを始められる(`in_thread` で時刻を管理)。直前の glitch は、区切られない(スライサーの外)ことで、一番はっきり聞こえるアクセントになる。最後の1拍のあとが、ドロップの頭
- 数値: ビルド15秒録音で、ピーク -4.3 dBFS、RMS -23.9 dBFS。10ms ごとの音量の揺れ幅(90%点 − 10%点)は、通常の区間 11〜17 dB に対し、15小節目(8分のチョップ)71.7 dB、16小節目前半(16分)41.1 dB、3拍目(32分)26.5 dB、4拍目(32分 + glitch)12.7 dB。細かくなるほど揺れ幅が小さくなるのは、切り替えのなめらかさ(`smooth 0.02`)と、リバーブの余韻で隙間が埋まるため
- 聴きどころ: 15小節目から、全部の音が細かく切れていくか。16小節目の最後の1拍で glitch が高くなりながら、ドロップの頭に入るか(聴いて確認)
- 課題: `phase: 0.125` を `0.25` のままにして(32分をやめ)、16分で止めたときの、最後の加速感の違いを聴き比べる
- 関連: L034, L038, L039
- 後日の変更: ユーザーの指示で、チョップの始まりを 24拍 → 26拍に遅らせ、区切りを 16分(26〜28拍)→ 32分(28拍〜最後)に変えた(`sleep 26`、`phase 0.25 → 0.125`、`smooth 0.005`)。64分も試したが、「32分までにして」で外した。調整後の録音(09_build_v22): ピーク -4.7 dBFS、RMS -23.5 dBFS。10ms ごとの音量の揺れ幅は、通常 10.9 dB、15小節の頭(まだ通常)8.6 dB、15小節3〜4拍(16分)33.0 dB、16小節(32分 + glitch)16.0 dB

### L041 9度のテンション(長い音の最高音として足す)
- タグ: #9度 #ninth #テンション #tension #ナインス #9th #トップノート #top-note #コードトーン #chord-tone #ダブルストップ #double-stop
- 日付 / 曲: 2026-10-14 / Dark Future Bass(ドロップA・Bのメロディの長い音。`ninth_pc = [7, 3, 10, 0]`)
- 決めた人: ユーザーの指示(「すべてのドロップのバイオリンだけ9thのテンションを加える。それ以外は変更しない」)。9度の置き方(長い音の上、短3度以上離れた一番近い音、音量 0.7 倍)は AI が決めた
- 選んだ案: メロディの前半の長い音(2拍)の上に、そのコードの9度を最高音として重ねる。Fm7 = G、D♭maj7 = E♭、A♭maj7 = B♭、B♭(借用 IV)= C。ドロップBは、メロディがドロップAと同じなので、9度もドロップAと同じ4つを繰り返す(コードごとの9度にすると、トップノートがドロップAと変わったため)
- コード: `ninth_pc = [7, 3, 10, 0]` / `nine = n + 3; nine += 1 until nine % 12 == ninth_pc[bar]` / `s9 = synth …, note: nine, amp: loud * 0.7 * 0.35, amp_slide: 1.0`
- 意味(理論): 9度は、根音の1オクターブ上の2度の音(根音 F なら G)。7th コードにさらに足すと、響きに広がりが出る(テンション)。長い音の上に最高音として重ねると、メロディが少し開いて聞こえる。2度の濁りを避けるため、長い音から短3度(3半音)以上離れた最も近い音を選んだ
- 数値: ドロップAの録音で、9度の音の成分が、9度なしの録音に対して増えた(E♭5: 32.5 → 189.6、B♭5: 18.2 → 98.9、C6: 15.7 → 45.2。Fm7 の G6 は 14.7 → 19.4 と小さい)
- 聴きどころ: 各小節の頭の長い音の上に、少し高い音が重なって響くか。1小節目(Fm7)の G6 は小さいので聞こえにくい可能性(聴いて確認)
- 課題: `+ 3` を `+ 5` にして、9度を長い音からもう少し離したときの響きの違いを聴き比べる
- 関連: L035

### L042 ビルドアップ:stem を2小節ごとに増やす・ライザー・弦の段階的な増音
- タグ: #ビルドアップ #build-up #ライザー #riser #ノイズ #noise #rlpf #cutoff_slide #stem追加 #段階的な展開 #クレッシェンド #crescendo #チョップ #slicer #glitch
- 日付 / 曲: 2026-10-14 / Dark Future Bass(33-44小節、`work/proposals/31_buildup.rb`)
- 決めた人: ユーザーの指示(「breakをなくしてbuild-upに置き換えてriserを加えbuild-upでならす音をstemずつ増やして行く方法でbuild-upを長めにとって駆け上がって」「ライザーが少し長い」「始まる場所を遅らせて」「メロディの音を徐々に大きくして」)。stem の入り順、ライザーの作り、音量の値は AI が決めた
- 選んだ案: 12小節(2小節ごとに stem が1組ずつ増える): Pad(`cutoff` 60→100 に開く)→ 低音ピアノ → Solo Violin + Cello(5小節目から、0.2→1.0 へ1小節ごとに大きくする)→ キック(鼓動 → 付点)→ ハット + bass + sub → スネア + 低いタム。ライザーは7小節目(24拍目)から22拍: ノイズのローパス(`rlpf`)の `cutoff` が 60→125、音量が 0.02→0.35、F3→F5 に上がる `dsaw` を重ねる。最後の6拍は曲全体のスライサー(16分→32分)+ 直前の glitch。元のブレイク(音を引いて静かにする)との違いは、音を足して駆け上がること
- コード: `bu_pad_r`・`bu_keys_r`・`bu_kick_r` など、先頭に休みの小節を並べて入る小節を遅らせる / `control lp, cutoff: 125` / `control tn, note: :f5` / `loud = (bu_ramp_from + (1.0 - bu_ramp_from) * idx / 7.0) * bu_bar[b]`
- 意味(理論): ビルドアップは、音を少しずつ足して、密度とエネルギーを上げ、ドロップの開放感を大きくする。stem を一度に入れず2小節ごとに分けると、聞き手が「何かが増えた」と気付いて、展開が続いている感じが出る。ライザー(ノイズのフィルターが開き、音程が上がる音)は、高域の増加と音程の上昇で、緊張が高まる感覚を作る。音量を1小節ごとに上げる(クレッシェンド)と、始めから大きい版より、山が大きく見える。曲全体を同じ時刻で区切るスライサーは、バラバラの楽器をひとつの塊にして加速させる
- 数値: 通し録音で、ビルドアップ区間の2秒ごとの RMS が -37 → -35 → -33 → -28 → -24 → -24 → -21 → -18 と段階的に上がる(ドロップBの頭で -20 前後)
- 聴きどころ: 2小節ごとに楽器が1つずつ増える入りのタイミング(33・35・37・39・41・43小節目の頭)と、7小節目からのライザー、最後の6拍の区切り
- 課題: `grid_gate_at 42` を 40 にして、チョップを1拍早く始めたときの緊張を聴き比べる
- 関連: L010, L039, L040

### L043 チップ系リード + アルペジオ(glitch との相性)
- タグ: #チップチューン #chiptune #chiplead #矩形波 #square-wave #アルペジオ #arpeggio #スタッカート #staccato #glitch #パン #pan #散りばめる
- 日付 / 曲: 2026-10-14 / Dark Future Bass(ドロップA・B・ビルドアップの `lead_hi` と `lead_arp`)
- 決めた人: ユーザーの指示(「もっとglitchと相性がいいメロディってある？」→「楽器を変えてほしい。進行は変えないで」→「チップ系の音をもう少し小さくして。ハモリをなくしてアルペジオにして散りばめて」)。`chiplead` の選択、アルペジオの位置・順番・音量は AI が決めた
- 選んだ案: メロディの楽器を blade(ヴァイオリン風)から `chiplead`(矩形波のリード)に変え、ドロップは amp 0.4、ビルドアップは 0.3 に。3度下のハモリ(chipbass)をなくして、同じ `chiplead` のアルペジオを散りばめる: 1小節に6発(1・3・4・6・9・13 マス目)、和音の構成音を 0→1→2→3→2→1 番目の順に、1オクターブ上げて(F4〜E♭5 付近)、短く(音の長さの半分)、パンを ±0.3〜0.6 で交互に、amp 0.25
- コード: `arp_bar = ".o.o x.x. .o.. .o.."` / `arp_order = [0, 1, 2, 3, 2, 1]` / `arp_pan = [-0.5, 0.5, -0.3, 0.3, -0.6, 0.6]` / `sustain: [len * grid_step * 0.5, 0.05].max`
- 意味(理論): glitch は、短い断片の繰り返しで、デジタルな硬い倍音を持つ。そこで、倍音が硬く角のある矩形波(チップ系)にすると、glitch の質感に近づく。アルペジオ(和音の構成音を順に鳴らす)を、メロディの音の間(隙間)に少ない数で置くと、リズムが埋まらず、glitch の入る余地が残る。スタッカートと左右の振り分けで、きらめく粒のように散らばる
- 数値: 通し録音(38)で、ピーク -4.7 dBFS、RMS -23.3 dBFS、低中域 10%(blade の弦版は 30%)。ドロップの RMS は -21 前後で、弦版(-20〜-19)より約 1〜2dB 小さい
- 聴きどころ: ドロップの各小節の隙間で、アルペジオが小さくきらめくか。メロディ(chiplead)が硬すぎず、埋もれすぎないか(聴いて確認)
- 課題: `arp_bar` の `o`・`x` を増やして(例: `.oox xoxo .oo. .oo.`)、粒が密になったときの glitch との相性を聴き比べる
- 関連: L034, L038, L043 より前の L033, L035(置き換え前の弦の編成)

### L044 曲全体の組み立て(define と in_thread)と、最後の音を伸ばし切る
- タグ: #曲全体の組み立て #song-assembly #define #in_thread #set #get #time-state #変数のスコープ #sustain #release #伸ばし切る #録音スクリプト
- 日付 / 曲: 2026-10-14 / Dark Future Bass(`work/assemble_song.py` が `work/proposals/38_song_chip_arp.rb` を作る)
- 決めた人: ユーザーの指示(「最後まで曲を作ってmp3で保存し、再生して」「ドロップの最後のメロディーは伸ばし切る感じにして」)。組み立ての方法は AI が決めた
- 選んだ案: 6つのセクションを、それぞれ `define :grid_song_<名前>` の中に閉じ込め(変数が混ざらない)、`live_loop` を `in_thread` + 回数指定に変換して、最後に `in_thread` の中で順に呼ぶ(メインの流れが録音スクリプトの秒数で終わるため)。各ドロップの最後のメロディ(最後の小節の最後の音)は、3拍保持 + 2拍の余韻で伸ばし切る。ドロップAは4小節ループなので、最後の回だけ `set :last_pass, true` の合図で伸ばす
- コード: `define :grid_song_dropA do … set :last_pass, false; in_thread { sleep 48; set :last_pass, true } … end` / `if bar == str_n.size - 1 && k == str_n[bar].size - 1 && (str_n.size > 4 || get[:last_pass] == true)` / `sleep 4 if held_last`
- 意味(技法): Sonic Pi の `live_loop` は終わらずに回り続けるので、セクションが変わる曲には向かない。`define` の中の変数は、そこだけで使える(スコープ)ので、同じ名前(`pad_p` など)を別のセクションで使っても混ざらない。`set` と `get` は、スレッドをまたいで値を渡す仕組み(時刻つき)で、ループの何回目かを知らせるのに使える。音を伸ばし切るときは、FX(リバーブ)のブロックが終わると尾が切れるので、ループの終わりで待つ
- 数値: 通し録音(38)は 133.8 秒(BPM 130 で、68小節 ≒ 125.5 秒 + アウトロの余韻 8拍)。最初の通し録音は、メインの流れで曲の長さを待ってしまい、録音スクリプトの待ちと足されて、保存前に打ち切られた
- 聴きどころ: 各ドロップの終わりの、伸びる最後の F5 が、次のセクションに自然に重なるか
- 課題: `sleep 4 if held_last` をなくして、リバーブの尾が切れる様子を確かめる
- 関連: L020

### L045 ボーカルチョップ(NEUTRINO → 調声 → ボコーダー → 16分チョップ)
- タグ: #ボーカルチョップ #vocal-chop #ボコーダー #vocoder #NEUTRINO #調声 #pitch-lock #grid_chop #from #16分 #フォルマント #formant #母音 #vowel #歌声合成 #アルペジオに重ねる
- 日付 / 曲: 2026-10-14 / Dark Future Bass(`live_loop :lead_vox`、ドロップA・B)
- 決めた人: ユーザーの指示(「アルペジオにボコーダーで作って16分に切った音を重ねて」「ボーカルを少し大きく、リバーブを増やして」「ボーカルのattackをほんの少し遅く」)。歌詞(ら・な・お・い・ま・あ)、音の長さの割り当て、調声の値、切る位置は AI が決めた
- 選んだ案: アルペジオと同じ音・同じタイミングを NEUTRINO(MERROW)に歌わせる。フレーズA(ドロップAの進行)とフレーズB(ドロップB後半の進行)の2本。歌える音域(MIDI 55〜72)を超える音は1オクターブ下げる。調声(`--preset vocoder`)で `--pitch-lock` を 0.9 → 1.0 に動かし、音高のずれを 59 → 36 セントに縮めた。ボコーダー変換(DSP のみ)で4小節 = 16拍の wav にし、`grid_chop` でアルペジオの6つの位置から 16分(0.25拍)ずつ切って重ねる
- コード: `vox_pos = [0.25, 0.75, 1.0, 1.5, 2.25, 3.25]` / `vox_from4 = (0..3).flat_map { |b| vox_pos.map { |p| b * 4 + p } }` / `grid_chop vox_a, arp_r, from: vox_from4, amp: 0.7, pan: 0.0, attack: 0.03` / `with_fx :reverb, room: 0.85, mix: 0.5, damp: 0.5`
- 意味(理論): ボコーダーは、声の音色(フォルマント = 声道の共鳴)を、鋸波のキャリアに写す DSP。母音ごとに共鳴の位置が変わるので、同じ音高でも「あ・い・お」の違いが聞こえる。16分に切ると、母音の頭(子音と母音の立ち上がり)だけが短く鳴り、声が「楽器の粒」になる。アルペジオと同じ音・同じ位置に重ねると、粒が1つに溶けて、きらめきに声の質感が足される。`attack` を標準の 0.008拍から 0.03拍(約 14ms)に遅らせると、頭の硬い子音が少し丸くなる。リバーブを深くすると(`room 0.85`・`mix 0.5`)、短い粒に残響が付いて、空間に滲む
- 数値: 声の wav はピーク -1.9 dBFS(曲に重ねるときは amp 0.7 に下げた)。アルペジオの位置の RMS は -17〜-19 dBFS、休みの位置は -33 dBFS で、狙った位置に音がある。調声後の 4kHz 以上の比は 5.3%(子音が聞こえる)。通し録音(40)は、ピーク -5.0 dBFS、RMS -23.4 dBFS
- 聴きどころ: ドロップの各小節の6つの位置で、アルペジオの音と同じ高さの声の粒が重なるか(聴いて確認)
- 課題: `attack: 0.03` を `0.0` にして、頭の硬さがどう変わるか聴き比べる
- 関連: L043, L038

### L046 chiptune の高音を EQ で削る・音量とリバーブの微調整
- タグ: #EQ #イコライザー #equalizer #high_shelf #ハイシェルフ #chiptune #帯域 #reverb #amp #微調整 #試験録音
- 日付 / 曲: 2026-10-14 / Dark Future Bass(`lead_hi`・`lead_arp` と、ビルドアップの `bu_strings`・`bu_arp`)
- 決めた人: ユーザーの指示(「chiptuneの高音をeqで削って」)。削る量(-0.6)と位置(note 88)は AI が決めた
- 選んだ案: メロディとアルペジオのリバーブの内側に、`with_fx :eq, high_shelf: -0.6, high_shelf_note: 88, high_shelf_slope: 0.5` をかける。声には EQ をかけない。以前、ストリングスでは `-0.25`(浅い削り)と `-0.8`(強い削り)を試した
- コード: `with_fx :eq, high_shelf: -0.6, high_shelf_note: 88, high_shelf_slope: 0.5 do … end`
- 意味(理論): ハイシェルフは、ある周波数より上をまとめて下げる EQ。`high_shelf_note` は MIDI 番号で位置を決め(88 ≒ 1.3kHz)、`high_shelf` は -1〜1 の量。矩形波(chiptune)は奇数倍音が強く、1kHz 以上が硬く目立つので、そこを下げると、角が丸くなる。リバーブの内側(EQ → リバーブの順)に置くと、削った音がリバーブに送られ、残響も暗くなる。浅い削りは `wav_stats.py` の整数 % に出にくいので、強さを変えて(例: メロディだけ録音して EQ あり・なしを比べる)確かめる
- 数値: 通し録音で、ドロップの中高域(0.8〜4kHz)が EQ 前の 3% から 2% に減った(低域 91%、低中域 6〜7%)。以前、ストリングスのメロディだけで `-0.8` をかけると、中高域が 11% から 2% に減った
- 聴きどころ: chiptune の硬さが和らぎ、こもりすぎていないか(聴いて確認)
- 課題: `-0.6` を `-0.3` と `-0.9` にして録音し、同じ区間を聴き比べる
- 関連: L016, L043

### L047 Dark Bass へ: 低音管楽器のスタッカート・1オクターブ上の pad・9度つきの pluck
- タグ: #低音管楽器 #brass #スタッカート #staccato #gate #オクターブ上のpad #pluck #9th #ナインス #EQ #high_shelf #bass-extension #サイドチェイン #amp #cutoff
- 日付 / 曲: 2026-10-14 / Dark Bass(旧 Dark Future Bass。`songs/dark_bass.rb`)
- 決めた人: ユーザーの指示(「chiptuneをなくし、メロディではなくdrop前のbassの延長としてdropに低音系管楽器のスタッカートを入れて。1オクターブ上のpadも重ねて」「drop前の盛り上がりはセブンスコードのpluckに置き換えて。eqで高音域を削る」「dropにもpluckを入れて9thを足して弾いて。padに重ねて」「padをdropでも同じ感じで、build-upからdropにかけては少し小さく」「BPM135」「dark bassとして」)。音色(dsaw)・リズム・EQ の値・音量は AI が決めた
- 選んだ案: ①管楽器(トロンボーン〜テューバ風)= `dsaw`(`cutoff 82`・`detune 0.08`)を `gate 0.4` で短く切り、bass の1オクターブ上(F3〜)で bass と同じ位置(0・3・6 マス目)+ 4拍目の裏(12 = 5度上、14 = 1オクターブ上)。②pad の1オクターブ上を `supersaw` で重ねる。③ビルドアップは 7th コードの pluck(5〜12 小節目、音量 0.2 → 1.0)、ドロップは 7th + 9度の5音の pluck。どちらも `high_shelf -0.7`(note 84)で高音域を削る。④ドロップの pad は `cutoff 100`(ビルドアップ終盤と同じ)、pad の `amp` は 0.4 → 0.3(-2.5dB)。⑤BPM 130 → 135。声の wav も 135 で作り直した。選ばなかった案: chiptune のメロディとアルペジオ(外した)
- コード: `grid_play brass, brass_r, on: bass_p, fold: 48, steps: [0, 0, 0, 7, 12]` / `play chord_n + [nine], …`(`nine = 根音 + 14` を和音の最高音の上へ)/ `with_fx :eq, high_shelf: -0.7, high_shelf_note: 84`
- 意味(理論): bass の延長 = 同じ根音・同じ位置で1オクターブ上の音色を重ねると、低音の「打撃」に輪郭(倍音)が足され、メロディなしでも推進力が出る。5度(+7)と1オクターブ(+12)は、根音と最も協和する音で、コードの色(長・短)を変えずに動きを足せる。9度(根音の14半音上)は 7th コードの上に足す響きのテンション(Fm9 の G など)で、pad に重ねると和音が一段広がる。pluck の高音を削ると、粒が丸くなって pad に溶ける。サイドチェイン(ダッキング)は、キックと同時の管楽器・pluck にはかけない(打点がへこむため)
- 数値: 通し録音(52)は 121.8 秒、ピーク -3.2 dBFS、RMS -22.9 dBFS。ドロップは RMS -20.7、200Hz 未満 85%(旧 91%)。pluck を足しても RMS はほぼ変わらず(-20.6 → -20.6)、pluck は小さい可能性がある。管楽器の音色は Sonic Pi にないので `dsaw` の近似(未確認)
- 聴きどころ: ドロップ A の約 29〜57 秒で bass と管楽器のスタッカートが合うか / 約 57〜74 秒で pluck が大きくなっていくか(聴いて確認)
- 課題: `gate: 0.4` を 0.8 にして、スタッカートが伸びたときの違いを聴く
- 関連: L041, L042, L043, L046

### L048 ドロップのリードシンセ: 音階を1〜2度ずつ進み、音が短くなって、サブドミナントで終わる
- タグ: #リードシンセ #dsaw #パワーコード #音階 #scale #ナチュラルマイナー #サブドミナント #subdominant #緊張感 #音価 #note-length #トップノート
- 日付 / 曲: 2026-10-14 / Dark Bass(`lead_top`、ドロップA・B)
- 決めた人: ユーザーの指示(「リードシンセをdropにも持ってきてトップノートをなぞる感じでbuild-upと同じように」「半音ずつではなくFナチュラルマイナーの音階で1つか2つずつ変化」「4小節のうち2小節まで4拍、3小節は2拍、4小節は1拍にして緊張感」「4小節目は終わりに向かって下がり、最後はサブドミナント」)。具体的な音の並びは AI が決めた
- 選んだ案: ビルドと同じ `dsaw` のパワーコード(音の5度下)+ 1オクターブ下の単音を、F ナチュラルマイナーの音階(F G Ab Bb C Db Eb)の上で 1〜2 度ずつ進める。4小節で 4拍・4拍・2拍×2・1拍×4 と短くなり、最後は Bb4(IV の音)。1周 C5 → Db5 → F5 → Eb5 → G5 → Eb5 → C5 → Bb4。選ばなかった案: 半音ずつの進行(音階の外の音が出る)/ 4小節目に上がる形(最後が不安定)
- コード: `lead_scale = [:f4, …, :bb5]` / `lead_idx = [4, 5, 7, 6, 8, 6, 4, 3]` / `att = len >= 16 ? 0.5 : (len >= 8 ? 0.25 : 0.1)` / `play [low, top], …, time_warp 0.1 do play top - 12 … end`
- 意味(理論): 音階の 1〜2 度の動きは、順次進行(2度)と3度の跳躍で、メロディにならず「なぞる」程度の滑らかな動きになる。音が 4拍 → 2拍 → 1拍と短くなると、リズムが詰まって進行感と緊張が増える(音価の短縮)。終わりに下がって IV(Bb)で止まると、主和音に戻る手前の「開いた」感じで、次の周の頭(Fm7 の5度 C5)へ向かう。立ち上がり・リリースも短い音ほど速くした
- 数値: 通し録音(59)は、ピーク -3.2 dBFS、RMS -22.4 dBFS。ドロップの 200〜800Hz が約 10% から約 19% に増え、200Hz 未満は 85% から 75%
- 聴きどころ: ドロップ A の約 29〜57 秒で、4小節ごとに音が短くなって Bb で止まるか / 低音管楽器・pluck と帯域がぶつからないか(聴いて確認)
- 課題: `lead_idx` の最後の 3 を 5(Db5)に変えて、サブドミナントで終わる感じがどう変わるか聴く
- 関連: L043, L047

### L049 808 キックの 3-3-2(Dark Future Bass x Phonk のステップ1)
- タグ: #808 #bd_808 #キック #kick #3-3-2 #シンコペーション #syncopation #ローパス #lpf #ハーフタイム #half-time #サブ低音 #sub-bass
- 日付 / 曲: 2026-10-15 / Dark Future Bass x Phonk(`work/current.rb` の `live_loop :kick`。Eb minor・140 BPM)
- 決めた人: ユーザーが選んだ(ドラム5案から D を選び、808 系の音色と lpf を指示)。音量(`amp: 1.2`)・`lpf: 100`・2小節目の最後の強打は AI が決めた
- 選んだ案: 3-3-2 に跳ねるキックを 808 系の `bd_808` で鳴らす。選ばなかった案: 控えめ(A)・ロール重視(B/C)・タム入りの実験(E)
- コード: `kick = grid_voice :sample, :bd_808, amp: 1.2, lpf: 100` / `k_pat = "X..x ..x. X... ..x. | X..x ..x. ..X. ...."` / `with_fx :lpf, cutoff: 100`
- 意味(理論): 16マスを 3+3+2 で区切ると、等間隔の4つ打ちより重心がずれて「前のめり」に聞こえる(キックが 0・3・6・10 マス目)。ハーフタイムではスネアが3拍目にだけ入るので、キックの跳ねと対になる。`bd_808` はサイン波のサブ低音が長く伸びる音で、低域の土台になる。`lpf 100`(約 2.6kHz)で上の成分を削ると丸く暗くなる
- 数値: 録音 D-808 は ピーク -10.0 dBFS・<200Hz 66%。lpf を付けると <200Hz 77%・>4kHz 0%
- 聴きどころ: 頭から約 3 秒で、キックが 1拍目の頭・裏・次の拍へと跳ねるか(聴いて確認)
- 課題: `k_pat` の 2小節目の `..X.` を `.X..` に動かして、跳ね方がどう変わるか聴く
- 関連: L001

### L050 フィンガースナップのスネア: 3拍目だけ + 弱い EQ で低域寄りに
- タグ: #スネア #snare #フィンガースナップ #finger-snap #perc_snap #EQ #eq #low_shelf #high_shelf #ハーフタイム #half-time #音色の置き換え
- 日付 / 曲: 2026-10-15 / Dark Future Bass x Phonk(`work/current.rb` の `live_loop :snare`。Eb minor・140 BPM)
- 決めた人: ユーザーが選んだ(スネアの音色を何度か指示: 「高音すぎる・もっと硬く」→「リムショット」→「EQ で低音寄り」→「フィンガースナップ」→ 3案から c)。EQ の値(+0.4 / -0.3)は AI が決めた
- 選んだ案: `perc_snap` に弱い `eq`。選ばなかった案: `perc_snap` の EQ なし(a)・`perc_snap2`(b)。`sn_dub`・`drum_snare_hard` は高すぎ/硬さの要望で外れ、強い EQ(+0.8 / -0.8)は 0.8〜4kHz が 1% まで落ち、こもりすぎた
- コード: `snare = grid_voice :sample, :perc_snap, amp: 1.2` / `s_pat = ".... .... X... .... | .... .... X... ...."` / `with_fx :eq, low_shelf: 0.4, low_shelf_note: 72, high_shelf: -0.3, high_shelf_note: 84`
- 意味(理論): ハーフタイムは 3拍目(8マス目)だけに入るバックビート(裏の強拍)で、キックの 3-3-2 の跳ねと対になる。シェルフ EQ(low_shelf / high_shelf)は、指定した周波数より下(上)の全体を持ち上げる(削る)フィルターで、値は -1〜1・0 が変化なし。note は MIDI ノート番号(72 = 約 523Hz、84 = 約 1047Hz)。高域を削ると「パチッ」の鋭さが減り、低域を足すと厚みが出る。やりすぎると輪郭(クリック)が消える
- 数値: 録音 76_c は ピーク -11.2 dBFS・RMS -33.7 dBFS・<200Hz 97%・0.8-4kHz 2%(kick と合算)。EQ なし a は 0.8-4kHz 5%。聴感は未確認
- 聴きどころ: 約 1.7 秒(3拍目)で、キックの余韻の上にスナップの音が聞こえるか(聴いて確認)
- 課題: `high_shelf: -0.3` を 0 にして、パチッの鋭さが戻る度合いを聴く
- 関連: L049, L001

### L051 8分のハット: 強弱だけで刻む（x.o.）
- タグ: #ハイハット #hi-hat #8分音符 #eighth-notes #ベロシティ #velocity #強弱 #hat_snap #lpf #ローパス
- 日付 / 曲: 2026-10-15 / Dark Future Bass x Phonk(`work/current.rb` の `live_loop :hat`。Eb minor・140 BPM)
- 決めた人: ユーザーが選んだ(ハット5案から A「控えめ」)。音色 `hat_snap`・amp 0.4・専用 lpf 110 は AI が決めた（ユーザーは高域カットを希望）
- 選んだ案: 8分の刻みで、強弱だけ付ける。選ばなかった案: 16分+ロール(B)・オープンハット(C)・Phonk 風の隙間(D)・ロール多め(E)
- コード: `hat = grid_voice :sample, :hat_snap, amp: 0.4, finish: 0.5` / `h_pat = "x.o. x.o. x.o. x.o. | …"` / `with_fx :lpf, cutoff: 110`
- 意味(理論): 8分の刻みは、ハーフタイム（スネアが3拍目だけ）の遅い重心を支える「細かい目盛り」。`x`（0.75）と `o`（0.4）の強弱で、同じ音でも表と裏に抑揚が付く（ベロシティ）。`finish: 0.5` でサンプルの後半を切ると短く硬くなる。専用の lpf 110（約 4.2kHz）は、全体の lpf 100 より高域を残してハットの存在感を保つ
- 数値: 録音は未取得（B/D 案は >4kHz が 1〜2%）。聴感は未確認
- 聴きどころ: 頭から約 2 秒、ハットが 8分で一定に刻み、キックとスナップを邪魔しないか（聴いて確認）
- 課題: `h_pat` の `o` を `.` に変えて、裏の弱い音を抜いたときの軽さを聴く
- 関連: L049, L050

### L052 ベース: サブ + 鋸波の2層で、i - bVI - bIII - bVII の根音を弾く
- タグ: #ベース #bass #サブベース #sub-bass #サイン波 #sine #鋸波 #saw #コード進行 #chord-progression #ナチュラルマイナー #natural-minor #アタックとリリース #attack-release #キックとベースの位置 #fold
- 日付 / 曲: 2026-10-15 / Dark Future Bass x Phonk(`work/current.rb` の `live_loop :bass_sub` `:bass_saw`。Eb minor・140 BPM)
- 決めた人: ユーザーが選んだ（ベース5案から E）。アタック遅め・リリース短めはユーザーの指示。進行（i - bVI - bIII - bVII）、リズム（1・4・8・12 マス目）、鋸波の amp 0.25 / cutoff 75 は AI が決めた（ユーザーは進行を未確認）
- 選んだ案: サイン波の低音（Eb1〜）と、1オクターブ上の鋸波（lpf 75）を同じリズムで重ねる。選ばなかった案: 長い1音(A)・基本(B)・808 スライド(C)・オクターブ跳ね(D)
- コード: `bass_p = grid_prog [:eb1, :minor], [:cb1, :major], [:gb1, :major], [:db1, :major]` / `b_bar = ".X-. X-.. X-.. X---"` / `grid_play sub, b_pat, on: bass_p, fold: 27` / `grid_play saw, b_pat, on: bass_p, fold: 39`
- 意味(理論): Eb ナチュラルマイナー（Eb F Gb Ab Bb Cb Db）の音だけを使った進行で、i（Ebm）→ ♭VI（Cb）→ ♭III（Gb）→ ♭VII（Db）。ベースは根音だけを弾く。サイン波は倍音がなく低域が純粋（サブ）、鋸波は倍音が多く、lpf（cutoff 75 ≒ 392Hz）で上を削って輪郭だけ足す。リズムをキックの隙間（0・3・6・10 マス目を避ける）に置くと、低域の濁りを避けられる。アタック 0.1 拍の立ち上がりは打点を丸くし、リリース 0.03 拍で次の音と重ならない
- 数値: 録音 78_E は ピーク -10.4 dBFS・RMS -20.3 dBFS・<200Hz 99%。ドラムだけ(RMS 約 -33 dBFS)より約 13 dB 大きく、ベースが前に出ている可能性が高い。鋸波の 0.8-4kHz は 0%（効きが弱い）。聴感は未確認
- 聴きどころ: 約 1.7 秒付近でキックの後にベースが入り、濁らないか（聴いて確認）
- 課題: 鋸波の `cutoff: 75` を 90 にして、倍音の増え方を聴く
- 関連: L049, L050, L051

### L053 コード: スタブ + セカンダリードミナント(Db7)+ 4小節目をマイナー化(Dbm7)
- タグ: #コード #chords #supersaw #スタブ #stab #セカンダリードミナント #secondary-dominant #共通音保持 #common-tone #マイナー化 #minor #借用和音 #borrowed-chord #モーダルミクスチャー #7th #9th
- 日付 / 曲: 2026-10-15 / Dark Future Bass x Phonk(`work/current.rb` の `live_loop :chords`、`bass_p`。Eb minor・140 BPM)
- 決めた人: ユーザーが選んだ（コード5案から C）。「4小節目をマイナーに」はユーザーの指示（`bass_p` の4つ目を minor に）。和音の並び（Ebm9 / Cbmaj7 / Gbmaj7 / Dbm7）と Db7 の位置、スタブのリズム、amp 0.8 は AI が決めた
- 選んだ案: `supersaw` のスタブで、2小節目の後半だけ Db7、4小節目を Db の長三和音から短三和音（Dbm7）に。選ばなかった案: パッド(A)・スタブのみ(B)・上声ペダル(D)・Ab の借用(E)
- コード: `bass_p = grid_prog …, [:db1, :minor]` / `chords_n = [[:eb4, :gb4, :bb4, :db5, :f5], …, [:db4, :e4, :ab4, :cb5]]` / `db7_n = [:db4, :f4, :ab4, :cb5]` / `notes = db7_n if bar == 1 && (i % 16) >= 8`
- 意味(理論): 2小節目後半の Db7（Db F Ab Cb）は、次の Gb（3小節目）の属七（V7）。Db7 の7度 Cb がベースの根音と同じなので、ベースを変えずに張り詰めた響きを足せる（セカンダリードミナント）。4小節目は元の Db major（Db F Ab）の長3度 F を半音下げて Fb（= E）にすると Dbm7 になり、Eb ナチュラルマイナーの外の音（Fb）を使う借用的な暗さ（短3度）が出る。ベースは根音だけを弾くので、`bass_p` の minor は音に出ず、暗さは上の Dbm7 が担う
- 数値: 録音 80 は ピーク -9.9 dBFS・RMS -20.2 dBFS・<200Hz 97%（ベース主体。和音の amp は 0.3 → 0.8 に上げた）。聴感は未確認
- 聴きどころ: 約 2.6〜3.4 秒（2小節目の後半）の張り詰め / 約 5.1〜6.9 秒（4小節目）の暗さ（聴いて確認）
- 課題: `db7_n` から `:cb5` を抜いて（7度なし）、張り詰め方の違いを聴く
- 関連: L052

### L053 コードのスタブ: Ebm9 → Cbmaj7 → Gbmaj7 → Dbm7 と、2小節目後半の Db7
- タグ: #コード #chords #スタブ #stab #supersaw #スーパーソウ #共通音保持 #common-tone #セカンダリードミナント #secondary-dominant #属七 #Db7 #9th #ナインス #grid_prog #chord_true
- 日付 / 曲: 2026-10-15 / Dark Future Bass x Phonk(`work/current.rb` の `live_loop :chords` `:dom7`。Eb minor・140 BPM)
- 決めた人: ユーザーが選んだ（コード5案から C）。4小節目を Dbm7（マイナー）にしたのはユーザーの変更。ヘルパーの書式（種類を省略可）の修正もユーザーの指示。和音の音・リズム・amp 0.8 は AI が決めた
- 選んだ案: ベースの進行 Eb - Cb - Gb - Db の上に supersaw のスタブを重ね、2小節目の後半だけ Db7 にする。選ばなかった案: 伸ばすパッド(A)・上声ペダル(D)・借用和音 Ab(E)
- コード: `chord_p = grid_prog [:eb4, :m9], [:cb4, :major7], [:gb4, :major7], [:db4, :minor7]` / `dom_p = grid_prog [:db4, :dom7]` / `grid_play stab, c_pat, on: chord_p, chord: true`
- 意味(理論): Ebm9（i）→ Cbmaj7（♭VI）→ Gbmaj7（♭III）は、Eb ナチュラルマイナーの音だけでできていて、隣り合う和音が 2〜3 音を共有する（共通音保持: Eb Gb Bb → Gb Bb Db ...）ので滑らかにつながる。Db7（Db F Ab Cb）は次の Gb の V7（属七）で、2小節目の後半に挟むと V7 → I の解決で 3 小節目が「落ち着く」（セカンダリードミナント）。ベースの Cb が Db7 の b7 に当たるので、ベースを変えずに済む。4小節目の Dbm7 は、Db の長3度 F を短3度 Fb(= E)に下げて暗くした響き（ナチュラルマイナーの外の音を含む）。`grid_prog` の種類（`:m9` など）は `chord: true` のときだけ読まれ、ベースの根音では読まれない
- 数値: 録音（ドラム + ベース + コード）は ピーク -9.5 dBFS・RMS -20.2 dBFS・<200Hz 97%。コードを足しても RMS はほぼ変わらず、ベースが約 13 dB 大きい状態で、コードは埋もれている可能性が高い（要調整）
- 聴きどころ: 約 3.4 秒(3小節目の頭)で Db7 から Gb への解決が落ち着くか / 約 6.9 秒(4小節目)で Dbm7 が暗く聞こえるか（聴いて確認）
- 課題: `c_bar` の `..X-`（10 マス目のスタブ）を 1 マス後ろにずらして、キックとの跳ね方を聴く
- 関連: L052, L049

### L054 メロディ: 山なりの2小節フレーズを繰り返し、最後の1音だけ変える(grid_repeat_phrase)
- タグ: #メロディ #melody #山なり #arch #反復 #repetition #変化 #variation #カウンターメロディ #counter-melody #溜め #tame #跳ね #swing #付点 #dotted #息継ぎ #breath #疲労度 #fatigue-score #supersaw #grid_repeat_phrase
- 日付 / 曲: 2026-10-16 / Dark Future Bass x Phonk(`work/current.rb` の `live_loop :lead`。Eb minor・140 BPM)
- 決めた人: ユーザーの指示(「前半を繰り返し最後だけ変える」「中央へ上がり頂点から下がる」「supersaw にする」「溜め・跳ね・付点・息継ぎの4関数だけでリズムを作る」「快適スコア」)。音の選び・強弱・解釈(2小節フレーズ×2)は AI が決めた
- 選んだ案: 2小節のフレーズ(1小節目 Eb F Gb Ab で上がる、2小節目 Bb(頂点) Ab Gb で下がる)を 2回。1回目の終わり F、2回目の終わり Eb。選ばなかった案: 4小節全体で1つの山(繰り返しと両立しない)
- コード: `m_notes, m_acc = grid_repeat_phrase(m_up_down, m_acc_phrase, :f5, :eb5)` / リズムは `m_bars = m_phrase + m_phrase`
- 意味(理論): 同じ型を繰り返すと「覚えやすさ」が生まれ、最後の1音だけ変えると、1回目は半音上の F で未解決、2回目は根音 Eb で着地する問答になる(反復+変化)。山なりの輪郭(アーチ)は、上がる間に緊張、頂点で最大、下がる間に解決へ向かう。頂点を強さ 1.0 にすると、溜めも深くなり重みが出る。疲労度はリズムだけを見るので、1・2小節目が 26.6 のまま
- 数値: 録音 current_arch_v1(14秒)。音の聴感は未確認
- 聴きどころ: 約 1.7 秒(2小節目の頭)の Bb の山 / 約 5〜6.9 秒の Eb への着地
- 課題: `:bb5` を `:c6` にして、頂点を高く(Eb マイナーの外へ)した聞こえ方を比べる
- 関連: L053

### L055 ベース進行: i – bVI – iv – V7(Eb – Cb – Ab – Bb)で暗くし、ベースを -6dB
- タグ: #コード進行 #chord-progression #属七 #dominant #V7 #ハーモニックマイナー #harmonic-minor #セカンダリードミナント #secondary-dominant #音量バランス #mix-balance
- 日付 / 曲: 2026-10-16 / Dark Future Bass x Phonk(`work/current.rb` の `bass_p` `chord_p` `dom_p`、`sub` `saw` の amp)
- 決めた人: ユーザーが選んだ(ベース進行の5案から C)。ベースの音量を下げる指示もユーザー。ペダルポイント案(E)はユーザーが不採用にした。上の和音(Abm7・Bb7)と dom_p の Eb7 は AI が決めた
- 選んだ案: ベースの根音を Eb – Cb – Ab – Bb、上の和音を Ebm9 – Cbmaj7 – Abm7 – Bb7。2小節目後半は Eb7。選ばなかった案: A(i-iv-v-bVI)・B(フリジアン)・D(ナポリ)・E(ペダルポイント。不採用)
- コード: `bass_p = grid_prog :eb1, :cb1, :ab1, :bb1` / `chord_p = grid_prog [:eb4, :m9], [:cb4, :major7], [:ab4, :minor7], [:bb3, :dom7]` / `sub` amp 1.0 → 0.5、`saw` amp 0.25 → 0.125
- 意味(理論): 元の進行は Cb から Gb へ長3度で上がり、Cbmaj7・Gbmaj7 が明るかった。Cb から Ab は短3度の下降で、Abm7(iv)が暗く落ち着く。4小節目の Bb7(V7)は、3度 D がマイナースケール外の音(ハーモニックマイナーの導音)で、Ebm に戻りたくなる張り詰めがある。ループの頭に戻る力が強い。ベースの amp は半分(-6dB)にした
- 数値: 録音(14秒)は ピーク -9.7 dBFS・RMS -23.5 dBFS・<200Hz 68%・200〜800Hz 29%(前は <200Hz 88%)。聴感は未確認
- 聴きどころ: 約 3.4〜5.1 秒(Abm7)の暗さ / 約 5.1〜6.9 秒(Bb7)の張り詰めと、ループの頭への戻り
- 課題: `:bb1` を `:f1` に変えて、最後の和音の働きが変わるのを聴く
- 関連: L052, L053

### L056 メロディ: 同じ音の連打 + 一部を削るシンコペーション + クリシェ(Eb → D → Db → C)
- タグ: #メロディ #melody #クリシェ #cliche #シンコペーション #syncopation #連打 #repetition #phonk #dsaw #溜め #tame #grid_dotted #grid_repeat_phrase #疲労度 #fatigue-score
- 日付 / 曲: 2026-10-16 / Dark Future Bass x Phonk(`work/current.rb` の `live_loop :lead`)
- 決めた人: ユーザーの指示(連打、削る、クリシェ、丸みのある saw、グライドを消す)。音の列・強弱・削る位置は AI が決めた。ユーザーが「メロディはこれでいい」と採用
- 選んだ案: 1小節ごとに1つの音を8分で連打し、小節ごとに半音ずつ降りる(Eb5 → D5 → Db5 → C5)。1小節 5音に削り、奇数小節は 0 2 6 8 12、偶数小節は 0 6 8 10 14。音色は dsaw(cutoff 80)。途中案: ロングトーン + グライド + ビブラート(グライドは不採用)、山なり、ペダル Bb5(不採用)
- コード: `m_notes = m_line.flat_map { |n| [n] * 5 }` / `grid_dotted([2, 2, -2, 2, 2, -2, 2, -2])` / `play ..., sustain: 0.1, release: 0.12, cutoff: 80`
- 意味(理論): クリシェは和音が変わっても線が一方向に半音ずつ降り続ける手法。同じ音の連打は、リズムだけを聞かせて phonk の反復感を出し、拍の頭や裏を削ると、残った裏が前に出てシンコペーションになる。短い音は中高域が少なく、帯域は <200Hz 88%・中高域 1%(ベースに埋もれやすい。未確認)
- 聴きどころ: 約 0〜0.9 秒の 0 と 2 の連打 / 約 1.7〜3.4 秒の裏への詰め
- 課題: 1小節目の `2, 2` を `2, -2` に変える
- 関連: L054

### L057 glitch: 小節の最後の1拍で和音を16分にこま切れ
- タグ: #glitch #グリッチ #スタッター #stutter #コード #chords #supersaw #cut #深み
- 日付 / 曲: 2026-10-16 / Dark Future Bass x Phonk(`work/current.rb` の `glitch` `g_pat` `live_loop :glitch`)
- 決めた人: ユーザーの指示(次の候補の A を加える)。位置・音の数・強弱・amp は AI が決めた
- 選んだ案: 2小節目の15マス目に軽く1音(`x`)、4小節目の12〜15マスに4連(`xoXx`)。和音は `chord_p` と同じ(2小節目 Cbmaj7、4小節目 Bb7)。音は `cut: 0.05` で短く切る。選ばなかった案: 808 スライド・カウベル・ビルドアップ・リバースシンバル(後回し)
- コード: `glitch = grid_voice :synth, :supersaw, amp: 0.6, ..., cut: 0.05` / `g_pat = ".... .... .... .... | .... .... .... ..x. | .... .... .... .... | .... .... .... xoXx"` / `live_loop :glitch do grid_play glitch, g_pat, on: chord_p, chord: true end`
- 意味(理論): スタブの最後の1拍(空いている拍)に、同じ和音を 16分で短く刻むと、ループの切れ目に細かい動きが入り、次の小節の頭が引き立つ。4小節目は Bb7 の張り詰めと重なり、ループの頭へ向かう緊張が強まる
- 数値: 録音(14秒)は ピーク -9.8 dBFS・RMS -23.5 dBFS(glitch なしと同じ程度)。聴感は未確認
- 聴きどころ: 約 2.8〜3.4 秒(2小節目の最後の1音)/ 約 6.4〜6.9 秒(4小節目の4連)
- 課題: `xoXx` を `XXXX` にして、強さの抑揚のない刻みと聴き比べる
- 関連: L055, L053

### L058 カウンターメロディ(ロングトーン)+ メロディを4音に + リバーブ + サブベース・EQ
- タグ: #カウンターメロディ #counter-melody #ロングトーン #long-tone #リバーブ #reverb #EQ #eq #サブベース #sub-bass #音量バランス #mix-balance #シンコペーション #syncopation
- 日付 / 曲: 2026-10-16 / Dark Future Bass x Phonk(`work/current.rb` の `live_loop :counter` `:lead`、`sub` の amp)
- 決めた人: ユーザーが選んだ(カウンター5案から A)。「メロディの音を少なく」「メロディとカウンターにリバーブ」「サブベースを大きく」「メロディの高音を EQ で小さく・低音を大きく」はユーザーの指示。音の高さ・リバーブの値は AI が決めた
- 選んだ案: カウンターは `blade` で Gb5 を14マス伸ばし(1小節に1音)、最後の小節だけ F5。メロディは1小節4音(奇数小節 0 6 8 12、偶数小節 0 6 8 14)。両方に `reverb room: 0.7, mix: 0.3`。`sub` amp 0.5 → 0.8。メロディに `eq`(low_shelf +0.4 @ C5、high_shelf -0.5 @ C6)。選ばなかった案: B(隙間で応える)・C(逆向きの線)・D(低い音域)・E(前打ち)
- コード: `m_notes = m_line.flat_map { |n| [n] * 4 }` / `with_fx :reverb, room: 0.7, mix: 0.3 do … end` / `cm_len_bars = [[14, -2]] * 4`、`cm_notes = %i[gb5 gb5 gb5 f5]`
- 意味(理論): Gb5 は Ebm の短3度、Cbmaj7 の5度、Abm7 の7度で、3小節続けて保つ(共通音保持)ので和音が変わっても動かない。最後の Bb7 で F5(5度)へ半音下がり、ループの頭へ向かう。連打のメロディ(短い・動く)と長い音(静か・動かない)でリズムの役割が分かれる。リバーブは残響で奥行きを足し、room が大きいほど残響が長い。短い連打には残響が音の隙間を埋める。音数を減らすと隙間が増え、残響が目立つ
- 数値: 録音(14秒)は ピーク -6.1 dBFS・RMS -20.4 dBFS・<200Hz 79%・200〜800Hz 20%・中高域 1%。聴感は未確認
- 聴きどころ: 約 1〜3 秒でメロディの隙間にリバーブの尾が聞こえるか / 約 5.1〜6.9 秒で F5 への下降が Bb7 と合うか
- 課題: `mix: 0.3` を 0.15 と 0.5 にして、奥行きと濁りの境目を聴き比べる
- 関連: L056, L055

### L059 808 スライド(5度の跳ね)+ メロディのオクターブ重ね
- タグ: #808 #スライド #slide #ポルタメント #portamento #note_slide #control #オクターブ重ね #octave-doubling #ベース #bass #メロディ #melody
- 日付 / 曲: 2026-10-17 / Dark Future Bass x Phonk(`work/current.rb` の `grid_slide_note` `bass_midi`、`live_loop :lead`)
- 決めた人: ユーザーが選んだ(808 スライド5案から D)。「メロディも同様の音をオクターブ上で鳴らして」はユーザーの指示(「同様」を、同じ音・同じリズムを +12 半音で重ねる意味に解釈。スライドは入れていない)。滑らせる長さ・位置は AI が決めた
- 選んだ案: 3拍目の半ばで根音から +7 半音(5度)へ跳ね(0.1 拍)、4拍目の頭で根音へ 0.2 拍かけて滑り降りる。ベースの sub と saw の両方。メロディは dsaw をやめ、サイン波で5度上から 0.15 拍かけて目標の音へ滑り降りる（sustain 0.15・release 0.2・amp 1.0）。オクターブ重ねは外した。選ばなかった案: A(次の根音へ滑り込み)・B(ピッチドロップ)・C(しゃくり)・E(4小節目の下降)
- コード: `nd = play r, **o, note_slide: 0.1; time_warp 0.5 do control nd, note: r + 7 end` / `play r + 7, **o, note_slide: 0.2; control nd, note: r` / `play note(m_notes[k]) + 7, ..., note_slide: 0.15; control nd, note: note(m_notes[k])`
- 意味(理論): `note_slide` は、`control` で note を変えたとき、新しい高さへ滑らかに移る長さ(拍)。音高が連続して動くと、サイン波のサブが「歌う」808 らしい唸りになる。5度は協和度が高く、根音への戻りが安定して聞こえる。メロディをオクターブ上に重ねると、同じ音名なので和声は変わらず、太さと明るさが増える(倍音の位置が揃う)
- 数値: 録音(14秒)は ピーク -4.0 dBFS・RMS -20.2 dBFS・中高域 5%(メロディ重ね前は 1%)。聴感は未確認
- 聴きどころ: 約 0.4〜0.5 秒・1.2〜1.4 秒(3〜4拍目)の5度の跳ねと降り / 約 0〜1.7 秒でメロディの音の頭に唸りが聞こえ、ベースと音域が重なって濁らないか
- 課題: `r + 7` を `r + 12`(オクターブ)にして、跳ねの協和度の違いを聴く
- 関連: L055, L058

### L060 メロディの試行と撤去: 9th の追加と削除・全音の山・問いと答えの削除・高音ピアノ → 低音ピアノのリフへ
- タグ: #メロディ #melody #9th #ナインス #テンション #tension #半音 #semitone #全音 #whole-tone #トリル #trill #call-and-response #問いと答え #サブドミナント #subdominant #カウベル #cowbell #ピアノ #piano
- 日付 / 曲: 2026-10-17 / Dark Future Bass x Phonk(`work/current.rb` の旧 `live_loop :lead`。今は外した)
- 決めた人: ユーザーの指示(9th を加える→なくす、小さな山を入れる、半音を全音にする、問いと答えをなくす、メロディが浮くので置き換える)。音の選びは AI が決めた
- 選んだ案: 最終的に、メロディ(bass_foundation の連打)と高音ピアノは外した。途中の試行は次のとおり。8小節に増やす(前半 6音の問い + 後半 4音の答え)→ 終わりをサブドミナント Ab5 に →コードに 9th(Cbmaj9・Abm9・Bb9)を追加 →「なくして」で 7th に戻す(Ebm9 だけ残す)→ 半音の往復(Eb E Eb E)を入れた → 「ピコピコ」の原因と指摘 → 全音の往復(Eb F Eb F)にして、問いと答えの切り替えを外した → 浮いて聞こえるので外し、ピアノ2本(L061)に置き換えた。カウベル(drum_cowbell・pitch 12)の高音リフも試して外した
- コード: `m_notes = [%i[eb5 f5 eb5 f5 eb5 db5], …].flatten` / `chord_p = grid_prog [:eb4, :m9], [:cb4, :major7], [:ab4, :minor7], [:bb3, :dom7]`(9th 版は `:major9` `:minor9` `:'9'`。`:dom9` は無い)/ `cowbell = grid_voice :sample, :drum_cowbell, pitch: 12`
- 意味(理論): 9th は根音の2度上(オクターブ上の2度)の音で、7th の上に積むとテンションが出る。半音の往復は狭い音程で不協和に近く、8分で行き来すると「ピコピコ」の細かい動きになる。全音にすると幅が広がり、ピコピコが減る。8小節の山谷が大きいと「浮く」。和音の構成音に狙いを付けず、音域(C5〜Ab5)がスタブ(Eb4〜)やベースと離れていると、メロディだけ孤立して聞こえる。終止をサブドミナント(iv = Abm の根音 Ab)にすると、ドミナント Bb7 の7度にもなり、ループの頭へ降りたくなる
- 数値: 全音版 録音(28秒)は ピーク -7.2 dBFS・RMS -20.2 dBFS・<200Hz 75%・200〜800Hz 20%。聴感は未確認
- 聴きどころ: (撤去済み)当時は約 0〜1.7 秒の往復が全音でピコピコが減るか
- 課題: 往復の `f5` を `gb5`(短3度)にして、全音との違いを聴く
- 関連: L056, L058, L059

### L061 低音ピアノのリフ + 1オクターブ上のピアノ + ベロシティ・リバーブ
- タグ: #ピアノ #piano #リフ #riff #ベロシティ #velocity #リバーブ #reverb #オクターブ重ね #octave-doubling #パワーコード風 #5度 #fifth #グリッド #grid_each #溜め #tame
- 日付 / 曲: 2026-10-17 / Dark Future Bass x Phonk(`work/current.rb` の `live_loop :piano_lo` `:piano_up`、`lo_pat` `lo_off`)
- 決めた人: ユーザーの指示(高音ピアノをなくし低音ピアノのリフに置き換え、ベロシティを下げ、リバーブを足し、1オクターブ上のピアノを重ね、ampを上げた)。リフの音・位置・数値は AI が決めた
- 選んだ案: 低音ピアノ(ベースの根音 +12 半音)がキックの位置(0 3 6 8 14 / 0 3 6 10)で、根音 根音 5度 オクターブ(5度)と跳ねるリフ。1オクターブ上(+24)のピアノを同じリズムで重ねる。`vel` 0.35・`hard` 0.25、`amp` 0.16(下)/ 0.125(上)、リバーブ `room` 0.9・`mix` 0.5・`damp` 0.5。選ばなかった案: 高音シンセ(dsaw、2オクターブ上)で重ねる(ユーザーが「ピアノで」と訂正)
- コード: `play bass_midi[(i / 16) % 4] + 12 + lo_off[k], amp: piano_lo_amp * lvl, hard: 0.25, vel: 0.35, …` / `lo_offsets = [[0, 0, 7, 12, 7], [0, 0, 7, 12]]`
- 意味(理論): 根音・5度・オクターブだけで3度を弾かないので、長調(Cbmaj7)・短調(Ebm9)どちらの小節でも濁らない(パワーコードと同じ発想)。キックと同じ位置に置くと、リズムが一体になる。`vel` は弾く強さ、`hard` は鍵盤の硬さで、下げると倍音が減って柔らかく丸くなる。ピアノの `amp` は効きが鈍い(`amp` 0.05 → 0.1 でピーク +1.8dB 程度)。リバーブの `damp` を上げると高域が吸われて暗い残響になる
- 数値: 録音(16秒)は ピーク -4.5 dBFS・RMS -18.0 dBFS・<200Hz 93%・200〜800Hz 6%。聴感は未確認
- 聴きどころ: 約 0〜1.7 秒でリフが跳ねるか、オクターブ重ねで太く聞こえるか
- 課題: `lo_offsets` の最後の `7` を `10`(短7度)にして、リフの終わりを比べる
- 関連: L055, L059, L060

### L062 キック: 3層(bd_klub + bd_haus + bd_boom)+ リバースキック
- タグ: #キック #kick #強いキック #bd_klub #bd_haus #bd_boom #リバースキック #reverse-kick #逆再生 #rate #sample_duration #ヘッドルーム #headroom #音量バランス #mix-balance
- 日付 / 曲: 2026-10-17 / Dark Future Bass x Phonk(`work/current.rb` の `kick` `kick3` `kick2` `live_loop :kick_rev`)
- 決めた人: ユーザーの指示(強めのキックを重ねる、リバースのキックを2・4小節目の終わりに重ねる、キックが弱いので別のキックを重ねる、強いキックのサンプルに替える)。サンプルの選び・amp は AI が決めた
- 選んだ案: 基本キックを bd_808 から bd_klub(硬く鋭い)に、重ねを bd_fat から bd_haus(パンチ)に替え、リフの位置に bd_boom(低域が太い)を重ねる。リバースキックは bd_808 を `rate: -1` で逆再生し、`sample_duration` ぶん前から鳴らして小節線で終わらせる(2小節周期)。`amp` は bd_klub 1.0・bd_haus 0.9・bd_boom 1.2。初めは bd_klub 1.6 / bd_haus 1.5 でピーク -1.0 dBFS(割れる寸前)になり下げた
- コード: `kick = grid_voice :sample, :bd_klub, amp: 1.0, lpf: 100` / `sample :bd_808, rate: -1, …` / `sleep 8 - d`(`d = sample_duration(:bd_808, rate: 1)`)
- 意味(理論): キックを層にすると、アタック(硬さ)と低域の太さを別のサンプルで役割分担できる。同時に鳴ると位相がずれて濁ることがある。逆再生は音量が最後に最大になるので、小節線に向かって吸い込まれる盛り上がりになる(リバースシンバルの代わり)。サンプルは `amp` に比例して大きくなるので、層を足すとピークがすぐ上がる
- 数値: 録音(16秒)は ピーク -3.7 dBFS・RMS -16.3 dBFS・<200Hz 92%(キックを重ねる前は -20.3 dBFS 前後)。余裕は約 3.7dB。リバースキックが小節線ちょうどかは未測定・未確認
- 聴きどころ: 約 0〜0.9 秒で3つのキックが濁らず強いか / 約 3.0〜3.4 秒の逆再生が3小節目の頭に向かうか
- 課題: `kick` の `:bd_klub` を `:bd_zum` に替えて、質感を比べる
- 関連: L055, L061

### L063 vox(ボーカルチョップ風)+ ディストーション + EQ
- タグ: #vox #ボーカルチョップ #vocal-chop #フォルマント #formant #grid_vsing #ディストーション #distortion #EQ #eq #リバーブ #reverb #パン #pan #16分 #配置
- 日付 / 曲: 2026-10-17 / Dark Future Bass x Phonk(`work/current.rb` の `grid_formants` `grid_vsing` `vox_pat` `live_loop :vox`)
- 決めた人: ユーザーの指示(voxを作り細かく配置、ディストーションを加える、上げる、ampを下げる/上げる、EQで高音を減らし低音を増やす)。音節・音高・配置・数値は AI が決めた
- 選んだ案: `docs/vocal-helper.rb` の `vsing` を `grid_vsing` に写し、saw を母音のフォルマント(F1 F2 F3)の `bpf` 3つに通して声に聞かせる。音節 `ha ya o a ya ho` ほか、16分の裏(奇数小節 2 5 7 10 13 15 / 偶数小節 1 4 6 9 11 14)に 0.2 拍で散らす。音高は和音の根音から 根音・5度・オクターブ(Eb4 付近)。`distort` 0.85、`lpf` 105、`eq`(low_shelf +0.5 @ 262Hz、high_shelf -0.6 @ 831Hz)、リバーブ。`vox_amp` は 0.4 → 0.8 → 0.5 → 0.2 → 0.12 → 0.16 → 0.2。選ばなかった案: NEUTRINO の歌声をボコーダーにして `grid_chop` で切る方法
- コード: `grid_vsing vox_syl[k], bass_midi[(i / 16) % 4] + 36 + vox_off[k], 0.2, vox_amp * lvl, pan` / `with_fx :distortion, distort: 0.85 …` / `with_fx :eq, low_shelf: 0.5, low_shelf_note: 60, high_shelf: -0.6, high_shelf_note: 80`
- 意味(理論): 声の母音は、口の形で決まる共鳴(フォルマント)の位置の違い。鋸波を帯域通過フィルタに通すと、母音らしい響きになる。短く散らす16分の配置で、phonk のチョップ感が出る。ディストーションは倍音を増やして荒くする。歪みの強さは入力の `amp` に依存する(`amp` を下げると歪みも弱まる)。EQ の `shelf` は、指定の周波数より上(または下)をまとめて持ち上げ・削る
- 数値: 録音(16秒)は ピーク -3.4 dBFS・RMS -16.4 dBFS・0.8〜4kHz 1%。最初の `amp` 0.4 では 800〜2500Hz が +0.7dB でほとんど聞こえず、0.8 + `distort` 0.85 では中高域 11% まで増えた。聴感は未確認
- 聴きどころ: 約 0.1〜0.9 秒で ha・ya が隙間に散らばるか、荒さを残して聞き取れるか
- 課題: `high_shelf: -0.6` を -0.3 に緩めて、聞き取りやすさの変化を聴く
- 関連: L057, L061

### L064 ベースと glitch のディストーション
- タグ: #ディストーション #distortion #ベース #bass #サブベース #sub-bass #サイン波 #sine #倍音 #harmonics #glitch #グリッチ #amp #distort
- 日付 / 曲: 2026-10-17 / Dark Future Bass x Phonk(`work/current.rb` の `with_fx :distortion` を掛けた `:bass_sub` `:bass_saw` と `:glitch`)
- 決めた人: ユーザーの指示(ベースにディストーションを掛ける、glitch に掛ける)。「他に掛けたほうがいいステムは?」への AI の推薦(glitch・強いキック・スネア)から、glitch をユーザーが選んだ。`distort` の量は AI が決めた
- 選んだ案: ベースは `distort` 0.4・`amp` 0.7 で戻す。glitch は `distort` 0.5・`amp` 0.6。選ばなかった案: 強いキック・スネア・スタブ・ピアノへの歪み(ピアノ・カウンター・ハットは非推奨と伝えた)
- コード: `with_fx :distortion, distort: 0.4, mix: 1.0, amp: 0.7 do live_loop :bass_sub … end`
- 意味(理論): サイン波は倍音がないので、歪ませると奇数倍音が生まれ、小さなスピーカーでも低音が聞こえるようになる(Eb1 は約 39Hz で、再生できない機器が多い)。歪みで音量が上がるので、`amp` で戻す。短い刻み(glitch)は、歪ませてもほかの音を濁らせにくい
- 数値: ベース歪み後の録音は ピーク -5.2 dBFS・RMS -17.9 dBFS。glitch 歪み後は -5.5 dBFS で、全体の数値はほとんど変わらない(短い刻みのため)。聴感は未確認
- 聴きどころ: 約 0〜1.7 秒でベースに荒い倍音が乗るか / 約 6.4〜6.9 秒の glitch の4連がざらつくか
- 課題: ベースの `distort` を 0.4 から 0.7 にして、荒さが太さと輪郭のどちらを強めるか聴く
- 関連: L052, L057, L059

### L065 パワーコードのペダルポイント
- タグ: #パワーコード #power-chord #ペダルポイント #pedal-point #ディストーション #distortion #dsaw #ブリッジミュート #palm-mute #5度 #オクターブ
- 日付 / 曲: 2026-10-17 / Dark Future Bass x Phonk(`work/current.rb` の `live_loop :power`、`pc_pat` `pc_amp`)
- 決めた人: ユーザーの指示(パワーコードを追加→ベースのペダルポイントにする→小さく)。リズム・音色・数値は AI が決めた
- 選んだ案: 根音 + 5度 + オクターブ(Eb3 Bb3 Eb4)を Eb に固定(ベースが Cb・Ab・Bb に動いても動かさない)。`dsaw` の `cutoff` 85、`distort` 0.6、`lpf` 100、軽いリバーブ。リズム `X.x. ..x. X... x.x.`(X は 0.5 拍、x は 0.12 拍のブリッジミュート風)。`pc_amp` は 0.35 → 0.25。初めは根音がベースに追従する案だった(ユーザーがペダルポイントに変更)
- コード: `r = bass_midi[0] + 24` / `play [r, r + 7, r + 12], …, sustain: sus`
- 意味(理論): パワーコードは3度がない和音で、長調・短調のどちらにも聞こえ、歪ませると重く攻撃的になる。根音を Eb に固定すると、ベースの動きに対して、Cb で長3度(Cbmaj7 の構成音)、Ab で5度、Bb で4度(Bb7 の構成音の外。サスペンド風の緊張)と、同じ音の意味が変わる。ペダルポイントは、低音を固定して上の和声を動かす手法
- 数値: 録音(16秒)は ピーク -3.2 dBFS・RMS -16.4 dBFS(`pc_amp` 0.25)。固定前は -3.6 dBFS。聴感は未確認
- 聴きどころ: 約 5.1〜6.9 秒(4小節目の Bb の上の Eb)の緊張 / 頭の X の長い音と x の短い音のチャグ
- 課題: `bass_midi[0]` を `bass_midi[3]`(Bb)に変えて、固定する音の違いを聴く
- 関連: L055, L061, L064

### L066 疑似サイドチェイン + 先読みの調整
- タグ: #サイドチェイン #sidechain #level #amp_slide #control #ダッキング #ducking #set_sched_ahead_time #timing #キック #kick
- 日付 / 曲: 2026-10-17 / Dark Future Bass x Phonk(`work/current.rb` の `sc_pat` `grid_pump_hit` `with_fx :level` と `pump_*` ループ)
- 決めた人: ユーザーの指示(サイドチェインを掛ける)。技法はユーザーが最初に選んだもの。対象・深さ・戻りの長さは AI が決めた
- 選んだ案: Sonic Pi には外部入力のサイドチェインがないので、`with_fx :level` の `amp` を、キックの強い位置(0・8 / 0・10 マス)で `sc_depth` 0.3 まで一瞬下げ、`sc_rel` 0.35 拍かけて 1 に戻す(`control` と `amp_slide`)。対象はベース・コード(スタブ + glitch)・ピアノ2本・パワーコード。キック・スネア・ハット・カウンター・vox は対象外。ループが増えて `thread got too far behind time` が出たので、`set_sched_ahead_time! 1` を足した
- コード: `control node, amp: depth, amp_slide: 0.01` → `time_warp 0.02 do control node, amp: 1, amp_slide: rel end` / `set_sched_ahead_time! 1`
- 意味(理論): サイドチェインは、キックが鳴る瞬間に他の音を凹ませ、キックの低域を空ける手法。戻る早さが「息をする」感じを決める(0.35 拍 ≒ 0.15 秒)。先読み(`sched_ahead_time`)を増やすと、処理が重いときでも、音の再生が遅れにくい(代わりに、ライブコーディングの反応が遅れる)
- 数値: 録音(16秒)は ピーク -5.4 dBFS・RMS -18.2 dBFS。凹みが効いているかは、録音の波形では確認できず、未確認
- 聴きどころ: 約 0〜0.9 秒でキックの瞬間にベースとコードが引っ込み、すぐ戻るか
- 課題: `sc_depth` を 0.3 から 0.1 にして、息の深さを聴く
- 関連: L062, L064

### L067 曲の構成: セクションごとにステムを切り替える(grid_gate)と 64小節の並び
- タグ: #構成 #structure #セクション #section #イントロ #intro #ビルドアップ #build-up #ドロップ #drop #ブレイク #break #アウトロ #outro #grid_gate #tick #コード進行 #chord-progression
- 日付 / 曲: 2026-10-17 / Dark Future Bass x Phonk(`work/song.rb`、`work/structure.md`)
- 決めた人: ユーザーが並び(イントロ → ビルド → ドロップ → ブレイク → ドロップ → アウトロ)を選び、「全部作って順に鳴らして」と指示。各セクションの長さ・進行・楽器・つなぎは AI が決めた。ユーザーが「すべて進めて」(2026-10-17)と言ったので、構成表に ✔ を付けた
- 選んだ案: 64小節(イントロ 8 → ビルド 6 → ドロップ前の静寂 2 → ドロップ 16 → ブレイク 8 → ドロップ 16 → アウトロ 8)。進行はドロップが i – ♭VI – iv – V7(Ebm9 – Cbmaj7 – Abm7 – Bb7)、イントロ/アウトロが i – i – ♭VI – ♭VI(動きを少なく)、ビルドが iv – ♭VI – ♭VII – V7(緊張)、ブレイクが ♭III – ♭VII – i – ♭VI(浮遊)
- コード: `define :grid_gate do |name, bars, &blk| … tick(name) * bars … end` / `live_loop :hat do grid_gate(:hat, 2) { |sec, rts, bar| grid_play hat, … } end`
- 意味(理論): Sonic Pi の `live_loop` は独立に回るので、曲の流れを作るには「いま何小節目か」を各ループが自分で数える。`tick(名前)` は各ループのスレッドごとに数えるので、全ループが同じ時間軸（0 から）で並ぶ。鳴らさないセクションは、ループの長さぶん `sleep` して拍を保つ。ドロップは進行を変えず、前後（イントロ、ブレイク）は動きを少なくするか、別の進行にして、落差と変化を作った。選んだつなぎ方では、ビルドの Bb7（V7）がドロップへ向かうセカンダリードミナントに近い働きをする
- 数値: 録音(115秒)の 2秒ごとの RMS は、イントロ約 -34 dBFS → ビルド約 -22 → ドロップ約 -16 → ブレイク約 -28 → ドロップ約 -16 → アウトロ約 -29。ピーク -3.7 dBFS。聴感は未確認
- 聴きどころ: 約 27秒(ドロップの頭)の落差 / 約 55秒(ブレイク)の静けさ / 約 96秒以降(アウトロ)の終わり方
- 課題: `grid_song_stems` のドロップから `:glitch` を抜いて、2回目のドロップだけ変化を付ける
- 関連: L055, L058, L061

### L068 土台と上モノ + ドロップ内で音を止める(4・8小節ごと)
- タグ: #土台 #foundation #上モノ #top-layer #レイヤー #layer #無音 #silence #ブレイク #break #インパクト #impact #with_fx #level #control
- 日付 / 曲: 2026-10-17 / Dark Future Bass x Phonk(`work/song.rb` の `grid_song_base` `grid_song_top` `live_loop :gap`)
- 決めた人: ユーザーの指示（「上モノと土台に分けたい」「4・8小節目の終わりで音を止めて無音を作ると、次のキックとベースのインパクトが跳ね上がる」の提案を実装）。ゲインの大きさ・長さ・対象セクションは AI が決めた
- 選んだ案: 土台（リズムと低音: キック3層・スネア・ハット・808ベース・ピアノ（下）・パワーコード・逆再生キック）と上モノ（和音と高音: スタブ・Eb7・glitch・ピアノ（上）・カウンター）をセクションごとに別々に選ぶ。ドロップの 4小節ごとの終わりは 0.5 拍、8小節ごとの終わりは 1 拍、master の amp を 0 にする。逆再生キックだけ master の外に置く
- コード: `with_fx :level, amp: 1 do |master| … control master, amp: 0, amp_slide: 0.005 … end` / `gap4 = 0.5` `gap8 = 1.0`
- 意味(理論): 音を一瞬止めると、次の拍の音が「無音からの立ち上がり」になるので、実際の音量以上に大きく感じる（コントラスト）。短い無音ではキックとベースが目立つ。逆再生キックを無音の中に通すと、次の頭に吸い込まれる。土台と上モノを分けると、セクションごとに「リズムを抜く／和音を抜く」を独立に決められる
- 数値: 録音で、8小節目の終わりの直前の 0.5 拍が -55.1 dB(ほぼ無音)。そのあとの 0.5 拍は -25.2 dB（逆再生キック）。通常の小節の終わりは -20.9 dB。聴感は未確認
- 聴きどころ: 約 28 秒・31 秒付近（ドロップの 4・8小節目の終わり）の止まり方
- 課題: `gap4` を 1.0 にして、4小節ごとの区切りと 8小節ごとの区切りの強弱を比べる
- 関連: L066, L067

### L069 ドロップ前: ライザーなしの静寂 + ハットの 16分への盛り上げ
- タグ: #ドロップ前 #pre-drop #静寂 #silence #ハイハット #hi-hat #16分 #sixteenth #ロール #roll #クレッシェンド #crescendo #逆再生キック #reverse-kick
- 日付 / 曲: 2026-10-17 / Dark Future Bass x Phonk(`work/song.rb` の `:predrop` セクション、`h_pat_build`、`grid_hat_pat`)
- 決めた人: ユーザーの指示（「ライザーを使わず、キックやドラムの静寂でドロップ前を表現して」「ハイハットでドロップに向かって16分まで刻んで盛り上げて」）。静寂の長さ（2小節）と刻み方の段階は AI が決めた
- 選んだ案: ビルド(9〜14小節)のハットを、2小節ごとに 8分 → 8分 + 弱い 16分 → 16分の連打（拍の頭を強く）と細かくする。15〜16小節は逆再生キックだけ残して全部止める（静寂）。ライザー(ノイズ)は使わない
- コード: `h_pat_build = [h_pat, "x.oo x.oo …", "Xxxx Xxxx …"]` / `when :predrop then [:kick_rev]`
- 意味(理論): ライザーは音で緊張を上げるが、静寂は「音を引く」ことで緊張を作る。刻みを細かくするのは、密度（リズムの細かさ）で盛り上げる定番の手法。16分に達したあと一気に無音にし、ドロップで全部入ると落差が最大になる
- 数値: ハットの帯域(4kHz 以上)の RMS が 9〜10小節 -55.9 dB → 13〜14小節 -52.1 dB(+3.8 dB)。15〜16小節 -68.3 dB(静寂)。聴感は未確認
- 聴きどころ: 約 24〜27 秒(16分の連打)→ 27.4 秒（静寂）→ 約 31 秒（ドロップの頭）の落差
- 課題: 13〜14小節のパターンを `XxXx XxXx XxXx XxXx` に変えて、切迫感を比べる
- 関連: L062, L067, L068

### L070 ピアノのリフ 16小節ループ(A → A' → B → C)
- タグ: #ピアノ #piano #リフ #riff #16小節 #phrase #フレーズ #反復と変化 #variation #grid_song_rel
- 日付 / 曲: 2026-10-17 / Dark Future Bass x Phonk(`work/song.rb` の `riff_pats` `riff_offs`、`live_loop :piano_lo` `:piano_up`)
- 決めた人: ユーザーの指示（「ピアノのメロディを16小節ループにして」）。フレーズの内容は AI が決めた
- 選んだ案: 4小節のフレーズを 4つ並べる。A（今までのリフ）→ A'（A とほぼ同じで、8小節目の終わりに 16分の駆け上がり）→ B（別のリズムと高めの音）→ C（8分の刻みで盛り上げ、最後は 16分の駆け上がり）。音は根音 +0・+7・+12・+19 半音だけ（3度は使わない）。各セクションの頭から数える
- コード: `ph = (grid_song_rel(bar) / 4) % 4` / `grid_each(riff_pats[ph])` / `play rts[(i / 16) % 4] + 12 + offs[k], …`
- 意味(理論): 同じリフを 16小節繰り返すと単調になる。4小節ごとに少しずつ変え（A'）、半分でリズムを変え（B）、最後に密度を上げる（C）と、「前半は安定、後半は展開」の山ができる。根音・5度・オクターブだけなので、和音が変わる小節でも濁らない
- 数値: 録音(115秒)は ピーク -3.7 dBFS・RMS -19.3 dBFS（16小節化の前後で変化なし）。聴感は未確認
- 聴きどころ: 約 41〜48 秒（C）の 8分の刻み / 8・16小節目の駆け上がり（止める処理で切れる可能性）
- 課題: B の最初の小節を `"X..x ..x. X.x. ..x."` に変えて、重心の違いを聴く
- 関連: L061, L068

### L071 ドロップの2周と、楽器を少しずつ足す(32小節の山)
- タグ: #ドロップ #drop #段階的な展開 #layering #レイヤー #密度 #density #繰り返しと変化 #variation
- 日付 / 曲: 2026-10-18 / sea_sky_night(`work/daw/sea_sky_night.json` 46〜77小節)
- 決めた人: ユーザーの指示(「最後のドロップの32小節分に持っていって」「1周目と2周目の両方ですべての音を」)。足す順番は AI が決めた
- 選んだ案: 16小節の進行を2周。最初は核(キック・ベース・ピアノ・パッド)だけで、4小節ごとにキック2・ゴースト → 下のピアノ・パワーコード → 上のピアノ → pluck・prophet・対旋律 → クラップと足す。のちに、2周目だけだった楽器を1周目にも入れ、2周とも全部で鳴らす形に変更(山は「足す」から「全部で2周」へ)
- コード: 各トラックの `notes` を 2周目(244〜308拍)から1周目(180〜244拍)へ 64拍ずらして複製
- 意味(理論): 同じ16小節を繰り返すと単調になるため、密度(同時に鳴る音数)を段階的に上げて、前へ進む感じを作る。全部を最初から鳴らすと、2周目に上げ幅が残らない。2周とも全部で鳴らすと、迫力は一定になるが、展開は進行・ハモリ・フィルに頼る
- 数値: 録音の長さ 153.2 秒(83小節)。ピークは 3回の変更後は未計測(直近の測定は -0.1 dBFS)
- 聴きどころ: 約 1:07(46小節)と約 1:37(62小節)で、楽器数が同じに聞こえるか
- 課題: pluck の `amp` を 0.65 → 0.4 にして、2周目の「新しさ」が戻るか聴く
- 関連: L068, L070

### L072 ドロップ前の「波打つローパス」と無音の1拍・riser・リバース
- タグ: #ローパスフィルター #lpf #オートメーション #automation #riser #ライザー #リバースシンバル #reverse-cymbal #リバースキック #間 #無音 #フィル #fill
- 日付 / 曲: 2026-10-18 / sea_sky_night(`predrop_lpf`、42〜45小節)
- 決めた人: ユーザーの指示(「ドロップに向かうLPFを波打つように」「壊れる音を普通のドラム・ハット・riserで置き換えて」「フィルでリバースキックを加えて」)。波の周期・数値は AI が決めた
- 選んだ案: LPF の cutoff を `automation` で上下させ、音を弱める/戻すを繰り返す。通常のドラム+ハット・スネアのロール、ambi_swoosh の riser、rate を負にしたシンバル(-0.7)とキック(-1)の逆再生。最後の1拍は無音にして、ドロップの落差を作る
- コード: fx `lpf` の `automation: {param: "cutoff", points: [[拍, 値], …]}` / `rev_cym` は `sample :drum_cymbal_open, rate: -0.7`
- 意味(理論): フィルターで高域を削ると音がこもり、開くと前に出る。波打つと、ドロップへの期待が呼吸のように高まる。逆再生は「音が膨らんで、拍の頭に着く」形になるので、小節頭の直前に置く。最後の無音は、直前との落差(コントラスト)が大きいほど、次の1拍目が強く聞こえる
- 数値: `rev_cym` amp 0.7 / rate -0.7(位置は 7・31・43・59小節目の後半、各1回)/ `rev_kick` amp 0.8
- 聴きどころ: 約 1:00〜1:04(ドロップ手前)で、こもりと戻りの繰り返しと、最後の無音
- 課題: `rev_cym` の位置を 11マス目から 9マス目に動かし、ドロップとの距離の違いを聴く
- 関連: L010, L011, L069

### L073 ゴーストノートとキックの細分化(シンコペーションの勢い)
- タグ: #ゴーストノート #ghost-note #シンコペーション #syncopation #キック #kick #スネア #snare #ハイハット #hi-hat #ベロシティ #amp #16分グリッド
- 日付 / 曲: 2026-10-18 / sea_sky_night(`snare_ghost`、`hat_ghost`、`kick2`)
- 決めた人: ユーザーの指示(「ドラムにシンコペーション」「スネアのゴーストノートも」「シンコペーションに向かって音が細かくなる感じ」)。位置は AI が決めた
- 選んだ案: 本番のスネアの間に、とても小さい音(amp 0.2)のスネアを16分の裏に置く。ハットも小さい別トラック(amp 0.14)で細かく。キックは、シンコペーションの手前で間隔を詰めていく
- コード: `snare_ghost`(sn_dolf, amp 0.2)/ `hat_ghost`(hat_cab, amp 0.14)を別トラックにし、本体とは別に `steps` を書く
- 意味(理論): 強い拍だけだとリズムが平らになる。小さい音を裏に足すと、強弱の差で「ノリ」が出る。音が細かくなっていくと、次の強い拍に向かって加速して聞こえる。別トラックにすると、amp とミュートを独立して扱える
- 数値: ゴースト amp 0.2 / 0.14(本体 snare 0.55・hat 0.35 の約 1/3〜2/5)
- 聴きどころ: 約 0:40〜0:55(ドロップ1)のスネアの間の細かい音
- 課題: `snare_ghost` の amp を 0.2 → 0.35 にして、ノリが「うるさい」に変わる境目を探す
- 関連: L002, L006, L023

### L074 ピアノの9thと、高音のアルペジオ
- タグ: #9th #テンション #tension #4和音 #アルペジオ #arpeggio #ピアノ #piano #コードトーン #chord-tone #音域の住み分け #オクターブ重ね
- 日付 / 曲: 2026-10-18 / sea_sky_night(`hipiano`、`hipiano_arp`、`hipiano_up`、`hipiano_down`)
- 決めた人: ユーザーの指示(「9thのテンション」「セブンスコード+9thの4和音」「アルペジオを加える」「ピアノを1つ上と下のオクターブで重ねて」)。音の選び方(3rd・5th・7th・9th)は AI が決めた
- 選んだ案: 9th を単音で足すと、メロディとぶつかる。3rd・5th・7th・9th の4音の和音にして、下のパッドの実音と合う 7th/3rd を選ぶ。ドロップの最後は、メロディを置き換えず、別トラック `hipiano_arp` で 8分音符の 根→3rd→5th→7th→9th→戻る を重ねる。オクターブ上・下の2トラックで厚みを出す
- コード: `hipiano_arp`(piano, amp 0.3, pan -0.2, 8分刻み)。`piano` は amp を 0.2 倍する特別扱い
- 意味(理論): 9th(根音の2度上のオクターブ上)は、明るく浮く響き。7th を足して4和音にすると、単音より濁りにくい。アルペジオは、和音を時間に並べて動きを作る。メロディと同じ音域で重ねると濁るので、別トラック・左右(pan)で分ける
- 数値: アルペジオ amp 0.3 / pan -0.2、基準オクターブ 4、60小節目の最後の拍は休み。濁りの確認は `analyze2.py` で、短2度・長7度・トライトーンの衝突なし
- 聴きどころ: 約 1:07 以降の高音の粒と、メロディとの分離
- 課題: `hipiano_arp` の pan を -0.2 → 0.6 にして、左右の分離を聴く
- 関連: L012, L013, L018

### L075 グライド・ピッチベンド・パラメータのオートメーション
- タグ: #グライド #glide #ポルタメント #portamento #ピッチベンド #pitch-bend #オートメーション #automation #control #slide
- 日付 / 曲: 2026-10-18 / sea_sky_night(`voice.glide`、ノートの4番目の値、fx の `automation`)
- 決めた人: ユーザーの指示(「グライドを使った方が自然なメロディは？」「シンセに glide」「ピッチベンド」「フィルターの変化時間を短く」)。値は AI が決めた
- 選んだ案: シンセ(bass・melody)に、次の音が続くとき最後の `glide` 拍で滑る `note_slide` を付ける(prophet は 0.25拍)。ピアノは音程を滑らせられないので対象外。ベンドは音の長さ全体で音程を動かす。ピッチベンドのグリッチ音は、ユーザーが削除した
- コード: `voice.glide = 0.25` → `control node, note: …`、`automation.points = [[拍, 値], …]` → `<param>_slide`
- 意味(理論): 歌や弦楽器は音を滑らせてつなぐ。滑りが長すぎると音程が不明瞭になり、短いとレガートだけが残る。0.25拍(130 BPM で約 0.115 秒)は、メロディの輪郭を保てる範囲(未確認)
- 数値: glide 0〜2 拍で指定、prophet は 0.25
- 聴きどころ: prophet のメロディの音の移り目
- 課題: `glide` を 0.25 → 1 にして、音程が曖昧になる点を探す
- 関連: L008

### L076 prophet の3度下ハモリ
- タグ: #ハモリ #harmony #3度 #third #下ハモリ #コードトーン #chord-tone #prophet #音階 #scale
- 日付 / 曲: 2026-10-18 / sea_sky_night(`lead` + `lead_harmony`、46〜77小節)
- 決めた人: ユーザーの指示(「prophet にハモリを追加」)。音程の選び方は AI が決めた
- 選んだ案: メロディの各音から 3・4・5 半音下の候補を取り、その小節のコードトーンを優先、次にキーの音階の音を選ぶ。2度下(短い間隔)は濁るので候補から外す。ハモリなしの prophet は 1回目のドロップにも足した
- コード: `lead_harmony`(prophet, amp 0.2, pan -0.2, glide 0.25)。本体は amp 0.25 / pan 0.15
- 意味(理論): 3度のハモリは、2音が協和して厚みが出る(短3度 3 半音・長3度 4 半音)。コードトーンに乗せると、和音が変わっても濁りにくい。左右に振ると、2音が分離して聞こえる
- 数値: 96音(46〜77小節)。メロディとの間隔は 3〜5 半音のみ。聴感は未確認
- 聴きどころ: 約 1:07 以降の prophet の2声
- 課題: ハモリを 3度下 → 6度下(8〜9 半音)にして、響きの違いを聴く
- 関連: L018

### L077 パワーコードを最後のドロップだけで(重ならない・長さをそろえる)
- タグ: #パワーコード #power-chord #ディストーション #distortion #シンコペーション #syncopation #重なり #tri #音を引く
- 日付 / 曲: 2026-10-18 / sea_sky_night(`power`、`power_dist`、54〜77小節)
- 決めた人: ユーザーの指示(「ドロップでパワーコード」「伸ばしてベースを支えて」「短めでシンコペーション」「長さは同じ」「重ならないように」「最後のドロップのみ」「dsaw はギザギザしてメロディとぶつかる」)。音色 tri は AI が決めた
- 選んだ案: 根音+5度(+オクターブ)の和音を、0.5拍で同じ長さにそろえ、前の音と重ならないようにする。音色は tri(倍音が少なく、メロディとぶつからない)、軽い歪み(distortion 0.4・mix 0.35)。1回目のドロップには入れず、最後だけ
- コード: `power`(tri, amp 0.2, cutoff 80)/ `power_dist`(fx distortion)/ 同じ高さの音は重ねない
- 意味(理論): 5度の和音は3度を持たず、長調でも短調でも使える。歪みは倍音を増やして力強くするが、鋸波(dsaw)は倍音が多く、メロディと帯域が重なるため、tri に変更した。長さをそろえると、リズムが固まる
- 数値: `power` amp 0.2 / cutoff 80 / 351 音のトラック(4096 音の上限内)
- 聴きどころ: 約 1:10 以降のベースの上の刻み
- 課題: `cutoff` を 80 → 110 にして、メロディとの帯域の被りを聴く
- 関連: L005, L009

### L078 海と空の glitch(ノイズ + ビットクラッシャー)
- タグ: #グリッチ #glitch #ノイズ #noise #bnoise #cnoise #ビットクラッシャー #bitcrusher #テクスチャ
- 日付 / 曲: 2026-10-18 / sea_sky_night(`sea_glitch`、`sky_glitch`、`glitch_crush`)
- 決めた人: ユーザーの指示(「海と空のノイズを glitch として」)。音色は AI が決めた
- 選んだ案: 海はこもったノイズ(bnoise)、空は明るいノイズ(cnoise)。短い音を置いて、bitcrusher(bits 6・sample_rate 5000・mix 0.7)で粗くする。ロボット系は不採用
- コード: `with_fx :bitcrusher, mix: 0.7, bits: 6, sample_rate: 5000`
- 意味(理論): ノイズは、音程を持たない質感として、テーマ(海・空)を支える。ビット数とサンプルレートを下げると、デジタルの粗さが出る
- 数値: bits 6 / sample_rate 5000 / mix 0.7
- 聴きどころ: ブレイク〜ビルド付近のノイズの粒
- 課題: `bits` を 6 → 3 にして、粗さを聴く
- 関連: L015

### L079 イントロのローパスと低音ピアノ・アウトロの閉じ方
- タグ: #ローパスフィルター #lpf #オートメーション #automation #イントロ #アウトロ #outro #フェードアウト #音域の住み分け #ピアノ #piano
- 日付 / 曲: 2026-10-18 / sea_sky_night(`intro_lpf`、`pad_low`、`end_lpf`、78〜83小節)
- 決めた人: ユーザーの指示(「ローパスで音をぼかして、徐々に開く」「短めのアウトロ」「ピアノの溜めをなくす」)。数値は AI が決めた
- 選んだ案: 低いピアノの7thの和音と pad_low から始め、フィルターを開く。アウトロは低いピアノのイントロ4小節+高いピアノのメロディの頭、最後に Bbm7 を2小節伸ばし、最後の8拍で cutoff を 130 → 45 に閉じる
- コード: `end_lpf` の `automation: cutoff 130 → 45`(最後の8拍)
- 意味(理論): 始まりと終わりを同じ素材にすると、曲が閉じた印象になる。フィルターで高域を削ると、音が遠くなる。溜め(0.125拍の遅れ)を外すと、拍にまっすぐ乗る
- 数値: アウトロ 6小節(約 11 秒)。全体は 83小節 ≒ 2:33
- 聴きどころ: 約 2:22〜2:33 の音が遠ざかる部分
- 課題: end の cutoff を 45 → 70 にして、終わり方の違いを聴く
- 関連: L013

### L080 同時に読み込めないとき: with_fx を in_thread で包む(技術メモ)
- タグ: #in_thread #too-far-behind #sched_ahead #スレッド #with_fx #再生トラブル
- 日付 / 曲: 2026-10-18 / sea_sky_night(`daw_codegen.py` の生成コード)
- 決めた人: AI が決めた(再生中に起きた不具合の修正。ユーザーは未確認)
- 選んだ案: 曲の途中から再生すると、読み込みに約 1.6 秒かかって、後ろの live_loop が「thread got too far behind time」で止まり、ピアノが消えた。各 `with_fx` のグループを `in_thread do … end` で包み、グループごとに読み込みを分けた。確認は `POST /api/player` の `errors` が空であること
- コード: `in_thread do / with_fx … / end`
- 意味(理論): Sonic Pi は、先に予約した時刻より遅れると、そのスレッドを止める。包んでおくと、1つの遅れが他に及ばない
- 数値: 読み込み約 1.6 秒 / `errors` は空(確認済み)
- 聴きどころ: 曲の途中(例: 40小節)から ▶ を押して、すべての楽器が鳴ること
- 課題: `GET /api/player` の `errors` を見て、止まったトラック名を探す
- 関連: L020

### L081 ハーフタイムのキック(0・2拍。暗い artcore の土台)
- タグ: #ハーフタイム #half-time #キック #kick #ベロシティ #velocity #隙間 #space
- 日付 / 曲: 2026-10-19 / dark_creep(`work/daw/dark_creep.json` の `kick`)
- 決めた人: ユーザーが選んだ(5案から①控えめを選択)。ベロシティの数値は AI が決めた
- 選んだ案: 1小節の 0拍と2拍にだけ打つ。②4つ打ち・③ブレイク・④808・⑤漸増は選ばず、隙間の多さを優先した
- コード: `voice: bd_pure, amp 1` / `hits: [[0,120],[2,100]]`(毎小節。BPM 125)
- 意味(理論): 1・3拍目(0拍・2拍)だけに置くと、体感の拍が半分に感じられる。間(1拍・3拍)が空くので、ピアノ・弦・ベースが入る余地が大きい。0拍(小節頭)を強く(120)、2拍を少し弱く(100)して、頭を重くする
- 数値: 125 BPM で 1拍 ≒ 0.48 秒、キックの間隔は 0.96 秒。録音での測定は未確認
- 聴きどころ: 画面の ▶ で 1〜8小節。キックの間が長く空いて、不穏な余白に聞こえるか
- 課題: `[2,100]` を `[2.5,100]` にずらして、ハーフタイムが崩れて跳ねる感じを聴き比べる
- 関連: L001

### L082 スネアとゴーストスネアを別トラックに分ける
- タグ: #ゴーストノート #ghost-note #スネア #snare #ハーフタイム #half-time #トラック分け #ベロシティ #velocity
- 日付 / 曲: 2026-10-19 / dark_creep(`work/daw/dark_creep.json` の `snare`・`ghost`)
- 決めた人: ユーザーの指示(③ゴースト付きを選び、「スネアとゴーストスネアを別のトラックとして配置」)。ベロシティの数値は AI が決めた
- 選んだ案: 主拍 `snare` は 2 拍(ベロシティ 100)、`ghost` は 1.75(20)と 3.75(40)。①控えめ(ゴーストなし)や②バックビート(1・3 拍)は選ばず、ハーフタイムを保ったままグルーヴを足した
- コード: snare `hits: [[2,100]]` / ghost `hits: [[1.75,20],[3.75,40]]`(毎小節。どちらも `sn_dolf`、amp 1)
- 意味(理論): 2 拍のスネアが拍の体感を半分にする(ハーフタイム)。その直前(1.75)と小節の最後(3.75)の弱い音が、次の強拍を呼び込む(ゴーストノート)。弱いので音量はほとんど変わらず、跳ねる感じだけが足される。別トラックにすると、ゴーストの `amp`・`pan`・FX を主拍と独立に調整できる(例: ゴーストだけ左右に振る、ハイパスで軽くする)
- 数値: ベロシティ 20 / 40 は 100 の 1/5〜2/5。実音量は未測定(「未確認」)
- 聴きどころ: ▶ で 1〜8 小節。ゴーストが聞こえるか聞こえないかの薄さで、2 拍・次の頭を呼び込んでいるか
- 課題: `ghost` トラックの `amp` を 1 → 0.5 に下げて、グルーヴの違いを聴く
- 関連: L081, L001

### L083 キックを軽く固い音に替える(bd_pure → bd_tek)
- タグ: #キック #kick #音色選び #帯域 #low-end #アタック #attack #サンプル測定
- 日付 / 曲: 2026-10-19 / dark_creep(`kick` の `voice`)
- 決めた人: ユーザーの指示(「軽やかで固く響く音に」)。サンプルの選定と `amp` は AI が決めた
- 選んだ案: `bd_pure`(全部が 100Hz 未満・長さ 0.43 秒の純粋なサブ)をやめ、`bd_tek` に変更。`bd_zum`(0.13 秒・高域が多い)や `bd_zome` は選ばず、低域も残る中間を選んだ
- コード: `voice: bd_tek, amp 1.5`(ユーザーが画面で 2.15 にしていた音量を、ピークが揃うよう下げた。L081 の位置・ベロシティはそのまま)
- 意味(理論): 重く沈んで聞こえる原因は、低域(100Hz 未満)に偏り、余韻が長いこと。軽く固くするには、100〜500Hz の「胴鳴り」を増やして音の重心を上げ、余韻を短くする
- 数値(Sonic Pi 同梱 wav の先頭 0.4 秒を FFT。録音ではない): `bd_pure` 100Hz 未満 100%・重心 47Hz・減衰 0.37 秒 → `bd_tek` 73%・重心 99Hz・減衰 0.21 秒、100〜500Hz が 27%。ピークは 0.95 → 1.41 なので、`amp` を 2.15 → 1.5(ピーク 約 2.04 → 2.1)にして音量を揃えた。実際の聴感は未確認
- 聴きどころ: ▶ で 1〜8 小節。キックが沈まずに打点がはっきりするか、スネア(2 拍)と重なる部分が濁らないか
- 課題: `bd_tek` を `bd_zum` に替えて、さらに軽く固い音との違いを聴く
- 関連: L081

### L084 3-3-2 のハット(跳ねるシンコペーション)
- タグ: #3-3-2 #シンコペーション #syncopation #ハイハット #hi-hat #ベロシティ #velocity #グルーヴ #groove #ゴーストノート
- 日付 / 曲: 2026-10-19 / dark_creep(`work/daw/dark_creep.json` の `hat`)
- 決めた人: ユーザーが選んだ(5案から③を選択)。ベロシティの数値は AI が決めた
- 選んだ案: 0、0.75、1.5、2、2.75、3.5 拍に `hat_cab`。①裏拍のみ・②16 分刻み・④増加・⑤抜きは選ばず、ハーフタイムの余白を残しつつ跳ねる形を優先した
- コード: `hits: [[0,80],[0.75,40],[1.5,60],[2,80],[2.75,40],[3.5,60]]`(毎小節。voice: hat_cab, amp 1)
- 意味(理論): 間隔が 0.75 → 0.75 → 0.5 の組(3-3-2)を 2 周すると 1 小節になる。16 分の 3・3・2 つ分で、ラテン系やブレイクビーツで多い型。表拍(0・2)を 80 にして土台を揃え、0.75・2.75 は 40 に落として、ゴースト(1.75・3.75)と半拍ずらした。強弱が音の揺れを作る
- 数値: 1 小節 6 打。16 分グリッド上の位置 0・3・6・8・11・14。実音量は未測定(「未確認」)
- 聴きどころ: ▶ で 1〜8 小節。ゴーストと重ならずに揺らぎが出ているか
- 課題: 3.5 のベロシティを 60 → 20 に下げ、次の小節へ向かう勢いの違いを聴く
- 関連: L082, L081

### L085 ペダルポイントのイントロ + フリジアンのドロップ(低音ピアノのベタ打ち)
- タグ: #ペダルポイント #pedal-point #フリジアン #phrygian #半音 #借用和音 #セクション構成 #導音 #leading-tone #低音ピアノ
- 日付 / 曲: 2026-10-19 / dark_creep(`pianolow`、1〜8 小節=イントロ、9〜16 小節=ドロップ)
- 決めた人: ユーザーの指示(「ペダルポイントで導入の安定感を出し、ドロップではフリジアンでメロディーを強調する」)。コードの声部配置と音量は AI が決めた
- 選んだ案: イントロ=①ペダル(Am / Bb/A / Am / Bb/A / Dm/A / Am / F/A / E7)、ドロップ=②王道フリジアン(Am / Bb / Am / Bb / Am / Dm / Bb / E7)。③アンダルシア・④半音上昇・⑤ディミニッシュは使わなかった
- コード: イントロは根音 A2 を全小節で鳴らし、上のコードだけ動かす(`a2` + `bb3 d4 f4` など)。ドロップは各コードの根音が変わる(`bb2 bb3 d4 f4`)。4 拍の全音符、ベロシティ 60、`piano` `amp` 0.2
- 意味(理論): ペダルポイント(同じ低音を保つ)では、上のコードが変わっても土台が動かないので、安定して聞こえる。ドロップで低音も Bb に動くと、A↔Bb の半音(フリジアンの♭II)が前面に出て、緊張が増す。ベタ打ちで動きが少ないぶん、メロディが際立つ余地になる。最後の E7(G# を借りる)は、次の Am へ向かう導音の引力を作る
- 数値: 各 8 小節 ≒ 15.4 秒(125 BPM、1 小節 1.92 秒)。録音での測定は未確認
- 聴きどころ: 約 15 秒(9 小節目)で、低音が A から動き出して緊張が変わるか
- 課題: ドロップの 9 小節目だけ Bb を Bb/A に変えて、低音が動かない場合と聴き比べる
- 関連: L081, L084

### L086 ドロップの主旋律: 長い音のピアノ(余白で暗さを作る)
- タグ: #主旋律 #melody #ロングトーン #long-tone #余白 #space #フリジアン #phrygian #導音 #leading-tone #ピアノ #piano
- 日付 / 曲: 2026-10-19 / dark_creep(`lead`、9〜16 小節=ドロップ)
- 決めた人: ユーザーが選んだ(5案から①控えめを選択)。音の並びとベロシティは AI が決めた
- 選んだ案: 2〜3 拍の長い音が中心(e5 → f5 → e5 → c5 …)。②半音モチーフ・③コール&レスポンス・④上昇・⑤増2度は選ばず、余白とストリングスの入る余地を優先した
- コード: `lead` の `notes`(例: 9 小節 `[0,"e5",3,80]`、10 小節 `[0,"f5",3,80]`、16 小節 `[0,"e5",1,80],[1,"gs5",1,100],[2,"a5",2,100]`)。`piano` `amp` 0.25
- 意味(理論): 長い音は拍の頭に置くだけで、音の数が少ない。e5 → f5(E と F の半音)は、フリジアンの♭II の迫り方が主音 A でなく E でも聞こえる。16 小節目の gs5(導音)が a5 に上がって、ループの頭の Am へつなぐ
- 数値: 音域 c5〜a5。ドロップ 8 小節 ≒ 15.4 秒。実音量は未測定(「未確認」)
- 聴きどころ: 約 15.4 秒(9 小節目)で e5 が長く伸びて、余白が暗さに聞こえるか
- 課題: 10 小節目の f5 を e5 のままにして、半音がない場合と聴き比べる
- 関連: L085

### L087 ヴァイオリンのメロディ2: ロングトーンとスタッカートの混合
- タグ: #ロングトーン #long-tone #スタッカート #staccato #対旋律 #counter-melody #3-3-2 #半音 #ヴァイオリン #violin #ベロシティ #velocity #コール&レスポンス
- 日付 / 曲: 2026-10-19 / dark_creep(`violin`、9〜16 小節=ドロップ)
- 決めた人: ユーザーの指示(「ロングトーンとスタッカートを混ぜた迫力のあるメロディ」)。音の並びとベロシティ・音量は AI が決めた(AI が書いたコード)
- 選んだ案: 5案(トレモロ・3-3-2・ラン・スフォルツァンド・半音トリル)から選ばず、長い音(3〜2 拍)と短い音(0.25 拍)を同じトラックに混ぜる形にした
- コード: 9 小節 `[0,"a4",3,100]`(長い音)+ `[3,"a4",.25,120],[3.25,"a4",.25,100],[3.5,"bb4",.25,120]`(スタッカート)。11・13 小節はスタッカートだけの 3-3-2(0、0.75、1.5、2、2.75、3.5)。16 小節は `gs4 → b4` の上昇から `[2,"b4",2,120]`。`violin_section`、`amp` 4、`pan` 0.3、`env` stab
- 意味(理論): 長い音は余韻で土台を作り、短い音は拍の頭にアクセントを刺す。長い音のあとに短い連打が来ると、息をつく間もない前のめりの勢いが出る(長短の対比)。ピアノ(e5〜a5)の下の a4〜d5 に置いて、音域を分けた。ピアノが休む位置(3 拍目付近)で短い音を鳴らし、掛け合いにした。11・13 小節の 3-3-2 はハットの位置と合わせて、リズムを一体にした。A と Bb の半音が終わりに鳴り(3.5 拍)、次の小節へ押す
- 数値: 音域 e4〜d5(wav は g2〜d5)。`violin_section` の wav ピークは -21.6 dBFS と小さいので `amp` を 4 にした(L086 のあと、`AMP_MAX` を 4 → 16 に拡大)。実際の音量は未測定(「未確認」)
- 聴きどころ: 約 15.4 秒(9 小節目)の長い a4 のあとの 3 拍目の短い音、約 21 秒(11〜12 小節)の 3-3-2 の刻み、約 29 秒(16 小節目)の上昇
- 課題: 11 小節目のスタッカートの長さ 0.25 を 0.5 に伸ばして、切れ味の違いを聴く
- 関連: L086, L084

### L088 低音ピアノを強音・弱音の2トラックに分け、スタッカートで細かく刻む
- タグ: #スタッカート #staccato #強弱 #dynamics #ゴーストノート #ghost-note #アルペジオ #arpeggio #ベロシティ #velocity #トラック分け #16分 #ピアノ #piano
- 日付 / 曲: 2026-10-20 / dark_creep(`pianolow` 強音、`pianolow_weak` 弱音。1〜16 小節)
- 決めた人: ユーザーの指示(「ベロシティごとに音を分け、ドラムと同様に弱音パートと強音パートにする。スタッカートで細かく弾く」)。刻む位置・音の並び・ベロシティの数値は AI が決めた
- 選んだ案: ベタ打ち(全音符のコード)をやめた。強音=0 拍(ベロシティ 80)と 2 拍(60)に、コードの全音を 0.25 拍で同時に弾く。弱音=0・2 拍を除く 16 分の 14 か所に、コードの構成音を上がって下がる順に 1 音ずつ 0.125 拍で弾く(3-3-2 の位置 0.75・1.5・2.75・3.5 は 40、ほかは 20)
- コード: 強音 `[b+0, 各音, 0.25, 80], [b+2, 各音, 0.25, 60]` / 弱音 `[b+0.25, 音, 0.125, 20]` など。どちらも `piano`、`amp` 1.45(ユーザーの値)。進行は L085 のまま
- 意味(理論): 強音がキック(0・2 拍)と同じ位置に和音で刺さり、リズムの骨格を作る。弱音はスネアのゴーストと同じ考えで、強音の間を細かい単音でつなぐ(ゴーストノート)。3-3-2 の位置を少し強くして、ハットの跳ねと揃える。短い音(0.125〜0.25 拍)なので、余韻が残らず、ベタ打ちより動きが出る。分けたので、強音と弱音を別の音量・FX で調整できる
- 数値: 強音 132 音、弱音 224 音。弱音の実音量は `amp 1.45 × 20 ÷ 60 × 0.2 ≒ 0.1`。実際の音量は未測定(「未確認」)
- 聴きどころ: ▶ で 1〜8 小節。0・2 拍の和音の刺さりと、その間の細かい動きがハットと揃うか。ヴァイオリンの長い音の下で、うるさくないか
- 課題: 弱音のベロシティを 20 / 40 → 40 / 60 に上げて、粒立ちが前に出る違いを聴く
- 関連: L085, L084, L082

### L089 フルートのソロイントロ: 明るい機能和声から、マイナーとサスで暗くする
- タグ: #ソロ #solo #レガート #legato #機能和声 #functional-harmony #sus4 #sus-to-tonic #マイナーの増加 #休符 #rest #リリース #release #分散和音 #arpeggio
- 日付 / 曲: 2026-10-20 / dark_creep(`flute`、`flute_end`。1〜16 小節=ソロ、17〜18 小節=休符)
- 決めた人: ユーザーが選んだ(②の旋律を採用)+ ユーザーの指示(16 小節 + 休符 2 小節、最後の音を伸ばして大きなリリース、徐々にマイナーを増やす、sus コード + トニックを入れる)。8〜16 小節の旋律・コードの並び・数値は AI が決めた
- 選んだ案: 1〜7 小節は F メジャーの I – V – IV – V – I(F / C / Bb / C / F / C / Bb)。8 小節目の Dm から、マイナーを増やす(Dm / C / Gm / Dm / Gm / Dm / Bb / Am)。他の音は鳴らさず、スケールは A フリジアンのまま
- コード: 旋律は和音の構成音中心の 2 拍ずつ。sus + トニックは 6 小節(Csus4 → C: f5 → e5)、14 小節(Dsus4 → Dm: g4 → f4)、16 小節(Asus4 → Am: d5 → c5)。16 小節の最後の a4(2 拍)は `flute_end` に分けて、`release` 4 拍、`attack` 0.15
- 意味(理論): F メジャーの属和音 → 主和音(C → F)の引力と、分散和音の旋律が、クラシカルな明るさを作る。sus4(4 度の音)は和音の 3 度を待たせる緊張で、下がって解決(f → e、g → f、d → c)すると、安心感が一瞬だけ戻る。マイナーを少しずつ増やすと、同じ旋律の動きでも、明るさが減って暗くなる。休符 2 小節は、直前の長音の余韻(リリース)が溶けていく空白で、次のビルドアップの入りを際立たせる
- 数値: 16 小節 ≒ 30.7 秒、休符 2 小節 ≒ 3.8 秒。最後の音の `release` 4 拍 ≒ 1.9 秒(休符の 8 拍 ≒ 3.8 秒の中に収まる)。実際の聴感は未確認
- 聴きどころ: 約 13 秒(7 小節目)から、マイナーが入って響きが変わるところ。約 28〜31 秒(16 小節目)の Asus4 → Am と、最後の a4 の余韻。その後の 2 小節の静けさ
- 課題: 6 小節目の f5 → e5(sus4 の解決)を f5 のまま伸ばして、解決しない緊張がどう聞こえるかを聴く
- 関連: L085, L086

### L090 つなぎ: 減七の橋とティンパニの心拍(イントロ → ビルドアップ)
- タグ: #つなぎ #transition #減七和音 #diminished-seventh #ティンパニ #timpani #裏打ち #offbeat #クレッシェンド #crescendo #アウフタクト #anacrusis
- 日付 / 曲: 2026-10-20 / dark_creep(`work/daw/dark_creep.json`、72〜88 拍 + 68〜76 拍)
- 決めた人: ユーザーが選んだ(5案から案4)+ ユーザーの指示(18〜19小節のティンパニの打ち方を何度も指定)
- 選んだ案: Am | Am | G#dim7 | Am/E の4小節。他の案(♭II の暗転・半音下行・ティンパニの心拍・リズムの予告)との違いは、橋の中に導音 G# を置いて「次へ移る」感じを和声で作ること
- コード: `timpani` hits 18小節 `[69,40] [70,50] [71,60]`、19小節 `[73,80] [74,100] [75,120]`(表打ち、ベロシティを 6 打で上げる。`timpani_layer` は ×0.6)
- 意味(理論): 減七和音(G#dim7 = G# B D F)は、全部の音が短3度で積まれ、4つの半音下行先(Am・Gm 系)へ解決できるので、「どこへでも行ける」不安定さを作る。ティンパニの表打ち3つ → 溜め → 3つは、同じ形を強くして返す呼びかけと応答。裏打ち(拍の間)は浮く、表打ちは足を地面に着ける
- 数値: 125 BPM で 1 拍 0.48 秒。ティンパニの間隔は最大でも 8分(0.5 拍 = 0.24 秒)に抑える(連打に向かない音源のため)。75 拍の 120 は 76 拍(Am)の 1 拍前
- 聴きどころ: 約 33〜37 秒(18〜19小節の 3 打 + 溜め + 3 打 → 20小節の Am)
- 課題: 19小節の頭(72 拍)にも打って、4 つ打ちに埋めたときの勢いの違いを聴く
- 関連: L089

### L091 コントラバスと sus・add9・m9 の曖昧な和声(声部づくり)
- タグ: #コントラバス #contrabass #sus和音 #suspended #add9 #m9 #声部 #voicing #浮遊感 #floating #wav音源 #sampled-instrument
- 日付 / 曲: 2026-10-20 / dark_creep(`contrabass`、イントロ後半の `prog`)
- 決めた人: ユーザーの指示(低音ストリングス、浮遊感・不安定さを増やす)+ AI が決めた(sus の置き場所・音の選択)
- 選んだ案: 後半(9〜16小節)を Dsus2 / Cadd9 / Gsus4 / Dsus4 / Gm9 / Dsus4 / Bbadd9 / Asus4 にして、3度の音を抜く・入れ替える
- コード: `{"name":"work/samples/contrabass","amp":10.3,"env":"pad","attack":0.1,"release":0.8}`(`sample` + `rate` で音程をずらす)
- 意味(理論): sus2 / sus4 は 3度を 2度か 4度に置き換えるので、長調か短調かが決まらず、解決(sus4 → 3度)を待たせる緊張が残る。add9 / m9 は 9度(1オクターブ上の2度)で空気の層を足す。低音のコントラバスが根音を長く鳴らすと、上の曖昧さが「地面が揺れない」安心と対比になる。コントラバスの声部は根音の支え、ヴィオラ・ヴァイオリンのロングが内声
- 数値: コントラバスの wav は A#0〜G#2 のみ。範囲外は `rate` でずらすため、遠いほど音色が変わる(未確認)
- 聴きどころ: 約 15〜31 秒(9〜16小節)の sus の連なり
- 課題: Gsus4 の 4度(c)を 3度(b)に替えて、sus の緊張が消える違いを聴く
- 関連: L089

### L092 ストリングスのロングトーンの置き方(前方を長く、後ろは休符)
- タグ: #ロングトーン #long-tone #休符 #rest #リリース #release #ヴィオラ #viola #sustain #wav-sustain
- 日付 / 曲: 2026-10-20 / dark_creep(`violin_long` `viola_long`)
- 決めた人: ユーザーの指示
- 選んだ案: 1 小節ごとに規則的に配置し、ベタ打ち(4 拍)ではなく 3〜3.5 拍で鳴らして最後に休符を残す
- コード: `["violin_long","e5",3.5,80]`、wav 楽器の `sustain` は秒なので `l * 60.0 / current_bpm` に直した
- 意味(理論): 小節の後ろに休符(0.5〜1 拍)を残すと、次の小節の頭で弦が再び入る「息継ぎ」ができ、ベタ打ちの壁が呼吸する音になる。以前は `sustain` を拍の数のまま秒として扱い、約 2 倍の長さで鳴っていた(試験録音で 2 拍 = 0.96 秒のはずが約 2.1 秒)
- 数値: 125 BPM で 3.5 拍 = 1.68 秒
- 聴きどころ: 約 34〜40 秒(つなぎ以降)で、弦が小節の頭で切れて入り直す感じ
- 課題: 3.5 拍を 4 拍に伸ばして、ベタ打ちとの違いを聴く
- 関連: L091

### L093 パッド(supersaw)とトレモロ、オクターブ下を重ねない深み
- タグ: #パッド #pad #supersaw #ノコギリ波 #saw #ギザギザ #aliasing #トレモロ #tremolo #サイドチェイン #sidechain #attack
- 日付 / 曲: 2026-10-20 / dark_creep(`pad` `pad_trem` `sc`)
- 決めた人: ユーザーが選んだ(オクターブ下を重ねない案 1・4)+ ユーザーの指示(saw、prophet、attack を短く)
- 選んだ案: `pad` を supersaw にして、トレモロ(phase 2、depth 0.3)と、`attack` を 0.05 拍に短縮。サイドチェイン(depth 0.4、release 0.3)をピアノ・パッド・サブベースに掛ける
- コード: `{"name":"supersaw","amp":1,"env":"pad","attack":0.05}` / `sidechain` の `steps` はキックと同じ位置の `X`
- 意味(理論): 低いノコギリ波は倍音が多く、低音に重ねると位相の干渉で「ギザギザ」(ビート)に聞こえる。`cutoff` を下げるか、重ねずに同じ音色で厚みを出す。サイドチェインはキックの打点で他の音量を下げ、`release` 拍かけて戻す。キックが前に出る(ポンピング)
- 数値: サイドチェインの `release` 0.3 拍 = 0.14 秒、`depth` 0.4 = 音量を 60% 下げる
- 聴きどころ: 約 58 秒以降のドロップで、キックに合わせてパッドが息をする感じ
- 課題: `depth` を 0.4 から 0.8 に上げて、ポンピングの深さを聴く
- 関連: L085

### L094 キックの跳ね(0・2.5・3.5)とキック・ティンパニの重ね
- タグ: #キック #kick #シンコペーション #syncopation #レイヤー #layer #イコライザー #eq #lpf #ローパス #ティンパニ #timpani
- 日付 / 曲: 2026-10-20 / dark_creep(`kick` `kick_layer` `kick_lpf` `timpani_layer`)
- 決めた人: ユーザーの指示
- 選んだ案: キックを 1 小節に 0 拍・2.5 拍・3.5 拍(2 つ目を後ろにずらして溜め、3 つ目を着地)にする。軽い `bd_ada` と `drum_tom_lo_soft` を ×0.6 で重ねる
- コード: `kick` hits `[0,120] [2.5,80] [3.5,60]` / `kick_layer` `{"name":"bd_ada","amp":1.0}` / `timpani_layer` `{"name":"drum_tom_lo_soft","amp":0.8}`
- 意味(理論): 2 つ目のキックを 8 分遅らせると、拍の頭で来るはずのものが来ない「溜め」ができ、3 つ目で着地して跳ねる。軽い音を重ねるのは、本体の音を変えずに中域の輪郭と太さ(アタックの粒)を足すため。`kick_lpf`(cutoff 80)でキックの「カチッ」を丸める
- 数値: 重ねる音のベロシティは本体の 0.6 倍(10 刻みに丸める)
- 聴きどころ: 約 58 秒以降のドロップのキックの跳ね
- 課題: `kick_layer` の `amp` を 1.0 から 0.5 に下げて、厚みの変わり方を聴く
- 関連: L083, L084

### L095 ハットの駆け抜け・スネアの連打とシンコペーション
- タグ: #ハイハット #hi-hat #16分音符 #sixteenth #シンコペーション #syncopation #スネアロール #snare-roll #3つ打ち #triple-hit
- 日付 / 曲: 2026-10-20 / dark_creep(`hat` `snare` `ghost`、ドロップ手前と最後の小節)
- 決めた人: ユーザーの指示
- 選んだ案: ハットの連打に休符を入れて、16分音符 + 短い休符を何度か。アクセントをキックの 0.25 拍手前(シンコペーション)に置く。最後の小節は 3 つ打ち(3.0 / 3.5 / 3.75)
- コード: `hat` hits の 1・2・3 / 7・8・9 / 11・12・13 / 15 の 16分(アクセント 80)
- 意味(理論): キックの直前に弱いハットのアクセントを置くと、キックが前のめりに聞こえる(アンティシペーション)。連打に休符を入れると、息継ぎのような「駆け抜け」になる
- 数値: 16分 = 0.25 拍 = 0.12 秒
- 聴きどころ: 約 74 秒・約 130 秒・約 172 秒(各ドロップ周の最後)
- 課題: アクセントの位置を 0.25 拍から 0.125 拍手前に変えて、前のめりの度合いを聴く
- 関連: L084

### L096 フルートの風(対旋律・スタッカートへの応答・下降)
- タグ: #対旋律 #counter-melody #フルート #flute #コールアンドレスポンス #call-and-response #スタッカート #staccato #グライド #glide #ベンド #bend
- 日付 / 曲: 2026-10-20 / dark_creep(`flute_wind`)
- 決めた人: ユーザーの指示(息継ぎは休符、そうでない所はレガート、半音・全音で下がって風が吹き抜ける)
- 選んだ案: ビルドアップで、弦のスタッカートの後に答える短くて強い下降(ベンド −1 / −2、ベロシティ 30 → 80)。ドロップのフルートは音が多すぎて削除
- コード: `flute_wind` `{"attack":0.15,"release":0.6,"glide":0.3}`、`reverb_wind`(mix 0.6、room 0.9)
- 意味(理論): 弦が先に鳴り、その隙間にフルートが答える形(コール&レスポンス)にすると、音が重ならずに対話になる。半音・全音の下降は、風が通り過ぎる音の移動の感じ
- 数値: 下降ごとに 1〜1.5 拍、ベロシティ 30 → 40 → 50 / 40 → 60 → 80
- 聴きどころ: 約 42〜57 秒(ビルドアップ)
- 課題: ベンドを 0 にして、風の動きが消えた音との違いを聴く
- 関連: L089

### L097 後半の構成: ドロップ2周目・ブレイク・ドロップ前半・最後のドロップ
- タグ: #構成 #structure #ブレイク #break #ドロップ #drop #dim7 #diminished-seventh #導音 #leading-tone #ドミナント #dominant #ベロシティ #velocity #コードの置換 #chord-mapping
- 日付 / 曲: 2026-10-20 / dark_creep(120〜299 拍)
- 決めた人: ユーザーの指示
- 選んだ案: ドロップ2周目は普通の三和音(sus・dim・7th なし)、ブレイクはフルート 3 声と低音の伴奏だけで Am | Dm | Gm | Am を 2 周、ドロップ前半(Am7 | Bbsus2 | G#dim7 | Asus4)、最後のドロップは 1 回目の 2 周ループでベロシティ +10。1 周目の最後は Esus4 → E7(2 拍ずつ)で解決
- コード: コピー先で和音の音を「旧和音内の位置 → 新和音の同じ位置」に置き換える(`conv`)
- 意味(理論): 同じ素材を 3 回出すのは、変化が和声(sus → 普通 → dim7)と編成(全部 → 低音だけ → 全部)に集中するため。Esus4 は 3度(G#)を待たせる浮遊感で、G#(導音)を 2 拍後に入れると Am への引力が出る
- 数値: 75 小節 + アウトロ 16 = 91 小節。ベロシティは 10 刻み(上限 120)
- 聴きどころ: 約 94〜120 秒(ブレイク 2 周)、約 126 秒以降(最後のドロップ)
- 課題: 38小節の E7 の G# を A に戻して、sus の浮遊感の違いを聴く
- 関連: L085, L086, L089

### L098 riser: ノイズのスウィープと弦のトレモロ、無音の拍
- タグ: #riser #ライザー #ノイズ #noise #ハイパス #hpf #オートメーション #automation #トレモロ奏法 #tremolo-strings #休符 #rest #リバーブ #reverb
- 日付 / 曲: 2026-10-20 / dark_creep(59小節、232〜236 拍)
- 決めた人: ユーザーが選んだ(案 1 と 3)+ ユーザーの指示(59小節に挿入、noise にリバーブなし、休符を 2 拍に)
- 選んだ案: `noise` が 2 拍かけて膨らみ(`attack` 2)、`hpf` の `cutoff` を 40 → 120 に上げる。A4 の弦を 16分で 8 回(ベロシティ 30 → 120)。最後の 2 拍は無音
- コード: `riser_hpf` の `automation` `{"param":"cutoff","points":[[232,40],[234,120]]}`
- 意味(理論): ハイパスのカットオフが上がると低域から削れて、音が高く細くなる。上昇の聞こえ方で期待を作り、無音で期待を一度切ると、次のキックが前に出る。リバーブの余韻(`room` 0.9)は無音に流れ込むので、ノイズは対象から外した
- 数値: 2 拍の無音 = 0.96 秒
- 聴きどころ: 約 111〜113 秒
- 課題: `riser_noise` の `attack` を 2 から 1 に変えて膨らみ方を聴く
- 関連: L090

### L099 アウトロ: コーラス風の進行から減らす(Dsus2・lpf 沈め)
- タグ: #アウトロ #outro #サブドミナント #subdominant #sus2 #ローパス #lpf #オートメーション #automation #引き算 #subtractive-arrangement #A-フリジアン #phrygian
- 日付 / 曲: 2026-10-20 / dark_creep(300〜364 拍、76〜91小節)
- 決めた人: ユーザーの指示(コーラスっぽく、段々と減らす、16小節)+ AI が決めた(進行・メロディ)
- 選んだ案: Am | F | C | Gm を 3 周、最後は Am | F | Gm | Am。各 4 小節の最後を Dsus2(IV の sus2)にし、`outro_lpf` で cutoff 120 → 72 に沈める。4 小節ごとにドラム → ピアノ → 弦を抜く
- コード: `outro_lpf` `{"name":"lpf","automation":{"param":"cutoff","points":[[300,120],[364,72]]}}`
- 意味(理論): 私が最初に G メジャー(B ナチュラル)を使い、フリジアンの外で明るく聞こえた(Gm に直した)。Dsus2 は 3度を抜いた IV で、解決先(Am)を待たせる浮遊感。lpf を下げると倍音が減って音が遠く暗くなる。キック・スネアは抜き、ティンパニとハットは残す
- 数値: cutoff 72 ≒ 約 370 Hz。最後のフルート a4(440 Hz)はこもる
- 聴きどころ: 約 144〜175 秒
- 課題: 最後の Dsus2 を Dm に替えて、IV → i の解決感の違いを聴く
- 関連: L097

### L100 glitch の自作サンプルと、スライサー + スタッター
- タグ: #グリッチ #glitch #ビットクラッシャー #bitcrusher #スライサー #slicer #スタッター #stutter #タイムストレッチ #time-stretch #atempo #自作サンプル #synthesized-sample
- 日付 / 曲: 2026-10-20〜21 / dark_creep(`glitch_zip` `glitch_gate` `glitch_slicer` と `lead`)
- 決めた人: ユーザーが選んだ(5 音から 4・5、案 1 + 3)+ ユーザーの指示(長さ、下降、強さの調整)
- 選んだ案: 自作の zip(下降、保持幅を細かい → 粗い)と gate(Am の和音を 1/40 秒で刻む)を 2.5 倍に伸ばして、ドロップの 2・6小節目の最後に置く。スライサー(phase 0.125、pulse_width 0.5)を半拍だけ有効に、`lead` を 4 連打
- コード: `ffmpeg -af atempo=0.5,atempo=0.7318`(音程を保って伸ばす)
- 意味(理論): glitch は音が規則的に壊れる質感。sample-and-hold ノイズの保持幅が長いほど低く粗く聞こえる。スライサーは音を 1/32 拍ごとに切り、スタッターは同じ音を 0.125 拍刻みで繰り返して、旋律の音程を壊さずにどもらせる
- 数値: gate 0.40 秒 → 0.99 秒、zip 0.30 秒 → 0.75 秒(ffmpeg の atempo が短めに出るので補正)
- 聴きどころ: 約 62 秒、約 69 秒
- 課題: `pulse_width` を 0.5 から 0.3 に下げて、刻みの強さを聴く
- 関連: L095

### L101 ピアノを wav(Knight)に替える、イントロのピアノ(3和音 + トップノートをなぞる + 9th)
- タグ: #ピアノ #piano #wav音源 #sampled-instrument #アップライト #upright #9th #ninth #トップノート #top-note #追従 #follow #声部 #voicing
- 日付 / 曲: 2026-10-21 / dark_creep(`pianolow` `pianolow_weak` `lead` `intro_piano` `intro_piano_top`)
- 決めた人: ユーザーの指示(Knight、3和音、フルートに追従、トップで 9th)
- 選んだ案: VCSL Upright Piano, Knight の弱い層(`vl1`)をコピー。イントロは和音をフルートの変化に追従して弾き直し(29 回)、フルートの頂点には 9th を下に足す(♭9th は A フリジアンの外のとき)
- コード: `{"name":"work/samples/piano_knight","amp":1.2,"release":1.5}`(`:piano` の 0.2 倍補正がない分、amp を約 2 倍に)
- 意味(理論): 古いアップライトは箱鳴りで温かく、倍音が柔らかい。トップノートに 9th を足すと、メロディの下に透明な層ができる。9th が頂点と 2度だとにごるので、1 オクターブ下げて 9度以上に離す
- 数値: wav のピークは約 −16〜−20 dBFS。弱い層なので小さい音で温かい
- 聴きどころ: 約 0〜31 秒
- 課題: トップに足した 9th を 1 つ消して、3 和音との違いを聴く
- 関連: L089

### L102 イントロの「暗闇に向かう」オートメーション(lpf と reverb の mix)
- タグ: #オートメーション #automation #ローパス #lpf #リバーブ #reverb #mix #room #音色変化 #timbre-automation
- 日付 / 曲: 2026-10-21 / dark_creep(`intro_lpf` `intro_reverb`、0〜76 拍)
- 決めた人: ユーザーが選んだ(案 1 + 2)+ ユーザーの指示(19小節の終わりまで)
- 選んだ案: `cutoff` を 120 → 105(32 拍)→ 75(76 拍)。`mix` を 0.1 → 0.3 → 0.7(`room` 0.95 固定)。終わったら戻す
- コード: `{"param":"mix","points":[[0,0.1],[32,0.3],[76,0.7],[78,0]]}`
- 意味(理論): 高域を削ると遠く暗く、残響が深いと奥の部屋に引き込まれる。和声が暗くなる 8小節目(32 拍)に合わせて、後半の動きを急にした。1つの FX では 1 つの値しか動かせないので、`room` は固定
- 数値: `mix` は原音と残響の割合、`room` は部屋の大きさ(残響の長さ)
- 聴きどころ: 約 15〜37 秒
- 課題: `cutoff` の終わりを 75 から 90 にして、暗さの深さを聴く
- 関連: L089, L099
