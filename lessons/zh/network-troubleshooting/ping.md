---
lang: "zh"
title: "ping"
meta_title: "ping - 故障排除"
meta_description: "学习如何使用 Linux ping 命令来测试网络连接和排除故障。了解 ICMP、TTL 和往返时间，以进行有效的网络诊断。"
meta_keywords: "Linux ping, 网络连接，ICMP, TTL, Linux 网络，Linux 初学者，Linux 教程，ping 命令"
---

## Lesson Content

**ping** 是最简单的网络工具之一，用于测试数据包是否能到达主机。它通过向目标主机发送 ICMP 回显请求（类型 8）数据包，并等待 ICMP 回显回复（类型 0）来工作。当主机发出请求数据包并从目标接收到响应时，ping 成功。我们来看一个例子：

```plaintext
pete@icebox:~$ ping -c 3 www.google.com
PING www.google.com (74.125.239.112) 56(84) bytes of data.
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=1 ttl=128 time=29.0 ms
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=2 ttl=128 time=23.7 ms
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=3 ttl=128 time=15.1 ms
```

在这个例子中，我们使用 ping 来检查是否能访问 <www.google.com>。`-c` 标志（count）用于在达到指定计数后停止发送回显请求数据包。

第一部分表示我们正在向 74.125.239.112 (google.com) 发送 64 字节的数据包，其余部分显示了行程的详细信息。默认情况下，它每秒发送一个数据包。

### icmp_seq

`icmp_seq` 字段用于显示已发送数据包的序列号。在这个例子中，我发送了 3 个数据包，我们可以看到 3 个数据包都回来了。如果你进行 ping 操作时发现某些序列号缺失，这意味着发生了连接问题，并非所有数据包都通过了。如果序列号乱序，你的连接可能非常慢，因为你的数据包超出了默认的一秒。

### ttl

Time To Live (TTL) 字段用作跳数计数器。每经过一次跳跃，计数器就会减一，一旦跳数计数器达到 0，我们的数据包就会“死亡”。这是为了给数据包一个生命周期；我们不希望数据包永远在网络中传输。

### time

从你发送回显请求数据包到收到回显回复所花费的往返时间。

## Exercise

对一个网站执行 ping 操作，并查看你收到的输出。

## Quiz Question

往返时间（roundtrip time）的测量单位是什么？

## Quiz Answer

ms
