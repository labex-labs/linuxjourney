---
index: 1
lang: "zh"
title: "System V 概述"
meta_title: "System V 概述 - Init"
meta_description: "探索传统的 System V 初始化系统，也称为 SysV 或 init v。本指南涵盖 systemv 如何管理进程、其顺序启动以及运行级别在 Linux 中的作用。了解经典的 initv 进程的基础知识。"
meta_keywords: "System V, systemv, SysV init, systemv init, init v, initv, Linux 运行级别，init 系统，进程管理，Linux 教程"
---

## Lesson Content

init 系统的主要作用是启动和停止必要的进程。Linux 经历了三种主要的 init 实现：System V、Upstart 和 systemd。本课程重点介绍最传统的版本——**System V init**，通常简称为 **SysV** 或直接称为 **systemv**（发音为“System Five”）。

要确定您的系统是否使用 **systemv** 实现，请检查是否存在 `/etc/inittab` 文件。如果该文件存在，那么您很可能正在运行基于 SysV 的发行版。

### System V 如何管理进程

**systemv init** 进程按顺序启动和停止服务。例如，如果一个名为 `foo-b` 的服务依赖于 `foo-a`，那么在 `foo-a` 完全运行之前，`foo-b` 无法启动。**initv** 系统通过使用 shell 脚本来实现这一点。这些脚本位于特定目录中，负责服务的启动和停止。虽然您可以编写自定义脚本，但大多数系统依赖于预先打包好的脚本来管理必要的操作系统服务。

### 优点和缺点

这种顺序方法的优点在于其简单性和可预测性。依赖关系的故障排除很直接，因为您知道 `foo-a` 总是先于 `foo-b` 启动。然而，**init v** 模型的主要缺点是性能，因为服务通常一次只启动一个，与现代并行系统相比，这会导致更慢的启动时间。

### 理解 System V 中的运行级别

在 **systemv** 环境中，机器的状态由**运行级别**（runlevels）定义，编号从 0 到 6。这些模式在不同的 Linux 发行版中可能略有不同，但它们通常遵循以下标准约定：

- 0: 关机 (Shutdown)
- 1: 单用户模式 (Single User Mode)
- 2: 多用户模式，无网络 (Multiuser mode without networking)
- 3: 多用户模式，带网络 (Multiuser mode with networking)
- 4: 未使用 (Unused)
- 5: 多用户模式，带网络和图形界面 (Multiuser mode with networking and GUI)
- 6: 重启 (Reboot)

### Init 脚本和目录

当您的系统启动时，它会检查其配置的运行级别并执行相应的脚本。这些脚本通常位于 **/etc/rc.d/rc[runlevel].d/** 等目录中，或位于中央的 **/etc/init.d** 目录内。以 `S`（Start，启动）开头的脚本在启动时执行，而以 `K`（Kill，终止）开头的脚本在关机时运行。`S` 或 `K` 后面的数字决定了执行顺序。

例如：

```bash
pete@icebox:/etc/rc.d/rc0.d$ ls
K10updates  K80openvpn
```

在这个例子中，切换到运行级别 0（关机）时，将首先运行终止更新服务的脚本，然后运行 OpenVPN 的脚本。您可以在 `/etc/inittab` 文件中找到机器的默认运行级别，也可以在那里更改它。

需要注意的是，在大多数现代 Linux 发行版中，**System V** 已基本被 `systemd` 取代。然而，您可能仍然会在较新的 init 系统中遇到运行级别的概念，因为它们通常提供一个兼容层来支持依赖于 **systemv init** 脚本的遗留服务。

## Exercise

实践造就完美！以下是一些实践实验，可帮助您巩固对 Linux 进程管理和系统配置的理解，这些是 init 系统工作方式的基础：

1. **[管理和监控 Linux 进程](https://labex.io/zh/labs/comptia-manage-and-monitor-linux-processes-590864)** - 练习与前台和后台进程的交互，使用 `ps` 检查它们，使用 `top` 监控资源，并使用 `kill` 终止它们。这直接关系到 init 的“启动和停止必要进程”方面。
2. **[在 Linux 中使用 at 和 cron 调度任务](https://labex.io/zh/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - 学习调度一次性任务和定期任务，这建立在类似于 init 脚本管理服务的方式上的自动化执行概念之上。
3. **[管理 Linux 中的文件和目录权限](https://labex.io/zh/labs/comptia-manage-file-and-directory-permissions-in-linux-590844)** - 了解如何管理文件和目录权限，这是处理系统配置文件和 `/etc/init.d` 等目录中脚本的关键技能。

这些实验将帮助您在实际场景中应用这些概念，并增强您对基本 Linux 系统管理任务的信心。

## Quiz Question

通常用于关机的运行级别是哪个？

## Quiz Answer

0
