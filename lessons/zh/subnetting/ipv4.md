---
lesson_id: "ipv4"
course_id: "subnetting"
lang: "zh"
order_index: 1
title: "IPv4"
description: "学习 IPv4 地址、前缀、作用域和 Linux 接口输出之间的关系。"
meta_title: "IPv4 - 子网划分"
meta_description: "通过完整的 IPv4 地址 Linux 教程开始学习。本指南面向 Linux 初学者，介绍 IP 结构以及 ip addr 等重要命令行工具。"
meta_keywords: "IPv4, IP 地址, Linux 初学者, 学习 Linux, 完整 Linux 教程, 免费 Linux 在线课程, Linux 网络, ifconfig, ip addr"
---

IPv4 为经过路由的数据包提供 32 位源地址和目标地址。地址只有与其前缀、接口、作用域、路由策略和有效期结合起来才有意义，并不是整台设备的永久标识符。

## 点分十进制表示法

IPv4 显示为由点分隔的四个八位组：

```text
192.0.2.165
```

每个八位组的取值范围为 0 到 255，因此完整地址包含四个字节。前缀长度表示从开头起多少位属于网络前缀，例如 `192.0.2.165/24`。

:::single-choice{#ipv4-address-size}
IPv4 地址有多大？

::option[32 位，由四个八位组组成。]{#ipv4-thirty-two-bits .correct explanation="四组八位构成点分十进制表示。"}
::option[每个网络中都是 24 位。]{#ipv4-always-twenty-four explanation="/24 只是一种前缀长度，并不是每个 IPv4 地址的大小。"}
::option[128 个字节，并用冒号分隔。]{#ipv4-128-bytes explanation="IPv6 是 128 位，使用冒号分隔的十六进制表示。"}
:::

## 地址作用域与用途

并非每个 IPv4 地址都能进行全局路由。例如环回地址 `127.0.0.0/8`、链路本地地址 `169.254.0.0/16`、`10.0.0.0/8` 等私有范围，以及 `192.0.2.0/24` 等文档范围。多播和受限广播地址具有其他语义。

私有地址可以在相互独立的网络中重复使用。NAT 可以为外部通信转换这些地址，但私有路由域内部的通信并不需要 NAT。

:::single-choice{#ipv4-private-reuse}
为什么许多组织中都可以出现 `10.0.0.1`？

::option[每个实例都标识同一台物理路由器。]{#ipv4-same-router explanation="该地址在各自网络内具有意义，并不全球唯一。"}
::option[IPv4 路由器会忽略第一个八位组。]{#ipv4-ignore-octet explanation="所有地址位都会参与路由匹配。"}
::option[它属于可供私有网络重复使用的地址范围。]{#ipv4-private-range .correct explanation="互相独立的私有网络可以使用相同地址，而不向全球网络通告。"}
:::

## 检查 Linux IPv4 地址

使用以下命令显示 IPv4 分配：

```bash
$ ip -4 address show
```

下面这样的行报告的不只是地址：

```text
inet 192.0.2.165/24 brd 192.0.2.255 scope global dynamic eth0
```

它显示前缀、广播地址、作用域、动态来源标记和接口。其他行还可以显示有效期和首选期。一个接口可以拥有多个 IPv4 地址。

:::single-choice{#ipv4-ip-output-prefix}
`192.0.2.165/24` 中的 `/24` 表示什么？

::option[该地址会在 24 秒后过期。]{#ipv4-prefix-seconds explanation="有效期会单独报告。"}
::option[地址的前 24 位组成网络前缀。]{#ipv4-prefix-bits .correct explanation="剩余八位标识该前缀内的位置。"}
::option[该接口使用 TCP 端口 24。]{#ipv4-prefix-port explanation="CIDR 前缀表示法与传输端口无关。"}
:::

## 确定所选源地址

接口上存在某个地址，并不能证明 Linux 会对目标使用它。路由、策略规则、度量值和应用程序绑定都会影响源地址选择。使用以下命令查询当前路由决策：

```bash
$ ip route get 198.51.100.20
```

读取所选下一跳、接口和源地址，然后测试真实应用程序路径。没有控制台访问和回滚计划时，不要更改远程主机的地址。

:::single-choice{#ipv4-route-get-purpose}
`ip route get DESTINATION` 可以显示什么？

::option[完整互联网路径上每台路由器的配置。]{#ipv4-all-router-config explanation="本地查询不会查询下游设备配置。"}
::option[本地路由决策，包括接口和首选源地址。]{#ipv4-route-decision .correct explanation="它会针对所给目标评估当前主机的路由策略。"}
::option[目标用户的密码。]{#ipv4-password explanation="路由命令不会暴露应用程序凭据。"}
:::

## 总结

现在，你可以把 IPv4 地址作为接口和路由状态的一部分来解读。

1. 认识到 IPv4 由四个八位组组成，总计 32 位。
2. 将地址与其前缀结合起来解释。
3. 区分私有、环回、链路本地及其他作用域。
4. 检查地址分配和针对目标所选的源地址。
