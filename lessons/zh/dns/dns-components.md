---
lesson_id: "dns-components"
course_id: "dns"
lang: "zh"
order_index: 2
title: "DNS 组件"
description: "了解递归解析器、权威服务器、区域和资源记录如何划分 DNS 职责。"
meta_title: "DNS 组件 - DNS"
meta_description: "了解 DNS 的各项组件：名称服务器、区域文件和资源记录。通过初学者指南理解 DNS 的工作方式，开启 Linux 网络学习之旅！"
meta_keywords: "DNS 组件, 名称服务器, 区域文件, 资源记录, DNS 教程, Linux 网络, 初学者指南"
---

DNS 将面向客户端的递归查询职责与权威发布职责分开。理解这条边界，才能避免把缓存答案的提供者误当成区域的所有者。

## 存根解析器与递归解析器

应用程序或操作系统中的存根解析器将查询发送给已配置的递归解析器。递归解析器利用缓存，并在必要时执行迭代查询，最终返回查询结果、错误或转介结果。只有应答服务器对相关数据具有权威时，其回复才能带有权威应答标志；仅仅执行递归查询并不会使服务器成为权威。

:::single-choice{#dns-components-recursive-role} 递归解析器为存根客户端做什么？

::option[利用缓存和其他名称服务器取得最终 DNS 结果。]{#dns-components-recursive-result .correct explanation="客户端把多步骤查询工作委托给递归服务。"}
::option[取代数据包路径上的每一台网络路由器。]{#dns-components-replaces-router explanation="名称解析与 IP 转发是彼此独立的。"}
::option[成为其缓存的每条记录的权威来源。]{#dns-components-cache-authority explanation="缓存数据的权威仍来自其源头；解析器并不是区域所有者。"}
:::

## 权威名称服务器

权威服务器从自己有权管理的区域数据中作答。一个区域应配置多台数据同步的权威服务器，并考虑彼此独立的故障风险。仅提供权威服务的服务器无须为任意客户端执行递归查询。

:::single-choice{#dns-components-authoritative-role} 服务器因何成为某个区域的权威服务器？

::option[它曾经通过公共解析器查询过该区域。]{#dns-components-once-queried explanation="查询或缓存并不会赋予权威。"}
::option[它依据相关委派和配置提供该区域的数据。]{#dns-components-serves-zone .correct explanation="权威来自 DNS 委派和服务器加载的区域，而不是来自一份缓存副本。"}
::option[它对某一次 ping 的响应最快。]{#dns-components-fastest-ping explanation="ICMP 时延不能定义 DNS 权威。"}
:::

## 区域与区域存储

区域是 DNS 命名空间中由某个管理主体提供服务的一部分。它从区域顶点开始，并可继续委派子区域。区域数据可以存放在文本区域文件中，也可以从数据库生成、通过 API 加载或由软件合成；“区域文件”并不是强制要求的物理实现。

区域顶点通常拥有一条 SOA 记录和一组 NS 记录。父区域的委派数据标识子区域的权威服务器；有时还会附带粘合地址记录，以便访问名称位于该子区域内的服务器。

:::single-choice{#dns-components-zone-meaning} 什么是 DNS 区域？

::option[命名空间中由某个管理主体提供服务的一部分。]{#dns-components-admin-portion .correct explanation="无论采用何种存储后端，它都可以包含记录和委派。"}
::option[每台客户端上都必须存在的单个文本文件。]{#dns-components-client-file explanation="权威实现可以使用多种存储形式，客户端也不会保存每个区域。"}
::option[由 VLAN 标识的以太网广播域。]{#dns-components-vlan explanation="DNS 区域与链路层网段是彼此独立的概念。"}
:::

## 资源记录字段

一条资源记录包含所有者名称、TTL、类、类型和特定于类型的 RDATA。例如：

```text
www.example.com.  300  IN  A  192.0.2.25
```

所有者是 `www.example.com.`，TTL 为 300 秒，类是 Internet，类型是 IPv4 地址，RDATA 则是该地址。区域文件语法中的字段省略和相对名称规则要求你谨慎处理起点（origin）。

:::single-choice{#dns-components-mx-type} 哪种记录类型会发布邮件交换器的优先级和主机名？

::option[`A`]{#dns-components-a explanation="A 记录保存 IPv4 地址。"}
::option[`NS`]{#dns-components-ns explanation="NS 记录标识权威名称服务器。"}
::option[`MX`]{#dns-components-mx .correct explanation="MX 的 RDATA 包含优先级和邮件交换器名称。"}
:::

## TTL 与否定缓存

正面记录使用 TTL 限制缓存复用时间。经过确认的名称不存在等否定回答，也可以按照源自 SOA 的规则缓存。在计划变更前不久降低 TTL，只会影响缓存看到较低 TTL 后获取的记录；先前以较长 TTL 缓存的记录仍会保留到过期。

:::single-choice{#dns-components-lower-ttl-timing} 为什么要在计划更改地址之前很早就降低 DNS TTL？

::option[TTL 会修改服务器的以太网 MTU。]{#dns-components-ttl-mtu explanation="缓存生命周期与链路数据包大小无关。"}
::option[较低的 TTL 能保证新应用程序健康。]{#dns-components-ttl-health explanation="它影响缓存行为，而不是服务正确性。"}
::option[现有缓存需要时间，让按原先较长 TTL 获取的记录过期。]{#dns-components-old-cache-expiry .correct explanation="更改权威数据无法追溯缩短已缓存记录的剩余生命周期。"}
:::

## 总结

现在，你可以区分 DNS 的递归查询、权威、命名空间管理和记录缓存。

1. 识别存根解析器与递归解析器的职责。
2. 通过受委派区域的服务关系定义权威。
3. 把区域理解为命名空间责任，而不是某个必需文件。
4. 解读所有者、TTL、类、类型和 RDATA 字段。
5. 在 DNS 变更之前规划缓存生命周期。
