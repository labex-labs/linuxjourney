---
index: 5
lang: "zh"
title: "touch 命令"
meta_title: "touch 命令 - 命令行教程"
meta_description: "通过示例学习 Linux touch 命令，包括创建空文件、更新时间戳、设置日期、使用参考文件以及避免覆盖等用法。"
meta_keywords: "linux touch 命令, touch 命令, linux 创建文件, 更新时间戳 linux, touch -d, touch -r, touch -c"
---

## Lesson Content

`touch` 命令是类 Unix 操作系统上的标准工具。虽然它的主要用途是更改文件的时间戳，但它也常用于创建新的空文件。

基本语法是：

```bash
touch [OPTIONS] FILE...
```

### 创建新文件

创建空文件最简单的方法是使用 `touch` 后跟文件名。如果文件不存在，`touch` 会创建它。

```bash
$ touch mysuperduperfile
```

运行此命令后，当前目录中会出现一个名为 `mysuperduperfile` 的新空文件。你也可以通过列出多个文件名一次创建多个文件。

```bash
$ touch file1.txt file2.txt file3.log
```

这在搭建项目结构或在添加内容之前创建占位文件时非常有用。

### 更新文件时间戳

`touch` 的原始功能是更新文件或目录的访问和修改时间戳。如果你对已存在的文件使用 `touch`，它会将时间戳更新为当前时间。

你可以通过使用 `ls -l` 查看文件时间戳，运行 `touch` 后再查看来验证这一点。

```bash
# Check the original timestamp
$ ls -l mysuperduperfile

# Update the timestamp
$ touch mysuperduperfile

# Check the new timestamp
$ ls -l mysuperduperfile
```

### 高级时间戳控制

`touch` 命令还提供了更精确的时间戳操作选项。

使用 `-r` 选项指定参考文件，将一个文件的时间戳复制到另一个文件。

```bash
$ touch -r file1.txt file2.txt
```

使用 `-d` 设置具体的日期和时间：

```bash
$ touch -d "2026-06-23 12:30:00" mysuperduperfile
```

当你只想更新已存在的文件时，使用 `-c`。带上 `-c`，`touch` 不会创建缺失的文件。

```bash
$ touch -c existing-file.txt
```

### 常用 touch 选项

- `-a`：只更改访问时间。
- `-m`：只更改修改时间。
- `-c`：如果文件不存在，则不创建。
- `-d "DATE"`：使用指定的日期字符串。
- `-r FILE`：使用另一个文件的时间戳作为参考。
- `-t STAMP`：使用紧凑的数字格式时间戳。

例如，这条命令只更改修改时间：

```bash
$ touch -m notes.txt
```

### 常见问题

**touch 会向文件添加文本吗？** 不会。`touch` 创建空文件或更新时间戳。要添加文本，请使用编辑器、`echo` 或 `cat`。

**touch 会覆盖已有文件吗？** 不会。它只更新时间戳，不会替换文件内容。

**为什么在脚本中使用 touch？** 这是确保文件存在或标记某个任务发生时间的快捷方法。

## Exercise

熟能生巧！以下是一些动手实验，帮助你巩固创建和管理文件系统对象的理解：

1. **[Linux mkdir 命令：目录创建](https://labex.io/zh/labs/linux-linux-mkdir-command-directory-creating-209739)** - 学习如何使用 Linux 的 `mkdir` 命令创建目录、设置权限并组织文件系统。这将帮助你理解文件系统中新建项目的更广泛概念。
2. **[搭建新项目结构](https://labex.io/zh/labs/linux-setting-up-a-new-project-structure-387859)** - 通过创建特定的项目结构并使用 `mkdir` 和 `cd` 等基本命令进行导航，练习你的 Linux 目录管理技能。

这些实验将帮助你在实际场景中应用文件系统创建和组织的概念，并增强使用 Linux 命令的信心。

## Quiz Question

如何创建一个名为 `myfile` 的文件？请仅使用英文命令回答，注意大小写。

## Quiz Answer

touch myfile
