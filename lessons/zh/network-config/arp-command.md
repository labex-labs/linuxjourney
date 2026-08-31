---
lesson_id: "arp-command"
course_id: "network-config"
lang: "zh"
order_index: 5
title: "arp"
description: "学习如何检查和解读 Linux IPv4 ARP 与 IPv6 邻居缓存状态。"
meta_title: "arp - 网络配置"
meta_description: "了解 Linux ARP 命令、如何查看 ARP 缓存，以及 ARP 在网络通信中的作用。面向初学者的 ARP 指南。"
meta_keywords: "Linux ARP, ARP 缓存, ip neighbour show, 网络命令, Linux 网络, Linux 初学者, Linux 教程"
---

Linux 会在邻居表中存储最近解析的下一跳链路地址。以太网上的 IPv4 条目通过 ARP 学习，IPv6 则使用邻居发现。旧式 `arp` 命令只显示部分状态，而 `ip neighbor` 同时支持两个地址族。

## 查看邻居条目

检查所有条目或某个接口：

```bash
$ ip neighbor show
$ ip neighbor show dev enp1s0
```

条目包含 IP 地址、链路层地址、设备和可达性状态。启动后邻居表可能为空，并随着流量需要本地下一跳而填充。

:::single-choice{#arp-command-modern-view}
哪个命令显示现代 Linux 邻居表状态？

::option[`pwd neighbor`]{#arp-command-pwd explanation="pwd 报告 shell 工作目录。"}
::option[`ip neighbor show`]{#arp-command-ip-neighbor .correct explanation="它同时报告 IPv4 ARP 派生条目和 IPv6 邻居发现条目。"}
::option[`route --passwords`]{#arp-command-route-passwords explanation="路由检查不应存在这种暴露凭据的命令。"}
:::

## 解析 IPv4 邻居

链路内 IPv4 映射缺失时，主机会广播 ARP 请求，询问谁拥有目标地址。目标或明确执行代理 ARP 的路由器会作出回复。发送方缓存该映射，再发送等待中的帧。

对于远程 IP 目标，主机解析的是所选网关地址，而不是远程主机的 MAC。

:::single-choice{#arp-command-remote-target}
对于链路外目标，主机会解析哪个 IPv4 邻居？

::option[跨越所有路由器的最终远程服务器。]{#arp-command-final-server explanation="它的 MAC 地址在源链路上没有意义。"}
::option[解析器配置中列出的每台 DNS 服务器。]{#arp-command-all-dns explanation="邻居解析遵循所选路由，而不是解析器列表。"}
::option[所选链路内网关。]{#arp-command-gateway .correct explanation="本地以太网帧会发送给负责转发 IP 数据包的路由器。"}
:::

## 解读状态

常见状态包括 `REACHABLE`、`STALE`、`DELAY`、`PROBE`、`INCOMPLETE` 和 `FAILED`。`STALE` 表示最近的可达性确认已经过期；协议栈仍可使用缓存地址，并按需探测。`FAILED` 表示解析或可达性检测未成功，但原因可能是链路、VLAN、地址、路由、过滤问题或对端已关闭。

:::single-choice{#arp-command-stale-state}
`STALE` 是否表示已知邻居不可达？

::option[不是；它缺少最近确认，可以在使用时探测。]{#arp-command-stale-probe .correct explanation="该状态不等同于 FAILED。"}
::option[是，而且该条目永远无法再次使用。]{#arp-command-stale-dead explanation="过期条目仍是候选项，可以在可达性检查后转换状态。"}
::option[是，因为它的 DNS 记录已经过期。]{#arp-command-stale-dns explanation="邻居状态与 DNS 缓存相互独立。"}
:::

## 谨慎更改邻居状态

静态条目和缓存刷新都会改变状态，可能中断活动流量或隐藏原始证据。应先记录当前路由、数据包计数器和邻居状态。在获得授权的测试网络上，应优先使用针对性探测和数据包捕获，而不是刷新整个接口。

ARP 没有内置身份验证，因此重复地址或伪造回复可能污染映射。交换机保护、分段、监控和更高层身份验证有助于降低影响。

:::single-choice{#arp-command-flush-first}
为什么不应把刷新整个邻居表作为第一项诊断步骤？

::option[邻居条目只存储在 DNS 根服务器中。]{#arp-command-neighbors-dns explanation="它们由本地网络协议栈维护。"}
::option[刷新会永久移除接口硬件。]{#arp-command-flush-hardware explanation="它移除缓存条目，而不是物理设备。"}
::option[它会改变证据，并可能中断原本正常的下一跳。]{#arp-command-flush-disrupts .correct explanation="只读检查和针对性测试能保留诊断原因所需的状态。"}
:::

## 总结

现在，你可以检查邻居解析，而不会把每种缓存状态都当作故障。

1. 使用 `ip neighbor` 查看 IPv4 和 IPv6 状态。
2. 只有目标位于链路内时才直接解析它。
3. 为链路外 IP 流量解析网关。
4. 在针对性更改状态前保留缓存证据。
