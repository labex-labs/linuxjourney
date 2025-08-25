---
index: 4
lang: "zh"
title: "磁盘分区"
meta_title: "磁盘分区 - 文件系统"
meta_description: "使用 parted 学习 Linux 磁盘分区。了解如何分区、选择、查看和调整磁盘大小。通过这份适合初学者的指南开始学习！"
meta_keywords: "Linux 磁盘分区，parted 命令，fdisk, gparted, Linux 教程，Linux 初学者，磁盘管理，Linux 指南"
---

## Lesson Content

让我们通过在 USB 驱动器上操作来实践文件系统。如果你没有 USB 驱动器，也没关系，你仍然可以继续学习接下来的几节课。

首先，我们需要对磁盘进行分区。有许多工具可以完成此操作：

- fdisk - 基本的命令行分区工具；它不支持 GPT
- parted - 这是一个命令行工具，支持 MBR 和 GPT 分区
- gparted - 这是 parted 的 GUI 版本
- gdisk - fdisk 的替代品，但它不支持 MBR，只支持 GPT

让我们使用 parted 进行分区。假设我连接了 USB 设备，并且设备名称是 /dev/sdb2。

### 启动 parted

```bash
sudo parted
```

你将进入 parted 工具；在这里你可以运行命令来分区你的设备。

### 选择设备

```bash
select /dev/sdb2
```

要选择你将要操作的设备，请通过其设备名称进行选择。

### 查看当前分区表

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

在这里你将看到设备上可用的分区。**start** 和 **end** 点表示分区在硬盘上占用的空间；你需要为你的分区找到一个好的起始和结束位置。

### 分区设备

```bash
mkpart primary 123 4567
```

现在只需选择一个起始点和结束点并创建分区；你需要根据你使用的分区表指定分区类型。

### 调整分区大小

如果空间不足，你也可以调整分区大小。

```bash
resize 2 1245 3456
```

选择分区号，然后选择你想要调整到的起始点和结束点。

Parted 是一个非常强大的工具，在对磁盘进行分区时应小心谨慎。

## Exercise

熟能生巧！以下是一些动手实验，以巩固你对 Linux 磁盘分区和文件系统管理的理解：

1. [管理 Linux 分区和文件系统](https://labex.io/zh/labs/comptia-manage-linux-partitions-and-filesystems-590845) - 在此实验中，你将学习如何在 Linux 中管理磁盘分区和文件系统。你将使用 fdisk 创建新分区，用 ext4 格式化，挂载它，在 /etc/fstab 中配置持久挂载，并创建一个交换分区，所有这些都在一个安全的辅助虚拟磁盘上进行。

本实验将帮助你在实际场景中应用磁盘分区和文件系统管理的概念，并增强你对这些基本 Linux 管理技能的信心。

## Quiz Question

创建分区的 parted 命令是什么？

## Quiz Answer

mkpart
