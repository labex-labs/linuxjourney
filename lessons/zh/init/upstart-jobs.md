---
index: 4
lang: "zh"
title: "Upstart 作业"
meta_title: "Upstart 作业 - Init"
meta_description: "学习使用 initctl 命令在 Linux 中管理 Upstart 作业。了解作业状态、启动、停止和重启服务。提高您的 Linux 系统管理技能。"
meta_keywords: "Upstart 作业，initctl, Linux 服务，系统管理，Linux 教程，初学者指南"
---

## Lesson Content

Upstart 可以触发许多事件和作业运行。不幸的是，没有简单的方法可以查看事件或作业的来源，因此您必须在 `/etc/init` 中仔细检查作业配置。大多数情况下，您根本不需要查看 Upstart 作业配置文件，但您会希望更轻松地控制某些特定作业。在 Upstart 系统中，您可以使用许多有用的命令。

### 查看作业

```plaintext
initctl list

shutdown stop/waiting
console stop/waiting
...
```

您将看到一个 Upstart 作业列表，它们具有不同的状态。在每一行中，作业名称是第一个值，第二个字段（在 `/` 之前）实际上是作业的目标。第三个值（在 `/` 之后）是当前状态。因此，我们看到 `shutdown` 作业最终想要停止，但它目前处于等待状态。作业状态和目标将随着您启动或停止作业而改变。

### 查看特定作业

```plaintext
initctl status networking
networking start/running
```

我们不会深入探讨如何编写 Upstart 作业配置的细节；但是，我们已经知道这些配置中的作业是停止、启动和重新启动的。这些作业还会发出事件，因此它们可以启动其他作业。我们将介绍 Upstart 操作的手动命令，但如果您好奇，应该更深入地研究 `.conf` 文件。

### 手动启动作业

```bash
sudo initctl start networking
```

### 手动停止作业

```bash
sudo initctl stop networking
```

### 手动重启作业

```bash
sudo initctl restart networking
```

### 手动发出事件

```bash
sudo initctl emit some_event
```

## Exercise

熟能生巧！虽然 Upstart 没有特定的实验，但了解如何调度和管理任务对于控制系统进程至关重要。这是一个动手实验，旨在加强您对任务管理的理解：

1. **[在 Linux 中使用 at 和 cron 调度任务](https://labex.io/zh/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - 练习创建、管理和删除一次性任务和重复性任务，这些是与 Linux 环境（如 Upstart 处理的环境）中服务和任务管理方式相关的基本概念。

本实验将帮助您在实际场景中应用任务自动化概念，并增强管理系统操作的信心。

## Quiz Question

我将如何手动重启一个名为 `peanuts` 的 Upstart 作业？

## Quiz Answer

sudo initctl restart peanuts
