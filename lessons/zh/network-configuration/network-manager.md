---
lang: "zh"
title: "网络管理器"
description: "了解 Linux 中的 NetworkManager，它如何自动化网络配置，以及使用 nm-tool 和 nmcli 命令。通过此初学者指南开始学习！"
keywords: "NetworkManager, nm-tool, nmcli, Linux 网络，网络配置，Linux 教程，初学者指南"
---

## Lesson Content

当然，如果您希望系统的网络自动运行，已经有相应的工具可以实现。大多数发行版都使用 NetworkManager 守护程序来自动配置其网络。

如果您正在使用 GUI，您会注意到 NetworkManager 以小程序的形式出现在桌面任务栏的某个位置。如您所见，它管理着您网络的硬件和连接信息。例如，在启动时，NetworkManager 会收集网络硬件信息，搜索连接（无线、有线等），然后激活它们。

还有一些命令行工具可以与 NetworkManager 交互：

### nm-tool

`nm-tool` 报告 NetworkManager 的状态及其设备。

```plaintext
pete@icebox:/$ nm-tool
NetworkManager Tool

State: connected (global)

- Device: eth0  [Wired connection 1] -------------------------------------------
  Type:              Wired
  Driver:            pcnet32
  State:             connected
  Default:           yes
  HW Address:        12:3D:45:56:7D:CC

  Capabilities:
    Carrier Detect:  yes

  Wired Properties
    Carrier:         on

  IPv4 Settings:
    Address:         192.168.22.1
    Prefix:          24 (255.255.255.0)
    Gateway:         192.168.22.2

    DNS:             192.168.22.2
```

### nmcli

`nmcli` 命令允许您控制和修改 NetworkManager。有关更多详细信息，请参阅其手册页。

## Exercise

No exercises for this lesson.

## Quiz Question

查看 NetworkManager 信息的命令是什么？

## Quiz Answer

nm-tool
