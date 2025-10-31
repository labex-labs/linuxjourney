---
index: 15
lang: "zh"
title: "帮助"
meta_title: "帮助 - 命令行"
meta_description: "了解如何使用 Linux help 命令在终端中快速获取帮助。本 Bash 教程解释了如何获取 shell 内建命令的帮助以及如何为其他 Linux 程序使用 --help 标志。"
meta_keywords: "Linux help 命令，Bash 帮助，命令行帮助，Linux 命令，Linux 入门，Linux 教程，Bash 教程，shell 内建命令，命令行辅助"
---

## Lesson Content

在 Linux 命令行工作时，您经常需要快速回顾某个命令的工作方式或它接受哪些选项。幸运的是，Linux 提供了出色的工具，可以直接在终端中获取命令行帮助。

### Bash 内建命令的 'help' 命令

最直接的工具之一是 `help`，它是直接内置于 Bash shell 中的一个命令。它专门用于提供有关其他 Bash 内建命令的信息。内建命令是 shell 本身的一部分，而不是一个单独的程序。示例包括 `echo`、`cd` 和 `pwd`。

要使用 **Linux help 命令**，只需键入 `help`，后跟内建命令的名称。

```bash
help echo
```

这将显示 `echo` 命令的摘要、其语法以及可用选项的列表。这是获取 shell 特定功能帮助的最快方法。

### 可执行程序的 --help 标志

对于大多数不是内置于 shell 中的其他可执行程序，`help` 命令将不起作用。相反，一个常见的约定是提供一个 `--help` 标志。此选项会指示程序打印用法摘要然后退出。

```bash
ls --help
```

虽然大多数开发者都遵循此标准，但它并非普遍适用。然而，尝试使用 `--help` 标志通常是查找不熟悉程序的帮助信息的第一步。这是学习 **Linux 命令** 的任何人的一项基本技能。

## Exercise

虽然此主题没有特定的实验，但我们建议探索综合性的 [Linux 学习路径](https://labex.io/zh/learn/linux) 来练习相关的 Linux 技能和概念。

## Quiz Question

如何为内置的 Bash 命令获取快速的命令行帮助？（请提供单个命令名称，使用英文且小写。）

## Quiz Answer

help
