---
index: 7
lang: "zh"
title: "IPv6"
meta_title: "IPv6 - 子网划分"
meta_description: "IPv6 协议的初学者指南。了解 IPv6 的创建原因、它与 IPv4 的区别，并掌握其现代 Linux 网络寻址方案的基础知识。"
meta_keywords: "IPv6, IPv4, IP 地址，Linux 网络，网络协议，互联网协议，地址耗尽，初学者，教程，指南"
---

## Lesson Content

从您的服务器到智能手机，连接到互联网的每个设备都需要一个唯一的 IP 地址才能通信。使用最广泛的版本 IPv4 提供的地址数量是有限的，在我们日益互联的世界中，我们正迅速接近这个限制。这个问题被称为 IPv4 地址耗尽。

### 什么是 IPv6？

为了解决这个问题，互联网工程任务组 (IETF) 开发了新版本的互联网协议：IPv6。IPv6 的主要目的是大幅扩展可用的 IP 地址池，确保互联网能够持续增长并容纳数十亿新设备。它还包含对网络协议的其他改进。

### IPv4 与 IPv6

尽管 IPv6 是为解决 IPv4 的局限性而创建的，但其采用是渐进的。它并非旨在立即取代 IPv4。相反，这两种网络协议旨在共存和互补。如今，许多网络以“双栈”模式运行，同时支持 IPv4 和 IPv6。如果您熟悉 IPv4，IPv6 的核心概念将很容易掌握。

### 理解 IPv6 地址

您注意到的最显著区别是地址格式。IPv4 地址是一个 32 位数字，通常写成由句点分隔的四个十进制数（例如 `192.168.1.1`）。相比之下，IPv6 地址是一个 128 位数字，以十六进制表示，并由冒号分隔。

典型的 IPv6 地址如下所示：

```plaintext
2dde:1235:1256:3:200:f8ed:fe23:59cf
```

这种更长的格式允许更多的唯一 IP 地址，确保了互联网连接的未来。

## Exercise

为了掌握 IPv6 的概念，实践至关重要。以下是一些实践实验，可帮助您在 Linux 环境中巩固对 IPv6 寻址及其与 IPv4 交互的理解：

1. **[在 Linux 中配置和验证 IPv6 地址](https://labex.io/zh/labs/comptia-configure-and-verify-ipv6-addresses-in-linux-592858)** - 练习分配静态 IPv6 地址并使用 `ip` 和 `ping6` 命令测试连通性。
2. **[在 Linux 中执行 IPv6 DNS 查询](https://labex.io/zh/labs/comptia-perform-ipv6-dns-lookups-in-linux-592862)** - 学习查询 AAAA 记录并使用 `dig`、`nslookup` 和 `ping6` 验证 IPv6 DNS 解析。
3. **[在 Linux 中配置 IPv4 到 IPv6 的 6to4 隧道](https://labex.io/zh/labs/comptia-configure-an-ipv4-to-ipv6-6to4-tunnel-in-linux-592867)** - 获得动手经验，设置 6to4 隧道，以便在现有 IPv4 网络上启用 IPv6 连接。

这些实验将帮助您在实际场景中应用 IPv6 的概念，并建立对网络配置和故障排除的信心。

## Quiz Question

What is the name of the IP protocol designed to increase the number of available addresses for hosts on the Internet? Please answer in English using the protocol's common name, paying attention to capitalization.

## Quiz Answer

IPv6
