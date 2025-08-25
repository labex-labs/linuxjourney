---
index: 6
lang: "zh"
title: "mount 和 umount"
meta_title: "mount 和 umount - 文件系统"
meta_description: "了解如何使用 Linux mount 和 umount 命令来管理文件系统。了解设备挂载、卸载以及 UUID，适合初学者。"
meta_keywords: "Linux mount, umount 命令，挂载文件系统，Linux UUID, Linux 初学者，Linux 教程，挂载点，Linux 指南"
---

## Lesson Content

在查看文件系统内容之前，您必须先挂载它。为此，我需要设备位置、文件系统类型和挂载点。挂载点是系统上文件系统将要附加到的目录。所以，我们基本上想将设备挂载到挂载点。

首先，创建挂载点；在我们的例子中，**mkdir /mydrive**。

```bash
sudo mount -t ext4 /dev/sdb2 /mydrive
```

就这么简单！现在，当我们进入 /mydrive 时，我们可以看到文件系统内容。**-t** 指定文件系统类型，然后是设备位置，然后是挂载点。

要从挂载点卸载设备：

```bash
sudo umount /mydrive
```

or

```bash
sudo umount /dev/sdb2
```

请记住，内核按照发现设备的顺序命名它们。如果我们的设备名称在挂载后因某种原因发生变化怎么办？幸运的是，您可以使用设备的通用唯一 ID (UUID) 而不是名称。

要查看系统上块设备的 UUID：

```bash
pete@icebox:~$ sudo blkid
/dev/sda1: UUID="130b882f-7d79-436d-a096-1e594c92bb76" TYPE="ext4"
/dev/sda5: UUID="22c3d34b-467e-467c-b44d-f03803c2c526" TYPE="swap"
/dev/sda6: UUID="78d203a0-7c18-49bd-9e07-54f44cdb5726" TYPE="xfs"
```

我们可以看到设备名称、相应的文件系统类型及其 UUID。现在，当我们要挂载某些东西时，我们可以使用：

```bash
sudo mount UUID=130b882f-7d79-436d-a096-1e594c92bb76 /mydrive
```

大多数情况下，您不需要通过 UUID 挂载设备；使用设备名称要容易得多，而且通常操作系统会知道如何挂载 USB 驱动器等常见设备。但是，如果您需要在启动时自动挂载文件系统，例如您添加了辅助硬盘驱动器，您将需要使用 UUID，我们将在下一课中介绍这一点。

## Exercise

熟能生巧！这是一个动手实验，旨在巩固您对管理 Linux 文件系统的理解：

- **[管理 Linux 分区和文件系统](https://labex.io/zh/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - 在此实验中，您将学习如何在 Linux 中管理磁盘分区和文件系统。您将使用 fdisk 创建新分区，使用 ext4 格式化它，挂载它，在 /etc/fstab 中配置持久挂载，并创建交换分区，所有这些都在一个安全的辅助虚拟磁盘上进行。

此实验将帮助您在实际场景中应用挂载和卸载的概念，并增强您对文件系统管理的信心。

## Quiz Question

用于附加文件系统的命令是什么？

## Quiz Answer

mount
