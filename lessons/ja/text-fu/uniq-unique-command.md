---
index: 14
lang: "ja"
title: "uniq (ユニーク)"
meta_title: "uniq (ユニーク) - テキスト処理"
meta_description: "Linux の `uniq` コマンドを使用して、テキストファイルから重複行を削除する方法を学びます。-c、-u、-d などのオプションを発見し、`sort` と組み合わせて効果的なデータクリーンアップを行います。"
meta_keywords: "uniq コマンド，Linux uniq, 重複削除，sort uniq, Linux チュートリアル，テキスト処理，初心者 Linux, Linux ガイド"
---

## Lesson Content

`uniq` (unique) コマンドは、テキストを解析するためのもう一つの便利なツールです。

重複がたくさんあるファイルがあるとします。

```plaintext
reading.txt
book
book
paper
paper
article
article
magazine
```

そして、重複を削除したい場合、`uniq` コマンドを使用できます。

```bash
$ uniq reading.txt
book
paper
article
magazine
```

行の出現回数を数えてみましょう。

```bash
$ uniq -c reading.txt
2 book
2 paper
2 article
1 magazine
```

一意の値のみを取得してみましょう。

```bash
$ uniq -u reading.txt
magazine
```

重複する値のみを取得してみましょう。

```bash
$ uniq -d reading.txt
book
paper
article
```

**注**: `uniq` は、隣接していない重複行を検出しません。例：

隣接していない重複があるファイルがあるとします。

```plaintext
reading.txt
book
paper
book
paper
article
magazine
article
```

```bash
$ uniq reading.txt
reading.txt
book
paper
book
paper
article
magazine
article
```

`uniq` によって返される結果には、最初の例とは異なり、すべてのエントリが含まれます。

`uniq` のこの制限を克服するために、`sort` と `uniq` を組み合わせて使用できます。

```bash
bash
$ sort reading.txt | uniq
article
book
magazine
paper
```

## Exercise

練習は完璧をもたらします！ここでは、`uniq` と `sort` を使用したテキスト処理の理解を深めるための実践的な演習をいくつか紹介します。

1. **[Linux uniq Command: Duplicate Filtering](https://labex.io/ja/labs/linux-linux-uniq-command-duplicate-filtering-219199)** - Linux の `uniq` コマンドを `sort` と組み合わせて使用し、テキストファイル内の重複行を識別、フィルタリング、分析する方法を学びます。
2. **[Linux sort Command: Text Sorting](https://labex.io/ja/labs/linux-linux-sort-command-text-sorting-219196)** - `sort` コマンドを使用してテキストファイルの行を整理する練習をします。これは、`uniq` を効果的に使用する前の重要なステップです。
3. **[Word Count and Sorting](https://labex.io/ja/labs/linux-word-count-and-sorting-388125)** - この実践的な課題で、Linux の基本的なテキスト処理ツールである `wc` (ワードカウント) と `sort` を学びます。行、単語、文字を数え、頻繁なパターンを見つけ、さまざまなテキスト分析タスクのためにデータを効率的にソートする方法を学びます。

これらの演習は、実際のシナリオで概念を適用し、Linux でのテキスト処理とデータ操作に自信をつけるのに役立ちます。

## Quiz Question

ファイル内の重複を削除するために使用するコマンドは何ですか？

## Quiz Answer

uniq
