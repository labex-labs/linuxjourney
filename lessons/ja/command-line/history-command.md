---
index: 9
lang: "ja"
title: "history"
meta_title: "history - コマンドライン"
meta_description: "Linux の history コマンド、!! ショートカット、Ctrl-R を使って効率的にコマンドを呼び出す方法を学びましょう。これらの必須のヒントでターミナルの生産性を向上させましょう！"
meta_keywords: "Linux history, bash history, Ctrl-R, clear command, Linux tutorial, command line, beginner guide"
---

## Lesson Content

シェルには、以前に入力したコマンドの履歴があります。これらのコマンドを実際に確認することができます。これは、以前に使用したコマンドを再入力せずに見つけて実行したい場合に非常に便利です。

```bash
history
```

以前と同じコマンドを実行したいですか？上矢印を押すだけです。

前のコマンドを再入力せずに実行したいですか？ `!!` を使用します。もし `cat file1` と入力して、それをもう一度実行したい場合、単に `!!` と入力するだけで、最後に実行したコマンドが実行されます。

もう一つの履歴ショートカットは `Ctrl-R` です。これは逆検索コマンドです。`Ctrl-R` を押して、目的のコマンドの一部を入力し始めると、一致するものが表示されます。`Ctrl-R` キーをもう一度押すことで、それらをナビゲートできます。もう一度使用したいコマンドを見つけたら、Enter キーを押すだけです。

ターミナルが少し散らかってきましたね？少し整理しましょう。`clear` コマンドを使用してディスプレイをクリアします。

```bash
clear
```

ほら、その方が見栄えがいいでしょう？

便利なことについて話している間に、コマンドライン環境で最も便利な機能の 1 つはタブ補完です。コマンド、ファイル、ディレクトリなどの先頭を入力し始め、Tab キーを押すと、検索しているディレクトリ内で見つかったものに基づいて自動補完されます。ただし、同じ文字で始まる他のファイルがない場合に限ります。たとえば、`chrome` コマンドを実行しようとしている場合、`chr` と入力して Tab を押すと、`chrome` に自動補完されます。

## Exercise

上矢印キーと下矢印キーを使って、以前のコマンド履歴をナビゲートしてください。`Ctrl-R` 逆検索を試してみてください。

Linux コマンドラインナビゲーションの追加の実践練習については、以下のインタラクティブなラボを探索してください。

- [Linux Directory Navigation](https://labex.io/ja/labs/linux-directory-navigation-387844)
- [Linux ls Command: Content Listing](https://labex.io/ja/labs/linux-linux-ls-command-content-listing-219205)

## Quiz Question

ターミナルをクリアするコマンドは何ですか？

## Quiz Answer

clear
