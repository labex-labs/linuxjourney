---
index: 1
lang: "zh"
title: "IPv4"
meta_title: "IPv4 - 子网划分"
meta_description: "通过理解 IPv4 地址，发现学习 Linux 网络知识的最佳方法。本初学者指南涵盖 IP 结构以及如何使用命令行查找您的 IP。"
meta_keywords: "IPv4, IP 地址，Linux 入门，学习 Linux 最佳方法，Linux 命令行入门，ifconfig, ip addr, 网络基础"
---

## Lesson Content

连接到网络的每个设备都有一个唯一的地址，称为 IP（Internet Protocol，互联网协议）地址。在本课程中，我们将重点关注 IPv4 地址，这是您会遇到的最常见的类型。理解它们是学习 Linux 网络知识的核心部分。

IPv4 地址是一个 32 位的数字，通常以人类可读的格式表示，如下所示：

```
204.23.124.23
```

该地址包含两个不同的部分：**网络部分**，用于识别设备所在的特定网络；以及**主机部分**，用于识别该网络上的特定设备。

### IP 地址的结构

IPv4 地址被点（.）分隔成四个部分。每个部分称为一个**八位字节 (octet)**。在计算机科学中，一个八位字节是 8 位的一组，由于 8 位等于 1 字节，因此 IPv4 地址长 4 字节。这种结构是基础，掌握它是在网络方面学习 `Linux 命令行入门的最佳资源` 之一。

### 在 Linux 上查找您的 IP 地址

对于任何 `Linux 入门` 用户来说，首要任务之一是找到系统的 IP 地址。您可以使用命令行工具来完成此操作。

传统的命令是 `ifconfig`。虽然它仍然存在于许多系统上，但它被认为是遗留工具。

```bash
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
```

在上面的输出中，IPv4 地址是 `192.168.1.129`。

### 使用 ip addr 的现代方法

如今，学习 Linux 网络知识的`最佳方法`是使用现代的 `ip` 命令。`ip addr` 命令取代了 `ifconfig`，是大多数当前 Linux 发行版上的标准命令。

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

通过以下实践实验来巩固您对 Linux 中 IP 地址和网络识别的理解：

1. **[在 Linux 中识别 MAC 地址和 IP 地址](https://labex.io/zh/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - 练习使用 `ip a` 命令来识别 Linux 系统上的网络寻址信息，包括 IPv4 和 IPv6 地址。
2. **[在 Linux 中探索 IP 地址类型和可达性](https://labex.io/zh/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - 探索不同的 IP 地址类型，并使用 `ping` 和 `ip a` 等命令测试网络可达性。
3. **[在 Linux 终端中执行 IP 子网划分和二进制转换](https://labex.io/zh/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - 掌握 IP 子网划分和二进制转换，这对于深入理解 IP 地址和网络在位级别上的结构至关重要。

这些实验将帮助您在实际场景中应用 IP 寻址概念，并增强您对 Linux 中网络配置和故障排除的信心。

## Quiz Question

一个 IPv4 地址包含多少字节？

## Quiz Answer

4
