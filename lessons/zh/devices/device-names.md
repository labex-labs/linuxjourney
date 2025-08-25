---
index: 3
lang: "zh"
title: "设备名称"
meta_title: "设备名称 - 设备"
meta_description: "了解 Linux 设备名称，如 SCSI (sd)、伪设备和 PATA (hd) 设备。在这份适合初学者的指南中，了解 /dev/sda、/dev/null 等。"
meta_keywords: "Linux 设备名称，/dev, SCSI 设备，伪设备，PATA 设备，Linux 教程，Linux 初学者，设备文件"
---

## Lesson Content

以下是您将遇到的最常见的设备名称：

### SCSI 设备

如果您的机器上有任何大容量存储设备，很可能它使用的是 SCSI（发音为“scuzzy”）协议。SCSI 代表小型计算机系统接口；它是一种用于允许磁盘、打印机、扫描仪和其他外围设备与您的系统之间进行通信的协议。您可能听说过 SCSI 设备，它们在现代系统中实际上并未在使用；然而，我们的 Linux 系统将 SCSI 磁盘与 `/dev` 中的硬盘驱动器对应起来。它们由 `sd`（SCSI 磁盘）前缀表示：

常见的 SCSI 设备文件：

- `/dev/sda` - 第一个硬盘
- `/dev/sdb` - 第二个硬盘
- `/dev/sda3` - 第一个硬盘上的第三个分区

### 伪设备

正如我们之前讨论的，伪设备并没有真正物理连接到您的系统。最常见的伪设备是字符设备：

- `/dev/zero` - 接受并丢弃所有输入，产生连续的 NULL（零值）字节流
- `/dev/null` - 接受并丢弃所有输入，不产生任何输出
- `/dev/random` - 产生随机数

### PATA 设备

有时在较旧的系统中，您可能会看到硬盘驱动器以 `hd` 前缀引用：

- `/dev/hda` - 第一个硬盘
- `/dev/hdd2` - 第四个硬盘上的第二个分区

## Exercise

熟能生巧！以下是一些动手实验，旨在加深您对 Linux 设备名称和存储管理的理解：

1. **[管理 Linux 分区和文件系统](https://labex.io/zh/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - 练习创建、格式化和挂载分区，这直接涉及到设备名称的使用。
2. **[探索 Linux 中的硬件设备](https://labex.io/zh/labs/comptia-explore-hardware-devices-in-linux-590861)** - 学习在 Linux 环境中识别和检查各种硬件设备及其相关名称。

这些实验将帮助您在实际场景中应用概念，并增强在 Linux 中管理存储和理解硬件的信心。

## Quiz Question

第二个 SCSI 磁盘上的第一个分区通常的设备名称是什么？

## Quiz Answer

sdb1
