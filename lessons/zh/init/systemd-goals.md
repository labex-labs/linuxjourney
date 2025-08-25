---
index: 6
lang: "zh"
title: "Systemd 目标"
meta_title: "Systemd 目标 - Init"
meta_description: "学习 systemd 单元基础知识和基本的 systemctl 命令。了解如何在 Linux 中管理服务、查看状态和启用单元。开始你的旅程！"
meta_keywords: "systemd, systemctl, Linux 服务, 单元文件, 初学者, 教程, 指南, Linux 命令"
---

## Lesson Content

我们不会深入探讨编写 systemd 单元文件的细节。但是，我们将简要概述单元文件以及如何手动控制单元。

这是一个基本的服务单元文件：foobar.service

```
[Unit]
Description=My Foobar
Before=bar.target

[Service]
ExecStart=/usr/bin/foobar

[Install]
WantedBy=multi-user.target
```

这是一个简单的服务目标。在文件的开头，我们看到一个 `[Unit]` 部分。这允许我们为单元文件提供描述，并控制何时激活单元的顺序。下一部分是 `[Service]` 部分；在这里，我们可以启动、停止或重新加载服务。而 `[Install]` 部分用于依赖项。这只是编写 systemd 文件的冰山一角，所以如果你想了解更多，我恳请你阅读相关主题。

现在，让我们来看看一些可以与 systemd 单元一起使用的命令：

### 列出单元

```bash
systemctl list-units
```

### 查看单元状态

```bash
systemctl status networking.service
```

### 启动服务

```bash
sudo systemctl start networking.service
```

### 停止服务

```bash
sudo systemctl stop networking.service
```

### 重启服务

```bash
sudo systemctl restart networking.service
```

### 启用单元

```bash
sudo systemctl enable networking.service
```

### 禁用单元

```bash
sudo systemctl disable networking.service
```

同样，你还没有看到 systemd 深入的程度，所以如果你想了解更多，请阅读相关资料。

## Exercise

熟能生巧！这里有一些实践实验室，可以帮助你巩固对进程管理的理解，这些进程通常由 systemd 服务控制：

1. **[管理和监控 Linux 进程](https://labex.io/zh/labs/comptia-manage-and-monitor-linux-processes-590864)** - 练习与前台和后台进程交互，使用 `ps` 检查它们，使用 `top` 监控资源，使用 `renice` 调整优先级，并使用 `kill` 终止它们。这个实验室将为你提供 systemd 单元管理运行时效果的实践经验。

这些实验室将帮助你将概念应用于实际场景，并增强在 Linux 中进行进程管理的信心。

## Quiz Question

启动名为 peanut.service 的服务的命令是什么？

## Quiz Answer

sudo systemctl start peanut.service
