---
lesson_id: "classless-interdomain-routing-cidr"
course_id: "subnetting"
lang: "zh"
order_index: 5
title: "CIDR"
description: "学习 CIDR 前缀如何表示地址范围、子网边界和聚合路由。"
meta_title: "CIDR - 子网划分"
meta_description: "CIDR 表示法指南。了解 CIDR 格式、CIDR 子网划分，以及如何计算包括 Ubuntu 服务器在内的网络主机数量，掌握 CIDR IP 寻址。"
meta_keywords: "CIDR, CIDR 子网划分, CIDR 格式, 子网掩码, IP 寻址, Ubuntu 服务器子网 CIDR, 网络前缀, Linux 网络"
---

无类别域间路由使用前缀长度表示地址范围，而不依赖历史地址类别。CIDR 为 IPv4 和 IPv6 支持大小可变的分配、子网划分和路由聚合。

## 阅读前缀表示法

在 `10.42.3.17/24` 中，前 24 位是网络前缀，剩余八位表示范围内的位置。规范网络为 `10.42.3.0/24`；配置接口时，仍可将所给主机地址与前缀写在一起。

:::single-choice{#cidr-prefix-meaning} IPv4 CIDR 值中的 `/24` 指定什么？

::option[开头的二十四个网络前缀位。]{#cidr-24-prefix-bits .correct explanation="IPv4 的其余八位可在该前缀内变化。"}
::option[每个子网有二十四个可用地址。]{#cidr-24-addresses explanation="/24 包含 256 个地址值。"}
::option[该网络的 TCP 目标端口。]{#cidr-24-port explanation="CIDR 与传输端口相互独立。"}
:::

## 计算范围大小

IPv4 前缀 `/23` 留出九个主机位，因此覆盖 `2^9 = 512` 个地址。对齐的前缀 `123.12.24.0/23` 范围为：

```text
first: 123.12.24.0
last:  123.12.25.255
```

在传统广播用法中，第一个地址是网络地址，最后一个地址是定向广播地址。不要把“减去两个”的可用主机快捷公式盲目应用到 `/31` 点对点链路或 `/32` 主机路由。

:::single-choice{#cidr-23-total} `/23` 包含多少个 IPv4 地址？

::option[512]{#cidr-total-512 .correct explanation="九个可变位产生 2^9 种组合。"}
::option[23]{#cidr-total-23 explanation="前缀数字统计固定的位数，而不是地址数。"}
::option[510]{#cidr-total-510 explanation="这是减去特殊端点后的传统可用数量，并不是总范围大小。"}
:::

## 检查对齐

前缀必须从其二进制边界开始。当前面的八位组固定时，`/23` 在第三个八位组中以 2 为块递增，因此 `123.12.24.0/23` 已对齐，而 `123.12.25.0/23` 会规范化为相同的 `123.12.24.0/23` 范围。

:::single-choice{#cidr-canonical-25} 包含 `123.12.25.0` 的规范 `/23` 网络是什么？

::option[只能是从 25 开始的 `123.12.25.0/23`。]{#cidr-25-unaligned explanation="最后一个前缀位会把第三个八位组值按对齐的二元组分组。"}
::option[`123.12.0.0/23`]{#cidr-third-zero explanation="它描述的是另一个 /23 范围。"}
::option[`123.12.24.0/23`]{#cidr-24-canonical .correct explanation="第三个八位组的 24 和 25 共享同一个对齐的 23 位前缀。"}
:::

## 聚合路由

CIDR 可以用一条聚合路由通告多个连续、等大且正确对齐的前缀。例如，`192.0.2.0/25` 和 `192.0.2.128/25` 可以合并为 `192.0.2.0/24`。只有通告路由器能够正确到达整个聚合范围，或有策略防止环路和黑洞时，聚合才是安全的。

:::single-choice{#cidr-aggregate-two-25s} 哪个聚合前缀覆盖 `192.0.2.0/24` 的两个半区？

::option[`192.0.2.0/26`]{#cidr-aggregate-26 explanation="/26 只覆盖 64 个地址，比任意一个半区都小。"}
::option[`192.0.3.0/25`]{#cidr-aggregate-other explanation="它位于所述地址范围之外。"}
::option[`192.0.2.0/24`]{#cidr-aggregate-24 .correct explanation="两个连续对齐的 /25 范围只在下一位不同，共享 /24 前缀。"}
:::

## 最长前缀路由

当路由重叠时，转发通常会选择匹配前缀最长的合格路由。`/24` 路由比覆盖它的 `/16` 更具体；默认路由 `/0` 只有在没有更具体的合格路由胜出时才会被选中。

:::single-choice{#cidr-route-specificity} 对于目标 `10.42.3.8`，哪条合格路由更具体？

::option[`10.42.3.0/24`]{#cidr-route-24 .correct explanation="24 位匹配更长，因此比 /8 更具体。"}
::option[`10.0.0.0/8`]{#cidr-route-8 explanation="它能够匹配，但固定的目标位更少。"}
::option[`0.0.0.0/0`]{#cidr-default explanation="默认路由是最不具体的 IPv4 前缀。"}
:::

## 总结

现在，你可以使用 CIDR 表示地址范围和路由选择。

1. 将斜杠后的值解释为开头前缀位的数量。
2. 根据剩余位计算总范围大小。
3. 将前缀规范化到对齐的网络边界。
4. 只聚合具有有效可达性的连续对齐范围。
5. 路由查找时优先选择最长的合格前缀。
