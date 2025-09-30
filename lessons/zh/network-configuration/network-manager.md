---
index: 4
lang: "zh"
title: "网络管理器"
meta_title: "Network Manager - 网络配置"
meta_description: "了解 Linux 中的 NetworkManager，它如何自动化网络配置，以及使用 nm-tool 和 nmcli 命令。通过这份初学者指南开始学习！"
meta_keywords: "NetworkManager, nm-tool, nmcli, Linux 网络，网络配置，Linux 教程，初学者指南"
---

## Lesson Content

当然，如果你希望系统网络自动启动并运行，已经有相应的机制。大多数发行版都使用 NetworkManager 守护进程来自动配置其网络。

如果你使用图形用户界面 (GUI)，你会注意到 NetworkManager 以小程序的形式出现在桌面任务栏的某个位置。正如你所看到的，它管理着你的网络硬件和连接信息。例如，在启动时，NetworkManager 会收集网络硬件信息，搜索连接（无线、有线等），然后激活它们。

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

`nmcli` 命令允许你控制和修改 NetworkManager。有关更多详细信息，请参阅其 man 手册页。

## Exercise

熟能生巧！虽然 NetworkManager 自动化了大部分网络配置，但理解它所管理的底层命令和概念对于故障排除和高级管理至关重要。以下是一些动手实验，以加强你对 Linux 中网络识别和管理的理解：

1. **[在 Linux 中识别 MAC 和 IP 地址](https://labex.io/zh/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - 练习使用 `ip a` 命令识别 Linux 系统上的网络寻址信息，包括 MAC 和 IP 地址。
2. **[在 Linux 中管理 IP 寻址](https://labex.io/zh/labs/comptia-manage-ip-addressing-in-linux-592736)** - 学习配置静态和动态 IP 地址，设置默认网关，并使用 `ip` 命令和 `dhclient` 验证网络配置。
3. **[使用 ping 和 arp 在 Linux 中探索网络层交互](https://labex.io/zh/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - 使用 `ping` 和 `arp` 来理解网络层和数据链路层如何交互，观察 ARP 的实际作用以及默认网关如何处理流量。

这些实验将帮助你在实际场景中应用网络识别和配置的概念，并建立对 Linux 网络基础知识的信心。

## Quiz Question

查看 NetworkManager 信息的命令是什么？

## Quiz Answer

nm-tool
