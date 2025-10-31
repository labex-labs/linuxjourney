---
index: 1
lang: "zh"
title: "IPv4"
meta_title: "IPv4 - 子网划分"
meta_description: "通过我们完整的 IPv4 地址 Linux 教程开始您的学习之旅。本指南专为初学者设计，是学习 Linux 网络知识的最佳途径，涵盖 IP 结构和 ip addr 等基本命令行工具。"
meta_keywords: "IPv4, IP 地址，Linux 初学者，学习 Linux 的最佳方式，完整 Linux 教程，免费在线 Linux 课程，免费 Linux 认证课程，Linux 网络，ifconfig, ip addr"
---

## Lesson Content

网络上的每个设备都有一个唯一的标识符，称为 IP（Internet Protocol，互联网协议）地址。本课程是我们“完整 Linux 教程”的关键部分，重点介绍 IPv4 地址——您将遇到的最常见的类型。对于任何“Linux 新手”来说，理解 IPv4 是进入网络世界的关键第一步。

### 为什么 IPv4 至关重要

学习 IPv4 对于任何认真对待系统管理或网络管理的人来说都是基础性的。它构成了大多数网络通信的骨干。本指南提供了从头开始学习 Linux 网络知识的“最佳方式”。虽然这不属于那些“免费 Linux 认证课程”之列，但掌握这些基础知识是迈向专业认证的关键一步。

### IPv4 地址结构

IPv4 地址是一个 32 位的数字，但通常以易于人类阅读的格式显示，如下所示：

```
204.23.124.23
```

该地址有两个主要部分：标识网络的**网络部分**和标识该网络上特定设备的**主机部分**。该地址被点（句点）分隔成四个部分，每个部分称为一个**八位字节 (octet)**。一个八位字节是 8 位的一组，这意味着一个 IPv4 地址长 4 字节（32 位）。理解这种结构对于网络配置和故障排除至关重要。

### 查找您的 IP 地址

任何 Linux 用户要做的第一项任务之一就是查找其系统的 IP 地址。您可以使用简单的命令行工具来完成此操作。传统的命令是 `ifconfig`。虽然它在许多系统上仍然存在，但它被认为是遗留工具。

```bash
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
```

在上面的输出中，IPv4 地址是 `192.168.1.129`。

### 使用 ip addr 命令

现代推荐的方法是使用 `ip` 命令。`ip addr` 命令取代了 `ifconfig`，是大多数当前 Linux 发行版上的标准。它提供更详细的信息，是您应该专注于学习的工具。

```bash
pete@icebox:~$ ip addr show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 1d:3a:32:24:4d:ce brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.129/24 brd 192.168.1.255 scope global dynamic eth0
       valid_lft 85646sec preferred_lft 85646sec
```

在这里，您可以在 `eth0` 接口的 `inet` 旁边找到相同的 IPv4 地址 `192.168.1.129`。

## Exercise

使用这些动手实验来巩固您对 Linux 中 IP 寻址和网络识别的理解：

1. **[在 Linux 中识别 MAC 地址和 IP 地址](https://labex.io/zh/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - 练习使用 `ip a` 命令来识别 Linux 系统上的网络寻址信息，包括 IPv4 和 IPv6 地址。
2. **[在 Linux 中探索 IP 地址类型和可达性](https://labex.io/zh/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - 探索不同的 IP 地址类型，并使用 `ping` 和 `ip a` 等命令测试网络可达性。
3. **[在 Linux 终端中执行 IP 子网划分和二进制转换](https://labex.io/zh/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - 掌握 IP 子网划分和二进制转换，这对于深入理解 IP 地址和网络在位级别上的结构至关重要。

这些实验将帮助您在实际场景中应用 IP 寻址概念，并增强您对 Linux 中网络配置和故障排除的信心。

## Quiz Question

一个 IPv4 地址有多少字节？

## Quiz Answer

4
