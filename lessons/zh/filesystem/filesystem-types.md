---
lesson_id: "filesystem-types"
course_id: "filesystem"
lang: "zh"
order_index: 2
title: "文件系统类型"
description: "了解 Linux VFS 如何通过统一接口呈现本地、网络和虚拟文件系统。"
meta_title: "文件系统类型 - 文件系统"
meta_description: "探索不同的 Linux 文件系统类型，包括 ext4、Btrfs 和 XFS。本指南解释日志和虚拟文件系统（VFS）等关键概念，帮助你理解 Linux 可用的各种文件系统类型。"
meta_keywords: "linux 文件系统类型，文件系统类型，ext4, Btrfs, XFS, 日志，VFS, linux 教程"
---

Linux 支持许多文件系统实现，它们的磁盘格式、网络协议、一致性模型、功能和运维工具各不相同。合适的选择取决于发行版支持、工作负载、恢复要求、存储拓扑和管理员经验。

## 虚拟文件系统层

内核的虚拟文件系统层（Virtual Filesystem，VFS）提供打开、读取、写入、重命名和权限检查等通用操作。各文件系统实现再把这些操作连接到自己的数据结构和后端存储。

因此，一个进程可以通过统一的路径名和文件描述符模型访问 ext4、XFS、NFS、tmpfs 和 procfs。这并不会让所有文件系统的功能或行为完全一致；大小写敏感性、锁定、权限、重命名保证、扩展属性和错误处理都可能不同。

