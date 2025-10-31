---
index: 6
lang: "zh"
title: "挂载与卸载"
meta_title: "挂载与卸载 - 文件系统"
meta_description: "学习如何在 Linux 中使用 mount 和 umount 命令来挂载和分离文件系统。本指南涵盖设备挂载、安全的 sudo umount 过程以及使用 UUID。"
meta_keywords: "挂载，卸载，sudo 卸载，umount linux, linux 卸载，debian 卸载，挂载文件系统，卸载设备，Linux UUID, 挂载点"
---

## Lesson Content

在访问存储设备上的文件之前，您必须先将其文件系统挂载到系统上的一个目录。此过程涉及设备位置、文件系统类型和挂载点。挂载点只是一个现有的目录，文件系统将被附加到该目录。

### 如何挂载文件系统

首先，您需要创建一个挂载点。让我们为此目的创建一个目录：

```bash
sudo mkdir /mydrive
```

挂载点准备就绪后，您可以使用 `mount` 命令来附加您的设备。`-t` 标志指定了文件系统类型。

```bash
sudo mount -t ext4 /dev/sdb2 /mydrive
```

就这么简单！现在，如果您导航到 `/mydrive` 目录，您将看到设备文件系统的内容。

### 如何在 Linux 中卸载文件系统

完成设备使用后，应将其卸载，以确保所有数据都已安全写入并且文件系统已干净分离。在 Linux 中执行此操作的标准命令是 `umount`。要执行 `linux unmount`，您可以指定挂载点或设备名称。

使用挂载点：

```bash
sudo umount /mydrive
```

或者，使用设备名称：

```bash
sudo umount /dev/sdb2
```

最佳实践是使用 `sudo umount` 以确保您拥有分离文件系统所需的权限。此命令在所有 Linux 发行版中都是通用的，因此无论您使用的是 Ubuntu、Fedora 还是执行 `debian umount`，语法都是相同的。请注意，如果设备当前正在使用中（例如，如果文件已打开或您的当前工作目录在该设备上），则无法 `umount` 它。

### 使用 UUID 实现稳定挂载

内核按发现顺序命名设备，这意味着 `/dev/sdb2` 这样的设备名称在重新启动之间可能会发生变化。为避免出现问题，您可以使用设备始终不变的通用唯一 ID (UUID)。

要查看块设备的 UUID，请使用 `blkid` 命令：

```bash
pete@icebox:~$ sudo blkid
/dev/sda1: UUID="130b882f-7d79-436d-a096-1e594c92bb76" TYPE="ext4"
/dev/sda5: UUID="22c3d34b-467e-467c-b44d-f03803c2c526" TYPE="swap"
/dev/sda6: UUID="78d203a0-7c18-49bd-9e07-54f44cdb5726" TYPE="xfs"
```

此输出显示设备名称、它们的文件系统类型以及它们对应的 UUID。然后，您可以使用设备的 UUID 挂载设备：

```bash
sudo mount UUID=130b882f-7d79-436d-a096-1e594c92bb76 /mydrive
```

虽然您不总是需要通过 UUID 挂载设备，但这是在启动时自动挂载文件系统（例如辅助硬盘）的推荐方法。我们将在下一课中介绍该过程。

## Exercise

实践造就完美！这是一个强化您管理 Linux 文件系统理解的动手实验：

- **[管理 Linux 分区和文件系统](https://labex.io/zh/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - 在此实验中，您将学习如何在 Linux 中管理磁盘分区和文件系统。您将使用 fdisk 创建一个新分区，用 ext4 格式化它，挂载它，在 `/etc/fstab` 中配置持久挂载，并创建一个交换分区，所有这些都在一个安全的辅助虚拟磁盘上。

此实验将帮助您在实际场景中应用挂载和卸载的概念，并建立对文件系统管理的信心。

## Quiz Question

用于附加文件系统的命令是什么？（请使用单个小写的英文字词作为答案。）

## Quiz Answer

mount
