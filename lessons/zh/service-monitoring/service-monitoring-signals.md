---
lesson_id: "service-monitoring-signals"
course_id: "service-monitoring"
lang: "zh"
order_index: 1
title: "监控信号"
description: "学习怎样为 Web 服务的问题选择合适的监控信号。"
meta_title: "监控信号 - 服务监控"
meta_description: "从用户症状出发，区分可用性、延迟、流量、错误和资源饱和度。"
meta_keywords: "监控信号, 可用性, 延迟, 流量, 饱和度, 服务监控, Linux Journey"
---

访客说页面打开得慢。先弄清访客遇到了什么，再挑一项能描述这种情况的测量结果。**信号**是观测到的信息，例如计数、测量值或保存下来的事件。

## 查看用户体验

**可用性**描述服务能否完成预期的工作。例如，可以请求主页，看它是否成功响应。**延迟**是请求花费的时间。页面可以正常打开，但仍可能要等几秒。

:::single-choice{#service-monitoring-signals-slow-page} 访客收到了网页，但等了几秒。哪个信号最直接地反映这一症状？

::option[服务器上的容器数量。]{#service-monitoring-signals-slow-page-b explanation="容器数无法衡量访客等了多久。"}
::option[收到网页用了多长时间。]{#service-monitoring-signals-slow-page-a .correct explanation="延迟衡量请求用了多久。"}
::option[源代码仓库的字节数。]{#service-monitoring-signals-slow-page-c explanation="仓库大小无法说明请求耗时。"}
:::

## 统计请求和错误

**流量**是服务收到的请求量，例如每分钟处理多少个请求。记录失败请求数时，也要记录请求总数。同样是五个错误，发生在一千次请求里和十次请求里，影响很不一样。

:::single-choice{#service-monitoring-signals-count-context} 两个时间段各有五次失败。什么信息有助于比较对用户的影响？

::option[各时段的请求总数。]{#service-monitoring-signals-count-context-b .correct explanation="要比较错误率，两个失败次数分别需要对应的分母。"}
::option[仪表板的名称。]{#service-monitoring-signals-count-context-a explanation="名称可以告诉你图表在哪里，不能衡量流量。"}
::option[服务在列表中的顺序。]{#service-monitoring-signals-count-context-c explanation="列表顺序无法衡量受影响的请求数量。"}
:::

## 检查资源压力

**饱和度**描述资源有多接近容量上限。即使 Web 进程仍在运行，一些请求也可能正在等数据库处理。下结论前，应把用户看到的情况与资源信号对照起来。

:::single-choice{#service-monitoring-signals-saturation-check} 请求变慢的同时，积压也在增长。合理的下一步是什么？

::option[认定积压就是根本原因。]{#service-monitoring-signals-saturation-check-a explanation="两项变化提供了有用的线索，因果关系还需更多证据。"}
::option[重新数一遍主机上保存的镜像。]{#service-monitoring-signals-saturation-check-b explanation="镜像是否存在，无法解释为什么有请求排队。"}
::option[检查负责处理积压任务的资源。]{#service-monitoring-signals-saturation-check-c .correct explanation="查看这个资源，有助于判断它是否来不及处理收到的任务。"}
:::

## 总结

现在，你可以根据用户碰到的现象，选择合适的监控信号。

1. 区分可用性和延迟。
2. 结合请求总量解读失败次数。
3. 通过饱和度调查容量问题。
