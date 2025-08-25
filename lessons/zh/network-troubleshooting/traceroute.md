---
index: 3
lang: "zh"
title: "traceroute"
meta_title: "traceroute - 故障排除"
meta_description: "了解如何使用 Linux traceroute 命令跟踪网络路由并排除连接故障。为初学者理解 TTL 和数据包路由。"
meta_keywords: "traceroute, Linux 网络，网络故障排除，TTL, Linux 命令，初学者，教程"
---

## Lesson Content

`traceroute` 命令用于查看数据包如何路由。它通过发送 TTL（生存时间）值递增的数据包来工作，从 1 开始。因此，第一个路由器接收到数据包并将 TTL 值减一，从而丢弃数据包。路由器会向我们发送一个 ICMP 时间超出消息。然后，下一个数据包的 TTL 值为 2，因此它会通过第一个路由器，但当它到达第二个路由器时，TTL 为 0，它会返回另一个 ICMP 时间超出消息。Traceroute 以这种方式工作，因为它在发送和丢弃数据包时，会构建一个数据包遍历的路由器列表，直到最终到达目的地并收到 ICMP Echo Reply 消息。

以下是 `traceroute` 的一个简短片段：

```bash
$ traceroute google.com
traceroute to google.com (216.58.216.174), 30 hops max, 60 byte packets
 1  192.168.4.254 (192.168.4.254)  0.028 ms  0.009 ms  0.008 ms
 2  100.64.1.113 (100.64.1.113)  1.227 ms  1.226 ms 0.920 ms
 3  100.64.0.20 (100.64.0.20)  1.501 ms 1.556 ms  0.855 ms
```

每一行代表您和目标之间的路由器或机器。它显示目标的名称及其 IP 地址，最后三列对应于数据包到达该路由器的往返时间。默认情况下，沿路由发送三个数据包。

## Exercise

熟能生巧！以下是一些动手实验，以巩固您对网络路径发现和故障排除的理解：

1. **[在 Linux 中管理 IP 地址](https://labex.io/zh/labs/linux-manage-ip-addressing-in-linux-592736)** - 练习使用 `ip` 命令配置网络设置并使用 `traceroute` 验证连接。
2. **[使用 ping 和 arp 在 Linux 中探索网络层交互](https://labex.io/zh/labs/linux-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - 了解 `ping` 和 `arp` 如何工作以理解网络层交互，这是 `traceroute` 运行的基础。

这些实验将帮助您在实际场景中应用网络诊断概念，并增强您使用 Linux 网络工具的信心。

## Quiz Question

在网络中进行跳跃时，什么值会减一？

## Quiz Answer

TTL
