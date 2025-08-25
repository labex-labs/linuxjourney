---
index: 4
lang: "zh"
title: "sysfs"
meta_title: "sysfs - 设备"
meta_description: "了解 sysfs，一个用于详细 Linux 设备信息和管理的虚拟文件系统。理解 /sys 与 /dev 的区别。开始你的 Linux 之旅！"
meta_keywords: "sysfs, /sys 目录，Linux 设备，虚拟文件系统，Linux 教程，初学者指南"
---

## Lesson Content

Sysfs 在很久以前被创建，旨在更好地管理我们系统上的设备，这是 `/dev` 目录未能充分完成的任务。Sysfs 是一个虚拟文件系统，通常挂载到 `/sys` 目录。它为我们提供了比在 `/dev` 目录中能看到的更详细的信息。`/sys` 和 `/dev` 这两个目录看起来非常相似，在某些方面确实如此，但它们有很大的不同。基本上，`/dev` 目录很简单；它允许其他程序访问设备本身，而 `/sys` 文件系统用于查看信息和管理设备。

`/sys` 文件系统基本上包含了系统上所有设备的所有信息，例如制造商和型号、设备插入的位置、设备的状态、设备的层次结构等等。你在这里看到的文件不是设备节点，所以你不会真正从 `/sys` 目录与设备交互；相反，你是在管理设备。

查看 `/sys` 目录的内容：

```bash
pete@icebox:~$ ls /sys/block/sda
alignment_offset  discard_alignment  holders   removable  sda6       trace
bdi               events             inflight  ro         size       uevent
capability        events_async       power     sda1       slaves
dev               events_poll_msecs  queue     sda2       stat
device            ext_range          range     sda5       subsystem
```

## Exercise

熟能生巧！这里有一些动手实验来巩固你对 Linux 中硬件设备探索的理解：

1. **[在 Linux 中探索硬件设备](https://labex.io/zh/labs/comptia-explore-hardware-devices-in-linux-590861)** - 练习在 Linux 环境中识别和检查硬件设备，类似于 `/sys` 文件系统提供设备信息的方式。

这个实验将帮助你应用理解系统硬件及其在 Linux 中表示的概念，从而增强设备探索的信心。

## Quiz Question

哪个目录用于查看设备的详细信息？

## Quiz Answer

/sys
