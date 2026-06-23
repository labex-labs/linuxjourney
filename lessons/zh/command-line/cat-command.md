---
index: 7
lang: "zh"
title: "cat 命令"
meta_title: "cat 命令 - 命令行教程"
meta_description: "通过示例学习 Linux cat 命令，用于查看文件、连接文件、给行编号、创建文件以及安全使用重定向。"
meta_keywords: "linux cat 命令, cat 命令, 查看文件 linux, 连接文件, cat -n, cat -b, cat 重定向, linux cat"
---

## Lesson Content

学习了如何浏览文件系统后，下一步是查看文件内容。一个基础且多功能的工具是 `cat` 命令。`cat` 是 "concatenate"（连接）的缩写，暗示了它能够将文件链接在一起的功能。

### 查看文件内容

`cat` 命令最基本的用法是直接在终端显示单个文件的内容。

```bash
$ cat myfile.txt
```

该命令会将 `myfile.txt` 的全部内容打印到屏幕上。虽然这非常适合查看简短的配置文件或文本片段，但对于大文件来说并不理想，因为文本会快速滚动。我们将在后续课程中介绍更适合查看大文件的工具。

### 连接文件

顾名思义，`cat` 可以将多个文件连接起来并显示它们的合并输出。它按照提供的顺序读取文件并依次打印。

```bash
$ cat dogfile birdfile
```

该命令会先显示 `dogfile` 的内容，紧接着显示 `birdfile` 的内容。

要将合并的输出保存到新文件中，可以使用重定向：

```bash
$ cat dogfile birdfile > animals
```

### 使用重定向创建文件

你也可以使用 `cat` 和输出重定向操作符（`>`）来创建新文件。这是直接从终端写入文本到文件的快捷方式。

```bash
$ cat > newfile.txt
```

运行该命令后，你可以输入文本。在新的一行按 `Ctrl+D` 保存并退出。这将创建包含你输入文本的 `newfile.txt`。请注意，使用 `>` 操作符会完全覆盖已有文件。

如果想追加内容而不是覆盖，使用 `>>`。

```bash
$ cat >> notes.txt
```

### 常用 cat 命令选项

`cat` 命令有多个选项可以改变其行为。

- `-n`：为所有输出行编号，从 1 开始。
- `-b`：只为非空输出行编号。
- `-s`：将多个空行压缩为一行空行。
- `-A`：显示不可打印字符、制表符和行尾符。

示例：

```bash
$ cat -n script.sh
$ cat -b notes.txt
$ cat -s messy.txt
```

### 何时不使用 cat

`cat` 适合短文件。对于长文件，使用 `less`，这样你可以滚动、搜索并退出，而不会让终端内容泛滥。

```bash
$ less /var/log/syslog
```

### 常见问题

**cat 是什么缩写？** 它是 concatenate（连接）的缩写。

**cat 能编辑文件吗？** 不能交互式编辑。它可以通过重定向创建或覆盖文件，但编辑文件最好用文本编辑器。

**`>` 和 `>>` 有什么区别？** `>` 会覆盖文件，`>>` 会追加到文件末尾。

## Exercise

熟能生巧！以下是一些动手实验，帮助你巩固查看文件内容的理解：

1. **[Linux cat 命令：文件连接](https://labex.io/zh/labs/linux-linux-cat-command-file-concatenating-210986)** - 学习 `cat` 命令用于查看、连接和操作文本文件，提升命令行处理文本文件的效率。
2. **[在 Linux 中查看日志和配置文件](https://labex.io/zh/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - 练习使用 `cat` 等命令高效查看和浏览文本文件，包括系统日志和配置文件，以提取关键信息。

这些实验将帮助你在实际场景中应用所学概念，增强 Linux 文件内容查看的信心。

## Quiz Question

在命令行中用于显示文件内容的命令是什么？（注意：你的答案应为一个小写的英文单词。）

## Quiz Answer

cat
