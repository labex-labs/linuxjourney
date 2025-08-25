---
index: 12
lang: "zh"
title: "符号链接"
meta_title: "符号链接 - 文件系统"
meta_description: "了解 Linux 符号链接和硬链接，包括如何创建和管理它们。通过这份适合初学者的指南，了解它们的区别和用例。"
meta_keywords: "Linux 符号链接，硬链接，ln 命令，符号链接，Linux 文件系统，Linux 教程，Linux 初学者"
---

## Lesson Content

让我们使用之前的一个 inode 信息示例：

```plaintext
pete@icebox:~$ ls -li
140 drwxr-xr-x 2 pete pete 6 Jan 20 20:13 Desktop
141 drwxr-xr-x 2 pete pete 6 Jan 20 20:01 Documents
```

您可能已经注意到，我们一直忽略了 `ls` 命令的第三个字段；该字段是链接计数。链接计数是文件拥有的硬链接总数。嗯，这现在对您来说没有任何意义，所以我们先讨论链接。

### 符号链接

在 Windows 操作系统中，有一种叫做快捷方式的东西。快捷方式只是其他文件的别名。如果您对原始文件进行操作，可能会破坏快捷方式。在 Linux 中，快捷方式的等价物是符号链接（或软链接或 symlinks）。符号链接允许我们通过文件名链接到另一个文件。Linux 中发现的另一种链接是硬链接；这些实际上是另一个带有 inode 链接的文件。让我们从符号链接开始，看看我在实践中是什么意思。

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

您可以看到我创建了一个名为 `myfilelink` 的符号链接，它指向 `myfile`。符号链接由 `->` 表示。请注意我如何获得了一个新的 inode 号；符号链接只是指向文件名的文件。当您修改符号链接时，文件也会被修改。Inode 号对于文件系统是唯一的；您不能在单个文件系统中拥有两个相同的 inode 号，这意味着您不能通过其 inode 号引用不同文件系统中的文件。但是，如果您使用符号链接，它们不使用 inode 号；它们使用文件名，因此可以在不同的文件系统之间引用。

### 硬链接

让我们看一个硬链接的例子：

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

硬链接只是创建另一个文件，该文件链接到相同的 inode。因此，如果我修改 `myfile2` 或 `myhardlink` 的内容，更改将在两者上都可见。但是，如果我删除了 `myfile2`，文件仍然可以通过 `myhardlink` 访问。这就是 `ls` 命令中的链接计数发挥作用的地方。链接计数是 inode 拥有的硬链接数量。当您删除文件时，它将减少该链接计数。只有当指向 inode 的所有硬链接都被删除时，inode 才会被删除。当您创建文件时，其链接计数为 1，因为它是唯一指向该 inode 的文件。与符号链接不同，硬链接不跨文件系统，因为 inode 对于文件系统是唯一的。

### 创建符号链接

```bash
ln -s myfile mylink
```

要创建符号链接，您使用 `ln` 命令，带 `-s` 表示符号链接，然后指定目标文件和链接名称。

### 创建硬链接

```bash
ln somefile somelink
```

类似于符号链接的创建，只是这次您省略了 `-s`。

## Exercise

熟能生巧！这里有一些动手实验，以巩固您对文件管理、链接和 inode 的理解：

1. **[在 Linux 中管理文件和目录](https://labex.io/zh/labs/comptia-manage-files-and-directories-in-linux-590835)** - 练习创建、复制、移动和删除文件和目录，并特别学习符号链接和硬链接，以及如何分析 inode。
2. **[在 Linux 中导航文件系统](https://labex.io/zh/labs/comptia-navigate-the-filesystem-in-linux-590971)** - 掌握 `pwd`、`cd` 和 `ls` 等基本命令，以高效地在 Linux 文件系统中移动，这是理解文件及其 inode 所在位置的基础技能。

这些实验将帮助您在实际场景中应用文件管理和链接的概念，并增强您对 Linux 文件系统的信心。

## Quiz Question

用于创建符号链接的命令是什么？

## Quiz Answer

ln -s
