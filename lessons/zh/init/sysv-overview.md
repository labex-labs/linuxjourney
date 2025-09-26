---
index: 1
lang: "zh"
title: "System V 概述"
meta_title: "System V 概述 - Init"
meta_description: "了解 System V init、其运行级别以及它如何在 Linux 中管理进程。为初学者和中级用户理解 SysV 基础知识。"
meta_keywords: "System V, SysV init, Linux 运行级别，init 系统，Linux 教程，初学者指南，进程管理"
---

## Lesson Content

init 的主要目的是启动和停止系统上的基本进程。Linux 中有三种主要的 init 实现：System V、Upstart 和 systemd。在本课中，我们将介绍最传统的 init 版本，即 System V init 或 Sys V（发音为‘System Five’）。

要查找您是否正在使用 Sys V init 实现，请检查是否存在 `/etc/inittab` 文件；如果存在，那么您很可能正在运行 Sys V。

Sys V 顺序地启动和停止进程。例如，如果您想启动一个名为 `foo-a` 的服务，`foo-b` 在 `foo-a` 已经运行时才能工作。Sys V 通过脚本实现这一点。这些脚本为我们启动和停止服务。我们可以编写自己的脚本，或者大多数情况下，使用操作系统中内置的脚本来加载基本服务。

使用此 init 实现的好处是解决依赖关系相对容易，因为您知道 `foo-a` 在 `foo-b` 之前启动。然而，性能不是很好，因为通常一次只有一个进程在启动或停止。

使用 Sys V 时，机器的状态由运行级别定义，运行级别从 0 到 6 设置。这些不同的模式因发行版而异，但大多数情况下如下所示：

- 0: Shutdown
- 1: Single User Mode
- 2: Multiuser mode without networking
- 3: Multiuser mode with networking
- 4: Unused
- 5: Multiuser mode with networking and GUI
- 6: Reboot

当您的系统启动时，它会查看您所在的运行级别，并执行位于该运行级别配置中的脚本。脚本位于 **/etc/rc.d/rc[runlevel number].d/** 或 **/etc/init.d**。以 S（start）或 K（kill）开头的脚本将分别在启动和关机时运行。这些字符旁边的数字表示它们运行的顺序。

例如：

```bash
pete@icebox:/etc/rc.d/rc0.d$ ls
K10updates  K80openvpn
```

我们看到，当切换到运行级别 0 或关机模式时，我们的机器将尝试运行一个脚本来终止 updates 服务，然后是 OpenVPN。要找出您的机器启动到哪个运行级别，您可以在 `/etc/inittab` 文件中查看默认运行级别。您也可以在此文件中更改默认运行级别。

需要注意的一点是：在大多数现代 Linux 发行版中，System V 已在很大程度上被 systemd 取代。然而，您可能会在其他 init 实现中看到运行级别出现。这主要是为了支持那些仅使用 System V init 脚本启动或停止的服务。

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of Linux process management and system configuration, which are foundational to how init systems operate:

1. **[管理和监控 Linux 进程](https://labex.io/zh/labs/comptia-manage-and-monitor-linux-processes-590864)** - 练习与前台和后台进程交互，使用 `ps` 检查它们，使用 `top` 监控资源，并使用 `kill` 终止它们。这直接关系到 init 的“启动和停止基本进程”方面。
2. **[使用 at 和 cron 在 Linux 中安排任务](https://labex.io/zh/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - 学习安排一次性任务和定期任务，这建立在自动执行的概念之上，类似于 init 脚本管理服务的方式。
3. **[管理 Linux 中的文件和目录权限](https://labex.io/zh/labs/comptia-manage-file-and-directory-permissions-in-linux-590844)** - 了解如何管理文件和目录权限，这是处理系统配置文件和脚本（如 `/etc/init.d` 中的脚本）的关键技能。

这些实验将帮助您在实际场景中应用这些概念，并增强对基本 Linux 系统管理任务的信心。

## Quiz Question

What runlevel is usually used for shutdown?

## Quiz Answer

0
