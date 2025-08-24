---
index: 15
lang: "ja"
title: "help"
meta_title: "help - コマンドライン"
meta_description: "Bash で'help'コマンドを使用して、コマンドラインで素早くアシスタンスを得る方法を学びます。組み込みコマンドを理解し、Linux プログラムのオプションを見つけます。"
meta_keywords: "Linux help コマンド，Bash help, コマンドラインヘルプ，Linux コマンド，Linux 初心者，Linux チュートリアル，Bash チュートリアル"
---

## Lesson Content

Linux には、コマンドの使用方法を理解したり、コマンドで利用可能なフラグを確認したりするのに役立つ優れた組み込みツールがいくつかあります。そのうちの 1 つである`help`は、他の Bash コマンド（例：`echo`、`logout`、`pwd`）のヘルプを提供する組み込みの Bash コマンドです。

```bash
help echo
```

これにより、`echo`を実行したいときに使用できる説明とオプションが表示されます。他の実行可能プログラムの場合、`--help`またはそれに類するオプションを持つのが慣例です。

```bash
echo --help
```

実行可能ファイルを配布するすべての開発者がこの標準に準拠するわけではありませんが、プログラムに関するヘルプを見つけるにはおそらくこれが最善の方法です。

## Exercise

`echo`コマンド、`logout`コマンド、および`pwd`コマンドで`help`を実行してください。

基本的な Linux コマンドの追加のハンズオン練習については、これらのインタラクティブなラボを探索してください。

- [Linux pwd Command: Directory Displaying](https://labex.io/ja/labs/linux-linux-pwd-command-directory-displaying-209734)
- [Linux cd Command: Directory Changing](https://labex.io/ja/labs/linux-linux-cd-command-directory-changing-209733)

## Quiz Question

組み込みの Bash コマンドのコマンドラインヘルプをすばやく取得するにはどうすればよいですか？

## Quiz Answer

help
