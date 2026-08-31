---
lesson_id: "stderr-standard-error-redirect"
course_id: "text-fu"
lang: "ja"
order_index: 3
title: "stderr（標準エラー出力）"
description: "Bash で標準エラーを個別にリダイレクトする方法と、標準出力へまとめる方法を学びます。"
meta_title: "stderr（標準エラー出力） - Text-Fu"
meta_description: "Linux で標準エラー出力を管理する方法を学びます。このガイドでは、stderr のリダイレクト、stderr ファイルディスクリプタ（2）、および 2>、2>&1、&>を使用して stderr をファイルまたは/dev/null にリダイレクトする方法について説明します。"
meta_keywords: "stderr, 標準エラー出力 Linux, stderr ファイルディスクリプタ，stderr ファイル，Linux 標準エラー, stderr リダイレクト，2>, 2>&1, &>, /dev/null, bash エラー処理"
---

プログラムは通常、通常の結果を標準出力へ、診断メッセージを **stderr**（標準エラー）という別のストリームへ書き出します。ストリームを分けることで、エラーメッセージを混ぜずに有用なデータを保存できます。

## 通常の出力とエラーを分ける

存在しないパスを指定したコマンドを考えます。

```bash
$ ls /fake/directory > peanuts.txt
ls: cannot access '/fake/directory': No such file or directory
```

`>` 演算子がリダイレクトするのは stdout だけです。診断は stderr へ書かれ、stderr は端末に接続されたままです。一方、`ls` が通常の結果を生成しなくても、シェルは stdout 用に `peanuts.txt` を作成または切り詰めます。

標準ストリームには慣例として次のファイルディスクリプタが使われます。

- `0`：stdin（標準入力）
- `1`：stdout（標準出力）
- `2`：stderr（標準エラー）

