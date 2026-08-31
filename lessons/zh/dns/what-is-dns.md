---
lesson_id: "what-is-dns"
course_id: "dns"
lang: "zh"
order_index: 1
title: "什么是 DNS？"
description: "了解 DNS 如何组织和解析分布式名称及不同类型的资源记录。"
meta_title: "什么是 DNS？ - DNS"
meta_description: "要学习 Linux 网络，理解 DNS 至关重要。本指南介绍域名系统（DNS）是什么、它如何将域名解析为 IP 地址，以及为何它是互联网不可或缺的地址簿。非常适合作为 Linux 学习的起点。"
meta_keywords: "DNS, 域名系统, IP 地址, 学习 Linux, Linux 学习, 主机名, Linux 网络, 初学者, 教程, 指南, LabEx Linux"
---

域名系统（DNS）是一个分布式、分层的数据库与查询协议。客户端可以用它获取与名称关联的类型化信息，包括地址、邮件路由、权威服务器、服务数据和验证记录。

## 名称与资源记录

DNS 所做的不只是把一个主机名转换为一个 IP 地址。`A` 记录保存 IPv4 地址，`AAAA` 记录保存 IPv6 地址，`MX` 记录保存邮件路由数据，`NS` 记录保存权威服务器名称，还有许多其他记录类型承载不同的数据。一个名称可以拥有多条记录，也可能根本没有地址记录。

:::single-choice{#dns-purpose-beyond-address}
为什么说 DNS 不只是主机名到地址的列表？

::option[它会为每个以太网帧永久分配 MAC 地址。]{#dns-mac-frames explanation="链路层邻居发现并不以这种方式使用 DNS。"}
::option[它存储多种服务与委派数据所需的类型化记录。]{#dns-typed-records .correct explanation="地址、邮件、权威、别名以及策略相关记录各有不同语义。"}
::option[它保证每个具名应用程序都处于健康状态。]{#dns-health-guarantee explanation="即使目标服务不可用，DNS 数据仍可能成功解析。"}
:::

## 分层名称

完全限定域名（FQDN）标识 DNS 树中的一条路径。在 `www.example.com.` 中，末尾的点表示根，`com` 位于根之下，`example` 位于 `com` 之下，而 `www` 是该域中的一个名称。用户界面通常省略末尾的点，但在配置中区分绝对名称和相对于本地域的名称时，这个点很重要。

:::single-choice{#dns-trailing-dot}
`www.example.com.` 末尾的点表示什么？

::option[DNS 根和一个绝对名称。]{#dns-root-dot .correct explanation="这个点结束了从具名节点到根的完整路径。"}
::option[匹配所有顶级域的通配符。]{#dns-dot-wildcard explanation="通配符使用 `*` 之类的标签，而不是根终止符。"}
::option[仅使用 IPv4 的指令。]{#dns-dot-ipv4 explanation="请求的地址族由记录类型控制。"}
:::

## 分布式权威

DNS 权威沿层级向下委派。根服务器将解析器引向顶级域服务器，顶级域服务器再将其引向受委派区域的权威服务器。各组织可以管理自己的权威数据，而无须由一台中央服务器存储整个全球命名空间。

:::single-choice{#dns-authoritative-data}
谁为一个受委派的 DNS 区域提供最终数据？

::option[任何曾经访问过该站点的浏览器。]{#dns-browser-authority explanation="浏览器缓存并不是该区域的权威来源。"}
::option[该区域配置的权威名称服务器。]{#dns-authoritative-servers .correct explanation="委派指定了负责提供权威回答的服务器。"}
::option[将数据包转发到该地址的每一台路由器。]{#dns-router-authority explanation="数据包转发与 DNS 权威是彼此独立的角色。"}
:::

## 解析与缓存

主机的存根解析器通常把查询发送给递归解析器。递归解析器可以使用仍然有效的缓存作答，或代表客户端查询 DNS 层级。记录的 TTL 限制了缓存条目通常可以复用的时长，这提高了系统的可扩展性，却也会使变更在缓存刷新前无法立即显现。

DNS 成功并不能证明路由、传输、TLS 或应用程序处于正常状态。DNS 失败也可能在任何外部查询发生前出现，因为 `/etc/hosts`、搜索后缀、本地缓存和名称服务策略都会影响系统解析器。

:::single-choice{#dns-cache-ttl-role}
DNS 记录的 TTL 主要控制什么？

::option[IP 数据包可以经过多少台路由器。]{#dns-ip-hop-limit explanation="IP TTL 或 Hop Limit 是另一个协议字段。"}
::option[应用程序必须保持健康多长时间。]{#dns-app-health-time explanation="DNS 缓存不提供任何服务可用性保证。"}
::option[解析器在正常规则下可以缓存该记录多长时间。]{#dns-cache-lifetime .correct explanation="缓存时间缩短或延长会影响查询负载与变更传播。"}
:::

## 总结

现在，你可以把 DNS 描述为一个类型化、带缓存且分层的数据系统。

1. 按用途区分 DNS 资源记录类型。
2. 从根开始向下解读完全限定域名。
3. 识别委派关系与权威责任。
4. 将名称解析与应用程序连接能力区分开来。
