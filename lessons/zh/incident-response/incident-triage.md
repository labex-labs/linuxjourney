---
lesson_id: "incident-triage"
course_id: "incident-response"
lang: "zh"
order_index: 1
title: "事件研判"
description: "学习从初始事件报告中划定范围，开始第一轮调查。"
meta_title: "事件研判 - 事件响应"
meta_description: "明确受影响的服务、时间和症状，判断当前影响，并选择最值得先看的证据。"
meta_keywords: "事件研判, 事件影响, 初步调查, 事件响应, Linux Journey"
---

最初的报告可能只说网页出错了，或者触发了告警。**事件研判**是确定哪些情况需要优先处理。决定如何响应之前，先记下受影响的服务、时间和观察到的现象。

## 阅读报告

一位同事写下了这份模拟报告。

```text
09:22 UTC: Visitors received 503 from the public homepage.
The staff preview still loaded during the same check.
First failure observed at approximately 09:19 UTC.
```

报告列出了两条访问路径和两种不同的结果。先核实公开主页的实际结果，并记录检查时间和使用的地址。

:::single-choice{#incident-triage-affected-service} 第一次检查应该关注哪个症状？

::option[员工预览页面返回 503。]{#incident-triage-affected-service-b explanation="报告说预览页仍能正常加载。"}
::option[公开主页返回 503。]{#incident-triage-affected-service-a .correct explanation="报告指出受影响的正是这条路径。"}
::option[另一台无关主机上的页面找不到。]{#incident-triage-affected-service-c explanation="那条路径不在这份报告的范围内。"}
:::

## 估计影响

检查受到影响的用户或请求数量，以及服务是否还可使用。确认事件现在是否仍在发生。如果估计尚不确定，就明确把它写成估计，直到有更充分的证据。按事件响应计划决定需要通知谁。

:::single-choice{#incident-triage-triage-scope} 哪项观测有助于判断问题现在是否仍然紧急？

::option[对失败路径进行当前检查，并查看近期请求结果。]{#incident-triage-triage-scope-b .correct explanation="这样能判断症状是否还存在，以及影响范围有多大。"}
::option[仓库第一次提交距今多久。]{#incident-triage-triage-scope-a explanation="这无法说明当前的影响。"}
::option[只看最初报告上的严重程度标签。]{#incident-triage-triage-scope-c explanation="原标签可供参考，当前的影响才能帮助判断是否依然紧急。"}
:::

## 选择第一项有用的操作

如果现在请求仍然失败，保留检查结果，再查看受影响时段的服务变更和日志。另一条仍然正常的路径可以缩小排查范围。不要把第一个说得通的解释当成已确认的原因。

:::single-choice{#incident-triage-first-next-step} 公开路径依然失败，员工预览仍然正常。接下来应该查看什么？

::option[公司所有无关项目。]{#incident-triage-first-next-step-a explanation="报告已经把范围缩小到特定服务和时段。"}
::option[其他日期里随便找的一条错误。]{#incident-triage-first-next-step-b explanation="先查看观测到故障前后的证据。"}
::option[报告时段内公开访问路径的记录。]{#incident-triage-first-next-step-c .correct explanation="这些记录有助于区分路由问题和服务故障。"}
:::

## 总结

现在，你可以针对事件报告安排有明确范围的初步响应。

1. 说清受影响的路径、时间和症状。
2. 核查用户当前受到的影响。
3. 确定接下来要看哪个数据来源。
