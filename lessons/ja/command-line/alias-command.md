---
index: 18
lang: "ja"
title: "alias"
meta_title: "alias - コマンドライン"
meta_description: "一般的なコマンドのLinuxエイリアスを作成および管理する方法を学びます。.bashrcでの一時的および永続的なエイリアス設定を発見します。コマンドラインの効率を向上させましょう！"
meta_keywords: "Linux alias, bash alias, unalias command, .bashrc, Linux tutorial, command line, beginner Linux, Linux guide"
---

## Lesson Content

コマンドの入力が非常に反復的になったり、長いコマンドを何度も入力する必要がある場合、それにはエイリアスを使用するのが最善です。コマンドのエイリアスを作成するには、エイリアス名を指定し、それをコマンドに設定するだけです。

```bash
alias foobar='ls -la'
```

これで、`ls -la` と入力する代わりに `foobar` と入力するだけで、そのコマンドが実行されます。これは非常に便利です。このコマンドは再起動後にエイリアスを保存しないことに注意してください。そのため、再起動後も永続的に使用したい場合は、以下の場所に永続的なエイリアスを追加する必要があります。

```plaintext
~/.bashrc
```

または類似のファイルに追加します。

`unalias` コマンドでエイリアスを削除できます。

```bash
unalias foobar
```

## Exercise

このトピックに関する特定のラボはありませんが、関連するLinuxスキルと概念を練習するために、包括的な[Linux学習パス](https://labex.io/ja/learn/linux)を探索することをお勧めします。

## Quiz Question

エイリアスを作成するために使用されるコマンドは何ですか？

## Quiz Answer

alias