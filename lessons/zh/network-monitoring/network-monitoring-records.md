---
lesson_id: "network-monitoring-records"
course_id: "network-monitoring"
lang: "zh"
order_index: 1
title: "网络记录"
description: "学习针对具体的监测问题，选择能够提供相关证据的网络记录。"
meta_title: "网络记录 - 网络监测"
meta_description: "区分网络流、DNS 日志与抓包数据，理解不同观测位置能看到什么。"
meta_keywords: "网络记录, 流量汇总, DNS 日志, 抓包, 网络监测, Linux Journey"
---

网络观测结果描述的是某个工具从一个位置看到了什么。先明确你想弄清的问题。即使是同一次活动，不同的数据来源也会显示不同的部分。

## 选择记录类型

**流记录**汇总网络端点之间的通信。**DNS 日志**报告解析器看到的名称查询。**数据包捕获**会保存从抓包位置看到的单个数据包的副本。端点是通信的一方，通常可用地址和端口识别。

:::single-choice{#network-monitoring-records-choose-dns} 你想知道解析器对 site.example 返回了哪个应答。应该查看哪个来源？

::option[运行中的 Web 工作进程数量。]{#network-monitoring-records-choose-dns-b explanation="工作进程的数量与这次查询无关。"}
::option[该解析器的 DNS 日志。]{#network-monitoring-records-choose-dns-a .correct explanation="解析器可以记录自己处理的查询和应答。"}
::option[只记录流量大小的汇总。]{#network-monitoring-records-choose-dns-c explanation="流量汇总可能没有 DNS 查询和应答。"}
:::

## 找到观测位置

在笔记本电脑上抓包，只能记录选定接口可见的数据包。服务器日志记录到达服务器的事件，或者服务器自身记下的信息。例如，用户请求可能在到达服务器之前就失败。应选择观测位置与问题相符的数据来源。

:::single-choice{#network-monitoring-records-capture-scope} 在另一台电脑抓到的数据里找不到请求。下结论之前应该检查什么？

::option[抓包接口是否覆盖相关的路径和时间。]{#network-monitoring-records-capture-scope-b .correct explanation="没有抓到数据包，可能是因为该观测位置看不到它。"}
::option[抓包文件中是否有其他无关的数据包。]{#network-monitoring-records-capture-scope-a explanation="有无关流量说明抓包确实发生了，但无法说明相关路径和时段是否可见。"}
::option[是否还有另一台主机同时抓包。]{#network-monitoring-records-capture-scope-c explanation="另一台主机同时抓包，无法说明当前接口能看到什么。"}
:::

## 缩小样本范围

抓包文件可能包含人们不打算分享的内容。学习读包时，可以使用事先准备的、只包含无害练习流量的抓包文件。如果要分享简短片段，把查看时的时间信息和过滤条件也一起给出，方便他人理解其覆盖范围。

:::single-choice{#network-monitoring-records-choosing-evidence} 哪种样本最适合用来学习如何识别 DNS 响应？

::option[一份很长的文件，里面都是无关的员工流量。]{#network-monitoring-records-choosing-evidence-a explanation="这会加入不必要的数据，还可能暴露隐私。"}
::option[一份没有查询相关字段的汇总。]{#network-monitoring-records-choosing-evidence-b explanation="这样学员就没有可以解读的证据。"}
::option[一份小型练习抓包，包含本次查询和应答。]{#network-monitoring-records-choosing-evidence-c .correct explanation="它正好提供了回答问题所需的一次通信。"}
:::

## 总结

现在，你可以选择合适的网络记录，并解释它能观测到什么。

1. 区分流量汇总、DNS 日志和抓包数据。
2. 根据网络路径选择相应的观测位置。
3. 选用精简而合适的样本来核查。
