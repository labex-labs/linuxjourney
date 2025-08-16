---
title: "join と split"
description: "Linux の'join'コマンドと'split'コマンドを使用してファイルを操作する方法を学びます。共通のフィールドでファイルを結合し、大きなファイルを効率的に分割する方法を理解します。実用的な例とヒントを得られます。"
keywords: "Linux join コマンド，Linux split コマンド，ファイル操作，Linux チュートリアル，コマンドライン，初心者 Linux, Linux ガイド"
---

## Lesson Content

`join`コマンドを使用すると、共通のフィールドで複数のファイルを結合できます。

結合したい 2 つのファイルがあるとします。

```plaintext
file1.txt
1 John
2 Jane
3 Mary

file2.txt
1 Doe
2 Doe
3 Sue
```

```bash
$ join file1.txt file2.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

ファイルが結合されたのがわかりますか？デフォルトでは最初のフィールドで結合され、フィールドは同一である必要があります。同一でない場合は、ソートできます。この場合、ファイルは 1、2、3 を介して結合されています。

次のファイルをどのように結合しますか？

```plaintext
file1.txt
John 1
Jane 2
Mary 3

file2.txt
1 Doe
2 Doe
3 Sue
```

このファイルを結合するには、結合するフィールドを指定する必要があります。この場合、`file1.txt`のフィールド 2 と`file2.txt`のフィールド 1 が必要なので、コマンドは次のようになります。

```bash
$ join -1 2 -2 1 file1.txt file2.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

`-1`は`file1.txt`を指し、`-2`は`file2.txt`を指します。かなり便利です。`split`コマンドを使用してファイルを異なるファイルに分割することもできます。

```bash
split somefile
```

これにより、ファイルは異なるファイルに分割されます。デフォルトでは、1000 行の制限に達すると分割されます。ファイルはデフォルトで`x**`という名前になります。

## Exercise

各ファイルで異なる行数の 2 つのファイルを結合します。何が起こりますか？

## Quiz Question

`cat`、`dog`、`cow`という名前のファイルを結合するには、どのコマンドを使用しますか？

## Quiz Answer

join cat dog cow
