---
lesson_id: "kernel-overview"
course_id: "kernel"
lang: "zh"
order_index: 1
title: "内核概述"
description: "学习 Linux 内核如何协调硬件、资源、隔离机制和用户空间请求。"
meta_title: "内核概述 - 内核"
meta_description: "从 Linux 内核概述开始你的 Linux 学习之旅，理解它在管理硬件和用户空间方面的核心作用，这是 linuxjourney.com 上的一项基础概念。"
meta_keywords: "Linux 内核, 操作系统, 硬件, 用户空间, Linux 学习之旅, linuxjourney.com, 内核概述"
---

Linux 是操作系统内核：负责管理处理器、内存、设备、进程和通用资源抽象的特权软件。一个完整的 Linux 系统还包括用户空间库、实用工具、服务、shell、图形软件以及发行版策略。

## 硬件资源

处理器执行指令，内存保存活动状态，控制器则连接存储、网络、显示器、输入设备和其他外设。硬件提供的是与架构和设备相关的机制，而不是可供每个应用程序安全使用的统一接口。

内核通过架构代码和设备驱动程序初始化并控制这些资源。它在不同工作负载之间实施访问边界，同时处理中断、DMA 协调、定时器和电源管理事件。

:::single-choice{#kernel-overview-hardware-manager}
在 Linux 上，通常由哪一层协调设备驱动程序和硬件中断？

::option[每个用户的 shell 历史文件。]{#kernel-overview-shell-history explanation="历史文件记录命令，并不处理硬件执行。"}
::option[软件包仓库索引。]{#kernel-overview-repository-index explanation="仓库元数据描述软件包，而不是实时硬件事件。"}
::option[内核。]{#kernel-overview-kernel-layer .correct explanation="特权内核代码将硬件事件和驱动程序操作连接到受控的系统接口。"}
:::

## 内核职责

主要职责包括：

- 在 CPU 上调度可运行线程
- 创建并隔离虚拟地址空间
- 实施进程凭据、权限和安全策略
- 提供文件系统、网络、IPC 和设备接口
- 处理信号、定时器和进程生命周期
- 分配、统计并回收资源

Linux 通常被称为单体内核，因为核心服务和许多驱动程序都在同一个特权内核地址空间中执行。它同时也支持模块化：受支持的组件可以作为内核模块加载和卸载。特权内核代码中的缺陷可能危及整个系统，因此内核更新和模块来源对安全至关重要。

:::single-choice{#kernel-overview-scheduler-role}
内核调度器管理什么？

::option[用户下一篇阅读哪个文档页面。]{#kernel-overview-documentation explanation="学习导航不属于内核调度。"}
::option[哪些可运行线程获得 CPU 执行时间。]{#kernel-overview-thread-scheduling .correct explanation="调度器根据策略、优先级、亲和性和 CPU 可用性选择执行上下文。"}
::option[管理员应信任哪个仓库签名密钥。]{#kernel-overview-repository-key explanation="信任配置属于软件包管理策略。"}
:::

## 用户空间

用户空间包含普通进程：init 和服务、命令行工具、语言运行时、数据库、shell 以及桌面应用程序。硬件特权机制会阻止这些程序直接执行许多敏感指令或访问任意内核内存。

进程通过系统调用请求内核工作，并与文件描述符、套接字、设备节点、procfs、sysfs、netlink 和内存映射等公开接口交互。库通常会将这些接口封装成更高层的 API。

用户空间中的 root 按照策略拥有很高的授权，但通常仍在处理器的用户模式中执行。用户身份和 CPU 特权模式是两个不同的概念。

:::single-choice{#kernel-overview-root-user-mode}
普通的 root 用户应用程序会在内核模式下执行全部指令吗？

::option[会；UID 0 会永久将每条指令都切换到 ring 0。]{#kernel-overview-root-ring-zero explanation="普通 root 进程仍然是用户空间进程。"}
::option[会；root 应用程序会自动变成可加载内核模块。]{#kernel-overview-root-module explanation="用户可执行文件不会因为所有者 UID 而转化为内核代码。"}
::option[不会；它通常在用户模式下运行，并通过受控接口进入内核。]{#kernel-overview-root-userspace .correct explanation="root 凭据影响授权，而处理器模式只在进入和执行内核代码时改变。"}
:::

## 边界与抽象

内核向外提供虚拟进程、文件、套接字和地址空间，而不是直接暴露原始物理设备。这些抽象有助于隔离和可移植性，但本身并不是完美的安全边界。命名空间、cgroup、能力、安全模块、seccomp 和虚拟化提供了专门的附加控制。

排查问题时，应判断行为归哪一层所有：应用程序、库、系统调用接口、文件系统、驱动程序、内核子系统、固件还是硬件。使用来自错误层面的证据，可能导致错误的修复方案。

:::single-choice{#kernel-overview-system-call-boundary}
什么是系统调用？

::option[用户空间对内核服务发出的受控请求。]{#kernel-overview-controlled-request .correct explanation="处理器会通过规定的接口进入内核模式，由内核验证并执行操作。"}
::option[绕过所有访问控制检查的直接命令。]{#kernel-overview-bypass-checks explanation="许多验证和授权检查正是在系统调用处进行的。"}
::option[包含设备驱动程序的软件包归档。]{#kernel-overview-package-archive explanation="软件包可以分发软件，但系统调用是运行时执行接口。"}
:::

可通过[在 Linux 中管理内核模块](https://labex.io/labs/comptia-manage-kernel-modules-in-linux-590865)，在受控环境中观察内核的一个模块化组成部分。

## 总结

现在，你可以把内核置于物理资源与相互隔离的用户空间进程之间来理解。

1. 理解驱动程序和架构代码与硬件控制的关系。
2. 识别调度、内存、安全、文件系统和网络方面的职责。
3. 将 root 凭据与处理器内核模式视为不同概念。
4. 在受控的运行时接口处定位用户空间与内核的交互。
