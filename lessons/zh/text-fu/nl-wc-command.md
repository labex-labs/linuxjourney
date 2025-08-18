---
lang: "zh"
title: "wc 和 nl"
meta_title: "wc 和 nl - 文本操作"
meta_description: "学习 wc 和 nl Linux 命令。了解字数统计、行编号和文件分析。立即提高您的 Linux 命令行技能！"
meta_keywords: "wc 命令，nl 命令，Linux 字数统计，Linux 行号，文件分析，Linux 教程，Linux 初学者，Linux 指南"
---

## Lesson Content

`wc`（word count，字数统计）命令显示文件中单词的总数。

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

另一个可以用来检查文件中行数的命令是 `nl`（number lines，行号）命令。

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

如何在不搜索整个输出的情况下，使用 `nl` 命令获取总行数？提示：使用您在本课程中学习过的其他一些命令。

## Quiz Question

您会使用什么命令来获取文件中单词的总数，并且只显示单词数？

## Quiz Answer

wc -w
