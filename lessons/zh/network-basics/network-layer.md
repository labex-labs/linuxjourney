---
lesson_id: "network-layer"
course_id: "network-basics"
lang: "zh"
order_index: 7
title: "网络层"
description: "学习 IP 寻址、前缀、路由表和跳数限制如何在网络之间传送数据包。"
meta_title: "网络层 - 网络基础"
meta_description: "探索 Linux 网络中的网络层。本指南介绍 IP 地址和子网如何实现数据包路由，使数据能够跨网络传输。"
meta_keywords: "网络层, IP 地址, 子网, Linux 网络, 数据包路由, 数据传输, OSI 模型, IP 数据包"
---

网络层在互连网络之间提供逻辑寻址和尽力而为的数据包传送。在互联网协议族中，IPv4 和 IPv6 承载数据包，路由器则为每个目标选择下一跳。

## IP 数据包

IP 标头包含源地址和目标地址，以及转发与协议处理所需的字段。其载荷通常包含 TCP 段、UDP 数据报或 ICMP 消息。IP 不保证数据包到达、按序传送或不重复。

:::single-choice{#network-layer-ip-service}
IP 本身提供哪种传送服务？

::option[保证应用程序事务完成提交。]{#network-layer-guaranteed-commit explanation="IP 传送结果不能证明应用程序已持久保存数据。"}
::option[尽力而为的数据包传送。]{#network-layer-best-effort .correct explanation="所需的恢复或排序由更高层或应用程序添加。"}
::option[永久保留一根物理电缆。]{#network-layer-cable-reservation explanation="数据包转发不会保留专用物理路径。"}
:::

## 前缀与子网

地址和前缀长度共同定义从开头起哪些位组成网络前缀。主机使用这些信息和路由，判断目标是否在链路上，还是需要经过下一跳路由器。子网是某个前缀与策略下的地址范围；不同子网不会自动相互连接。

:::single-choice{#network-layer-prefix-decision}
什么帮助主机判断 IPv4 目标是否位于本地链路？

::option[目标的应用程序密码。]{#network-layer-password explanation="身份验证数据不定义网络前缀。"}
::option[以太网电缆的颜色。]{#network-layer-cable-color explanation="电缆外观没有寻址语义。"}
::option[已配置的前缀和路由表。]{#network-layer-prefix-routes .correct explanation="主机会将目标与包括直连前缀在内的路由进行比较。"}
:::

## 路由决策

Linux 查询路由策略和路由表，以选择传出接口、下一跳和首选源信息。在其他条件都符合的路由中，通常优先选择匹配最具体前缀的路由。使用以下命令检查某个目标的实际决策：

```bash
$ ip route get 203.0.113.10
```

这只是本地路由查询，不能证明每台下游路由器都有正常路由，也不能证明目标会接受流量。

:::single-choice{#network-layer-longest-prefix}
在到达同一目标的合格路由中，通常哪一条胜出？

::option[接口名称按字母排序最靠前的路由。]{#network-layer-alphabetical explanation="接口拼写不是选择规则。"}
::option[最旧的路由，无论其前缀如何。]{#network-layer-oldest explanation="仅凭存在时间不能凌驾于前缀匹配之上。"}
::option[具有最具体匹配前缀的路由。]{#network-layer-most-specific .correct explanation="最长前缀匹配会选择覆盖范围最窄的匹配地址范围。"}
:::

## 跳数限制与转发变化

每个 IPv4 数据包都有 TTL，每个 IPv6 数据包都有 Hop Limit。路由器会将其递减；当值到达零时，路由器丢弃数据包，并可以发送 ICMP 错误。这能防止数据包在转发环路中无限循环。

路由器通常保留端到端 IP 地址，但 NAT、隧道、代理和其他中间设备可能转换或封装数据包。无论如何，链路层标头都会在每个路由跳点改变。

:::single-choice{#network-layer-hop-limit}
为什么路由器要递减 TTL 或 Hop Limit？

::option[提高应用程序的文件权限。]{#network-layer-hop-permissions explanation="跳数与文件系统授权无关。"}
::option[把每个数据包从 IPv4 转换为 IPv6。]{#network-layer-hop-convert explanation="协议转换不是该字段的用途。"}
::option[防止数据包永远循环。]{#network-layer-prevent-loop .correct explanation="有限的跳数确保持续存在的路由环路最终会丢弃数据包。"}
:::

## 总结

现在，你可以解释 IP 主机如何选择通向目标的下一步。

1. 将 IP 传送视为尽力而为。
2. 使用前缀和路由区分本地链路目标与经过路由的目标。
3. 将最长前缀匹配应用到路由选择。
4. 认识跳数限制如何约束转发环路。
