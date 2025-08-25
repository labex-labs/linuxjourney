---
index: 12
lang: "zh"
title: "sort"
meta_title: "sort - 文本高手"
meta_description: "学习如何使用 Linux sort 命令对文本文件进行排序。探索反向和数值排序等选项。提高你的 Linux 命令行技能！"
meta_keywords: "Linux sort 命令，sort -r, sort -n, Linux 教程，命令行，Linux 初学者，sort 指南"
---

## Lesson Content

`sort` 命令用于对行进行排序。

```plaintext
file1.txt
dog
cow
cat
elephant
bird

$ sort file1.txt
bird
cat
cow
dog
elephant
```

你也可以进行反向排序：

```bash
$ sort -r file1.txt
elephant
dog
cow
cat
bird
```

也可以按数值排序：

```bash
$ sort -n file1.txt
bird
cat
cow
elephant
dog
```

## Exercise

熟能生巧！这里有一些动手实验，可以帮助你巩固对 `sort` 命令和文本处理的理解：

1. **[Linux sort 命令：文本排序](https://labex.io/zh/labs/linux-linux-sort-command-text-sorting-219196)** - 这个实验直接介绍了 `sort` 命令，让你练习以各种方式（包括升序和降序）对文本文件行进行排序。
2. **[单词计数和排序](https://labex.io/zh/labs/linux-word-count-and-sorting-388125)** - 在这个挑战中，你将运用排序和单词计数的知识来分析文本数据，帮助你找到常见的模式并高效地排序数据。

这些实验将帮助你在实际场景中应用这些概念，并增强在 Linux 中进行文本操作和排序的信心。

## Quiz Question

你使用哪个标志来执行反向排序？

## Quiz Answer

-r
