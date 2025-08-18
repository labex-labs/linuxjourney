---
lang: "zh"
title: "引导过程：引导加载程序"
meta_title: "引导过程：引导加载程序 - 启动系统"
meta_description: "了解 Linux 引导加载程序、其功能以及常见的内核参数，如 initrd 和 root。了解 GRUB 并优化您的 Linux 引导过程。"
meta_keywords: "Linux 引导加载程序，GRUB, 内核参数，initrd, 根文件系统，Linux 引导过程，Linux 教程，Linux 初学者"
---

## Lesson Content

引导加载程序的主要职责是：

- 引导操作系统；它也可以用于引导非 Linux 操作系统。
- 选择要使用的内核。
- 指定内核参数。

Linux 最常见的引导加载程序是 GRUB；您很可能在您的系统上使用它。还有许多其他引导加载程序可以使用，例如 LILO、EFILINUX、Coreboot、SYSLINUX 等。但是，我们将只使用 GRUB 作为我们的引导加载程序。

所以，我们知道引导加载程序的主要目标是加载内核，但是它在哪里找到内核呢？要找到它，我们需要查看我们的内核参数。通过在启动时使用“e”键进入 GRUB 菜单可以找到这些参数。如果您没有 GRUB，不用担心，我们将介绍您将看到的引导参数：

- `initrd` - 指定初始 RAM 盘的位置（我们将在下一课中详细讨论）。
- `BOOT_IMAGE` - 这是内核镜像所在的位置。
- `root` - 根文件系统的位置；内核在此位置内搜索以查找 `init`。它通常由其 UUID 或设备名称表示，例如 `/dev/sda1`。
- `ro` - 此参数非常标准；它以只读模式挂载文件系统。
- `quiet` - 添加此参数是为了让您在引导期间看不到后台显示的消息。
- `splash` - 这允许显示启动画面。

## Exercise

如果您的引导加载程序是 GRUB，请使用“e”键进入 GRUB 菜单并查看设置。

## Quiz Question

哪个内核参数能让您看不到启动消息？

## Quiz Answer

quiet
