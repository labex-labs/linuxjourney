---
lesson_id: "boot-process-overview"
course_id: "boot-system"
lang: "zh"
order_index: 1
title: "启动过程概述"
description: "了解从平台固件到内核，再到第一个用户空间进程的主要控制权交接。"
meta_title: "启动过程概述 - 系统启动"
meta_description: "清晰概述 Linux 启动过程，详细介绍四个关键阶段：BIOS、引导加载程序、内核和 init。了解从开机到登录提示的完整 Linux 操作系统启动流程。"
meta_keywords: "Linux 启动过程，启动过程 linux, linux 启动，linux 操作系统启动过程，BIOS, 引导加载程序，内核，init, Linux 教程，Linux 指南，新手"
---

启动是一连串信任与控制权转移，把平台复位转变为运行中的用户空间环境。常见 PC 路径可以概括为固件、启动管理器或加载程序、带有可选早期用户空间的内核，以及作为 PID 1 的 init 系统。不同架构、虚拟机、嵌入式系统和容器可能采用不同路径。

## 固件初始化

平台固件会初始化足够的 CPU、内存和设备状态，以选择启动目标。传统 PC 使用 BIOS 约定，当前 PC 通常使用 UEFI。固件设置、启动顺序、平台验证和安全启动策略会决定哪个下一阶段可执行文件获准运行。

固件不一定理解已安装的 Linux 根文件系统。它会根据自身接口定位启动路径，例如选定磁盘上的 BIOS 启动代码，或指向 EFI 系统分区中 EFI 可执行文件的 UEFI 启动条目。

:::single-choice{#boot-overview-first-stage}
典型 PC 复位后，哪个组件首先开始平台初始化？

::option[用户的交互式 shell。]{#boot-overview-shell explanation="Shell 要晚得多才会由用户空间服务或登录流程启动。"}
::option[BIOS 或 UEFI 等平台固件。]{#boot-overview-firmware .correct explanation="Linux 运行前，固件先建立早期硬件状态并选择下一个启动目标。"}
::option[文件系统修复工具。]{#boot-overview-fsck explanation="检查器可能根据启动策略在之后参与流程，但不是初始固件阶段。"}
:::

## 引导加载程序或启动管理器

GRUB 等加载程序可以显示启动条目、把选定 Linux 内核和初始 RAM 文件系统载入内存、构造内核命令行并移交控制权。UEFI 也可以直接加载构建为 EFI 可执行文件的内核，因此独立的多阶段加载程序很常见，但并非普遍必需。

所选内容必须相互匹配：内核版本、initramfs 内容、根目录标识符、安全签名和命令行选项都会影响下一次交接能否成功。

:::single-choice{#boot-overview-loader-role}
Linux 引导加载程序通常承担什么职责？

::option[加载选定内核并传递其命令行。]{#boot-overview-load-kernel .correct explanation="加载程序准备内核映像和参数，通常还包括 initramfs。"}
::option[每次启动时从头创建所有用户账户。]{#boot-overview-create-users explanation="持久账户数据库属于用户空间配置，不会由加载程序重新创建。"}
::option[登录后调度每个应用程序进程。]{#boot-overview-schedule-apps explanation="CPU 调度由运行中的内核负责。"}
:::

## 内核与早期用户空间

内核会按需解压或重定位、初始化核心子系统、解析命令行并发现可用硬件。Initramfs 可以提供存储发现、RAID、加密、LVM、网络或其他组装真实根文件系统所需的模块与早期工具。

预期根目录可用后，早期用户空间会切换到它，内核再执行配置的第一个用户空间程序。由谁执行文件系统检查或重新以读写方式挂载等细节，取决于发行版的启动设计，并不存在一套通用顺序。

:::single-choice{#boot-overview-initramfs-purpose}
系统为什么可能使用 initramfs？

::option[把每个用户的桌面会话永久保存在固件中。]{#boot-overview-desktop-firmware explanation="Initramfs 是启动时文件系统映像，而不是固件会话存储。"}
::option[提供访问真实根文件系统所需的早期工具和驱动程序。]{#boot-overview-early-root-tools .correct explanation="早期用户空间可以组装加密、逻辑、网络或依赖驱动的根存储。"}
::option[登录后替换内核的进程调度器。]{#boot-overview-replace-scheduler explanation="整个运行期间，调度职责仍由内核承担。"}
:::

## PID 1 与系统就绪

第一个用户空间进程获得 PID 1。许多发行版使用 systemd，其他系统则使用 sysvinit、OpenRC、runit、BusyBox init 或专用程序。PID 1 建立用户空间服务环境、回收孤儿子进程并负责关闭系统。

到达 PID 1 并不表示系统已经完全就绪。服务可能仍在启动，存储可能仍在挂载，网络配置可能尚未完成，而图形或控制台登录也只是可能的目标状态之一。

:::single-choice{#boot-overview-final-stage}
什么操作开始主要的用户空间初始化阶段？

::option[每次启动时创建磁盘的保护性 MBR。]{#boot-overview-create-mbr explanation="创建分区表并不是周期性启动阶段。"}
::option[删除所有内核命令行参数。]{#boot-overview-delete-command-line explanation="内核会解析并公开命令行，并不要求删除它。"}
::option[执行 PID 1 init 程序。]{#boot-overview-pid-one .correct explanation="完成根目录设置后，第一个用户空间进程启动或监管达到配置系统状态所需的服务。"}
:::

[自定义 GRUB2 引导菜单](https://labex.io/zh/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)实验演示了一种加载程序配置路径。只能在具备恢复能力的实验系统中应用更改。

## 总结

现在，你可以追踪 Linux 启动的主要控制权交接，而不会把它们误认为通用实现细节。

1. 从固件初始化和目标选择开始。
2. 理解加载程序与内核、initramfs 和命令行选择之间的关系。
3. 通过早期用户空间理解复杂根存储的组装。
4. 把 PID 1 视为服务初始化的开始，而不是系统已经就绪的证明。
