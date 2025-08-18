---
lang: "ja"
title: "mv (移動)"
meta_description: "Linux の mv コマンドを使ってファイルやディレクトリを移動・名前変更する方法を学びましょう。そのオプションを理解し、上書きを防ぎます。Linux の旅を始めましょう！"
meta_keywords: "mv コマンド，Linux mv, ファイル移動 Linux, ファイル名変更 Linux, Linux チュートリアル，初心者，Linux ガイド"
---

## Lesson Content

ファイルを移動したり、名前を変更したりするために使用されます。フラグや機能の点で `cp` コマンドと非常によく似ています。

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

`cp` と同様に、ファイルまたはディレクトリを `mv` すると、同じディレクトリ内のすべてが上書きされます。そのため、`-i` フラグを使用して、上書きする前にプロンプトを表示させることができます。

```bash
mv -i directory1 directory2
```

ファイルを `mv` して以前のものを上書きしたいとします。そのファイルのバックアップを作成することもでき、古いバージョンは `~` で名前が変更されます。

```bash
mv -b directory1 directory2
```

## Exercise

ファイルの名前を変更し、そのファイルを別のディレクトリに移動します。

## Quiz Question

`cat` という名前のファイルを `dog` に変更するにはどうすればよいですか？

## Quiz Answer

mv cat dog
