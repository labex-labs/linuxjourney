---
index: 15
lang: "ja"
title: "wc と nl"
meta_title: "wc および nl - テキスト処理の達人"
meta_description: "wc および nl Linux コマンドを学びましょう。単語数、行番号付け、ファイル分析を理解しましょう。今すぐ Linux コマンドラインスキルを向上させましょう！"
meta_keywords: "wc コマンド，nl コマンド，Linux 単語数，Linux 行番号，ファイル分析，Linux チュートリアル，初心者 Linux, Linux ガイド"
---

## Lesson Content

`wc` (word count) コマンドは、ファイル内の単語の総数を表示します。

```bash
$ wc /etc/passwd
 96     265    5925 /etc/passwd
```

これは、行数、単語数、バイト数をそれぞれ表示します。

特定のフィールドのカウントのみを表示するには、それぞれ `-l`、`-w`、または `-c` オプションを使用します。

```bash
$ wc -l /etc/passwd
96
```

ファイル内の行数をチェックするために使用できるもう 1 つのコマンドは、`nl` (number lines) コマンドです。

```plaintext
file1.txt
i
like
turtles
```

```bash
$ nl file1.txt
1. i
2. like
3. turtles
```

## Exercise

練習は完璧をもたらします！Linux でのテキストカウントと行番号付けの理解を深めるための実践的なラボをいくつか紹介します。

1. **[Linux wc コマンド：テキストカウント](https://labex.io/ja/labs/linux-linux-wc-command-text-counting-219200)** - `wc` コマンドを使用して、テキストファイル内の単語、行、文字を数える練習をします。
2. **[Linux nl コマンド：行番号付け](https://labex.io/ja/labs/linux-linux-nl-command-line-numbering-210988)** - `nl` コマンドで行番号を付ける方法を学びます。
3. **[単語カウントとソート](https://labex.io/ja/labs/linux-word-count-and-sorting-388125)** - `wc` の知識を応用して行、単語、文字を数え、実用的なテキスト分析タスクのためにソートと組み合わせます。

これらのラボは、実際のシナリオで概念を適用し、Linux でのテキスト処理に自信を持つのに役立ちます。

## Quiz Question

ファイル内の単語の総数を取得し、単語のみを取得するために使用するコマンドは何ですか？

## Quiz Answer

wc -w
