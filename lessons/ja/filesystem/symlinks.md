---
title: "シンボリックリンク"
description: "Linux のシンボリックリンクとハードリンクについて、それらの作成方法と管理方法を含めて学びます。初心者向けのこのガイドで、それらの違いと使用例を理解しましょう。"
keywords: "Linux シンボリックリンク，ハードリンク，ln コマンド，シンボリックリンク，Linux ファイルシステム，Linux チュートリアル，初心者向け Linux"
---

## Lesson Content

inode 情報の以前の例を使用してみましょう。

```plaintext
pete@icebox:~$ ls -li
140 drwxr-xr-x 2 pete pete 6 Jan 20 20:13 Desktop
141 drwxr-xr-x 2 pete pete 6 Jan 20 20:01 Documents
```

`ls`コマンドの 3 番目のフィールドを見過ごしてきたことにお気づきかもしれません。このフィールドはリンクカウントです。リンクカウントとは、ファイルが持つハードリンクの総数です。現時点ではこれは意味をなさないので、まずリンクについて説明しましょう。

### Symlinks

Windows オペレーティングシステムには、ショートカットと呼ばれるものがあります。ショートカットは、他のファイルへのエイリアスに過ぎません。元のファイルに何かを行うと、ショートカットが壊れる可能性があります。Linux では、ショートカットに相当するものがシンボリックリンク（またはソフトリンク、symlinks）です。シンボリックリンクを使用すると、ファイル名によって別のファイルにリンクできます。Linux で見られるもう 1 つの種類のリンクはハードリンクです。これらは実際には inode へのリンクを持つ別のファイルです。シンボリックリンクから始めて、実際に何を意味するのか見てみましょう。

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

`myfile`を指す`myfilelink`というシンボリックリンクを作成したことがわかります。シンボリックリンクは`->`で示されます。ただし、新しい inode 番号を取得したことに注目してください。シンボリックリンクは、ファイル名を指す単なるファイルです。シンボリックリンクを変更すると、ファイルも変更されます。inode 番号はファイルシステムに固有です。単一のファイルシステム内に同じ inode 番号を 2 つ持つことはできません。つまり、異なるファイルシステム内のファイルをその inode 番号で参照することはできません。ただし、シンボリックリンクを使用する場合、それらは inode 番号を使用せず、ファイル名を使用するため、異なるファイルシステム間で参照できます。

### Hardlinks

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

ハードリンクは、同じ inode へのリンクを持つ別のファイルを作成するだけです。したがって、`myfile2`または`myhardlink`の内容を変更した場合、その変更は両方で確認できます。しかし、`myfile2`を削除しても、ファイルは`myhardlink`を介して引き続きアクセスできます。ここで、`ls`コマンドのリンクカウントが関係してきます。リンクカウントは、inode が持つハードリンクの数です。ファイルを削除すると、そのリンクカウントが減少します。inode は、inode へのすべてのハードリンクが削除された場合にのみ削除されます。ファイルを作成すると、そのリンクカウントは 1 になります。なぜなら、その inode を指すファイルはそれだけだからです。シンボリックリンクとは異なり、ハードリンクは inode がファイルシステムに固有であるため、ファイルシステムをまたがることはありません。

### Creating a symlink

```bash
ln -s myfile mylink
```

シンボリックリンクを作成するには、`ln`コマンドを`-s`（シンボリック用）とともに使用し、ターゲットファイルとリンク名を指定します。

### Creating a hardlink

```bash
ln somefile somelink
```

シンボリックリンクの作成と似ていますが、今回は`-s`を省略します。

## Exercise

シンボリックリンクとハードリンクを作成して試してみてください。いくつか削除して、何が起こるか見てみましょう。

## Quiz Question

シンボリックリンクを作成するために使用されるコマンドは何ですか？

## Quiz Answer

ln -s
