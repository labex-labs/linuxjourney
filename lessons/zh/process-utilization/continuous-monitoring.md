---
lang: "zh"
title: "持续监控"
meta_description: "使用 sar 学习持续的 Linux 系统监控。了解安装、数据收集以及如何分析历史资源使用情况以优化性能。立即开始！"
meta_keywords: "sar, sysstat, Linux 监控，系统性能，持续监控，初学者，教程，指南"
---

## Lesson Content

当您的机器出现问题时，这些监控工具很有用，但是当您不查看时，那些出现问题的机器怎么办？对于这些情况，您需要使用持续监控工具，它可以收集、报告和保存您的系统活动信息。在本课程中，我们将介绍一个非常棒的工具：**sar**。

### Installing sar

Sar 是一个用于对系统进行历史分析的工具。首先，通过安装 `sysstat` 软件包来确保您已安装它：`sudo apt install sysstat`。

### Setting up data collection

通常，一旦您安装了 `sysstat`，您的系统将自动开始收集数据。如果它没有自动收集，您可以通过修改 `/etc/default/sysstat` 中的 `ENABLED` 字段来启用它。

### Using sar

```bash
sudo sar -q
```

此命令将列出从当天开始的详细信息。

```bash
sudo sar -r
```

这将列出从当天开始的内存使用详细信息。

```bash
sudo sar -P
```

这将列出 CPU 使用的详细信息。

要查看不同日期的视图，您可以进入 `/var/log/sysstat/saXX`，其中 `XX` 是您要查看的日期。

```bash
sar -q /var/log/sysstat/sa02
```

## Exercise

在您的系统上安装 sar，并开始收集和分析您的系统资源利用率。

## Quiz Question

用于监控系统资源的好工具是什么？

## Quiz Answer

sar
