---
lesson_id: "sysfs"
course_id: "devices"
lang: "zh"
order_index: 4
title: "sysfs"
description: "学习 sysfs 如何在 `/sys` 下公开 Linux 内核的实时设备、驱动程序、总线和类别模型。"
meta_title: "sysfs - 设备"
meta_description: "探索 sysfs 是什么及其在 Linux sys 系统中的作用。本指南介绍 Linux /sys 目录这一用于设备信息的虚拟文件系统，并将其与 /dev 进行比较。"
meta_keywords: "sysfs, 什么是 sysfs, /sys, Linux /sys, Linux sys, sys 系统, 虚拟文件系统, Linux 设备, /dev"
---

`sysfs` 是通常挂载在 `/sys` 的虚拟文件系统。它通过目录、符号链接和小型属性文件表示内核对象及其关系。设备发现工具和管理器通过它了解内核当前的设备模型。

## 浏览设备模型

重要的顶层视图包括：

- `/sys/devices/`：物理和逻辑设备层次结构
- `/sys/class/`：按功能类别分组的设备，例如块设备或网络设备
- `/sys/bus/`：总线及其设备和驱动程序
- `/sys/block/`：便于查看块设备的视图
- `/sys/dev/`：按字符或块设备主次设备号索引的链接

`/sys/devices` 以外的许多条目都是指向规范层次结构的符号链接。需要实际父路径时，可用 `readlink -f` 解析链接：

```bash
$ readlink -f /sys/class/block/sda
```

使用其他存储接口的系统上可能没有示例中的名称。

:::single-choice{#sysfs-canonical-device-tree} 哪个 sysfs 子树包含内核的主要设备层次结构？

::option[`/sys/passwords/`]{#sysfs-passwords-tree explanation="sysfs 不是用户身份验证秘密的存储库。"}
::option[`/sys/devices/`]{#sysfs-devices-tree .correct explanation="devices 子树表示设备父子拓扑；类别和总线视图会链接到其中。"}
::option[`/sys/packages/`]{#sysfs-packages-tree explanation="已安装软件包状态由发行版软件包工具维护，而不是由该 sysfs 路径维护。"}
:::

## 读取属性

属性文件公开单个值或控制项。块设备的示例可能包括：

```bash
$ cat /sys/class/block/sda/dev
8:0
$ cat /sys/class/block/sda/ro
0
$ cat /sys/class/block/sda/size
1953525168
```

`dev` 报告主设备号和次设备号。`ro` 报告块设备的只读标志。对于 Linux 块设备，`size` 通常以 512 字节扇区为单位，而不考虑设备的物理扇区大小。必须查阅内核 ABI 文档，确认具体属性的单位和含义。

:::single-choice{#sysfs-dev-attribute} 块设备的 sysfs `dev` 属性通常包含什么？

::option[当前存储在设备上的每个文件。]{#sysfs-file-list explanation="文件系统目录树不会嵌入这个小型设备属性中。"}
::option[安装该硬件的软件包名称。]{#sysfs-package-name explanation="硬件不是由 dev 属性标识的软件包来安装的。"}
::option[它的主设备号和次设备号。]{#sysfs-major-minor .correct explanation="该属性将 sysfs 对象与相应块设备身份关联起来。"}
:::

## 关联 `/sys` 与 `/dev`

`/dev` 包含应用程序为设备 I/O 打开的节点。`/sys` 则公开对象关系、属性、状态和部分控制项。`/dev/sda` 这样的块设备节点可以与 `/sys/dev/block/8:0` 匹配，后者会解析到相关 sysfs 对象。

两个接口相互补充。任何一个都不能单独提供完整的硬件事实清单，而且设备可能在检查过程中消失。

:::single-choice{#sysfs-versus-dev} 哪项说法正确区分了 `/sys` 与 `/dev`？

::option[`/sys` 存储用户文档；`/dev` 存储软件包归档。]{#sysfs-dev-user-files explanation="这两个目录都不承担这些普通数据存储职责。"}
::option[`/sys` 公开内核对象属性；`/dev` 提供用于 I/O 的设备节点。]{#sysfs-dev-distinction .correct explanation="sysfs 为对象及控制项建模，而设备节点将操作路由到字符或块驱动程序。"}
::option[两者都是安装期间一次性创建的静态列表。]{#sysfs-dev-static explanation="随着设备和内核对象出现或消失，它们的可见状态会发生变化。"}
:::

## 安全写入属性

有些 sysfs 属性可写，能够改变电源状态、驱动程序绑定、队列行为、设备授权、LED 或其他实时控制。一次成功的文本写入可能立即影响硬件或服务；它并不等同于编辑持久配置文件。

应阅读相关 ABI 文档和当前值，确定如何持久保存设置，并且只在获得授权的系统上测试。绝不要在 `/sys` 中递归修改权限或写入猜测的值。

:::single-choice{#sysfs-write-risk} 为什么写入 sysfs 属性可能对运行产生重大影响？

::option[每次写入都会在磁盘上创建普通备份副本。]{#sysfs-backup-copy explanation="sysfs 是虚拟文件系统，不会自动备份控制变更。"}
::option[即使属性可写，sysfs 也会忽略所有写入。]{#sysfs-ignore-writes explanation="可写属性存在的目的正是接收受支持的控制值。"}
::option[写入可能调用实时内核或驱动程序控制。]{#sysfs-live-control .correct explanation="可写属性是活动接口，可能立即改变设备行为。"}
:::

可通过[在 Linux 中探索硬件设备](https://labex.io/labs/comptia-explore-hardware-devices-in-linux-590861)，以只读方式浏览 sysfs，并将其与设备节点关联。

## 总结

现在，你可以使用 sysfs 作为实时内核对象的结构化视图。

1. 浏览设备、类别、总线、块设备和设备号视图。
2. 以正确单位逐个读取有文档说明的属性。
3. 将 sysfs 对象与 `/dev` 节点关联。
4. 将可写属性视为实时控制接口。
