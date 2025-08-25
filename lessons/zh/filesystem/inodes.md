---
index: 11
lang: "zh"
title: "Inode"
meta_title: "Inode - 文件系统"
meta_description: "了解 Linux inode、它们的结构以及它们如何管理文件。理解 inode 号并使用 `df -i` 和 `ls -li` 检查 inode 使用情况。开始您的 Linux 之旅！"
meta_keywords: "Linux inode, inode 教程，df -i, ls -li, Linux 文件系统，Linux 初学者，Linux 指南"
---

## Lesson Content

还记得我们的文件系统是由所有实际文件和一个管理这些文件的数据库组成的吗？这个数据库就是 inode 表。

### 什么是 inode？

inode（索引节点）是此表中的一个条目，每个文件都有一个。它描述了文件的一切，例如：

- 文件类型 - 普通文件、目录、字符设备等。
- 所有者
- 组
- 访问权限
- 时间戳 - mtime（文件最后修改时间）、ctime（最后属性更改时间）、atime（最后访问时间）
- 文件的硬链接数量
- 文件大小
- 分配给文件的块数量
- 指向文件数据块的指针 - 最重要！

基本上，inode 存储了文件的一切，除了文件名和文件本身！

### Inode 何时创建？

当文件系统创建时，inode 的空间也会被分配。算法会根据磁盘容量等因素确定您需要多少 inode 空间。您可能在某个时候遇到过磁盘空间不足的错误。inode 也会发生同样的情况（尽管不那么常见）；您可能会用完 inode，因此无法创建更多文件。请记住，数据存储取决于数据和数据库（inode）。

要查看系统上还剩下多少 inode，请使用命令 `df -i`。

### Inode 信息

inode 通过数字标识。当文件创建时，会分配一个 inode 号，并且该号码按顺序分配。但是，您有时可能会注意到，当您创建新文件时，它获得的 inode 号低于其他文件。这是因为一旦 inode 被删除，它们可以被其他文件重用。要查看 inode 号，请运行 `ls -li`：

```bash
pete@icebox:~$ ls -li
140 drwxr-xr-x 2 pete pete 6 Jan 20 20:13 Desktop
141 drwxr-xr-x 2 pete pete 6 Jan 20 20:01 Documents
```

此命令的第一个字段列出了 inode 号。

您还可以使用 `stat` 查看文件的详细信息；它也会告诉您有关 inode 的信息。

```bash
pete@icebox:~$ stat ~/Desktop/
  File: ‘/home/pete/Desktop/’
  Size: 6               Blocks: 0          IO Block: 4096   directory
Device: 806h/2054d      Inode: 140         Links: 2
Access: (0755/drwxr-xr-x)  Uid: ( 1000/   pete)   Gid: ( 1000/   pete)
Access: 2016-01-20 20:13:50.647435982 -0800
Modify: 2016-01-20 20:13:06.191675843 -0800
Change: 2016-01-20 20:13:06.191675843 -0800
 Birth: -
```

### Inode 如何定位文件？

我们知道我们的数据在磁盘上的某个地方。不幸的是，它可能不是按顺序存储的，所以我们必须使用 inode。Inode 指向文件的实际数据块。在典型的文件系统（并非所有文件系统都相同）中，每个 inode 包含 15 个指针。前 12 个指针直接指向数据块。第 13 个指针指向一个包含更多块指针的块，第 14 个指针指向另一个嵌套的指针块，第 15 个指针又指向另一个指针块！我知道这很令人困惑！这样做是为了保持每个 inode 的结构相同，但能够引用不同大小的文件。如果您的文件很小，您可以使用前 12 个直接指针更快地找到它；较大的文件可以通过嵌套的指针找到。无论哪种方式，inode 的结构都是相同的。

## Exercise

熟能生巧！这里有一些动手实验来巩固您对 Linux 文件系统和文件管理的理解：

1. **[在 Linux 中管理文件和目录](https://labex.io/zh/labs/comptia-manage-files-and-directories-in-linux-590835)** - 练习创建、删除、复制和移动文件和目录，并探索创建符号链接和硬链接，同时分析 inode。
2. **[在 Linux 中导航文件系统](https://labex.io/zh/labs/comptia-navigate-the-filesystem-in-linux-590971)** - 学习使用 `pwd`、`cd` 和 `ls` 等基本 shell 命令导航 Linux 文件系统的基本技能。
3. **[在 Linux 中查找文件和命令](https://labex.io/zh/labs/comptia-find-files-and-commands-in-linux-590834)** - 掌握使用 `find`、`locate`、`whereis`、`which` 和 `type` 在 Linux 中查找文件和命令的基本技术。

这些实验将帮助您在实际场景中应用概念，并增强对 Linux 文件系统管理的信心。

## Quiz Question

如何查看系统上还剩下多少 inode？

## Quiz Answer

df -i
