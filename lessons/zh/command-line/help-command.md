---
index: 15
lang: "zh"
title: "help"
meta_title: "help - 命令行"
meta_description: "了解如何在 Bash 中使用 'help' 命令以获取快速命令行帮助。理解内置命令并查找 Linux 程序的选项。"
meta_keywords: "Linux help 命令，Bash help, 命令行帮助，Linux 命令，Linux 初学者，Linux 教程，Bash 教程"
---

## Lesson Content

Linux 有一些很棒的内置工具，可以帮助您了解如何使用命令或检查命令有哪些可用标志。其中一个工具 `help` 是一个内置的 Bash 命令，它为其他 Bash 命令（例如 `echo`、`logout`、`pwd`）提供帮助。

```bash
help echo
```

这将为您提供 `echo` 命令的描述以及您可以使用的选项。对于其他可执行程序，约定是有一个名为 `--help` 或类似名称的选项。

```bash
bash --help
```

并非所有发布可执行文件的开发人员都会遵循此标准，但这可能是您寻求程序帮助的最佳选择。

## Exercise

虽然本主题没有特定的实验，但我们建议您探索全面的 [Linux 学习路径](https://labex.io/zh/learn/linux) 来练习相关的 Linux 技能和概念。

## Quiz Question

如何快速获取内置 Bash 命令的命令行帮助？

## Quiz Answer

help
