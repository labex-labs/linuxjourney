---
lesson_id: "network-traffic-baselines"
course_id: "network-monitoring"
lang: "zh"
order_index: 5
title: "流量基线"
description: "判断流量变化是否异常之前，学习选择条件相近的时段进行比较。"
meta_title: "流量基线 - 网络监测"
meta_description: "为同一服务选择可比的流量基线，结合预期变更和采集范围解读差异。"
meta_keywords: "流量基线, 流量分析, 观测范围, 网络监测, 网络安全, Linux Journey"
---

**基线**描述在特定条件下通常会看到的表现。在流量监测中，可以用同一项服务在一天中同一时段的常见请求数或范围作为基线。

## 选择可比较的时间窗口

公开网页在工作时间可能收到更多访问。要找出变化，就应选择日常规律相近的时段比较。这个例子按五分钟统计同一项服务的请求量。

```text
Window                 Requests
Typical weekdays 09:00  90–120
Today 09:00                230
Typical nights 02:00       2–8
```

230 次请求明显高于工作日上午的常见范围。与深夜的范围相比，参考价值就没那么高。

:::single-choice{#network-traffic-baselines-baseline-fit} 哪一行适合作为今天 09:00 这个时间窗口的基线？

::option[02:00 的典型深夜流量。]{#network-traffic-baselines-baseline-fit-b explanation="这反映的是另一种流量规律。"}
::option[只看今天观测到的 230 次请求。]{#network-traffic-baselines-baseline-fit-c explanation="一个当前观测值还需要与参考值比较，才能说明发生了什么变化。"}
::option[工作日 09:00 的典型流量。]{#network-traffic-baselines-baseline-fit-a .correct explanation="它与正在核查的服务和一天中的时段相符。"}
:::

## 查找相关背景

公告横幅或定时任务都可能解释流量变化。先看请求路径、时间以及已获准的变更，再决定是否继续调查。基线能指出差异，为调查提供一个起点。

:::single-choice{#network-traffic-baselines-baseline-explain} 宣布上线后流量翻倍了。应该查什么？

::option[把流量变化直接当作账户被入侵的证据。]{#network-traffic-baselines-baseline-explain-a explanation="次数本身无法说明原因，也没有记录账户事件。"}
::option[把观测到的时间和路径与上线预期对照。]{#network-traffic-baselines-baseline-explain-b .correct explanation="这样可以用相关观测结果验证一种合理解释。"}
::option[忽略这一变化，因为上线总能解释每次流量高峰。]{#network-traffic-baselines-baseline-explain-c explanation="预期变化和其他无关活动可能同时出现。"}
:::

## 核对采集口径

即使实际流量没有变化，采集器配置调整也能影响计数。如果昨天开始监测另一个网络，就要核对每个时间窗口包含了哪些流量。记录比较所用的服务、观测位置、时间和单位。

:::single-choice{#network-traffic-baselines-changed-coverage} 采集器开始记录第二个站点。怎样让接下来的比较更有意义？

::option[使用相同站点和相同采集范围比较计数。]{#network-traffic-baselines-changed-coverage-c .correct explanation="统一范围，有助于区分流量变化和观测范围变化。"}
::option[直接比较两次的总数，不检查范围。]{#network-traffic-baselines-changed-coverage-a explanation="采集范围改变后，这两个总数就没那么容易直接比较。"}
::option[扩大时间窗口后，把新的总数与昨天的总数比较。]{#network-traffic-baselines-changed-coverage-b explanation="如果两个总数覆盖的站点和来源仍然不同，延长时间窗口也无法统一范围。"}
:::

## 总结

现在，你可以判断网络流量比较是否使用了有效的基线。

1. 匹配服务、时间和统计单位。
2. 解释差异前，先寻找预期的变更。
3. 查明采集覆盖范围是否改变。
