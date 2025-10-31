---
index: 15
lang: "zh"
title: "wc 和 nl 命令"
meta_title: "wc 和 nl 命令 - Text-Fu"
meta_description: "在此 Linux 教程中掌握 wc 和 nl 命令。学习如何执行 Linux 单词计数、为文件添加行号以及进行基本的文件分析。一份完美的初学者指南，可提升您的命令行技能。"
meta_keywords: "wc 命令，nl 命令，Linux 单词计数，Linux 文件中计数单词，Linux 行号，nl 命令 Linux, 文件分析，Linux 文本处理，Linux 命令行，Linux 初学者教程"
---

## Lesson Content

在 Linux 中，分析文本文件是一项常见任务。用于此目的的两个基本实用程序是 `wc` 和 `nl`，它们分别帮助您计算内容和编号行。

### 使用 wc 命令进行计数

`wc`（word count，字数统计）命令是一个强大的基本文件分析工具。在文件上运行时，它会提供其内容的摘要。

```bash
$ wc /etc/passwd
 96     265    5925 /etc/passwd
```

输出显示三个数字，后跟文件名。从左到右，这些数字代表：

1.  行数。
2.  单词数（Linux 字数统计）。
3.  字节数。

### 获取特定计数

通常，您只需要一个信息片段。您可以使用选项来显示特定的计数，而不是全部三个。

- `-l`：仅显示行数。
- `-w`：仅显示单词数。
- `-c`：仅显示字节数。

例如，要仅查看 `/etc/passwd` 文件中的行数，您可以使用：

```bash
$ wc -l /etc/passwd
96
```

### 使用 nl 命令对行进行编号

检查文件的另一个有用命令是 `nl` (number lines，行编号)。顾名思义，它会读取文件并输出其内容，在每行开头添加行号。这对于查看脚本或配置文件特别有帮助。

考虑一个名为 `file1.txt` 的文件，内容如下：

```plaintext
i
like
turtles
```

使用 `nl` 命令，您可以轻松添加 Linux 行号：

```bash
$ nl file1.txt
     1	i
     2	like
     3	turtles
```

`wc` 和 `nl` 都是日常 Linux 命令行文本处理中的基本命令。

## Exercise

为了掌握这些命令，动手实践是关键。尝试这些练习，以巩固您在 Linux 上进行文本计数和行编号的技能：

1.  **[Linux wc 命令：文本计数](https://labex.io/zh/labs/linux-linux-wc-command-text-counting-219200)** - 练习使用 `wc` 命令统计文本文件中的单词、行和字符数。
2.  **[Linux nl 命令：行编号](https://labex.io/zh/labs/linux-linux-nl-command-line-numbering-210988)** - 学习使用 `nl` 命令为文本文件中的行添加编号。
3.  **[字数统计与排序](https://labex.io/zh/labs/linux-word-count-and-sorting-388125)** - 应用您对 `wc` 的知识来计算行数、单词数和字符数，并将其与排序结合起来进行实用的文本分析任务。

这些实验将帮助您在现实场景中应用这些概念，并增强您对 Linux 文本处理的信心。

## Quiz Question

您将使用哪个命令和选项来仅显示文件的总单词数？请仅使用命令及其选项（英文）回答。答案区分大小写。

## Quiz Answer

wc -w
