---
index: 2
lang: "zh"
title: "ping"
meta_title: "ping - 故障排除"
meta_description: "了解如何使用 Linux ping 命令测试网络连接和排除故障。了解 ICMP、TTL 和往返时间，以进行有效的网络诊断。"
meta_keywords: "Linux ping, 网络连接，ICMP, TTL, Linux 网络，Linux 初学者，Linux 教程，ping 命令"
---

## Lesson Content

**ping** 是最简单的网络工具之一，用于测试数据包是否能到达主机。它通过向目标主机发送 ICMP 回显请求（类型 8）数据包并等待 ICMP 回显回复（类型 0）来工作。当主机发出请求数据包并从目标接收到响应时，ping 成功。让我们看一个例子：

```plaintext
pete@icebox:~$ ping -c 3 www.google.com
PING www.google.com (74.125.239.112) 56(84) bytes of data.
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=1 ttl=128 time=29.0 ms
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=2 ttl=128 time=23.7 ms
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=3 ttl=128 time=15.1 ms
```

在这个例子中，我们使用 ping 来检查是否可以访问 `www.google.com`。`-c` 标志（count）用于在达到指定计数后停止发送回显请求数据包。

第一部分表示我们正在向 74.125.239.112 (google.com) 发送 64 字节的数据包，其余部分显示了行程的详细信息。默认情况下，它每秒发送一个数据包。

### icmp_seq

`icmp_seq` 字段用于显示已发送数据包的序列号。在本例中，我发送了 3 个数据包，我们可以看到 3 个数据包都返回了。如果您执行 ping 并且缺少一些序列号，这意味着发生了连接问题，并非所有数据包都已通过。如果序列号乱序，您的连接可能非常慢，因为您的数据包超出了默认的一秒。

### ttl

Time To Live (TTL) 字段用作跳数计数器。每经过一次跳跃，计数器就会减一，一旦跳数计数器达到 0，我们的数据包就会“死亡”。这是为了给数据包一个生命周期；我们不希望数据包永远在网络中传输。

### time

从您发送回显请求数据包到收到回显回复所花费的往返时间。

## Exercise

熟能生巧！以下是一些动手实验，以巩固您对网络连接和 `ping` 命令的理解：

1. **[使用 ping 和 arp 探索 Linux 中的网络层交互](https://labex.io/zh/labs/linux-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - 使用 `ping` 和 `arp` 探索网络和数据链路层交互，并观察默认网关如何处理远程流量。
2. **[探索 Linux 中的 IP 地址类型和可达性](https://labex.io/zh/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** - 利用 `ping` 和 `ip a` 测试本地 TCP/IP 堆栈，验证公共互联网连接，并探索网络可达性。
3. **[模拟 Linux 中的网络层连接](https://labex.io/zh/labs/linux-simulate-network-layer-connectivity-in-linux-592752)** - 学习使用 `ip addr` 分配静态 IP 地址，并在相同和不同子网中通过 `ping` 测试连接。

这些实验将帮助您在实际场景中应用网络可达性和 `ping` 命令的概念，并增强您在 Linux 中进行网络诊断的信心。

## Quiz Question

往返时间测量单位是什么？

## Quiz Answer

ms
