---
index: 4
lang: "zh"
title: "sysfs"
meta_title: "sysfs - 设备"
meta_description: "了解什么是 sysfs 及其在 Linux sys 系统中的作用。本指南解释了 Linux /sys 目录，这是一个用于设备信息的虚拟文件系统，并将其与 /dev 进行对比。"
meta_keywords: "sysfs, 什么是 sysfs, /sys, linux /sys, linux sys, sys 系统，虚拟文件系统，linux 设备，/dev"
---

## Lesson Content

sysfs 文件系统是为了提供一种更好的方式来管理 Linux 系统上的设备而引入的，而 /dev 目录在这方面并不完全具备能力。理解**Linux 中的 /sys 是什么**是现代系统管理的关键。

### 什么是 sysfs？

`sysfs` 是一个虚拟文件系统，通常挂载在 `/sys`，它将内核对象、硬件设备和驱动程序的信息从内核设备模型导出到用户空间。与物理磁盘上的文件不同，`/sys` 中的文件和目录是即时生成的，代表了 **sys system** 的当前状态。

### linux /sys 目录的作用

**linux /sys** 目录的主要目的是提供对系统上所有设备的结构化视图。它包含详细信息，例如制造商和型号、设备连接的位置、当前状态以及它在设备层次结构中的位置。

您在此处看到的文件不是像 `/dev` 中的设备节点。您不通过 `/sys` 直接与设备本身交互；相反，您使用它来查看信息和管理设备的属性。

### sysfs 与 /dev

虽然 `/sys` 和 `/dev` 都与设备相关，但它们的功能不同。

- `/dev` 目录提供设备节点，这些特殊文件允许程序访问设备本身。
- `/sys` 文件系统用于查看有关设备的信息和管理设备。它暴露了底层的设备模型。

例如，让我们检查 `/sys` 中块设备目录的内容：

```bash
pete@icebox:~$ ls /sys/block/sda
alignment_offset  discard_alignment  holders   removable  sda6       trace
bdi               events             inflight  ro         size       uevent
capability        events_async       power     sda1       slaves
dev               events_poll_msecs  queue     sda2       stat
device            ext_range          range     sda5       subsystem
```

此输出显示了与 `sda` 硬盘相关的各种属性和子目录，比单独的 `/dev/sda` 提供了更详细的视图。

## Exercise

实践造就完美！以下是一些实践实验，以加强您对 Linux 中硬件设备探索的理解：

1. **[在 Linux 中探索硬件设备](https://labex.io/zh/labs/comptia-explore-hardware-devices-in-linux-590861)** - 练习在 Linux 环境中识别和检查硬件设备，类似于 sysfs 文件系统提供设备信息的方式。

此实验将帮助您应用理解系统硬件及其在 Linux 中表示的概念，增强设备探索的信心。

## Quiz Question

哪个目录用于查看设备的详细信息？请用英语回答。

## Quiz Answer

/sys
