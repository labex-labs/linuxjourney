---
lesson_id: "nat-network-address-translation"
course_id: "subnetting"
lang: "zh"
order_index: 6
title: "NAT"
description: "学习源地址、目标地址和端口转换如何修改 IPv4 流量与连接状态。"
meta_title: "NAT - 子网划分"
meta_description: "了解 Linux 中的 NAT（网络地址转换）、它的工作原理及其在网络安全中的作用，并理解私有 IP 与公网 IP 的区别。"
meta_keywords: "NAT, 网络地址转换, Linux 网络, 私有 IP, 公网 IP, Linux 教程, 初学者指南"
---

网络地址转换会在数据包经过转换设备时重写地址字段，而且通常也会重写传输端口。它广泛用于通过较少的外部可路由地址连接采用私有地址的 IPv4 网络。

## 源地址转换

源 NAT 会在数据包离开网络时替换其源地址。多对一部署还会转换源端口，使多个内部流可以共享一个外部地址。这种考虑端口的形式通常称为 NAPT、PAT；当外部地址可能变化时，也常称为伪装。

转换器会跟踪映射，以便把回复数据包转换回原始内部端点。它通常转发同一个传输流，不必像应用程序代理那样建立单独的代理连接。

:::single-choice{#nat-source-translation} 源 NAT 会更改出站数据包的什么内容？

::option[只更改目标应用程序的文件权限。]{#nat-file-permissions explanation="NAT 操作网络和传输标头，而不是远程文件系统。"}
::option[更改源地址；在多对一使用中通常还会更改源端口。]{#nat-source-fields .correct explanation="该映射使返回流量能够与原始内部流关联。"}
::option[永久更改客户端存储的 DNS 名称。]{#nat-dns-name explanation="转换不会重写客户端的名称服务数据库。"}
:::

## 目标地址转换

目标 NAT 会重写目标地址或端口，常用于通过外部端点发布内部服务。端口转发规则可以把外部 TCP 端口映射到不同的内部地址和端口。返回流量需要进行一致的反向转换。

:::single-choice{#nat-port-forward} 哪种 NAT 形式通常用于实现入站端口转发？

::option[仅在路由查找前执行源 NAT。]{#nat-snat-port-forward explanation="发布内部目标需要转换目标字段。"}
::option[完全不进行地址或端口转换。]{#nat-no-translation explanation="按照定义，端口转发规则就是转换策略。"}
::option[目标 NAT。]{#nat-dnat .correct explanation="DNAT 将外部目标映射到所选内部服务端点。"}
:::

## NAT 与防火墙策略

NAT 不是防火墙。有状态转换器可能没有与未经请求的入站流量对应的映射，但显式转发、目标转换、过滤和应用程序暴露共同决定哪些内容可达。安全策略应通过防火墙规则、最小权限服务和端到端控制明确表达并接受审计，而不能从地址重写中推断。

:::single-choice{#nat-not-firewall} 为什么不能把 NAT 本身视为安全策略？

::option[NAT 会自动加密每个载荷。]{#nat-encrypts explanation="地址转换不提供载荷机密性。"}
::option[转换规则与流量过滤规则的用途不同。]{#nat-filter-separate .correct explanation="即使存在转换，可达性和授权仍需要明确的过滤与服务策略。"}
::option[NAT 会阻止管理员定义防火墙规则。]{#nat-prevents-firewall explanation="转换与防火墙策略通常会共存。"}
:::

## 运维影响

NAT 可能耗尽地址和端口映射、增加点对点协议的复杂性、让应用程序看不到原始来源，并要求特殊处理在协议中嵌入地址的情况。如果需要追踪流量，日志必须保留转换时间戳和映射详情。

在 Linux 上，现代策略通常使用 nftables 和连接跟踪进行配置。更改前应检查实际规则集：

```bash
$ sudo nft list ruleset
$ sudo conntrack -L
```

第二条命令需要 conntrack 工具和特权。更改规则集可能中断远程访问，因此应准备控制台恢复、原子配置、验证和回滚。

:::single-choice{#nat-trace-flow} 将共享地址流量追溯到内部客户端需要什么证据？

::option[只需要外部地址，不需要时间或端口。]{#nat-address-only explanation="许多客户端和流都可能共享该地址。"}
::option[只需要客户端显示的主机名。]{#nat-hostname-only explanation="转换器映射数据包元组，并不一定映射主机名。"}
::option[包含协议和端口且经过时间关联的转换映射。]{#nat-correlated-mapping .correct explanation="完整元组和时间戳可以区分并发转换流。"}
:::

## 总结

现在，你可以区分地址转换、路由、代理和防火墙策略。

1. 识别出站流上的源地址转换。
2. 识别已发布服务中的目标地址转换。
3. 理解端口映射如何实现地址共享。
4. 应用显式过滤，而不是把 NAT 当作安全机制。
5. 更改期间保留映射证据和恢复通道。
