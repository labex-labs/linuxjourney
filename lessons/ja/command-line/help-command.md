---
index: 15
lang: "ja"
title: "help"
meta_title: "help - コマンドライン"
meta_description: "Bashで'help'コマンドを使用して、コマンドラインでの迅速な支援を得る方法を学びます。組み込みコマンドを理解し、Linuxプログラムのオプションを見つけます。"
meta_keywords: "Linux helpコマンド, Bash help, コマンドラインヘルプ, Linuxコマンド, Linux初心者, Linuxチュートリアル, Bashチュートリアル"
---

## Lesson Content

Linuxには、コマンドの使用方法を理解したり、コマンドで利用可能なフラグを確認したりするのに役立つ優れた組み込みツールがいくつかあります。そのうちの1つである`help`は、他のBashコマンド（例：`echo`、`logout`、`pwd`）のヘルプを提供する組み込みのBashコマンドです。

```bash
help echo
```

これにより、`echo`を実行したいときに使用できる説明とオプションが表示されます。他の実行可能プログラムの場合、`--help`またはそれに類するオプションを持つのが慣例です。

```bash
echo --help
```

実行可能ファイルを配布するすべての開発者がこの標準に準拠するわけではありませんが、プログラムに関するヘルプを見つけるには、これが最も良い方法でしょう。

## Exercise

このトピックに関する特定のラボはありませんが、関連するLinuxスキルと概念を練習するために、包括的な[Linux学習パス](https://labex.io/ja/learn/linux)を探索することをお勧めします。

## Quiz Question

組み込みのBashコマンドのコマンドラインヘルプを素早く取得するにはどうすればよいですか？

## Quiz Answer

help