---
lang: "zh"
title: "创建文件系统"
meta_description: "学习如何使用 mkfs 在 Linux 上创建文件系统。这本面向初学者的指南涵盖了 ext4 和磁盘分区。开始您的 Linux 之旅吧！"
meta_keywords: "mkfs, 创建文件系统，ext4, Linux 分区，Linux 教程，Linux 初学者，磁盘管理，Linux 指南"
---

## Lesson Content

既然您已经对磁盘进行了分区，那么让我们来创建一个文件系统吧！

```bash
sudo mkfs -t ext4 /dev/sdb2
```

就这么简单！**mkfs**（make filesystem）工具允许我们指定所需的文件系统类型以及创建位置。您只应该在新分区的磁盘上创建文件系统，或者在重新分区旧磁盘时创建。如果您尝试在现有文件系统之上创建文件系统，很可能会导致文件系统损坏。

## Exercise

在 USB 驱动器上创建一个 ext4 文件系统。

## Quiz Question

用于创建文件系统的命令是什么？

## Quiz Answer

mkfs
