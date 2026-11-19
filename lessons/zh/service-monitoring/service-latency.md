---
lesson_id: "service-latency"
course_id: "service-monitoring"
lang: "zh"
order_index: 4
title: "延迟"
description: "学习把典型请求耗时与较慢的请求放在一起比较。"
meta_title: "延迟 - 服务监控"
meta_description: "读懂请求耗时的中位数和 p95，并选择可比的请求来调查响应变慢的问题。"
meta_keywords: "延迟, 请求耗时, 中位数, p95, 服务监控, Linux Journey"
---

**延迟**指完成请求所用的时间。只看一个数字，可能看不到不同的用户体验。在相同的请求路径和时间窗口内，对比典型请求与较慢的请求。

## 读取小样本

下面五个耗时用毫秒表示。四次请求在 100 毫秒内完成，一次请求用了两秒。

```text
40  50  60  70  2000
```

**中位数**也叫第 50 百分位数，是把样本按大小排序后位于中间的值。这里是 60 毫秒。最慢的一次为 2,000 毫秒。把五次耗时相加再除以 5，可以算出平均值为 444 毫秒。

:::single-choice{#service-latency-sample-median} 在这个已排序的样本里，哪个数值代表中间的那次请求？

::option[444 毫秒。]{#service-latency-sample-median-a explanation="这是平均值，把那次较慢的请求也算了进去。"}
::option[60 毫秒。]{#service-latency-sample-median-b .correct explanation="五个数按顺序排列后，第三个就是中位数。"}
::option[2,000 毫秒。]{#service-latency-sample-median-c explanation="这是观测到的最大值。"}
:::

## 看较慢的那部分请求

**百分位数**可以用来描述一定比例的观测值处在什么范围。第 95 百分位延迟通常写作 p95，代表较大样本中接近较慢一端的阈值。比较时要始终采用相同的计算口径。样本太小，对慢请求一端的估计就容易波动。

:::single-choice{#service-latency-slow-end} 中位数几乎没有变化，但访客仍然反映偶尔很慢。查看什么比较有用？

::option[延迟分布中较慢的一端，以及所统计的请求数。]{#service-latency-slow-end-a .correct explanation="慢的请求可能更慢了，中间位置却没有明显变化。"}
::option[再看一次中位数。]{#service-latency-slow-end-b explanation="只看中位数可能漏掉影响少数访客的变化。"}
::option[日志文件的总大小。]{#service-latency-slow-end-c explanation="文件大小无法说明请求花了多长时间。"}
:::

## 比较相似的请求

应在相似流量下比较同一条请求路径。下载文件比执行一项简短的状态检查慢，很正常。如果某条路径明显变慢，再检查相同时间段内的请求日志和依赖服务。用指标定位问题，再用其他证据查清原因。

:::single-choice{#service-latency-compare-route} 哪个比较最适合检查发布后同一个主页是否变慢？

::option[拿今天的主页响应与上个月的下载请求相比。]{#service-latency-compare-route-a explanation="请求做的工作不同，时段也不同，结果很难解释。"}
::option[每个版本只比较一次请求，忽略请求时间。]{#service-latency-compare-route-b explanation="孤立的单次测量无法反映波动。"}
::option[在发布前后选择可比的时段，比较主页延迟。]{#service-latency-compare-route-c .correct explanation="匹配请求路径和负载，变化更容易解释。"}
:::

## 总结

现在，你可以把典型请求和较慢请求的耗时放在一起看。

1. 在排好序的小样本中找出中位数。
2. 查看较慢的请求时，也留意请求总数。
3. 比较相似的请求，再调查差异。
