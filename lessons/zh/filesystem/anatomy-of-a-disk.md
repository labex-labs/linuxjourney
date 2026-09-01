---
lesson_id: "anatomy-of-a-disk"
course_id: "filesystem"
lang: "zh"
order_index: 3
title: "磁盘结构"
description: "了解块设备、分区表、分区和文件系统如何构成彼此独立的存储层。"
meta_title: "磁盘结构 - 文件系统"
meta_description: "探索 Linux 中磁盘的结构。本指南解释磁盘的哪个组件告诉操作系统磁盘如何分区，涵盖 MBR 和 GPT 分区表、不同类型的 Linux 分区及其组织方式。"
meta_keywords: "linux 磁盘，linux 分区，linux 分区类型，磁盘哪个组件告诉操作系统如何分区，硬盘分区组织信息包含什么，MBR, GPT, 分区表，文件系统"
---

存储设备会呈现为 `/dev/sda` 或 `/dev/nvme0n1` 这样的块设备。它可以包含分区表，其中的条目描述各个区域，并把它们呈现为子块设备。分区中可以再保存文件系统、交换空间签名、RAID 成员、加密容器、逻辑卷物理卷或其他数据格式。

这些层彼此独立：并非每块磁盘都有分区表，并非每个分区都包含文件系统，文件系统也可以位于逻辑卷或整个设备上。

## 分区表与边界

分区表记录起始位置、长度、类型标识符和分区方案特有的属性。内核读取这些内容后，创建 `/dev/sda1` 或 `/dev/nvme0n1p1` 这样的分区块设备。

在普通布局中，分区边界不得重叠。从分区表角度看，所有条目之外的空间尚未分配，但其中仍可能残留旧签名或数据。更改分区表不会自动移动文件系统内容来匹配新边界。

