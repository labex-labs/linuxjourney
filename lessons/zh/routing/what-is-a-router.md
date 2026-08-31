---
lesson_id: "what-is-a-router"
course_id: "routing"
lang: "zh"
order_index: 1
title: "什么是路由器？"
description: "学习路由器如何选择下一跳，并在网络之间转发 IP 数据包。"
meta_title: "什么是路由器？ - 路由"
meta_description: "面向初学者的网络路由器指南。了解路由、分组交换、跳点，以及路由器如何使用路由表跨网络转发数据，是学习 Linux 网络的重要内容。"
meta_keywords: "路由器, 网络, 路由, 跳点, 分组交换, Linux 网络, 初学者教程, 网络指南"
---

路由器连接网络层域，并在它们之间转发 IP 数据包。启用转发，并正确配置接口、路由、邻居发现和过滤策略后，Linux 主机也可以充当路由器。

## 路由与转发

路由负责建立或选择可达前缀的信息。转发将这些信息应用到每个数据包：检查目标、选择合格路由和下一跳、递减跳数限制，然后通过传出接口发送。

两者分别属于控制平面和数据平面。路由可能存在，但防火墙策略阻止转发；转发接口也可能处于启用状态，但没有有效路由。

:::single-choice{#router-forwarding-role}
数据包转发会做什么？

::option[应用路由信息，把数据包发向下一跳。]{#router-apply-route .correct explanation="转发是根据所选路由和策略对每个数据包执行的操作。"}
::option[为每个目标创建永久应用程序登录。]{#router-create-login explanation="路由不管理远程应用程序账户。"}
::option[没有路由时把每个数据包复制到所有接口。]{#router-flood-no-route explanation="普通 IP 转发会丢弃无法路由的数据包，而不会退回到以太网式泛洪。"}
:::

## 路由表与默认路由

一条路由将目标前缀与传出接口、下一跳、度量值、源地址偏好或其他属性关联。最长前缀匹配会优先选择更具体的合格路由。IPv4 `/0` 或 IPv6 `::/0` 默认路由是最不具体的匹配，只有没有更具体路由胜出时才会使用。

如果没有合格路由，路由器会丢弃数据包，并可能生成 ICMP 不可达消息。默认路由是可选的，也不必直接指向公网。

:::single-choice{#router-default-route}
什么时候会选择默认路由？

::option[检查任何目标特定前缀之前。]{#router-default-first explanation="更具体的合格前缀优先。"}
::option[仅当数据包是以太网广播时。]{#router-default-broadcast explanation="IP 路由选择依据网络层目标。"}
::option[没有更具体的合格路由匹配时。]{#router-default-fallback .correct explanation="零长度前缀是最不具体的路由。"}
:::

## 本地流量与路由流量

位于同一个链路内子网的两台主机通常会直接交换帧，而不把 IP 数据包发送给路由器。只有路由选择将路由器选作下一跳，或拓扑和策略有意强制经过路由器时，路由器才会参与。

家用“路由器”通常组合了 IP 路由器、以太网交换机、Wi-Fi 接入点、DHCP 服务、NAT 和防火墙。应分别诊断每项功能。

:::single-choice{#router-same-subnet-path}
两台链路内主机之间的流量必须经过默认路由器吗？

::option[必须，因为每个数据包都必须到达 WAN 端口。]{#router-always-wan explanation="本地链路内传送可以直接发生。"}
::option[必须，除非两台主机都使用公网地址。]{#router-public-required explanation="公网或私有作用域不决定基本的链路内转发。"}
::option[不必；发送方可以在本地链路上直接寻址目标。]{#router-direct-on-link .correct explanation="路由表会将直连前缀标识为链路内。"}
:::

## 跳点与环路预防

路由跳点是一次网络层转发步骤。IPv4 TTL 和 IPv6 Hop Limit 会在每台路由器处递减，从而限制环路。跳数并不是完整的距离或质量指标：不同链路的带宽、延迟、丢包、策略和拥塞各不相同。

:::single-choice{#router-hop-count-limit}
较少的跳数无法保证什么？

::option[至少存在一个路由步骤。]{#router-hop-exists explanation="正跳数直接表示经过了路由。"}
::option[应用程序路径更快或更好。]{#router-hop-not-quality .correct explanation="较少的路由器仍可能经过较慢、拥塞或受策略限制的链路。"}
::option[跳数限制字段是有限的。]{#router-hop-limit-finite explanation="这些字段按协议设计就是有限值。"}
:::

## 总结

现在，你可以区分路由器的路由选择与转发操作。

1. 根据在 IP 网络之间转发来定义路由器。
2. 区分控制平面路由与数据平面转发。
3. 将默认路由视为最不具体的后备选择。
4. 认识到仅凭跳数不能衡量路径质量。
