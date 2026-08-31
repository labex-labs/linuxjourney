---
lesson_id: "join-split-command"
course_id: "text-fu"
lang: "ja"
order_index: 11
title: "結合と分割"
description: "並べ替え済みの 2 つのテキストファイルをキーで結合し、1 つのファイルを名前付きの断片へ分割する方法を学びます。"
meta_title: "結合と分割 - Text-Fu"
meta_description: "Linux の join コマンドと split コマンドの使い方を習得しましょう。共通のフィールドに基づいてファイルを効率的に結合する方法や、大きなファイルを小さな部分に分割する方法を学びます。このガイドでは、cat、dog、cow という名前のファイルを結合する際に使用するコマンドや、その他の実用的な例を解説します。"
meta_keywords: "linux ファイル結合，ファイルを結合するコマンド，linux join コマンド，linux split コマンド，ファイル操作，コマンドライン，テキスト処理"
---

`join` と `split` は異なるファイル処理を行います。`join` は並べ替え済みの 2 つのテキスト入力から関連レコードを結合し、`split` は 1 つの入力を連続した小ファイルへ分割します。

## 先頭フィールドで 2 ファイルを結合する

`join` は標準で、ちょうど 2 つの入力ファイルにある先頭の空白区切りフィールドを比較します。次のファイルは並べ替え済みです。

`people.txt`：

```text
1 John
2 Jane
3 Mary
```

`surnames.txt`：

```text
1 Doe
2 Doe
3 Sue
```

キーが等しいレコードを結合します。

```bash
$ join people.txt surnames.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

出力には共有キーが 1 回、その後に第 1、第 2 ファイルの残りのフィールドが入ります。`join` が一度に処理するのは 2 ファイルで、3 つの通常ファイルを 3 方向の関係結合としては受け取りません。

:::single-choice{#join-default-key}
フィールドオプションなしの `join first.txt second.txt` はどのレコードを結合しますか？

::option[先頭の空白区切りフィールドが等しい行。]{#join-first-fields .correct explanation="`join` の標準動作は、並べ替え済みの 2 入力からフィールド 1 を比較します。"}
::option[物理的な行番号が同じ行。]{#join-line-numbers explanation="一致は単なるレコード位置ではなく、キーフィールドの値に基づきます。"}
::option[第 1 ファイルの全行と第 2 ファイルの全行の組み合わせ。]{#join-all-pairs explanation="`join` は全行の無制限な直積ではなく、一致するキーのレコードを出力します。"}
:::

## 結合キーを並べ替える

各入力は、互換性のある比較規則で結合フィールド順に並べる必要があります。標準のフィールド 1 なら、`sort -k 1,1` でコピーを用意します。

```bash
$ LC_ALL=C sort -k 1,1 people-raw.txt > people.txt
$ LC_ALL=C sort -k 1,1 surnames-raw.txt > surnames.txt
$ LC_ALL=C join people.txt surnames.txt
```

並べ替えと結合で同じロケールを使えば照合規則が一致します。シェルが先にファイルを切り詰めるため、並べ替え結果を同じ入力パスへリダイレクトしないでください。

:::single-choice{#join-sort-requirement}
`join` が確実に一致を処理するため、通常どの準備が必要ですか？

::option[両ファイルの物理的な行数を完全に同じにする。]{#join-equal-line-count explanation="入力の長さは異なっても構いません。結合出力は行数ではなくキーの一致で決まります。"}
::option[2 つのファイル名をアルファベット順で隣り合わせにする。]{#join-filename-order explanation="並べ替える必要があるのは内容のキーで、ファイル名同士の辞書順は無関係です。"}
::option[両ファイルをそれぞれの結合フィールドで互換性のある順序に並べる。]{#join-sorted-keys .correct explanation="`join` は順序付きキーを進むため、各入力の順序は比較規則と一致している必要があります。"}
:::

## 異なる結合フィールドを選ぶ

第 1 ファイルのキーには `-1 FIELD`、第 2 ファイルには `-2 FIELD` を使います。第 1 入力に次が含まれるとします。

```text
John 1
Jane 2
Mary 3
```

第 2 入力には次が含まれます。

```text
1 Doe
2 Doe
3 Sue
```

第 1 入力をフィールド 2、第 2 入力をフィールド 1 で並べた後、次を実行できます。

```bash
$ join -1 2 -2 1 people.txt surnames.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

