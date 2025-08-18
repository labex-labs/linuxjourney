---
lang: "ja"
title: "stdin (標準入力)"
meta_title: "stdin (標準入力) - テキスト操作"
meta_description: "Linux における stdin（標準入力）のリダイレクトについて学びます。ファイルやコマンドで '<' 演算子を使用する方法を理解します。実践的な例を探求し、Linux コマンドラインスキルを向上させます。"
meta_keywords: "stdin, 標準入力，Linux リダイレクト，< 演算子，Linux チュートリアル，コマンドライン，初心者，ガイド"
---

## Lesson Content

前回のレッスンでは、ファイルや画面など、使用できるさまざまな stdout ストリームがあることを学びました。同様に、使用できるさまざまな標準入力（stdin）ストリームもあります。キーボードのようなデバイスからの stdin があることは知っていますが、ファイル、他のプロセスからの出力、およびターミナルも使用できます。例を見てみましょう。

この例では、前回のレッスンで使用した `peanuts.txt` ファイルを使用します。このファイルには「Hello World」というテキストが含まれていました。

```bash
cat < peanuts.txt > banana.txt
```

stdout リダイレクトに `>` を使用したのと同様に、stdin リダイレクトには `<` を使用できます。

通常、`cat` コマンドでは、ファイルを送信するとそのファイルが stdin になります。この場合、`peanuts.txt` を stdin としてリダイレクトしました。その後、`cat peanuts.txt` の出力である「Hello World」が `banana.txt` という別のファイルにリダイレクトされます。

## Exercise

いくつかのコマンドを試してください。

```bash
echo < peanuts.txt > banana.txt
ls < peanuts.txt > banana.txt
pwd < peanuts.txt > banana.txt
```

## Quiz Question

stdin をリダイレクトするために使用するリダイレクタは何ですか？

## Quiz Answer

<
