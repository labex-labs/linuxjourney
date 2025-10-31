---
index: 4
lang: "zh"
title: "Upstart 任务"
meta_title: "Upstart 任务 - Init"
meta_description: "Linux 环境下使用 Upstart 任务管理服务的指南。学习使用 initctl 工具在 upstart Linux 系统上列出、启动、停止和重启任务。"
meta_keywords: "Upstart 任务，initctl, upstart linux, Linux 服务，系统管理，init 系统，Linux 教程"
---

## Lesson Content

Upstart 是一个基于事件的初始化系统，用于某些 **upstart linux** 发行版，以在系统启动和运行时管理服务和任务。它通过一套作业（jobs）和事件（events）来运作。虽然追踪每个事件的来源可能很复杂，通常需要您检查 `/etc/init` 中的作业配置文件，但更常见的是您需要直接从命令行管理这些作业。`initctl` 实用程序为此目的提供了一套命令。

### 查看作业状态

要查看所有已知 Upstart 作业及其当前状态的列表，请使用 `list` 命令。

```plaintext
initctl list

shutdown stop/waiting
console stop/waiting
...
```

输出显示作业名称、其目标（goal）和当前状态。在示例 `shutdown stop/waiting` 中，作业名称是 `shutdown`，其目标是 `stop`，当前状态是 `waiting`。当您与它们交互时，作业状态和目标将会改变。

要检查特定作业的状态，请使用 `status` 命令。

```plaintext
initctl status networking
networking start/running
```

### 手动控制作业

虽然 `/etc/init` 中的作业配置文件定义了作业如何启动、停止以及如何与事件交互，但您可以使用 `initctl` 手动覆盖这些操作。这对于故障排除或执行管理任务非常有用。

要手动启动一个作业：

```bash
sudo initctl start networking
```

要手动停止一个作业：

```bash
sudo initctl stop networking
```

要手动重启一个作业，这是停止然后启动它的便捷快捷方式：

```bash
sudo initctl restart networking
```

### 发出自定义事件

Upstart 作业由事件触发。您也可以手动“发出”（emit）一个事件，这对于触发自定义作业或用于测试目的非常有用。任何配置为在 `some_event` 上启动的作业都将由以下命令触发。

```bash
sudo initctl emit some_event
```

## Exercise

实践造就完美！虽然 Upstart 没有特定的实验环境，但了解如何调度和管理任务对于控制系统进程至关重要。这是一个强化您对任务管理理解的动手实验：

1. **[在 Linux 中使用 at 和 cron 调度任务](https://labex.io/zh/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - 练习创建、管理和删除一次性任务和定期任务，这些是与 Upstart 等 Linux 环境中服务和任务管理方式相关的基本概念。

此实验将帮助您在实际场景中应用任务自动化的概念，并增强管理系统操作的信心。

## Quiz Question

您将如何手动重启一个名为 `peanuts` 的 Upstart 作业？请提供完整的命令。（注意：答案区分大小写，并且必须是英文。）

## Quiz Answer

sudo initctl restart peanuts
