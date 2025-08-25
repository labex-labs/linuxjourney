---
index: 6
lang: "zh"
title: "cut"
meta_title: "cut - 文本处理"
meta_description: "学习如何使用 Linux `cut` 命令从文件中提取文本。这个适合初学者的教程涵盖了字符和字段剪切。提高您的 Linux 文本处理技能！"
meta_keywords: "cut 命令，Linux 文本处理，提取文本，Linux 教程，Linux 初学者，cut 示例，Linux 指南"
---

## Lesson Content

我们将学习几个可以用来处理文本的有用命令。在开始之前，让我们创建一个将要使用的文件。复制并粘贴以下命令；完成后，在“lazy”和“dog”之间添加一个 TAB 键（按住 Ctrl-v + TAB）。

```bash
echo 'The quick brown; fox jumps over the lazy  dog' > sample.txt
```

我们将学习的第一个命令是 `cut` 命令。它从文件中提取部分文本。

按字符列表提取内容：

```bash
cut -c 5 sample.txt
```

这将输出文件中每一行的第 5 个字符。在本例中，它是“q”；请注意，空格也算作一个字符。

要按字段提取内容，我们需要做一些修改：

```bash
cut -f 2 sample.txt
```

`-f` 或字段标志根据字段剪切文本。默认情况下，它使用 TAB 作为分隔符，因此由 TAB 分隔的所有内容都被视为一个字段。您应该会看到“dog”作为输出。

您可以将字段标志与分隔符标志结合使用，以自定义分隔符提取内容：

```bash
cut -f 1 -d ";" sample.txt
```

这将把 TAB 分隔符更改为“;”分隔符，由于我们剪切的是第一个字段，结果应该是“The quick brown”。

## Exercise

熟能生巧！这里有一些动手实验，以加强您对使用 `cut` 和其他相关命令进行文本处理的理解：

1. **[Linux cut 命令：文本剪切](https://labex.io/zh/labs/linux-linux-cut-command-text-cutting-219187)** - 本实验直接动手介绍了 `cut` 命令，让您练习从文本文件中提取特定列或字段，正如课程中讨论的那样。
2. **[简单文本处理](https://labex.io/zh/labs/linux-simple-text-processing-18004)** - 通过使用 `tr`、`col`、`join` 和 `paste` 等强大命令，扩展您的文本操作技能，以高效地处理和分析文本数据。
3. **[序列控制和管道](https://labex.io/zh/labs/linux-sequence-control-and-pipeline-17994)** - 通过学习控制命令执行序列、利用管道以及利用 `cut`、`grep`、`wc`、`sort` 和 `uniq` 等强大的文本处理工具，提高您的命令行效率。

这些实验将帮助您在实际场景中应用这些概念，并增强在 Linux 中进行文本处理的信心。

## Quiz Question

您会使用什么命令来获取文件中每一行的第一个字符？

## Quiz Answer

cut -c 1
