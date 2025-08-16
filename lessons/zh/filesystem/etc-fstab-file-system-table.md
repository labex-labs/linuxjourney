---
title: "/etc/fstab"
description: "了解 Linux 中的 /etc/fstab，如何在启动时配置文件系统挂载，以及管理设备条目。理解 fstab，适合初学者！"
keywords: "/etc/fstab, Linux fstab, 挂载文件系统，Linux 启动，fstab 教程，初学者，指南"
---

## Lesson Content

当我们想在启动时自动挂载文件系统时，我们可以将它们添加到名为 `/etc/fstab`（发音为“eff es tab”，而不是“eff stab”）的文件中，它是文件系统表的缩写。此文件包含已挂载文件系统的永久列表。

```plaintext
pete@icebox:~$ cat /etc/fstab
UUID=130b882f-7d79-436d-a096-1e594c92bb76 /               ext4    relatime,errors=remount-ro 0       1
UUID=78d203a0-7c18-49bd-9e07-54f44cdb5726 /home           xfs     relatime        0       2
UUID=22c3d34b-467e-467c-b44d-f03803c2c526 none            swap    sw              0       0
```

每行代表一个文件系统；字段包括：

- UUID - 设备标识符
- Mount point - 文件系统挂载到的目录
- Filesystem type - 文件系统类型
- Options - 其他挂载选项；更多详细信息请参阅手册页
- Dump - 由 `dump` 工具用于决定何时进行备份；您应该默认设置为 0
- Pass - 由 `fsck` 用于决定文件系统应按什么顺序检查；如果值为 0，则不会检查

要添加条目，只需使用上述条目语法直接修改 `/etc/fstab` 文件。修改此文件时请务必小心；如果您搞砸了，可能会让您的生活变得有点困难。

## Exercise

将我们一直在使用的 USB 驱动器添加为 `/etc/fstab` 中的条目。重启后，您应该仍然看到它已挂载。

## Quiz Question

哪个文件用于定义文件系统应如何挂载？

## Quiz Answer

/etc/fstab
