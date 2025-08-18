---
lang: "zh"
title: "System V 概述"
meta_description: "了解 System V init、其运行级别以及它如何在 Linux 中管理进程。为初学者和中级用户理解 SysV 基础知识。"
meta_keywords: "System V, SysV init, Linux 运行级别，init 系统，Linux 教程，初学者指南，进程管理"
---

## Lesson Content

init 的主要目的是启动和停止系统上的基本进程。Linux 中 init 有三种主要实现：System V、Upstart 和 systemd。在本课程中，我们将介绍最传统的 init 版本，即 System V init 或 Sys V（发音为“System Five”）。

要查明您是否正在使用 Sys V init 实现，请检查是否存在 `/etc/inittab` 文件；如果存在，您很可能正在运行 Sys V。

Sys V 顺序启动和停止进程。例如，如果您想启动一个名为 `foo-a` 的服务，那么在 `foo-a` 运行之前，`foo-b` 无法工作。Sys V 通过脚本来实现这一点。这些脚本为我们启动和停止服务。我们可以编写自己的脚本，或者大多数时候，使用操作系统中已内置的用于加载基本服务的脚本。

使用此 init 实现的优点是相对容易解决依赖关系，因为您知道 `foo-a` 在 `foo-b` 之前。然而，性能不佳，因为通常一次只有一个进程启动或停止。

使用 Sys V 时，机器的状态由运行级别定义，运行级别设置为 0 到 6。这些不同的模式会因发行版而异，但大多数时候会如下所示：

- 0: Shutdown
- 1: Single User Mode
- 2: Multiuser mode without networking
- 3: Multiuser mode with networking
- 4: Unused
- 5: Multiuser mode with networking and GUI
- 6: Reboot

当您的系统启动时，它会查看您处于哪个运行级别，并执行位于该运行级别配置中的脚本。脚本位于 **/etc/rc.d/rc[runlevel number].d/** 或 **/etc/init.d** 中。以 S（启动）或 K（终止）开头的脚本将分别在启动和关闭时运行。这些字符旁边的数字表示它们运行的顺序。

例如：

```bash
pete@icebox:/etc/rc.d/rc0.d$ ls
K10updates  K80openvpn
```

我们看到，当我们切换到运行级别 0 或关机模式时，我们的机器将尝试运行一个脚本来终止更新服务，然后是 OpenVPN。要查明您的机器正在启动到哪个运行级别，您可以在 `/etc/inittab` 文件中查看默认运行级别。您也可以在此文件中更改您的默认运行级别。

需要注意的一点是：System V 正在慢慢被取代，也许不是今天，甚至不是几年后。但是，您可能会在其他 init 实现中看到运行级别出现。这主要是为了支持那些仅使用 System V init 脚本启动或停止的服务。

## Exercise

如果您正在运行 System V，请将您机器的默认运行级别更改为其他值，看看会发生什么。

## Quiz Question

哪个运行级别通常用于关机？

## Quiz Answer

0
