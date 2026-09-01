---
lesson_id: "subnets"
course_id: "subnetting"
lang: "zh"
order_index: 2
title: "子网"
description: "学习前缀如何定义 IPv4 子网，并影响链路内传送、路由和策略。"
meta_title: "子网 - 子网划分"
meta_description: "掌握 Linux 子网和子网掩码基础。本指南介绍子网划分、网络前缀，以及如何在 Linux 子网环境中管理网络分段。"
meta_keywords: "Linux 子网, 子网掩码, 子网划分, 子网, 网络前缀, Linux 网络, IP 地址"
---

子网是由网络前缀定义的 IP 地址范围。同一子网中的主机通常位于同一条本地链路，但物理距离并不是定义；VLAN、隧道、覆盖网络和路由链路都可能改变拓扑。

## 前缀与掩码

IPv4 可以将 24 位前缀表示为 `/24`，也可以表示为掩码 `255.255.255.0`。在二进制中，有效的传统子网掩码由连续的一和随后的零组成：

```text
11111111.11111111.11111111.00000000
```

对于地址 `192.168.1.8/24`，网络前缀是 `192.168.1.0/24`。某些上下文也能理解 `192.168.1.0/255.255.255.0`，但 CIDR 前缀表示法才是标准的紧凑形式。

:::single-choice{#subnets-mask-24} 哪个点分十进制掩码对应 `/24`？

::option[`255.255.255.0`]{#subnets-mask-correct .correct explanation="三个完整八位组包含 24 个开头的一位。"}
::option[`255.255.0.255`]{#subnets-noncontiguous explanation="其中的网络位不连续，不是传统的 /24 掩码。"}
::option[`0.0.0.24`]{#subnets-prefix-as-octet explanation="前缀长度不会放入掩码的最后一个八位组。"}
:::

## 判断目标是否在链路上

Linux 根据接口地址和前缀安装直连路由。它会将目标与符合条件的路由比较，而不是只比较前三个十进制八位组。对于 `/20` 等不在八位组边界上的前缀，分界会落在一个八位组内部。

使用以下命令检查直连路由和某个地址的决策：

```bash
$ ip route show
$ ip route get 192.168.1.50
```

:::single-choice{#subnets-on-link-decision} Linux 主机如何确定直接发送还是通过路由器发送？

::option[它始终假定以 `.1` 结尾的地址位于本地。]{#subnets-dot-one explanation="主机号惯例不能取代已配置的前缀和路由。"}
::option[它查询前缀和路由策略。]{#subnets-route-policy .correct explanation="所选路由会指出目标是否在链路上，以及使用哪个接口或下一跳。"}
::option[连接后再向目标应用程序询问子网掩码。]{#subnets-ask-application explanation="路由选择必须先于应用程序交换发生。"}
:::

## 子网间路由

具有适当接口和路由的路由器可以在子网之间转发流量。默认网关只是默认路由选择的下一跳；它不必使用第一个可用地址，也不必以 `.1` 结尾。

子网分隔提供了应用路由和过滤策略的位置，但不会自动成为安全边界。如果转发没有受到限制性策略约束，不同子网中的主机仍可通信。

:::single-choice{#subnets-security-boundary} 创建两个子网会自动阻止它们之间的流量吗？

::option[会，因为路由器无法连接不同前缀。]{#subnets-never-route explanation="连接不同前缀正是路由的主要工作。"}
::option[不会；路由和过滤策略决定允许哪些流量。]{#subnets-policy-required .correct explanation="分段使策略实施成为可能，但本身不会定义策略。"}
::option[会，除非两者都使用主机地址 `.1`。]{#subnets-dot-one-security explanation="主机号惯例不会控制转发。"}
:::

## 子网划分的原因

子网划分可以组织地址分配、限制链路层广播范围、分隔故障域，并提供策略边界。它也可能增加路由、防火墙、DHCP、监控和文档复杂度。应根据实际规模、增长、冗余和安全要求设计前缀，而不是想当然地认为越小就越快。

:::single-choice{#subnets-design-tradeoff} 真实的子网划分权衡是什么？

::option[较小的广播域不需要路由或文档。]{#subnets-no-complexity explanation="更多边界通常需要管理更多路由、策略、地址和服务。"}
::option[分段可以改善组织方式，但会增加策略复杂度。]{#subnets-tradeoff .correct explanation="子网边界有助于控制，但也会增加必须维护的运行状态。"}
::option[每个子网都保证拥有相同的互联网延迟。]{#subnets-equal-latency explanation="路径和工作负载状况决定延迟。"}
:::

## 总结

现在，你可以将 IPv4 前缀与本地传送和路由策略关联起来。

1. 使用 CIDR 前缀长度表示连续掩码。
2. 根据地址位和掩码计算网络前缀。
3. 使用路由判断链路内传送还是下一跳传送。
4. 将子网隔离视为应用策略的机会，而不是保证。
