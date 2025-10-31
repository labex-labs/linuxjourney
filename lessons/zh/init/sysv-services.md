---
index: 2
lang: "zh"
title: "System V 服务"
meta_title: "System V 服务 - Init"
meta_description: "了解如何在 Linux 中管理传统的 System V (SysV) 服务。本指南涵盖使用 `service` 命令在 System V init 系统上列出、启动、停止和重启服务。"
meta_keywords: "system v, sysv init, linux 服务，service 命令，管理 linux 服务，启动服务，停止服务，重启服务，linux system v"
---

## Lesson Content

**System V**（或 SysV）是类 Unix 操作系统中的经典初始化系统之一。尽管许多现代 Linux 发行版已转向如 `systemd` 等较新的系统，但了解如何管理 **System V** 服务仍然是一项宝贵的技能，因为许多系统都保持了向后兼容性。

### service 命令

与 **System V** init 系统上的服务交互的主要工具是 `service` 命令。它充当一个包装脚本，简化了控制服务的流程。

### 列出所有服务

要查看所有可用服务及其当前状态的概览，您可以使用 `--status-all` 标志。此命令会列出每个服务，并指示它是正在运行（`+`）、已停止（`-`）还是状态未知（`?`）。

```bash
service --status-all
```

### 控制特定服务

要管理单个服务，您需要指定服务名称，后跟 `start`（启动）、`stop`（停止）或 `restart`（重启）等操作。这些操作需要管理员权限，因此您通常会使用 `sudo`。

要启动一个服务，例如网络服务：

```bash
sudo service networking start
```

要停止一个正在运行的服务：

```bash
sudo service networking stop
```

要停止然后立即启动一个服务（这对于应用配置更改很有用）：

```bash
sudo service networking restart
```

这些命令并非 **System V** init 系统独有；您通常也可以使用它们来管理 Upstart 服务。随着 Linux 发行版的不断发展，`service` 命令等兼容层被保留下来，以帮助缓解从传统 init 脚本的过渡。

## Exercise

实践造就完美！以下是一些实践实验室，可帮助您巩固对进程和任务管理的理解，这是管理 Linux 服务的基础：

1. **[管理和监控 Linux 进程](https://labex.io/zh/labs/comptia-manage-and-monitor-linux-processes-590864)** - 在真实的 Linux 环境中练习与进程的交互、检查、监控和终止。
2. **[使用 at 和 cron 在 Linux 中安排任务](https://labex.io/zh/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - 学习使用 `at` 进行一次性作业和使用 `cron` 进行定期任务来自动化任务，这是服务自动化的关键技能。

这些实验室将帮助您在实际场景中应用这些概念，并增强您对系统操作管理的信心。

## Quiz Question

在 System V 系统上停止名为 `peanut` 的服务的完整命令是什么？请注意大小写，提供准确的英文命令。

## Quiz Answer

sudo service peanut stop
