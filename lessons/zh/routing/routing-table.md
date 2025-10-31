---
index: 2
lang: "zh"
title: "路由表"
meta_title: "路由表 - 路由"
meta_description: "理解 Linux 路由表的指南。学习如何解释 route 命令的输出，包括目标、网关、子网掩码 (genmask) 和 eth0 接口。掌握您的 Linux 路由表基础知识。"
meta_keywords: "linux 路由表，linux 路由表，genmask, eth0, route 命令，网络路由，IP 路由，目标，网关，子网掩码，linux 网络"
---

## Lesson Content

**Linux 路由表** 包含决定网络数据包发送去向的规则。每当您的系统需要向一个 IP 地址发送数据包时，它都会查阅此表以找到合适的路径。要查看您机器的 **Linux 路由表**，您可以使用 `route` 命令。

```plaintext
pete@icebox:~$ sudo route -n
内核 IP 路由表
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.224.2   0.0.0.0         UG    0      0        0 eth0
192.168.224.0   0.0.0.0         255.255.255.0   U     1      0        0 eth0
```

### 理解列

`route` 命令的输出被组织成几列，每列都提供有关特定网络路由的具体信息。

### Destination (目标地址)

Destination 列指定一个网络或主机。条目 `192.168.224.0` 指示所有发往该特定网络的数据包。如果数据包的目标地址在此网络内（例如，从 192.168.224.5 到 192.168.224.7），它将通过指定的接口（如 `eth0`）直接发送。

目标地址 `0.0.0.0` 是默认路由。如果路由表中没有针对数据包目标的更具体条目，则使用此路由。

### Gateway (网关)

Gateway 列显示数据包被发送到的路由器。如果数据包不在同一个本地网络上，它将被转发到此网关地址。对于默认路由，这是将您的本地网络连接到其他网络（如互联网）的路由器的 IP 地址。

### Genmask (子网掩码)

`genmask`，即生成掩码，是目标网络的子网掩码。它与目标 IP 一起用于确定数据包是否属于该网络。例如，`genmask` 为 `255.255.255.0` 意味着 IP 地址的前三个八位字节必须与目标的​​前三个八位字节匹配。

### Flags (标志)

这些标志提供有关路由的附加信息：

- **U**: 表示路由已启动并处于活动状态。
- **G**: 表示路由指向一个网关（路由器）。
- **UG**: 表示路由处于活动状态并指向一个网关。

### Iface (接口)

此列指示数据包将通过哪个网络接口发送，例如 `eth0`。`eth0` 通常代表您系统上的第一个以太网适配器。

## Exercise

熟能生巧！以下是一些实践实验，以加强您对网络路由和 IP 地址分配的理解：

1. **[在 Linux 中识别 MAC 地址和 IP 地址](https://labex.io/zh/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - 练习使用 `ip a` 命令来识别网络寻址信息，包括 IP 地址和网络接口，它们是路由表中的关键组成部分。
2. **[在 Linux 中管理 IP 地址分配](https://labex.io/zh/labs/comptia-manage-ip-addressing-in-linux-592736)** - 学习管理 IP 地址分配、配置静态 IP、设置默认网关以及验证网络配置，这些都与路由表中找到的条目直接相关。
3. **[在 Linux 中探索 IP 地址类型和可达性](https://labex.io/zh/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - 使用 `ping` 和 `ip a` 探索 IP 地址分配和网络可达性，帮助您了解不同 IP 类型如何交互以及网络可达性是如何确定的，这反映在路由决策中。

这些实验将帮助您在实际场景中应用概念，并建立对网络配置和故障排除的信心。

## Quiz Question

如果在路由表中找不到目标地址，数据包会被发送到哪里？请用一个英文单词回答，注意大小写。

## Quiz Answer

Gateway
