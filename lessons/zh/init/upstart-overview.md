---
title: "Upstart 概述"
description: "了解 Upstart 及其事件驱动模型，以及它如何在 Linux 中管理服务。理解 Upstart 作业配置及其作为 init 系统的作用。"
keywords: "Upstart, init 系统，Linux 服务，Ubuntu, SysV, 初学者教程，Linux 指南"
---

## Lesson Content

Upstart 由 Canonical 开发，因此它曾是 Ubuntu 上一段时间的 init 实现；然而，在现代 Ubuntu 安装中，现在使用的是 systemd。创建 Upstart 是为了改进 SysV 的问题，例如严格的启动过程、任务阻塞等。Upstart 的事件和作业驱动模型使其能够响应实时发生的事件。

要确定您是否正在使用 Upstart，如果您的 `/usr/share/upstart` 目录存在，这是一个很好的指示。

作业是 Upstart 执行的操作，事件是从其他进程接收到的消息，用于触发作业。要查看作业列表及其配置：

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

这意味着它将在运行级别 2、3 或 5 时开始设置网络，并在运行级别 0 时停止网络。配置文件的编写方式有很多种，当您查看可用的不同作业配置时，您会发现这一点。

Upstart 的工作方式是：

1. 首先，它从 `/etc/init` 加载作业配置。
2. 一旦发生启动事件，它将运行由该事件触发的作业。
3. 这些作业将产生新的事件，然后这些事件将触发更多的作业。
4. Upstart 会持续这样做，直到完成所有必要的作业。

## Exercise

如果您正在运行 Upstart，请尝试理解 `/etc/init` 中的作业配置。

## Quiz Question

Ubuntu 使用的 init 实现是什么？

## Quiz Answer

upstart
