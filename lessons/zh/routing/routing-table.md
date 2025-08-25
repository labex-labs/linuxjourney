---
index: 2
lang: "zh"
title: "路由表"
meta_title: "路由表 - 路由"
meta_description: "学习理解 Linux 路由表以及如何使用 route 命令路由数据包。探索网络基础知识中的目标、网关和接口。"
meta_keywords: "Linux 路由表，route 命令，网络路由，Linux 网络，Linux 初学者，Linux 教程，网络指南"
---

## Lesson Content

Look at your machine's routing table:

```plaintext
pete@icebox:~$ sudo route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.224.2   0.0.0.0         UG    0      0        0 eth0
192.168.224.0   0.0.0.0         255.55.255.0   U     1      0        0 eth0
```

### 目标

在第一个字段中，我们有一个目标 IP 地址 192.168.224.0。这意味着任何尝试访问此网络的包都将通过我的以太网电缆 (eth0) 发送出去。如果我是 192.168.224.5 并且想访问 192.168.224.7，我将直接使用网络接口 eth0。

请注意，我们有地址 **0.0.0.0**。这意味着没有指定地址或地址未知。因此，例如，如果我想将一个包发送到 IP 地址 151.123.43.6，我们的路由表不知道它要去哪里，所以它将其表示为 0.0.0.0，因此将我们的包路由到网关。

### 网关

如果我们要发送的包不在同一个网络上，它将被发送到这个网关地址，这个地址恰如其分地被称为通往另一个网络的网关。

### 子网掩码

这是子网掩码，用于确定哪些 IP 地址与哪个目标匹配。

### 标志

- UG - 网络已启动且是网关
- U - 网络已启动

### 接口

这是我们的包将要发出的接口。eth0 通常代表系统上的第一个以太网设备。

## Exercise

熟能生巧！以下是一些动手实验，以巩固您对网络路由和 IP 寻址的理解：

1. **[在 Linux 中识别 MAC 和 IP 地址](https://labex.io/zh/labs/linux-identify-mac-and-ip-addresses-in-linux-592731)** - 练习使用 `ip a` 命令识别网络寻址信息，包括 IP 地址和网络接口，它们是路由表的关键组成部分。
2. **[在 Linux 中管理 IP 寻址](https://labex.io/zh/labs/linux-manage-ip-addressing-in-linux-592736)** - 学习管理 IP 寻址、配置静态 IP、设置默认网关以及验证网络配置，这些都与路由表中找到的条目直接相关。
3. **[在 Linux 中探索 IP 地址类型和可达性](https://labex.io/zh/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** - 使用 `ping` 和 `ip a` 探索 IP 寻址和网络可达性，帮助您了解不同 IP 类型如何交互以及如何确定网络可达性，这反映在路由决策中。

这些实验将帮助您在实际场景中应用概念，并增强网络配置和故障排除的信心。

## Quiz Question

如果我们的路由表不知道，数据包会被路由到哪里？

## Quiz Answer

Gateway
