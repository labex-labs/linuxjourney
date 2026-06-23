---
index: 1
lang: "zh"
title: "Shell 介绍"
meta_title: "Shell - 命令行基础"
meta_description: "了解什么是 Linux shell，Bash 提示符如何工作，以及如何使用适合初学者的命令行示例运行你的第一个命令。"
meta_keywords: "linux shell, bash shell, 命令行, linux 终端, shell 提示符, echo 命令, 基础 linux 命令"
---

## Lesson Content

### 什么是 Linux Shell

欢迎开始你的 Linux 之旅！第一步是了解 Linux shell。Shell 是一个程序，它接受你输入的命令，向操作系统请求执行这些命令，然后将结果打印回你的终端。

如果你使用过图形用户界面，你习惯于点击窗口、菜单和按钮。而在命令行中，你输入精确的指令。名为“Terminal”、“Console”或“Konsole”的应用程序通常会为你打开一个 shell 会话。

Shell 很有用，因为它速度快、可编写脚本，并且几乎在所有 Linux 系统上都可用。随着你学习更多命令，你可以将它们组合起来检查文件、管理目录、搜索文本、安装软件以及自动化重复的工作。

### 与 Bash Shell 交互

在本课程中，我们将重点介绍 Bash，全称 Bourne Again Shell。Bash 是最常见的 Linux shell 之一，即使你以后使用 `zsh`、`fish` 或其他 shell，学习 Bash 也是一个很好的基础。

当你打开终端时，会看到 shell 提示符。它的外观可能不同，但通常会显示你的用户名、主机名和当前目录。

```plaintext
pete@icebox:/home/pete $
```

`$` 符号表示 shell 已准备好接受你作为普通用户的输入。输入命令时不需要输入这个符号；它是 shell 显示的。如果你看到 `#`，通常表示你以 root 用户身份工作，拥有更高权限但风险也更大。

命令通常遵循以下模式：

```bash
command options arguments
```

例如，在 `echo Hello World` 中，`echo` 是命令，`Hello World` 是传递给它的文本。

### 你的第一个 Linux 命令

让我们从初学者最基础的 Linux 命令之一开始：`echo`。这个命令会将你提供的文本显示回终端。

```bash
$ echo Hello World
Hello World
```

试试更多示例：

```bash
$ echo Linux is fun
Linux is fun
$ echo "Hello from Bash"
Hello from Bash
```

当你希望 shell 将多个单词视为一段文本时，使用引号非常有用。

### 初学者常见提示

- 按 `Enter` 键运行命令。
- 使用 `上箭头` 键调出之前的命令。
- Linux 中命令和文件名区分大小写。
- 空格很重要。`echo hello` 和 `echohello` 是不同的命令。
- 如果命令似乎卡住，通常按 `Ctrl-C` 可以取消。

### 常见问题

**Shell 和终端是一样的吗？** 不完全一样。终端是你输入的窗口或应用程序，shell 是运行在其中的程序。

**我需要输入示例中的 `$` 吗？** 不需要。`$` 是提示符标记，只输入它后面的命令。

**既然有其他 shell，为什么要学 Bash？** Bash 广泛可用，文档丰富，是教程和脚本中常用的 shell。

## Exercise

我们推荐探索全面的 [![Shell Learning Path](https://labex.io/_ipx/f_webp&q_100&s_20x20/https://file.labex.io/path/FaVTnI4iqZP0.png)Shell Learning Path](https://labex.io/zh/learn/shell) 来练习相关技能和概念。

## Quiz Question

当你输入 `echo Hello World` 时，屏幕上显示的准确输出是什么？请用英文回答，注意大小写和空格。

## Quiz Answer

Hello World
