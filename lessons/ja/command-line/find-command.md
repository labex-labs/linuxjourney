---
lang: "ja"
title: ""find""
meta_description: "Linux の'find'コマンドを使ってファイルやディレクトリを見つける方法を学びましょう。基本的な検索オプションを発見し、Linux のファイル管理スキルを向上させましょう。"
meta_keywords: "Linux find コマンド，Linux ファイル検索，Linux ディレクトリ検索，find コマンド チュートリアル，Linux ファイル管理，Linux 初心者，Linux ガイド"
---

## Lesson Content

システム上にあるこれらすべてのファイルの中から特定のファイルを見つけ出すのは、少し大変な場合があります。しかし、そのためのコマンドがあります。それが `find` です！

```bash
find /home -name puppies.jpg
```

`find` を使用する場合、検索するディレクトリと検索対象を指定する必要があります。この場合、`puppies.jpg` という名前のファイルを見つけようとしています。

検索しようとしているファイルのタイプを指定できます。

```bash
find /home -type d -name MyFolder
```

ここでは、検索しようとしているファイルのタイプをディレクトリを示す `d` に設定し、引き続き `MyFolder` という名前で検索していることがわかります。

注目すべきクールな点の 1 つは、`find` が検索しているディレクトリで止まらないことです。そのディレクトリが持つサブディレクトリ内も検索します。

## Exercise

1. ルートディレクトリから「net」という単語を含むファイルを見つけなさい。

## Quiz Question

名前で検索したい場合、`find` にどのオプションを指定すべきですか？

## Quiz Answer

-name