コロンなど 1 文字の非空白区切りには `-t CHARACTER` を使います。`-a 1` や `-a 2` は片方にしかない行を含められますが、標準では一致したキーだけを出力します。

:::single-choice{#join-different-fields}
第 1 ファイルのフィールド 2 と第 2 ファイルのフィールド 1 を結合するオプションはどれですか？

::option[`-1 1 -2 2`]{#join-fields-reversed explanation="第 1 入力のフィールド 1 と第 2 入力のフィールド 2 を選ぶため、要求と逆です。"}
::option[`-1 2 -2 1`]{#join-fields-two-one .correct explanation="`-1 2` は第 1 ファイルのフィールド 2、`-2 1` は第 2 ファイルのフィールド 1 を選びます。"}
::option[`-f 2 -d 1`]{#join-cut-style-options explanation="他のテキストツールのフィールド、区切りオプションに似ていますが、`join` のフィールド選択ではありません。"}
:::

## 行数で分割する

`split` は 1 つの入力の連続部分を別々の出力ファイルへ書きます。キー結合を行う `join` の逆操作ではありません。

```bash
$ split large.txt
```

GNU の標準動作では 1 ファイルにつき最大 1000 行、接頭辞 `x` を使い、`xaa`、`xab`、`xac` などを作ります。行数は `-l NUMBER`、出力接頭辞は最後のオペランドで指定します。

```bash
$ split -l 500 large.txt part-
```

:::single-choice{#split-lines-with-prefix}
`large.txt` を最大 500 行ずつ、接頭辞 `part-` の断片へ分割するコマンドはどれですか？

::option[`split -b 500 large.txt part-`]{#split-five-hundred-bytes explanation="`-b` はバイトを選ぶため、通常のテキストでは 500 行よりはるかに小さな断片になります。"}
::option[`split -l 500 large.txt part-`]{#split-five-hundred-lines .correct explanation="`-l 500` が最大行数を設定し、最後のオペランドが出力ファイル名の接頭辞です。"}
::option[`join -l 500 large.txt part-`]{#join-split-lines explanation="`join` は 2 ファイルのキー付きレコードを結合し、1 入力を分割しません。"}
:::

## サイズで分割する

`-b SIZE` は入力をバイトサイズで分割します。GNU の `K`、`M`、`G` などはここでは 1024 の累乗です。

```bash
$ split -b 10M archive.bin chunk-
```

最後の断片だけ小さくなる可能性があります。`split` はアーカイブの目録や再構築用メタデータを作らないため、接尾辞の順序を保ち、必要なら順番に連結してください。

:::single-choice{#split-ten-mebibytes}
`archive.bin` を接頭辞 `chunk-`、10 MiB ずつに分割するコマンドはどれですか？

::option[`split -l 10M archive.bin chunk-`]{#split-lines-ten-m explanation="`-l` は行数を取り、バイナリ断片のバイトサイズ接尾辞は指定しません。"}
::option[`join -b 10M archive.bin chunk-`]{#join-bytes explanation="`join` はバイナリ入力を分割せず、この断片サイズ操作も受け付けません。"}
::option[`split -b 10M archive.bin chunk-`]{#split-ten-mib .correct explanation="`-b` が断片サイズを選び、`10M` は 10×1024×1024 バイト、`chunk-` は接頭辞です。"}
:::

キー結合と構造化データ処理を練習するには、次のラボを試してください。

1. **[Linux join コマンド：ファイル結合](https://labex.io/ja/labs/linux-linux-join-command-file-joining-219193)** - 共通フィールドに基づき、並べ替え済み 2 ファイルの行を結合します。
2. **[従業員データの処理](https://labex.io/ja/labs/linux-processing-employees-data-388132)** - `join` や `awk` で複数ソースのデータを結合、処理します。

## まとめ

並べ替え済みレコードを結合し、1 つの入力を順序付きの断片へ分割できるようになりました。

1. 等しいキーフィールドでちょうど 2 ファイルを結合する。
2. 両入力を結合キーで一貫して並べ替える。
3. `-1` と `-2` で標準以外のキーフィールドを選ぶ。
4. `-l` で行数ごとに分割する。
5. `-b` と明確な接頭辞でバイトサイズごとに分割する。
