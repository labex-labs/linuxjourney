---
index: 4
lang: "zh"
title: "磁盘分区"
meta_title: "磁盘分区 - 文件系统"
meta_description: "使用 parted 学习 Linux 磁盘分区。了解如何分区、选择、查看和调整磁盘大小。通过这个适合初学者的指南开始吧！"
meta_keywords: "Linux 磁盘分区，parted 命令，fdisk, gparted, Linux 教程，Linux 初学者，磁盘管理，Linux 指南"
---

## Lesson Content

让我们通过在 USB 驱动器上操作来实际学习文件系统。如果你没有 USB 驱动器，也没关系，你仍然可以继续学习接下来的几节课。

首先，我们需要对磁盘进行分区。有许多工具可以完成这项工作：

- fdisk - 基本的命令行分区工具；它不支持 GPT
- parted - 这是一个命令行工具，支持 MBR 和 GPT 分区
- gparted - 这是 parted 的 GUI 版本
- gdisk - fdisk，但它不支持 MBR，只支持 GPT

让我们使用 parted 进行分区。假设我连接了 USB 设备，并且设备名称是/dev/sdb2。

### Launch parted

```bash
sudo parted
```

你将进入 parted 工具；在这里你可以运行命令来分区你的设备。

### Select the device

```bash
select /dev/sdb2
```

要选择你将要操作的设备，请通过其设备名称进行选择。

### View current partition table

```plaintext
(parted) print
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

在这里你将看到设备上可用的分区。**start**和**end**点是分区在硬盘上占据空间的位置；你需要为你的分区找到一个好的起始和结束位置。

### Partition the device

```bash
mkpart primary 123 4567
```

现在只需选择一个起始点和结束点来创建分区；你需要根据你使用的分区表指定分区的类型。

### Resize a partition

如果没有空间，你也可以调整分区大小。

```bash
resize 2 1245 3456
```

选择分区号，然后选择你想要调整大小的起始和结束点。

Parted 是一个非常强大的工具，在分区磁盘时应小心谨慎。

## Exercise

使用一半的驱动器作为 ext4，另一半作为空闲空间来分区一个 USB 驱动器。

## Quiz Question

创建分区的 parted 命令是什么？

## Quiz Answer

mkpart
