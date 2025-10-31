---
index: 7
lang: "zh"
title: "猫"
meta_title: "cat 命令 - 命令行"
meta_description: "掌握 Linux cat 命令以查看、创建和连接文件。本指南涵盖基本用法、常用选项以及如何将 linux cat 与重定向（如 linux cat >）一起使用。"
meta_keywords: "linux cat 命令，cat linux, cat 手册 linux, linux cat >, 查看文件内容，连接文件，linux 命令，命令行"
---

## Lesson Content

学习了文件系统导航后，下一步是查看文件内容。一个基本且多功能的工具是`linux cat command`。`cat`的名称是“concatenate”（连接）的缩写，这暗示了它将文件链接在一起的能力。

### 查看文件内容

`cat`命令最基本的使用方法是将单个文件的内容直接显示在终端中。

```bash
cat myfile.txt
```

此命令会将`myfile.txt`的全部内容打印到屏幕上。虽然这对于简短的配置文件或文本片段非常理想，但对于查看大文件来说并不理想，因为文本会滚动得非常快。我们将在后续课程中介绍更适合大文件的工具。

### 连接文件

顾名思义，`cat`可以组合或连接多个文件，并显示它们的组合输出。`cat linux`实用程序按提供的顺序读取文件并按顺序打印它们。

```bash
cat dogfile birdfile
```

此命令将首先显示`dogfile`的内容，紧接着是`birdfile`的内容。

### 使用重定向创建文件

您还可以将`cat`与输出重定向运算符（`>`）一起使用来创建新文件。`linux cat >`组合是一种直接从终端向文件中写入文本的快速方法。

```bash
cat > newfile.txt
```

运行此命令后，您可以输入文本。在新的一行上按`Ctrl+D`保存并退出。这将使用您输入的内容创建`newfile.txt`。请注意，对现有文件使用`>`会完全覆盖它。

### 常见的 cat 命令选项

`cat`命令有一些选项可以修改其行为。以下是两个常见的选项：

- `-n`: 此选项对所有输出行进行编号，从 1 开始。
- `-b`: 此选项仅对非空输出行进行编号。

有关功能的完整列表，您可以随时通过在终端中输入`man cat`来查阅`cat manual linux`页面。

## Exercise

实践造就完美！以下是一些实践操作，以加强您对查看文件内容的理解：

1. **[Linux cat 命令：文件连接](https://labex.io/zh/labs/linux-linux-cat-command-file-concatenating-210986)** - 学习使用`cat`命令来查看、连接和操作文本文件，增强您在命令行中高效处理文本文件的技能。
2. **[在 Linux 中查看日志和配置文件](https://labex.io/zh/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - 练习使用`cat`等命令来高效查看和导航文本文件，包括系统日志和配置文件，以提取关键信息。

这些实验将帮助您在实际场景中应用这些概念，并建立在 Linux 中查看文件内容方面的信心。

## Quiz Question

在命令行上用于显示文件内容的是哪个命令？（注意：您的答案应为单个小写英文字符串。）

## Quiz Answer

cat
