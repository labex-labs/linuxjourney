---
lang: "ja"
title: "sort"
meta_description: "Linux の sort コマンドを使ってテキストファイルをソートする方法を学びましょう。逆順ソートや数値ソートなどのオプションを発見してください。Linux のコマンドラインスキルを向上させましょう！"
meta_keywords: "Linux sort コマンド，sort -r, sort -n, Linux チュートリアル，コマンドライン，Linux 初心者，sort ガイド"
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

また、数値でソートすることもできます。

```bash
$ sort -n file1.txt
bird
cat
cow
elephant
dog
```

## Exercise

`sort`の真の力は、他のコマンドと組み合わせる能力にあります。次のコマンドを試して、何が起こるか見てみましょう。

```bash
ls /etc | sort -rn
```

## Quiz Question

逆順ソートを実行するために使用するフラグは何ですか？

## Quiz Answer

-r
