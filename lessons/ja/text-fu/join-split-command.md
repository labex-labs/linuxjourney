---
index: 11
lang: "ja"
title: "join と split"
meta_title: "join と split - テキスト操作"
meta_description: "Linux の'join'コマンドと'split'コマンドを使ってファイルを操作する方法を学びましょう。共通のフィールドでファイルを結合したり、大きなファイルを効率的に分割したりする方法を理解します。実践的な例とヒントを得られます。"
meta_keywords: "Linux join コマンド，Linux split コマンド，ファイル操作，Linux チュートリアル，コマンドライン，初心者 Linux, Linux ガイド"
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

`-1`は`file1.txt`を指し、`-2`は`file2.txt`を指します。とても便利ですね。`split`コマンドを使ってファイルを分割することもできます。

```bash
split somefile
```

これにより、ファイルが分割されます。デフォルトでは、1000 行の制限に達すると分割されます。ファイルはデフォルトで`x**`という名前になります。

## Exercise

練習は完璧をもたらします！テキストファイルの結合と操作の理解を深めるための実践的な演習をいくつか紹介します。

1. **[Linux join Command: File Joining](https://labex.io/ja/labs/linux-linux-join-command-file-joining-219193)** - この演習では、`join`コマンドの直接的で実践的な入門を提供し、レッスンで説明したように、共通のフィールドに基づいて 2 つのソートされたテキストファイルから行をマージする練習ができます。
2. **[Processing Employees Data](https://labex.io/ja/labs/linux-processing-employees-data-388132)** - `join`や`awk`のような強力な Linux コマンドラインユーティリティの知識を適用して、複数のソースからのデータを結合および処理し、実際のデータ分析シナリオをシミュレートします。
3. **[Sequence Control and Pipeline](https://labex.io/ja/labs/linux-sequence-control-and-pipeline-17994)** - コマンド実行シーケンスを制御し、パイプラインを利用し、強力なテキスト処理ツールを活用する方法を学ぶことで、コマンドラインの効率とデータ操作スキルを向上させます。これは、`join`のデータ結合機能を補完します。

これらの演習は、テキストファイルの操作とデータ結合の概念を実際のシナリオに適用し、Linux コマンドラインツールに自信を持つのに役立ちます。

## Quiz Question

`cat`、`dog`、`cow`という名前のファイルを結合するために使用するコマンドは何ですか？

## Quiz Answer

join cat dog cow
