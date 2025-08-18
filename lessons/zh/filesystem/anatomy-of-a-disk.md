---
lang: "zh"
title: "磁盘剖析"
meta_description: "了解 Linux 磁盘分区、MBR 与 GPT 的区别以及文件系统结构。理解分区、分区表以及如何组织数据。通过此初学者指南开始学习！"
meta_keywords: "Linux 磁盘分区，MBR, GPT, 文件系统结构，Linux 分区，初学者，教程，指南"
---

## Lesson Content

硬盘可以细分为分区，本质上是创建多个块设备。回想一下这样的例子，如 `/dev/sda1` 和 `/dev/sda2`。`/dev/sda` 是整个磁盘，而 `/dev/sda1` 是该磁盘上的第一个分区。分区对于分离数据非常有用，如果您需要特定的文件系统，您可以轻松创建一个分区，而不是将整个磁盘设置为一种文件系统类型。

### Partition Table

每个磁盘都会有一个分区表。此表告诉系统磁盘是如何分区的。此表告诉您分区从何处开始和结束，哪些分区是可引导的，磁盘的哪些扇区分配给哪个分区等等。有两种主要的分区表方案：主引导记录（MBR）和 GUID 分区表（GPT）。

### Partition

磁盘由分区组成，分区帮助我们组织数据。一个磁盘上可以有多个分区，它们不能相互重叠。如果存在未分配给分区的空间，则称为空闲空间。分区的类型取决于您的分区表。在一个分区内，您可以拥有一个文件系统，或者将分区专用于其他用途，例如交换空间（我们很快会讲到）。

_MBR_

- 传统分区表，曾是标准
- 可以有主分区、扩展分区和逻辑分区
- MBR 的主分区限制为四个
- 可以通过将一个主分区转换为扩展分区来创建更多分区（一个磁盘上只能有一个扩展分区）。然后，在扩展分区内部，您可以添加逻辑分区。逻辑分区的使用方式与任何其他分区相同。我知道这很奇怪。
- 支持最大 2 TB 的磁盘

_GPT_

- GUID 分区表（GPT）正在成为磁盘分区的新标准
- 只有一种分区类型，并且可以创建许多分区
- 每个分区都有一个全局唯一标识符（GUID）
- 主要与基于 UEFI 的引导结合使用（我们将在另一门课程中详细介绍）

### Filesystem Structure

我们从之前的课程中了解到，文件系统是文件和目录的有序集合。最简单的形式是，它由一个用于管理文件的数据库和实际文件本身组成；但是，我们将更详细地介绍。

- Boot block - 这位于文件系统的前几个扇区，文件系统本身并不真正使用它。相反，它包含用于引导操作系统的 S 信息。操作系统只需要一个引导块。如果您有多个分区，它们将拥有引导块，但其中许多是未使用的。
- Super block - 这是一个位于引导块之后的单个块，它包含有关文件系统的信息，例如 inode 表的大小、逻辑块的大小和文件系统的大小。
- Inode table - 将其视为管理我们文件的数据库（我们有一整节课专门讲 inode，所以不用担心）。每个文件或目录在 inode 表中都有一个唯一的条目，并且它包含有关文件的各种信息。
- Data blocks - 这是文件和目录的实际数据。

让我们看看不同的分区表。下面是使用 MBR 分区表（msdos）的分区示例。您可以看到机器上的主分区、扩展分区和逻辑分区。

```plaintext
pete@icebox:~$ sudo parted -l
Model: Seagate (scsi)
Disk /dev/sda: 21.5GB
Sector size (logical/physical): 512B/512B
Partition Table: msdos

Number  Start   End     Size    Type      File system     Flags
 1      1049kB  6860MB  6859MB  primary   ext4            boot
 2      6861MB  21.5GB  14.6GB  extended
 5      6861MB  7380MB  519MB   logical   linux-swap(v1)
 6      7381MB  21.5GB  14.1GB  logical   xfs
```

此示例是 GPT，仅使用唯一 ID 作为分区。

```plaintext
Model: Thumb Drive (scsi)
Disk /dev/sdb: 4041MB
Sector size (logical/physical): 512B/512B
Partition Table: gpt

Number  Start   End     Size     File system  Name        Flags
 1      17.4kB  1000MB  1000MB                first
 2      1000MB  4040MB  3040MB                second
```

## Exercise

在您的机器上运行 **parted -l** 并评估您的结果。

## Quiz Question

在 MBR 分区方案中，哪种分区类型用于创建超过 4 个分区？

## Quiz Answer

extended