:::single-choice{#anatomy-disk-partition-table-role} 什么内容告诉操作系统磁盘分区从哪里开始、在哪里结束？

::option[当前 shell 的工作目录。]{#anatomy-disk-shell-directory explanation="Shell 路径与磁盘上的分区边界无关。"}
::option[磁盘的分区表。]{#anatomy-disk-table-boundaries .correct explanation="分区条目描述内核可以呈现为子块设备的区域。"}
::option[用户账户的主组。]{#anatomy-disk-user-group explanation="账户凭据不定义磁盘几何或分区布局。"}
:::

## MBR 分区

传统的 DOS/MBR 方案把主分区表存放在第一个逻辑扇区中。它包含四个主表条目，其中一个条目可以描述扩展分区，作为一系列链式逻辑分区的容器，从而提供四个以上的可用区域。

使用 32 位扇区地址和 512 字节逻辑扇区时，MBR 常见的容量上限约为 2 TiB。精确寻址能力取决于扇区大小和工具支持。MBR 也没有 GPT 的冗余表头、分区表副本和每分区 GUID。

:::single-choice{#anatomy-disk-mbr-more-than-four} MBR 中的哪个结构允许创建四个以上的可用分区？

::option[包含更多主分区条目的日志分区。]{#anatomy-disk-mbr-journal explanation="文件系统日志与 MBR 表的四条目限制无关。"}
::option[包含逻辑分区的扩展分区。]{#anatomy-disk-mbr-extended .correct explanation="一个主条目可以定义扩展容器，其中以链式方式保存逻辑分区。"}
::option[重新编号条目的文件系统超级块。]{#anatomy-disk-mbr-superblock explanation="文件系统元数据不会扩展磁盘分区表。"}
:::

## GPT 分区

GUID 分区表（GPT）使用 64 位逻辑块地址，通常在磁盘开头附近保存主表头和条目数组，并在磁盘末尾附近保存备份副本。保护性 MBR 可以避免旧式、仅支持 MBR 的软件把磁盘误认为空盘。

每个 GPT 条目都包含分区类型 GUID 和唯一分区 GUID；因此，GPT 并不是只有一种分区类型。可用条目数由分配的分区表和工具决定，通常远多于四个，而且不需要扩展分区或逻辑分区。

GPT 通常用于 UEFI 启动磁盘，但分区方案与固件启动模式是不同概念。UEFI 系统还需要适当的启动文件和 EFI 系统分区；仅有 GPT 并不会让磁盘可启动。

:::single-choice{#anatomy-disk-gpt-identifiers} GPT 分区条目包含哪些标识符？

::option[类型 GUID 和唯一分区 GUID。]{#anatomy-disk-gpt-guids .correct explanation="类型描述预期用途，唯一 GUID 则标识具体的分区条目。"}
::option[所有 GPT 分区共同使用的唯一一种通用类型。]{#anatomy-disk-gpt-one-type explanation="GPT 为不同分区用途定义了许多类型 GUID。"}
::option[创建者登录账户的 UID 和 GID。]{#anatomy-disk-gpt-user-ids explanation="文件系统账户标识符并不是 GPT 分区身份字段。"}
:::

## 文件系统结构取决于具体格式

完成分区后，文件系统创建工具会写入该文件系统规定的结构。许多格式都有超级块、分配元数据、目录记录以及数据区段或数据块等概念，但具体布局、冗余方式和术语并不相同。

例如，ext 文件系统使用 inode 和块组，其他文件系统则通过不同的树或分配结构组织元数据。不要把“引导块、一个超级块、inode 表、数据块”这一简化图套用到每一种文件系统。

:::single-choice{#anatomy-disk-filesystem-layer} 创建分区时会自动在其中创建文件系统吗？

::option[不会；格式化或其他明确用途是独立步骤。]{#anatomy-disk-partition-not-filesystem .correct explanation="分区表只定义块区域，其中的内容仍然彼此独立。"}
::option[会；每个分区都会自动格式化为 ext4。]{#anatomy-disk-auto-ext4 explanation="分区工具不会统一创建 ext4 文件系统。"}
::option[会；GPT 条目本身就是已挂载目录。]{#anatomy-disk-gpt-mounted explanation="分区条目描述存储区域，并不是文件系统挂载点。"}
:::

## 检查当前布局

进行任何修改前，应先使用只读视图：

```bash
$ lsblk -o NAME,PATH,TYPE,SIZE,PTTYPE,PARTTYPE,FSTYPE,MOUNTPOINTS
$ sudo parted --list
```

`PTTYPE` 描述检测到的分区表方案，`PARTTYPE` 表示分区类型标识符，`FSTYPE` 则表示检测到的内容签名。检测结果只是一项证据，并不保证内容健康或可以安全挂载。

设备名称可能变化，残留签名也可能干扰检测。以写模式打开任何分区工具前，应确认型号、序列号、容量、传输方式、持久链接、活动挂载、交换空间、RAID、LVM、加密和备份。

:::single-choice{#anatomy-disk-lsblk-fields} 哪个 `lsblk` 字段用于区分检测到的文件系统内容与分区表方案？

::option[`FSTYPE`]{#anatomy-disk-fstype .correct explanation="`FSTYPE` 报告检测到的文件系统或其他已识别内容签名，`PTTYPE` 则报告分区表方案。"}
::option[`NAME`]{#anatomy-disk-name-field explanation="`NAME` 标记内核块设备条目，并不专门标识内容格式。"}
::option[`SIZE`]{#anatomy-disk-size-field explanation="容量表示大小，而不是文件系统类型。"}
:::

只应在可丢弃存储上使用[管理 Linux 分区和文件系统](https://labex.io/zh/labs/comptia-manage-linux-partitions-and-filesystems-590845)实验练习这些存储层。

## 总结

现在，你可以区分磁盘布局元数据与其中保存的数据格式。

1. 识别整个设备及其分区子设备。
2. 理解 MBR 扩展分区与传统四条目限制的关系。
3. 理解 GPT 的冗余分区表和每分区 GUID。
4. 把创建文件系统视为独立于创建分区的操作。
5. 进行变更前，检查每一层存储及其活动使用者。