:::single-choice{#filesystem-types-vfs-role} Linux VFS 的主要作用是什么？

::option[把每个已挂载文件系统在磁盘上转换为 ext4。]{#filesystem-types-vfs-convert-ext4 explanation="这一抽象会保留不同的文件系统实现和格式。"}
::option[在应用程序写入每个文件前自动备份它。]{#filesystem-types-vfs-backup explanation="VFS 分派操作，不提供自动备份历史。"}
::option[为不同文件系统实现提供通用的内核文件操作。]{#filesystem-types-vfs-common-interface .correct explanation="VFS 让应用程序使用统一系统调用，同时由各文件系统实现底层行为。"}
:::

## 日志与崩溃一致性

日志文件系统会把选定的更新记录到日志中，以便在崩溃后重放或丢弃未完成的事务。日志的主要用途，是比完整扫描更快地恢复文件系统结构的一致性。

它并不保证最新的应用数据一定保留下来、多文件应用事务一定有效，或存储硬件确实完成了所有已确认写入。文件系统提供不同的数据模式和顺序保证，而应用程序必须采用适当的刷新和原子更新方式。日志不是备份，无法防止删除、恶意软件或设备故障。

:::single-choice{#filesystem-types-journal-scope} 文件系统日志主要帮助在崩溃后恢复什么？

::option[一致的文件系统元数据和已记录事务。]{#filesystem-types-journal-consistency .correct explanation="日志重放有助于使文件系统结构恢复到协调一致的状态。"}
::option[每份用户文档的所有历史版本。]{#filesystem-types-journal-versions explanation="日志并不是带版本的备份存储。"}
::option[物理损毁的存储设备中的数据。]{#filesystem-types-journal-hardware-loss explanation="从设备损坏中恢复需要失败设备以外的冗余或备份。"}
:::

## 常见本地文件系统

- **ext4** 是成熟的日志文件系统，得到 Linux 发行版和恢复工具的广泛支持。
- **XFS** 是可扩展的日志文件系统，常用于大型文件系统和并行 I/O 工作负载。
- **Btrfs** 是写时复制文件系统，提供校验和、子卷、快照和集成式多设备功能。

各项功能必须结合运维环境理解。Btrfs 快照最初与源数据共享存储；如果仍位于同一块可能故障的设备上，它并不是独立备份。XFS 和 ext4 的扩容、缩容、修复和调优能力也不同。选择或更改根文件系统前，应确认已安装内核、启动环境和恢复工具对它的支持。

:::single-choice{#filesystem-types-btrfs-snapshot} 为什么同一设备上的 Btrfs 快照不是完整备份？

::option[快照总会立即删除原始子卷。]{#filesystem-types-snapshot-deletes explanation="快照会创建另一个子卷视图，本身不会删除源子卷。"}
::option[它与原始数据处于同一个存储故障域。]{#filesystem-types-snapshot-failure-domain .correct explanation="设备丢失或严重的文件系统损坏可能同时影响源数据和本地快照。"}
::option[Btrfs 无法表示一个以上的文件。]{#filesystem-types-btrfs-one-file explanation="Btrfs 是能够保存目录树和大量文件的通用文件系统。"}
:::

## 互操作、网络与虚拟文件系统

Linux 可以挂载 FAT 变体、exFAT 和 NTFS 等互操作格式，但它们的 Unix 所有权、权限、链接和文件名语义各不相同。Linux 如何呈现这些格式缺少的功能，取决于挂载选项和驱动程序实现。

NFS 和 SMB 等网络文件系统依赖服务器和网络协议，并拥有各自的缓存与身份规则。tmpfs、procfs 和 sysfs 等虚拟文件系统不使用普通的持久磁盘格式：tmpfs 在内存后端页面中保存易失数据，procfs 和 sysfs 则公开内核接口。

:::single-choice{#filesystem-types-procfs-category} 哪个描述最符合 procfs？

::option[用于可移动介质的 Windows 交换格式。]{#filesystem-types-procfs-windows explanation="FAT 或 exFAT 更符合这种用途；procfs 面向 Linux 内核。"}
::option[公开进程和内核接口的虚拟文件系统。]{#filesystem-types-procfs-virtual .correct explanation="Procfs 生成实时内核视图，而不是在磁盘上保存普通持久文件。"}
::option[面向数据库卷设计的日志磁盘文件系统。]{#filesystem-types-procfs-journal explanation="Procfs 没有普通的磁盘日志或数据卷用途。"}
:::

## 发现活动类型

使用以下命令显示已挂载文件系统的类型：

```bash
$ findmnt -o TARGET,SOURCE,FSTYPE,OPTIONS
```

其他视图包括：用 `df -T` 查看已挂载空间统计，用 `lsblk -f` 查看块设备和检测到的文件系统签名，以及用 `/proc/filesystems` 查看运行中内核支持或已知的类型。这些视图回答的是不同问题；未挂载的文件系统不会出现在普通的已挂载文件系统列表中。

:::single-choice{#filesystem-types-findmnt-output} 本课所示的哪个命令会直接列出挂载目标、来源、类型和选项？

::option[`findmnt -o TARGET,SOURCE,FSTYPE,OPTIONS`]{#filesystem-types-findmnt .correct explanation="Findmnt 读取挂载表，并格式化请求的已挂载文件系统字段。"}
::option[`lsblk -o NAME,SIZE,MODEL,SERIAL,ROTA`]{#filesystem-types-mkfs-destructive explanation="该命令列出块设备硬件信息，而不是实际挂载的文件系统类型和选项。"}
::option[`cat /proc/filesystems | sort --unique`]{#filesystem-types-rm-proc explanation="该命令报告内核支持的文件系统类型，而不是实际挂载来源和选项。"}
:::

可以在[管理 Linux 分区和文件系统](https://labex.io/zh/labs/comptia-manage-linux-partitions-and-filesystems-590845)实验的可丢弃存储上比较不同类型、挂载选项和发现视图。

## 总结

现在，你可以比较不同文件系统类别，而不会假定它们具有完全相同的语义。

1. 理解 VFS 如何为不同实现提供通用操作。
2. 把日志视为崩溃一致性支持，而不是备份。
3. 根据支持的操作和工作负载比较 ext4、XFS 与 Btrfs。
4. 区分本地磁盘、网络、互操作和虚拟文件系统。
5. 使用挂载工具和块设备工具回答不同的清单问题。
