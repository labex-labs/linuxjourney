---
index: 8
lang: "zh"
title: "交换"
meta_title: "交换分区 - 文件系统"
meta_description: "了解 Linux 交换空间、其工作原理以及如何创建和管理交换分区。通过本指南优化您的系统内存使用！"
meta_keywords: "Linux 交换，mkswap, swapon, swapoff, /etc/fstab, 虚拟内存，Linux 初学者，Linux 教程"
---

## Lesson Content

在之前的示例中，我向您展示了如何查看分区表。让我们重新审视该示例，更具体地说是这一行：

```
Number  Start   End     Size    Type      File system     Flags
 5      6861MB  7380MB  519MB   logical   linux-swap(v1)
```

这个交换分区是什么？嗯，交换是我们用来为系统分配虚拟内存的。如果您的内存不足，系统会使用此分区将空闲进程的内存片段“交换”到磁盘，这样您就不会因为内存不足而陷入困境。

### 使用分区作为交换空间

假设我们想将分区 `/dev/sdb2` 用于交换空间。

1. 首先，确保分区上没有任何内容。
2. 运行：`mkswap /dev/sdb2` 以初始化交换区域。
3. 运行：`swapon /dev/sdb2`。这将启用交换设备。
4. 如果您希望交换分区在启动时持久存在，则需要向 `/etc/fstab` 文件添加一个条目。`sw` 是您将使用的文件系统类型。
5. 要移除交换：`swapoff /dev/sdb2`。

通常，您应该分配大约两倍于您内存的交换空间。然而，如今的现代系统通常足够强大，并且本身就拥有足够的 RAM。

## Exercise

熟能生巧！这里有一些动手实验，以加强您对 Linux 交换空间和虚拟内存管理的理解：

1. **[在 Linux 中创建并激活交换文件](https://labex.io/zh/labs/comptia-create-and-activate-a-swap-file-in-linux-590858)** - 练习创建和激活交换文件，这是管理系统虚拟内存的关键技能。

这个实验将帮助您在实际场景中应用交换分区的概念，并增强您对系统资源管理的信心。

## Quiz Question

启用设备上交换空间的命令是什么？

## Quiz Answer

swapon
