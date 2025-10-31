---
index: 5
lang: "zh"
title: "CIDR"
meta_title: "CIDR - 子网划分"
meta_description: "CIDR 表示法指南。了解 CIDR 格式、CIDR 子网划分以及如何在您的网络（包括 Ubuntu 服务器）上计算主机数。掌握 CIDR IP 地址分配。"
meta_keywords: "CIDR, cidr 子网划分，cidr 格式，子网掩码，IP 地址分配，ubuntu 服务器子网 cidr, ubuntu 子网 cidr, 网络前缀，Linux 网络"
---

## Lesson Content

CIDR（无类别域间路由）是一种分配 IP 地址和路由网际协议数据包的方法。它提供了一种比旧的分类网络设计更简洁、更高效的表示子网掩码的方式。理解 CIDR 对于现代网络管理至关重要。

### CIDR 格式

您经常会看到使用 **CIDR 格式**表示的网络，即 IP 地址后跟一个斜杠和一个数字。例如，子网 `10.42.3.0`，其子网掩码为 `255.255.255.0`，可以写成 `10.42.3.0/24`。这种单一的表示法同时包含了网络地址和前缀长度。

斜杠后的数字表示用于网络前缀的 IP 地址位数。这是在 **Ubuntu 服务器**等系统上配置网络时的一项常见任务，您可能需要使用 `ubuntu subnet cidr` 地址来定义一个接口。

### CIDR 子网划分和主机计算

IPv4 地址由 4 个字节组成，共 32 位。CIDR 前缀决定了地址中网络部分和主机部分的划分。要实现有效的 **cidr subnetting**（CIDR 子网划分），您需要知道如何计算可用主机的数量。

我们以 `123.12.24.0/23` 为例。这意味着前 23 位是网络前缀。要找到可用主机的数量：

1.  从总位数 (32) 中减去 CIDR 前缀：`32 - 23 = 9`。这为主机部分留下了 9 位。
2.  计算子网中的总地址数：`2^9 = 512`。
3.  总数减去 2。一个地址保留给网络本身，一个保留给广播地址。这样就剩下 `512 - 2 = 510` 个可用主机地址。

另一个常见的例子是 `/30` 网络，它提供 `32 - 30 = 2` 个主机位。这导致 `2^2 = 4` 个总地址，只留下 2 个可用地址，非常适合点对点链路。

## Exercise

为了掌握这些概念，请通过一些实践实验来加强您对 CIDR、IP 地址分配和 **cidr subnetting**（CIDR 子网划分）的理解：

1.  **[在 Linux 终端中执行 IP 子网划分和二进制转换](https://labex.io/zh/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - 掌握 IP 子网划分和二进制转换，包括转换 CIDR 掩码和计算可用主机。
2.  **[在 Linux 中模拟网络层连通性](https://labex.io/zh/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - 学习分配静态 IP 地址，并观察 IP 子网如何在模拟环境中控制直接网络通信。
3.  **[在 Linux 中探索 IP 地址类型和可达性](https://labex.io/zh/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - 使用 `ping` 和 `ip a` 等命令探索 IP 地址分配和网络可达性，以测试各种 IP 类型和连通性。

这些实验将帮助您在实际场景中应用 CIDR 和 IP 地址分配的概念，并建立网络配置的信心。
