---
index: 3
lang: "zh"
title: "stderr (标准错误)"
meta_title: "stderr (标准错误) - Text-Fu"
meta_description: "了解如何在 Linux 中管理标准错误。本指南涵盖 stderr 重定向、stderr 文件描述符 (2) 以及如何使用 2>、2>&1 和 &> 将 stderr 重定向到文件或 /dev/null。"
meta_keywords: "stderr, 标准错误 linux, stderr 文件描述符，stderr 文件，linux 标准错误，重定向 stderr, 2>, 2>&1, &>, /dev/null, bash 错误处理"
---

## Lesson Content

让我们探索一下当命令产生错误时会发生什么。尝试列出一个不存在的目录的内容，并将输出重定向到一个名为 `peanuts.txt` 的文件。

```bash
ls /fake/directory > peanuts.txt
```

你不会看到一个干净的提示符，而是在屏幕上看到一条错误消息：

```plaintext
ls: cannot access /fake/directory: No such file or directory
```

你可能会想，为什么这条消息没有被发送到文件中。这是因为另一个 I/O 流在起作用：**标准错误**，或 **stderr**。

### 什么是 Linux 中的标准错误？

在 Linux 中，`stderr` 是程序用于发送错误消息和诊断信息的默认输出流。它与用于正常程序输出的标准输出 (`stdout`) 流完全分开。默认情况下，`stdout` 和 `stderr` 都会将它们的输出发送到你的终端屏幕，这就是你直接看到错误消息的原因。

要控制 `stderr`，你需要一种不同的重定向方法。

### 理解文件描述符

为了管理像 `stdin`、`stdout` 和 `stderr` 这样的 I/O 流，系统使用文件描述符。**文件描述符** 是内核用来识别打开的文件或流的非负整数。默认的文件描述符是：

- `0`: stdin (标准输入)
- `1`: stdout (标准输出)
- `2`: stderr (标准错误)

数字 `2` 是专用的 **stderr 文件描述符**，我们可以用它来控制错误消息的去向。

### 将 stderr 重定向到文件

要将 `stderr` 重定向到文件，你需要使用文件描述符 `2` 后面跟上 `>` 运算符。此命令会将任何错误消息发送到指定的 `stderr 文件`。

```bash
ls /fake/directory 2> peanuts.txt
```

现在，你的终端会保持安静，而错误消息将位于 `peanuts.txt` 中。

### 合并 stdout 和 stderr

如果想将正常输出和错误消息都捕获到同一个文件中，该怎么办？你可以通过重定向两个流来实现这一点。

```bash
ls /fake/directory /etc/passwd > peanuts.txt 2>&1
```

我们来分解一下：

1. `> peanuts.txt` 将 `stdout` (文件描述符 1) 重定向到 `peanuts.txt` 文件。
2. `2>&1` 将 `stderr` (文件描述符 2) 重定向到 `stdout` (文件描述符 1) 当前指向的相同位置。

顺序很重要。`2>&1` 将 `stderr` 发送到 `stdout` 的当前目标。在这种情况下，`stdout` 指向一个文件，因此 `stderr` 也被发送到该文件。

重定向 `stdout` 和 `stderr` 的更现代、更简洁的方法是使用 `&>`。

```bash
ls /fake/directory /etc/passwd &> peanuts.txt
```

### 丢弃错误消息

有时，你可能希望运行一个命令并完全忽略任何潜在的错误消息。要做到这一点，你可以将 `stderr` 重定向到一个名为 `/dev/null` 的特殊文件，该文件会丢弃写入其中的任何数据。

```bash
ls /fake/directory 2> /dev/null
```

此命令将执行，并且来自 `stderr` 的任何错误输出都将被发送到 `/dev/null` 并被丢弃，使你的屏幕保持干净。

## Exercise

熟能生巧！这里有一些实践练习，以加强你对输入/输出重定向的理解：

1. **[在 Linux 中重定向输入和输出](https://labex.io/zh/labs/comptia-redirecting-input-and-output-in-linux-590840)** - 在此实验中，你将学习如何在 Linux shell 中重定向输入和输出。你将通过操纵标准输出 (stdout)、标准错误 (stderr) 和标准输入 (stdin) 以及使用 `>`、`>>`、`2>` 和 `tee` 命令等运算符来练习控制命令的数据流。

此实验将帮助你在实际场景中应用 I/O 重定向的概念，并建立对管理 Linux 中数据流的信心。

## Quiz Question

用于重定向 `stderr` 流的运算符是什么？请在答案中提供确切的运算符。

## Quiz Answer

2>
