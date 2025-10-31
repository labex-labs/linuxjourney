---
index: 3
lang: "zh"
title: "traceroute"
meta_title: "traceroute - 网络故障排除"
meta_description: "掌握 traceroute Linux 命令以跟踪网络路由和排除连接问题。本教程解释了 traceroute 如何使用 TTL 来映射数据包到达目的地的路径。"
meta_keywords: "traceroute, traceroute linux, Linux 网络，网络故障排除，TTL, 数据包路由，Linux 命令，入门，教程"
---

## Lesson Content

traceroute 命令是一个基本的网络诊断工具，用于跟踪数据包从您的计算机到目标主机所经过的路径。通过显示沿途的每一个“跳”（hop）或路由器，它可以帮助您识别网络瓶颈并解决连接问题。traceroute linux 实用程序对于任何系统管理员或网络工程师都至关重要。

### Traceroute 的工作原理

tracertoute 背后的机制在于其巧妙地操纵 IP 数据包头中的“生存时间”（Time To Live, TTL）字段。过程如下：

1. traceroute 发送一个 TTL 值为 1 的探测数据包。
2. 路径上的第一个路由器接收到数据包，将 TTL 减至 0 并丢弃它。然后路由器会向您的计算机发送一个 ICMP“超时”（Time Exceeded）消息。
3. traceroute 记录路由器的 IP 地址和往返时间。
4. 接着它发送另一个数据包，这次 TTL 值为 2。该数据包成功通过第一个路由器，但在第二个路由器处被丢弃，第二个路由器同样发送一个“超时”消息。
5. 此过程重复进行，后续每组数据包的 TTL 都会递增一。通过收集返回“超时”消息的路由器列表，traceroute 就能绘制出完整的路径。
6. 当数据包最终到达目标主机时，目标主机响应一个 ICMP“回显应答”（Echo Reply）消息，过程结束。

### 理解 Traceroute 输出

让我们检查在 Linux 终端中运行 traceroute 的一个示例输出：

```bash
$ traceroute google.com
traceroute to google.com (216.58.216.174), 30 hops max, 60 byte packets
 1  192.168.4.254 (192.168.4.254)  0.028 ms  0.009 ms  0.008 ms
 2  100.64.1.113 (100.64.1.113)  1.227 ms  1.226 ms 0.920 ms
 3  100.64.0.20 (100.64.0.20)  1.501 ms 1.556 ms  0.855 ms
```

每行编号的行代表网络路径上的一个跳点。以下是如何解释这些信息：

- **跳数 (Hop Number):** 第一列（例如 `1`、`2`、`3`）表示路径中路由器的顺序。
- **路由器名称和 IP 地址：** 下一部分显示了该跳的（如果可以解析）主机名和 IP 地址。
- **往返时间 (RTT):** 最后三列显示了发送到该特定跳点的三个探测数据包的往返时间。这些时间以毫秒 (ms) 为单位，有助于您评估旅程中每一步的延迟。

有效使用 traceroute linux 命令可以为您的网络性能和结构提供宝贵的见解。

## Exercise

实践是掌握网络诊断的关键。以下动手实验将帮助您巩固对网络路径发现和使用 traceroute 等工具进行故障排除的理解：

1. **[在 Linux 中管理 IP 地址](https://labex.io/zh/labs/comptia-manage-ip-addressing-in-linux-592736)** - 练习使用 `ip` 命令配置网络设置，然后使用 `traceroute` 验证连接和路由路径。
2. **[在 Linux 中探索与 ping 和 arp 的网络层交互](https://labex.io/zh/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - 了解 `ping` 和 `arp` 如何协同工作以理解网络层交互，这些是 traceroute 运行所依赖的基础概念。

这些实验将帮助您在现实场景中应用网络诊断概念，并增强对基本 Linux 网络工具的信心。

## Quiz Question

What gets decremented by one when making hops across the network? (Please answer in English, paying attention to capitalization.)

## Quiz Answer

TTL
