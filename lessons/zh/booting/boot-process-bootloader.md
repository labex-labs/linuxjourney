---
index: 3
lang: "zh"
title: "引导过程：引导加载程序"
meta_title: "引导过程：引导加载程序 - 启动系统"
meta_description: "了解 Linux 引导加载程序、其功能以及常见的内核参数，如 initrd 和 root。理解 GRUB 并优化您的 Linux 引导过程。"
meta_keywords: "Linux 引导加载程序，GRUB, 内核参数，initrd, 根文件系统，Linux 引导过程，Linux 教程，Linux 初学者"
---

## Lesson Content

引导加载程序的主要职责是：

- 启动操作系统；它也可以用于启动非 Linux 操作系统。
- 选择要使用的内核。
- 指定内核参数。

Linux 最常见的引导加载程序是 GRUB；您很可能在您的系统上使用它。您可以使用许多其他引导加载程序，例如 LILO、EFILINUX、Coreboot、SYSLINUX 等。但是，我们将只使用 GRUB 作为我们的引导加载程序。

所以，我们知道引导加载程序的主要目标是加载内核，但它在哪里找到内核呢？要找到它，我们需要查看我们的内核参数。可以通过在启动时使用“e”键进入 GRUB 菜单来找到这些参数。如果您没有 GRUB，不用担心，我们将介绍您将看到的引导参数：

- `initrd` - 指定初始 RAM 磁盘的位置（我们将在下一课中详细讨论）。
- `BOOT_IMAGE` - 这是内核映像所在的位置。
- `root` - 根文件系统的位置；内核在此位置内搜索以查找 `init`。它通常由其 UUID 或设备名称表示，例如 `/dev/sda1`。
- `ro` - 此参数非常标准；它以只读模式挂载文件系统。
- `quiet` - 添加此参数是为了让您在启动期间看不到后台正在进行的显示消息。
- `splash` - 这允许显示启动画面。

## Exercise

熟能生巧！这是一个动手实验，旨在加强您对 GRUB 引导加载程序及其配置的理解：

1. **[在 Linux 中自定义 GRUB2 引导菜单](https://labex.io/zh/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)** - 练习修改 GRUB2 主配置文件以更改引导菜单设置并应用这些更改。

本实验将帮助您在实际场景中应用概念，并增强对引导加载程序管理的信心。

## Quiz Question

哪个内核参数可以让你看不到启动消息？

## Quiz Answer

quiet
