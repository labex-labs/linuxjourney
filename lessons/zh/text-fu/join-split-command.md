---
title: "join 和 split"
description: "学习使用 Linux 的 'join' 和 'split' 命令进行文件操作。了解如何通过共同字段合并文件以及如何高效地拆分大型文件。获取实用示例和技巧。"
keywords: "Linux join 命令，Linux split 命令，文件操作，Linux 教程，命令行，Linux 初学者，Linux 指南"
---

## Lesson Content

`join` 命令允许您通过一个共同的字段将多个文件连接在一起：

假设我有两个文件要连接：

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

看到它是如何连接我的文件的了吗？默认情况下，它们通过第一个字段连接在一起，并且字段必须相同。如果不同，您可以对它们进行排序。在这种情况下，文件通过 1、2、3 连接。

我们将如何连接以下文件？

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

要连接此文件，您需要指定要连接的字段。在这种情况下，我们想要 `file1.txt` 的字段 2 和 `file2.txt` 的字段 1，因此命令将如下所示：

```bash
$ join -1 2 -2 1 file1.txt file2.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

`-1` 指的是 `file1.txt`，`-2` 指的是 `file2.txt`。非常棒。您还可以使用 `split` 命令将文件拆分成不同的文件：

```bash
split somefile
```

这会将其拆分成不同的文件。默认情况下，当文件达到 1000 行限制时，它会进行拆分。默认情况下，文件名为 `x**`。

## Exercise

连接两个行数不同的文件。会发生什么？

## Quiz Question

您会使用什么命令来连接名为 `cat`、`dog`、`cow` 的文件？

## Quiz Answer

join cat dog cow
