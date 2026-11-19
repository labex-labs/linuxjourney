---
lesson_id: "network-monitoring-alerts"
course_id: "network-monitoring"
lang: "zh"
order_index: 6
title: "网络告警"
description: "根据网络告警寻找支撑下一项防御决策所需的证据。"
meta_title: "网络告警 - 网络监测"
meta_description: "解读 DNS 告警的触发范围，用相关主机日志验证解释，并记录尚未查清的事项。"
meta_keywords: "网络告警, DNS 告警, 证据核查, 网络监测, 网络安全, Linux Journey"
---

网络告警表示监测条件已经满足。判断发生了什么之前，先读触发条件和数据来源。告警可能描述异常流量、反复失败，或预期观测结果缺失。

## 读懂告警覆盖的范围

下面的模拟告警基于 DNS 记录，把五分钟内的失败按客户端归组。

```text
Window: 09:20–09:25 UTC
Client: 192.0.2.10
Condition: at least 10 failed name lookups
Observed: 12 failures
```

这提示你检查查询内容和结果。仅凭告警还无法确定哪个程序发起了查询。

:::single-choice{#network-monitoring-alerts-alert-scope} 告警直接观测到了什么？

::option[记录中的客户端在这个时段有 12 次查询失败。]{#network-monitoring-alerts-alert-scope-b .correct explanation="这正是该告警报告的次数和范围。"}
::option[已经确认发生数据丢失。]{#network-monitoring-alerts-alert-scope-a explanation="规则只统计名称查询失败的次数。"}
::option[有 12 个不同的客户端。]{#network-monitoring-alerts-alert-scope-c explanation="告警将同一个客户端地址的记录归在一起。"}
:::

## 查找相关的主机记录

假设多数失败都在查询 `preview.example`。客户端的服务日志可能表明，某项过时的设置导致了反复重试。查看预计发出查询的程序在相近时间的记录。把活动归到某台机器之前，先核对监测系统使用的主机标签。

:::single-choice{#network-monitoring-alerts-evidence-choice} 哪条记录有助于核实，是否是某项服务反复重试查询？

::option[随后在另一台主机上出现的公开页面访问记录。]{#network-monitoring-alerts-evidence-choice-b explanation="端点和时间都与正在调查的模式不符。"}
::option[不带活动时间的已安装应用列表。]{#network-monitoring-alerts-evidence-choice-c explanation="知道软件已安装，仍无法说明哪个软件发出了查询。"}
::option[告警期间记录同一失败查询的服务日志。]{#network-monitoring-alerts-evidence-choice-a .correct explanation="这可以把查询模式与该程序联系起来。"}
:::

## 记录下一步判断

如果服务日志与告警匹配，记录原因，并在修正获准调整的配置后，验证一次有代表性的查询。如果证据仍不完整，写明还缺什么。把告警、支持结论的记录和核查结果一并保存。

:::single-choice{#network-monitoring-alerts-uncertainty} 手头只有 DNS 告警，没有对应的主机记录。应该怎么报告？

::option[已经识别出具体程序。]{#network-monitoring-alerts-uncertainty-a explanation="仅凭 DNS 证据无法识别进程。"}
::option[已确认查询模式，但还不知道哪个程序发起了查询。]{#network-monitoring-alerts-uncertainty-c .correct explanation="这样既保留了观测结果，也说明还缺什么。"}
::option[告警什么都无法说明。]{#network-monitoring-alerts-uncertainty-b explanation="告警仍然描述了解析器观测到的条件。"}
:::

## 核对预期的重试模式

假设团队安排了一项定时任务，会反复解析一个测试主机名。对照任务计划时间、DNS 记录中的名称和任务自己的日志。多项信息相符，可以支持这一解释。没有对上的失败记录仍需继续调查。

:::single-choice{#network-monitoring-alerts-final-application} 哪项发现最能支持是这个定时任务触发了告警？

::option[告警来自一台还运行其他定时任务的主机。]{#network-monitoring-alerts-final-application-c explanation="主机背景不能说明哪个程序发起了这些查询。"}
::option[任务日志记录了相同主机名，并且在告警时间窗口内有重试。]{#network-monitoring-alerts-final-application-a .correct explanation="名称和时间都匹配，有理由把观测到的模式与该任务联系起来。"}
::option[这项任务安排在当天的某个时间。]{#network-monitoring-alerts-final-application-b explanation="只知道大致日期，仍无法核对告警时段和查询名称。"}
:::

## 总结

现在，你可以根据网络告警安排有针对性的核查。

1. 识别检测规则及其覆盖范围。
2. 选择相关记录来验证一种解释。
3. 记下观测结果和还没有解决的问题。
