---
index: 14
lang: "ja"
title: "uniq (ユニーク)"
meta_title: "uniq (ユニーク) - テキスト操作"
meta_description: "Linux の`uniq`コマンドを使用して、テキストファイルから重複する行を削除する方法を学びます。-c、-u、-d などのオプションを発見し、`sort`と組み合わせて効果的なデータクリーンアップを行う方法を学びましょう。"
meta_keywords: "uniq コマンド，Linux uniq, 重複削除，sort uniq, Linux チュートリアル，テキスト処理，初心者 Linux, Linux ガイド"
---

## Lesson Content

`uniq` (unique) コマンドは、テキストを解析するためのもう 1 つの便利なツールです。

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

行の出現回数を取得してみましょう。

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

**注**: `uniq` は、隣接していない重複行を検出しません。例えば：

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

`uniq` によって返される結果は、最初の例とは異なり、すべてのエントリを含みます。

`uniq` のこの制限を克服するために、`sort` と `uniq` を組み合わせて使用できます。

```bash
$ sort reading.txt | uniq
article
book
magazine
paper
```

## Exercise

`uniq -uc` を試した場合、どのような結果が得られますか？

## Quiz Question

ファイル内の重複を削除するために使用するコマンドは何ですか？

## Quiz Answer

uniq
