---
lesson_id: "boot-process-init"
course_id: "boot-system"
lang: "zh"
order_index: 5
title: "启动过程：Init"
description: "了解 PID 1 如何初始化用户空间、监管服务、回收子进程并协调关机。"
meta_title: "启动过程：Init - 系统启动"
meta_description: "探索 Linux 启动过程的核心。了解传统 System V、Upstart 和现代标准 systemd 等不同 Linux init 系统，以及它们如何启动并管理机器上的服务。"
meta_keywords: "Linux init, systemd, System V init, Upstart, Linux 启动过程，Linux 教程，Linux 入门，Linux 指南"
---

内核会在 PID 命名空间中以 PID 1 启动第一个用户空间进程。在完整 Linux 系统上，这个 init 进程会建立服务环境。在容器中，PID 1 也可能是小型 init 包装程序或应用程序本身，但仍承担特殊的信号和子进程回收职责。

## PID 1 的职责

Init 系统通常会：

- 启动并监管服务、登录、挂载和其他工作单元
- 根据依赖关系和配置的目标状态安排工作顺序
- 接管并回收孤儿子进程
- 根据策略响应服务失败
- 协调有序关机和重启

具体边界有所不同。设备管理、网络、日志和定时任务可以是由 init 监管的独立程序，而不是直接内置到 PID 1 中。

:::single-choice{#boot-init-pid-one-role}
在自身 PID 命名空间中，哪项职责是 PID 1 所特有的？

::option[每次启动时从源代码编译所有应用程序。]{#boot-init-compile-apps explanation="普通服务启动使用已安装程序，不会重新构建所有软件。"}
::option[定义磁盘的物理扇区大小。]{#boot-init-sector-size explanation="在 init 管理服务前，存储硬件和驱动程序已经公开扇区几何信息。"}
::option[接管并回收孤儿子进程。]{#boot-init-reap-orphans .correct explanation="PID 1 是最终父进程，必须收集终止状态，避免僵尸记录累积。"}
:::

## System V Init 与运行级别

传统 sysvinit 使用 `/etc/inittab` 等配置，以及各运行级别对应的启动与关闭脚本。运行级别表示一种运行模式，但数字级别的含义可能因发行版而异。脚本顺序由约定决定，发行版工具也可以扩展或并行执行。

不能仅仅因为存在 `/etc/init.d/` 就推断主机正在使用哪种 init 系统；即使 PID 1 是其他实现，兼容脚本也可能保留。

:::single-choice{#boot-init-sysv-runlevel}
System V 运行级别表示什么？

::option[由引导加载程序选择的内核版本号。]{#boot-init-runlevel-kernel explanation="内核选择属于加载程序职责，不由 init 运行级别编码。"}
::option[与服务操作关联的已配置运行模式。]{#boot-init-runlevel-mode .correct explanation="SysV 布局把级别与启动或关闭脚本的集合及顺序关联起来。"}
::option[文件系统当前 inode 用量百分比。]{#boot-init-runlevel-inodes explanation="文件系统元数据容量与服务运行模式无关。"}
:::

## 基于事件和依赖的系统

Upstart 引入了事件驱动的作业模型，旧版 Ubuntu 和其他一些系统曾使用它。现在它主要只具有历史或旧系统运维意义。

Systemd 被当前许多通用发行版广泛使用。它把服务、套接字、挂载、定时器、设备、目标和其他资源建模为单元。声明式依赖关系和激活机制让独立工作能够并发推进，同时保留必要顺序。

其他仍在使用的 init 和监管设计包括 OpenRC、runit、s6 和 BusyBox init。“最新”并不是有用的兼容性规则；应识别实际系统运行的内容并使用其文档。

:::single-choice{#boot-init-systemd-unit-model}
Systemd 如何表示服务和挂载等受管资源？

::option[表示为 MBR 主分区条目。]{#boot-init-systemd-partitions explanation="磁盘分区元数据与服务管理器单元无关。"}
::option[只表示为指向 PID 1 可执行文件的硬链接。]{#boot-init-systemd-hard-links explanation="单元是配置和运行时对象，不只是 inode 别名。"}
::option[表示为具有依赖和激活关系的单元。]{#boot-init-systemd-units .correct explanation="不同单元类型使用统一模型表示顺序、状态和监管。"}
:::

## 识别正在运行的 Init

应检查 PID 1，而不是根据已安装文件猜测：

```bash
$ ps -p 1 -o pid,comm,args=
$ readlink /proc/1/exe
```

权限、容器和命名空间会影响看到的内容。在容器中运行命令时，报告的是该命名空间中的 PID 1，不一定是主机 init。识别后，应使用其原生状态和日志工具，不要混用其他 init 家族的命令。

:::single-choice{#boot-init-detect-running}
为什么检查 PID 1 比查看是否存在旧式脚本目录更可靠？

::option[每个 Linux 系统的 PID 1 可执行文件名称都相同。]{#boot-init-same-name explanation="Systemd、sysvinit、BusyBox、容器 init 程序等都可能占据 PID 1。"}
::option[即使正在运行另一种 init 实现，兼容文件也可能存在。]{#boot-init-compatibility-files .correct explanation="活动 PID 1 可执行文件是判断当前 init 系统更有力的证据。"}
::option[旧式目录会在每次启动时自动删除。]{#boot-init-directories-deleted explanation="已安装的兼容文件可以跨启动保留。"}
:::

## 总结

现在，你可以把 init 理解为一种角色，而不是强制要求的单一实现。

1. 理解 PID 1 与服务初始化、子进程回收和关机的关系。
2. 把 System V 运行级别理解为发行版定义的运行模式。
3. 理解 systemd 资源与依赖关系如何映射为单元。
4. 选择工具前，检查相关命名空间中正在运行的 PID 1。
