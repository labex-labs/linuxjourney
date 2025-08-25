---
index: 1
lang: "zh"
title: "Shell"
meta_title: "Shell - 命令行"
meta_description: "了解 Linux shell、Bash 和基本命令，如 'echo'。理解 shell 提示符，并通过这个适合初学者的指南开始您的 Linux 之旅。"
meta_keywords: "Linux shell, Bash, echo 命令，Linux 教程，命令行，Linux 初学者，shell 提示符，Linux 指南"
---

## Lesson Content

世界是你的牡蛎，或者说，shell 是你的牡蛎。什么是 shell？Shell 基本上是一个程序，它从键盘接收你的命令并将其发送给操作系统执行。如果你曾经使用过 GUI，你可能见过“终端”或“控制台”之类的程序；这些只是为你启动 shell 的程序。在整个课程中，我们将学习 shell 的奇妙之处。

在本课程中，我们将使用 shell 程序 Bash (Bourne Again Shell)。几乎所有的 Linux 发行版都将默认使用 Bash shell。还有其他可用的 shell，例如 `ksh`、`zsh` 和 `tsch`，但我们不会涉及这些。

让我们直接开始吧！根据发行版的不同，你的 shell 提示符可能会有所不同，但大多数情况下，它应该遵循以下格式：

```plaintext
username@hostname:current_directory
pete@icebox:/home/pete $
```

注意到提示符末尾的 `$` 了吗？不同的 shell 会有不同的提示符。在我们的例子中，`$` 表示使用 Bash、Bourne 或 Korn shell 的普通用户。你输入命令时不需要添加提示符符号；只需知道它在那里即可。

让我们从一个简单的命令 `echo` 开始。`echo` 命令只是将文本参数打印到显示器上。

```bash
echo Hello World
```

## Exercise

虽然本主题没有具体的实验，但我们建议探索全面的 [Linux 学习路径](https://labex.io/zh/learn/linux) 来练习相关的 Linux 技能和概念。

## Quiz Question

当您输入 `echo Hello World` 时，显示器上应该输出什么？

## Quiz Answer

Hello World
