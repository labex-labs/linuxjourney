---
index: 5
lang: "zh"
title: "arp"
meta_title: "arp - 网络配置"
meta_description: "了解 Linux ARP 命令以及如何查看您的 ARP 缓存。理解 ARP 在网络通信中的作用。ARP 初学者指南。"
meta_keywords: "Linux ARP, ARP 缓存，ip neighbour show, 网络命令，Linux 网络，Linux 初学者，Linux 教程"
---

## Lesson Content

请记住，当我们使用 ARP 查找 MAC 地址时，它首先检查我们系统上本地存储的 ARP 缓存。您实际上可以查看此缓存：

```
pete@icebox:~$ arp
Address                  HWtype  HWaddress           Flags Mask            Iface
192.168.22.1            ether   00:12:24:fc:12:cc   C                     eth0
192.168.22.254          ether   00:12:45:f2:84:64   C                     eth0
```

当机器启动时，ARP 缓存实际上是空的；它会在数据包发送到其他主机时填充。如果我们将数据包发送到 ARP 缓存中不存在的目标，则会发生以下情况：

1. 源主机创建带有 ARP 请求数据包的以太网帧。
2. 源主机将此帧广播到整个网络。
3. 如果网络上的某个主机知道正确的 MAC 地址，它将发送包含 MAC 地址的回复数据包和帧。
4. 源主机将 IP 到 MAC 地址的映射添加到 ARP 缓存，然后继续发送数据包。

您还可以通过 `ip` 命令查看 ARP 缓存：

```bash
ip neighbour show
```

## Exercise

熟能生巧！以下是一些动手实验，可帮助您巩固对 ARP 和网络层交互的理解：

1. **[在 Linux 中使用 ping 和 arp 探索网络层交互](https://labex.io/zh/labs/linux-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - 使用 `ping` 和 `arp` 命令观察 IP 地址如何解析为 MAC 地址以及默认网关如何处理流量。
2. **[在 Linux 中识别 MAC 和 IP 地址](https://labex.io/zh/labs/linux-identify-mac-and-ip-addresses-in-linux-592731)** - 学习使用 `ip a` 命令识别网络寻址信息，包括 MAC 和 IP 地址，这些信息是理解 ARP 的基础。
3. **[在 Linux 中管理 IP 寻址](https://labex.io/zh/labs/linux-manage-ip-addressing-in-linux-592736)** - 练习使用 `ip` 命令管理 IP 寻址，并使用 `arp` 和 `traceroute` 验证网络配置。

这些实验将帮助您在实际场景中应用 ARP 和网络寻址的概念，并增强您对 Linux 网络的信心。

## Quiz Question

您可以使用什么命令来查看您的 ARP 缓存？

## Quiz Answer

arp
