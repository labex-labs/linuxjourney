---
lang: "ja"
title: "tr (Translate)"
description: "Linux の'tr'コマンドを使って文字を変換・削除する方法を学びます。文字変換の例と演習を通して理解を深めましょう。Linux の学習を始めましょう！"
keywords: "tr command, Linux tr, 文字変換，文字削除，Linux チュートリアル，初心者 Linux, Linux ガイド"
---

## Lesson Content

`tr` (translate) コマンドは、ある文字セットを別の文字セットに変換することができます。すべての小文字を大文字に変換する例を試してみましょう。

```bash
$ tr a-z A-Z
hello
HELLO
```

ご覧のとおり、`a-z` の範囲を `A-Z` にすることで、入力されたすべての小文字が大文字に変換されます。

## Exercise

次のコマンドを試してください。何が起こりますか？

```bash
$ tr -d ello
hello
```

## Quiz Question

文字を変換するために使用されるコマンドは何ですか？

## Quiz Answer

tr
