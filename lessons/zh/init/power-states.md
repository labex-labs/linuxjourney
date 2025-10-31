---
index: 7
lang: "zh"
title: "电源状态"
meta_title: "电源状态 - Init"
meta_description: "了解如何管理 Linux 系统电源状态。本指南涵盖基本的关机、重启和停止命令，以安全地关闭或重新启动您的 Linux 系统。掌握这些基本的 Linux 命令，以进行系统管理。"
meta_keywords: "linux 电源状态，shutdown 命令，reboot 命令，halt 命令，poweroff linux, 重启 linux, linux 系统管理，linux 入门，linux 命令，systemd, init"
---

## Lesson Content

正确管理您的 Linux 系统的电源状态是一项基本技能。虽然您可以使用图形界面，但命令行提供了强大而灵活的选项来关闭或重启您的计算机。这些过程与系统的初始化系统（如 `init` 或 `systemd`）相关联，该系统管理不同的运行状态，包括启动和关机。

### 关闭系统

管理电源状态的主要命令是 `shutdown`。要立即关闭您的 Linux 系统，您可以使用带有 `-h`（halt，暂停）标志和时间参数 `now` 的 `shutdown` 命令。需要管理员权限，因此您需要使用 `sudo`。

```bash
sudo shutdown -h now
```

`-h` 标志指示系统在关闭服务后暂停。在大多数现代硬件上，这将完全关闭计算机电源。您也可以安排在将来的某个时间关机。要以特定分钟数关闭系统，请使用 `+m` 格式：

```bash
sudo shutdown -h +2
```

此命令将在两分钟后关闭您的系统，这对于向其他用户发出警告或允许后台进程正常完成很有用。

### 重启系统

要重启您的 Linux 系统，您可以使用带有 `-r`（reboot，重启）标志的 `shutdown` 命令。

```bash
sudo shutdown -r now
```

一个更直接且常用的替代方法是 `reboot` 命令，它实现了安全重启系统的相同目标。

```bash
sudo reboot
```

### 替代电源命令

为了更直接的控制，您可能还会遇到 `halt` 和 `poweroff` 命令。在许多现代 Linux 发行版中，这些本质上是调用 `shutdown` 命令的快捷方式。例如，运行 `poweroff` 通常等同于运行 `shutdown -h now`。

## Exercise

请随时在虚拟机中练习这些命令。对于更具指导性的练习，请探索全面的[Linux 学习路径](https://labex.io/zh/learn/linux)来练习各种 Linux 技能。

## Quiz Question

包含 `sudo` 以安排系统在 4 分钟后断电的完整命令是什么？请提供完整的英文命令，注意空格和大小写。

## Quiz Answer

sudo shutdown -h +4
