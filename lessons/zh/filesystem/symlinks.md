---
index: 12
lang: "zh"
title: "符号链接"
meta_title: "符号链接 - 文件系统"
meta_description: "探索 Linux 符号链接（软链接）和硬链接。学习如何使用 ln 命令创建它们，使用 ls 命令检查 Linux 中的链接数，并理解 ls 输出中符号链接和硬链接的区别。"
meta_keywords: "Linux 符号链接，硬链接，ln 命令，软链接，ls 符号链接，Linux 链接数，ls 符号链接，ls 链接，Linux 文件系统，Linux 教程"
---

## Lesson Content

当你以详细信息列表显示文件时，会看到很多信息。让我们看一下之前使用 `ls -li` 命令输出的 inode 信息示例：

```plaintext
pete@icebox:~$ ls -li
140 drwxr-xr-x 2 pete pete 6 Jan 20 20:13 Desktop
141 drwxr-xr-x 2 pete pete 6 Jan 20 20:01 Documents
```

我们之前略过了此输出中的第三个字段。这个字段就是链接数（link count）。

### Linux 中的链接数

**Linux 中的链接数**是一个文件拥有的硬链接（hard link）的总数。要理解这意味着什么，我们首先需要讨论什么是链接。在 Linux 中，有两种类型的链接：符号链接（symbolic links，即 symlinks）和硬链接（hard links）。

### 理解符号链接 (Symlinks)

在 Windows 操作系统中，你有快捷方式（shortcuts），它们本质上是指向其他文件的别名。在 Linux 中，等效物是符号链接，也称为软链接或 **symlink**。符号链接是一种特殊类型的文件，它通过名称指向另一个文件或目录。

让我们在实践中看看。我们将创建几个文件，然后创建一个符号链接。

```bash
pete@icebox:~/Desktop$ echo 'myfile' > myfile
pete@icebox:~/Desktop$ echo 'myfile2' > myfile2
pete@icebox:~/Desktop$ echo 'myfile3' > myfile3

pete@icebox:~/Desktop$ ln -s myfile myfilelink
pete@icebox:~/Desktop$ ls -li
total 12
  151 -rw-rw-r-- 1 pete pete 7 Jan 21 21:36 myfile
93401 -rw-rw-r-- 1 pete pete 8 Jan 21 21:36 myfile2
93402 -rw-rw-r-- 1 pete pete 8 Jan 21 21:36 myfile3
93403 lrwxrwxrwx 1 pete pete 6 Jan 21 21:39 myfilelink -> myfile
```

在这里，我们创建了一个名为 `myfilelink` 的符号链接，它指向 `myfile`。当你使用 `ls` 查看一个 `ls symlink` 时，它通过权限字符串开头的 `l` 和指向目标的 `->` 符号被明确标识。请注意，符号链接有自己唯一的 inode 号（93403）。由于符号链接指向文件名而不是 inode，因此它们可以跨越不同的文件系统。

### 理解硬链接 (Hard Links)

另一种链接是硬链接。硬链接创建另一个直接指向原始文件相同 inode 的文件条目。

让我们为 `myfile2` 创建一个硬链接：

```bash
pete@icebox:~/Desktop$ ln myfile2 myhardlink
pete@icebox:~/Desktop$ ls -li
total 16
  151 -rw-rw-r-- 1 pete pete 7 Jan 21 21:36 myfile
93401 -rw-rw-r-- 2 pete pete 8 Jan 21 21:36 myfile2
93402 -rw-rw-r-- 1 pete pete 8 Jan 21 21:36 myfile3
93403 lrwxrwxrwx 1 pete pete 6 Jan 21 21:39 myfilelink -> myfile
93401 -rw-rw-r-- 2 pete pete 8 Jan 21 21:36 myhardlink
```

请注意，`myhardlink` 与 `myfile2` 共享完全相同的 inode 号（93401）。两个文件的链接数也增加到了 2。这是因为现在有两个文件条目指向同一个 inode。如果你修改 `myfile2` 的内容，更改将反映在 `myhardlink` 中，反之亦然。如果你删除了 `myfile2`，该文件的数据仍然可以通过 `myhardlink` 访问。只有当链接数降至零时，inode 及其数据才会被从磁盘中删除。由于硬链接指向单个文件系统内唯一的 inode，因此它们不能跨越不同的文件系统。

### 创建符号链接和硬链接

你可以使用 `ln` 命令创建这两种类型的链接。语法很简单。

要创建符号链接，请使用 `-s` 标志：

```bash
ln -s /path/to/original /path/to/link
```

要创建硬链接，请省略 `-s` 标志：

```bash
ln /path/to/original /path/to/link
```

使用 `ls symlinks` 或常规的 `ls links` 命令并使用 `-l` 选项对于管理和识别这些不同类型的文件至关重要。

## Exercise

熟能生巧！这里有一些实践操作实验，以加强你对文件管理、链接和 inode 的理解：

1.  **[在 Linux 中管理文件和目录](https://labex.io/zh/labs/comptia-manage-files-and-directories-in-linux-590835)** - 练习创建、复制、移动和删除文件和目录，并专门学习符号链接和硬链接，以及如何分析 inode。
2.  **[在 Linux 中导航文件系统](https://labex.io/zh/labs/comptia-navigate-the-filesystem-in-linux-590971)** - 掌握 `pwd`、`cd` 和 `ls` 等基本命令，以高效地在 Linux 文件系统中移动，这是理解文件及其 inode 位置的基础技能。

这些实验将帮助你在真实场景中应用文件管理和链接的概念，并增强你对 Linux 文件系统的信心。

## Quiz Question

用于创建符号链接的命令及其主要选项是什么？你的答案必须是英文且区分大小写。请在命令和选项之间包含空格。

## Quiz Answer

ln -s
