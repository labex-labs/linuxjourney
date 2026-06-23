---
index: 17
lang: "zh"
title: "whatis 命令"
meta_title: "whatis 命令 - 命令行指南"
meta_description: "学习 Linux whatis 命令，通过示例了解如何从手册页获取命令的一行描述，以及理解多个手册章节。"
meta_keywords: "whatis 命令, linux whatis, 命令描述 linux, 手册页摘要, 命令行帮助, apropos"
---

## Lesson Content

当你探索 Linux 命令行时，会遇到大量的命令。忘记某个特定命令的作用是很自然的事情。幸运的是，有一个简单的工具可以帮助你。

### 什么是 whatis 命令

`whatis` 命令直接从命令的手册页中显示简洁的一行描述。它是快速提醒你命令主要功能的好方法，无需阅读整个手册页。

### 如何使用 whatis 命令

使用 `whatis` 非常简单。输入 `whatis` 后跟你想了解的命令。

```bash
$ whatis cat
cat (1)              - concatenate files and print on the standard output
```

### 理解输出内容

`whatis` 提供的描述来自命令手册页的 `NAME` 部分。如果某个名称在不同章节有多个手册页，`whatis` 可能会显示多行。

```bash
$ whatis passwd
passwd (1)           - change user password
passwd (5)           - the password file
```

括号中的数字是手册页的章节号。

### whatis 与 man 和 apropos 的区别

- `whatis ls`：显示精确命令名称的一行描述。
- `man ls`：打开完整的手册页。
- `apropos 关键词`：搜索手册页描述中的关键词。

例如：

```bash
$ apropos password
```

当你知道命令名称但忘记它的作用时，使用 `whatis`。

### 常见问题

**为什么 whatis 显示“nothing appropriate”？** 可能是该命令没有安装手册页，或者手册数据库需要更新。

**whatis 会显示命令选项吗？** 不会。使用 `man COMMAND` 或 `COMMAND --help` 查看选项。

**whatis 和 which 是一样的吗？** 不是。`whatis` 描述命令，`which` 显示可执行文件路径。

## Exercise

熟能生巧！虽然没有专门针对 `whatis` 命令的实验，但了解如何查找命令和文件的信息非常重要。以下是一些动手实验，帮助你巩固在 Linux 中定位命令和文件的知识：

1. **[Linux which 命令：命令定位](https://labex.io/zh/labs/linux-linux-which-command-command-locating-215210)** - 练习使用 `which` 命令定位可执行文件，了解系统 PATH 中命令的优先级。
2. **[Linux whereis 命令：文件和命令查找](https://labex.io/zh/labs/linux-linux-whereis-command-file-and-command-finding-215211)** - 学习使用 `whereis` 查找命令的二进制文件、源代码和手册页，加深对命令结构的理解。
3. **[发现关键系统资源](https://labex.io/zh/labs/linux-discover-critical-system-resources-388032)** - 该挑战结合使用 `which`、`whereis` 和 `find`，帮助你高效浏览文件系统，发现重要的系统资源。

这些实验将帮助你在实际场景中应用命令和文件查找的概念，增强对 Linux 基本工具的信心。

## Quiz Question

你可以使用什么命令查看命令的简短描述？请用英文回答，注意小写。

## Quiz Answer

whatis
