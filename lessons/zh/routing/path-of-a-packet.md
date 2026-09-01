---
lesson_id: "path-of-a-packet"
course_id: "routing"
lang: "zh"
order_index: 3
title: "数据包的路径"
description: "学习路由、邻居发现、帧和路由器如何沿路径承载 IP 数据包。"
meta_title: "数据包的路径 - 路由"
meta_description: "探索数据在本地网络和互联网中传输的完整数据包路径。了解 IP 地址、MAC 地址、ARP 和路由表如何协同工作，确保 Linux 网络通信成功。"
meta_keywords: "数据包路径, 网络通信, ARP, IP 地址, MAC 地址, 路由表, 默认网关, Linux 网络, 数据包传输"
---

一条数据包路径由一系列本地决策组成。源主机、每台路由器和目标都会应用各自的路由、邻居、过滤和协议状态；任何端点通常都无法提前知道每项内部决策。

## 发送到链路内目标

对于由直连路由覆盖的目标，源主机会选择接口和源 IP。然后，它解析目标的链路地址——以太网上的 IPv4 使用 ARP，IPv6 使用邻居发现——再发送承载 IP 数据包的帧。交换机可以转发该帧，而不会成为 IP 跳点。

:::single-choice{#packet-path-switch-hop} 普通以太网交换机算作 IP 路由跳点吗？

::option[不算；它转发本地帧，不会递减 IP 跳数字段。]{#packet-path-switch-not-hop .correct explanation="只有路由器处理并转发 IP 数据包时才构成路由跳点。"}
::option[算；每台交换机都会替换 IP 目标。]{#packet-path-switch-replaces-ip explanation="二层转发通常不会重写 IP 目标。"}
::option[算；每个电缆连接器也是 IP 跳点。]{#packet-path-cable-hop explanation="物理组件不执行 IP 路由。"}
:::

## 通过网关发送

对于链路外目标，所选路由会标识下一跳路由器。IP 目标仍是远程端点，而本地帧的目标则是网关的链路地址。主机在本地链路上解析的是网关，而不是远程服务器。

:::single-choice{#packet-path-gateway-mac} 发送到链路外服务器的第一个以太网帧使用谁的 MAC 地址？

::option[跨越所有中间网络使用远程服务器的地址。]{#packet-path-remote-mac explanation="远程链路地址在源 LAN 上没有意义。"}
::option[根据服务器 DNS 名称计算出的值。]{#packet-path-dns-mac explanation="DNS 名称不会编码本地下一跳 MAC。"}
::option[所选本地网关的地址。]{#packet-path-local-gateway .correct explanation="帧会送达下一跳，而 IP 标头仍以最终端点为目标。"}
:::

## 每台路由器上的处理

路由器会移除传入链路帧、验证并处理 IP 标头、递减 TTL 或 Hop Limit、查找目标、应用策略，再为传出链路创建新帧。对于 IPv4，标头校验和处理会反映 TTL 的变化。如果跳数字段到达零，路由器会丢弃数据包，并可以返回 ICMP 超时消息。

:::single-choice{#packet-path-router-change} 每个正常路由跳点都会更改哪个 IP 字段？

::option[应用程序用户名。]{#packet-path-username explanation="基本转发不需要路由器了解应用程序账户数据。"}
::option[IPv4 TTL 或 IPv6 Hop Limit。]{#packet-path-hop-field .correct explanation="每台路由器都会递减该字段，以限制路由环路。"}
::option[所有情况下都更改传输层目标端口。]{#packet-path-port explanation="普通路由保留传输端点；NAT 才可能进行独立转换。"}
:::

## 考虑中间设备与 MTU

普通路由会保留源和目标 IP 地址，但 NAT 可以重写它们，隧道则可以封装原始数据包。防火墙可能静默丢弃或明确拒绝流量。不同链路的 MTU 也不相同；IPv4 路由器有时可以对数据包分片，而 IPv6 路由器不会对转发的数据包分片，而是依赖路径 MTU 发现。

:::single-choice{#packet-path-address-change-exception} 端到端 IP 地址何时可能沿路径改变？

::option[以太网交换机每次学习源 MAC 时。]{#packet-path-switch-learning-ip explanation="交换机学习影响链路转发表，而不是 IP 端点地址。"}
::option[NAT 策略转换数据包标头时。]{#packet-path-nat-change .correct explanation="转换是普通路由转发之外的中间设备功能。"}
::option[DNS 缓存条目每次过期时。]{#packet-path-dns-expiry explanation="已经存在的数据包包含数字地址。"}
:::

## 跟踪返回路径

目标会为响应执行自己的路由查找。由于路由策略、负载均衡或故障，返回路径可能经过不同的路由器。有状态防火墙和 NAT 必须考虑观察到的流，因此即使 IP 允许路径不对称，它在运维上仍可能产生影响。

:::single-choice{#packet-path-return-symmetry} 回复必须按相反顺序经过相同的路由器吗？

::option[必须，因为 IP 会在每个数据包中记录完整的出站路由。]{#packet-path-records-route explanation="普通 IP 数据包不携带强制性的完整反向路由。"}
::option[必须，除非源和目标共享一个主机名。]{#packet-path-hostname-symmetry explanation="名称不会强制路径对称。"}
::option[不必；两个方向各自独立路由。]{#packet-path-independent-return .correct explanation="策略和拓扑可以产生不对称但有效的路径。"}
:::

## 总结

现在，你可以跟踪路由 IP 数据包周围不断变化的链路状态。

1. 只有最终主机在链路上时才直接解析它。
2. 将链路外流量装入发送给所选本地网关的帧。
3. 跟踪每台路由器上的路由查找和跳数限制处理。
4. 考虑 NAT、过滤、隧道和 MTU 限制。
5. 将返回方向视为一条独立路由。
