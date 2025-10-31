---
index: 2
lang: "zh"
title: "文件系统类型"
meta_title: "文件系统类型 - 文件系统"
meta_description: "了解不同的 Linux 文件系统类型，包括 ext4、Btrfs 和 XFS。本指南解释了日志记录和虚拟文件系统 (VFS) 等关键概念，帮助您理解可用于 Linux 的各种文件系统类型。"
meta_keywords: "linux 文件系统类型，文件系统类型，ext4, Btrfs, XFS, 日志记录，VFS, linux 教程"
---

## Lesson Content

Linux 支持各种各样的文件系统实现。有些针对速度进行了优化，有些针对大容量存储进行了优化，还有一些是为小型设备设计的。每种不同的文件系统类型都有其独特的数据组织方式。

### 虚拟文件系统 (VFS) 的作用

由于有如此多的不同实现可用，应用程序需要一种与它们交互的统一方式。这就是虚拟文件系统 (VFS) 的用武之地。VFS 是 Linux 内核中的一个抽象层，位于应用程序和各种文件系统之间。它提供了一个单一的、统一的接口，确保应用程序可以无缝工作，而无需关心底层的文件系统类型。这种灵活性允许您在磁盘上拥有多个文件系统，通常通过分区来组织，这将在未来的课程中介绍。

### 用于数据完整性的日志记录

大多数现代文件系统类型默认包含一个称为日志记录（journaling）的功能。要理解它的重要性，想象一下在您电脑突然断电时复制一个大文件。在非日志文件系统中，这种中断可能导致文件损坏和文件系统状态不一致。重新启动后，您的系统需要执行完整的磁盘检查 (fsck)，这对于大容量磁盘来说可能非常耗时。

日志文件系统可以防止这个问题。在执行写入操作之前，它首先将预期的更改记录在一个特殊的日志文件或“日志”（journal）中。一旦操作成功完成，日志就会被更新以标记任务已完成。如果发生崩溃，系统可以在重新启动时简单地读取日志，查看哪些操作正在进行中，并快速将文件系统恢复到一致状态。这大大减少了恢复时间并防止了数据损坏。

### 常见的 Linux 文件系统类型

以下是您会遇到的一些最常见的 **linux 文件系统类型**：

- **ext4** - 作为 Linux 扩展文件系统 (Extended Filesystem) 的最新版本，ext4 是许多发行版的默认设置。它向后兼容其前身 (ext2/ext3)，并支持非常大的磁盘卷（高达 1 EB）和文件大小（高达 16 TB）。它是大多数用例的可靠和标准选择。
- **Btrfs** - 通常称为“B 树文件系统”(B-tree FS)，Btrfs 是一种现代文件系统，具有内置快照、增量备份和改进性能等高级功能。虽然它现在被认为是稳定的，并且是某些发行版的默认设置，但它仍在积极开发中。
- **XFS** - 一种高性能的日志文件系统，在处理大文件和并行 I/O 操作方面表现出色。这使得它成为管理大量数据的系统（如媒体服务器）的绝佳选择。
- **NTFS 和 FAT** - 这些是标准的 Windows 文件系统类型。Linux 提供对它们的完全读写支持，这对于双启动系统非常有用。
- **HFS+** - macOS 使用的主要文件系统。Linux 默认对其提供只读支持，可通过附加工具实现写入支持。

You can see which filesystems are in use on your machine with the `df` command:

```plaintext
pete@icebox:~$ df -T
Filesystem     Type     1K-blocks    Used Available Use% Mounted on
/dev/sda1      ext4       6461592 2402708   3707604  40% /
udev           devtmpfs    501356       4    501352   1% /dev
tmpfs          tmpfs       102544    1068    101476   2% /run
/dev/sda6      xfs       13752320  460112  13292208   4% /home
```

The `df` command reports file system disk space usage. The `-T` flag specifically shows the filesystem type. We will explore this tool in more detail later.

## Exercise

为了将您的知识付诸实践，请完成以下动手实验。它将帮助您巩固对 Linux 文件系统和分区的理解：

1. **[管理 Linux 分区和文件系统](https://labex.io/zh/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - 在此实验中，您将练习创建新分区、使用特定文件系统类型对其进行格式化、挂载它，并配置它以进行持久挂载。这些是管理 Linux 存储的基本技能。

此实验允许您在现实场景中应用这些概念，并建立对磁盘管理的信心。

## Quiz Question

What is the most common and default filesystem type for many Linux distributions? (Please answer in English, paying attention to case sensitivity)

## Quiz Answer

ext4
