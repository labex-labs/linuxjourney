---
index: 6
lang: "ja"
title: "file"
meta_title: "file - コマンドライン"
meta_description: "Linux の`file`コマンドを使用して、ファイルの種類と内容を識別する方法を学びます。この初心者向けのガイドで、Linux のファイル命名規則を理解しましょう。"
meta_keywords: "Linux file コマンド，ファイルタイプ識別，Linux チュートリアル，ファイル命名，初心者向け Linux, Linux ガイド"
---

## Lesson Content

前回のレッスンでは、`touch`について学びました。少し振り返ってみましょう。ファイル名が、Windows などの他のオペレーティングシステムで見たことがあるような、標準的な命名規則に準拠していないことに気づきましたか？通常、`banana.jpeg`というファイルは JPEG 画像ファイルであると予想するでしょう。

Linux では、ファイル名がファイルの内容を表す必要はありません。実際には GIF ではない`funny.gif`というファイルを作成できます。

ファイルがどのような種類のファイルであるかを知るには、`file`コマンドを使用できます。これにより、ファイルの内容の説明が表示されます。

```bash
file banana.jpg
```

## Exercise

いくつかの異なるディレクトリとファイルに対して`file`コマンドを実行し、その出力をメモしてください。

## Quiz Question

ファイルのファイルタイプを調べるには、どのコマンドを使用できますか？

## Quiz Answer

file
