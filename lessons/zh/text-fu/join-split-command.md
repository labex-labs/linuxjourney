---
index: 11
lang: "zh"
title: "join 和 split"
meta_title: "join 和 split - 文本处理"
meta_description: "学习使用 Linux 'join' 和 'split' 命令进行文件操作。了解如何通过公共字段组合文件以及高效地拆分大文件。获取实用示例和技巧。"
meta_keywords: "Linux join 命令，Linux split 命令，文件操作，Linux 教程，命令行，Linux 初学者，Linux 指南"
---

## Lesson Content

`join` 命令允许您通过一个公共字段将多个文件连接在一起：

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

看到它是如何连接我的文件的吗？它们默认通过第一个字段连接在一起，并且这些字段必须相同。如果不同，您可以对它们进行排序。在这种情况下，文件通过 1、2、3 连接。

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

要连接此文件，您需要指定要连接的字段。在这种情况下，我们想要 `file1.txt` 上的字段 2 和 `file2.txt` 上的字段 1，因此命令将如下所示：

```bash
$ join -1 2 -2 1 file1.txt file2.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

`-1` 指的是 `file1.txt`，`-2` 指的是 `file2.txt`。非常棒。您还可以使用 `split` 命令将文件拆分为不同的文件：

```bash
split somefile
```

这将把它拆分成不同的文件。默认情况下，它会在达到 1000 行限制时进行拆分。文件默认命名为 `x**`。

## Exercise

熟能生巧！这里有一些动手实验来巩固您对连接和操作文本文件的理解：

1. **[Linux join 命令：文件连接](https://labex.io/zh/labs/linux-linux-join-command-file-joining-219193)** - 本实验直接、动手地介绍了 `join` 命令，让您练习根据共同字段合并两个已排序文本文件中的行，正如课程中讨论的那样。
2. **[处理员工数据](https://labex.io/zh/labs/linux-processing-employees-data-388132)** - 运用您对 `join` 和其他强大的 Linux 命令行实用程序（如 `awk`）的知识，结合和处理来自多个来源的数据，模拟真实的 数据分析场景。
3. **[序列控制和管道](https://labex.io/zh/labs/linux-sequence-control-and-pipeline-17994)** - 通过学习控制命令执行序列、利用管道和利用强大的文本处理工具来提高您的命令行效率和数据操作技能，这补充了 `join` 的数据组合能力。

这些实验将帮助您在实际场景中应用文本文件操作和数据组合的概念，并增强您使用 Linux 命令行工具的信心。

## Quiz Question

您将使用什么命令来连接名为 `cat`、`dog`、`cow` 的文件？

## Quiz Answer

join cat dog cow
