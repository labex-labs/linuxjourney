---
index: 7
lang: "ja"
title: "paste"
meta_title: "paste - テキスト操作"
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

この区切り文字（`-d`）をもう少し読みやすいものに変更してみましょう。

```bash
paste -d ' ' -s sample2.txt
```

これで、すべてがスペースで区切られた 1 行になるはずです。

## Exercise

練習は完璧をもたらします！Linux でのテキスト処理とデータ操作の理解を深めるための実践的なラボをいくつか紹介します。

1. **[シンプルなテキスト処理](https://labex.io/ja/labs/linux-simple-text-processing-18004)** - `tr`、`col`、`join`、`paste`などの強力なコマンドを使用して、テキストデータを効率的に操作および分析する方法を学びます。
2. **[データストリームのリダイレクト](https://labex.io/ja/labs/linux-data-stream-redirection-17995)** - Linux のストリームリダイレクトの技術と、標準入力、出力、エラーのストリームを操作する方法を学びます。これは、`paste`のようなコマンドがどのように動作するかを理解する上で不可欠です。
3. **[シーケンス制御とパイプライン](https://labex.io/ja/labs/linux-sequence-control-and-pipeline-17994)** - コマンドの実行シーケンスを制御し、パイプラインを利用する方法を学び、複雑なデータタスクのために`paste`を他のコマンドと組み合わせる能力を高めます。

これらのラボは、実際のシナリオで概念を適用し、Linux でのテキスト処理とデータ処理に自信をつけるのに役立ちます。

## Quiz Question

`paste`コマンドで、すべてを 1 行にするために使用するフラグは何ですか？

## Quiz Answer

-s
