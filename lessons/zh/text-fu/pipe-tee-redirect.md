---
index: 4
lang: "zh"
title: "管道和 tee"
meta_title: "管道和 tee - Text-Fu"
meta_description: "探索 Linux 中强大的管道 (pipe) 和 tee 命令。学习如何使用 Linux 管道 tee 组合链接命令，并将输出重定向到屏幕和文件。本指南涵盖如何将管道连接到 tee 以实现高级命令行数据流。"
meta_keywords: "linux 中的 pipe 和 tee 命令，linux 管道 tee, 管道到 tee, Linux 管道，tee 命令，stdout, stdin, 命令行重定向，Linux 教程"
---

## Lesson Content

在 Linux 中，当您开始连接命令时，命令行会变得异常强大。您不再需要运行一个命令、保存其输出，然后再运行另一个命令，而是可以创建一个管道，将数据直接在它们之间传递。

### 理解管道操作符

让我们从一个产生大量输出的命令开始：

```bash
ls -la /etc
```

列表项可能太长，无法在屏幕上显示，难以阅读。虽然您可以将此输出重定向到文件，但更有效的方法是将其直接发送到另一个命令，例如 `less`，以便于查看。

```bash
ls -la /etc | less
```

管道操作符 `|`（表示为竖线）是此过程的关键。它获取左侧命令的标准输出（`stdout`），并将其用作右侧命令的标准输入（`stdin`）。在这种情况下，我们将 `ls -la /etc` 的输出通过管道直接传输到 `less` 命令中。管道是一个您将持续使用的基本工具。

### 使用 Tee 命令分割输出

如果您想同时在屏幕上查看输出并将其保存到文件中怎么办？这时 `tee` 命令就派上用场了。`linux 中的 pipe and tee 命令` 是用于日志记录和监控的经典组合。

```bash
ls | tee peanuts.txt
```

运行此命令后，您将在终端上看到 `ls` 的输出。如果您检查 `peanuts.txt` 的内容，您会发现完全相同的信息。`tee` 命令有效地将输出流分成两个方向：一个到标准输出，另一个到指定的文件。

### 结合管道和 Tee

通过链接这些命令，您可以创建更高级的工作流程。一种常见模式是在较长的命令链中间使用 `pipe to tee`。这允许您在继续处理数据之前保存中间结果。

例如，您可以使用 `linux pipe tee` 组合来在进一步过滤之前查看和保存输出：

```bash
ls -la /etc | tee etc_listing.txt | grep "conf"
```

此命令执行三件事：

1.  它列出 `/etc` 目录的内容。
2.  它将该输出通过管道传输到 `tee`，`tee` 将一份副本保存到 `etc_listing.txt` 中，并同时将其传递下去。
3.  来自 `tee` 的输出随后通过管道传输到 `grep`，`grep` 过滤出包含 "conf" 的行。

掌握这些命令将显著提高您在命令行上的效率。

## Exercise

实践造就完美！以下是一些实践实验，以加强您对输入/输出重定向和管道的理解：

1. **[在 Linux 中重定向输入和输出](https://labex.io/zh/labs/comptia-redirecting-input-and-output-in-linux-590840)** - 通过操作标准输出 (stdout)、标准错误 (stderr) 和标准输入 (stdin)，并使用 `>`, `>>`, `2>` 和 `tee` 命令等操作符，练习控制命令的数据流。
2. **[序列控制和管道](https://labex.io/zh/labs/linux-sequence-control-and-pipeline-17994)** - 学习控制命令执行序列，利用管道，并利用强大的文本处理工具，如 `cut`、`grep`、`wc`、`sort` 和 `uniq`。
3. **[数据流重定向](https://labex.io/zh/labs/linux-data-stream-redirection-17995)** - 学习 Linux 流重定向的艺术，包括操作标准输入、输出和错误流，组合输出以及利用 `/dev/null`。

这些实验将帮助您在实际场景中应用管道和重定向的概念，并建立对命令行数据处理的信心。

## Quiz Question

在 Linux 命令中，代表管道操作符的单个字符是什么？请仅用符号回答。

## Quiz Answer

|
