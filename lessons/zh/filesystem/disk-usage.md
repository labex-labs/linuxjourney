---
lang: "zh"
title: "磁盘使用情况"
meta_title: "磁盘使用情况 - 文件系统"
meta_description: "学习如何使用 df 和 du 命令在 Linux 中检查磁盘使用情况和空闲空间。了解它们的区别以及何时使用。Linux 磁盘管理教程。"
meta_keywords: "df 命令，du 命令，Linux 磁盘使用，检查空闲空间，Linux 教程，Linux 初学者，磁盘管理，Linux 指南"
---

## Lesson Content

有几种工具可以用来查看磁盘利用率：

```bash
pete@icebox:~$ df -h
Filesystem     1K-blocks    Used Available Use% Mounted on
/dev/sda1       6.2G  2.3G  3.6G  40% /
```

`df` 命令显示当前已挂载文件系统的利用率。`-h` 标志提供人类可读的格式。你可以看到设备是什么，以及使用了多少容量和可用容量。

假设你的磁盘快满了，你想知道哪些文件或目录占用了这些空间；为此，你可以使用 **du** 命令。

```bash
du -h
```

这会显示你当前所在目录的磁盘使用情况。你可以使用 `du -h /` 查看根目录，但这可能会有点混乱。

这两个命令的语法如此相似，以至于很难记住该使用哪一个。要检查你的**磁盘**有多少**空闲空间**，请使用 `df`。要检查**磁盘使用情况**，请使用 `du`。

## Exercise

使用 `du` 和 `df` 查看你的磁盘使用情况和空闲空间。

## Quiz Question

哪个命令用于显示磁盘上有多少空闲空间？

## Quiz Answer

df
