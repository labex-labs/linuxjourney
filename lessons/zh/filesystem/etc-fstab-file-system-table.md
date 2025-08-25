---
index: 7
lang: "zh"
title: "/etc/fstab"
meta_title: "/etc/fstab - 文件系统"
meta_description: "了解 Linux 中的 /etc/fstab，如何在启动时配置文件系统挂载，以及管理设备条目。为初学者讲解 fstab！"
meta_keywords: "/etc/fstab, Linux fstab, 挂载文件系统，Linux 启动，fstab 教程，初学者，指南"
---

## Lesson Content

当我们需要在启动时自动挂载文件系统时，可以将其添加到名为 `/etc/fstab`（发音为“eff es tab”，而不是“eff stab”）的文件中，它是文件系统表的缩写。此文件包含一个永久挂载的文件系统列表。

```plaintext
pete@icebox:~$ cat /etc/fstab
UUID=130b882f-7d79-436d-a096-1e594c92bb76 /               ext4    relatime,errors=remount-ro 0       1
UUID=78d203a0-7c18-49bd-9e07-54f44cdb5726 /home           xfs     relatime        0       2
UUID=22c3d34b-467e-467c-b44d-f03803c2c526 none            swap    sw              0       0
```

每行代表一个文件系统；字段包括：

- UUID - 设备标识符
- 挂载点 - 文件系统挂载到的目录
- 文件系统类型
- 选项 - 其他挂载选项；更多详情请参阅手册页
- Dump - 由 dump 工具使用，决定何时进行备份；您应该默认设置为 0
- Pass - 由 fsck 使用，决定文件系统检查的顺序；如果值为 0，则不会被检查

要添加条目，只需使用上述条目语法直接修改 `/etc/fstab` 文件。修改此文件时请务必小心；如果操作不当，可能会给自己带来一些麻烦。

## Exercise

熟能生巧！动手实践对于理解如何管理文件系统并确保它们在系统启动时正确挂载至关重要。以下是一些动手实验，旨在加深您对 Linux 文件系统管理和 `/etc/fstab` 文件的理解：

1. **[管理 Linux 分区和文件系统](https://labex.io/zh/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - 练习创建分区、格式化分区、挂载分区，并使用 `/etc/fstab` 配置持久挂载。
2. **[在 Linux 中创建和激活交换文件](https://labex.io/zh/labs/comptia-create-and-activate-a-swap-file-in-linux-590858)** - 学习创建和激活交换文件的基本管理任务，这通常涉及 `/etc/fstab` 中的条目。

这些实验将帮助您在实际场景中应用文件系统挂载和配置的概念，并增强您在 Linux 中管理磁盘资源的信心。

## Quiz Question

哪个文件用于定义文件系统应如何挂载？

## Quiz Answer

/etc/fstab
