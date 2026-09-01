---
lesson_id: "dns-process"
course_id: "dns"
lang: "zh"
order_index: 3
title: "DNS 解析过程"
description: "了解存根解析器和递归解析器如何利用缓存、转介、粘合记录与权威来回答 DNS 查询。"
meta_title: "DNS 解析过程 - DNS"
meta_description: "逐步探索从根服务器到权威 DNS 服务器的 DNS 解析过程。了解 Linux 服务器如何找到域名，这是生产环境和域名托管中的关键概念。"
meta_keywords: "DNS 过程, DNS 查询, 域名解析, Linux DNS, 生产服务器, 域名托管, DNS 服务器, 顶级域, 根服务器, 权威 DNS"
---

普通应用程序会询问操作系统的存根解析器；存根解析器先查询本地名称服务策略，再向已配置的解析器发送递归查询。只有在仍然有效的缓存无法回答问题时，递归解析器才会遍历 DNS 层级。

## 从本地策略和缓存开始

系统解析器可以按照配置的顺序查询 `/etc/hosts`、DNS 和其他来源。搜索后缀可能把一个短名称转换成多个候选名称。递归解析器随后会先检查正面和否定缓存条目，再决定是否发送上游流量。

:::single-choice{#dns-process-cache-first} 为什么递归解析器可能完全不联系任何权威服务器？

::option[DNS 要求每次查询必须先在本地失败。]{#dns-process-requires-failure explanation="解析器可以立即用缓存作答。"}
::option[它拥有一条仍然有效的缓存答案。]{#dns-process-valid-cache .correct explanation="缓存可以避免在记录生命周期结束前重复遍历 DNS 层级。"}
::option[权威服务器只接受来自客户端的以太网帧。]{#dns-process-authoritative-ethernet explanation="DNS 使用 IP 传输协议，可以跨越路由网络。"}
:::

## 查询根服务器

缓存未命中时，递归解析器可以查询根服务器。DNS 根拥有 A 到 M 共 13 个具名服务器标识，并通过任播等弹性部署技术由许多物理实例提供服务。其响应通常会把解析器转介给相关顶级域的权威服务器，而不是直接返回最终主机地址。

:::single-choice{#dns-process-root-response} 对于未缓存的 `www.example.com` 查询，根服务器通常会返回什么？

::option[指向 `com` 顶级域服务器的转介。]{#dns-process-root-referral .correct explanation="DNS 层级通过委派划分职责，而不是在根中存储每个最终主机记录。"}
::option[`www.example.com` 托管的网页。]{#dns-process-root-webpage explanation="DNS 返回资源记录数据，而不是应用程序内容。"}
::option[目标的以太网 MAC 地址。]{#dns-process-root-mac explanation="MAC 地址在本地链路上解析，而不通过 DNS 层级。"}
:::

## 跟随顶级域与权威转介

解析器询问 `com` 权威服务器，后者返回 `example.com` 受委派的权威名称服务器。如果需要访问名称位于受委派子区域内的服务器，转介中可以包含粘合地址记录。随后，解析器向一台权威服务器查询所请求的记录。

:::single-choice{#dns-process-glue-purpose} DNS 粘合记录帮助解决什么问题？

::option[在 DNS 解析后加密 HTTP 载荷。]{#dns-process-glue-http explanation="TLS 或其他应用安全机制负责载荷加密。"}
::option[选择最快的以太网交换机端口。]{#dns-process-glue-switch explanation="粘合记录是委派地址数据，不是链路转发策略。"}
::option[无需循环解析即可访问名称位于区域内的服务器。]{#dns-process-glue-reachability .correct explanation="父区域提供联系名称位于子区域内的服务器所需的地址数据。"}
:::

## 跟随别名与记录类型

回答中可能包含需要再次查询名称的 CNAME 别名，也可能包含会引发更多查询的应用专用记录。查询 `A` 只会返回 IPv4 地址记录及相关链路数据；必须另行查询 `AAAA` 才能获取 IPv6 地址。最终响应会带有 `NOERROR`、`NXDOMAIN` 或 `SERVFAIL` 等状态，而这些状态各有不同含义。

:::single-choice{#dns-process-nxdomain-meaning} `NXDOMAIN` 表示什么？

::option[根据权威结果，查询的域名不存在。]{#dns-process-name-does-not-exist .correct explanation="这不同于名称存在但没有所请求的记录类型。"}
::option[名称存在，并且始终有一条空的 A 记录。]{#dns-process-empty-a explanation="名称存在但没有请求的数据时，通常产生无数据响应，而不是 NXDOMAIN。"}
::option[解析器达到了以太网帧的最大尺寸。]{#dns-process-frame-size explanation="该状态描述的是名称是否存在。"}
:::

## 验证、缓存与应用程序使用

执行验证的递归解析器可以使用 DNSSEC 签名和信任链，验证经认证的否定回答或记录完整性。DNSSEC 不会加密查询，也无法证明返回地址上的应用程序值得信任。

解析器按照 TTL 规则缓存结果并将其返回给存根解析器。应用程序随后选择一个地址，并尝试自己的网络协议与安全协议。

:::single-choice{#dns-process-dnssec-limit} DNSSEC 验证不提供什么？

::option[已签名 DNS 数据的完整性和来源认证。]{#dns-process-dnssec-does-integrity explanation="这些正是 DNSSEC 的核心目标。"}
::option[对已签名的不存在数据进行认证否定。]{#dns-process-authenticated-denial explanation="签名否定机制可以提供这种验证。"}
::option[DNS 查询和响应的机密性。]{#dns-process-no-confidentiality .correct explanation="加密需要 DoT 或 DoH 等独立的受保护 DNS 传输。"}
:::

## 总结

现在，你可以追踪一次递归 DNS 查询从本地策略到缓存最终响应的全过程。

1. 先检查本地来源和解析器缓存。
2. 跟随根与顶级域的转介。
3. 使用粘合记录访问适当的受委派服务器。
4. 区分别名、无数据回答和名称不存在。
5. 将 DNSSEC 完整性与传输机密性区分开来。
