---
index: 7
lang: "zh"
title: "IPv6"
meta_title: "IPv6 - 子网划分"
meta_description: "了解 IPv6、其目的以及它如何补充 IPv4。理解 IPv6 寻址及其在连接更多设备到互联网中的作用。"
meta_keywords: "IPv6, IPv4, IP 地址，Linux 网络，网络协议，初学者，教程，指南"
---

## Lesson Content

我们或多或少都听说过 IPv6 这个术语，但它到底是什么呢？连接到互联网的每个设备都有自己的 IP 地址。然而，在数字时代，这个数字是有限的，我们很快就会达到极限。创建 IPv6 是为了让我们能够连接更多的设备到互联网；它带来了更多的 IP 改进。然而，它的普及速度相当缓慢。它并非旨在取代 IPv4；它们旨在相互补充。这两种 IP 协议非常相似，如果你了解 IPv4，你就会理解 IPv6。主要区别在于地址的写法。以下是典型的 IPv6 地址：

```plaintext
2dde:1235:1256:3:200:f8ed:fe23:59cf
```

## Exercise

熟能生巧！以下是一些动手实验，以加强您对 IPv6 寻址及其与 IPv4 交互的理解：

1. **[在 Linux 中配置和验证 IPv6 地址](https://labex.io/zh/labs/linux-configure-and-verify-ipv6-addresses-in-linux-592858)** - 练习分配静态 IPv6 地址并使用 `ip` 和 `ping6` 命令测试连接。
2. **[在 Linux 中执行 IPv6 DNS 查找](https://labex.io/zh/labs/linux-perform-ipv6-dns-lookups-in-linux-592862)** - 学习查询 AAAA 记录并使用 `dig`、`nslookup` 和 `ping6` 验证 IPv6 DNS 解析。
3. **[在 Linux 中配置 IPv4 到 IPv6 的 6to4 隧道](https://labex.io/zh/labs/linux-configure-an-ipv4-to-ipv6-6to4-tunnel-in-linux-592867)** - 获得设置 6to4 隧道的实践经验，以在现有 IPv4 网络上启用 IPv6 连接。

这些实验将帮助您在实际场景中应用 IPv6 概念，并增强网络配置和故障排除的信心。

## Quiz Question

哪种 IP 地址用于帮助增加可以连接到互联网的主机数量？

## Quiz Answer

IPv6
