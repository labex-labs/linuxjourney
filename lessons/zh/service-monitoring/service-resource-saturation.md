---
lesson_id: "service-resource-saturation"
course_id: "service-monitoring"
lang: "zh"
order_index: 5
title: "资源饱和度"
description: "学习结合资源利用率和队列，判断服务在哪个环节可能接近容量上限。"
meta_title: "资源饱和度 - 服务监控"
meta_description: "比较工作池的利用率与积压，区分短时高峰与持续的资源压力。"
meta_keywords: "资源饱和度, 利用率, 工作池, 队列, 服务监控, Linux Journey"
---

如果服务收到的任务超出某项资源能立即处理的数量，请求就可能需要等待。持续等待会表现为队列积压或响应变慢。

## 理解容量与需求

**利用率**描述资源已被使用的程度。例如，一个工作池可能最多同时处理四个任务。四个工作单元都忙时，说明工作池当前已用满。此时如果有新任务到达，它可以先进入队列，等其中一个工作单元空闲。

:::single-choice{#service-resource-saturation-worker-capacity} 四个工作单元都忙，另有三个任务在排队。可以得出什么结论？

::option[正好有七个工作单元在运行。]{#service-resource-saturation-worker-capacity-b explanation="其中三个任务在等待，还没有占用工作单元。"}
::option[所有请求都已经失败了。]{#service-resource-saturation-worker-capacity-c explanation="有工作单元空闲时，等待的任务还可以继续处理。"}
::option[所有处理位置都被占用，还有任务在等待。]{#service-resource-saturation-worker-capacity-a .correct explanation="忙碌的工作单元数反映当前使用情况，队列则显示超出的需求。"}
:::

## 比较不同时刻的指标

短时突发与连续几次观察到的队列增长不同。应在同一时间窗口内把队列、请求延迟和流量放在一起比较。

```text
Time   Busy workers   Queued jobs   Typical response
09:10       2 / 4           0             80 ms
09:11       4 / 4           5            300 ms
09:12       4 / 4          14            640 ms
```

在这个例子里，工作池一直用满，队列还在增长。这说明任务到达的速度可能超过了完成速度。接下来应检查工作单元都在忙什么。

:::single-choice{#service-resource-saturation-sustained-pressure} 哪个现象最能说明资源持续承压？

::option[09:10 有两个工作单元在忙。]{#service-resource-saturation-sustained-pressure-a explanation="这一行显示还有闲置容量，没有任务等待。"}
::option[所有工作单元一直忙，队列也在增长。]{#service-resource-saturation-sustained-pressure-b .correct explanation="处理能力持续被占用，等待的任务越积越多。"}
::option[队列仍为空，但有一次响应变慢。]{#service-resource-saturation-sustained-pressure-c explanation="一次慢响应值得留意，但多次观察到容量用满且队列增长，更能说明压力持续存在。"}
:::

![模拟的工作池指标显示所有单元都在忙，排队任务逐渐增加](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/service-monitoring/service-resource-saturation/worker-queue.png)

## 调查原因

工作单元持续忙碌，可能是因为请求来得更快，也可能是依赖服务变慢，或近期的改动让每个任务花费更多时间。把请求量、处理耗时与依赖服务的观测结果相互比较，再决定如何处理。

:::single-choice{#service-resource-saturation-next-observation} 请求量没有变化，但每个任务开始花更长时间。查什么有助于解释积压？

::option[对照任务耗时与依赖服务的耗时。]{#service-resource-saturation-next-observation-c .correct explanation="这样可以找出任务为什么占用处理位置更久。"}
::option[先扩容，再考虑收集其他证据。]{#service-resource-saturation-next-observation-a explanation="如果任务被依赖服务卡住，扩容也可能解决不了问题。"}
::option[统计仓库里的角色数量。]{#service-resource-saturation-next-observation-b explanation="仓库角色无法说明工作单元在等待什么。"}
:::

## 总结

现在，你可以区分资源暂时很忙和任务持续积压。

1. 把忙碌的工作单元数与工作池容量联系起来。
2. 比较队列与请求表现随时间的变化。
3. 调查哪些任务占用了紧张的资源。
