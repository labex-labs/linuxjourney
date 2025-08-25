---
index: 15
lang: "zh"
title: "wc 和 nl"
meta_title: "wc 和 nl - 文本处理技巧"
meta_description: "学习 wc 和 nl Linux 命令。了解单词计数、行编号和文件分析。立即提高您的 Linux 命令行技能！"
meta_keywords: "wc 命令，nl 命令，Linux 单词计数，Linux 行号，文件分析，Linux 教程，Linux 初学者，Linux 指南"
---

## Lesson Content

`wc`（word count）命令显示文件中单词的总数。

```bash
$ wc /etc/passwd
 96     265    5925 /etc/passwd
```

它分别显示行数、单词数和字节数。

要只查看某个字段的计数，请分别使用 `-l`、`-w` 或 `-c` 选项。

```bash
$ wc -l /etc/passwd
96
```

另一个可以用来检查文件中行数的命令是 `nl`（number lines）命令。

```plaintext
file1.txt
i
like
turtles
```

```bash
$ nl file1.txt
1. i
2. like
3. turtles
```

## Exercise

熟能生巧！这里有一些动手实验，以加强您对 Linux 中文本计数和行编号的理解：

1. **[Linux wc 命令：文本计数](https://labex.io/zh/labs/linux-linux-wc-command-text-counting-219200)** - 练习使用 `wc` 命令计算文本文件中的单词、行和字符。
2. **[Linux nl 命令：行编号](https://labex.io/zh/labs/linux-linux-nl-command-line-numbering-210988)** - 学习使用 `nl` 命令为文本文件编号。
3. **[单词计数和排序](https://labex.io/zh/labs/linux-word-count-and-sorting-388125)** - 应用您对 `wc` 的知识来计数行、单词和字符，并将其与排序结合起来，用于实际的文本分析任务。

这些实验将帮助您在实际场景中应用概念，并增强在 Linux 中处理文本的信心。

## Quiz Question

您会使用什么命令来获取文件中单词的总数，并且只显示单词数？

## Quiz Answer

wc -w
