---
index: 3
lang: "ja"
title: "stderr（標準エラー出力）"
meta_title: "stderr（標準エラー出力） - Text-Fu"
meta_description: "Linux で標準エラー出力を管理する方法を学びます。このガイドでは、stderr のリダイレクト、stderr ファイルディスクリプタ（2）、および 2>、2>&1、&>を使用して stderr をファイルまたは/dev/null にリダイレクトする方法について説明します。"
meta_keywords: "stderr, 標準エラー出力 Linux, stderr ファイルディスクリプタ，stderr ファイル，Linux 標準エラー, stderr リダイレクト，2>, 2>&1, &>, /dev/null, bash エラー処理"
---

## Lesson Content

コマンドがエラーを生成したときに何が起こるかを探ってみましょう。存在しないディレクトリの内容をリストし、その出力を `peanuts.txt` という名前のファイルにリダイレクトしてみてください。

```bash
ls /fake/directory > peanuts.txt
```

クリーンなプロンプトの代わりに、画面にエラーメッセージが表示されます。

```plaintext
ls: cannot access /fake/directory: No such file or directory
```

なぜこのメッセージがファイルに送信されなかったのか疑問に思うかもしれません。これは、別の I/O ストリームである**標準エラー**、または**stderr**が関係しているためです。

### Linux における標準エラー (Standard Error) とは？

Linux では、`stderr` はプログラムがエラーメッセージや診断情報を送信するために使用するデフォルトの出力ストリームです。これは、通常のプログラム出力に使用される標準出力 (`stdout`) ストリームとは完全に分離されています。デフォルトでは、`stdout` と `stderr` の両方が出力をターミナル画面に送信するため、エラーメッセージが直接表示されます。

`stderr` を制御するには、別のリダイレクト方法が必要です。

### ファイルディスクリプタの理解

`stdin`、`stdout`、`stderr` のような I/O ストリームを管理するために、システムはファイルディスクリプタを使用します。**ファイルディスクリプタ**とは、カーネルがオープンされたファイルやストリームを識別するために使用する非負の数値です。デフォルトのファイルディスクリプタは次のとおりです。

- `0`: stdin (標準入力)
- `1`: stdout (標準出力)
- `2`: stderr (標準エラー)

The number `2` is the dedicated **stderr file descriptor**, and we can use it to control where error messages go.

### stderr をファイルにリダイレクトする

`stderr` をファイルにリダイレクトするには、ファイルディスクリプタ `2` の後に `>` 演算子を使用します。このコマンドは、すべてエラーメッセージを指定された `stderr file` に送信します。

```bash
ls /fake/directory 2> peanuts.txt
```

これで、ターミナルは静かになり、エラーメッセージは `peanuts.txt` の中に入ります。

### stdout と stderr の結合

通常の出力とエラーメッセージの両方を同じファイルにキャプチャしたい場合はどうでしょうか？両方のストリームをリダイレクトすることで実現できます。

```bash
ls /fake/directory /etc/passwd > peanuts.txt 2>&1
```

これを分解してみましょう。

1. `> peanuts.txt` は `stdout` (ファイルディスクリプタ 1) を `peanuts.txt` ファイルにリダイレクトします。
2. `2>&1` は `stderr` (ファイルディスクリプタ 2) を、現在 `stdout` (ファイルディスクリプタ 1) が指しているのと同じ場所にリダイレクトします。

順序は重要です。`2>&1` は `stderr` を `stdout` の現在の宛先に送信します。この場合、`stdout` はファイルを参照しているため、`stderr` もそのファイルに送信されます。

`stdout` と `stderr` の両方をリダイレクトする、よりモダンで短い方法は `&>` を使用することです。

```bash
ls /fake/directory /etc/passwd &> peanuts.txt
```

### エラーメッセージの破棄

場合によっては、コマンドを実行し、発生する可能性のあるエラーメッセージを完全に無視したいことがあります。これを行うには、`stderr` を `/dev/null` という特別なファイルにリダイレクトします。これは、そこに書き込まれたデータを破棄します。

```bash
ls /fake/directory 2> /dev/null
```

このコマンドは実行され、`stderr` からのエラー出力は `/dev/null` に送信されて破棄されるため、画面はクリーンなままになります。

## Exercise

練習あるのみです！入出力リダイレクトの理解を深めるための実践的なラボを次に示します。

1. **[Linux における入力と出力のリダイレクト](https://labex.io/ja/labs/comptia-redirecting-input-and-output-in-linux-590840)** - このラボでは、Linux シェルでの入力と出力のリダイレクトについて学習します。標準出力 (stdout)、標準エラー (stderr)、および標準入力 (stdin) を、演算子 (>, >>, 2>、tee コマンドなど) を操作することで制御し、コマンドからのデータフローを操作する練習をします。

このラボは、I/O リダイレクトの概念を実際のシナリオに適用し、Linux でのデータストリーム管理に対する自信を構築するのに役立ちます。

## Quiz Question

stderr ストリームをリダイレクトするために使用される演算子はどれですか？回答には正確な演算子を指定してください。

## Quiz Answer

2>
