---
lang: "ja"
title: "paste"
meta_description: "Linux の paste コマンドを使ってファイルの行を結合する方法を学びましょう。この必須の Linux コマンドチュートリアルで、区切り文字を発見し、ファイルを結合しましょう。"
meta_keywords: "Linux paste コマンド，paste コマンドチュートリアル，ファイル行の結合，Linux コマンド，初心者 Linux, Linux ガイド"
---

## Lesson Content

`paste`コマンドは`cat`コマンドに似ており、ファイル内の行を結合します。以下の内容で新しいファイルを作成しましょう。

```
sample2.txt
The
quick
brown
fox
```

これらの行をすべて 1 行に結合してみましょう。

```bash
paste -s sample2.txt
```

`paste`のデフォルトの区切り文字は TAB なので、各単語が TAB で区切られた 1 行になります。

この区切り文字 (`-d`) をもう少し読みやすいものに変更してみましょう。

```bash
paste -d ' ' -s sample2.txt
```

これで、すべてがスペースで区切られた 1 行になるはずです。

## Exercise

複数のファイルを一緒に paste してみてください。何が起こりますか？

## Quiz Question

すべてを 1 行にするために`paste`で使用するフラグは何ですか？

## Quiz Answer

-s
