---
index: 1
lang: "zh"
title: "IPv4"
meta_title: "IPv4 - 子网划分"
meta_description: "了解 IPv4 地址、它们的结构以及如何使用 ifconfig 查找您的 IP。了解 Linux 初学者的网络基础知识。"
meta_keywords: "IPv4, IP 地址，ifconfig, 网络基础，Linux 网络，初学者，教程，指南"
---

## Lesson Content

我们知道网络主机有一个唯一的地址可以找到它们。这些地址被称为 IP 地址。一个 IPv4 地址看起来像这样：

```
204.23.124.23
```

这个地址实际上包含两部分：网络部分，告诉我们它在哪一个网络上；以及主机部分，告诉我们它是该网络上的哪一个主机。在本课程中，我们主要讨论 IPv4 地址，这是您在提及 IP 地址时通常会看到的。

IP 地址由句点分隔成八位字节。因此，一个 IPv4 地址有 4 个八位字节。如果您懂一点计算机科学，一个八位字节是 8 位，8 位实际上等于 1 字节，所以我们也称一个 IPv4 地址有 4 字节。在处理子网和 IP 地址时，我们经常使用位。

您可以使用 `ifconfig -a` 命令查看您的 IP 地址：

```bash
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
```

如您所见，我的 IPv4 地址是：192.168.1.129

## Exercise

熟能生巧！以下是一些动手实验，旨在加强您对 Linux 中 IP 寻址和网络识别的理解：

1. **[在 Linux 中识别 MAC 和 IP 地址](https://labex.io/zh/labs/linux-identify-mac-and-ip-addresses-in-linux-592731)** - 练习使用 `ip a` 命令在 Linux 系统上识别网络寻址信息，包括 IPv4 和 IPv6 地址。
2. **[探索 Linux 中的 IP 地址类型和可达性](https://labex.io/zh/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** - 探索不同的 IP 地址类型，并使用 `ping` 和 `ip a` 等命令测试网络可达性。
3. **[在 Linux 终端中执行 IP 子网划分和二进制转换](https://labex.io/zh/labs/linux-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - 掌握 IP 子网划分和二进制转换，这对于更深入地理解 IP 地址和网络在位级别的结构至关重要。

这些实验将帮助您在实际场景中应用 IP 寻址的概念，并增强您在 Linux 中进行网络配置和故障排除的信心。

## Quiz Question

一个 IPv4 地址有多少字节？

## Quiz Answer

4
