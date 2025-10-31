---
index: 1
lang: "zh"
title: "内核概述"
meta_title: "内核概述 - Linux 内核"
meta_description: "通过了解 Linux 内核的概述，开启您的 Linux 学习之旅。了解其在管理硬件和用户空间中的核心作用，这是 linuxjourney.com 上的一个基本概念。"
meta_keywords: "Linux 内核，操作系统，硬件，用户空间，Linux 学习之旅，linuxjourney.com, 内核概述"
---

## Lesson Content

正如你所学到的，内核是操作系统的核心。要真正理解 Linux，我们必须了解它的所有部分是如何协同工作的。本课程提供了一个高层次的概述，这是你 Linux 之旅中的关键第一步。

Linux 操作系统可以组织成三个不同的抽象级别。

### 系统硬件

最基本的级别是硬件。这包括 CPU、内存（RAM）、硬盘、网络端口和其他物理设备。这一层是执行我们机器实际计算和操作的基础。

### Linux 内核

下一个级别是内核。内核的主要工作是充当桥梁，与硬件通信，以执行我们的进程请求的任务。它处理进程和内存管理、设备通信、系统调用以及文件系统的设置。这是你在 linux jorney.com 上将探索的一个中心主题。

### 用户空间

你最熟悉的级别是用户空间。这包括 shell、你运行的程序、图形界面和所有其他应用程序。这些程序与内核交互以完成工作，而无需了解底层硬件的具体细节。

在本课程中，我们将深入研究内核，揭开其复杂性的神秘面纱。你 Linux 之旅的这一部分将充满挑战但收获颇丰。

## Exercise

为了将理论付诸实践，请尝试以下动手实验。它们将加强你对 Linux 内核及其与系统组件交互的理解：

1. **[在 Linux 中管理内核模块](https://labex.io/zh/labs/comptia-manage-kernel-modules-in-linux-590865)** - 练习列出、检查、加载和卸载内核模块，并配置它们以便在启动时自动加载。
2. **[在 Linux 中探索硬件设备](https://labex.io/zh/labs/comptia-explore-hardware-devices-in-linux-590861)** - 学习使用命令行实用程序在 Linux 环境中识别和检查硬件设备。
3. **[管理 Linux 分区和文件系统](https://labex.io/zh/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - 获得有关创建分区、格式化文件系统、挂载它们以及配置持久性挂载的实践经验，所有这些都由内核管理。

这些实验将帮助你在真实场景中应用内核与硬件和系统资源交互的概念，并增强低级 Linux 管理的信心。

## Quiz Question

操作系统的哪个级别管理设备？（请用一个单独的小写英文字回答。）

## Quiz Answer

kernel
