---
index: 4
lang: "zh"
title: "磁盘分区"
meta_title: "磁盘分区 - 文件系统"
meta_description: "使用 parted 命令学习 Linux 磁盘分区。本指南涵盖如何使用 `sudo parted -l` 查看分区、创建和调整它们的大小。还介绍了流行的图形化替代工具 gparted。"
meta_keywords: "Linux 磁盘分区，parted 命令，sudo parted -l, gparted, gparted 替代工具，fdisk, 磁盘管理，创建分区，调整分区大小，Linux 指南"
---

## Lesson Content

本课程提供了一个实用的指南，介绍如何通过分区磁盘（例如 USB 驱动器）来管理文件系统。如果您没有备用磁盘，仍然可以跟随操作以理解这些概念。

首先，我们需要对磁盘进行分区。此任务有许多可用工具：

- **fdisk**: 一个基本的命令行分区工具；它不支持 GPT。
- **parted**: 一个强大的命令行工具，同时支持 MBR 和 GPT 分区。
- **gparted**: `parted` 的图形化版本。对于偏爱可视化界面的用户来说，`gparted` 是一个直观的工具，通常被认为是优秀的 `gparted windows alternative`（gparted Windows 替代品）。
- **gdisk**: 与 `fdisk` 类似，但它只支持 GPT。

我们的示例将使用 `parted`。

### 列出现有分区

在进行更改之前，识别您的磁盘及其当前布局至关重要。一个快速的方法是使用 `sudo parted -l` 命令，它会列出所有连接的块设备的（分区）表。

```bash
sudo parted -l
```

此命令可帮助您在开始修改之前找到正确的设备名称，例如 `/dev/sdb`。

### 启动交互模式

要开始进行更改，请以交互模式启动 `parted`。我们假设目标设备是 `/dev/sdb`。

```bash
sudo parted
```

您将进入 `parted` 工具的 shell 环境，可以在其中运行命令来管理设备的（分区）表。

### 选择设备

进入 `parted` shell 后，您必须选择要修改的磁盘。请务必选择正确的磁盘，以避免数据丢失。

```bash
select /dev/sdb
```

### 查看分区表

使用 `print` 命令显示所选磁盘的分区表。

```plaintext
(parted) print
Model: ATA VBOX HARDDISK (scsi)
Disk /dev/sdb: 10.7GB
Sector size (logical/physical): 512B/512B
Partition Table: msdos
Disk Flags:

Number  Start   End     Size    Type      File system  Flags
 1      1049kB  10.7GB  10.7GB  primary   ext4         boot
```

此输出显示了设备上可用的分区。**Start**（开始）和 **End**（结束）列指示了每个分区在磁盘上的位置。

### 创建分区

`mkpart` 命令用于创建新分区。您需要指定分区类型（例如 `primary`）、可选的文件系统类型以及开始和结束点。

```bash
mkpart primary ext4 1MB 5000MB
```

此命令创建一个 ext4 格式的主分区，从 1MB 开始，到 5000MB 结束。

### 调整分区大小

您也可以使用 `resize` 命令调整现有分区的大小。您需要分区编号以及新的开始和结束点。

```bash
resize 1 1MB 8000MB
```

此命令将分区 1 的大小调整为在 8000MB 标记处结束。

`parted` 是一个非常强大的工具。在执行任何命令之前，请务必仔细检查，以防止意外数据丢失。

## Exercise

实践造就完美！以下是一些实践实验，以加强您对 Linux 磁盘分区和文件系统管理的理解：

1. [管理 Linux 分区和文件系统](https://labex.io/zh/labs/comptia-manage-linux-partitions-and-filesystems-590845) - 在此实验中，您将学习如何在 Linux 中管理磁盘分区和文件系统。您将在安全的辅助虚拟磁盘上使用 fdisk 创建新分区、用 ext4 格式化它、挂载它、在 /etc/fstab 中配置持久挂载，并创建一个交换分区。

此实验将帮助您在真实场景中应用磁盘分区和文件系统管理的理念，并建立对这些基本 Linux 管理技能的信心。

## Quiz Question

用于创建分区的 `parted` 命令是什么？（请用英语回答，注意区分大小写）。

## Quiz Answer

mkpart
