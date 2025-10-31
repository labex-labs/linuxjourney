---
index: 6
lang: "zh"
title: "剪切"
meta_title: "cut 命令 - 文本处理工具"
meta_description: "学习如何使用 Linux `cut` 命令从文件中提取特定文本部分。本指南涵盖按字符和字段（`cut f`）进行剪切，包括如何使用自定义分隔符进行字段剪切。是掌握 Linux 文本处理的理想选择。"
meta_keywords: "cut 命令，Linux 文本处理，提取文本，cut f, 如何使用 cut f, Linux 教程，cut 示例，Linux 指南，字段剪切"
---

## Lesson Content

我们将学习几个用于处理文本的有用命令。在开始之前，让我们创建一个用于操作的文件。复制并粘贴以下命令。粘贴后，您需要在 "lazy" 和 "dog" 之间添加一个字面上的 TAB 字符（您通常可以通过按 Ctrl-v 然后按 TAB 来实现）。

```bash
echo 'The quick brown; fox jumps over the lazy  dog' > sample.txt
```

我们首先探索的命令是 `cut`，它用于从文件中提取文本部分。

### 按字符切割

您可以使用 `-c` 标志根据字符位置提取内容。

```bash
cut -c 5 sample.txt
```

此命令输出文件中每行的第 5 个字符。在我们的例子中，输出是 "q"。请注意，空格也算作字符。

### 使用 cut f 按字段切割

一个更强大的功能是按字段切割。`cut f` 语法使用 `-f` 标志，允许您根据字段位置提取文本。默认情况下，`cut` 使用 TAB 字符作为分隔符，这意味着由 TAB 分隔的所有内容都被视为一个独立的字段。

让我们看看如何根据字段使用 cut f：

```bash
cut -f 2 sample.txt
```

由于我们在 "lazy" 和 "dog" 之间插入了一个 TAB，此命令将 "dog" 视为第二个字段。您的输出应该是 "dog"。

### 使用自定义分隔符

您还可以将字段标志与分隔符标志 (`-d`) 结合使用，以指定自定义分隔符。当处理使用逗号或分号等字符分隔数据的​​文件时，这非常有用。

```bash
cut -f 1 -d ";" sample.txt
```

此命令将分隔符从 TAB 更改为分号 (`;`)。由于我们正在切割第一个字段 (`-f 1`)，结果将是 "The quick brown"。

## Exercise

实践造就完美！以下是一些实践实验，以加强您对使用 `cut` 和其他相关命令进行文本处理的理解：

1. **[Linux cut 命令：文本切割](https://labex.io/zh/labs/linux-linux-cut-command-text-cutting-219187)** - 此实验提供了对 `cut` 命令的直接实践介绍，允许您像课程中所讨论的那样，练习从文本文件中提取特定的列或字段。
2. **[简单文本处理](https://labex.io/zh/labs/linux-simple-text-processing-18004)** - 通过使用 `tr`、`col`、`join` 和 `paste` 等强大命令来扩展您的文本操作技能，以高效地处理和分析文本数据。
3. **[序列控制和管道](https://labex.io/zh/labs/linux-sequence-control-and-pipeline-17994)** - 通过学习控制命令执行序列、利用管道以及利用 `cut`、`grep`、`wc`、`sort` 和 `uniq` 等强大的文本处理工具，提高您的命令行效率。

这些实验将帮助您在实际场景中应用这些概念，并建立在 Linux 中进行文本处理的信心。

## Quiz Question

您将使用什么命令来获取文件中每一行的第一个字符？

## Quiz Answer

cut -c 1
