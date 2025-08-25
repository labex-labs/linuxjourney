---
index: 11
lang: "ja"
title: "mv (移動)"
meta_title: "mv (移動) - コマンドライン"
meta_description: "Linux の mv コマンドを使ってファイルやディレクトリを移動・名前変更する方法を学びましょう。そのオプションを理解し、上書きを防ぎましょう。Linux の旅を始めましょう！"
meta_keywords: "mv コマンド，Linux mv, ファイル移動 Linux, ファイル名変更 Linux, Linux チュートリアル，初心者，Linux ガイド"
---

## Lesson Content

ファイルを移動したり、名前を変更したりするために使用されます。フラグと機能の点で `cp` コマンドと非常によく似ています。

ファイルの名前は次のように変更できます。

```bash
mv oldfile newfile
```

または、実際にファイルを別のディレクトリに移動することもできます。

```bash
mv file2 /home/pete/Documents
```

そして、複数のファイルを移動します。

```bash
mv file_1 file_2 /somedirectory
```

ディレクトリの名前も変更できます。

```bash
mv directory1 directory2
```

`cp` と同様に、ファイルまたはディレクトリを `mv` すると、同じディレクトリ内のすべてが上書きされます。そのため、上書きする前にプロンプトを表示するには、`-i` フラグを使用できます。

```bash
mv -i directory1 directory2
```

ファイルを `mv` して以前のファイルを上書きしたいとします。そのファイルのバックアップを作成することもでき、古いバージョンは `~` で名前が変更されます。

```bash
mv -b directory1 directory2
```

## Exercise

練習は完璧をもたらします！ `mv` のような Linux コマンドを習得するには、実践的な経験が不可欠です。これらのラボは、実際の環境でファイルやディレクトリを移動および名前変更する理解を深めるのに役立ちます。

1. **[Linux mv コマンド：ファイルの移動と名前変更](https://labex.io/ja/labs/linux-linux-mv-command-file-moving-and-renaming-209743)** - `mv` コマンドを使用してファイルやディレクトリを移動および名前変更する練習をします。これには、さまざまなオプションと動作の理解も含まれます。
2. **[ファイルの整理とディレクトリ](https://labex.io/ja/labs/linux-organizing-files-and-directories-387877)** - `mv`（`cp` および `rm` とともに）の知識を実用的な課題に適用して、プロジェクト構造を整理し、ファイルを移動し、ディレクトリをクリーンアップします。

これらのラボは、実際のシナリオで概念を適用し、`mv` コマンドを使用したファイルおよびディレクトリ管理に自信を築くのに役立ちます。

## Quiz Question

`cat` という名前のファイルを `dog` に名前変更するにはどうすればよいですか？

## Quiz Answer

mv cat dog
