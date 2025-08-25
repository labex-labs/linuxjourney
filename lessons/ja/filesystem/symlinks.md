---
index: 12
lang: "ja"
title: "シンボリックリンク"
meta_title: "シンボリックリンク - ファイルシステム"
meta_description: "Linux のシンボリックリンクとハードリンクについて、作成方法と管理方法を含めて学びます。この初心者向けのガイドで、それらの違いと使用例を理解しましょう。"
meta_keywords: "Linux シンボリックリンク，ハードリンク，ln コマンド，シンボリックリンク，Linux ファイルシステム，Linux チュートリアル，初心者向け Linux"
---

## Lesson Content

以前の inode 情報の例を使用しましょう。

```plaintext
pete@icebox:~$ ls -li
140 drwxr-xr-x 2 pete pete 6 Jan 20 20:13 Desktop
141 drwxr-xr-x 2 pete pete 6 Jan 20 20:01 Documents
```

`ls`コマンドの 3 番目のフィールドをこれまで無視してきたことにお気づきかもしれません。このフィールドはリンクカウントです。リンクカウントとは、ファイルが持つハードリンクの総数です。現時点では意味がわからないでしょうから、まずリンクについて説明しましょう。

### シンボリックリンク

Windows オペレーティングシステムには、ショートカットと呼ばれるものがあります。ショートカットは、他のファイルへのエイリアスに過ぎません。元のファイルに何か変更を加えると、ショートカットが壊れる可能性があります。Linux では、ショートカットに相当するものがシンボリックリンク（またはソフトリンク、シンリンク）です。シンボリックリンクを使用すると、ファイル名で別のファイルにリンクできます。Linux で見られるもう 1 つの種類のリンクはハードリンクです。これらは実際には、inode へのリンクを持つ別のファイルです。シンボリックリンクから始めて、実際にどういうことか見てみましょう。

```bash
pete@icebox:~/Desktop$ echo 'myfile' > myfile
pete@icebox:~/Desktop$ echo 'myfile2' > myfile2
pete@icebox:~/Desktop$ echo 'myfile3' > myfile3

pete@icebox:~/Desktop$ ln -s myfile myfilelink
pete@icebox:~/Desktop$ ls -li
total 12
  151 -rw-rw-r-- 1 pete pete 7 Jan 21 21:36 myfile
93401 -rw-rw-r-- 1 pete pete 8 Jan 21 21:36 myfile2
93402 -rw-rw-r-- 1 pete pete 8 Jan 21 21:36 myfile3
93403 lrwxrwxrwx 1 pete pete 6 Jan 21 21:39 myfilelink -> myfile
```

`myfile`を指す`myfilelink`というシンボリックリンクを作成したことがわかります。シンボリックリンクは`->`で示されます。ただし、新しい inode 番号を取得したことに注意してください。シンボリックリンクは、ファイル名を指す単なるファイルです。シンボリックリンクを変更すると、ファイルも変更されます。inode 番号はファイルシステムに固有です。単一のファイルシステム内に同じ inode 番号を 2 つ持つことはできません。つまり、別のファイルシステム内のファイルをその inode 番号で参照することはできません。ただし、シンボリックリンクを使用する場合、それらは inode 番号を使用せず、ファイル名を使用するため、異なるファイルシステム間で参照できます。

### ハードリンク

ハードリンクの例を見てみましょう。

```bash
pete@icebox:~/Desktop$ ln myfile2 myhardlink
pete@icebox:~/Desktop$ ls -li
total 16
  151 -rw-rw-r-- 1 pete pete 7 Jan 21 21:36 myfile
93401 -rw-rw-r-- 2 pete pete 8 Jan 21 21:36 myfile2
93402 -rw-rw-r-- 1 pete pete 8 Jan 21 21:36 myfile3
93403 lrwxrwxrwx 1 pete pete 6 Jan 21 21:39 myfilelink -> myfile
93401 -rw-rw-r-- 2 pete pete 8 Jan 21 21:36 myhardlink
```

ハードリンクは、同じ inode へのリンクを持つ別のファイルを作成するだけです。したがって、`myfile2`または`myhardlink`の内容を変更すると、両方に変更が反映されます。しかし、`myfile2`を削除しても、ファイルは`myhardlink`を介してアクセスできます。ここで、`ls`コマンドのリンクカウントが関係してきます。リンクカウントは、inode が持つハードリンクの数です。ファイルを削除すると、そのリンクカウントが減少します。inode は、inode へのすべてのハードリンクが削除された場合にのみ削除されます。ファイルを作成すると、その inode を指す唯一のファイルであるため、リンクカウントは 1 になります。シンボリックリンクとは異なり、ハードリンクは inode がファイルシステムに固有であるため、ファイルシステムをまたがることはありません。

### シンボリックリンクの作成

```bash
ln -s myfile mylink
```

シンボリックリンクを作成するには、`ln`コマンドを`-s`（シンボリック用）とともに使用し、ターゲットファイルとリンク名を指定します。

### ハードリンクの作成

```bash
ln somefile somelink
```

シンボリックリンクの作成と似ていますが、今回は`-s`を省略します。

## Exercise

練習は完璧をもたらします！ファイル管理、リンク、および inode の理解を深めるための実践的なラボをいくつか紹介します。

1. **[Linux でのファイルとディレクトリの管理](https://labex.io/ja/labs/comptia-manage-files-and-directories-in-linux-590835)** - ファイルとディレクトリの作成、コピー、移動、削除を練習し、特にシンボリックリンクとハードリンク、および inode の分析方法について学びます。
2. **[Linux でのファイルシステムのナビゲート](https://labex.io/ja/labs/comptia-navigate-the-filesystem-in-linux-590971)** - `pwd`、`cd`、`ls`などの必須コマンドを習得して、Linux ファイルシステムを効率的に移動します。これは、ファイルとその inode がどこにあるかを理解するための基礎的なスキルです。

これらのラボは、ファイル管理とリンクの概念を実際のシナリオに適用し、Linux ファイルシステムへの自信を築くのに役立ちます。

## Quiz Question

シンボリックリンクを作成するために使用されるコマンドは何ですか？

## Quiz Answer

ln -s
