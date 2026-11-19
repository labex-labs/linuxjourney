---
lesson_id: "service-availability-errors"
course_id: "service-monitoring"
lang: "zh"
order_index: 3
title: "可用性与错误"
description: "学习结合同一时间窗口内的请求总数和失败次数来比较错误情况。"
meta_title: "可用性与错误 - 服务监控"
meta_description: "计算观察到的请求错误率，并判断时间范围、请求路径和样本量是否可比。"
meta_keywords: "可用性, 错误率, 请求总数, 时间窗口, 服务监控, Linux Journey"
---

即使服务能响应大多数访客，也可能有部分请求失败。用同一时间窗口内的请求总数和失败次数，可以算出观测到的请求中有多少比例失败了。

## 计算错误率

用失败请求数除以观测到的请求总数，得到**错误率**。将结果乘以 100，就可以用百分比表示。

```text
Window          Requests   Failures
09:00–09:05          100          2
09:05–09:10           20          2
```

第一个时段每一百个请求有两个失败，错误率是 2%。下一个时段也有两个失败，但总共只有二十个请求，因此错误率是 10%。

:::single-choice{#service-availability-errors-compare-windows} 哪个时段的失败比例更高？

::option[09:05 到 09:10。]{#service-availability-errors-compare-windows-b .correct explanation="二十次中有两次失败，比例高于一百次中有两次失败。"}
::option[两个时段一样，因为各有两次失败。]{#service-availability-errors-compare-windows-a explanation="两个时段的请求总数不同。"}
::option[09:00 到 09:05，因为这个时段的流量更大。]{#service-availability-errors-compare-windows-c explanation="在失败次数相同的情况下，请求总数越大，失败比例越小。"}
:::

## 保持统计范围一致

比较时要留意时间窗口、请求路径和失败的定义。即使需要调用依赖服务的网页发生故障，健康检查端点也可能正常响应。如果你关心的是使用某个网页的体验，就要统计这个网页的请求。

:::single-choice{#service-availability-errors-route-scope} 健康检查端点始终正常，但顾客报告结账时出现错误。应该查看什么？

::option[只看健康检查端点的响应。]{#service-availability-errors-route-scope-b explanation="这些响应描述的是另一项操作。"}
::option[服务账户的名称。]{#service-availability-errors-route-scope-c explanation="账户名称无法统计受影响的请求。"}
::option[结账请求以及其中的失败情况。]{#service-availability-errors-route-scope-a .correct explanation="用户报告的问题发生在结账路径上。"}
:::

## 解读低流量时段

如果来了两个请求，其中一个失败，观测到的错误率就是 50%。这个结果只描述手上的样本。请求很少时，百分比容易大幅波动，所以要把请求数与百分比一起展示。如果没有真实请求，就无法为这段流量计算错误率。单独安排定时检查，仍可确认一次测试请求是否成功。

:::single-choice{#service-availability-errors-zero-traffic} 某个时段没有访客请求。应该怎样描述访客请求的错误率？

::option[这证明服务可用性完美。]{#service-availability-errors-zero-traffic-a explanation="没有观测到访客请求，无法证明这一点。"}
::option[该时段没有可供计算错误率的请求数据。]{#service-availability-errors-zero-traffic-c .correct explanation="要确认服务能否响应，可另外进行测试。"}
::option[错误率肯定是 100%。]{#service-availability-errors-zero-traffic-b explanation="没有观测到请求，分母为零，无法计算。"}
:::

## 总结

现在，你可以在说明错误率时交代必要的背景。

1. 在同一时间窗口内比较失败次数和请求总数。
2. 根据要回答的问题选择请求路径和失败定义。
3. 流量稀少时也展示请求总数。
