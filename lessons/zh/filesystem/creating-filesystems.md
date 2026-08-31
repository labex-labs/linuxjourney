---
lesson_id: "creating-filesystems"
course_id: "filesystem"
lang: "zh"
order_index: 5
title: "创建文件系统"
description: "学习如何核实块设备目标，并使用特定格式的工具创建文件系统。"
meta_title: "创建文件系统 - 文件系统"
meta_description: "学习如何使用 mkfs 命令在 Linux 分区上创建文件系统。本初学者指南涵盖磁盘管理、使用 ext4 格式化以及 Linux 分区的基本步骤。"
meta_keywords: "mkfs, 创建文件系统，ext4, Linux 分区，Linux 教程，Linux 入门，磁盘管理，Linux 指南，格式化磁盘 linux"
---

创建文件系统会向块设备写入新的分配和元数据结构。这是破坏性的初始化步骤，而不只是更改标签。练习时只能使用可丢弃存储；格式化曾经保存过重要数据的设备前，必须准备经过恢复测试的备份。

## 理解 `mkfs`

`mkfs` 通常是一个前端，会把操作分派给 `mkfs.ext4`、`mkfs.xfs` 或 `mkfs.btrfs` 等特定文件系统程序。通用命令形式如下：

```bash
$ sudo mkfs -t ext4 /dev/VERIFIED-PARTITION
```

只有完成核实后，才能替换这个占位符。对应的特定格式语法通常是：

```bash
$ sudo mkfs.ext4 /dev/VERIFIED-PARTITION
```

不同实现支持的选项、默认值、功能集和覆盖提示并不相同。应阅读具体格式化程序的本机手册，不要假定所有 `mkfs` 后端行为一致。

:::single-choice{#creating-filesystems-mkfs-role}
`mkfs -t ext4 TARGET` 请求执行什么操作？

::option[挂载现有文件系统，而不改变它。]{#creating-filesystems-mount-existing explanation="挂载是独立操作；mkfs 会初始化设备上的元数据。"}
::option[在目标上创建 ext4 文件系统结构。]{#creating-filesystems-create-ext4 .correct explanation="此前端会为指定块设备选择 ext4 格式化实现。"}
::option[列出当前挂载的所有文件系统。]{#creating-filesystems-list-mounted explanation="已挂载文件系统的只读清单应使用 `findmnt` 等工具。"}
:::

## 核实每一层存储

格式化前，应根据型号、序列号、容量、拓扑、持久链接和预期用途识别目标：

```bash
$ lsblk -o NAME,PATH,TYPE,SIZE,MODEL,SERIAL,FSTYPE,UUID,MOUNTPOINTS
$ findmnt --real
$ sudo wipefs --no-act /dev/VERIFIED-PARTITION
```

`wipefs --no-act` 会报告识别到的签名，但不会擦除它们。此外还要检查交换空间、LVM、RAID、加密、虚拟机、容器和应用程序是否正在使用设备。即使 `MOUNTPOINTS` 为空，设备也可能处于活动状态。

应通过每一层自身的工具卸载或停用所有相关内容。枚举名称可能发生变化，因此运行格式化程序前要立即再次核实身份。

:::single-choice{#creating-filesystems-wipefs-no-act}
在此工作流程中，`wipefs --no-act TARGET` 提供什么？

::option[识别到的签名的只读报告。]{#creating-filesystems-signature-report .correct explanation="无操作模式可以揭示现有文件系统、分区表、RAID 或其他签名，但不会移除它们。"}
::option[一个可直接挂载的全新空文件系统。]{#creating-filesystems-wipefs-formats explanation="检查签名不会初始化新文件系统。"}
::option[目标未被任何进程使用的保证。]{#creating-filesystems-wipefs-no-users explanation="必须另外检查挂载情况和更广泛存储栈中的使用情况。"}
:::

## 有意识地选择文件系统

选择的类型应得到发行版、启动环境、备份工具、修复工具和工作负载支持。应考虑所需上限、快照、校验和、配额、加密层次、扩容或缩容行为以及跨平台访问。

不要只因为某种格式流行就选择它。例如，ext4、XFS 和 Btrfs 的运维功能和恢复流程各不相同。用于跨系统交换的可移动设备可能需要另一种格式，而其 Unix 权限语义也会不同。

:::single-choice{#creating-filesystems-type-choice}
选择文件系统类型时，哪项依据合理？

::option[选择名称最短、输入最方便的类型。]{#creating-filesystems-shortest-name explanation="命令长度无法反映持久性、功能或支持情况。"}
::option[选择承诺今后永远不会发生存储故障的类型。]{#creating-filesystems-no-failure explanation="没有任何文件系统能够消除硬件故障或备份需求。"}
::option[结合工作负载需求，以及受支持的备份、启动和恢复工具。]{#creating-filesystems-supported-workflow .correct explanation="格式既要满足技术要求，也要适合环境的运维和恢复能力。"}
:::

## 标签、UUID 与验证

格式化程序通常会生成文件系统 UUID，而且往往可以设置便于阅读的标签。标签在当前环境中应足够唯一；克隆的文件系统同时挂载时，不能保留相互冲突的标识符。

创建成功后，可以在不挂载的情况下检查：

```bash
$ lsblk -f /dev/VERIFIED-PARTITION
$ sudo blkid /dev/VERIFIED-PARTITION
```

记录 UUID，以供后续挂载配置使用。创建文件系统并不会挂载它、创建应用目录、恢复备份内容，也不会让它在启动时自动挂载。

:::single-choice{#creating-filesystems-after-mkfs}
创建文件系统后，哪项操作仍需单独完成？

::option[把它挂载到预期目录。]{#creating-filesystems-mount-separate .correct explanation="格式化写入文件系统结构，而挂载会把文件系统附加到可见目录树。"}
::option[为块设备分配任何容量。]{#creating-filesystems-capacity explanation="底层分区或逻辑设备已经提供了将被格式化的容量。"}
::option[从头创建内核的 `/dev` 目录。]{#creating-filesystems-create-dev explanation="设备节点管理独立于格式化单个目标。"}
:::

请只在[管理 Linux 分区和文件系统](https://labex.io/zh/labs/comptia-manage-linux-partitions-and-filesystems-590845)实验的可丢弃辅助磁盘上练习。

## 总结

现在，你可以把创建文件系统描述为经过核实的破坏性操作。

1. 将 `mkfs` 视为分派到特定格式工具的前端。
2. 核实持久身份、现有签名和所有活动使用者。
3. 根据支持情况和恢复要求选择文件系统。
4. 挂载前检查生成的类型、标签和 UUID。
