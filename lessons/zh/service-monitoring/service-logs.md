---
lesson_id: "service-logs"
course_id: "service-monitoring"
lang: "zh"
order_index: 2
title: "服务日志"
description: "学习用请求 ID 和时间在不同服务的日志中追踪同一次请求。"
meta_title: "服务日志 - 服务监控"
meta_description: "用请求 ID 关联多条服务日志，筛选同一次请求的记录，并准确描述发现的问题。"
meta_keywords: "服务日志, 请求 ID, 日志筛选, 依赖服务, 服务监控, Linux Journey"
---

用户遇到了错误。服务日志能告诉你，这次请求在处理过程中是哪一步失败了。先确定时间，再找**请求 ID**，也就是传给同一次请求所产生日志的标识。

## 追踪一次请求

下面的示例涉及两个服务。**依赖服务**是另一个程序完成工作时需要调用的服务。这里，Web 服务要向目录服务请求一份项目清单。

```text
09:14:02 service=web     request=r17 path=/items status=502
09:14:02 service=catalog request=r17 action=read result=timeout
09:14:03 service=catalog request=r18 action=read result=ok
```

Web 服务的记录显示 `r17` 响应失败。目录服务中相同 ID 的记录显示请求超时。旁边那条成功的目录请求属于 `r18`。

:::single-choice{#service-logs-matching-request} 目录服务的哪个结果对应 Web 服务中失败的 r17？

::option[r18 的成功结果。]{#service-logs-matching-request-a explanation="那一行属于另一条请求。"}
::option[目录服务的两条结果。]{#service-logs-matching-request-c explanation="时间接近的记录仍可能属于不同请求。"}
::option[r17 的超时结果。]{#service-logs-matching-request-b .correct explanation="共同的 ID 把这次请求的两条记录关联起来。"}
:::

## 筛选示例日志

把上面三行保存为练习目录中的 `requests.log`。用 `grep -F` 按原样查找指定文本。在标识后面保留空格，这样就能匹配这个示例里字段的结束位置。

```bash
$ grep -F 'request=r17 ' requests.log
```

预期会看到 Web 和目录服务中对应 `r17` 的两行。实际日志格式可能不同，也可能没有请求 ID。使用字段关联服务之前，要确认这些字段在各个服务里的含义一致。

:::single-choice{#service-logs-choose-filter} 为什么要匹配整个请求字段，而不只搜索 timeout？

::option[这样能确保所有流量都出现了同样的错误。]{#service-logs-choose-filter-b explanation="这个筛选只找出某一次请求的记录。"}
::option[即使只有一行包含 timeout，也能找到 Web 和目录服务中对应的两条记录。]{#service-logs-choose-filter-a .correct explanation="两个服务共用同一个 ID，可以用它追踪整条请求。"}
::option[这样会修改日志，让之后的搜索得到正确结果。]{#service-logs-choose-filter-c explanation="grep 读取文件并打印匹配行。"}
:::

![grep 输出用请求 ID r17 关联了 Web 错误和目录服务超时](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/service-monitoring/service-logs/request-id.png)

## 明确报告的范围

超时指出这次请求在哪个环节出了问题，却不能说明目录服务内部究竟哪个组件速度变慢了。接下来可以检查依赖服务自己的指标或近期日志。把日志片段交给同事时，保留请求 ID，并删去对方不需要的机密信息或个人数据。

:::single-choice{#service-logs-evidence-limit} 第一份报告里应该怎么说？

::option[请求 r17 在目录服务处超时，需要进一步检查。]{#service-logs-evidence-limit-c .correct explanation="这概括了相互匹配的记录，没有猜测背后的原因。"}
::option[目录服务的所有请求都超时了。]{#service-logs-evidence-limit-a explanation="示例还包括另一条成功的目录服务请求。"}
::option[数据库中的某块磁盘故障了。]{#service-logs-evidence-limit-b explanation="这些记录没有包含任何磁盘观测结果。"}
:::

想在 Linux 主机上练习查询服务记录，可参考 [分析日志以响应事件](https://labex.io/labs/linux-monitoring-and-incident-response-log-analysis-594586)。

## 总结

现在，你可以顺着一次请求查阅多个服务的日志。

1. 在相关记录中匹配请求 ID。
2. 用字面文本筛选日志样本。
3. 说明日志支持的结论，并找出下一个要核查的问题。
