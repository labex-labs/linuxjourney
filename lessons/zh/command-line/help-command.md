---
lang: "zh"
title: "帮助"
description: "学习如何在 Bash 中使用'help'命令获取快速命令行帮助。了解内置命令并查找 Linux 程序的选项。"
keywords: "Linux help 命令，Bash help, 命令行帮助，Linux 命令，Linux 初学者，Linux 教程，Bash 教程"
---

## Lesson Content

Linux 有一些很棒的内置工具，可以帮助你理解如何使用命令或查看命令可用的标志。其中一个工具`help`是一个内置的 Bash 命令，它为其他 Bash 命令（例如`echo`、`logout`、`pwd`）提供帮助。

```bash
help echo
```

这将为你提供`echo`命令的描述以及你可以使用的选项。对于其他可执行程序，通常会有一个名为`--help`或类似名称的选项。

```bash
echo --help
```

并非所有发布可执行文件的开发者都会遵循此标准，但这可能是你找到程序帮助的最佳途径。

## Exercise

对`echo`命令、`logout`命令和`pwd`命令运行`help`。

## Quiz Question

如何获取内置 Bash 命令的快速命令行帮助？

## Quiz Answer

help
