---
lesson_id: "disk-partitioning"
course_id: "filesystem"
lang: "zh"
order_index: 4
title: "磁盘分区"
description: "学习使用 `parted` 检查、创建和调整分区边界的验证优先工作流程。"
meta_title: "磁盘分区 - 文件系统"
meta_description: "使用 parted 命令学习 Linux 磁盘分区。本指南涵盖如何使用 `sudo parted -l` 查看分区、创建和调整它们的大小。还介绍了流行的图形化替代工具 gparted。"
meta_keywords: "Linux 磁盘分区，parted 命令，sudo parted -l, gparted, gparted 替代工具，fdisk, 磁盘管理，创建分区，调整分区大小，Linux 指南"
---

编辑分区会改变定义存储边界的映射。选错设备、起点或终点，都可能使现有数据无法访问，或覆盖关键元数据。只应在可丢弃的虚拟磁盘上练习；修改有价值的存储前，必须准备一份位于其他位置且经过恢复测试的备份。

## 选择工具

常用工具包括：

- `fdisk`：util-linux 提供的终端分区编辑器，支持 MBR 和 GPT
- `parted`：支持 GPT、MBR 和其他分区表格式的终端及脚本化编辑器
- `gdisk`：以 GPT 为重点的交互式编辑器
- GParted：图形化的分区和文件系统前端

工具能力会不断变化，因此应查阅本机手册和发行版文档。图形界面并不会让破坏性操作变得安全，它仍然修改相同的磁盘元数据。

