---
index: 1
lang: "zh"
title: "启动过程概述"
meta_title: "启动过程概述 - 启动系统"
meta_description: "了解 Linux 启动过程的阶段：BIOS、bootloader、kernel 和 init。了解 Linux 如何从开机到登录。Linux 初学者必备指南。"
meta_keywords: "Linux 启动过程，BIOS, bootloader, kernel, init, Linux 教程，Linux 指南，初学者"
---

## Lesson Content

既然我们已经对 Linux 的一些重要组件有了相当好的理解，那么让我们通过学习系统如何启动来将它们整合在一起。当你打开你的机器时，它会做一些很酷的事情，比如显示徽标屏幕，运行一些不同的消息，然后最后，你会看到一个登录窗口。实际上，从你按下电源按钮到你登录之间，发生了大量的事情，我们将在本课程中讨论这些。

Linux 启动过程可以分为 4 个简单的阶段：

### 1. BIOS

BIOS（“基本输入/输出系统”的缩写）初始化硬件，并通过加电自检 (POST) 确保所有硬件都准备就绪。BIOS 的主要工作是加载 bootloader。

### 2. Bootloader

bootloader 将 kernel 加载到内存中，然后使用一组 kernel 参数启动 kernel。最常见的 bootloader 之一是 GRUB，它是一个通用的 Linux 标准。

### 3. Kernel

当 kernel 加载后，它会立即初始化设备和内存。kernel 的主要工作是加载 init 进程。

### 4. Init

请记住，init 进程是第一个启动的进程。Init 启动和停止系统上的基本服务进程。Linux 发行版中有三种主要的 init 实现。我们将简要介绍它们，然后在另一门课程中深入探讨它们。

这就是 Linux 启动过程的（非常）简单的解释。我们将在接下来的课程中更详细地介绍这些阶段。

## Exercise

Reboot your system and see if you can spot each step as your machine boots up.

## Quiz Question

Linux 启动过程的最后一个阶段是什么？

## Quiz Answer

init
