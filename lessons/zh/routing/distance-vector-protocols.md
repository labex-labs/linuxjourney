---
lesson_id: "distance-vector-protocols"
course_id: "routing"
lang: "zh"
order_index: 5
title: "距离矢量协议"
description: "学习距离矢量协议如何根据邻居通告推导路由并限制环路。"
meta_title: "距离矢量协议 - 路由"
meta_description: "面向初学者的网络路由距离矢量协议指南。本教程介绍 RIP 等协议如何使用跳数确定路由，以及它们在现代 Linux 网络中的局限。"
meta_keywords: "距离矢量协议, 网络路由, RIP, 路由信息协议, 跳数, Linux 网络, 初学者指南, 教程"
---

距离矢量路由会告诉邻居哪些目标可达，并提供描述距离的度量值。路由器将邻居通告与到达该邻居的开销结合起来，推导自己的候选路径。

## 通过邻居学习

如果路由器 A 通告到某个前缀的距离为三，而路由器 B 到达 A 的开销为一，那么 B 可以推导出经由 A 的距离为四。该信息描述方向和度量，而不是完整拓扑图，因此这种方法有时称为“听信传闻的路由”。

:::single-choice{#distance-vector-derived-distance} 如果邻居通告度量值 3，链路开销为 1，经由它推导出的度量值是多少？

::option[2]{#distance-vector-two explanation="链路开销应相加，而不是相减。"}
::option[31]{#distance-vector-thirty-one explanation="这些值是度量，而不是要拼接的十进制数字。"}
::option[4]{#distance-vector-four .correct explanation="邻居距离与本地链路开销相加得到候选路径。"}
:::

## 环路与无穷计数

故障发生后，邻居可能错误地把路由相互通告回去，使其度量值逐渐增加。协议使用有限的无穷值、水平分割、路由毒化、毒性逆转、触发更新和计时器来缓解这一问题。这些机制可以降低风险，但无法让每次拓扑变化都瞬间收敛。

:::single-choice{#distance-vector-split-horizon} 水平分割旨在减少什么？

::option[每个 IPv4 地址中的位数。]{#distance-vector-ip-bits explanation="IPv4 地址大小固定，与路由更新无关。"}
::option[应用程序载荷中的加密开销。]{#distance-vector-encryption explanation="该技术关注路由通告方向。"}
::option[把学习到的路由通告回它所来自的邻居。]{#distance-vector-no-return .correct explanation="抑制该方向有助于防止简单反馈环路。"}
:::

## RIP 度量与限制

RIP 使用跳数。度量值为 16 的路由不可达，因此最大可用度量值为 15。这限制了环路中的度量增长，也限制了网络直径。较少的跳数不一定意味着更低延迟或更高带宽。

RIPv2 使用周期更新和触发更新，并支持 CIDR 信息。它通常使用多播发送更新，而不是在每种情况下都广播整张路由表。身份验证和过滤仍需有意配置。

:::single-choice{#distance-vector-rip-infinity} RIP 度量值 16 表示什么？

::option[具有十六条并行链路的最快路径。]{#distance-vector-fastest-16 explanation="RIP 将该值视为不可达。"}
::option[无穷，即目标不可达。]{#distance-vector-unreachable .correct explanation="RIP 将可用路径限制为最多 15 跳。"}
::option[从 BGP 学习到的路由。]{#distance-vector-bgp-route explanation="该数字具有 RIP 特有的含义。"}
:::

## 评估学习到的路由

应检查邻居状态、接收和通告的前缀、度量值、下一跳、路由安装及数据平面可达性。一条路由可能在 RIP 内有效，但根据本地偏好策略输给另一个路由来源。

:::single-choice{#distance-vector-fewest-hop-limit} 为什么 RIP 的最少跳路径可能表现很差？

::option[跳数不包含链路带宽、延迟、丢包或拥塞信息。]{#distance-vector-hop-limited .correct explanation="跳数更多的路径可能具有更好的链路和应用程序性能。"}
::option[RIP 始终选择跳数最多的路由。]{#distance-vector-most-hops explanation="它的度量偏好较小的可用跳数。"}
::option[跳数以磁盘空间字节为单位。]{#distance-vector-disk-bytes explanation="它统计路由转换，而不是存储空间。"}
:::

## 总结

现在，你可以解释距离矢量路由的简洁性与局限。

1. 根据邻居通告推导候选距离。
2. 识别环路和无穷计数行为。
3. 解释 RIP 的 15 跳可用上限和度量值 16。
4. 分别验证路由安装和数据平面结果。
