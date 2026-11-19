---
lesson_id: "incident-timelines"
course_id: "incident-response"
lang: "zh"
order_index: 3
title: "事件时间线"
description: "学习在同一条时间线上排列证据，并标注不确定的事件时间。"
meta_title: "事件时间线 - 事件响应"
meta_description: "把不同来源的记录统一到同一时区，保留原始时间戳，并区分时间先后与因果关系。"
meta_keywords: "事件时间线, 时间戳, UTC, 时区, 事件响应, Linux Journey"
---

事件时间线会按发生顺序排列来自不同来源的观测结果。使用同一时区，也要在记录里保留原始时间戳。弄清事件顺序后，就可以进一步问哪些情况可能有关。

## 换算一条时间戳

这个例子中的 Web 报告采用 UTC，部署记录则使用比 UTC 快两小时的时区偏移。

```text
Deployment record:  2026-11-19 11:17:00 +02:00
Web report:         2026-11-19 09:22:00 UTC
```

在装有 GNU date 的 Linux 系统上，`-d` 读取给定的时间戳，`-u` 要求以 UTC 输出。以 `+` 开头的参数设置显示格式。

```bash
$ date -u -d '2026-11-19 11:17:00+02:00' '+%Y-%m-%d %H:%M:%S UTC'
```

结果是 `2026-11-19 09:17:00 UTC`。在这个例子里，它比 Web 报告早五分钟。

:::single-choice{#incident-timelines-earlier-event} 把时区统一后，哪条记录更早？

::option[部署记录。]{#incident-timelines-earlier-event-a .correct explanation="换算得到 09:17 UTC，早于 09:22 的报告。"}
::option[Web 报告。]{#incident-timelines-earlier-event-b explanation="屏幕上显示的小时数较小，是因为两条记录最初使用的时区不同。"}
::option[两件事发生在完全相同的时间。]{#incident-timelines-earlier-event-c explanation="统一后的两个时间相差五分钟。"}
:::

![记录的 GNU date 输出将 +02:00 时区的 11:17 换算为 09:17 UTC](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/incident-response/incident-timelines/normalize-utc.png)

## 区分观测和估计

报告可能说第一次故障大约在 09:19。应该保留这个估计的性质。用户报告问题的时间，与第一次请求真正失败的时间是两回事。为每一行注明来源以及时间精确到什么程度。

:::single-choice{#incident-timelines-estimated-time} 同事说大约在 09:19。时间线上应该怎么写？

::option[写成日志确认的 09:19:00 整。]{#incident-timelines-estimated-time-a explanation="消息来源只提供了一个估计时间。"}
::option[记为一项没有来源的事件。]{#incident-timelines-estimated-time-c explanation="要判断这个时间有多可靠，就需要知道来源。"}
::option[记为该报告给出的近似时间。]{#incident-timelines-estimated-time-b .correct explanation="这样既保留了报告所说的内容，也保留了它的精度。"}
:::

## 排列顺序，继续核实原因

部署可能发生在服务出问题之前，却未必是故障原因。检查受影响的路径有没有变化，以及其他信号是否支持两者相关。把尚未解答的问题记在时间线旁边。

:::single-choice{#incident-timelines-timeline-cause} 单凭整理好的顺序，能确认什么？

::option[部署导致了公开页面故障。]{#incident-timelines-timeline-cause-a explanation="顺序提示一种可能性，还不足以确定原因。"}
::option[记录中的部署早于 Web 报告。]{#incident-timelines-timeline-cause-c .correct explanation="这就是记录显示的时间关系。"}
::option[不可能还有其他相关事件。]{#incident-timelines-timeline-cause-b explanation="时间线只包含选定的观测结果。"}
:::

## 总结

现在，你可以整理一条时间线，同时保留证据和不确定性。

1. 始终按相同方式换算记录中的时区。
2. 注明每项时间的来源，并标记估计值。
3. 根据事件顺序选择后续检查。
