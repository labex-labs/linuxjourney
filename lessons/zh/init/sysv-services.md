---
lang: "zh"
title: "System V 服务"
description: "学习使用命令行工具管理 System V 服务。通过这个适合初学者的 Linux 教程，了解如何列出、启动、停止和重启服务。"
keywords: "System V 服务，Linux 服务，service 命令，SysV init, Linux 教程，Linux 初学者，服务管理，Linux 指南"
---

## Lesson Content

有许多命令行工具可用于管理 Sys V 服务。

### List services

```bash
service --status-all
```

### Start a service

```bash
sudo service networking start
```

### Stop a service

```bash
sudo service networking stop
```

### Restart a service

```bash
sudo service networking restart
```

这些命令并非 Sys V init 系统特有；您也可以使用它们来管理 Upstart 服务。由于 Linux 正试图摆脱更传统的 Sys V init 脚本，因此仍有一些机制来帮助这一过渡。

## Exercise

管理几个服务并更改它们的状态。您观察到了什么？

## Quiz Question

使用 Sys V 停止名为 `peanut` 的服务的命令是什么？

## Quiz Answer

sudo service peanut stop