:::single-choice{#stderr-not-in-stdout-file}
`ls /missing > results.txt` のエラーが通常、端末に残るのはなぜですか？

::option[`>` は stdout をリダイレクトし、診断は stderr へ書かれるから。]{#stderr-separate-stream .correct explanation="通常の `>` が変更するのはファイルディスクリプタ 1 だけです。ファイルディスクリプタ 2 は端末という既存の出力先を保ちます。"}
::option[`ls` はファイルが閉じるまでエラーを表示しないから。]{#stderr-waits-for-close explanation="問題はタイミングではありません。通常のメッセージと診断メッセージは異なる出力ストリームを使います。"}
::option[`results.txt` は通常のテキストを保存できるが、診断は保存できないから。]{#stderr-file-capability explanation="通常のファイルにはどちらのストリームも保存できます。このコマンドラインでは stderr をそこへリダイレクトしていないだけです。"}
:::

## 2> で stderr をリダイレクトする

`>` の前にファイルディスクリプタ `2` を置くと stderr をリダイレクトできます。

```bash
$ ls /fake/directory 2> errors.txt
```

シェルは `errors.txt` を作成または切り詰め、ディスクリプタ 2 へ接続します。stdout の出力先は変わりません。エラー出力を追記する場合は `2>> errors.txt` を使います。

:::single-choice{#stderr-to-error-file}
`find /restricted` の診断で `errors.log` を置き換え、stdout の出力先は変えないコマンドはどれですか？

::option[`find /restricted > errors.log`]{#stdout-errors-log explanation="通常の `>` はディスクリプタ 1 をリダイレクトするため、診断ではなく通常の結果を取り込みます。"}
::option[`find /restricted < errors.log`]{#stdin-errors-log explanation="小なり記号はファイルを stdin として渡します。どちらの出力ストリームも取り込みません。"}
::option[`find /restricted 2> errors.log`]{#stderr-errors-log .correct explanation="先頭の `2` が stderr を選び、`>` がそのストリームの出力先を作成または切り詰めます。"}
:::

## stdout と stderr をまとめる

両方を 1 つのファイルへ入れるには、まず stdout をリダイレクトし、次に stderr を stdout の現在の出力先へ複製します。

```bash
$ ls /fake/directory /etc/passwd > combined.txt 2>&1
```

リダイレクトは左から右へ処理されます。

1. `> combined.txt` が stdout をファイルへ接続します。
2. `2>&1` が stderr を、その時点で stdout が指している出力先へ接続します。

順序を逆にすると結果が変わります。

```bash
$ ls /fake/directory /etc/passwd 2>&1 > regular.txt
```

ここでは stderr が最初に stdout の元の端末出力先を複製します。その後 stdout だけが `regular.txt` へ移るため、2 つのストリームは別の場所へ送られます。

:::single-choice{#stderr-combine-order}
`command` の stdout と stderr を両方とも `all.log` へ送る Bash のリダイレクトはどれですか？

::option[`command 2>&1 > all.log`]{#stderr-before-stdout explanation="これは stderr を stdout の元の出力先へ接続してから stdout だけをファイルへ移すため、ストリームが分かれます。"}
::option[`command 2> all.log > /dev/null`]{#stderr-file-stdout-null explanation="stderr は `all.log` へ送りますが、stdout は破棄します。両方をファイルへまとめていません。"}
::option[`command > all.log 2>&1`]{#stdout-then-stderr .correct explanation="最初に stdout をファイルへ送り、次に stderr がその時点の stdout の出力先を複製します。"}
:::

Bash では、両方のストリームでファイルを置き換える短い構文 `&>` も使えます。

```bash
$ ls /fake/directory /etc/passwd &> combined.txt
```

Bash で両方を追記するには `&>>` を使います。`> file 2>&1` という明示的な形も、シェルスクリプトや文書でよく使われるため覚えておきましょう。

:::single-choice{#stderr-bash-short-form}
`build` の stdout と stderr を両方とも `build.log` へ追記する Bash コマンドはどれですか？

::option[`build &> build.log`]{#replace-both-build explanation="Bash の `&>` は両方をリダイレクトしますが、既存ファイルへ追記せず置き換えます。"}
::option[`build 2>> build.log`]{#append-errors-build explanation="これは stderr だけを追記します。stdout の出力先は変わりません。"}
::option[`build &>> build.log`]{#append-both-build .correct explanation="Bash の `&>>` はファイルディスクリプタ 1 と 2 を同じ出力先へ追記します。"}
:::

## ストリームを意図的に破棄する

`/dev/null` は書き込まれたデータを破棄する特殊なデバイスです。診断が想定内で不要だと確認した場合にだけ、stderr をそこへリダイレクトします。

```bash
$ ls /fake/directory 2> /dev/null
```

これはコマンドを成功させるものでも、終了ステータスを変えるものでもなく、診断ストリームを隠すだけです。トラブルシューティング中は、必要な情報を破棄せず保存または表示しましょう。

:::single-choice{#stderr-dev-null-effect}
`check-data 2> /dev/null` は何を変更しますか？

::option[stdout を破棄し、すべてのエラーを成功に変える。]{#discard-stdout-success explanation="ディスクリプタ 2 は stdout ではなく stderr であり、リダイレクトはプログラムの終了ステータスを書き換えません。"}
::option[stderr を破棄するが、終了ステータスを強制的に成功にはしない。]{#discard-stderr-only .correct explanation="リダイレクトは診断の出力先を変えます。成功か失敗かは引き続きプログラム自身が決めます。"}
::option[stderr を `/dev/null` という隠しファイルへ保存する。]{#save-dev-null explanation="`/dev/null` は書き込まれたデータを破棄し、後で復元する保存ファイルではありません。"}
:::

3 つの標準ストリームの管理を練習するには、次のハンズオンラボを試してください。

1. **[Linux における入出力のリダイレクト](https://labex.io/ja/labs/comptia-redirecting-input-and-output-in-linux-590840)** - `>`、`>>`、`2>` などの演算子や `tee` コマンドを使い、標準出力、標準エラー、標準入力を操作してデータフローを制御します。

## まとめ

診断を通常のコマンド出力から分けたり、両者をまとめたりできるようになりました。

1. stderr がファイルディスクリプタ 2 であることを認識する。
2. `2>` または `2>>` でエラーログを置き換えるか追記する。
3. 複数のリダイレクトを左から右へ適用する。
4. 意図に合った構文で両方の出力ストリームをまとめる。
5. 情報を失ってもよい場合にだけ診断を破棄する。
