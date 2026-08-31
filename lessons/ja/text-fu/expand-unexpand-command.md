---
lesson_id: "expand-unexpand-command"
course_id: "text-fu"
lang: "ja"
order_index: 10
title: "展開と折りたたみ"
description: "タブストップを基準に、expand と unexpand でタブと空白を相互変換する方法を学びます。"
meta_title: "展開と折りたたみ - Text-Fu"
meta_description: "expand コマンドと unexpand コマンドで Linux のテキスト書式設定をマスターしましょう。タブをスペースに、スペースをタブに戻す方法を学び、一貫したファイルレイアウトを実現します。"
meta_keywords: "expand コマンド，unexpand コマンド，Linux タブ，Linux スペース，テキスト書式設定，Linux チュートリアル，初心者 Linux, Linux ガイド"
---

タブは一定数の可視空白ではなく、次のタブストップまでの移動を保存します。表示幅は現在の列とタブストップ設定によって変わります。`expand` と `unexpand` はその位置を考慮してタブ文字と空白を相互変換します。

## タブを空白へ変換する

`expand` は入力を読み、各タブを適切なタブストップまでに必要な空白へ置き換え、結果を stdout へ書きます。

```bash
$ expand sample.txt
```

標準ではタブストップは 8 列ごとです。1 列目のタブと 6 列目のタブでは展開が異なり、常に 8 個の空白へ置換されるわけではありません。

:::single-choice{#expand-default-tab-stops}
標準設定の `expand` はタブ文字をどのように置き換えますか？

::option[次の標準タブストップまでに必要な数の空白を挿入する。]{#expand-next-stop .correct explanation="`expand` は現在の列から必要な空白数を計算し、タブストップでの配置を保ちます。"}
::option[常にちょうど 8 個の空白を挿入する。]{#expand-eight-spaces explanation="標準のストップは 8 列間隔ですが、空白数は現在の列に依存します。"}
::option[文字を追加せずタブを削除する。]{#expand-remove-tab explanation="後続テキストが選択したタブストップに揃うよう、タブを空白へ置き換えます。"}
:::

## タブストップを選ぶ

`-t NUMBER` で、指定列数ごとにタブストップを置きます。

```bash
$ expand -t 4 sample.txt
```

GNU `expand` は明示的なタブ位置をカンマ区切りで指定することもできます。各行で最初の非空白文字より前のタブだけを変換するには `-i` を使います。

:::single-choice{#expand-four-column-stops}
4 列ごとのタブストップでタブを変換するコマンドはどれですか？

::option[`expand -i 4 sample.txt`]{#expand-initial-four explanation="`-i` は先頭のタブだけに変換を制限し、`4` を間隔として取りません。"}
::option[`unexpand -t 4 sample.txt`]{#unexpand-tabs-four explanation="`unexpand` は適切な空白をタブへ変える逆方向の処理です。"}
::option[`expand -t 4 sample.txt`]{#expand-tabs-four .correct explanation="`-t` がタブストップ間隔を設定し、`4` は 4 列ごとのストップを指定します。"}
:::

## 変換結果を安全に保存する

`expand` は入力ファイルを直接編集しません。保存するときは stdout を別のパスへリダイレクトします。

```bash
$ expand sample.txt > result.txt
```

`expand sample.txt > sample.txt` は使わないでください。シェルが `expand` の読み取り前に出力先を切り詰めるため、元データが失われます。別に書いた結果を検証してから、適切なファイル操作で元を置き換えます。

:::single-choice{#expand-safe-output-file}
`sample.txt` を読み取る前に切り詰めず、展開したテキストを保存するコマンドはどれですか？

::option[`expand sample.txt > sample.txt`]{#expand-same-file explanation="シェルは `expand` の起動前に `sample.txt` を出力用に開いて切り詰め、入力を消す恐れがあります。"}
::option[`expand sample.txt > result.txt`]{#expand-separate-result .correct explanation="入出力パスが異なるため、元を壊さず `result.txt` を作成できます。"}
::option[`> sample.txt expand result.txt`]{#expand-leading-redirection explanation="これも `sample.txt` を切り詰め、元ファイルからの安全な変換を表しません。"}
:::

## 空白をタブへ変換する

`unexpand` は、選択したタブストップでの配置を保ちながら、変換可能な空白をタブへ置き換えます。GNU `unexpand` は標準では各行の最初の非空白文字より前だけを変換します。

```bash
$ unexpand result.txt
```

```bash
$ unexpand -a result.txt
```

`-a` は行全体の適切な空白を対象にします。8 個の空白を機械的に置き換えるのではなく、`expand` と同様に列位置とタブストップに依存します。異なる規則なら `-t 4` などを指定します。

:::single-choice{#unexpand-default-scope}
`-a` がない場合、GNU `unexpand` は通常どの空白を変換対象にしますか？

::option[ファイル内のあらゆる場所にあるすべての空白列。]{#unexpand-every-group explanation="行全体の空白には `-a` が必要で、変換はタブストップ位置にも依存します。"}
::option[最後の単語より後ろにある空白だけ。]{#unexpand-trailing-blanks explanation="標準の対象は末尾の空白ではなく、行頭の空白です。"}
::option[最初の非空白文字より前にある行頭の空白だけ。]{#unexpand-initial-blanks .correct explanation="GNU `unexpand` の標準動作は各行の先頭の空白に限られます。"}
:::

:::single-choice{#unexpand-all-blanks}
最初の非空白文字より後ろの空白も対象にする GNU `unexpand` のオプションはどれですか？

::option[`-i`]{#unexpand-initial-option explanation="`expand` の `-i` は先頭タブだけに制限するもので、`unexpand` の全空白オプションではありません。"}
::option[`-a`]{#unexpand-all-option .correct explanation="`-a` は各入力行全体の適切な空白を変換対象にします。"}
::option[`-t`]{#unexpand-tab-list-option explanation="`-t` はタブストップを設定します。GNU では広い変換を伴う場合もありますが、全空白を明示するのは `-a` です。"}
:::

どちらのコマンドもファイル名がなければ stdin を読むため、パイプラインで使えます。表示上の配置が同じでも、空白へ変換して戻した結果が元のタブと空白の選択を完全には再現しないことがあります。

## まとめ

タブストップでの配置を保ちながら、タブと空白を変換できるようになりました。

1. タブを次の設定済みストップまで展開する。
2. `-t` で独自のタブストップを設定する。
3. 入力を置き換える前に別ファイルへ保存する。
4. `unexpand` の標準動作で行頭の空白を変換する。
5. 行全体の空白を対象にする場合は `-a` を使う。
