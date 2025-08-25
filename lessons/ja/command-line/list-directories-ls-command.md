---
index: 4
lang: "ja"
title: "ls (ディレクトリ一覧)"
meta_title: "ls (ディレクトリ一覧) - コマンドライン"
meta_description: "Linux で`ls`コマンドを使ってディレクトリの内容を一覧表示し、隠しファイルを表示し、ファイルの詳細を理解する方法を学びましょう。Linux コマンドラインスキルを向上させましょう！"
meta_keywords: "ls コマンド，ディレクトリ一覧，Linux チュートリアル，隠しファイル，Linux コマンド，初心者 Linux, Linux ガイド"
---

## Lesson Content

システム内を移動する方法がわかったところで、何が利用できるかを知るにはどうすればよいでしょうか？今のところ、暗闇の中を移動しているようなものです。そこで、素晴らしい `ls` コマンドを使ってディレクトリの内容を一覧表示できます。`ls` コマンドは、デフォルトでは現在のディレクトリ内のディレクトリとファイルを一覧表示しますが、ディレクトリを一覧表示したいパスを指定することもできます。

```bash
ls
ls /home/pete
```

`ls` は非常に便利なツールで、見ているファイルやディレクトリに関する詳細情報も表示します。

また、ディレクトリ内のすべてのファイルが表示されるわけではないことに注意してください。`.` で始まるファイル名は隠しファイルです。ただし、`ls` コマンドに `-a` フラグ（`a` は all の意味）を渡すことで表示できます。

```bash
ls -a
```

もう 1 つ便利な `ls` フラグに、`-l`（long の意味）があります。これは、ファイルの詳細なリストを長い形式で表示します。これにより、左から順に、ファイル権限、リンク数、所有者名、所有者グループ、ファイルサイズ、最終変更日時、ファイル/ディレクトリ名といった詳細情報が表示されます。

```bash
ls -l
```

```plaintext
pete@icebox:~$ ls -l
total 80
drwxr-x--- 7 pete penguingroup   4096 Nov 20 16:37 Desktop
drwxr-x--- 2 pete penguingroup   4096 Oct 19 10:46  Documents
drwxr-x--- 4 pete penguingroup   4096 Nov 20 09:30 Downloads
drwxr-x--- 2 pete penguingroup   4096 Oct  7 13:13   Music
drwxr-x--- 2 pete penguingroup   4096 Sep 21 14:02 Pictures
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Public
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Templates
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Videos
```

コマンドには、機能を追加するためのフラグ（引数やオプションなど、呼び方は何でも構いません）があります。`-a` と `-l` を追加したのと同じように、これらを `-la` でまとめて追加できます。フラグの順序によって、それが適用される順序が決まります。ほとんどの場合、これはあまり重要ではないため、`ls -al` としても機能します。

```bash
ls -la
```

## Exercise

練習は完璧をもたらします！ここでは、`ls` コマンドの理解を深めるための実践的な演習をご紹介します。

- **[Linux ls コマンド：コンテンツのリスト表示](https://labex.io/ja/labs/linux-linux-ls-command-content-listing-219205)** - `ls` コマンドを使用して、ファイルとディレクトリの内容を効率的にリスト表示し、分析する練習をします。詳細なリスト表示、隠しファイルの表示、人間が読みやすいサイズの表示、ソート技術など、さまざまなオプションを学び、コマンドラインスキルを向上させます。

この演習は、実際のシナリオで概念を適用し、Linux でのディレクトリリスト表示に自信を持つのに役立ちます。

## Quiz Question

隠しファイルを表示するために使用するコマンドは何ですか？

## Quiz Answer

ls -a
