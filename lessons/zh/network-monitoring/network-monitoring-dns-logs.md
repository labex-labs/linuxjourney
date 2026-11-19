---
lesson_id: "network-monitoring-dns-logs"
course_id: "network-monitoring"
lang: "zh"
order_index: 3
title: "DNS 日志"
description: "区分 DNS 查询、查询应答，以及之后的应用连接。"
meta_title: "DNS 日志 - 网络监测"
meta_description: "解读 DNS 日志里的查询类型、结果和应答，并核查客户端之后是否建立连接。"
meta_keywords: "DNS 日志, DNS 查询, NOERROR, NXDOMAIN, 网络监测, Linux Journey"
---

客户端在按名称连接服务前，可能会先通过 DNS 查询地址。解析器可以记录查询及其结果。**解析器**负责为客户端查找名称。

## 识别查询内容

DNS 日志可以包含时间、客户端地址、查询名称和请求的记录类型。`A` 查询请求的是 IPv4 地址。

```text
09:21:00Z client=192.0.2.10 query=site.example type=A result=NOERROR answer=192.0.2.20
09:21:03Z client=192.0.2.10 query=preview.example type=A result=NXDOMAIN
```

第一条结果包含 `site.example` 的地址。第二条报告，在这次查询中 DNS 没有找到与 `preview.example` 匹配的名称。

:::single-choice{#network-monitoring-dns-logs-lookup-name} 哪一行返回了所查询名称的 IPv4 地址？

::option[site.example 的查询结果。]{#network-monitoring-dns-logs-lookup-name-a .correct explanation="这一行的应答包含 IPv4 地址。"}
::option[preview.example 的查询结果。]{#network-monitoring-dns-logs-lookup-name-b explanation="NXDOMAIN 表示从该查询所用的视图来看，查询的名称不存在。"}
::option[两行都返回了，因为客户端相同。]{#network-monitoring-dns-logs-lookup-name-c explanation="两条记录来自同一客户端，但查询结果不同。"}
:::

## 读取查询结果

`NOERROR` 表示 DNS 交换没有报告协议错误。还要查看应答字段。响应可以显示 `NOERROR`，但没有返回所请求类型的地址记录。查询失败也可能显示为其他结果，例如客户端记录的超时。

:::single-choice{#network-monitoring-dns-logs-no-answer} 某行 DNS 日志显示 NOERROR，但没有地址应答。应该怎么报告？

::option[客户端一定收到了 IPv4 地址。]{#network-monitoring-dns-logs-no-answer-a explanation="应答字段显示示例中有哪些地址返回。"}
::option[网站肯定拒绝了浏览器连接。]{#network-monitoring-dns-logs-no-answer-c explanation="这条记录描述的是 DNS 查询结果，没有涉及浏览器请求。"}
::option[这次交换没有报告协议错误，该行没有给出地址。]{#network-monitoring-dns-logs-no-answer-b .correct explanation="结果字段和应答字段分别回答不同的问题。"}
:::

## 单独追踪后续连接

客户端可以先查找名称，再决定是否发起连接。要确认连接是否发生，需要找匹配的流记录或连接记录，并对照端点和时间。DNS 结果可以缓存，因此即使已经建立连接，手头的日志里也可能没有新的查询。

:::single-choice{#network-monitoring-dns-logs-dns-vs-flow} 什么证据最能表明客户端后来确实连接了返回的地址？

::option[从另一个界面查看同一条 DNS 应答。]{#network-monitoring-dns-logs-dns-vs-flow-a explanation="应答只列出一个可供客户端使用的地址。"}
::option[显示相应目标地址的连接记录或流记录。]{#network-monitoring-dns-logs-dns-vs-flow-c .correct explanation="这会把后续流量与名称查询分别记录下来。"}
::option[同一个客户端再次发起的 DNS 查询。]{#network-monitoring-dns-logs-dns-vs-flow-b explanation="新查询可以确认重复发生了名称解析活动，无法验证后续的应用连接。"}
:::

## 总结

现在，你可以解读 DNS 日志，并将它与后续网络活动区分开来。

1. 找出客户端、查询名称和请求的记录类型。
2. 结合结果和应答解读查询。
3. 另找记录核实后续连接。
