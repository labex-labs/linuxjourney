---
index: 9
lang: "zh"
title: "磁盘使用"
meta_title: "磁盘使用 - 文件系统"
meta_description: "了解如何使用 df 和 du 命令在 Linux 中检查磁盘使用情况和可用空间。了解它们的区别以及何时使用。Linux 磁盘管理教程。"
meta_keywords: "df 命令，du 命令，Linux 磁盘使用，检查可用空间，Linux 教程，Linux 初学者，磁盘管理，Linux 指南"
---

## Lesson Content

您可以使用一些工具来查看磁盘利用率：

```bash
pete@icebox:~$ df -h
Filesystem     1K-blocks    Used Available Use% Mounted on
/dev/sda1       6.2G  2.3G  3.6G  40% /
```

`df` 命令显示当前挂载文件系统的利用率。`-h` 标志以人类可读的格式显示。您可以查看设备是什么以及使用了多少容量和可用容量。

假设您的磁盘快满了，您想知道哪些文件或目录占用了这些空间；为此，您可以使用 **du** 命令。

```bash
du -h
```

这显示了您当前所在目录的磁盘使用情况。您可以使用 `du -h /` 查看根目录，但这可能会有点混乱。

这两个命令的语法如此相似，以至于很难记住使用哪一个。要检查您的**磁盘**有多少**空闲**空间，请使用 `df`。要检查**磁盘使用情况**，请使用 `du`。

## Exercise

熟能生巧！以下是一些动手实验，以加强您对 Linux 中磁盘空间管理和利用的理解：

1. **[管理 Linux 分区和文件系统](https://labex.io/zh/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - 练习创建、格式化和挂载文件系统，这些是 `df` 和 `du` 报告的基础结构。
2. **[在 Linux 中创建和激活交换文件](https://labex.io/zh/labs/comptia-create-and-activate-a-swap-file-in-linux-590858)** - 学习管理磁盘上的虚拟内存，这是影响磁盘空间系统资源管理的关键方面。

这些实验将帮助您在实际场景中应用概念，并增强管理磁盘资源的信心。

## Quiz Question

哪个命令用于显示磁盘上的空闲空间？

## Quiz Answer

df
