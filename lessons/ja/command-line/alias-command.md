---
index: 18
lang: "ja"
title: "alias"
meta_title: "alias - コマンドライン"
meta_description: "一般的なコマンドの Linux エイリアスを作成および管理する方法を学びます。.bashrc での一時的および永続的なエイリアス設定を発見します。コマンドラインの効率を向上させましょう！"
meta_keywords: "Linux alias, bash alias, unalias command, .bashrc, Linux tutorial, command line, beginner Linux, Linux guide"
---

## Lesson Content

コマンドを入力するのが非常に面倒になったり、長いコマンドを何度も入力する必要がある場合は、それに対して使用できるエイリアスを持つのが最善です。コマンドのエイリアスを作成するには、エイリアス名を指定し、それをコマンドに設定するだけです。

```bash
alias foobar='ls -la'
```

これで、`ls -la`と入力する代わりに、`foobar`と入力するだけでそのコマンドが実行されます。これは非常に便利です。このコマンドは再起動後にエイリアスを保存しないことに注意してください。そのため、再起動後もエイリアスを保持したい場合は、永続的なエイリアスを以下に追加する必要があります。

```plaintext
~/.bashrc
```

または同様のファイルに追加します。

`unalias`コマンドでエイリアスを削除できます。

```bash
unalias foobar
```

## Exercise

いくつかのエイリアスを作成し、それらを削除してください。

Linux コマンドラインの基本をさらに実践的に練習するには、以下のインタラクティブなラボを探索してください。

- [Linux Directory Navigation](https://labex.io/ja/labs/linux-directory-navigation-387844)
- [Linux ls Command: Content Listing](https://labex.io/ja/labs/linux-linux-ls-command-content-listing-219205)

## Quiz Question

エイリアスを作成するために使用されるコマンドは何ですか？

## Quiz Answer

alias
