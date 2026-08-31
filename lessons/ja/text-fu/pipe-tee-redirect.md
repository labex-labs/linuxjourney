---
lesson_id: "pipe-tee-redirect"
course_id: "text-fu"
lang: "ja"
order_index: 4
title: "パイプと tee"
description: "パイプラインがコマンド同士を接続する仕組みと、tee でストリームを先へ渡しながら保存する方法を学びます。"
meta_title: "パイプと tee - Text-Fu"
meta_description: "Linux における強力なパイプと tee コマンドを探求しましょう。Linux のパイプと tee の組み合わせでコマンドを連鎖させ、出力を画面とファイルの両方にリダイレクトする方法を学びます。このガイドでは、高度なコマンドラインデータフローのために tee にパイプする方法を解説します。"
meta_keywords: "Linux のパイプと tee コマンド，Linux パイプ tee, tee へのパイプ，Linux パイプ，tee コマンド，stdout, stdin, コマンドラインリダイレクト，Linux チュートリアル"
---

パイプラインは小さなコマンド同士を接続し、中間ファイルを使わずにデータを流します。`tee` コマンドを使うと、その流れを先へ送りながら一部をファイルへコピーできます。

## | でコマンドを接続する

ディレクトリ一覧が長すぎて一度に読めない場合を考えます。

```bash
$ ls -la /etc
```

パイプ演算子 `|` をコマンド間に置くと、左側の stdout が右側の stdin へ接続されます。

```bash
$ ls -la /etc | less
```

シェルはパイプラインのコマンドを起動し、ストリームを接続します。コマンドは並行して動作でき、`ls` が一覧全体を生成する前に `less` は読み始められます。

