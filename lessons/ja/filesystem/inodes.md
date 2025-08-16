---
title: "Inodes"
description: "Linux の inode、その構造、およびファイル管理方法について学びます。inode 番号を理解し、`df -i`と`ls -li`を使用して inode の使用状況を確認します。Linux の学習を始めましょう！"
keywords: "Linux inode, inode チュートリアル，df -i, ls -li, Linux ファイルシステム，Linux 初心者，Linux ガイド"
---

## Lesson Content

ファイルシステムが、実際のすべてのファイルと、これらのファイルを管理するデータベースで構成されていることを覚えていますか？このデータベースは inode テーブルとして知られています。

### inode とは？

inode（index node）は、このテーブル内のエントリであり、すべてのファイルに対して 1 つ存在します。これは、ファイルに関するすべてを記述します。例えば、以下のような情報です。

- File type - regular file, directory, character device, etc.
- Owner
- Group
- Access permissions
- Timestamps - mtime (time of last file modification), ctime (time of last attribute change), atime (time of last access)
- Number of hardlinks to the file
- Size of the file
- Number of blocks allocated to the file
- Pointers to the data blocks of the file - most important!

基本的に、inode はファイル名とファイル自体を除く、ファイルに関するすべてを保存します！

### inode はいつ作成されますか？

ファイルシステムが作成されると、inode のためのスペースも割り当てられます。アルゴリズムは、ディスクの容量などに応じて、必要な inode スペースの量を決定します。おそらく人生のどこかで、ディスク容量不足のエラーを見たことがあるでしょう。inode についても同様のことが起こり得ます（ただし、より一般的ではありません）。inode が不足し、それ以上ファイルを作成できなくなることがあります。データストレージは、データとデータベース（inode）の両方に依存することを覚えておいてください。

システムに残っている inode の数を確認するには、`df -i`コマンドを使用します。

### Inode information

inode は番号で識別されます。ファイルが作成されると、inode 番号が割り当てられ、その番号は連番で割り当てられます。ただし、新しいファイルを作成したときに、他のファイルよりも小さい inode 番号が割り当てられることに気づくことがあります。これは、inode が削除されると、他のファイルによって再利用される可能性があるためです。inode 番号を表示するには、`ls -li`を実行します。

```bash
pete@icebox:~$ ls -li
140 drwxr-xr-x 2 pete pete 6 Jan 20 20:13 Desktop
141 drwxr-xr-x 2 pete pete 6 Jan 20 20:01 Documents
```

このコマンドの最初のフィールドは、inode 番号をリストします。

`stat`コマンドを使用すると、ファイルに関する詳細情報も確認できます。これも inode に関する情報を提供します。

```bash
pete@icebox:~$ stat ~/Desktop/
  File: ‘/home/pete/Desktop/’
  Size: 6               Blocks: 0          IO Block: 4096   directory
Device: 806h/2054d      Inode: 140         Links: 2
Access: (0755/drwxr-xr-x)  Uid: ( 1000/   pete)   Gid: ( 1000/   pete)
Access: 2016-01-20 20:13:50.647435982 -0800
Modify: 2016-01-20 20:13:06.191675843 -0800
Change: 2016-01-20 20:13:06.191675843 -0800
 Birth: -
```

### inode はどのようにファイルを特定しますか？

データはディスク上のどこかに存在することはわかっています。残念ながら、データは連続して保存されていない可能性が高いため、inode を使用する必要があります。inode は、ファイルの実際のデータブロックを指します。一般的なファイルシステム（すべてが同じように機能するわけではありません）では、各 inode に 15 個のポインタが含まれています。最初の 12 個のポインタはデータブロックを直接指します。13 番目のポインタは、さらに多くのブロックへのポインタを含むブロックを指し、14 番目のポインタは別のネストされたポインタブロックを指し、15 番目のポインタはさらに別のポインタブロックを指します！混乱しますよね！これがこのように行われる理由は、すべての inode で inode 構造を同じに保ちながら、異なるサイズのファイルを参照できるようにするためです。小さなファイルであれば、最初の 12 個の直接ポインタでより早く見つけることができます。大きなファイルは、ポインタのネストを使用して見つけることができます。いずれにしても、inode の構造は同じです。

## Exercise

異なるファイルの inode 番号を観察してください。通常、最初に作成されるのはどれですか？

## Quiz Question

システムに残っている inode の数を確認するにはどうすればよいですか？

## Quiz Answer

df -i