:::single-choice{#disk-partitioning-fdisk-gpt} 关于当前 Linux `fdisk`，哪个说法正确？

::option[它同时支持 MBR 和 GPT 分区表。]{#disk-partitioning-fdisk-supports-gpt .correct explanation="当前 util-linux fdisk 可以编辑 DOS/MBR、GPT 等多种布局。"}
::option[它只能编辑 GPT，完全不支持 MBR。]{#disk-partitioning-fdisk-only-gpt explanation="专注 GPT 的 `gdisk` 更接近这种描述；fdisk 支持多种标签类型。"}
::option[它可以创建文件系统，但不能编辑分区条目。]{#disk-partitioning-fdisk-filesystem-only explanation="它的核心用途正是查看和编辑分区表。"}
:::

## 识别目标并停止使用

先进行只读清点：

```bash
$ lsblk -o NAME,PATH,TYPE,SIZE,MODEL,SERIAL,TRAN,PTTYPE,FSTYPE,MOUNTPOINTS
$ findmnt --real
$ sudo parted --list
```

应根据持久身份、型号、序列号、容量、传输方式和拓扑确认整个设备，而不能只看 `/dev/sdX`。随后识别所有使用者：已挂载文件系统、交换空间、LVM、RAID、加密、容器、虚拟机、数据库和打开的文件描述符。

按照各层的文档流程卸载或停用所有相关内容。不能仅仅因为工具可以成功打开，就编辑正在运行系统所在磁盘的分区表。以可恢复的形式记录现有分区表，并确认备份位于不同故障域。

:::single-choice{#disk-partitioning-target-identity} 为什么不能把 `/dev/sdb` 这样的设备名作为唯一目标检查？

::option[Linux 从不在 `/dev` 下公开整个磁盘。]{#disk-partitioning-no-whole-disks explanation="整个磁盘通常确实会在 `/dev` 下拥有块设备节点。"}
::option[设备或拓扑变化时，枚举名称可能改变。]{#disk-partitioning-enumeration-changes .correct explanation="字母按发现顺序分配，在后续会话中可能指向另一块磁盘。"}
::option[分区工具只接受文件系统 UUID 作为操作数。]{#disk-partitioning-only-uuid explanation="核实身份后，编辑器通常操作整个块设备的路径。"}
:::

## 在 parted 中检查单个设备

打开已经明确核实的整个设备：

```bash
$ sudo parted /dev/VERIFIED-DISK
```

然后选择统一的显示单位并打印分区表：

```text
(parted) unit MiB
(parted) print free
```

`print free` 显示当前条目和未分配区域。`parted` 命令可能立即更新磁盘元数据，而不是等到最终“保存”，因此必须把交互式提示符视为实时写权限。

:::single-choice{#disk-partitioning-print-free} `parted` 中的 `print free` 有助于显示什么？

::option[可以删除以安全缩小任意文件系统的文件。]{#disk-partitioning-free-files explanation="Parted 读取分区布局，而不是文件系统级文件分配。"}
::option[远程系统中存储的所有备份。]{#disk-partitioning-remote-backups explanation="远程备份清单不属于分区编辑器的职责。"}
::option[现有分区条目和未分配区域。]{#disk-partitioning-free-regions .correct explanation="该视图有助于根据当前分区表和剩余空隙选择边界。"}
:::

## 创建分区条目

`mkpart` 的具体语法取决于分区表类型。以 MiB 为单位的 GPT 示例类似于：

```text
(parted) mkpart data ext4 1MiB 5000MiB
```

这会创建一个包含名称、建议内容类型、起点和终点的分区条目，**不会**创建 ext4 文件系统。格式化是独立的破坏性步骤，只有在内核识别到预期的新分区且其身份得到核实后才能执行。

应采用工具建议的对齐方式，并了解端点是否包含在内以及如何舍入。使用 `print` 和 `lsblk` 检查结果，不要假定请求的十进制边界一定被精确记录。

:::single-choice{#disk-partitioning-mkpart-effect} `parted` 的 `mkpart` 会创建什么？

::option[包含家目录的已挂载 ext4 文件系统。]{#disk-partitioning-mounted-filesystem explanation="创建分区后，格式化和挂载仍是独立操作。"}
::option[原分区内容的完整备份。]{#disk-partitioning-automatic-backup explanation="分区编辑器不会自动创建恢复备份。"}
::option[一个分区表条目，但不会格式化文件系统。]{#disk-partitioning-entry-only .correct explanation="文件系统类型参数会影响分区元数据，但不会运行 `mkfs`。"}
:::

## 调整边界与内容大小

`resizepart NUMBER END` 只会移动分区的结束边界，不会调整其中的文件系统或其他结构。

操作顺序至关重要：

- 扩容时，先扩大外层分区或逻辑设备，再使用对应文件系统支持的工具扩大文件系统。
- 缩容时，先确认文件系统支持缩小；按照其离线或在线要求先缩小文件系统，再缩短外层边界，并确保边界不会越过新的内容终点。

某些文件系统不支持缩小。加密、LVM、RAID 和嵌套布局还会增加更多必须按顺序操作的层。如果设备繁忙，内核也可能拒绝重新读取更改后的分区表，必须受控重启后才能使用新布局。

:::single-choice{#disk-partitioning-shrink-order} 文件系统支持缩小时，哪种顺序可以避免截断仍在使用的文件系统数据？

::option[先缩短分区，再确认文件系统能否放得下。]{#disk-partitioning-shrink-partition-first explanation="先缩短外层容器可能截断文件系统结构和数据。"}
::option[先缩小文件系统，再缩短包含它的分区边界。]{#disk-partitioning-shrink-filesystem-first .correct explanation="外层块设备缩短前，内容必须先适应更小的范围。"}
::option[删除分区表，让文件系统自行重建它。]{#disk-partitioning-delete-table explanation="文件系统在正常缩容过程中不会重建安全的分区表。"}
:::

请只在[管理 Linux 分区和文件系统](https://labex.io/zh/labs/comptia-manage-linux-partitions-and-filesystems-590845)实验指定的辅助虚拟磁盘上操作，不要替换成主机磁盘。

## 总结

现在，你可以把分区编辑描述为分层且具有破坏性的存储操作。

1. 选择支持实际分区表和工作流程的工具。
2. 核实磁盘的持久身份，并停用所有使用者。
3. 写入前检查单位、分区条目和空闲区域。
4. 牢记 `mkpart` 不会创建文件系统。
5. 按安全顺序调整内层内容与外层边界。
