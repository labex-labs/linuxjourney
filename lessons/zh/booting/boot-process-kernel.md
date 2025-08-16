---
lang: "zh"
title: "启动过程：内核"
description: "了解 Linux 启动过程、内核初始化以及 initramfs 的作用。理解内核如何挂载根文件系统。Linux 启动过程指南。"
keywords: "Linux 启动过程，内核启动，initramfs, initrd, 根文件系统，Linux 教程，Linux 初学者，Linux 指南"
---

## Lesson Content

既然我们的引导加载程序已经传递了必要的参数，让我们看看它是如何启动的：

### Initrd vs Initramfs

当我们谈论内核启动时，存在一个先有鸡还是先有蛋的问题。内核管理我们系统的硬件；然而，并非所有驱动程序在启动时都可供内核使用。因此，我们依赖一个临时根文件系统，它只包含内核访问其余硬件所需的基本模块。在旧版本的 Linux 中，这项工作由 initrd (initial ramdisk) 完成。内核会挂载 initrd，获取必要的启动驱动程序，然后当它加载完所需的一切后，它会用实际的根文件系统替换 initrd。现在，我们有了一种叫做 initramfs 的东西；这是一个内置在内核中的临时根文件系统，用于加载真实根文件系统所需的所有驱动程序，因此不再需要定位 initrd 文件。

### Mounting the root filesystem

现在内核拥有了创建根设备和挂载根分区所需的所有模块。在进一步操作之前，根分区实际上首先以只读模式挂载，以便 fsck 可以安全运行并检查系统完整性。之后，它会以读写模式重新挂载根文件系统。然后内核找到 init 程序并执行它。

## Exercise

No exercises for this lesson.

## Quiz Question

现代系统中使用什么来加载临时根文件系统？

## Quiz Answer

initramfs
