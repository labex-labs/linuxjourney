---
index: 1
lang: "zh"
title: "内核概述"
meta_title: "内核概述 - 内核"
meta_description: "了解 Linux 内核、它在操作系统中的作用以及它如何与硬件和用户空间交互。理解核心操作系统组件。"
meta_keywords: "Linux 内核，操作系统，硬件交互，用户空间，Linux 教程，初学者指南"
---

## Lesson Content

正如你目前所了解的，内核是操作系统的核心。我们已经讨论了操作系统的其他部分，但还没有展示它们是如何协同工作的。Linux 操作系统可以分为三个不同的抽象级别。

最基本的级别是硬件；这包括我们的 CPU、内存、硬盘、网络端口等。这是实际计算机器正在做什么的物理层。

下一个级别是内核，它处理进程和内存管理、设备通信、系统调用、设置文件系统等。内核的工作是与硬件通信，以确保它按照我们希望进程执行的方式运行。

你所熟悉的级别是用户空间。用户空间包括 shell、你运行的程序、图形等。

在本课程中，我们将重点关注内核并学习其复杂性。

## Exercise

熟能生巧！以下是一些动手实验，旨在加深你对 Linux 内核及其与系统组件交互的理解：

1. **[在 Linux 中管理内核模块](https://labex.io/zh/labs/comptia-manage-kernel-modules-in-linux-590865)** - 练习列出、检查、加载和卸载内核模块，并配置它们在启动时自动加载。
2. **[在 Linux 中探索硬件设备](https://labex.io/zh/labs/comptia-explore-hardware-devices-in-linux-590861)** - 学习使用命令行工具在 Linux 环境中识别和检查硬件设备。
3. **[管理 Linux 分区和文件系统](https://labex.io/zh/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - 获得创建分区、格式化文件系统、挂载它们以及配置持久挂载的实践经验，所有这些都由内核管理。

这些实验将帮助你在实际场景中应用内核与硬件和系统资源交互的概念，并增强你在低级 Linux 管理方面的信心。

## Quiz Question

操作系统的哪个级别管理设备？

## Quiz Answer

kernel
