---
index: 8
lang: "zh"
title: "交换"
meta_title: "交换 - 文件系统"
meta_description: "了解 Linux 交换空间的工作原理，以及如何创建和管理交换分区。通过本指南优化系统的内存使用！"
meta_keywords: "Linux 交换，mkswap, swapon, swapoff, /etc/fstab, 虚拟内存，Linux 入门，Linux 教程"
---

## Lesson Content

在我们之前的示例中，我向您展示了如何查看分区表。让我们回顾一下那个示例，更具体地说，是这一行：

```
Number  Start   End     Size    Type      File system     Flags
 5      6861MB  7380MB  519MB   logical   linux-swap(v1)
```

这个交换分区是什么？交换（Swap）是我们用来为系统分配虚拟内存的。如果您的内存不足，系统会使用此分区将空闲进程的内存片段“交换”到磁盘上，这样您就不会因为内存不足而运行缓慢。

### 使用分区作为交换空间

假设我们想将分区 `/dev/sdb2` 设置为用作交换空间。

1. 首先，确保分区上没有任何数据。
2. 运行：`mkswap /dev/sdb2` 来初始化交换区域。
3. 运行：`swapon /dev/sdb2`。这将启用交换设备。
4. 如果您希望交换分区在启动时保持活动状态，则需要在 `/etc/fstab` 文件中添加一个条目。`sw` 是您将使用的文件系统类型。
5. 要移除交换：`swapoff /dev/sdb2`。

通常，您应该分配大约两倍于您内存大小的交换空间。然而，如今的现代系统通常足够强大，并且已经拥有足够的内存了。

## Exercise

熟能生巧！以下是一些动手实验，以加强您对 Linux 交换空间和虚拟内存管理的理解：

1. **[在 Linux 中创建和激活交换文件](https://labex.io/zh/labs/comptia-create-and-activate-a-swap-file-in-linux-590858)** - 练习创建和激活交换文件，这是管理系统虚拟内存的一项关键技能。

此实验将帮助您在实际场景中应用交换分区的概念，并建立对系统资源管理的信心。

## Quiz Question

用于在设备上启用交换空间的命令是什么？

## Quiz Answer

swapon
