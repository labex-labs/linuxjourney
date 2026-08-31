---
lesson_id: "device-names"
course_id: "devices"
lang: "zh"
order_index: 3
title: "设备名称"
description: "学习 Linux 如何命名常见存储设备、分区、逻辑设备和持久设备链接。"
meta_title: "设备名称 - 设备"
meta_description: "探索 Linux 中常见的存储和外设名称。本指南介绍 SCSI 磁盘名称（如 sda）的命名惯例、sda 的含义，以及 /dev/null 等伪设备。"
meta_keywords: "Linux 设备名称, Linux 设备名, sda 含义, sd 元素名称, 第二块 SCSI 磁盘第一分区的设备名, /dev, SCSI 设备, 伪设备, PATA 设备"
---

Linux 设备名称反映提供接口的内核子系统和驱动程序，并不总是对应硬件上标示的物理连接器。应了解常见模式，但在更改存储前必须查明当前系统上的实际映射。

## SCSI 层磁盘名称

通过 SCSI 磁盘层呈现的磁盘通常使用 `sd` 名称，其中包括许多 SCSI、SATA、USB 存储和虚拟磁盘：

- `/dev/sda`：一整块磁盘
- `/dev/sdb`：另一整块磁盘
- `/dev/sda3`：`/dev/sda` 上的第 3 个分区
- `/dev/sdb1`：`/dev/sdb` 上的第 1 个分区

字母反映枚举顺序，而不是持久身份。添加控制器、改变固件顺序或连接设备，都可能改变某块磁盘获得的字母。

:::single-choice{#device-names-sdb-first-partition}
按照 `sd` 命名模式，哪个路径表示 `/dev/sdb` 上的第 1 个分区？

::option[`/dev/sda2`]{#device-names-sda-two explanation="它表示当前名为 /dev/sda 的磁盘上的第 2 个分区。"}
::option[`/dev/sdbp1`]{#device-names-sdb-p-one explanation="只有基础名称已经以数字结尾的模式才使用 p 分隔符，普通 sd 名称不使用。"}
::option[`/dev/sdb1`]{#device-names-sdb-one .correct explanation="对于 sd 磁盘，分区号直接追加到整盘名称之后。"}
:::

## 以数字结尾的名称

有些完整设备名称本身已经包含数字，因此其分区名称使用 `p` 作为分隔符：

- `/dev/nvme0n1`：控制器 0 上的 NVMe 命名空间 1
- `/dev/nvme0n1p2`：该命名空间上的第 2 个分区
- `/dev/mmcblk0`：一个 MMC 块设备
- `/dev/mmcblk0p1`：该设备上的第 1 个分区

NVMe 设备通常不会命名为 `/dev/sdX`，而是使用 NVMe 子系统的命名惯例。

:::single-choice{#device-names-nvme-partition}
哪个路径表示 `/dev/nvme0n1` 的第 2 个分区？

::option[`/dev/nvme0n1p2`]{#device-names-nvme-p-two .correct explanation="NVMe 分区名称会在分区号前插入 p。"}
::option[`/dev/nvme0n12`]{#device-names-nvme-no-p explanation="没有分隔符时，末尾数字会与命名空间编号混淆。"}
::option[`/dev/sda2`]{#device-names-nvme-sda explanation="这是 sd 层磁盘分区，并不表示指定的 NVMe 命名空间。"}
:::

## 逻辑与虚拟块设备

Linux 还会创建不与物理磁盘一一对应的块设备：

- `/dev/dm-N`：设备映射器设备，通常还会在 `/dev/mapper/` 下提供描述性链接
- `/dev/mdN`：Linux 软件 RAID 阵列
- `/dev/loopN`：作为环回块设备连接的普通文件

分区、加密层、RAID、逻辑卷和文件系统会形成一个堆栈。应使用 `lsblk` 等工具查看父子关系，而不是只根据名称推断堆栈。

:::single-choice{#device-names-device-mapper-link}
哪个位置通常为设备映射器设备提供描述性链接？

::option[`/dev/mapper/`]{#device-names-mapper-directory .correct explanation="LVM 和磁盘加密等设备映射器用户通常会在该目录公开具名链接。"}
::option[`/dev/null/`]{#device-names-null-directory explanation="/dev/null 是字符设备，不是映射块设备的目录。"}
::option[`/proc/partitions/mapper/`]{#device-names-proc-mapper explanation="这不是设备映射器名称链接的正常路径。"}
:::

## 持久存储链接

用户空间设备管理会在 `/dev/disk/` 下创建链接，常见分组包括：

- `by-id`：硬件或传输标识符
- `by-uuid`：文件系统 UUID
- `by-label`：文件系统标签
- `by-partuuid`：分区表 UUID
- `by-path`：依赖拓扑的路径

应选择与所需稳定对象相匹配的标识符。文件系统 UUID 标识的是文件系统，而不一定是其下的物理磁盘。克隆文件系统可能复制 UUID，因此依赖它之前应验证唯一性。

:::single-choice{#device-names-persistent-config}
在设备特定的配置中，为什么 `/dev/disk/by-id/` 链接通常比 `/dev/sdX` 更合适？

::option[它们会让破坏性写入自动变得可逆。]{#device-names-by-id-reversible explanation="稳定名称不提供快照、备份或写保护。"}
::option[它们会把块设备转换成普通文件。]{#device-names-by-id-regular explanation="该条目是符号链接，解析后仍指向块设备节点。"}
::option[它们根据设备身份生成，而不是根据当前枚举顺序。]{#device-names-by-id-stable .correct explanation="链接目标可以变化，而基于身份的链接仍与同一个已识别设备关联。"}
:::

## 伪设备名称

`/dev/null`、`/dev/zero` 和 `/dev/urandom` 等名称表示内核伪设备，而不是物理存储。`/dev/null` 丢弃写入，并在读取时返回文件结束；`/dev/zero` 提供零字节；`/dev/urandom` 则提供内核随机数生成器产生的字节。

:::single-choice{#device-names-zero-read}
从 `/dev/zero` 读取会产生什么？

::option[未使用存储设备的列表。]{#device-names-zero-storage-list explanation="它是产生字节的字符设备，不是发现命令。"}
::option[由零值字节组成的数据流。]{#device-names-zero-bytes .correct explanation="零伪设备会为读取请求返回空字节。"}
::option[像读取 `/dev/null` 一样立即返回文件结束。]{#device-names-zero-eof explanation="/dev/zero 会持续产生字节，而读取 /dev/null 会返回文件结束。"}
:::

可通过[在 Linux 中探索硬件设备](https://labex.io/labs/comptia-explore-hardware-devices-in-linux-590861)，在尝试分区操作前比较设备名称、持久链接和 `lsblk` 关系。

## 总结

现在，你可以解读常见 Linux 存储名称，而不会把它们当作永久身份。

1. 将 `sdXNUMBER` 识别为 `sd` 磁盘分区。
2. 当完整设备名称已以数字结尾时，使用 `pNUMBER`。
3. 识别设备映射器、RAID 和环回设备等逻辑设备。
4. 根据所需身份选择持久链接。
5. 区分存储名称与内核伪设备。
