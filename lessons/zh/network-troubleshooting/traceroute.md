---
index: 3
lang: "zh"
title: "traceroute"
meta_title: "traceroute - 故障排除"
meta_description: "学习如何使用 Linux traceroute 命令来跟踪网络路由和排查连接问题。了解 TTL 和数据包路由，适合初学者。"
meta_keywords: "traceroute, Linux 网络，网络故障排除，TTL, Linux 命令，初学者，教程"
---

## Lesson Content

`traceroute` 命令用于查看数据包的路由方式。它通过发送 TTL（Time To Live，生存时间）值递增的数据包来工作，从 1 开始。因此，第一个路由器接收到数据包并将其 TTL 值减一，从而丢弃该数据包。路由器会向我们发回一个 ICMP Time Exceeded 消息。然后，下一个数据包的 TTL 为 2，因此它会通过第一个路由器，但当它到达第二个路由器时，TTL 为 0，并返回另一个 ICMP Time Exceeded 消息。Traceroute 以这种方式工作，因为它在发送和丢弃数据包时，会构建一个数据包遍历的路由器列表，直到最终到达目的地并收到 ICMP Echo Reply 消息。

以下是 traceroute 的一个简短片段：

```bash
$ traceroute google.com
traceroute to google.com (216.58.216.174), 30 hops max, 60 byte packets
 1  192.168.4.254 (192.168.4.254)  0.028 ms  0.009 ms  0.008 ms
 2  100.64.1.113 (100.64.1.113)  1.227 ms  1.226 ms 0.920 ms
 3  100.64.0.20 (100.64.0.20)  1.501 ms 1.556 ms  0.855 ms
```

每一行代表您与目标之间的路由器或机器。它显示目标的名称及其 IP 地址，最后三列对应于数据包到达该路由器的往返时间。默认情况下，沿途发送三个数据包。

## Exercise

在您的机器上运行 `traceroute` 命令并观察输出。

## Quiz Question

在网络中进行跳跃时，什么值会减一？

## Quiz Answer

TTL
