---
index: 2
lang: "zh"
title: "标准输入 (stdin)"
meta_title: "标准输入 (stdin) - Text-Fu"
meta_description: "通过学习如何重定向标准输入 (stdin)，掌握 Linux 命令行操作。本指南涵盖 stdin 与 stdout 的关系、使用 '<' 运算符，以及如 'cat stdin' 等实用示例，以有效管理数据流。"
meta_keywords: "stdin, 标准输入，重定向 stdin, cat stdin, stdin 和 stdout, Linux 重定向，命令行，输入流"
---

## Lesson Content

在我们之前的课程中，我们学习了如何重定向标准输出（stdout）流。同样地，我们也可以管理标准输入（`stdin`）流。默认情况下，程序从键盘接收其 `stdin`，但我们也可以使用文件或其他进程的输出来作为输入源。

### 理解 stdin 和 stdout

Linux 中的每个命令行进程都至少有两个基本数据流：标准输入（`stdin`）和标准输出（`stdout`）。程序从 `stdin` 读取数据，并将其结果写入 `stdout`。理解如何控制 `stdin 和 stdout` 对于有效的命令行工作至关重要。

### 如何重定向 stdin

就像我们使用 `>` 来重定向 stdout 一样，我们使用 `<` 运算符来**重定向 stdin**。这个强大的功能允许您告诉命令从文件读取其输入，而不是等待您在键盘上输入。这是输入重定向的一个核心概念。

### 使用 cat stdin 的实际示例

让我们回顾一下上一课中的 `peanuts.txt` 文件，其中包含文本 "Hello World"。考虑以下命令：

```bash
cat < peanuts.txt > banana.txt
```

以下是发生情况的细分：

1.  `< peanuts.txt` 部分告诉 shell 为 `cat` 命令**重定向 stdin**，使其从 `peanuts.txt` 读取而不是从键盘读取。
2.  `cat` 命令处理其输入。在这种情况下，使用 `cat stdin` 意味着它读取 `peanuts.txt` 的内容。
3.  `> banana.txt` 部分将 `cat` 的标准输出重定向到一个名为 `banana.txt` 的新文件。

最终，`peanuts.txt` 的内容被复制到 `banana.txt`。这个例子有效地演示了如何在单个高效的命令中管理 `stdin 和 stdout`。

## Exercise

为了巩固您的理解，请尝试这些专注于 Linux 中输入和输出重定向的动手练习：

1.  **[Linux 中的输入和输出重定向](https://labex.io/zh/labs/comptia-redirecting-input-and-output-in-linux-590840)** - 通过使用 `>`、`>>`、`2>` 等运算符以及 `tee` 命令来操作标准输出 (stdout)、标准错误 (stderr) 和标准输入 (stdin)，练习控制命令的数据流。
2.  **[数据流重定向](https://labex.io/zh/labs/linux-data-stream-redirection-17995)** - 学习 Linux 流重定向的艺术。操作标准输入、输出和错误流，组合输出，并利用 `/dev/null` 进行高级文件操作。
3.  **[序列控制和管道](https://labex.io/zh/labs/linux-sequence-control-and-pipeline-17994)** - 学习控制命令执行序列并利用管道，这是将一个命令的输出作为另一个命令的输入进行导向的基础。

这些实验将帮助您在实际场景中应用输入和输出重定向的概念，并增强您对 shell 脚本和数据操作的信心。

## Quiz Question

用于重定向 stdin 的运算符是什么？请仅用所需的符号回答。

## Quiz Answer

<
