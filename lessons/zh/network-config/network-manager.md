---
index: 4
lang: "zh"
title: "网络管理器"
meta_title: "网络管理器 - 网络配置"
meta_description: "了解 NetworkManager 守护程序在现代 Linux 网络管理中的作用。学习此工具如何自动化网络配置，以及如何使用 nm-tool 和强大的 nmcli 命令行实用程序与其交互。"
meta_keywords: "NetworkManager, nm-tool, nmcli, Linux 网络管理器，NetworkManager Linux, Linux 网络管理工具，Linux 网络配置，网络配置，Linux 网络"
---

## Lesson Content

对于系统的网络自动配置，通常已经部署了一项服务。大多数现代 Linux 发行版都使用 NetworkManager 守护进程来实现此目的，使其成为**Linux 网络管理**的基石。

### 什么是 Linux 中的网络管理器？

如果您使用的是图形用户界面 (GUI)，您很可能会在桌面的任务栏中看到 **Network Manager Linux** 服务作为一个小程序。此工具管理您的网络硬件和连接信息。例如，在启动时，NetworkManager 会收集有关网络硬件的信息，搜索可用连接（如无线或有线网络），然后激活它们以上网。

### 命令行交互

虽然 GUI 小程序很方便，但也有强大的命令行工具可以与 **networkmanager linux** 服务进行交互。这些对于服务器管理和脚本编写至关重要。

### 使用 nm-tool

`nm-tool` 命令报告 NetworkManager 的当前状态及其管理设备的列表。请注意，在许多现代系统上，`nm-tool` 被认为已弃用，推荐使用 `nmcli`。

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

### 现代 nmcli 工具

`nmcli` 命令是控制和修改 **Linux Network Manager** 的主要命令行实用程序。它允许您直接从终端查看状态、管理连接和配置网络设备。有关其功能的完整列表，请参阅其手册页 (`man nmcli`)。

## Exercise

熟能生巧！虽然 NetworkManager 自动化了大部分网络配置，但了解它管理的底层命令和概念对于故障排除和高级管理至关重要。以下是一些实践实验室，以加强您对 Linux 中网络识别和管理的理解：

1. **[在 Linux 中识别 MAC 和 IP 地址](https://labex.io/zh/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - 练习使用 `ip a` 命令来识别 Linux 系统上的网络寻址信息，包括 MAC 和 IP 地址。
2. **[在 Linux 中管理 IP 寻址](https://labex.io/zh/labs/comptia-manage-ip-addressing-in-linux-592736)** - 学习使用 `ip` 命令和 `dhclient` 配置静态和动态 IP 地址、设置默认网关并验证网络配置。
3. **[使用 ping 和 arp 在 Linux 中探索网络层交互](https://labex.io/zh/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - 使用 `ping` 和 `arp` 来理解网络层和数据链路层如何交互，观察 ARP 的工作原理以及默认网关如何处理流量。

这些实验室将帮助您在实际场景中应用网络识别和配置的概念，并增强对 Linux 网络基础知识的信心。

## Quiz Question

查看如课程所示的 NetworkManager 状态和设备摘要的命令是什么？请仅使用小写的英文命令名称回答。

## Quiz Answer

nm-tool
