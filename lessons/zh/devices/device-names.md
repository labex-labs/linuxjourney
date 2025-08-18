---
lang: "zh"
title: "设备名称"
meta_description: "了解 Linux 设备名称，如 SCSI (sd)、伪设备和 PATA (hd) 设备。通过这份适合初学者的指南，理解/dev/sda、/dev/null 等。"
meta_keywords: "Linux 设备名称，/dev, SCSI 设备，伪设备，PATA 设备，Linux 教程，Linux 入门，设备文件"
---

## Lesson Content

您将遇到的最常见的设备名称如下：

### SCSI Devices

如果您的机器上有任何大容量存储设备，很可能它使用的是 SCSI（发音为“scuzzy”）协议。SCSI 代表小型计算机系统接口（Small Computer System Interface）；它是一种用于允许磁盘、打印机、扫描仪和其他外围设备与您的系统之间进行通信的协议。您可能听说过 SCSI 设备，但它们实际上并未在现代系统中使用；然而，我们的 Linux 系统将 SCSI 磁盘与`/dev`中的硬盘驱动器对应起来。它们以`sd`（SCSI 磁盘）作为前缀表示：

常见的 SCSI 设备文件：

- `/dev/sda` - 第一个硬盘
- `/dev/sdb` - 第二个硬盘
- `/dev/sda3` - 第一个硬盘上的第三个分区

### Pseudo Devices

正如我们之前讨论的，伪设备并没有真正物理连接到您的系统。最常见的伪设备是字符设备：

- `/dev/zero` - 接受并丢弃所有输入，产生连续的 NULL（零值）字节流
- `/dev/null` - 接受并丢弃所有输入，不产生任何输出
- `/dev/random` - 产生随机数

### PATA Devices

有时在旧系统中，您可能会看到硬盘驱动器以`hd`前缀引用：

- `/dev/hda` - 第一个硬盘
- `/dev/hdd2` - 第四个硬盘上的第二个分区

## Exercise

写入伪设备并观察会发生什么。请注意不要将您的磁盘写入这些设备！

## Quiz Question

第二个 SCSI 磁盘上的第一个分区通常的设备名称是什么？

## Quiz Answer

sdb1
