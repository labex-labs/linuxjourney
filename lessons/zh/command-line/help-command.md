---
index: 15
lang: "zh"
title: "help 命令"
meta_title: "help - 命令行帮助"
meta_description: "学习如何通过 Bash help、--help 输出、man 手册页和 type 命令获取 Linux 命令行帮助，包括 shell 内置命令和外部命令。"
meta_keywords: "linux help 命令, bash help, 命令行帮助, --help, shell 内置命令, man 命令, type 命令"
---

## Lesson Content

在使用 Linux 命令行时，你经常需要快速回顾某个命令的用法或它支持哪些选项。Linux 提供了多种直接在终端中使用的帮助工具。

### Bash 内置命令的 `help` 命令

最直接的工具之一是 `help`，这是一个直接内置在 Bash shell 中的命令。它专门用于提供其他 Bash 内置命令的信息。内置命令是 shell 自身的一部分，而不是独立的程序。示例包括 `echo`、`cd` 和 `pwd`。

使用 `help` 时，输入它后跟内置命令的名称。

```bash
$ help echo
```

这将显示 `echo` 命令的摘要、语法以及可用选项列表。这是获取 shell 特定功能帮助的最快方式。

### 可执行程序的 --help 选项

对于大多数不是内置于 shell 的其他可执行程序，`help` 命令不起作用。相反，常见的约定是提供一个 `--help` 选项。该选项会让程序打印使用说明摘要，然后退出。

```bash
$ ls --help
```

虽然大多数开发者遵循此标准，但并非所有程序都支持。尝试 `--help` 通常是了解不熟悉程序的第一步。

### 查找命令类型

如果你不确定某个命令是 Bash 内置命令还是外部程序，可以使用 `type`。

```bash
$ type cd
cd is a shell builtin
$ type ls
ls is /usr/bin/ls
```

这有助于你选择使用 `help cd`、`ls --help` 或 `man ls`。

### 选择合适的帮助工具

- 对于 Bash 内置命令如 `cd`、`echo` 和 `history`，使用 `help COMMAND`。
- 对于许多外部命令，使用 `COMMAND --help` 获取快速摘要。
- 使用 `man COMMAND` 查看详细的手册页。
- 使用 `whatis COMMAND` 获取一行描述。

### 常见问题

**为什么 help ls 不起作用？** `ls` 通常是外部程序，不是 Bash 内置命令。试试 `ls --help` 或 `man ls`。

**为什么不是所有命令都支持 --help？** 这是一个约定，而非严格规则。

**检查命令最快的方法是什么？** 对外部命令尝试 `COMMAND --help`，对 Bash 内置命令使用 `help COMMAND`。

## Exercise

虽然本主题没有特定的实验，但我们推荐探索全面的 [Linux 学习路径](https://labex.io/zh/learn/linux) 来练习相关的 Linux 技能和概念。

## Quiz Question

如何快速获取内置 Bash 命令的命令行帮助？（请用英文小写提供单个命令名称。）

## Quiz Answer

help
