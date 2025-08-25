---
index: 5
lang: "zh"
title: "CIDR"
meta_title: "CIDR - 子网划分"
meta_description: "学习 Linux 网络中的 CIDR 表示法。通过这份适合初学者的指南，了解子网掩码、IP 寻址和主机计算。提高您的网络技能！"
meta_keywords: "CIDR, 子网掩码，IP 寻址，网络前缀，Linux 网络，初学者，教程，指南"
---

## Lesson Content

CIDR（无类别域间路由）用于以更紧凑的方式表示子网掩码。您可能会看到以 CIDR 表示法表示的子网，例如 10.42.3.0/255.255.255.0 的子网被写为 10.42.3.0/24。这种表示法包括子网前缀和子网掩码。

请记住，IP 地址由 4 字节或 32 位组成。CIDR 表示用作网络前缀的位数。因此，123.12.24.0/23 意味着前 23 位被使用。那是什么意思？那有多少主机呢？

一个简单的技巧是从 IP 地址可以拥有的总位数（32）中减去 CIDR 地址（23）。这剩下 9 位。因此，2^9 = 512。但是，我们必须移除 2 个地址（子网地址和广播地址），所以我们有 510 个可用主机。

## Exercise

熟能生巧！这里有一些动手实验，以加强您对 CIDR、IP 寻址和子网划分的理解：

1. **[在 Linux 终端中执行 IP 子网划分和二进制转换](https://labex.io/zh/labs/linux-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - 掌握 IP 子网划分和二进制转换，包括转换 CIDR 掩码和计算可用主机。
2. **[在 Linux 中模拟网络层连接](https://labex.io/zh/labs/linux-simulate-network-layer-connectivity-in-linux-592752)** - 学习分配静态 IP 地址并观察 IP 子网如何在模拟环境中管理直接网络通信。
3. **[在 Linux 中探索 IP 地址类型和可达性](https://labex.io/zh/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** - 使用 `ping` 和 `ip a` 等命令探索 IP 寻址和网络可达性，以测试各种 IP 类型和连接。

这些实验将帮助您在实际场景中应用 CIDR 和 IP 寻址的概念，并增强网络配置的信心。

## Quiz Question

没有问题，继续！

## Quiz Answer
