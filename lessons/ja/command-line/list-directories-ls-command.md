---
lang: "ja"
title: "ls (ディレクトリを一覧表示)"
meta_description: "Linux で「ls」コマンドを使ってディレクトリの内容を一覧表示し、隠しファイルを表示し、ファイルの詳細を理解する方法を学びます。Linux コマンドラインスキルを向上させましょう！"
meta_keywords: "ls コマンド，ディレクトリ一覧，Linux チュートリアル，隠しファイル，Linux コマンド，Linux 初心者，Linux ガイド"
---

## Lesson Content

システム内を移動する方法がわかったところで、何が利用できるかを知るにはどうすればよいでしょうか？今は、暗闇の中を移動しているようなものです。そこで、素晴らしい `ls` コマンドを使ってディレクトリの内容を一覧表示できます。`ls` コマンドは、デフォルトでは現在のディレクトリ内のディレクトリとファイルを一覧表示しますが、ディレクトリを一覧表示したいパスを指定することもできます。

```bash
ls
ls /home/pete
```

`ls` は非常に便利なツールです。また、見ているファイルやディレクトリに関する詳細情報も表示します。

また、ディレクトリ内のすべてのファイルが表示されるわけではないことに注意してください。`.` で始まるファイル名は隠しファイルです。ただし、`ls` コマンドに `-a` フラグ（`a` は all の意味）を渡すことで、それらを表示できます。

```bash
ls -a
```

もう 1 つ便利な `ls` フラグに、`-l`（long の意味）があります。これは、ファイルの詳細なリストを長い形式で表示します。これにより、左から順に、ファイルパーミッション、リンク数、所有者名、所有者グループ、ファイルサイズ、最終変更タイムスタンプ、ファイル/ディレクトリ名といった詳細情報が表示されます。

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

コマンドには、より多くの機能を追加するためのフラグ（または引数、オプションなど、呼び方は何でも構いません）と呼ばれるものがあります。`-a` と `-l` を追加したのを見ましたね。これらは `-la` のように両方を一緒にすることもできます。フラグの順序によって、それが適用される順序が決まります。ほとんどの場合、これはあまり重要ではないので、`ls -al` としても機能します。

```bash
ls -la
```

## Exercise

異なるフラグを付けて `ls` を実行し、受け取る出力を確認してください。

## Quiz Question

隠しファイルを表示するには、どのコマンドを使用しますか？

## Quiz Answer

ls -a
