---
index: 14
lang: "ja"
title: "find"
meta_title: "find - コマンドライン"
meta_description: "Linux の'find'コマンドを使ってファイルやディレクトリを検索する方法を学びましょう。基本的な検索オプションを発見し、Linux のファイル管理スキルを向上させましょう。"
meta_keywords: "Linux find コマンド，find files Linux, Linux ディレクトリ検索，find コマンド チュートリアル，Linux ファイル管理，初心者 Linux, Linux ガイド"
---

## Lesson Content

システム上にあるこれらのファイルすべてを考えると、特定のファイルを見つけるのは少し大変になることがあります。しかし、そのために使えるコマンドがあります。それが `find` です！

```bash
find /home -name puppies.jpg
```

`find` を使う場合、検索するディレクトリと検索対象を指定する必要があります。この場合、`puppies.jpg` という名前のファイルを見つけようとしています。

検索したいファイルのタイプを指定できます。

```bash
find /home -type d -name MyFolder
```

ここでは、検索したいファイルのタイプをディレクトリを示す `d` に設定し、引き続き `MyFolder` という名前で検索していることがわかります。

注目すべきクールな点の 1 つは、`find` が検索対象のディレクトリで止まらないことです。そのディレクトリが持つサブディレクトリの中も検索します。

## Exercise

1. ルートディレクトリから「net」という単語を含むファイルを見つけてください。

`find` コマンドの実践的な練習には、このインタラクティブなラボを試してください。

- [Linux find Command: File Searching](https://labex.io/ja/labs/linux-linux-find-command-file-searching-219191)

## Quiz Question

名前で検索したい場合、`find` にどのようなオプションを指定すべきですか？

## Quiz Answer

-name
