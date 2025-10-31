---
index: 1
lang: "zh"
title: "启动过程概述"
meta_title: "启动过程概述 - 系统启动"
meta_description: "清晰概述 Linux 启动过程，详细介绍四个关键阶段：BIOS、引导加载程序、内核和 init。了解从开机到登录提示的完整 Linux 操作系统启动流程。"
meta_keywords: "Linux 启动过程，启动过程 linux, linux 启动，linux 操作系统启动过程，BIOS, 引导加载程序，内核，init, Linux 教程，Linux 指南，新手"
---

## Lesson Content

在探索了 Linux 的一些关键组件之后，现在让我们看看它们在系统启动时是如何组合在一起的。从按下电源按钮到出现登录提示符的整个序列，被称为 **Linux 启动过程** (Linux boot process)。这是一个将断电机器转变为功能齐全的操作系统迷人的旅程。

**Linux 操作系统启动过程** (booting process of the Linux operating system) 可以简化为四个主要阶段。

### 阶段 1 BIOS

BIOS（基本输入/输出系统）或其现代继任者 UEFI（统一可扩展固件接口）是您打开计算机电源时运行的第一个软件。它执行开机自检 (POST) 以初始化和验证 CPU、内存和存储设备等系统硬件。硬件检查通过后，BIOS 的主要任务是从存储设备定位并加载引导加载程序。

### 阶段 2 引导加载程序 (Bootloader)

引导加载程序从 BIOS 接管控制权。它的主要职责是将 Linux 内核加载到内存中。Linux 的常见引导加载程序是 GRUB（GRand 统一引导加载程序）。GRUB 通常会显示一个菜单，允许您选择要启动的操作系统或内核版本。在您做出选择（或超时后），它会将选定的内核和初始 RAM 磁盘 (initrd) 加载到内存中，然后将控制权传递给内核。

### 阶段 3 内核 (Kernel)

一旦内核加载到内存中，它就接管了系统的控制权。它首先解压缩自身并初始化核心硬件和内存管理。然后内核挂载根文件系统，其中包含所有系统文件。**Linux 启动过程** (boot process linux) 所依赖的最后一个也是最关键的任务是执行第一个用户空间程序：`init` 进程。

### 阶段 4 Init

`init` 进程是内核启动的第一个进程，也是系统上所有其他进程的祖先。它的主要工作是根据其配置启动必要的服务和后台进程（守护进程），使系统进入可用状态。`init` 有几种实现，例如传统的 System V init、Upstart 以及现在广泛采用的 systemd。

这提供了 **Linux 启动过程** (booting process linux) 的高级概述。我们将在接下来的课程中深入探讨这些阶段的每一个。

## Exercise

为了巩固您的理解，我们建议您尝试这个动手实验。它提供了一个实际环境，让您应用所学到的关于 Linux 启动过程的知识。

1.  **[在 Linux 中自定义 GRUB2 引导菜单](https://labex.io/zh/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)** - 练习修改 GRUB2 引导菜单，这是 Linux 启动序列中的一个关键组件。

## Quiz Question

Linux 启动过程的最后一个阶段是什么？（请用英文回答，注意大小写）

## Quiz Answer

init
