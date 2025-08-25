---
index: 7
lang: "zh"
title: "持续监控"
meta_title: "持续监控 - 进程利用率"
meta_description: "通过 sar 学习持续的 Linux 系统监控。了解安装、数据收集以及如何分析历史资源使用情况以提高性能。立即开始！"
meta_keywords: "sar, sysstat, Linux 监控，系统性能，持续监控，初学者，教程，指南"
---

## Lesson Content

当您的机器出现问题时，这些监控工具很有用，但是当您不在场时，那些出现问题的机器该怎么办？对于这些情况，您需要使用持续监控工具，它可以收集、报告和保存您的系统活动信息。在本课程中，我们将介绍一个很棒的工具：**sar**。

### 安装 sar

sar 是一个用于对系统进行历史分析的工具。首先，通过安装 `sysstat` 包来确保您已安装它：`sudo apt install sysstat`。

### 设置数据收集

通常，一旦您安装了 `sysstat`，您的系统将自动开始收集数据。如果它没有，您可以通过修改 `/etc/default/sysstat` 中的 `ENABLED` 字段来启用它。

### 使用 sar

```bash
sudo sar -q
```

此命令将列出从当天开始的详细信息。

```bash
sudo sar -r
```

这将列出从当天开始的内存使用情况的详细信息。

```bash
sudo sar -P
```

这将列出 CPU 使用情况的详细信息。

要查看不同日期的视图，您可以进入 `/var/log/sysstat/saXX`，其中 `XX` 是您要查看的日期。

```bash
sar -q /var/log/sysstat/sa02
```

## Exercise

熟能生巧！以下是一些动手实验，可帮助您加深对系统监控和资源分析的理解：

1. **[管理和监控 Linux 进程](https://labex.io/zh/labs/comptia-manage-and-monitor-linux-processes-590864)** - 练习与前台和后台进程交互，使用 `ps` 检查它们，使用 `top` 监控资源，并使用 `kill` 终止它们。
2. **[Linux top 命令：实时系统监控](https://labex.io/zh/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - 学习使用 `top` 命令的各种选项来排序进程、调整更新间隔、按用户过滤以及关注活动进程，以有效监控系统性能。
3. **[Linux df 命令：磁盘空间报告](https://labex.io/zh/labs/linux-linux-df-command-disk-space-reporting-219188)** - 本实验介绍了 Linux 中的 `df` 命令，这是一个显示已挂载文件系统上磁盘空间使用情况信息的实用程序，这是系统监控的一个关键方面。

这些实验将帮助您在实际场景中应用系统资源监控的概念，并增强分析系统活动的信心。

## Quiz Question

用于监控系统资源的好工具是什么？

## Quiz Answer

sar
