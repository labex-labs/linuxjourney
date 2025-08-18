---
lang: "ja"
title: "wc と nl"
meta_title: "wc と nl - テキスト操作"
meta_description: "wc および nl Linux コマンドを学習します。単語数、行番号付け、ファイル分析を理解します。今すぐ Linux コマンドラインスキルを向上させましょう！"
meta_keywords: "wc コマンド，nl コマンド，Linux 単語数，Linux 行番号，ファイル分析，Linux チュートリアル，初心者 Linux, Linux ガイド"
---

## Lesson Content

`wc` (word count) コマンドは、ファイル内の単語の総数を表示します。

```bash
$ wc /etc/passwd
 96     265    5925 /etc/passwd
```

これは、行数、単語数、バイト数をそれぞれ表示します。

特定のフィールドのカウントのみを表示するには、`-l`、`-w`、または `-c` オプションをそれぞれ使用します。

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

`nl` コマンドを使用して、出力全体を検索せずに総行数を取得するにはどうすればよいですか？ヒント：このコースで学んだ他のコマンドのいくつかを使用してください。

## Quiz Question

ファイル内の単語の総数と単語のみを取得するために使用するコマンドは何ですか？

## Quiz Answer

wc -w
