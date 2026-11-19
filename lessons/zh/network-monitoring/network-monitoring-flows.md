---
lesson_id: "network-monitoring-flows"
course_id: "network-monitoring"
lang: "zh"
order_index: 2
title: "网络流"
description: "学习读懂流量汇总中的地址、端口、时间和字节数。"
meta_title: "网络流 - 网络监测"
meta_description: "根据流记录判断流量方向与大小，并了解还需要哪些记录才能确认应用层的结果。"
meta_keywords: "网络流, 流记录, TCP 端口, 字节数, 网络监测, Linux Journey"
---

**网络流**把网络地址、端口、协议等属性相同的流量归在一起。监测系统可以统计一个流中的字节数或数据包数，不必记录完整内容。

## 读取两端的地址

在这份模拟汇总中，采集器记录了从来源到目标的方向。TCP 等传输层协议使用端口号，可以据此识别接收一侧的监听服务。

```text
start=09:21:00Z protocol=TCP src=192.0.2.10:51600 dst=192.0.2.20:443 bytes=1800
start=09:21:00Z protocol=TCP src=192.0.2.20:443 dst=192.0.2.10:51600 bytes=8200
```

第一行流量发往 443 端口。第二行记录相反的方向。有些采集器会把两个方向合并在一起，因此要先核对当前记录的格式。

:::single-choice{#network-monitoring-flows-endpoint-direction} 在第一行里，哪个地址和端口接收了记录中的流量？

::option[192.0.2.10:51600。]{#network-monitoring-flows-endpoint-direction-a explanation="它是第一个方向的发送端点。"}
::option[列表中的两个端点都属于目标。]{#network-monitoring-flows-endpoint-direction-c explanation="这个示例里，每行只记录一个方向。"}
::option[192.0.2.20:443。]{#network-monitoring-flows-endpoint-direction-b .correct explanation="目标字段给出流量发送到的位置。"}
:::

## 比较统计量

示例中，从 443 端口发出的字节更多。网页响应比较大可能是正常的。仅凭字节数无法知道页面内容、涉及的账户，或流量大小背后的原因。

:::single-choice{#network-monitoring-flows-byte-count} 第二行的 8,200 字节描述了什么？

::option[响应消息的具体文本。]{#network-monitoring-flows-byte-count-b explanation="流量汇总只记录大小，没有保存消息内容。"}
::option[记录到的这个方向的流量大小。]{#network-monitoring-flows-byte-count-a .correct explanation="字节数汇总流量大小，来源和目标用来判断方向。"}
::option[足以保证页面加载成功的信息。]{#network-monitoring-flows-byte-count-c explanation="流量大小无法说明 HTTP 请求的结果。"}
:::

## 补充上下文

结合已知的服务信息和时间，判断哪些流与问题有关。如果要知道 Web 服务器实际返回的内容，可以在资料允许的情况下，与同一时间和同一连接的访问日志对照。

:::single-choice{#network-monitoring-flows-next-source} 你想知道该 Web 请求的 HTTP 状态码。哪个额外的数据来源有用？

::option[对应的 Web 访问记录。]{#network-monitoring-flows-next-source-c .correct explanation="服务器的访问记录可以报告 HTTP 请求的结果。"}
::option[把流中的字节数四舍五入到最接近的百位。]{#network-monitoring-flows-next-source-a explanation="取整只改变数值精度，无法增加响应状态。"}
::option[同一对端点的第二份流量汇总。]{#network-monitoring-flows-next-source-b explanation="流量汇总可以提供更多网络观测。通常不会给出 HTTP 响应状态。"}
:::

## 总结

现在，你可以读懂一条流量汇总记录中的主要字段。

1. 找出端点地址和端口。
2. 按记录的方向解读字节数。
3. 需要应用层结果时，选择其他数据来源。
