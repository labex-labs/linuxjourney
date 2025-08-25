---
index: 5
lang: "zh"
title: "创建文件系统"
meta_title: "创建文件系统 - 文件系统"
meta_description: "学习如何使用 mkfs 在 Linux 上创建文件系统。这本面向初学者的指南涵盖了 ext4 和磁盘分区。开始你的 Linux 之旅！"
meta_keywords: "mkfs, 创建文件系统，ext4, Linux 分区，Linux 教程，Linux 初学者，磁盘管理，Linux 指南"
---

## Lesson Content

既然你已经对磁盘进行了分区，那么让我们来创建一个文件系统吧！

```bash
sudo mkfs -t ext4 /dev/sdb2
```

就这么简单！**mkfs**（创建文件系统）工具允许我们指定所需的文件系统类型以及创建位置。你只应该在新分区的磁盘上创建文件系统，或者在重新分区旧磁盘时创建。如果你试图在现有文件系统之上创建文件系统，很可能会导致文件系统损坏。

## Exercise

熟能生巧！这里有一些动手实验，以巩固你对管理 Linux 文件系统的理解：

1. **[管理 Linux 分区和文件系统](https://labex.io/zh/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - 在此实验中，你将学习如何在 Linux 中管理磁盘分区和文件系统。你将使用 fdisk 创建新分区，使用 ext4 格式化（使用 `mkfs`），挂载它，在 /etc/fstab 中配置持久挂载，并创建一个交换分区，所有这些操作都在一个安全的辅助虚拟磁盘上进行。

此实验将帮助你在实际场景中应用创建和管理文件系统的概念，并增强你在 Linux 磁盘管理方面的信心。

## Quiz Question

用于创建文件系统的命令是什么？

## Quiz Answer

mkfs
