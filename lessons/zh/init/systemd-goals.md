---
index: 6
lang: "zh"
title: "Systemd 目标"
meta_title: "Systemd 目标 - Init"
meta_description: "探索 systemd 目标，并学习使用 essential systemctl 命令管理 Linux 服务。本指南涵盖 systemd 单元文件基础知识、如何启动、停止和启用服务以及查看其状态。"
meta_keywords: "systemd, systemctl, Linux 服务，单元文件，systemd 目标，服务管理，systemd 单元，初学者，教程，指南，Linux 命令"
---

## Lesson Content

本课程提供了 systemd 单元文件 (unit file) 的基础概述，以及如何使用 `systemctl`（控制 init 系统的主要工具）来管理它们。我们将介绍单元文件的基本结构以及管理 Linux 服务的必要命令。

### 理解 Systemd 单元文件

A systemd 单元文件是一个纯文本文件，用于描述 systemd 可以管理的某个服务、挂载点、设备或其他资源。以下是一个名为 `foobar.service` 的服务单元文件的基本示例：

```
[Unit]
Description=My Foobar Service
After=network.target

[Service]
ExecStart=/usr/bin/foobar

[Install]
WantedBy=multi-user.target
```

这个简单的服务文件分为几个部分：

- **[Unit]**：此部分包含元数据和依赖信息。`Description` 提供了单元的人类可读名称。像 `After` 和 `Before` 这样的指令控制启动顺序，确保此单元在网络可用后启动。
- **[Service]**：此部分定义了如何管理服务。`ExecStart` 指令至关重要，因为它指定了执行以启动服务的命令。`ExecStop` 和 `ExecReload` 等其他指令可以定义如何停止或重新加载服务。
- **[Install]**：此部分定义了使用 `systemctl` 启用或禁用单元时的行为。`WantedBy` 指令告诉 systemd 将此服务作为特定目标的一部分启动，例如用于标准非图形化启动的 `multi-user.target`。

这只是 systemd 单元文件的一个概览。对于更高级的配置，强烈建议进一步阅读相关主题。

### 必要的 Systemctl 命令

现在，让我们探索您将用于与 systemd 单元交互和管理 Linux 服务的必要 `systemctl` 命令。

### 列出 Systemd 单元

要查看 systemd 当前正在管理的**所有活动单元**，请使用 `list-units` 命令。

```bash
systemctl list-units
```

### 检查单元状态

要查看特定单元的详细状态，包括它是否处于活动状态、是否已启用以及其最新的日志条目，请使用 `status` 命令。

```bash
systemctl status networking.service
```

### 管理服务状态

您可以使用 `start`、`stop` 和 `restart` 来控制服务的运行时状态。

立即启动服务：

```bash
sudo systemctl start networking.service
```

停止正在运行的服务：

```bash
sudo systemctl stop networking.service
```

停止然后再次启动服务：

```bash
sudo systemctl restart networking.service
```

### 启用和禁用服务

启用服务会创建一个符号链接，将其挂接到启动过程中，确保它自动启动。禁用服务则会移除该链接。

启用服务以便在启动时启动：

```bash
sudo systemctl enable networking.service
```

禁用服务以便启动时不要启动：

```bash
sudo systemctl disable networking.service
```

这些命令是现代 Linux 系统中服务管理的基础构建块。掌握它们是您 Linux 之旅中的关键一步。

## Exercise

实践是掌握新技能的关键。这个动手实验将帮助您巩固对管理进程的理解，而这些进程通常由 systemd 服务控制：

1. **[管理和监控 Linux 进程](https://labex.io/zh/labs/comptia-manage-and-monitor-linux-processes-590864)** - 练习与前台和后台进程交互，使用 `ps` 检查它们，使用 `top` 监控资源，使用 `renice` 调整优先级，以及使用 `kill` 终止它们。此实验将为您提供有关 systemd 单元管理运行时效果的实践经验。

此实验将帮助您在真实场景中应用这些概念，并建立对 Linux 进程管理的信心。

## Quiz Question

What is the command to start a service named peanut.service? Please answer in English. The answer is case-sensitive.

## Quiz Answer

sudo systemctl start peanut.service
