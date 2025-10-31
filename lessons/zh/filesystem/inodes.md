---
index: 11
lang: "zh"
title: "索引节点"
meta_title: "索引节点 - 文件系统"
meta_description: "探索 Linux 索引节点（inode）的概念。了解什么是 i 节点，Linux 中的 inode 如何管理文件元数据，以及如何使用 `df -i` 和 `ls -li` 检查 inode 使用情况。"
meta_keywords: "linux inode, linux 索引节点，i 节点，inode, inode linux, 索引节点号，文件系统，df -i, ls -li, stat"
---

## Lesson Content

还记得我们的文件系统由所有实际文件和一个管理它们的数据库组成吗？这个数据库被称为 inode 表，是`inode in linux`工作原理的基础部分。

### 什么是 Linux Inode

Inode（索引节点，index node 的缩写）是该表中的一个条目。每个文件和目录都有自己的`inode`。它描述了关于文件的所有信息，例如：

- 文件类型（例如，常规文件、目录、字符设备）
- 所有者
- 组
- 访问权限
- 时间戳：mtime（最后修改时间）、ctime（最后属性更改时间）、atime（最后访问时间）
- 对该文件的硬链接数
- 文件大小
- 分配给该文件的块数
- 指向文件数据块的指针（最重要！）

本质上，一个`i node`存储了关于文件的所有元数据，除了其名称和实际内容。

### Inode 的创建和分配

创建文件系统时，也会分配 inode 的空间。算法会根据磁盘的容量和其他因素确定您需要的`inode`空间量。您可能以前见过“磁盘空间不足”的错误。inode 也可能发生这种情况，尽管不太常见。如果 inode 用尽，您将无法创建新文件。数据存储同时依赖于数据块和数据库（`inode`表）。

要查看系统上还剩多少 inode，请使用`df -i`命令。对于管理大量小文件的系统管理员来说，这是一个至关重要的检查。

### 查看 Inode 信息

每个`linux inode`都由一个唯一的数字标识。创建文件时，会为其分配一个 inode 编号，通常是连续的。但是，您可能会注意到一个新文件获得了比旧文件更小的 inode 编号。这是因为被删除的 inode 编号可以被新文件重用。要查看 inode 编号，请运行`ls -li`：

```bash
pete@icebox:~$ ls -li
140 drwxr-xr-x 2 pete pete 6 Jan 20 20:13 Desktop
141 drwxr-xr-x 2 pete pete 6 Jan 20 20:01 Documents
```

该命令输出中的第一个字段就是 inode 编号。您还可以使用`stat`命令查看文件`i node`的详细信息：

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

### I-Node 如何指向数据

我们知道数据存储在磁盘上，但它可能不是在一个连续的块中。这就是`inode linux`结构变得至关重要的地方。Inode 指向文件的实际数据块。在典型文件系统中（尽管实现各不相同），每个 inode 包含 15 个指针。前 12 个指针直接指向数据块。第 13 个指针指向一个包含更多指针的块。第 14 和第 15 个指针指向更深层次的指针块。这可能看起来很复杂，但这种结构允许`i node`保持固定大小，同时能够引用不同大小的文件。小文件可以使用直接指针快速访问，而大文件则通过嵌套指针定位。

## Exercise

熟能生巧！这里有一些动手实验，以加强您对 Linux 文件系统和文件管理的理解：

1. **[在 Linux 中管理文件和目录](https://labex.io/zh/labs/comptia-manage-files-and-directories-in-linux-590835)** - 练习创建、删除、复制和移动文件和目录，并探索创建符号链接和硬链接，同时分析 inode。
2. **[在 Linux 中导航文件系统](https://labex.io/zh/labs/comptia-navigate-the-filesystem-in-linux-590971)** - 学习使用`pwd`、`cd`和`ls`等基本 shell 命令来导航 Linux 文件系统的基本技能。
3. **[在 Linux 中查找文件和命令](https://labex.io/zh/labs/comptia-find-files-and-commands-in-linux-590834)** - 掌握使用`find`、`locate`、`whereis`、`which`和`type`在 Linux 中定位文件和命令的基本技术。

这些实验将帮助您在实际场景中应用这些概念，并建立对 Linux 文件系统管理的信心。

## Quiz Question

如何查看系统上还剩下多少 inode？（请用英语回答，注意区分大小写。）

## Quiz Answer

df -i
