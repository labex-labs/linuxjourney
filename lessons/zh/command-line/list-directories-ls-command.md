---
index: 4
lang: "zh"
title: "ls (列出目录)"
meta_title: "ls (列出目录) - 命令行"
meta_description: "学习如何在 Linux 中使用强大的 ls 命令。本指南涵盖如何列出目录内容、使用 ls -a 查看隐藏文件、使用 ls -l 获取详细列表，以及使用 ls -r 命令进行反向排序。是掌握 cmd ls 的完美教程。"
meta_keywords: "ls 命令，列出目录，cmd ls, ls -r 命令，命令 ls, linux ls -r, 命令行 linux ls, 隐藏文件，Linux 命令，Linux 入门"
---

## Lesson Content

既然我们知道了如何在文件系统中移动，我们如何才能弄清楚我们有哪些可用内容呢？没有合适的工具，这就像在黑暗中摸索。幸运的是，强大的 `command linux ls` 命令通过列出目录内容来提供帮助。

### ls 命令的基本用法

默认情况下，`ls` 命令会列出当前目录中的目录和文件。但是，您也可以指定一个路径来列出另一个目录的内容。

```bash
ls
ls /home/pete
```

`command ls` 是一个多功能工具，可以向您显示有关您正在查看的文件和目录的详细信息。

### 查看隐藏文件

请注意，并非所有目录中的文件默认都是可见的。在 Linux 中，以点（`.`）开头的文件名是隐藏的。您可以使用带有 `-a` 标志的 `cmd ls` 来查看它们，`-a` 代表“all”（全部）。

```bash
ls -a
```

### 获取详细信息

另一个重要的 `ls` 标志是用于“long”（长格式）的 `-l`。此选项以长格式提供文件的详细列表。这将从左侧向您显示详细信息：文件权限、链接数、所有者名称、所有者组、文件大小、上次修改的时间戳以及文件或目录的名称。

```bash
ls -l
```

这是输出的一个示例：

```plaintext
pete@icebox:~$ ls -l
total 80
drwxr-x--- 7 pete penguingroup   4096 Nov 20 16:37 Desktop
drwxr-x--- 2 pete penguingroup   4096 Oct 19 10:46  Documents
drwxr-x--- 4 pete penguingroup   4096 Nov 20 09:30 Downloads
drwxr-x--- 2 pete penguingroup   4096 Oct  7 13:13   Music
drwxr-x--- 2 pete penguingroup   4096 Sep 21 14:02 Pictures
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Public
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Templates
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Videos
```

### 反向排序

有时您可能希望更改排序顺序。`ls -r command` 以反向字母顺序（倒序）列出文件和目录。当您想首先看到长列表中的最后几项时，`linux ls -r` 选项特别方便。

```bash
ls -r
```

### 组合命令标志

命令具有标志（也称为参数或选项）以添加更多功能。正如我们看到的 `-a` 和 `-l`，您可以将它们组合成一个命令，如 `ls -la`。标志的顺序通常无关紧要，因此 `ls -al` 的效果相同。您也可以添加反向标志：`ls -lar`。

```bash
ls -la
```

## Exercise

实践造就完美！这是一个强化您对 `ls` 命令理解的动手实验：

- **[Linux ls 命令：内容列表](https://labex.io/zh/labs/linux-linux-ls-command-content-listing-219205)** - 练习使用 `ls` 命令以高效地列出和分析文件和目录内容。您将学习用于详细列表、隐藏文件显示、人类可读大小和排序技术的各种选项，以增强您的命令行技能。

此实验将帮助您在真实场景中应用这些概念，并增强您对 Linux 中目录列表的信心。

## Quiz Question

您将使用什么命令来查看隐藏文件？请用英语回答，注意区分大小写。

## Quiz Answer

ls -a
