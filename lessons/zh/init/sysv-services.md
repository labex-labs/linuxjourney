---
index: 2
lang: "zh"
title: "System V 服务"
meta_title: "System V 服务 - Init"
meta_description: "学习使用命令行工具管理 System V 服务。通过这个适合初学者的 Linux 教程，了解如何列出、启动、停止和重启服务。"
meta_keywords: "System V 服务，Linux 服务，service 命令，SysV init, Linux 教程，Linux 入门，服务管理，Linux 指南"
---

## Lesson Content

有许多命令行工具可用于管理 Sys V 服务。

### 列出服务

```bash
service --status-all
```

### 启动服务

```bash
sudo service networking start
```

### 停止服务

```bash
sudo service networking stop
```

### 重启服务

```bash
sudo service networking restart
```

这些命令并非 Sys V init 系统特有；您也可以使用它们来管理 Upstart 服务。由于 Linux 正在尝试摆脱更传统的 Sys V init 脚本，因此仍然有一些措施来帮助这种过渡。

## Exercise

熟能生巧！以下是一些动手实验，以巩固您对进程和任务管理的理解，这对于在 Linux 中管理服务至关重要：

1. **[管理和监控 Linux 进程](https://labex.io/zh/labs/comptia-manage-and-monitor-linux-processes-590864)** - 在真实的 Linux 环境中练习与进程交互、检查、监控和终止进程。
2. **[在 Linux 中使用 at 和 cron 调度任务](https://labex.io/zh/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - 学习使用 `at` 进行一次性作业和 `cron` 进行重复任务来自动化任务，这是服务自动化的关键技能。

这些实验将帮助您在实际场景中应用概念，并增强管理系统操作的信心。

## Quiz Question

使用 Sys V 停止名为 `peanut` 的服务的命令是什么？

## Quiz Answer

sudo service peanut stop
