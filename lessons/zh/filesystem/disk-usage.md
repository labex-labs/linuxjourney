---
index: 9
lang: "zh"
title: "磁盘使用情况"
meta_title: "磁盘使用情况 - 文件系统"
meta_description: "学习使用 df 和 du 命令检查 Linux 磁盘使用情况和可用空间。本指南涵盖如何分析磁盘空间，包括使用 df -i linux 检查 inode 使用情况，以及查找哪些文件占用了空间。"
meta_keywords: "df 命令，du 命令，Linux 磁盘使用情况，检查可用空间，df -i linux, 磁盘管理，Linux 教程，磁盘利用率，文件系统使用"
---

## Lesson Content

管理磁盘空间是任何 Linux 用户或管理员的基本任务。为此，有两个基本命令是 `df` 和 `du`。让我们探索如何有效地使用它们来监控您的磁盘利用率。

### 使用 df 检查文件系统空间

`df`（disk free，磁盘空闲）命令报告当前挂载的文件系统上已用和可用的磁盘空间量。它提供了存储空间的高级概览。

要以人类可读的格式（例如 GB、MB、KB）获取报告，请使用 `-h` 标志：

```bash
pete@icebox:~$ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       6.2G  2.3G  3.6G  40% /
```

此输出显示了文件系统设备、总大小、已用空间、可用空间、使用百分比以及挂载点。

### 分析 Inode 使用情况

除了块空间外，文件系统还使用 inode 来存储有关文件的元数据（如权限、所有权和位置）。在极少数情况下，即使您有空闲磁盘空间，也可能会耗尽 inode。要检查 inode 使用情况，您可以使用 `df -i` 命令。在 Linux 中运行 `df -i` 可以清楚地了解 inode 分配情况。

```bash
pete@icebox:~$ df -i
Filesystem      Inodes  IUsed   IFree IUse% Mounted on
/dev/sda1      4128768 128768 4000000    4% /
```

### 使用 du 总结目录使用情况

当您发现磁盘即将变满时，您需要确定哪些文件或目录占用了最多的空间。对于这项任务，`du`（disk usage，磁盘使用量）命令是完美的工具。

在没有参数的情况下运行 `du` 会显示当前位置中每个子目录的磁盘使用情况。使用 `-h` 标志可提供人类可读的摘要：

```bash
du -h
```

您也可以指定一个路径，例如 `du -h /home/pete`，来分析特定目录。在根目录上运行它 (`du -h /`) 可能会产生大量输出，因此最好检查您怀疑较大的特定目录。

### df 与 du 快速总结

`df` 和 `du` 的语法非常相似，很容易混淆。这里有一个简单的方法来记住它们的区别：

- 使用 `df` 检查文件系统上有多少**d**isk is **f**ree（磁盘空闲）。
- 使用 `du` 检查特定文件和目录的**d**isk **u**sage（磁盘使用量）。

## Exercise

实践造就完美！以下是一些实践操作实验，以加强您对 Linux 中磁盘空间管理和利用率的理解：

1. **[管理 Linux 分区和文件系统](https://labex.io/zh/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - 练习创建、格式化和挂载文件系统，这些是 `df` 和 `du` 报告的基础结构。
2. **[在 Linux 中创建和激活交换文件](https://labex.io/zh/labs/comptia-create-and-activate-a-swap-file-in-linux-590858)** - 学习管理磁盘上的虚拟内存，这是影响磁盘空间的系统资源管理的关键方面。

这些实验将帮助您在实际场景中应用这些概念，并建立管理磁盘资源的信心。

## Quiz Question

哪个命令用于显示磁盘上有多少可用空间？请用小写英文字母回答。

## Quiz Answer

df
