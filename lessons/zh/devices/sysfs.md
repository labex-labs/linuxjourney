---
lang: "zh"
title: "sysfs"
meta_description: "了解 sysfs，一个用于详细 Linux 设备信息和管理的虚拟文件系统。理解 /sys 与 /dev 的区别。开始你的 Linux 之旅！"
meta_keywords: "sysfs, /sys 目录，Linux 设备，虚拟文件系统，Linux 教程，初学者指南"
---

## Lesson Content

Sysfs 是很久以前创建的，旨在更好地管理我们系统上的设备，这是 `/dev` 目录未能充分完成的任务。Sysfs 是一个虚拟文件系统，通常挂载到 `/sys` 目录。它提供了比我们在 `/dev` 目录中能看到的更详细的信息。`/sys` 和 `/dev` 这两个目录看起来非常相似，在某些方面它们确实如此，但它们也有主要区别。基本上，`/dev` 目录很简单；它允许其他程序访问设备本身，而 `/sys` 文件系统用于查看设备信息和管理设备。

`/sys` 文件系统基本上包含系统上所有设备的所有信息，例如制造商和型号、设备插入的位置、设备状态、设备层次结构等等。你在这里看到的文件不是设备节点，所以你不会真正从 `/sys` 目录与设备交互；相反，你是在管理设备。

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

查看 `/sys` 目录的内容，看看里面有哪些文件。

## Quiz Question

哪个目录用于查看设备的详细信息？

## Quiz Answer

/sys
