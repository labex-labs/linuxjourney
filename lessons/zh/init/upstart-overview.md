---
index: 3
lang: "zh"
title: "Upstart 概述"
meta_title: "Upstart 概述 - Init"
meta_description: "了解 Upstart、其事件驱动模型以及它如何在 Linux 中管理服务。理解 Upstart 作业配置及其作为 init 系统的作用。"
meta_keywords: "Upstart, init 系统，Linux 服务，Ubuntu, SysV, 初学者教程，Linux 指南"
---

## Lesson Content

Upstart 由 Canonical 开发，因此它曾是 Ubuntu 上的 init 实现；然而，在现代 Ubuntu 安装中，现在使用的是 systemd。Upstart 的创建是为了改进 SysV 的问题，例如严格的启动过程、任务阻塞等。Upstart 的事件和作业驱动模型使其能够响应事件的发生。

要确定您是否正在使用 Upstart，如果您的 `/usr/share/upstart` 目录存在，这是一个很好的指示。

作业是 Upstart 执行的操作，事件是接收自其他进程以触发作业的消息。要查看作业及其配置的列表：

```plaintext
pete@icebox:~$ ls /etc/init
acpid.conf                   mountnfs.sh.conf
alsa-restore.conf            mtab.sh.conf
alsa-state.conf              networking.conf
alsa-store.conf              network-interface.conf
anacron.conf                 network-interface-container.conf
```

在这些作业配置中，您会找到关于如何以及何时启动作业的信息。

例如，在 `networking.conf` 文件中，它可能只包含如下简单的内容：

```plaintext
start on runlevel [235]
stop on runlevel [0]
```

这意味着它将在运行级别 2、3 或 5 上开始设置网络，并在运行级别 0 上停止网络。配置文件的编写方式有很多种，当您查看可用的不同作业配置时，您会发现这一点。

Upstart 的工作方式是：

1. 首先，它从 `/etc/init` 加载作业配置。
2. 一旦发生启动事件，它将运行由该事件触发的作业。
3. 这些作业将产生新的事件，然后这些事件将触发更多的作业。
4. Upstart 会持续这样做，直到完成所有必要的作业。

## Exercise

熟能生巧！虽然 Upstart 是一个较旧的 init 系统，但理解进程如何管理以及任务如何调度对于任何 Linux 管理员都至关重要。以下是一些实践实验，旨在加强您对进程管理和任务自动化的理解，这些是 init 系统运行的基础：

1. **[管理和监控 Linux 进程](https://labex.io/zh/labs/comptia-manage-and-monitor-linux-processes-590864)** - 练习与前台和后台进程交互，使用 `ps` 检查它们，使用 `top` 监控资源，并使用 `kill` 终止它们。本实验帮助您理解进程的生命周期，这是 Upstart 等 init 系统所管理的。
2. **[在 Linux 中使用 at 和 cron 调度任务](https://labex.io/zh/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - 学习使用 `at` 调度一次性作业，并使用 `cron` 调度重复任务。这提供了任务自动化的实践经验，这是 init 系统为系统服务提供核心功能。

这些实验将帮助您在实际场景中应用进程控制和任务自动化的概念，从而增强您管理 Linux 系统的信心，无论使用何种特定的 init 系统。

## Quiz Question

Ubuntu 使用的 init 实现是什么？

## Quiz Answer

upstart
