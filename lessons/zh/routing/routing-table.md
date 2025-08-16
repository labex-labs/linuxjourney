---
lang: "zh"
title: "路由表"
description: "学习理解 Linux 路由表以及如何使用 route 命令路由数据包。探索目标、网关和接口以掌握网络基础知识。"
keywords: "Linux 路由表，route 命令，网络路由，Linux 网络，Linux 初学者，Linux 教程，网络指南"
---

## Lesson Content

查看您机器的路由表：

```plaintext
pete@icebox:~$ sudo route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.224.2   0.0.0.0         UG    0      0        0 eth0
192.168.224.0   0.0.0.0         255.255.255.0   U     1      0        0 eth0
```

### Destination

在第一个字段中，我们有一个目标 IP 地址 192.168.224.0。这意味着任何尝试发送到此网络的包都将通过我的以太网电缆 (eth0) 发送出去。如果我是 192.168.224.5 并且想要到达 192.168.224.7，我将直接使用网络接口 eth0。

请注意，我们有地址 **0.0.0.0**。这意味着没有指定地址或地址未知。因此，例如，如果我想将一个包发送到 IP 地址 151.123.43.6，我们的路由表不知道它将去向何处，因此它将其表示为 0.0.0.0，从而将我们的包路由到 Gateway。

### Gateway

如果我们要发送的包不在同一网络上，它将被发送到此 Gateway 地址，该地址恰如其分地被称为通往另一个网络的 Gateway。

### Genmask

这是子网掩码，用于确定哪些 IP 地址与哪个目标匹配。

### Flags

- UG - 网络已启动且是网关
- U - 网络已启动

### Iface

这是我们的包将要发出的接口。eth0 通常代表您系统上的第一个以太网设备。

## Exercise

查看您的路由表，看看您的数据包可以去往何处。

## Quiz Question

如果我们的路由表不知道，数据包会被路由到哪里？

## Quiz Answer

Gateway
