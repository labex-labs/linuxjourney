---
index: 1
lang: "ja"
title: "シェル"
meta_title: "シェル - コマンドライン"
meta_description: "Linux シェル、Bash、そして「echo」のような基本的なコマンドについて学びましょう。シェルプロンプトを理解し、この初心者向けのガイドで Linux の旅を始めましょう。"
meta_keywords: "Linux シェル，Bash, echo コマンド，Linux チュートリアル，コマンドライン，初心者 Linux, シェルプロンプト，Linux ガイド"
---

## Lesson Content

世界はあなたの思いのまま、いや、シェルがあなたの思いのままです。シェルとは何でしょうか？シェルは基本的に、キーボードからのコマンドを受け取り、それをオペレーティングシステムに送信して実行させるプログラムです。GUI を使ったことがあるなら、「ターミナル」や「コンソール」といったプログラムを見たことがあるでしょう。これらは単にシェルを起動するためのプログラムです。このコース全体を通して、シェルの素晴らしさについて学びます。

このコースでは、シェルプログラムである Bash（Bourne Again Shell）を使用します。ほとんどすべての Linux ディストリビューションは、デフォルトで Bash シェルを使用します。`ksh`、`zsh`、`tsch`などの他のシェルも利用可能ですが、それらについては触れません。

早速始めましょう！ディストリビューションによってシェルのプロンプトは異なるかもしれませんが、ほとんどの場合、以下の形式に従うはずです。

```plaintext
username@hostname:current_directory
pete@icebox:/home/pete $
```

プロンプトの最後にある`$`に気づきましたか？異なるシェルには異なるプロンプトがあります。この場合、`$`は Bash、Bourne、または Korn シェルを使用している通常のユーザー用です。コマンドを入力するときにプロンプト記号を追加する必要はありません。そこにあるということを知っておいてください。

簡単なコマンド、`echo`から始めましょう。`echo`コマンドは、テキスト引数をディスプレイに出力するだけです。

```bash
echo Hello World
```

## Exercise

Linux の基本コマンドを実践的に練習するには、インタラクティブコース「[Linux Basic Commands Practice Online](https://labex.io/ja/courses/linux-basic-commands-practice-online)」をお勧めします。

## Quiz Question

`echo Hello World`と入力したとき、ディスプレイには何が出力されるべきですか？

## Quiz Answer

Hello World
