---
index: 14
lang: "zh"
title: "uniq (唯一)"
meta_title: "uniq (唯一) - 文本处理技巧"
meta_description: "了解如何使用 Linux `uniq` 命令从文本文件中删除重复行。探索 -c、-u、-d 等选项，并结合 `sort` 进行有效的数据清理。"
meta_keywords: "uniq 命令，Linux uniq, 删除重复项，sort uniq, Linux 教程，文本处理，Linux 初学者，Linux 指南"
---

## Lesson Content

`uniq`（unique）命令是另一个用于解析文本的有用工具。

假设你有一个包含许多重复内容的文本文件：

```plaintext
reading.txt
book
book
paper
paper
article
article
magazine
```

如果你想删除重复项，可以使用 `uniq` 命令：

```bash
$ uniq reading.txt
book
paper
article
magazine
```

让我们获取每行出现的次数：

```bash
$ uniq -c reading.txt
2 book
2 paper
2 article
1 magazine
```

让我们只获取唯一值：

```bash
$ uniq -u reading.txt
magazine
```

让我们只获取重复值：

```bash
$ uniq -d reading.txt
book
paper
article
```

**注意**：`uniq` 只有在重复行相邻时才能检测到它们。例如：

假设你有一个文件，其中包含不相邻的重复项：

```plaintext
reading.txt
book
paper
book
paper
article
magazine
article
```

```bash
$ uniq reading.txt
reading.txt
book
paper
book
paper
article
magazine
article
```

`uniq` 返回的结果将包含所有条目，与第一个示例不同。

为了克服 `uniq` 的这个限制，我们可以将 `sort` 与 `uniq` 结合使用：

```bash
$ sort reading.txt | uniq
article
book
magazine
paper
```

## Exercise

熟能生巧！这里有一些动手实验，可以帮助你巩固对使用 `uniq` 和 `sort` 进行文本处理的理解：

1. **[Linux uniq 命令：重复项过滤](https://labex.io/zh/labs/linux-linux-uniq-command-duplicate-filtering-219199)** - 学习如何结合使用 Linux `uniq` 命令和 `sort` 来识别、过滤和分析文本文件中的重复行。
2. **[Linux sort 命令：文本排序](https://labex.io/zh/labs/linux-linux-sort-command-text-sorting-219196)** - 练习使用 `sort` 命令来组织文本文件行，这是有效使用 `uniq` 之前的关键步骤。
3. **[字数统计和排序](https://labex.io/zh/labs/linux-word-count-and-sorting-388125)** - 在这个动手挑战中学习基本的 Linux 文本处理工具 `wc`（字数统计）和 `sort`。学习统计行、单词和字符，查找常见模式，并高效地排序数据以完成各种文本分析任务。

这些实验将帮助你在实际场景中应用这些概念，并增强在 Linux 中进行文本处理和数据操作的信心。

## Quiz Question

你会使用什么命令来删除文件中的重复项？

## Quiz Answer

uniq
