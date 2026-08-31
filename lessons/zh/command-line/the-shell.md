---
lesson_id: "the-shell"
course_id: "command-line"
lang: "zh"
order_index: 1
title: "Shell 介绍"
description: "了解 Linux shell 是什么，以及系统如何执行命令。"
meta_title: "Shell - 命令行基础"
meta_description: "了解什么是 Linux shell，Bash 提示符如何工作，以及如何使用适合初学者的命令行示例运行你的第一个命令。"
meta_keywords: "linux shell, bash shell, 命令行, linux 终端, shell 提示符, echo 命令, 基础 linux 命令"
---

## 什么是 Linux Shell

欢迎开始你的 Linux 之旅！第一步是了解 Linux shell。Shell 是一个程序，它接受你输入的命令，向操作系统请求执行这些命令，然后将结果打印回你的终端。

如果你使用过图形用户界面，你习惯于点击窗口、菜单和按钮。而在命令行中，你输入精确的指令。名为“Terminal”、“Console”或“Konsole”的应用程序通常会为你打开一个 shell 会话。

终端是供你输入内容的窗口或应用程序，而 shell 是运行在终端内部的程序。

Shell 很有用，因为它速度快、可编写脚本，并且几乎在所有 Linux 系统上都可用。随着你学习更多命令，你可以将它们组合起来检查文件、管理目录、搜索文本、安装软件以及自动化重复的工作。

:::single-choice{#distinguish-shell-and-terminal}
以下哪项正确描述了终端与 shell 的关系？

::option[终端提供窗口，shell 在其中运行。]{#shell-runs-in-terminal .correct explanation="终端是你使用的界面，shell 则是在其中运行并处理命令的程序。"}
::option[终端接受命令，shell 只显示命令输出。]{#terminal-accepts-commands explanation="这个说法颠倒了二者的职责；终端提供界面，shell 接受并执行命令。"}
::option[终端和 shell 是同一个程序的两个名称。]{#terminal-equals-shell explanation="二者会协同工作，但并不是同一个程序；终端会打开一个运行 shell 的会话。"}
:::

## 与 Bash Shell 交互

在本课程中，我们将重点介绍 Bash，全称 Bourne Again Shell。Bash 是最常见的 Linux shell 之一，即使你以后使用 `zsh`、`fish` 或其他 shell，学习 Bash 也是一个很好的基础。

当你打开终端时，会看到 shell 提示符。它的外观可能不同，但通常会显示你的用户名、主机名和当前目录。

```plaintext
pete@icebox:/home/pete $
```

`$` 符号表示 shell 已准备好接受你作为普通用户的输入。输入命令时不需要输入这个符号；它是 shell 显示的。如果你看到 `#`，通常表示你以 root 用户身份工作，拥有更高权限但风险也更大。

:::single-choice{#interpret-dollar-prompt}
示例提示符末尾的 `$` 表示什么？

::option[shell 正以 root 用户权限运行。]{#root-user-ready explanation="root 提示符通常以 `#` 而不是 `$` 结尾；root 权限更大，风险也更高。"}
::option[shell 正在等待普通用户输入。]{#normal-user-ready .correct explanation="`$` 表示普通用户提示符，说明 shell 已准备好接收命令。"}
::option[下一条命令必须以美元符号开头。]{#type-dollar-first explanation="`$` 属于提示符；输入时只需键入其后的命令，不要复制这个符号。"}
:::

命令通常遵循以下模式：

```bash
command options arguments
```

例如，在 `echo Hello World` 中，`echo` 是命令，`Hello World` 是传递给它的文本。

:::single-choice{#identify-command-name}
在 `echo Hello World` 中，哪一部分是命令名？

::option[`Hello`]{#hello-command explanation="`Hello` 位于命令名之后，是传递给 `echo` 的文本之一。"}
::option[`World`]{#world-command explanation="`World` 同样是传递给 `echo` 的文本，而不是所执行命令的名称。"}
::option[`echo`]{#echo-command .correct explanation="`echo` 指定 shell 应运行的程序，后面的单词会作为参数传给它。"}
:::

## 你的第一个 Linux 命令

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

:::single-choice{#group-words-with-quotes}
哪个命令会让 shell 把 `Hello from Bash` 视为一段加引号的文本？

::option[`echo "Hello from Bash"`]{#quoted-words .correct explanation="引号把三个单词组合成一个参数，再传递给 `echo`。"}
::option[`echo Hello from Bash`]{#unquoted-words explanation="它会显示相同的文字，但由于没有引号，shell 会把三个单词视为不同参数。"}
::option[`"echo Hello from Bash"`]{#quoted-command explanation="给整行加引号会让 shell 查找具有这一完整名称的命令，而不是运行 `echo` 并向它传入文本。"}
:::

要练习这些技能，可以探索完整的 [![Shell 学习路径](https://labex.io/cdn-cgi/image/width=200,height=200,quality=80,format=auto,onerror=redirect/https://file.labex.io/path/FaVTnI4iqZP0.png)Shell 学习路径](https://labex.io/zh/learn/shell)。

## 初学者常见提示

- 按 `Enter` 键运行命令。
- 使用 `上箭头` 键调出之前的命令。
- Linux 中命令和文件名区分大小写。
- 空格很重要。`echo hello` 和 `echohello` 是不同的命令。
- 如果命令似乎卡住，通常按 `Ctrl-C` 可以取消。

## 总结

现在，你可以说明 shell 的作用，并与基本的 shell 提示符交互。

1. 区分终端和 shell。
2. 识别命令提示符。
3. 使用 `echo` 运行简单命令。
