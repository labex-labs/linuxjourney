---
index: 14
lang: "ja"
title: "find"
meta_title: "find - コマンドライン"
meta_description: "Linuxの 'find' コマンドを使ってファイルやディレクトリを検索する方法を学びましょう。基本的な検索オプションを発見し、Linuxのファイル管理スキルを向上させましょう。"
meta_keywords: "Linux find コマンド, Linux ファイル検索, Linux ディレクトリ検索, find コマンド チュートリアル, Linux ファイル管理, 初心者 Linux, Linux ガイド"
---

## Lesson Content

システム上にあるこれらのファイルすべてにおいて、特定のファイルを見つけようとすると少し大変になることがあります。しかし、そのためのコマンドがあります。それが `find` です！

```bash
find /home -name puppies.jpg
```

`find` を使う場合、検索するディレクトリと検索対象を指定する必要があります。この場合、`puppies.jpg` という名前のファイルを見つけようとしています。

検索したいファイルのタイプを指定できます。

```bash
find /home -type d -name MyFolder
```

ここでは、検索したいファイルのタイプをディレクトリを示す `d` に設定し、引き続き `MyFolder` という名前で検索していることがわかります。

注目すべきクールな点は、`find` が検索しているディレクトリで止まらないことです。そのディレクトリが持つサブディレクトリの中も検索します。

## Exercise

練習は完璧をもたらします！Linux でファイルやディレクトリを見つけることへの理解を深めるための実践的なラボをいくつか紹介します。

1. **[Linux find コマンド: ファイル検索](https://labex.io/ja/labs/linux-linux-find-command-file-searching-219191)** - このラボでは、さまざまな基準に基づいてファイルやディレクトリを検索・特定するための多機能ユーティリティである `find` コマンドの紹介を行います。`find` を使って特定のファイルを特定する練習をします。
2. **[重要なシステムリソースの発見](https://labex.io/ja/labs/linux-discover-critical-system-resources-388032)** - `find` を含む、ファイルや実行可能ファイルを特定するための重要な Linux コマンドを学びます。ファイルシステムを効率的にナビゲートし、重要なシステムリソースを発見する練習をします。

これらのラボは、概念を実際のシナリオに適用し、`find` コマンドを効果的に使用する自信を築くのに役立ちます。

## Quiz Question

名前で検索したい場合、`find` にどのオプションを指定すべきですか？

## Quiz Answer

-name