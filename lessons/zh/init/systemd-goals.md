---
lang: "zh"
title: "Systemd 目标"
meta_title: "Systemd 目标 - 初始化"
meta_description: "学习 systemd 单元基础知识和 essential systemctl 命令。了解如何在 Linux 中管理服务、查看状态和启用单元。开始您的旅程！"
meta_keywords: "systemd, systemctl, Linux 服务，单元文件，初学者，教程，指南，Linux 命令"
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

这是一个简单的服务目标。在文件开头，我们看到一个 `[Unit]` 部分。这允许我们为单元文件提供描述，并控制何时激活单元的顺序。下一部分是 `[Service]` 部分；在此之下，我们可以启动、停止或重新加载服务。而 `[Install]` 部分用于依赖项。这只是编写 systemd 文件的冰山一角，因此如果您想了解更多信息，我强烈建议您阅读相关资料。

现在，让我们来看看一些可以与 systemd 单元一起使用的命令：

### List units

```bash
systemctl list-units
```

### View status of unit

```bash
systemctl status networking.service
```

### Start a service

```bash
sudo systemctl start networking.service
```

### Stop a service

```bash
sudo systemctl stop networking.service
```

### Restart a service

```bash
sudo systemctl restart networking.service
```

### Enable a unit

```bash
sudo systemctl enable networking.service
```

### Disable a unit

```bash
sudo systemctl disable networking.service
```

同样，您还没有看到 systemd 深入到什么程度，所以如果您想了解更多，请阅读相关资料。

## Exercise

查看单元状态并启动和停止一些服务。您观察到了什么？

## Quiz Question

启动名为 peanut.service 的服务的命令是什么？

## Quiz Answer

sudo systemctl start peanut.service
