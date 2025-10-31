---
index: 12
lang: "ja"
title: "シンボリックリンク"
meta_title: "シンボリックリンク - ファイルシステム"
meta_description: "Linux のシンボリックリンク（シンリンク）とハードリンクを探求します。ln コマンドでの作成方法、ls でのリンク数の確認方法、そして ls でのシンボリックリンクとハードリンクの出力の違いを理解しましょう。"
meta_keywords: "Linux シンボリックリンク，ハードリンク，ln コマンド，シンリンク，ls シンボリックリンク，Linux リンク数，ls リンク，Linux ファイルシステム，Linux チュートリアル"
---

## Lesson Content

詳細にファイル一覧を表示すると、多くの情報が表示されます。`ls -li` コマンドによる inode 情報の以前の例を見てみましょう。

```plaintext
pete@icebox:~$ ls -li
140 drwxr-xr-x 2 pete pete 6 Jan 20 20:13 Desktop
141 drwxr-xr-x 2 pete pete 6 Jan 20 20:01 Documents
```

以前、この出力の 3 番目のフィールドは省略していました。このフィールドがリンクカウントです。

### Linux におけるリンクカウント

**Linux におけるリンクカウント**は、ファイルが持つハードリンクの総数です。これが何を意味するかを理解するには、まずリンクとは何かを議論する必要があります。Linux には、シンボリックリンク（symlink）とハードリンクの 2 種類のリンクがあります。

### シンボリックリンクの理解

Windows オペレーティングシステムにはショートカットがありますが、これは基本的に他のファイルを参照するエイリアスです。Linux では、これに相当するものがシンボリックリンク、またはソフトリンク、**symlink** と呼ばれます。シンボリックリンクは、名前によって別のファイルやディレクトリを指す特殊な種類のファイルです。

これを実際に見るために、いくつかのファイルを作成し、その後シンボリックリンクを作成します。

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

ここで、`myfile` を指す `myfilelink` という名前のシンボリックリンクを作成しました。`ls` を使用して `ls symlink` を表示すると、パーミッション文字列の先頭の `l` と、ターゲットを指す `->` 記号によって明確に識別されます。シンボリックリンクは独自の inode 番号 (93403) を持つことに注意してください。シンボリックリンクは inode ではなくファイル名を指すため、異なるファイルシステムをまたぐことができます。

### ハードリンクの理解

もう一方のリンクの種類はハードリンクです。ハードリンクは、元のファイルと同じ inode を直接指す別のファイルエントリを作成します。

`myfile2` のハードリンクを作成してみましょう。

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

`myhardlink` が `myfile2` と全く同じ inode 番号 (93401) を共有していることに注目してください。両方のファイルのリンクカウントも 2 に増加しています。これは、2 つのファイルエントリが同じ inode を指しているためです。`myfile2` の内容を変更すると、その変更は `myhardlink` に反映され、その逆も同様です。`myfile2` を削除しても、リンクカウントがゼロになるまで、そのファイルデータは `myhardlink` を通じてアクセス可能です。ハードリンクは単一のファイルシステム内で一意である inode を指すため、異なるファイルシステムをまたぐことはできません。

### シンボリックリンクとハードリンクの作成

どちらの種類のリンクも `ln` コマンドを使用して作成できます。構文は簡単です。

シンボリックリンクを作成するには、`-s` フラグを使用します。

```bash
ln -s /path/to/original /path/to/link
```

ハードリンクを作成するには、`-s` フラグを省略します。

```bash
ln /path/to/original /path/to/link
```

これらの異なるファイルタイプを管理および識別するには、`ls symlinks` または一般的な `ls links` コマンドに `-l` オプションを付けて使用することが不可欠です。

## Exercise

練習あるのみです！ファイル管理、リンク、inode の理解を深めるための実践的なラボを次に示します。

1. **[Linux でファイルとディレクトリを管理する](https://labex.io/ja/labs/comptia-manage-files-and-directories-in-linux-590835)** - ファイルとディレクトリの作成、コピー、移動、削除を練習し、特にシンボリックリンクとハードリンクについて学び、inode を分析する方法を習得します。
2. **[Linux でファイルシステムをナビゲートする](https://labex.io/ja/labs/comptia-navigate-the-filesystem-in-linux-590971)** - `pwd`、`cd`、`ls` などの必須コマンドを習得し、Linux ファイルシステム内を効率的に移動します。これは、ファイルとその inode がどこにあるかを理解するための基礎的なスキルです。

これらのラボは、ファイル管理とリンクの概念を実際のシナリオで適用し、Linux ファイルシステムに対する自信を築くのに役立ちます。

## Quiz Question

symlink を作成するために使用されるコマンドとその主要なオプションは何ですか？あなたの回答は英語で、大文字と小文字が区別されます。コマンドとオプションの間にはスペースを含めてください。

## Quiz Answer

ln -s
