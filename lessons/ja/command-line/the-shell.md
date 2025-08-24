---
index: 1
lang: "ja"
title: "シェル"
meta_title: "シェル - コマンドライン"
meta_description: "Linux シェル、Bash、そして「echo」のような基本的なコマンドについて学びましょう。シェルプロンプトを理解し、この初心者向けのガイドで Linux の旅を始めましょう。"
meta_keywords: "Linux シェル，Bash, echo コマンド，Linux チュートリアル，コマンドライン，初心者向け Linux, シェルプロンプト，Linux ガイド"
---

## Lesson Content

世界はあなたの思いのまま、いや、シェルこそがあなたの思いのままです。シェルとは何でしょうか？シェルは基本的に、キーボードからのコマンドを受け取り、それをオペレーティングシステムに送信して実行させるプログラムです。GUI を使ったことがあるなら、「ターミナル」や「コンソール」といったプログラムを見たことがあるでしょう。これらは単にシェルを起動するためのプログラムです。このコース全体を通して、シェルの素晴らしさについて学びます。

このコースでは、シェルプログラムである Bash（Bourne Again Shell）を使用します。ほとんどすべての Linux ディストリビューションは、デフォルトで Bash シェルを使用します。`ksh`、`zsh`、`tsch`などの他のシェルも利用可能ですが、それらについては触れません。

早速始めましょう！ディストリビューションによってシェルのプロンプトは異なるかもしれませんが、ほとんどの場合、以下の形式に従います。

```plaintext
username@hostname:current_directory
pete@icebox:/home/pete $
```

プロンプトの末尾にある`$`に気づきましたか？シェルが異なればプロンプトも異なります。この場合、`$`は Bash、Bourne、または Korn シェルを使用している通常のユーザー用です。コマンドを入力する際にプロンプト記号を追加する必要はありません。そこにあるということを知っておいてください。

簡単なコマンド、`echo`から始めましょう。`echo`コマンドは、テキスト引数をディスプレイに出力するだけです。

```bash
echo Hello World
```

## Exercise

異なるテキストで`echo`コマンドを実行してみてください。

Linux の基本コマンドを実践的に学ぶには、以下のインタラクティブなラボを試してみてください。

- [Linux Directory Navigation](https://labex.io/ja/labs/linux-directory-navigation-387844)
- [Linux pwd Command: Directory Displaying](https://labex.io/ja/labs/linux-linux-pwd-command-directory-displaying-209734)
- [Linux ls Command: Content Listing](https://labex.io/ja/labs/linux-linux-ls-command-content-listing-219205)

## Quiz Question

`echo Hello World`と入力したとき、ディスプレイには何が出力されるべきですか？

## Quiz Answer

Hello World
