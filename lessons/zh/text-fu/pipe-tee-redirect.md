---
index: 4
lang: "zh"
title: "管道和 tee"
meta_title: "管道和 tee - 文本技巧"
meta_description: "学习 Linux 管道和 tee 命令，实现高效的命令行数据流。理解 stdout、stdin 和文件输出。提升你的 Linux 技能！"
meta_keywords: "Linux 管道，tee 命令，Linux 教程，stdout, stdin, Linux 初学者，命令行，Linux 指南"
---

## Lesson Content

现在我们来做一些“管道”工作，虽然不是真的管道，但有点类似。我们来尝试一个命令：

```bash
ls -la /etc
```

你应该会看到一个非常长的列表；实际上，这有点难以阅读。与其将这个输出重定向到一个文件，如果我们能直接在另一个命令（比如 `less`）中看到输出，那不是很好吗？嗯，我们可以！

```bash
ls -la /etc | less
```

管道操作符 `|`，由一个竖线表示，允许我们获取一个命令的 `stdout` 并将其作为另一个进程的 `stdin`。在这个例子中，我们获取了 `ls -la /etc` 的 `stdout`，然后将其 _管道_ 到 `less` 命令。管道命令非常有用，我们将永远继续使用它。

那么，如果我想将命令的输出写入两个不同的流怎么办？这可以通过 `tee` 命令实现：

```bash
ls | tee peanuts.txt
```

你应该会在屏幕上看到 `ls` 的输出，如果你打开 `peanuts.txt` 文件，你应该会看到相同的信息！

## Exercise

熟能生巧！这里有一些动手实验，以巩固你对输入/输出重定向和管道的理解：

1. **[在 Linux 中重定向输入和输出](https://labex.io/zh/labs/comptia-redirecting-input-and-output-in-linux-590840)** - 练习使用 `>`、`>>`、`2>` 等操作符和 `tee` 命令，通过操作标准输出 (stdout)、标准错误 (stderr) 和标准输入 (stdin) 来控制命令的数据流。
2. **[序列控制和管道](https://labex.io/zh/labs/linux-sequence-control-and-pipeline-17994)** - 学习控制命令执行序列，利用管道，并利用 `cut`、`grep`、`wc`、`sort` 和 `uniq` 等强大的文本处理工具。
3. **[数据流重定向](https://labex.io/zh/labs/linux-data-stream-redirection-17995)** - 学习 Linux 流重定向的艺术，包括操作标准输入、输出和错误流，组合输出，以及利用 `/dev/null`。

这些实验将帮助你在实际场景中应用管道和重定向的概念，并增强你使用命令行进行数据操作的信心。

## Quiz Question

哪个键代表管道操作符？

## Quiz Answer

|
