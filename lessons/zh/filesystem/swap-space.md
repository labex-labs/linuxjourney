---
index: 8
lang: "zh"
title: "交换"
meta_title: "交换 - 文件系统"
meta_description: "了解 Linux 交换空间、其工作原理以及如何创建和管理交换分区。通过本指南优化您的系统内存使用！"
meta_keywords: "Linux 交换，mkswap, swapon, swapoff, /etc/fstab, 虚拟内存，Linux 初学者，Linux 教程"
---

## Lesson Content

In our previous example, I showed you how to see your partition table. Let's revisit that example, more specifically this line:

```
Number  Start   End     Size    Type      File system     Flags
 5      6861MB  7380MB  519MB   logical   linux-swap(v1)
```

What is this swap partition? Well, swap is what we use to allocate virtual memory to our system. If you are low on memory, the system uses this partition to "swap" pieces of memory of idle processes to the disk, so you're not bogged down for memory.

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
