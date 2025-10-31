---
index: 17
lang: "zh"
title: "什么是"
meta_title: "whatis - 命令行"
meta_description: "了解 Linux 中的 whatis 命令。学习 linux whatis 命令如何提供其他命令的单行描述，使其成为浏览命令行的重要工具。"
meta_keywords: "linux 中的 whatis 命令，whatis linux, linux whatis 命令，whatis 命令 linux, linux whatis, 命令行，linux 命令"
---

## Lesson Content

当您探索 Linux 命令行时，会遇到大量的命令。忘记特定命令的作用是很自然的。幸运的是，有一个简单的实用工具可以帮助您。

### 什么是 Linux 中的 whatis 命令

Linux 中的 `whatis` 命令直接从其手册（man）页面显示命令的简洁单行描述。这是一种快速了解命令主要功能的便捷方式，而无需阅读整个 man 页面。将 **linux whatis** 命令视为您终端的快速词典。

### 如何使用 whatis 命令

使用 **whatis command linux** 非常简单。只需键入 `whatis`，然后是您想了解的命令名称。例如，如果您不确定 `cat` 命令，可以运行：

```bash
whatis cat
```

这将返回一个简短的描述，例如“cat - concatenate files and print on the standard output”（cat - 连接文件并打印到标准输出）。

### 理解输出

**linux whatis command** 提供的描述直接来源于命令手册页的 NAME 部分。这确保了信息准确且与系统的文档一致。如果一个命令在不同的部分有多个手册页，`whatis` 可能会为每一页显示一行，帮助您理解其各种上下文。

## Exercise

熟能生巧！虽然 `whatis` 命令没有专门的实验，但了解如何查找有关命令和文件的信息至关重要。以下是一些加强您对在 Linux 中定位命令和文件理解的动手实验：

1. **[Linux which 命令：命令定位](https://labex.io/zh/labs/linux-linux-which-command-command-locating-215210)** - 练习使用 `which` 命令定位可执行文件并了解系统 PATH 中命令的优先级。
2. **[Linux whereis 命令：文件和命令查找](https://labex.io/zh/labs/linux-linux-whereis-command-file-and-command-finding-215211)** - 学习使用 `whereis` 来查找命令的二进制文件、源代码和手册页，加深对命令结构的理解。
3. **[发现关键系统资源](https://labex.io/zh/labs/linux-discover-critical-system-resources-388032)** - 此挑战结合了 `which`、`whereis` 和 `find`，以帮助您有效地导航文件系统并发现重要的系统资源。

这些实验将帮助您在实际场景中应用命令和文件发现的概念，并增强您对基本 Linux 工具的信心。

## Quiz Question

What command can you use to see a small description of a command? Please answer in English, paying attention to lowercase.

## Quiz Answer

whatis
