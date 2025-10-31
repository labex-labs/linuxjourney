---
index: 11
lang: "zh"
title: "连接与分割"
meta_title: "连接与分割 - Text-Fu"
meta_description: "掌握如何使用 Linux 的 join 和 split 命令。学习如何根据共同的字段高效地连接文件，以及将大文件分割成更小的部分。本指南涵盖了用于连接名为 cat、dog、cow 的文件以及其他实用示例的命令。"
meta_keywords: "linux 连接文件，用于连接文件的命令是什么，linux join 命令，linux split 命令，文件操作，命令行，文本处理"
---

## Lesson Content

在 Linux 中，管理和操作文本文件是一项常见任务。两个强大的实用工具是 `join` 和 `split`。`join` 命令根据共同的字段合并两个文件的行，而 `split` 将大文件分解成更小、更易于管理的部分。

### 按共同字段连接文件

当你需要 **linux join files** 时，`join` 命令是一个基本工具。默认情况下，它根据第一个相同的字段合并两个已排序文件的行。

例如，想象你有两个想要合并的文件：

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

使用 `join` 命令，你可以轻松地将它们组合起来：

```bash
$ join file1.txt file2.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

正如你所见，文件是根据第一个共同字段（1、2、3）连接起来的。为了让 `join` 正确工作，两个文件中的连接字段必须是已排序的。

### 指定不同的连接字段

如果共同字段不是第一列怎么办？你可以告诉 `join` 使用哪些字段。考虑以下文件：

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

在这里，我们需要根据 `file1.txt` 的第二个字段和 `file2.txt` 的第一个字段进行连接。命令将是：

```bash
$ join -1 2 -2 1 file1.txt file2.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

`-1 2` 标志指定第一个文件的第 2 个字段，`-2 1` 标志指定第二个文件的第 1 个字段。

### 分割大文件

`split` 命令与连接相反；它将大文件分成更小的文件。

```bash
$ split somefile
```

默认情况下，此命令在达到 1000 行限制时将 `somefile` 分割成新文件。输出文件命名为 `xaa`、`xab`，依此类推。你可以通过使用 `-l` 标志指定不同的行数或使用 `-b` 标志按文件大小分割来定制此行为。

## Exercise

实践造就完美！这里有一些动手实验，以加强你对连接和操作文本文件的理解：

1. **[Linux join 命令：文件连接](https://labex.io/zh/labs/linux-linux-join-command-file-joining-219193)** - 此实验提供了对 `join` 命令的直接、动手介绍，允许你练习根据共同字段合并两个已排序文本文件的行，就像课程中所讨论的那样。
2. **[处理员工数据](https://labex.io/zh/labs/linux-processing-employees-data-388132)** - 应用你对 `join` 和其他强大的 Linux 命令行实用程序（如 `awk`）的知识，以组合和处理来自多个源的数据，模拟现实世界的数据分析场景。
3. **[序列控制和管道](https://labex.io/zh/labs/linux-sequence-control-and-pipeline-17994)** - 通过学习控制命令执行序列、利用管道以及利用强大的文本处理工具来增强你的命令行效率和数据操作技能，这补充了 `join` 的数据组合功能。

这些实验将帮助你将文本文件操作和数据组合的概念应用于实际场景，并建立对 Linux 命令行工具的信心。

## Quiz Question

你会使用什么命令来连接名为 `cat`、`dog`、`cow` 的文件？请用英文提供完整的命令。命令和文件名应为小写。

## Quiz Answer

join cat dog cow
