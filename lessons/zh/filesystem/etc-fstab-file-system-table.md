---
index: 7
lang: "zh"
title: "/etc/fstab"
meta_title: "/etc/fstab - 文件系统"
meta_description: "了解如何在 Linux 中使用 /etc/fstab 文件在启动时自动挂载文件系统。本指南涵盖 fstab 语法、如何安全编辑 etc fstab 文件及其在系统启动中的作用。"
meta_keywords: "fstab, fstab linux, etc fstab, /etc/fstab, fstab 文件，挂载文件系统，Linux 启动，fstab 教程"
---

## Lesson Content

在 Linux 中，当您希望在启动时自动挂载文件系统时，您会在位于 `/etc/fstab` 的特殊配置文件中进行配置。`fstab` 是“filesystem table”（文件系统表）的缩写，该文件包含系统应在启动过程中挂载的文件系统的永久列表。理解 **fstab linux** 配置是任何系统管理员的一项关键技能。

### 什么是 /etc/fstab

`/etc/fstab` 文件是一个系统配置文件，它定义了所有可用的磁盘分区以及其他类型的文件系统和不一定是基于磁盘的数据源。系统在启动期间会查阅此文件，以确定要自动挂载哪些文件系统。

这是一个典型的 **fstab file** 示例：

```plaintext
pete@icebox:~$ cat /etc/fstab
UUID=130b882f-7d79-436d-a096-1e594c92bb76 /               ext4    relatime,errors=remount-ro 0       1
UUID=78d203a0-7c18-49bd-9e07-54f44cdb5726 /home           xfs     relatime        0       2
UUID=22c3d34b-467e-467c-b44d-f03803c2c526 none            swap    sw              0       0
```

### fstab 文件结构

**etc fstab** 文件中的每一行代表一个文件系统，包含六个由空格或制表符分隔的字段。让我们分解每个字段的含义：

- **设备标识符 (Device Identifier)**：指定要挂载的设备。现代系统使用 UUID（通用唯一标识符）以避免设备名称（例如 `/dev/sda1`）更改时出现问题。
- **挂载点 (Mount Point)**：设备将被挂载到文件系统中的目录（例如 `/` 或 `/home`）。
- **文件系统类型 (Filesystem Type)**：设备上的文件系统类型，例如 `ext4`、`xfs`、`btrfs` 或 `swap`。
- **选项 (Options)**：控制文件系统如何挂载的挂载选项。常见选项包括 `defaults`、`relatime` 和 `errors=remount-ro`。有关完整列表，请查阅 `mount` 手册页。
- **转储 (Dump)**：此字段由 `dump` 实用程序使用，以确定是否需要备份文件系统。值为 `0` 表示它将被忽略，这是一个安全的默认值。
- **通过 (Pass)**：此字段由 `fsck` 用于确定启动时检查文件系统的顺序。根文件系统 (`/`) 应为 `1`，其他文件系统应为 `2`，值为 `0` 表示文件系统将不会被检查。

### 如何编辑 /etc/fstab

您可以通过使用具有 root 权限的文本编辑器直接修改 `/etc/fstab` 文件来添加条目。编辑此文件时要极其小心；**fstab** 中不正确的条目可能会阻止系统正确启动。在进行更改之前备份文件始终是一个好习惯。保存更改后，您可以通过运行命令 `sudo mount -a` 来测试它们，而无需重新启动，该命令会挂载 `/etc/fstab` 中列出的所有文件系统。

## Exercise

实践造就完美！动手实践对于理解如何管理文件系统并确保它们在系统启动时正确挂载至关重要。以下是一些实践实验，以加强您对 Linux 文件系统管理和 `/etc/fstab` 文件的理解：

1. **[管理 Linux 分区和文件系统](https://labex.io/zh/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - 练习创建分区、格式化它们、挂载它们，以及使用 `/etc/fstab` 配置持久性挂载。
2. **[在 Linux 中创建和激活交换文件](https://labex.io/zh/labs/comptia-create-and-activate-a-swap-file-in-linux-590858)** - 学习创建和激活交换文件的基本管理任务，这通常涉及在 `/etc/fstab` 中添加条目。

这些实验将帮助您在实际场景中应用文件系统挂载和配置的概念，并增强您管理 Linux 磁盘资源的信心。

## Quiz Question

用于定义文件系统应如何挂载的文件是什么？（请提供完整路径。答案区分大小写。）

## Quiz Answer

/etc/fstab
