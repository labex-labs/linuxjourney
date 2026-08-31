---
lesson_id: "listing-devices"
course_id: "devices"
lang: "zh"
order_index: 6
title: "lsusb、lspci 与 lsscsi"
description: "学习如何检查 USB 拓扑、PCI 功能、SCSI 层设备及其活动驱动程序。"
meta_title: "lsusb、lspci 与 lsscsi - 设备"
meta_description: "了解如何列出并检查 Linux 系统上的 USB、PCI 和 SCSI 硬件。本指南介绍 lsusb、lspci 和 lsscsi 命令，包括使用 lsusb -t 查看设备树。"
meta_keywords: "lsusb, lspci, lsscsi, lsusb -t, 列出 USB 设备, 列出 PCI 设备, 列出 SCSI 设备, Linux 硬件, 设备信息"
---

Linux 提供针对总线和子系统的清单工具。每条命令展示不同视角，因此应结合标识符、拓扑、驱动程序、sysfs 路径和日志，而不要期待某个工具提供完整的硬件清单。

## 检查 USB 设备

`lsusb` 列出 USB 子系统可见的设备：

```bash
$ lsusb
```

输出通常包含总线号和设备号、厂商与产品 ID 对，以及来自本地 USB ID 数据库的描述。重新连接或重启后，数字总线/设备地址可能改变，不应将其当作持久身份。

使用以下命令显示控制器、集线器、端口、接口、驱动程序和速度之间的关系：

```bash
$ lsusb -t
```

还可以查看详细的描述符输出，但部分信息需要较高的读取权限。不要仅仅为了消除检查命令的权限提示，就授予范围过大的 USB 设备权限。

:::single-choice{#listing-devices-usb-tree}
哪个命令以拓扑树形式显示 USB 设备？

::option[`lspci -k`]{#listing-devices-lspci-tree explanation="它列出 PCI 功能和内核驱动程序信息，而不是 USB 拓扑。"}
::option[`lsscsi -t`]{#listing-devices-lsscsi-tree explanation="这不是本课介绍的 USB 树命令。"}
::option[`lsusb -t`]{#listing-devices-lsusb-tree .correct explanation="树选项显示控制器和集线器下的设备，以及端口和接口关系。"}
:::

## 检查 PCI 功能

`lspci` 列出在 PCI 和 PCI Express 总线上发现的功能：

```bash
$ lspci
```

内部和外部连接的 PCIe 设备可能包括图形、网络、存储、USB、音频和桥接控制器。使用以下命令显示当前使用的内核驱动程序和候选模块：

```bash
$ lspci -k
```

PCI 控制器出现在列表中，并不能证明其后的每个设备都已初始化或处于健康状态。排查问题时应检查驱动程序绑定和内核日志。

:::single-choice{#listing-devices-pci-driver}
哪个命令会在 PCI 列表中添加内核驱动程序信息？

::option[`lspci -k`]{#listing-devices-lspci-k .correct explanation="-k 选项显示当前内核驱动程序和能够处理每个 PCI 设备的模块。"}
::option[`lsusb -t`]{#listing-devices-usb-not-pci explanation="它描述 USB 层次结构和接口驱动程序。"}
::option[`lsblk -f`]{#listing-devices-lsblk-filesystem explanation="它报告块设备和文件系统字段，而不是 PCI 驱动程序绑定。"}
:::

## 检查 SCSI 层设备

`lsscsi` 列出通过 Linux SCSI 中间层表示的设备：

```bash
$ lsscsi
```

其中可能包括原生 SCSI 设备，以及通过 SCSI 兼容层呈现的 SATA、USB 存储或虚拟磁盘。NVMe 命名空间通常属于不同子系统，`lsscsi` 无法提供其完整清单。

要查看包含多种块设备类型、以存储为中心的层次结构，还应使用 `lsblk`：

```bash
$ lsblk -o NAME,TYPE,SIZE,MODEL,SERIAL,TRAN,FSTYPE,MOUNTPOINTS
```

:::single-choice{#listing-devices-lsscsi-scope}
`lsscsi` 主要列出什么？

::option[只列出每个 NVMe 命名空间和控制器。]{#listing-devices-only-nvme explanation="NVMe 使用自己的子系统和工具，尽管相关块设备视图可能出现在其他地方。"}
::option[只列出名称以 `.scsi` 结尾的文件。]{#listing-devices-scsi-extension explanation="该命令查询内核设备接口，而不是文件扩展名。"}
::option[通过 Linux SCSI 中间层表示的设备。]{#listing-devices-scsi-mid-layer .correct explanation="该命令报告 SCSI 主机、目标、逻辑单元，以及可用的相应设备节点。"}
:::

## 解读清单结果

描述通常来自本地 ID 数据库，可能过于笼统或已经过时。列出的设备可能没有正常工作的驱动程序，虚拟化环境也可能提供模拟或半虚拟化硬件。应根据权限和所调查的问题，将结果与 `udevadm info`、sysfs、`lsblk`、网络工具以及 `journalctl -k` 或 `dmesg` 相互关联。

这些实用工具可能分别打包，常见软件包包括 `usbutils`、`pciutils` 和 `lsscsi`。命令缺失时，应使用发行版软件包管理器，而不是下载来源不明的替代程序。

:::single-choice{#listing-devices-listed-not-working}
在 `lspci` 中看到设备，是否能证明它的驱动程序已活动并正常工作？

::option[不能；还应检查驱动程序绑定和相关内核消息。]{#listing-devices-needs-correlation .correct explanation="枚举只能证明 PCI 功能可见，不能证明更高层的初始化成功。"}
::option[能；PCI 枚举会执行完整功能测试。]{#listing-devices-complete-test explanation="列表不会运行每项硬件功能，也不会验证服务行为。"}
::option[能；`lspci` 会自动安装合适的驱动程序。]{#listing-devices-installs-driver explanation="该命令是清单工具，不会安装驱动程序软件包。"}
:::

可通过[在 Linux 中探索硬件设备](https://labex.io/labs/comptia-explore-hardware-devices-in-linux-590861)，在同一台受控主机上比较这些子系统视图。

## 总结

现在，你可以为所调查的设备子系统选择清单命令。

1. 使用 `lsusb` 和 `lsusb -t` 查看 USB 身份与拓扑。
2. 使用 `lspci -k` 查看 PCI 功能和驱动程序绑定。
3. 使用 `lsscsi` 查看 SCSI 层设备，使用 `lsblk` 查看块设备拓扑。
4. 将枚举结果与驱动程序、sysfs 和内核消息关联。
