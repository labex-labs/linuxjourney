---
lesson_id: "stdin-standard-in-redirect"
course_id: "text-fu"
lang: "ja"
order_index: 2
title: "stdin（標準入力）"
description: "プログラムが標準入力を読み取る仕組みと、Bash がそのストリームをファイルへ接続する方法を学びます。"
meta_title: "stdin（標準入力） - Text-Fu"
meta_description: "stdin（標準入力）のリダイレクトを学ぶことで、Linux コマンドライン操作を習得しましょう。このガイドでは、stdin と stdout の関係、'<'演算子の使用方法、およびデータストリームを効果的に管理するための「cat stdin」などの実践的な例を解説します。"
meta_keywords: "stdin, 標準入力，stdin リダイレクト，cat stdin, stdin と stdout, Linux リダイレクト，コマンドライン，入力ストリーム"
---

標準入力（**stdin**）は、プログラムが通常、受け取ったデータを読み込むストリームです。対話型端末では、シェルは一般に stdin を端末入力へ接続するため、プログラムは入力した内容を読み取れます。

## 標準入力とファイルディスクリプタ 0

慣例として、3 つの標準ストリームには次のファイルディスクリプタ番号が使われます。

- `0`：標準入力（`stdin`）
- `1`：標準出力（`stdout`）
- `2`：標準エラー（`stderr`）

プログラムは、これらのストリームを使うかどうか、またどのように使うかを選べます。stdin を読み取るよう設計されたコマンドは、ファイルオペランドなどの入力元を指定しなければ、端末からの入力を待つことがよくあります。

:::single-choice{#stdin-descriptor-number}
慣例上、標準入力を表すファイルディスクリプタはどれですか？

::option[`0`]{#stdin-fd-zero .correct explanation="標準入力には、慣例としてファイルディスクリプタ 0 が使われます。"}
::option[`1`]{#stdin-fd-one explanation="ファイルディスクリプタ 1 は、通常の結果を送る標準出力を表します。"}
::option[`2`]{#stdin-fd-two explanation="ファイルディスクリプタ 2 は標準エラーを表し、標準入力ではありません。"}
:::

## ファイルを stdin へリダイレクトする

`<` 演算子は、ファイルを読み取り用に開き、コマンドの stdin へ接続するよう Bash に指示します。

```bash
$ cat < peanuts.txt
Hello World
```

`< peanuts.txt` を処理するのはシェルです。`cat` は単にファイルディスクリプタ 0 から読み取ります。パス名は通常のファイルオペランドとして `cat` に渡されません。

入力ファイルが存在しない、または開けない場合、シェルはリダイレクトエラーを報告し、その入力でコマンドを起動しません。

:::single-choice{#stdin-from-file}
`sort` の標準入力を `names.txt` から読み取らせるコマンドはどれですか？

::option[`sort < names.txt`]{#sort-stdin-file .correct explanation="Bash は `names.txt` を読み取り用に開き、ファイルディスクリプタ 0 で `sort` へ接続します。"}
::option[`sort > names.txt`]{#stdout-to-names explanation="大なり記号は stdout をファイルへリダイレクトし、そのファイルを切り詰めることがあります。入力としてファイルを渡すものではありません。"}
::option[`sort names.txt >`]{#incomplete-sort-output explanation="これは出力リダイレクトが不完全です。要求された stdin の接続を表していません。"}
:::

## ファイルオペランドと入力リダイレクトの違い

コマンドによっては、ファイル名オペランドと stdin のどちらも受け取れますが、結果がわずかに異なることがあります。たとえば次のとおりです。

```bash
$ wc -l peanuts.txt
1 peanuts.txt
$ wc -l < peanuts.txt
1
```

どちらも同じデータの行数を数えています。1 つ目では、`wc` はファイル名を引数として受け取るため、その名前を認識しています。2 つ目では stdin のストリームだけを受け取るため、表示するファイル名がありません。

:::single-choice{#stdin-not-command-argument}
`wc -l < peanuts.txt` の出力に通常 `peanuts.txt` が含まれないのはなぜですか？

::option[`wc` は行数を数え終えるとファイル名を削除するから。]{#stdin-delete-name explanation="このコマンドは元ファイルの名前を変更したり削除したりしません。異なるのは入力の接続方法だけです。"}
::option[`<` 演算子がコマンドの表示する単語をすべて隠すから。]{#stdin-hide-words explanation="入力リダイレクトは stdout をフィルタリングしません。ファイル名がないのは、`wc` がそれを引数として受け取っていないためです。"}
::option[Bash がファイル名の引数ではなく stdin としてファイルを渡すから。]{#stdin-no-filename .correct explanation="シェルがリダイレクトを処理してファイルをディスクリプタ 0 へ接続するため、`wc` にはパス名がオペランドとして渡されません。"}
:::

## 入力と出力のリダイレクトを組み合わせる

1 つのコマンドラインで複数のストリームをリダイレクトできます。

```bash
$ cat < peanuts.txt > banana.txt
```

シェルは独立した 2 つの接続を行います。

1. `< peanuts.txt` は `peanuts.txt` を `cat` の stdin として開きます。
2. `> banana.txt` は `banana.txt` を作成または切り詰めて、`cat` の stdout へ接続します。

`cat` は stdin からバイトを読み取り、stdout へ書き出すため、`banana.txt` には元の内容が入ります。通常のファイルコピーなら `cp peanuts.txt banana.txt` のほうが意図を直接伝えられますが、ここでの例はストリームの接続を示すものです。

:::single-choice{#stdin-and-stdout-files}
`cat < input.txt > output.txt` では、どのファイルが stdin を供給し、どのファイルが stdout を受け取りますか？

::option[`output.txt` が stdin を供給し、`input.txt` が stdout を受け取る。]{#stdin-output-stdout-input explanation="これはリダイレクト演算子の意味を逆にしています。入力の矢印はコマンドへ、出力の矢印はファイルへ向かいます。"}
::option[`input.txt` が stdin を供給し、`output.txt` が stdout を受け取る。]{#stdin-input-stdout-output .correct explanation="`<` リダイレクトは `input.txt` をディスクリプタ 0 用に開き、`>` は `output.txt` をディスクリプタ 1 用に開きます。"}
::option[両方のファイルが stdin を供給し、stdout は端末のまま。]{#both-stdin explanation="2 つの演算子は異なる標準ストリームに作用します。`>` は stdout を端末から別の場所へリダイレクトします。"}
:::

入力と出力のリダイレクトを練習するには、次のハンズオンラボを試してください。

1. **[Linux における入出力のリダイレクト](https://labex.io/ja/labs/comptia-redirecting-input-and-output-in-linux-590840)** - `>`、`>>`、`2>` などの演算子や `tee` コマンドを使って標準出力、標準エラー、標準入力を操作し、コマンドからのデータフローを制御する練習をします。
2. **[データストリームのリダイレクト](https://labex.io/ja/labs/linux-data-stream-redirection-17995)** - Linux のストリームリダイレクトを学びます。標準入力、出力、エラーストリームを操作し、出力を結合し、高度なファイル操作に `/dev/null` を利用します。

## まとめ

シェルを通じて、コマンドの標準入力をファイルへ接続できるようになりました。

1. stdin がファイルディスクリプタ 0 であることを認識する。
2. `<` で読み取り可能なファイルをリダイレクトする。
3. ファイル名オペランドとリダイレクトされた入力を区別する。
4. stdin と stdout のリダイレクトを意図的に組み合わせる。
