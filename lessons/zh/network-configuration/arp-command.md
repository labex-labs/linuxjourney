---
lang: "zh"
title: "arp"
description: "了解 Linux ARP 命令以及如何查看 ARP 缓存。理解 ARP 在网络通信中的作用。ARP 初学者指南。"
keywords: "Linux ARP, ARP 缓存，ip neighbour show, 网络命令，Linux 网络，Linux 初学者，Linux 教程"
---

## Lesson Content

请记住，当我们使用 ARP 查找 MAC 地址时，它首先会检查我们系统上本地存储的 ARP 缓存。您可以实际查看此缓存：

```
pete@icebox:~$ arp
Address                  HWtype  HWaddress           Flags Mask            Iface
192.168.22.1            ether   00:12:24:fc:12:cc   C                     eth0
192.168.22.254          ether   00:12:45:f2:84:64   C                     eth0
```

当机器启动时，ARP 缓存实际上是空的；它会随着数据包发送到其他主机而填充。如果我们将数据包发送到 ARP 缓存中不存在的目标，则会发生以下情况：

1. 源主机创建包含 ARP 请求数据包的以太网帧。
2. 源主机将此帧广播到整个网络。
3. 如果网络上的某个主机知道正确的 MAC 地址，它将发送包含 MAC 地址的回复数据包和帧。
4. 源主机将 IP 到 MAC 地址的映射添加到 ARP 缓存，然后继续发送数据包。

您还可以通过 `ip` 命令查看 ARP 缓存：

```bash
ip neighbour show
```

## Exercise

观察您的机器重启后并在网络上执行某些操作时，您的 ARP 缓存会发生什么变化。

## Quiz Question

您可以使用什么命令来查看您的 ARP 缓存？

## Quiz Answer

arp
