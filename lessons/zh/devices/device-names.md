---
index: 3
lang: "zh"
title: "设备名称"
meta_title: "设备名称 - 设备"
meta_description: "探索常见的 Linux 存储和外围设备名称。本指南解释了 SCSI 磁盘（如 sda）的命名约定，sda 的含义，以及/dev/null 等伪设备。"
meta_keywords: "linux 设备名称，linux 设备名，sda 代表什么，sd 元素名称，第二个 scsi 磁盘上的第一个分区通常的设备名是什么，/dev, SCSI 设备，伪设备，PATA 设备"
---

## Lesson Content

在 Linux 中，每个设备都由 `/dev` 目录中的一个文件表示。理解这些文件的命名约定对于系统管理至关重要。以下是您会遇到的最常见的 Linux 设备名称类型。

### SCSI 和现代存储设备

即使您的机器使用 SATA、NVMe 或 USB 驱动器等现代存储，Linux 内核通常也会通过其 SCSI（小型计算机系统接口）子系统来管理它们。这就是为什么存储设备最常见的**前缀是 `sd`**，它最初代表“SCSI 磁盘”。

`sd 元素名称`遵循清晰的模式：

- `sd` 前缀表示大容量存储设备。
- 接下来的字母代表驱动器本身，按检测顺序分配（`a` 代表第一个，`b` 代表第二个，依此类推）。
- 末尾的数字表示该驱动器上的分区。

常见的 SCSI 设备文件包括：

- `/dev/sda`: 第一个存储驱动器。
- `/dev/sdb`: 第二个存储驱动器。
- `/dev/sda3`: 第一个存储驱动器上的第三个分区。

那么，第二块 SCSI 磁盘上的第一个分区的设备名称通常是什么？遵循该模式，第二块磁盘是 `sdb`，其第一个分区是 `1`。因此，设备名称是 `/dev/sdb1`。

### 伪设备 (Pseudo-Devices)

伪设备是特殊文件，不对应任何物理硬件，但提供有用的系统功能。它们通常是字符设备。

- `/dev/zero`: 接受并丢弃所有输入。读取时，它会产生一个连续的 NULL（零值）字节流。
- `/dev/null`: 接受并丢弃写入到它的所有输入，读取时不会产生任何输出。
- `/dev/random`: 从环境噪声中生成随机数流。

### 遗留 PATA 设备

在旧系统中，您可能会遇到使用并行 ATA (PATA) 接口的硬盘。Linux 中这些驱动器的设备名称使用 `hd` 前缀。

- `/dev/hda`: 第一个 PATA 硬盘。
- `/dev/hdd2`: 第四个 PATA 硬盘上的第二个分区。

## Exercise

实践造就完美！以下是一些实践实验，以加强您对 Linux 设备名称和存储管理的理解：

1. **[管理 Linux 分区和文件系统](https://labex.io/zh/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - 练习创建、格式化和挂载分区，这直接涉及到使用设备名称。
2. **[探索 Linux 中的硬件设备](https://labex.io/zh/labs/comptia-explore-hardware-devices-in-linux-590861)** - 学习在 Linux 环境中识别和检查各种硬件设备及其关联的名称。

这些实验将帮助您在实际场景中应用这些概念，并增强管理存储和理解 Linux 中硬件的信心。

## Quiz Question

第二块 SCSI 磁盘上的第一个分区的设备名称通常是什么？请用英文提供答案，注意正确的字母大小写。

## Quiz Answer

/dev/sdb1
