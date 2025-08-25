---
index: 3
lang: "zh"
title: "stderr（标准错误）"
meta_title: "stderr（标准错误）- Text-Fu"
meta_description: "了解 Linux stderr（标准错误）重定向。理解 2>、2>&1、&> 和 /dev/null 在 Bash 中处理错误。提高你的 Linux 命令行技能！"
meta_keywords: "Linux stderr, 标准错误，2> 重定向，2>&1, &> 重定向，/dev/null, Bash 错误处理，Linux 教程，Linux 初学者"
---

## Lesson Content

现在我们来尝试一些不同的东西。让我们尝试列出系统上不存在的目录的内容，并将输出再次重定向到 `peanuts.txt` 文件。

```bash
ls /fake/directory > peanuts.txt
```

你应该看到的是：

```plaintext
ls: cannot access /fake/directory: No such file or directory
```

现在你可能会想，这条消息不应该发送到文件吗？实际上，这里还有另一个 I/O 流，称为标准错误 (stderr)。默认情况下，stderr 也会将其输出发送到屏幕；它与 stdout 是一个完全不同的流。所以你需要以不同的方式重定向它的输出。

不幸的是，重定向器不如使用 `<` 或 `>` 那么好用，但它非常接近。我们将不得不使用文件描述符。文件描述符是一个非负数，用于访问文件或流。我们稍后会深入探讨这一点，但现在要知道 stdin、stdout 和 stderr 的文件描述符分别是 0、1 和 2。

所以现在如果我们要将 stderr 重定向到文件，我们可以这样做：

```bash
ls /fake/directory 2> peanuts.txt
```

你应该只在 `peanuts.txt` 中看到 stderr 消息。

现在，如果我想在 `peanuts.txt` 文件中同时看到 stderr 和 stdout 怎么办？使用文件描述符也可以做到这一点：

```bash
ls /fake/directory > peanuts.txt 2>&1
```

这会将 `ls /fake/directory` 的结果发送到 `peanuts.txt` 文件，然后通过 `2>&1` 将 stderr 重定向到 stdout。这里的操作顺序很重要；`2>&1` 将 stderr 发送到 stdout 指向的任何地方。在这种情况下，stdout 指向一个文件，所以 `2>&1` 也将 stderr 发送到一个文件。所以如果你打开 `peanuts.txt` 文件，你应该会看到 stderr 和 stdout。在我们的例子中，上面的命令只输出 stderr。

有一种更短的方法可以将 stdout 和 stderr 都重定向到一个文件：

```bash
ls /fake/directory &> peanuts.txt
```

现在，如果我不想看到任何这些垃圾，并想完全摆脱 stderr 消息怎么办？嗯，你也可以将输出重定向到一个名为 `/dev/null` 的特殊文件，它会丢弃任何输入。

```bash
ls /fake/directory 2> /dev/null
```

## Exercise

熟能生巧！这里有一些动手实验来巩固你对输入/输出重定向的理解：

1. **[在 Linux 中重定向输入和输出](https://labex.io/zh/labs/comptia-redirecting-input-and-output-in-linux-590840)** - 在此实验中，你将学习如何在 Linux shell 中重定向输入和输出。你将练习通过使用 >、>>、2> 和 tee 命令操作标准输出 (stdout)、标准错误 (stderr) 和标准输入 (stdin) 来控制命令的数据流。

此实验将帮助你在实际场景中应用 I/O 重定向的概念，并增强你在 Linux 中管理数据流的信心。

## Quiz Question

stderr 的重定向符是什么？

## Quiz Answer

2>
