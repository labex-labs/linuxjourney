---
lang: "zh"
title: "swap"
description: "了解 Linux swap 空间、其工作原理以及如何创建和管理 swap 分区。通过本指南优化您的系统内存使用！"
keywords: "Linux swap, mkswap, swapon, swapoff, /etc/fstab, 虚拟内存，Linux 初学者，Linux 教程"
---

## Lesson Content

在之前的例子中，我向您展示了如何查看您的分区表。让我们回顾一下那个例子，更具体地说是这一行：

```
Number  Start   End     Size    Type      File system     Flags
 5      6861MB  7380MB  519MB   logical   linux-swap(v1)
```

这个 swap 分区是什么？嗯，swap 是我们用来为系统分配虚拟内存的。如果您的内存不足，系统会使用这个分区将空闲进程的内存片段“交换”到磁盘，这样您就不会因为内存不足而卡顿。

### Using a partition for swap space

假设我们想将分区 `/dev/sdb2` 用于 swap 空间。

1. 首先，确保分区上没有任何内容。
2. 运行：`mkswap /dev/sdb2` 以初始化 swap 区域。
3. 运行：`swapon /dev/sdb2`。这将启用 swap 设备。
4. 如果您希望 swap 分区在启动时持久存在，您需要向 `/etc/fstab` 文件添加一个条目。`sw` 是您将使用的文件系统类型。
5. 要移除 swap：`swapoff /dev/sdb2`。

通常，您应该分配大约两倍于您内存的 swap 空间。然而，如今的现代系统通常足够强大，并且本身就拥有足够的 RAM。

## Exercise

将 USB 驱动器中的空闲空间分区用于 swap 空间。

## Quiz Question

在设备上启用 swap 空间的命令是什么？

## Quiz Answer

swapon
