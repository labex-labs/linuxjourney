---
index: 12
lang: "zh"
title: "mkdir (创建目录)"
meta_title: "mkdir (创建目录) - 命令行"
meta_description: "学习如何在 Linux 中使用 mkdir 命令创建新目录。本指南涵盖创建文件夹的 Linux 命令，包括如何从命令行创建多个目录和父目录。"
meta_keywords: "创建目录 linux, mkdir 命令 linux, 在 linux 中创建目录，命令行创建目录，创建文件夹 linux 命令，mkdir, 创建目录，linux"
---

## Lesson Content

在使用文件时，您需要将它们组织到目录中。完成此任务的主要工具是 `mkdir` 命令，它是“Make Directory”（创建目录）的缩写。此命令允许您直接从终端或**命令提示符**中**在 Linux 中创建目录**。

### 创建单个目录

**Linux 中的 mkdir 命令**最基本的用法是创建一个新的单个目录。如果该目录尚不存在，此命令将在您当前的位置创建它。例如，要创建一个名为 `documents` 的目录：

```bash
mkdir documents
```

### 创建多个目录

您也可以通过列出目录名称（用空格分隔）来一次创建多个目录。这是快速设置多个文件夹的有效方法。

```bash
mkdir books paintings
```

### 创建嵌套目录

有时您需要同时创建目录及其父目录。`-p`（父目录）选项非常适合此目的。这个**创建文件夹 Linux 命令**的强大功能可以防止在父目录不存在时出错。例如，要在 `books` 内部的 `hemmingway` 内部创建一个名为 `favorites` 的目录：

```bash
mkdir -p books/hemmingway/favorites
```

如果它们尚不存在，此单个命令将创建 `books`、`hemmingway` 和 `favorites`，展示了当您需要**在 Linux 中创建目录**时的关键能力。

## Exercise

实践造就完美！以下是一些实践实验，以加强您对目录创建和管理的理解：

1. **[Linux mkdir 命令：目录创建](https://labex.io/zh/labs/linux-linux-mkdir-command-directory-creating-209739)** - 学习如何在 Linux 中使用 `mkdir` 命令创建目录、设置权限以及组织文件系统。此实验涵盖了基本和高级用法，包括创建嵌套目录。
2. **[设置新的项目结构](https://labex.io/zh/labs/linux-setting-up-a-new-project-structure-387859)** - 通过创建特定的项目结构并使用 `mkdir` 和 `cd` 等基本命令在其中导航，来练习您的 Linux 目录管理技能。

这些实验将帮助您在实际场景中应用这些概念，并增强您在 Linux 中创建和组织目录的信心。

## Quiz Question

使用什么命令来创建目录？请仅使用小写英文命令回答。

## Quiz Answer

mkdir
