---
index: 1
lang: "zh"
title: "System V 概述"
meta_title: "System V 概述 - Init"
meta_description: "了解 System V init、其运行级别以及它如何在 Linux 中管理进程。了解 SysV 基础知识，适用于初学者和中级用户。"
meta_keywords: "System V, SysV init, Linux 运行级别，init 系统，Linux 教程，初学者指南，进程管理"
---

## Lesson Content

init 的主要目的是启动和停止系统上的基本进程。Linux 中 init 有三种主要的实现：System V、Upstart 和 systemd。在本课程中，我们将介绍最传统的 init 版本，System V init 或 Sys V（发音为“System Five”）。

要确定您是否正在使用 Sys V init 实现，请检查是否存在 `/etc/inittab` 文件；如果存在，您很可能正在运行 Sys V。

Sys V 顺序启动和停止进程。例如，如果您想启动一个名为 `foo-a` 的服务，那么在 `foo-a` 运行之前，`foo-b` 无法工作。Sys V 通过脚本来实现这一点。这些脚本为我们启动和停止服务。我们可以编写自己的脚本，或者大多数时候，使用操作系统中已有的用于加载基本服务的脚本。

使用这种 init 实现的优点是相对容易解决依赖关系，因为您知道 `foo-a` 在 `foo-b` 之前。然而，性能不佳，因为通常一次只有一个东西在启动或停止。

使用 Sys V 时，机器的状态由运行级别定义，运行级别设置为 0 到 6。这些不同的模式会因发行版而异，但大多数时候会如下所示：

- 0: 关机
- 1: 单用户模式
- 2: 无网络的多用户模式
- 3: 有网络的多用户模式
- 4: 未使用
- 5: 有网络和 GUI 的多用户模式
- 6: 重启

当您的系统启动时，它会查看您处于哪个运行级别，并执行位于该运行级别配置中的脚本。脚本位于 **/etc/rc.d/rc[运行级别号].d/** 或 **/etc/init.d** 中。以 S（启动）或 K（终止）开头的脚本将分别在启动和关机时运行。这些字符旁边的数字表示它们运行的顺序。

例如：

```bash
pete@icebox:/etc/rc.d/rc0.d$ ls
K10updates  K80openvpn
```

我们看到，当我们切换到运行级别 0 或关机模式时，我们的机器将尝试运行一个脚本来终止更新服务，然后是 OpenVPN。要了解您的机器正在启动到哪个运行级别，您可以在 `/etc/inittab` 文件中查看默认运行级别。您也可以在此文件中更改默认运行级别。

需要注意的一点是：System V 正在慢慢被取代，也许不是今天，甚至不是几年后。但是，您可能会在其他 init 实现中看到运行级别。这主要是为了支持那些仅使用 System V init 脚本启动或停止的服务。

## Exercise

熟能生巧！以下是一些动手实验，旨在加强您对 Linux 进程管理和系统配置的理解，这些是 init 系统运行的基础：

1. **[管理和监控 Linux 进程](https://labex.io/zh/labs/comptia-manage-and-monitor-linux-processes-590864)** - 练习与前台和后台进程交互，使用 `ps` 检查它们，使用 `top` 监控资源，并使用 `kill` 终止它们。这直接关系到 init 的“启动和停止基本进程”方面。
2. **[在 Linux 中使用 at 和 cron 调度任务](https://labex.io/zh/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - 学习调度一次性任务和重复任务，这建立在自动化执行的概念之上，类似于 init 脚本管理服务的方式。
3. **[管理 Linux 中的文件和目录权限](https://labex.io/zh/labs/comptia-manage-file-and-directory-permissions-in-linux-590844)** - 了解如何管理文件和目录权限，这是处理系统配置文件和脚本（例如 `/etc/init.d` 中找到的那些）的关键技能。

这些实验将帮助您在实际场景中应用概念，并增强您对基本 Linux 系统管理任务的信心。

## Quiz Question

哪个运行级别通常用于关机？

## Quiz Answer

0
