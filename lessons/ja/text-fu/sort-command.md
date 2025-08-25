---
index: 12
lang: "ja"
title: "sort"
meta_title: "sort - テキスト処理の達人"
meta_description: "Linux の sort コマンドを使ってテキストファイルをソートする方法を学びましょう。逆順ソートや数値ソートなどのオプションを発見してください。Linux コマンドラインスキルを向上させましょう！"
meta_keywords: "Linux sort コマンド，sort -r, sort -n, Linux チュートリアル，コマンドライン，初心者 Linux, sort ガイド"
---

## Lesson Content

`sort`コマンドは、行をソートするのに便利です。

```plaintext
file1.txt
dog
cow
cat
elephant
bird

$ sort file1.txt
bird
cat
cow
dog
elephant
```

逆順にソートすることもできます。

```bash
$ sort -r file1.txt
elephant
dog
cow
cat
bird
```

数値でソートすることもできます。

```bash
$ sort -n file1.txt
bird
cat
cow
elephant
dog
```

## Exercise

練習は完璧をもたらします！`sort`コマンドとテキスト処理の理解を深めるための実践的なラボをいくつか紹介します。

1. **[Linux sort コマンド：テキストのソート](https://labex.io/ja/labs/linux-linux-sort-command-text-sorting-219196)** - このラボでは、`sort`コマンドの直接的な紹介を提供し、昇順および降順を含むさまざまな方法でテキストファイルの行をソートする練習ができます。
2. **[単語のカウントとソート](https://labex.io/ja/labs/linux-word-count-and-sorting-388125)** - この課題では、単語のカウントとソートの知識を適用してテキストデータを分析し、頻繁なパターンを見つけ、データを効率的にソートするのに役立ちます。

これらのラボは、実際のシナリオで概念を適用し、Linux でのテキスト操作とソートに自信をつけるのに役立ちます。

## Quiz Question

逆順ソートを実行するために使用するフラグは何ですか？

## Quiz Answer

-r
