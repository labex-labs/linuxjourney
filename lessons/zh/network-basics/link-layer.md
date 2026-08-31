---
lesson_id: "link-layer"
course_id: "network-basics"
lang: "zh"
order_index: 8
title: "链路层"
description: "学习以太网帧、邻居发现、交换机和路由器如何在本地链路上传送数据包。"
meta_title: "链路层 - 网络基础"
meta_description: "探索 TCP/IP 链路层基础。了解链路层标头如何构建、ARP 如何将 IP 地址解析为 MAC 地址，以及数据包在本地网络中的传输过程。"
meta_keywords: "链路层, 链路层标头, ARP, TCP/IP, MAC 地址, 网络基础, Linux 网络, 数据包传输, 地址解析协议"
---

链路层在一条本地介质或虚拟链路上传送网络层数据包。以太网和 Wi-Fi 的成帧细节不同，但两者都在 IP 之下提供本地传送。

## 以太网帧

以太网帧包含目标和源 MAC 地址、EtherType 或长度字段、载荷，以及帧校验序列尾部。物理传输还会使用前导码和帧起始定界符。帧校验序列用于检测链路上的损坏；它不会修复受损帧，也不会提供加密保护。

:::single-choice{#link-layer-fcs-purpose}
以太网帧校验序列有什么用途？

::option[检测链路上的帧损坏。]{#link-layer-detect-corruption .correct explanation="接收方可以丢弃未通过完整性检查的帧。"}
::option[为所有路由跳点加密载荷。]{#link-layer-fcs-encryption explanation="FCS 是错误检测码，不是加密或身份验证。"}
::option[根据 TCP 端口选择应用程序。]{#link-layer-fcs-port explanation="传输端口承载在 IP 载荷内部。"}
:::

## 交换机与本地传送

以太网交换机会学习哪些源 MAC 地址出现在各个端口，并将已知单播帧转发到所学习的目标端口。广播和部分未知目标流量会在广播域内泛洪。VLAN 可以把一个交换系统划分为多个独立的逻辑链路域。

:::single-choice{#link-layer-switch-learning}
以太网交换机通常会从帧中学习什么信息？

::option[应用程序密码和 HTTP Cookie。]{#link-layer-switch-passwords explanation="基本转发表使用链路地址，而不是应用程序凭据。"}
::option[每台路由器的完整互联网路由表。]{#link-layer-switch-routing-table explanation="二层交换与全局路由交换是不同功能。"}
::option[与交换机端口关联的源 MAC 地址。]{#link-layer-switch-source .correct explanation="学习结果会建立转发表，用于后续已知单播流量。"}
:::

## 解析下一跳地址

对于以太网上的 IPv4，地址解析协议会把链路上的 IPv4 下一跳地址映射为 MAC 地址。主机首先检查邻居缓存；如有需要，它会广播 ARP 请求，由地址所有者或授权代理回复。

对于不在链路上的 IP 目标，主机解析的是默认网关或所选网关的 MAC 地址，而不是远程目标的 MAC 地址。IPv6 使用基于 ICMPv6 的邻居发现，而不是 ARP。

:::single-choice{#link-layer-remote-destination-mac}
对于不在链路上的 IPv4 目标，主机使用哪个 MAC 地址？

::option[所选下一跳路由器的 MAC 地址。]{#link-layer-gateway-mac .correct explanation="IP 数据包仍以远程主机为目标，而本地帧会发送给路由器。"}
::option[跨越每台路由器使用远程服务器的 MAC 地址。]{#link-layer-remote-mac explanation="MAC 地址是本地链路标识符，不会端到端传送。"}
::option[从 TCP 目标端口派生的 MAC 地址。]{#link-layer-port-mac explanation="传输端口不决定链路地址。"}
:::

## 检查邻居状态

使用以下命令查看 IPv4 ARP 与 IPv6 邻居发现条目：

```bash
$ ip neighbor show
```

`REACHABLE`、`STALE`、`DELAY`、`PROBE` 和 `FAILED` 等状态描述邻居不可达检测过程。`STALE` 并不表示故障；它表示缓存中的可达性确认已经不够新，可以在使用时重新测试。

:::single-choice{#link-layer-stale-neighbor}
`STALE` 邻居条目表示什么？

::option[邻居被防火墙永久阻止。]{#link-layer-stale-blocked explanation="该状态不描述防火墙策略。"}
::option[MAC 地址已作为备份写入磁盘。]{#link-layer-stale-backup explanation="邻居状态是运行时缓存信息。"}
::option[缓存的映射缺少最近的可达性确认。]{#link-layer-stale-confirmation .correct explanation="协议栈仍可使用它，并按需执行可达性检测。"}
:::

## 跨越路由器的封装

发送方把 IP 数据包装入发送到下一跳的帧。路由器验证并移除传入帧、处理 IP 标头、选择传出路由，再为该链路构建新帧。接收方逆向移除封装，将传输层载荷送到适当的套接字。

:::single-choice{#link-layer-router-reframing}
普通转发过程中，以太网帧在路由器处改变时，什么保持不变？

::option[IP 目标地址，除非 NAT 等中间设备对其进行更改。]{#link-layer-ip-destination .correct explanation="普通路由器会朝最终 IP 目标转发，同时替换仅作用于当前跳点的帧。"}
::option[传入帧的校验序列。]{#link-layer-same-fcs explanation="新的传出帧会获得自己的链路完整性值。"}
::option[每条链路上的目标 MAC 地址。]{#link-layer-same-mac explanation="每条链路都会使用相应下一跳的链路地址。"}
:::

## 总结

现在，你可以跟踪 IP 数据包在一条本地链路上的传送步骤。

1. 识别以太网帧的主要字段和完整性尾部。
2. 解释交换机如何学习本地转发位置。
3. 使用 ARP 解析 IPv4 下一跳，使用 NDP 解析 IPv6 邻居。
4. 解读邻居缓存状态，而不夸大故障。
5. 认识到路由器会为每条传出链路重新构建帧。
