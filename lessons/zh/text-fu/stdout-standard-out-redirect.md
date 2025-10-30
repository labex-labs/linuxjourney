---
index: 1
lang: "zh"
title: "标准输出 (stdout)"
meta_title: "标准输出 (stdout) - Text-Fu"
meta_description: "通过掌握标准输出 (stdout) 和 I/O 重定向，开始您的 Linux 学习之旅。本课程介绍如何使用 > 和 >> 运算符将命令输出重定向到文件，这是任何 Linux 用户的基础技能。"
meta_keywords: "Linux, 学习 Linux, stdout, I/O 重定向，标准输出，重定向输出，bash, shell 脚本，Linux 命令，Linux 教程"
---

## Lesson Content

当你继续学习 Linux 时，你已经看到了命令是如何产生输出的。这就引出了我们关于 I/O（输入/输出）流的重要主题，特别是标准输出或 **stdout**。让我们通过运行以下命令来探索这个概念：

```bash
echo Hello World > peanuts.txt
```

运行后，你会在当前目录中发现一个名为 `peanuts.txt` 的新文件。如果你查看其内容，你会看到文本 "Hello World"。让我们分解一下发生了什么。

### 理解标准输出 (stdout)

首先，考虑没有特殊字符的命令：

```bash
echo Hello World
```

默认情况下，许多命令会将它们的结果发送到 **stdout**，即你的终端屏幕。这就是为什么 `echo Hello World` 会直接在你的 shell 中显示文本。进程使用 I/O 流来接收输入（标准输入或 stdin）并发送输出。I/O 重定向允许我们更改这种默认行为，从而对数据进行更精细的控制。

### 使用 > 重定向 stdout

字符 `>` 是一个重定向运算符。它会拦截原本要发送到 **stdout** 的数据，并将其发送到一个新的目的地。

```bash
>
```

在我们的示例中，它将 `echo Hello World` 的输出发送到一个文件，而不是屏幕。如果文件不存在，它将被创建。**请小心**，如果文件已经存在，此运算符将完全覆盖其内容。

### 使用 >> 追加 stdout

如果你想向文件中添加内容而不擦除其内容，该怎么办？为此，我们使用 `>>` 运算符。

```bash
echo Hello World >> peanuts.txt
```

此运算符会将输出追加到指定文件的末尾。如果文件尚不存在，它将被创建，就像 `>` 运算符一样。掌握 **stdout** 重定向是你 Linux 之旅中的一个基本步骤。

## Exercise

为了巩固你对 I/O 重定向的理解，请尝试以下实践实验：

1.  **[在 Linux 中重定向输入和输出](https://labex.io/zh/labs/comptia-redirecting-input-and-output-in-linux-590840)** - 通过使用 `>`、`>>`、`2>` 等运算符以及 `tee` 命令来操作标准输出 (stdout)、标准错误 (stderr) 和标准输入 (stdin)，练习控制命令的数据流。

这个实验将帮助你在实际场景中应用这些概念，并增强你对 I/O 重定向的信心。

## Quiz Question

你使用哪个重定向符将输出追加到文件中？

## Quiz Answer

`>>`
