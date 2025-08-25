---
index: 2
lang: "zh"
title: "stdin（标准输入）"
meta_title: "stdin（标准输入）- Text-Fu"
meta_description: "了解 Linux 中的 stdin（标准输入）重定向。了解如何将“<”运算符与文件和命令一起使用。探索实际示例并提高您的 Linux 命令行技能。"
meta_keywords: "stdin, 标准输入，Linux 重定向，< 运算符，Linux 教程，命令行，初学者，指南"
---

## Lesson Content

在上一课中，我们了解到我们可以使用不同的 stdout 流，例如文件或屏幕。同样，我们也可以使用不同的标准输入 (stdin) 流。我们知道我们可以从键盘等设备获取 stdin，但我们也可以使用文件、其他进程的输出以及终端。让我们看一个例子。

让我们使用上一课中的 `peanuts.txt` 文件作为此示例。请记住，它里面有文本“Hello World”。

```bash
cat < peanuts.txt > banana.txt
```

就像我们使用 `>` 进行 stdout 重定向一样，我们可以使用 `<` 进行 stdin 重定向。

通常，在 `cat` 命令中，您将文件发送给它，该文件成为 stdin。在这种情况下，我们将 `peanuts.txt` 重定向为我们的 stdin。然后 `cat peanuts.txt` 的输出（即“Hello World”）被重定向到另一个名为 `banana.txt` 的文件。

## Exercise

熟能生巧！以下是一些动手实验，旨在加强您对 Linux 中输入和输出重定向的理解：

1. **[在 Linux 中重定向输入和输出](https://labex.io/zh/labs/comptia-redirecting-input-and-output-in-linux-590840)** - 练习通过使用 >、>>、2> 和 tee 命令等操作符来操作标准输出 (stdout)、标准错误 (stderr) 和标准输入 (stdin) 来控制命令的数据流。
2. **[数据流重定向](https://labex.io/zh/labs/linux-data-stream-redirection-17995)** - 学习 Linux 流重定向的艺术。操作标准输入、输出和错误流，组合输出，并利用 /dev/null 进行高级文件操作。
3. **[序列控制和管道](https://labex.io/zh/labs/linux-sequence-control-and-pipeline-17994)** - 学习控制命令执行序列并利用管道，这是将一个命令的输出作为另一个命令的输入的基础。

这些实验将帮助您在实际场景中应用输入和输出重定向的概念，并增强您对 shell 脚本和数据操作的信心。

## Quiz Question

您使用哪个重定向符来重定向 stdin？

## Quiz Answer

<
