---
lesson_id: "dev-directory"
course_id: "devices"
lang: "zh"
order_index: 1
title: "/dev 目录"
description: "学习 Linux 如何通过 `/dev` 下的节点公开设备接口和伪设备。"
meta_title: "/dev 目录 - 设备"
meta_description: "了解 Linux 中 /dev 目录的用途。本指南介绍 dev 文件夹是什么、如何使用 ls /dev 探索它，以及设备文件在系统硬件中的作用。"
meta_keywords: "Linux 中的 dev, Linux /dev 目录, Linux dev 文件夹, ls /dev, Linux dev 命令, 设备文件, 设备节点, Linux 设备"
---

Linux 通过称为设备节点的特殊文件系统对象公开许多内核设备接口。它们通常出现在 `/dev` 下，同一目录中还有实用的符号链接和通信端点。打开设备节点会让应用程序连接到内核驱动程序，而不是读取普通文件中存储的字节。

## 探索 `/dev`

列出目录，但不要解引用或读取设备：

```bash
$ ls -l /dev
```

其中的条目可以代表物理存储、终端、输入接口、逻辑设备或内核提供的伪设备。并非每个硬件组件都需要自己的用户可见节点，同一个设备也可能通过多个链接或接口表示。

长列表的第一个字符表示文件系统对象类型。字符设备节点和块设备节点分别显示为 `c` 和 `b`；后续课程会介绍这些类型及其主设备号和次设备号。

:::single-choice{#dev-directory-device-node-purpose}
程序打开 `/dev` 下的设备节点时会发生什么？

::option[它始终读取一个保存硬件副本的普通磁盘文件。]{#dev-directory-ordinary-copy explanation="设备节点是特殊对象，不会像普通文件一样存储设备数据副本。"}
::option[它访问由内核驱动程序实现的接口。]{#dev-directory-kernel-interface .correct explanation="设备节点操作会根据节点的设备身份路由到内核驱动程序行为。"}
::option[它为该设备重新编译驱动程序源代码。]{#dev-directory-recompile-driver explanation="打开接口不会调用编译器或重新构建内核模块。"}
:::

## 伪设备

有些节点提供内核服务，但不对应物理硬件。`/dev/null` 会接收并丢弃写入的数据：

```bash
$ command > /dev/null
```

其他常见示例包括产生零字节的 `/dev/zero`，以及通过内核随机数子系统提供随机字节的 `/dev/urandom`。每个伪设备都有特定语义；不要只根据文件名推断其行为。

:::single-choice{#dev-directory-null-behavior}
`/dev/null` 如何处理写入其中的数据？

::option[将数据保存到下次重启。]{#dev-directory-null-temporary-storage explanation="空设备是数据接收端，不充当临时存储。"}
::option[将数据发送到每个已登录终端。]{#dev-directory-null-broadcast explanation="终端广播与空伪设备无关。"}
::option[丢弃数据。]{#dev-directory-null-discards .correct explanation="空设备会接受写入，但不保留内容。"}
:::

## 动态设备管理

在现代 Linux 系统上，内核支持的 `devtmpfs` 可以随着设备出现而填充基本设备节点。像 `udev` 这样的用户空间设备管理器会处理事件、应用权限和所有权，并创建实用的符号链接或由策略决定的名称。具体职责因系统而异。

在配置中，`/dev/disk/by-id/` 或 `/dev/disk/by-uuid/` 下的稳定链接可能比 `/dev/sda` 这样的探测顺序名称更安全；硬件拓扑或发现顺序变化时，后者可能改变。

:::single-choice{#dev-directory-persistent-link}
为什么管理员可能更愿意在配置中使用 `/dev/disk/by-id/...` 而不是 `/dev/sda`？

::option[基于标识符的链接较少依赖设备发现顺序。]{#dev-directory-stable-identifier .correct explanation="持久链接根据设备属性生成，而不是使用枚举顺序分配的字母。"}
::option[该链接会自动备份设备上的每个块。]{#dev-directory-link-backup explanation="符号链接指向同一设备，不会创建备份数据。"}
::option[该链接会绕过目标设备的所有权限。]{#dev-directory-link-permissions explanation="通过符号链接打开设备仍会到达目标设备，并受其访问控制约束。"}
:::

## 安全交互

标准工具可以打开设备节点，但这并不意味着任意读写都是安全的。读取可能暴露敏感输入或存储内容；写入磁盘、终端或固件接口则可能破坏数据或干扰用户。设备节点权限、组、ACL、能力和服务中介正是为此限制访问。

应先使用只读发现工具，确认确切节点和设备身份，并遵循该设备的专门文档。绝不要在重要系统上通过向陌生的 `/dev` 条目重定向数据来进行实验。

:::single-choice{#dev-directory-direct-write-risk}
为什么应避免向陌生设备节点写入任意数据？

::option[每个设备节点都保证是无害的文本文件。]{#dev-directory-harmless-text explanation="设备节点恰恰不是普通文本文件。"}
::option[该操作可能直接影响硬件、存储或其他内核接口。]{#dev-directory-write-impact .correct explanation="设备写入会调用驱动程序定义的操作，可能造成破坏或中断。"}
::option[Linux 会把每次设备写入都转换成只读列表。]{#dev-directory-write-listing explanation="写入语义由驱动程序决定；内核不会普遍将写入转换成列表。"}
:::

可通过[在 Linux 中探索硬件设备](https://labex.io/labs/comptia-explore-hardware-devices-in-linux-590861)，在受控环境中进行只读检查。

## 总结

现在，你可以将 `/dev` 描述为一组面向内核的实时接口。

1. 区分设备节点与普通文件。
2. 识别 `/dev/null` 等伪设备。
3. 理解动态节点和持久链接与设备管理的关系。
4. 将直接设备访问视为与接口相关且可能具有破坏性的操作。
