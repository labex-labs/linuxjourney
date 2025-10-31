---
index: 3
lang: "zh"
title: "磁盘解剖"
meta_title: "磁盘解剖 - 文件系统"
meta_description: "探索 Linux 中磁盘的结构。本指南解释了磁盘的哪个组件告诉操作系统磁盘如何分区，涵盖 MBR 和 GPT 分区表、不同类型的 Linux 分区及其组织方式。"
meta_keywords: "linux 磁盘，linux 分区，linux 分区类型，磁盘哪个组件告诉操作系统如何分区，硬盘分区组织信息包含什么，MBR, GPT, 分区表，文件系统"
---

## Lesson Content

Linux 中的硬盘可以细分为分区，这些分区充当独立的块设备。您可能还记得像 /dev/sda1 和 /dev/sda2 这样的例子。在这里，/dev/sda 代表整个磁盘，而 /dev/sda1 是该磁盘上的第一个分区。分区对于分离数据非常有用。如果您需要为存储的一部分使用特定的文件系统，您可以为其创建一个新分区，而不是格式化整个磁盘。

### 分区表

那么，磁盘的哪个组件告诉操作系统如何对磁盘进行分区呢？答案是**分区表**。这个关键组件包含有关硬盘分区如何组织的信息。分区表指定了每个分区的开始和结束位置、哪些分区可引导，以及磁盘的哪些扇区分配给了每个分区。主要有两种分区表方案：主引导记录 (MBR) 和 GUID 分区表 (GPT)。

### 理解 Linux 分区

磁盘由分区组成，帮助我们组织数据。单个磁盘上可以有多个分区，但它们不能重叠。磁盘上未分配给分区的任何空间称为空闲空间。可用的 Linux 分区类型取决于您使用的分区表方案。在分区内部，您可以创建文件系统或将其专用于其他目的，例如交换空间。

### MBR 分区

主引导记录 (MBR) 是传统的分区表标准。

- 它支持主分区、扩展分区和逻辑分区。
- MBR 限制为四个主分区。
- 要创建更多分区，必须将一个主分区指定为扩展分区（每个磁盘只允许一个）。在此扩展分区内，您可以创建多个逻辑分区，它们的功能与其他任何分区一样。
- 它支持最大为 2TB 的磁盘。

### GPT 分区

GUID 分区表 (GPT) 是磁盘分区的现代标准。

- 它只有一种分区类型，您可以创建大量分区。
- 每个分区都被分配一个全局唯一标识符 (GUID)。
- GPT 通常与基于 UEFI 的引导系统一起使用。

### 文件系统结构

正如我们之前学到的，文件系统是文件和目录的组织集合。其核心包括一个用于管理文件的数据库和文件本身。让我们更详细地探讨其结构。

- **引导块 (Boot block)**：位于文件系统的最前几个扇区，该块本身不被文件系统使用。相反，它包含用于引导操作系统的文件。每个操作系统只需要一个引导块。虽然其他分区可能有引导块，但它们通常未被使用。
- **超级块 (Superblock)**：这是紧跟在引导块后面的一个块，包含有关文件系统的元数据，例如 inode 表的大小、逻辑块的大小以及文件系统的总大小。
- **Inode 表 (Inode table)**：这是管理文件和目录的数据库。每个文件或目录在 inode 表中都有一个唯一的条目，其中存储了有关它的各种属性。我们将在专门的课程中介绍 inode。
- **数据块 (Data blocks)**：这是存储文件和目录实际内容的地方。

下面是一个使用 MBR 分区表（标记为 `msdos`）的磁盘示例。您可以看到主分区、扩展分区和逻辑分区。

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

第二个示例显示了一个 GPT 分区表，它为其分区使用唯一的 ID。

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

为了巩固您对磁盘分区和文件系统的理解，我们推荐以下动手实验：

1.  **[管理 Linux 分区和文件系统](https://labex.io/zh/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - 练习创建新分区、使用 ext4 等文件系统格式化它们、挂载它们，以及在 `/etc/fstab` 中配置持久挂载。

此实验将帮助您在实际场景中应用磁盘管理概念，并增强对 Linux 存储的信心。

## Quiz Question

在 MBR 分区方案中，用于创建超过 4 个分区的分区类型是什么？（请用一个纯小写的英文字词回答。）

## Quiz Answer

extended
