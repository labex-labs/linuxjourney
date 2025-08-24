---
index: 15
lang: "zh"
title: "帮助"
meta_title: "help - 命令行"
meta_description: "学习如何在 Bash 中使用 'help' 命令以获得快速命令行帮助。了解内置命令并查找 Linux 程序的选项。"
meta_keywords: "Linux help 命令，Bash help, 命令行帮助，Linux 命令，Linux 初学者，Linux 教程，Bash 教程"
---

## Lesson Content

Linux 内置了一些很棒的工具，可以帮助您了解如何使用命令或检查命令有哪些可用的标志。其中一个工具 `help` 是一个内置的 Bash 命令，它为其他 Bash 命令（例如 `echo`、`logout`、`pwd`）提供帮助。

```bash
help echo
```

这将为您提供描述以及运行 `echo` 时可以使用的选项。对于其他可执行程序，约定是有一个名为 `--help` 或类似名称的选项。

```bash
bash --help
```

并非所有发布可执行文件的开发人员都会遵循此标准，但这可能是您查找程序帮助的最佳方式。

## Exercise

对 `echo` 命令、`logout` 命令和 `pwd` 命令运行 `help`。

如需更多关于基本 Linux 命令的实践练习，请探索以下交互式实验：

- [Linux pwd Command: Directory Displaying](https://labex.io/zh/labs/linux-linux-pwd-command-directory-displaying-209734)
- [Linux cd Command: Directory Changing](https://labex.io/zh/labs/linux-linux-cd-command-directory-changing-209733)

## Quiz Question

如何快速获取内置 Bash 命令的命令行帮助？

## Quiz Answer

help
