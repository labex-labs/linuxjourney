---
index: 1
lang: "zh"
title: "stdout (标准输出)"
meta_title: "stdout (标准输出) - Text-Fu"
meta_description: "了解 Linux stdout 和 I/O 重定向。了解如何使用 > 和 >> 运算符将命令输出重定向到文件。立即开始你的 Linux 之旅！"
meta_keywords: "Linux stdout, I/O 重定向，Linux 命令，重定向输出，Linux 教程，Linux 初学者，Linux 指南，shell 脚本"
---

## Lesson Content

到目前为止，我们已经熟悉了许多命令及其输出，这引出了我们的下一个主题：I/O（输入/输出）流。让我们运行以下命令，然后我们将讨论它是如何工作的。

```bash
echo Hello World > peanuts.txt
```

刚才发生了什么？嗯，检查你运行该命令的目录，瞧，你应该会看到一个名为 `peanuts.txt` 的文件。查看该文件，你应该会看到文本“Hello World”。一个命令中发生了许多事情，所以让我们来分解一下。

首先，让我们分解第一部分：

```bash
echo Hello World
```

我们知道这会将“Hello World”打印到屏幕上，但它是如何做到的呢？进程使用 I/O 流来接收输入和返回输出。默认情况下，`echo` 命令从键盘获取输入（标准输入或 stdin）并将输出（标准输出或 stdout）返回到屏幕。因此，当你输入 `echo Hello World` 时，你会在屏幕上看到“Hello World”。然而，I/O 重定向允许我们改变这种默认行为，从而提供更大的文件灵活性。

让我们继续命令的下一部分：

```bash
>
```

`>` 是一个重定向运算符，它允许我们改变标准输出的去向。它允许我们将 `echo Hello World` 的输出发送到文件而不是屏幕。如果文件不存在，它会为我们创建它。但是，如果它确实存在，它会覆盖它（你可以添加一个 shell 标志来防止这种情况，具体取决于你使用的 shell）。

这就是 stdout 重定向的工作原理！

嗯，假设我不想覆盖我的 `peanuts.txt`。幸运的是，也有一个重定向运算符可以做到这一点：`>>`。

```bash
echo Hello World >> peanuts.txt
```

这会将“Hello World”附加到 `peanuts.txt` 文件的末尾。如果文件不存在，它会为我们创建它，就像 `>` 重定向器一样！

## Exercise

熟能生巧！这里有一些动手实验来巩固你对 I/O 重定向的理解：

1. **[在 Linux 中重定向输入和输出](https://labex.io/zh/labs/comptia-redirecting-input-and-output-in-linux-590840)** - 练习通过使用 `>`, `>>`, `2>` 和 `tee` 命令操作标准输出 (stdout)、标准错误 (stderr) 和标准输入 (stdin) 来控制命令的数据流。

这个实验将帮助你在实际场景中应用这些概念，并增强你对 I/O 重定向的信心。

## Quiz Question

你使用哪个重定向器将输出附加到文件？

## Quiz Answer

> >