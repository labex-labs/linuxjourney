---
index: 14
lang: "zh"
title: "find 命令"
meta_title: "find 命令 - 命令行教程"
meta_description: "通过示例学习 Linux 中的 find 命令，按名称、类型、大小、修改时间搜索文件，并对匹配文件执行操作。"
meta_keywords: "linux find 命令, find 命令, linux 查找文件, 按名称查找, 按类型查找, 按大小查找, 按修改时间查找, find exec"
---

## Lesson Content

系统中有无数文件，定位特定文件可能很困难。`find` 命令通过名称、类型、大小和修改时间等条件搜索目录树。

### 使用 find 命令

基本语法是：

```bash
find [PATH] [EXPRESSION]
```

你需要指定搜索的目录和查找的条件。

例如，要在 `/home` 目录及其所有子目录中查找名为 `puppies.jpg` 的文件，可以使用：

```bash
$ find /home -name puppies.jpg
```

搜索默认是递归的，因此 `find /home` 会查找 `/home` 及其子目录。

### 按名称和类型搜索

`find` 最常用的功能之一是按文件名搜索。`-name` 选项用于精确匹配名称或使用 shell 风格的模式匹配。

```bash
$ find . -name "*.txt"
```

你还可以指定搜索的项目类型。`-type` 选项用于此目的。例如，如果你想查找目录而不是文件，可以使用 `d`。

```bash
$ find /home -type d -name MyFolder
```

在此命令中，我们将类型设置为 `d` 表示目录，并查找名为 `MyFolder` 的项目。要专门查找普通文件，可以使用 `-type f`。

### 按大小和时间搜索

你可以按文件大小搜索：

```bash
$ find . -type f -size +10M
$ find . -type f -size -1k
```

第一个命令查找大于 10 兆字节的文件。第二个查找小于 1 千字节的文件。

你也可以按修改时间搜索：

```bash
$ find . -type f -mtime -7
$ find . -type f -mtime +30
```

`-mtime -7` 表示最近 7 天内修改过。`-mtime +30` 表示 30 天前修改的。

### 对结果执行操作

默认情况下，`find` 会打印匹配的路径。你可以添加操作，如 `-print`、`-delete` 或 `-exec`。

显式打印匹配项：

```bash
$ find . -name "*.log" -print
```

对每个匹配项运行 `ls -l`：

```bash
$ find . -name "*.log" -exec ls -l {} \;
```

`{}` 占位符会被每个匹配路径替换。转义的分号表示命令结束。

使用破坏性操作如 `-delete` 时要小心。先运行不带 `-delete` 的相同搜索以确认匹配项。

### 常用 find 选项

- `-name PATTERN`：按文件名匹配。
- `-iname PATTERN`：按文件名匹配，忽略大小写。
- `-type f`：匹配普通文件。
- `-type d`：匹配目录。
- `-size +10M`：匹配大于 10 兆字节的文件。
- `-mtime -7`：匹配最近 7 天内修改的文件。
- `-maxdepth N`：限制 `find` 搜索的深度。

### 常见问题

**为什么 find 显示“Permission denied”？** 你的用户无法读取某些目录。请缩小搜索路径或使用合适的权限。

**为什么要给像 "*.txt" 这样的模式加引号？** 加引号可以防止 shell 在 `find` 接收之前扩展通配符。

**find 是递归搜索吗？** 是的，默认会搜索子目录。

## Exercise

实践是掌握 `find` 命令的关键。这些动手实验将帮助你巩固查找文件和目录的理解：

1. **[Linux find 命令：文件搜索](https://labex.io/zh/labs/linux-linux-find-command-file-searching-219191)** - 本实验介绍 `find` 命令，这是一款功能强大的工具，用于根据各种条件搜索和定位文件及目录。你将练习使用 `find` 定位特定文件。
2. **[发现关键系统资源](https://labex.io/zh/labs/linux-discover-critical-system-resources-388032)** - 学习定位文件和可执行文件的基本 Linux 命令，包括 `find`。你将练习高效浏览文件系统并发现关键系统资源。

这些实验将帮助你在实际场景中应用概念，增强使用 `find` 命令的信心。

## Quiz Question

使用 `find` 命令按名称搜索时应指定哪个选项？请仅使用英文选项回答，注意格式（例如 -option）。

## Quiz Answer

-name
