---
index: 14
lang: "zh"
title: "查找"
meta_title: "find 命令 - 命令行"
meta_description: "关于 Linux 中 find 命令的全面指南。学习如何使用 find 命令行按名称、类型等定位文件和目录。使用强大的 linux find 实用程序增强您的文件管理技能。"
meta_keywords: "find 命令行，linux 中的 find 命令，find 命令，find 命令 linux, 命令 linux find, 文件搜索，目录搜索，linux 教程"
---

## Lesson Content

系统中有无数文件，要定位特定文件可能很困难。幸运的是，我们可以使用一个强大的工具来实现这一目标：`find` 命令。这个工具对于高效的文件管理至关重要。

### 使用 Find 命令行

`find 命令行` 的基本语法是 `find [路径] [表达式]`。您必须指定要搜索的目录以及要查找内容的标准。

例如，要在 `/home` 目录及其所有子目录中搜索名为 `puppies.jpg` 的文件，您将使用：

```bash
find /home -name puppies.jpg
```

`find 命令在 linux` 中非常灵活，允许使用许多不同的搜索表达式。

### 按名称和类型搜索

`find 命令` 最常见的用途之一是按文件名搜索。如上所示，`-name` 选项允许您指定要查找的文件的确切名称。

您还可以指定要搜索的项目类型。`-type` 选项用于此目的。例如，如果您想查找目录而不是文件，可以使用 `d`。

```bash
find /home -type d -name MyFolder
```

在此命令中，我们将类型设置为 `d`（代表目录），并搜索名为 `MyFolder` 的项目。要专门搜索常规文件，您应使用 `-type f`。

### 递归搜索

`find 命令 linux` 用户欣赏的一个关键特性是它的递归性。当您指定一个起始目录时，`find` 不仅会查找该单个目录；它会自动搜索其中包含的所有子目录。这使其成为在目录树中的任何位置定位项目的极其彻底的工具。

## Exercise

实践是掌握 `find 命令在 linux` 中的关键。这些动手实验将帮助您巩固对查找文件和目录的理解：

1.  **[Linux find 命令：文件搜索](https://labex.io/zh/labs/linux-linux-find-command-file-searching-219191)** - 此实验介绍了 `find` 命令，这是一个用于根据各种标准搜索和定位文件和目录的多功能实用程序。您将练习使用 `find` 来定位特定文件。
2.  **[发现关键系统资源](https://labex.io/zh/labs/linux-discover-critical-system-resources-388032)** - 学习定位文件和可执行文件的基本 Linux 命令，包括 `find`。您将练习高效地导航文件系统并发现关键系统资源。

这些实验将帮助您在实际场景中应用这些概念，并建立有效使用 `find` 命令的信心。

## Quiz Question

您应该为 `find` 命令指定哪个选项来进行按名称搜索？请仅使用英文选项回答，注意所需的格式（例如，-option）。

## Quiz Answer

-name
