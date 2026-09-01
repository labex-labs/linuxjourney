---
lesson_id: "ipv6"
course_id: "subnetting"
lang: "zh"
order_index: 7
title: "IPv6"
description: "学习如何读取 IPv6 地址、前缀、作用域、自动配置和 Linux 路由状态。"
meta_title: "IPv6 - 子网划分"
meta_description: "面向初学者的 IPv6 协议指南。了解为何创建 IPv6、它与 IPv4 的区别，以及现代 Linux 网络中 IPv6 寻址方案的基础。"
meta_keywords: "IPv6, IPv4, IP 地址, Linux 网络, 网络协议, 互联网协议, 地址耗尽, 初学者, 教程, 指南"
---

IPv6 使用 128 位地址，旨在提供大得多的地址空间，同时更新数据包和邻居发现行为。IPv4 与 IPv6 是两种独立协议；双栈主机可以在网络过渡期间同时运行两者。

## 阅读 IPv6 表示法

IPv6 地址写成八个 16 位十六进制组：

```text
2001:0db8:0000:0000:0000:0000:0000:0025
```

每组开头的零可以省略，一段连续的零组可以使用 `::` 压缩：

```text
2001:db8::25
```

`::` 只能出现一次，否则无法确定省略了多少组。`2001:db8::/32` 保留用于文档示例。

:::single-choice{#ipv6-double-colon-rule} 为什么 `::` 在一个 IPv6 地址中最多出现一次？

::option[多个 `::` 标记会使展开结果不明确。]{#ipv6-compression-ambiguity .correct explanation="一个压缩标记可以展开成使地址恰好达到八组所需的组数。"}
::option[IPv6 地址只包含一个零位。]{#ipv6-one-zero explanation="一个地址可以包含许多零位和零组。"}
::option[该标记用于选择 TCP 端口零。]{#ipv6-port-zero explanation="地址压缩与传输端口无关。"}
:::

## 地址类型与作用域

重要地址和范围包括：

- `::1/128`：本地主机上的环回地址。
- `fe80::/10`：链路本地单播，通常存在于 IPv6 接口上。
- `2000::/3`：当前分配的全球单播空间。
- `ff00::/8`：多播。

IPv6 没有广播地址；多播和邻居发现承担 IPv4 中常由广播完成的用途。链路本地目标可能需要 `fe80::1%eth0` 这样的接口区域，因为每条链路上都存在相同前缀。

:::single-choice{#ipv6-link-local-scope} `fe80::/10` 地址的正常作用范围是什么？

::option[全球互联网上的每台主机。]{#ipv6-global-link-local explanation="全球单播地址用于经过路由的全球作用域。"}
::option[仅限 DNS 区域文件。]{#ipv6-dns-only explanation="链路本地地址会分配给接口，并用于网络通信。"}
::option[一条本地链路。]{#ipv6-one-link .correct explanation="路由器不会在链路之间转发普通链路本地流量。"}
:::

## 前缀与接口地址

IPv6 CIDR 表示法使用 `/0` 到 `/128` 的前缀长度。`/64` 是大多数 LAN 子网的标准大小，并支持无状态地址自动配置。一个接口可以同时拥有链路本地、稳定全球、临时隐私及其他地址，每个地址都有首选期和有效期。

:::single-choice{#ipv6-address-multiplicity} 为什么一个接口可能显示多个 IPv6 地址？

::option[IPv6 要求每个十六进制数字对应一个地址。]{#ipv6-one-per-digit explanation="数字只是表示法，并不是独立的接口分配。"}
::option[不同作用域以及隐私或有效期角色可以共存。]{#ipv6-several-roles .correct explanation="链路本地地址与一个或多个全球或临时地址同时存在是正常的。"}
::option[每个地址都标识一块独立的物理网卡。]{#ipv6-separate-card explanation="一个接口可以拥有多个地址。"}
:::

## 邻居发现与路由器发现

IPv6 邻居发现使用 ICMPv6 完成地址解析、重复地址检测、路由器发现和可达性信息交换。路由器通告可以提供前缀和默认路由器信息。主机可以将 SLAAC 与 DHCPv6 结合以获得其他配置；DHCPv6 通常不提供默认路由器。

阻止所有 ICMPv6 会破坏必要的协议行为。防火墙策略应在适当作用范围允许必需的消息类型，而不能把 ICMPv6 当作可有可无。

:::single-choice{#ipv6-default-router-source} IPv6 主机通常如何动态获得默认路由器？

::option[通过路由器通告。]{#ipv6-router-advertisements .correct explanation="路由器发现属于 ICMPv6 邻居发现的一部分。"}
::option[通过以太网广播地址。]{#ipv6-ethernet-broadcast explanation="IPv6 不使用 IP 广播地址。"}
::option[通过 TCP 三次握手。]{#ipv6-tcp-handshake explanation="TCP 在路由已经可用后才建立传输状态。"}
:::

## 检查和测试 IPv6

分别检查地址、路由和邻居：

```bash
$ ip -6 address show
$ ip -6 route show
$ ip -6 neighbor show
$ ping -6 -c 3 2001:db8::25
```

应使用真实分配的测试地址，而不是这里显示的文档地址。双栈应用程序可能通过 IPv4 成功而 IPv6 失败，反之亦然，因此应分别明确测试每个地址族及其 DNS `A` 或 `AAAA` 记录。

:::single-choice{#ipv6-dual-stack-test} 为什么要分别测试双栈服务的 IPv4 与 IPv6？

::option[每个 IPv6 数据包必须先变成 IPv4 广播。]{#ipv6-becomes-ipv4 explanation="原生 IPv6 与 IPv4 是两条不同协议路径。"}
::option[两个地址族可能具有不同的 DNS、路由、过滤和故障。]{#ipv6-independent-paths .correct explanation="成功的回退可能掩盖首选地址族已经损坏。"}
::option[IPv6 工具无法显示接口状态。]{#ipv6-tools-cannot explanation="ip -6 命令可以公开地址、路由和邻居状态。"}
:::

## 总结

现在，你可以读取和测试常见 IPv6 接口与路由状态。

1. 正确展开或压缩八个十六进制地址组。
2. 区分环回、链路本地、全球和多播作用域。
3. 预期一个接口上存在多个 IPv6 地址和有效期。
4. 保留必要的邻居发现与路由器通告流量。
5. 在双栈服务上分别测试 IPv4 和 IPv6 路径。
