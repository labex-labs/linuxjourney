---
index: 14
lang: "zh"
title: "uniq (唯一)"
meta_title: "uniq (唯一) - 文本工具"
meta_description: "探索 Linux 中的 uniq 命令，用于过滤和删除文本中相邻的重复行。了解如何使用 uniq linux 工具及其选项，如 -c、-u、-d，并将其与 sort 结合以进行强大的文本处理。"
meta_keywords: "uniq 命令，Linux uniq, uniq linux, 删除重复项，sort uniq, 文本处理，数据清洗，Linux 教程"
---

## Lesson Content

`uniq`（unique，唯一）命令是 Linux 文本处理中的一个基本工具。它能帮助您过滤和管理文本文件中重复的行，但要有效使用它，了解其工作原理至关重要。

### 基本的重复行删除

`uniq` 命令的主要功能是删除相邻的重复行。想象您有一个名为 `reading.txt` 的文件，内容如下：

```plaintext
book
book
paper
paper
article
article
magazine
```

要删除重复的行，您可以运行 `uniq` 命令：

```bash
$ uniq reading.txt
book
paper
article
magazine
```

正如您所见，`uniq` 输出的是删除了相邻重复行后的文件版本。

### 高级过滤选项

`uniq` 命令还提供了一些选项，用于更详细的分析。

要计算每行出现的次数，请使用 `-c`（count，计数）标志：

```bash
$ uniq -c reading.txt
      2 book
      2 paper
      2 article
      1 magazine
```

要仅显示不重复的行（即唯一的行），请使用 `-u`（unique，唯一）标志：

```bash
$ uniq -u reading.txt
magazine
```

相反，要仅显示重复的行，请使用 `-d`（duplicated，重复）标志：

```bash
$ uniq -d reading.txt
book
paper
article
```

### 排序的重要性

关于 **uniq linux** 命令的一个关键细节是，它只检测相邻的重复行。如果重复项分散在文件的不同位置，`uniq` 将无法识别它们。

考虑 `reading.txt` 的这个版本，其中重复项不相邻：

```plaintext
book
paper
book
paper
article
magazine
article
```

对该文件运行 `uniq` 会产生一个令人惊讶的结果：

```bash
$ uniq reading.txt
book
paper
book
paper
article
magazine
article
```

没有行被删除，因为没有两行完全相同的行是相邻的。要解决这个问题，您必须首先对文件的内容进行排序。通过将 `sort` 的输出通过管道传输到 `uniq`，可以确保所有相同的行都相邻，从而使 `uniq` 能够正确工作。这种组合是 shell 脚本中强大且常见的模式。

```bash
$ sort reading.txt | uniq
article
book
magazine
paper
```

此命令首先按字母顺序对行进行排序，然后 `uniq` 过滤掉重复项，为您提供一个干净的唯一条目列表。

## Exercise

实践造就完美！以下是一些实践实验，可帮助您巩固对使用 `uniq` 和 `sort` 进行文本处理的理解：

1. **[Linux uniq 命令：重复行过滤](https://labex.io/zh/labs/linux-linux-uniq-command-duplicate-filtering-219199)** - 学习如何将 Linux `uniq` 命令与 `sort` 结合使用，以识别、过滤和分析文本文件中的重复行。
2. **[Linux sort 命令：文本排序](https://labex.io/zh/labs/linux-linux-sort-command-text-sorting-219196)** - 练习使用 `sort` 命令来组织文本文件的行，这是有效使用 `uniq` 的关键步骤。
3. **[词频统计与排序](https://labex.io/zh/labs/linux-word-count-and-sorting-388125)** - 在这个实践挑战中，学习基本的 Linux 文本处理工具 `wc`（词频统计）和 `sort`。学习如何计算行数、单词数和字符数，查找常见模式，并有效地对数据进行排序以完成各种文本分析任务。

这些实验将帮助您在实际场景中应用这些概念，并增强您在 Linux 中进行文本处理和数据操作的信心。

## Quiz Question

您会使用什么命令来删除文件中相邻的重复行？请仅用小写英文字母回答命令名称。

## Quiz Answer

uniq
