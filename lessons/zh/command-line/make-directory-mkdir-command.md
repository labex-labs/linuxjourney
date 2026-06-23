---
index: 12
lang: "zh"
title: "mkdir（创建目录）"
meta_title: "mkdir（创建目录）- 命令行"
meta_description: "通过示例学习 Linux mkdir 命令，包括创建单个目录、多个目录、嵌套父目录以及设置权限。"
meta_keywords: "mkdir 命令, linux mkdir, 创建目录 linux, 创建文件夹 linux, mkdir -p, mkdir -m, 创建文件夹"
---

## Lesson Content

在处理文件时，您需要将它们组织到目录中。完成此任务的主要工具是 `mkdir` 命令，代表“make directory”（创建目录）。

基本语法是：

```bash
mkdir [OPTIONS] DIRECTORY...
```

### 创建单个目录

`mkdir` 最基本的用法是创建一个新的目录。如果该目录尚不存在，此命令将在您当前的位置创建它。

```bash
$ mkdir documents
```

### 创建多个目录

您也可以一次创建多个目录，只需用空格分隔它们的名称。这是快速设置多个文件夹的高效方法。

```bash
$ mkdir books paintings
```

### 创建嵌套目录

有时您需要同时创建一个目录及其父目录。`-p` 选项非常适合此用途。它可以防止当父目录不存在时出现错误。

```bash
$ mkdir -p books/hemingway/favorites
```

此命令会在目录不存在时创建 `books`、`hemingway` 和 `favorites`。

### 设置目录权限

使用 `-m` 选项可以在创建目录时设置权限。

```bash
$ mkdir -m 755 public
```

您稍后会学习更多关于权限的内容，但此示例创建了一个目录，所有者可以写入，其他用户可以读取和进入。

### 常用 mkdir 选项

- `-p`：按需创建父目录。
- `-m MODE`：为新目录设置权限。
- `-v`：为每个创建的目录打印一条消息。

示例：

```bash
$ mkdir -pv projects/app/src
mkdir: created directory 'projects'
mkdir: created directory 'projects/app'
mkdir: created directory 'projects/app/src'
```

### 常见问题

**为什么 mkdir 会提示“File exists”？** 说明已有同名文件或目录。使用 `ls` 查看它。

**如何创建嵌套目录？** 使用 `mkdir -p parent/child/grandchild`。

**mkdir 能创建文件吗？** 不能。使用 `touch` 创建空文件。

## Exercise

熟能生巧！以下是一些动手实验，帮助您巩固目录创建和管理的理解：

1. **[Linux mkdir 命令：目录创建](https://labex.io/zh/labs/linux-linux-mkdir-command-directory-creating-209739)** - 学习如何在 Linux 中使用 `mkdir` 命令创建目录、设置权限并组织文件系统。本实验涵盖基础和高级用法，包括创建嵌套目录。
2. **[搭建新项目结构](https://labex.io/zh/labs/linux-setting-up-a-new-project-structure-387859)** - 通过创建特定项目结构并使用 `mkdir` 和 `cd` 等基本命令导航，练习您的 Linux 目录管理技能。

这些实验将帮助您在实际场景中应用概念，增强创建和组织 Linux 目录的信心。

## Quiz Question

用什么命令来创建目录？请仅用小写英文命令回答。

## Quiz Answer

mkdir
