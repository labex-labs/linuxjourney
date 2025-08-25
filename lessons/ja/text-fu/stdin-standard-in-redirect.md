---
index: 2
lang: "ja"
title: "stdin (標準入力)"
meta_title: "stdin (標準入力) - Text-Fu"
meta_description: "Linux での stdin（標準入力）リダイレクトについて学びます。ファイルやコマンドで「<」演算子を使用する方法を理解します。実践的な例を探求し、Linux コマンドラインスキルを向上させます。"
meta_keywords: "stdin, 標準入力，Linux リダイレクト，< 演算子，Linux チュートリアル，コマンドライン，初心者，ガイド"
---

## Lesson Content

前回のレッスンでは、ファイルや画面など、使用できるさまざまな stdout ストリームがあることを学びました。同様に、使用できるさまざまな標準入力 (stdin) ストリームもあります。キーボードのようなデバイスからの stdin があることは知っていますが、ファイル、他のプロセスからの出力、およびターミナルも使用できます。例を見てみましょう。

この例では、前回のレッスンで使用した `peanuts.txt` ファイルを使用しましょう。覚えているかもしれませんが、その中には「Hello World」というテキストが含まれていました。

```bash
cat < peanuts.txt > banana.txt
```

stdout リダイレクトに `>` を使用したのと同様に、stdin リダイレクトには `<` を使用できます。

通常、`cat` コマンドでは、ファイルを送信するとそのファイルが stdin になります。この場合、`peanuts.txt` を stdin としてリダイレクトしました。その後、`cat peanuts.txt` の出力（「Hello World」）が `banana.txt` という別のファイルにリダイレクトされます。

## Exercise

練習は完璧をもたらします！Linux での入出力リダイレクトの理解を深めるための実践的なラボをいくつか紹介します。

1. **[Linux での入出力のリダイレクト](https://labex.io/ja/labs/comptia-redirecting-input-and-output-in-linux-590840)** - `>`、`>>`、`2>`、および `tee` コマンドなどの演算子を使用して、標準出力 (stdout)、標準エラー (stderr)、および標準入力 (stdin) を操作することで、コマンドからのデータフローを制御する練習をします。
2. **[データストリームのリダイレクト](https://labex.io/ja/labs/linux-data-stream-redirection-17995)** - Linux ストリームリダイレクトの技術を学びます。標準入力、出力、およびエラーのストリームを操作し、出力を結合し、高度なファイル操作のために `/dev/null` を利用します。
3. **[シーケンス制御とパイプライン](https://labex.io/ja/labs/linux-sequence-control-and-pipeline-17994)** - コマンド実行シーケンスを制御し、あるコマンドからの出力を別のコマンドへの入力として指示するために不可欠なパイプラインを利用する方法を学びます。

これらのラボは、実際のシナリオで入出力リダイレクトの概念を適用し、シェルスクリプトとデータ操作に自信をつけるのに役立ちます。

## Quiz Question

stdin をリダイレクトするために使用するリダイレクタは何ですか？

## Quiz Answer

<
