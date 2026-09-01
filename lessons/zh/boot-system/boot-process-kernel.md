---
lesson_id: "boot-process-kernel"
course_id: "boot-system"
lang: "zh"
order_index: 4
title: "启动过程：内核"
description: "了解内核如何初始化硬件、运行 initramfs 早期用户空间、到达真实根目录并启动 PID 1。"
meta_title: "启动过程：内核 - 系统启动"
meta_description: "探索 Linux 内核启动过程。了解 initramfs 如何从临时文件系统加载驱动程序以挂载最终启动根分区，以及从加载内核到执行 init 的步骤。"
meta_keywords: "启动根目录，initramfs, 内核启动，启动分区，initramfs ubuntu, /etc/default/grub, Linux 启动过程，根文件系统，内核初始化"
---

控制权到达 Linux 内核后，内核会初始化内存管理、调度、中断、内置驱动程序、安全框架和其他核心子系统。它会解析命令行，并准备启动第一个用户空间进程。

## 为什么需要早期用户空间

简单的根文件系统有时可以只使用内核内置驱动程序挂载。更复杂的系统则需要在访问真实根目录前加载模块和工具，例如：

- 存储控制器或文件系统模块
- 解锁加密根目录
- 组装 LVM 或 RAID
- 为网络根目录配置网络
- 发现设备并解析持久标识符

Initramfs 会把这些组件打包成与内核一起提供的早期用户空间环境。

:::single-choice{#boot-kernel-initramfs-purpose} Initramfs 通常解决什么问题？

::option[在真实根目录可用前，提供所需的早期工具和模块。]{#boot-kernel-early-tools .correct explanation="早期用户空间可以发现并组装仅凭内置支持无法访问的存储。"}
::option[把每个用户的永久家目录保存在固件中。]{#boot-kernel-home-firmware explanation="该归档是启动内容，而不是永久用户数据存储。"}
::option[第一次登录后替换 Linux 内核。]{#boot-kernel-replace-kernel explanation="Initramfs 代码在用户空间运行时，内核仍然保持活动。"}
:::

## Initramfs 与传统 Initrd

现代 initramfs 通常是一个或多个 cpio 归档，往往经过压缩；内核会把它解包到初始根文件系统，并从该环境执行早期 `/init` 程序。

传统 initrd 在概念上是载入 RAM 后端块设备并挂载的文件系统映像。这些术语经常在文件名和引导加载程序命令中宽泛使用，因此应检查实际工具，而不能仅凭名称推断格式。

Initramfs 必须与内核和启动设计匹配。即使内核映像本身有效，缺少模块、设备标识符过时，或遗漏加密和 LVM 工具，都可能使新安装的内核无法启动。

:::single-choice{#boot-kernel-initramfs-format} 现代 initramfs 通常以什么形式提供给内核？

::option[只能通过 HTTP 提供的交互式软件包仓库。]{#boot-kernel-http-repository explanation="早期用户空间可以配置网络访问，但这不是 initramfs 的定义格式。"}
::option[解包到初始根目录的 cpio 归档。]{#boot-kernel-cpio-archive .correct explanation="内核展开归档，并执行其中的早期用户空间初始化程序。"}
::option[磁盘的 GPT 备份表头。]{#boot-kernel-gpt-header explanation="分区表冗余与早期用户空间归档无关。"}
:::

## 到达真实根目录

早期用户空间会解释 `root=` 等参数、等待必要设备、激活存储层并挂载预期根文件系统。随后，它使用根目录切换操作，让该文件系统成为新的 `/`，并尽可能释放临时早期环境。

初始 `ro` 命令行请求可以支持一致性检查和受控启动，但具体顺序取决于发行版。文件系统检查属于用户空间操作；策略允许时，initramfs 或后续 init 系统可以把根目录重新挂载为可读写。

:::single-choice{#boot-kernel-root-switch} 早期用户空间成功挂载预期真实根目录后，会发生什么？

::option[每块磁盘上的分区表都会重新创建。]{#boot-kernel-recreate-tables explanation="切换根目录不会重新分区存储。"}
::option[内核退出，固件恢复普通进程调度。]{#boot-kernel-firmware-schedules explanation="控制权交接后，Linux 内核仍然负责进程和硬件。"}
::option[启动会把根目录视图切换到该文件系统，并继续用户空间启动。]{#boot-kernel-switch-root .correct explanation="临时早期根目录会把控制权交给已安装系统的根目录层次。"}
:::

## 启动 PID 1

内核执行配置的 init 程序，通常通过 `/sbin/init` 等路径找到，也可以由 `init=` 选择。该进程获得 PID 1，并负责主要的用户空间服务环境。

如果没有可用的 init 程序能够执行，内核就无法继续进入正常用户空间系统，通常会报告启动失败或 panic。应调试最早失败的层次：内核与命令行、initramfs 内容、根目录发现、根目录挂载或 PID 1 执行。

:::single-choice{#boot-kernel-pid-one} 在这一简化启动阶段中，内核最后一次主要交接是什么？

::option[以 PID 1 执行第一个用户空间程序。]{#boot-kernel-exec-init .correct explanation="随后由 PID 1 启动服务并达到配置的系统状态。"}
::option[把 `/proc` 变成持久软件包数据库。]{#boot-kernel-proc-package explanation="Procfs 仍然是运行时内核接口。"}
::option[为之后每个进程分配相同 PID。]{#boot-kernel-same-pid explanation="命名空间中的每个活动进程都有自己的 PID。"}
:::

## 总结

现在，你可以追踪从内核启动、早期用户空间到 PID 1 的过程。

1. 区分内核内置初始化与可加载的早期模块。
2. 理解 initramfs 与基于 cpio 的临时根目录及 `/init` 的关系。
3. 追踪存储组装和切换到真实根目录的过程。
4. 把执行 PID 1 视为向用户空间的控制权交接。
