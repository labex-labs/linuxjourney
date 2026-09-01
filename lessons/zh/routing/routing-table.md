---
lesson_id: "routing-table"
course_id: "routing"
lang: "zh"
order_index: 2
title: "路由表"
description: "学习如何读取 Linux 路由，并检查为某个目标选择的路由。"
meta_title: "路由表 - 路由"
meta_description: "理解 Linux 路由表的指南。学习如何解读 route 命令输出中的目标、网关、genmask 和 eth0 接口，掌握 Linux 路由表基础。"
meta_keywords: "Linux 路由表, genmask, eth0, route 命令, 网络路由, IP 路由, 目标, 网关, 子网掩码, Linux 网络"
---

Linux 路由状态决定对于某个 IP 目标，哪些下一跳、接口和源地址符合条件。旧式 `route -n` 视图仍然可见，但 `ip route` 能更直接地公开现代内核路由概念。

## 阅读 IPv4 路由

示例输出如下：

```text
$ ip -4 route show
default via 192.168.224.2 dev eth0 proto dhcp src 192.168.224.10 metric 100
192.168.224.0/24 dev eth0 proto kernel scope link src 192.168.224.10 metric 100
```

直连 `/24` 路由会将匹配的目标直接通过 `eth0` 发送。默认路由使用下一跳网关 `192.168.224.2`。`proto` 描述路由的安装方式，`src` 是匹配流量的首选源地址，度量值则帮助排列其他方面可比的路由。

:::single-choice{#routing-table-via-meaning} `via 192.168.224.2` 表示什么？

::option[唯一允许使用该路由的应用程序。]{#routing-table-application explanation="via 关键字不编码应用程序授权。"}
::option[该路由的下一跳网关。]{#routing-table-next-hop .correct explanation="数据包会装入发送给该链路内路由器的帧，同时保留其 IP 目标。"}
::option[该路由的文件系统挂载点。]{#routing-table-mount explanation="路由条目涉及网络转发，而不是文件系统。"}
:::

## 直连路由与默认路由

带有 `scope link` 且没有 `via` 下一跳的路由，会把该前缀视为可通过接口直接到达。默认路由匹配每个地址，但任何符合条件且更具体的路由都会优先于它。

:::single-choice{#routing-table-connected-route} 直连的 `scope link` 目标通常如何到达？

::option[即使匹配直连路由，也通过默认网关。]{#routing-table-connected-default explanation="直连前缀更具体，而且没有网关操作数。"}
::option[把目标转换为 DNS 服务器。]{#routing-table-connected-dns explanation="名称服务不属于已经选定的 IP 路由。"}
::option[完成邻居解析后，直接通过指定接口。]{#routing-table-direct .correct explanation="主机解析目标的链路内地址，并在本地构建帧。"}
:::

## 前缀长度与度量值

路由选择会考虑策略规则，并选择最长的合格前缀。度量值用于排列适当的可比路由；低度量值默认路由不会仅凭数字较小就覆盖匹配的 `/24`。

:::single-choice{#routing-table-prefix-before-default} 哪条路由通常对 `192.168.224.50` 匹配得更具体？

::option[`192.168.224.0/24 dev eth0`]{#routing-table-twenty-four .correct explanation="在列出的路由中，24 位匹配前缀最长。"}
::option[`default via 192.168.224.2`]{#routing-table-default-less-specific explanation="默认路由的前缀长度为零。"}
::option[`192.168.0.0/16 via 192.168.224.3`]{#routing-table-sixteen explanation="它覆盖该地址，但固定的位数少于 /24。"}
:::

## 策略规则与多张路由表

Linux 可以按照 `ip rule` 策略，根据源地址、标记、接口或其他选择条件查询多张路由表。因此，只查看主路由表可能会遗漏实际路径：

```bash
$ ip rule show
$ ip route show table all
```

网络命名空间和 VRF 也可以拥有独立状态。检查时应使用与受影响进程相同的上下文。

:::single-choice{#routing-table-policy-limit} 为什么仅运行 `ip route show` 可能无法解释应用程序路径？

::option[策略规则或另一个网络命名空间可能选择不同的路由状态。]{#routing-table-policy-context .correct explanation="有效查找取决于数据包属性和进程的网络上下文。"}
::option[Linux 路由表不包含目标前缀。]{#routing-table-no-prefixes explanation="目标前缀是基本路由键。"}
::option[应用程序从不发送 IP 数据包。]{#routing-table-apps-never explanation="应用程序流量通过网络和传输协议承载。"}
:::

## 查询生效路由

让内核评估目标和可选源地址：

```bash
$ ip route get 203.0.113.10
$ ip route get 203.0.113.10 from 192.168.224.10
```

结果预测当前时刻的本地查找。它不会发送探测，也不能证明邻居、下游、防火墙或应用程序可达。

:::single-choice{#routing-table-route-get-limit} `ip route get` 不会做什么？

::option[显示所选本地接口和下一跳。]{#routing-table-get-does-interface explanation="这些是查找结果中的主要字段。"}
::option[针对目标评估当前本地路由策略。]{#routing-table-get-does-policy explanation="该命令执行内核路由查找。"}
::option[证明数据成功经过每个下游跳点送达。]{#routing-table-get-not-probe .correct explanation="它是本地决策查询，而不是端到端网络探测。"}
:::

## 总结

现在，你可以读取 Linux 路由条目并查询实际生效的本地决策。

1. 区分直连路由与经由网关的路由。
2. 阅读前缀、接口、协议、源地址和度量值字段。
3. 在比较相关度量值前应用最长前缀匹配。
4. 考虑策略路由表、命名空间和 VRF。
5. 将 `ip route get` 视为查找，而不是可达性测试。
