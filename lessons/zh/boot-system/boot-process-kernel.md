---
index: 4
lang: "zh"
title: "启动过程：内核"
meta_title: "启动过程：内核 - 启动系统"
meta_description: "了解 Linux 启动过程、内核初始化和 initramfs 的作用。理解内核如何挂载根文件系统。Linux 启动过程指南。"
meta_keywords: "Linux 启动过程，内核启动，initramfs, initrd, 根文件系统，Linux 教程，Linux 初学者，Linux 指南"
---

## Lesson Content

So now that our bootloader has passed on the necessary parameters, let's see how it gets started:

### Initrd 与 Initramfs

当我们谈论内核启动时，会遇到一个“先有鸡还是先有蛋”的问题。内核管理我们系统的硬件；然而，并非所有驱动程序在启动时都可供内核使用。因此，我们依赖一个临时根文件系统，其中只包含内核访问其余硬件所需的必要模块。在旧版本的 Linux 中，这项工作由 initrd (initial ramdisk) 完成。内核会挂载 initrd，获取必要的启动驱动程序，然后当它加载完所需的一切后，它会用实际的根文件系统替换 initrd。现在，我们有了一种叫做 initramfs 的东西；这是一个内置于内核本身的临时根文件系统，用于加载真实根文件系统所需的所有驱动程序，因此不再需要定位 initrd 文件。

### 挂载根文件系统

现在内核拥有了创建根设备和挂载根分区所需的所有模块。在进一步操作之前，根分区实际上首先以只读模式挂载，以便 fsck 可以安全运行并检查系统完整性。之后，它会以读写模式重新挂载根文件系统。然后内核找到 init 程序并执行它。

## Exercise

熟能生巧！这是一个动手实验，旨在加深您对 Linux 启动过程的理解：

- **[在 Linux 中自定义 GRUB2 启动菜单](https://labex.io/zh/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)** - 学习修改 GRUB2 启动菜单，包括更改超时和默认条目，并应用这些更改。本实验将帮助您了解如何配置引导加载程序。

本实验将帮助您在实际场景中应用这些概念，并增强您对 Linux 启动配置的信心。

## Quiz Question

现代系统中使用什么来加载临时根文件系统？

## Quiz Answer

initramfs