:::single-choice{#pipe-stream-connection}
`ls -la /etc | less` で、`|` が標準で接続するストリームはどれですか？

::option[`ls` の stdin と `less` の stdout。]{#pipe-reversed-streams explanation="生成側と受信側の両方が逆です。データは左のコマンドの出力から右のコマンドの入力へ流れます。"}
::option[`ls` の stderr と `less` の両方のストリーム。]{#pipe-stderr-both explanation="通常のパイプは左側の stderr を接続せず、右側の両方のストリームを対象にもしません。"}
::option[`ls` の stdout と `less` の stdin。]{#pipe-stdout-stdin .correct explanation="標準のパイプラインは左側のファイルディスクリプタ 1 を右側のファイルディスクリプタ 0 へ接続します。"}
:::

## stderr を分けておく

通常の `|` が運ぶのは stdout だけです。左側の stderr は以前の出力先（多くは端末）を保ちます。

```bash
$ find /etc -name "*.conf" | less
```

一致したパス名はパイプを通り、権限に関する診断は端末へ直接表示されることがあります。別の動作が必要なら stderr を個別にリダイレクトします。

```bash
$ find /etc -name "*.conf" 2> find-errors.log | less
```

:::single-choice{#pipe-left-stderr}
`find /etc -name "*.conf" | less` で他のリダイレクトがない場合、`find` の stderr は通常どこへ送られますか？

::option[stdout と同じパイプを通って `less` へ送られる。]{#pipe-errors-to-less explanation="通常のパイプが接続するのは stdout だけで、stderr は自動的にまとめられません。"}
::option[現在のディレクトリの `stderr` というファイルへ送られる。]{#pipe-errors-to-file explanation="エラーファイルへのリダイレクトがないため、シェルはそのようなファイルを作りません。"}
::option[既存の出力先（通常は端末）へ送られる。]{#pipe-errors-terminal .correct explanation="ディスクリプタ 2 は変更されないため、診断は通常、端末に接続されたままです。"}
:::

## tee でストリームをコピーする

`tee` は stdin を読み取り、指定した各ファイルへコピーすると同時に、同じデータを stdout へも書き出します。

```bash
$ ls | tee listing.txt
```

`listing.txt` に一覧が保存され、`tee` の stdout は端末に接続されたままです。`tee` は標準では `>` と同様に指定ファイルを作成または切り詰めます。

:::single-choice{#tee-display-and-save}
`generate-report` の出力を表示し、同じ出力で `report.txt` を置き換えるコマンドはどれですか？

::option[`generate-report > report.txt`]{#redirect-report-only explanation="通常の出力リダイレクトはファイルへ書きますが、端末へ流れるコピーを残しません。"}
::option[`generate-report | tee report.txt`]{#tee-report .correct explanation="`tee` は stdin を `report.txt` と stdout の両方へコピーし、このパイプラインでは stdout が端末につながっています。"}
::option[`tee generate-report | report.txt`]{#tee-operands-reversed explanation="これは `generate-report` を出力先ファイルとして扱い、`report.txt` をコマンドとして実行しようとします。生成側は左に置きます。"}
:::

ファイルを置き換えず追記する場合は `-a` を使います。

```bash
$ date | tee -a activity.log
```

:::single-choice{#tee-append-log}
現在の日付を表示し、`activity.log` へ追記するコマンドはどれですか？

::option[`date | tee -a activity.log`]{#tee-append-activity .correct explanation="`-a` オプションにより、`tee` は入力を stdout へコピーし続けながらファイルへ追記します。"}
::option[`date | tee activity.log`]{#tee-replace-activity explanation="`-a` がなければ、`tee` は既存の内容を残さずファイルを置き換えます。"}
::option[`date > activity.log`]{#redirect-replace-activity explanation="これはファイルを置き換え、端末へコピーを送りません。追記と表示のどちらの要件も満たしません。"}
:::

## 中間結果を保存する

`tee` をパイプラインの途中に置くと、中間ストリームを保存しながら処理を続けられます。

```bash
$ ls -la /etc | tee etc-listing.txt | grep "conf"
```

このパイプラインは次の処理を行います。

1. 詳細な一覧全体を生成する。
2. その完全なストリームを `etc-listing.txt` に保存する。
3. 同じストリームを `grep` へ送り、`conf` を含む行だけを表示する。

ファイルには `grep` で絞り込む前のデータが入ります。絞り込まれた行だけを保存したい場合は、`tee` を `grep` の後ろに置きます。

:::single-choice{#tee-before-filter-result}
`produce | tee all.txt | grep error` が正常に終了した後、`all.txt` には何が入っていますか？

::option[`grep` が一致させた行だけ。]{#tee-filtered-only explanation="`tee` は `grep` より前に動くため、後段の一致結果ではなく絞り込み前の入力を書き込みます。"}
::option[`produce` の stderr だけ。]{#tee-producer-stderr explanation="通常のパイプが運ぶのは `produce` の stdout であり、stderr は `tee` の入力ではありません。"}
::option[絞り込み前に生成された stdout のすべて。]{#tee-complete-intermediate .correct explanation="`tee` は受け取ったすべてのバイトを保存し、同じストリームを `grep` へ渡して絞り込みます。"}
:::

パイプラインとストリームのコピーを練習するには、次のハンズオンラボを試してください。

1. **[Linux における入出力のリダイレクト](https://labex.io/ja/labs/comptia-redirecting-input-and-output-in-linux-590840)** - 標準出力、標準エラー、標準入力を操作してデータフローを制御します。
2. **[シーケンス制御とパイプライン](https://labex.io/ja/labs/linux-sequence-control-and-pipeline-17994)** - コマンドの実行順序やパイプライン、`cut`、`grep`、`wc`、`sort`、`uniq` などのツールを学びます。
3. **[データストリームのリダイレクト](https://labex.io/ja/labs/linux-data-stream-redirection-17995)** - 標準入力、出力、エラーの操作や出力の結合、`/dev/null` の利用を学びます。

## まとめ

コマンドを接続し、データストリームの必要な地点を保存できるようになりました。

1. あるコマンドの stdout を別のコマンドの stdin へパイプする。
2. 必要に応じて stderr を個別にリダイレクトする。
3. `tee` で入力をファイルと stdout の両方へコピーする。
4. ファイルを置き換えず `tee -a` で追記する。
5. フィルターの前後どちらに `tee` を置くか意図的に選ぶ。
