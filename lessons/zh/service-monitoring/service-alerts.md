---
lesson_id: "service-alerts"
course_id: "service-monitoring"
lang: "zh"
order_index: 6
title: "服务告警"
description: "学习读懂告警的触发条件、时间窗口和下一步检查。"
meta_title: "服务告警 - 服务监控"
meta_description: "根据阈值、样本数和观测时段解读告警，并核查用户现在是否仍受影响。"
meta_keywords: "告警, 触发阈值, 时间窗口, 用户影响, 服务监控, Linux Journey"
---

仪表板用来显示测量结果。**告警**则提示人们关注某个可能需要处理的情况。实用的告警会让读者弄清发生了什么，以及接下来该查什么。

## 读懂触发条件

假设一条规则检查五分钟内是否有超过 5% 的主页请求失败。它还要求至少观察到 100 个请求，确保样本量对这个服务有意义。

```text
Window   09:10–09:15 UTC
Route    /
Requests 120
Failures 12
```

120 个请求中有 12 个失败，错误率为 10%，规则的两个条件都满足了。告警指出的是观测到的主页请求失败。

:::single-choice{#service-alerts-condition-match} 如果十个请求里有一个失败，同一条规则会发出告警吗？

::option[不会，因为没有达到最低请求数。]{#service-alerts-condition-match-b .correct explanation="错误率和请求数量都必须满足这条规则。"}
::option[会，因为错误率超过了 5%。]{#service-alerts-condition-match-a explanation="这条规则还要求至少有 100 个请求。"}
::option[不会，因为十个请求里一个失败的错误率是 1%。]{#service-alerts-condition-match-c explanation="十次中有一次失败是 10%，但请求数仍达不到规则要求。"}
:::

## 核对时间窗口

即使仪表板上的当前状态看起来正常，也要使用告警写明的时间窗口。告警可能描述的是稍早发生的情况。确认指标是否回到了平时的范围，也要检查用户需要的功能是否已经恢复。

:::single-choice{#service-alerts-alert-window} 告警在 09:16 到达，描述的是 09:10 到 09:15 的情况。应该先在哪里找相关错误？

::option[只看上一周的报告。]{#service-alerts-alert-window-b explanation="上周报告可以作为基线，但不包含这次受影响的时间段。"}
::option[只看 09:16 之后的记录。]{#service-alerts-alert-window-c explanation="通知可能在观测到异常之后才送达。"}
::option[查告警注明的时间窗口。]{#service-alerts-alert-window-a .correct explanation="这是该规则统计错误的时段。"}
:::

## 选择有用的下一步

关于主页请求失败的告警，可以附上这条路径的指标和近期日志。分别核查用户是否受影响以及背后的原因。如果服务已经恢复，也应保留足够的背景，便于调查重复出现的告警。

:::single-choice{#service-alerts-next-check} 哪个操作能直接检查主页是否仍然失败？

::option[统计缓存里的所有容器镜像。]{#service-alerts-next-check-a explanation="告警描述的是实际请求的结果。"}
::option[向受影响的路径发出经批准的测试请求。]{#service-alerts-next-check-c .correct explanation="一次新的请求可以检查报告的问题是否还影响这条路径。"}
::option[禁用规则，让仪表板安静下来。]{#service-alerts-next-check-b explanation="这只改变通知，不会检查服务状态。"}
:::

## 总结

现在，你可以读懂告警，并决定要验证什么。

1. 查看指标、阈值和最小样本量。
2. 根据告警的时间窗口查找对应的证据。
3. 用适当的检查验证用户看到的症状。
