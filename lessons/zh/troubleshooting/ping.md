---
lesson_id: "ping"
course_id: "troubleshooting"
lang: "zh"
order_index: 2
title: "ping"
description: "了解如何运行有界的 ping 测试，以及如何解读应答、丢包、RTT、TTL 和局限性。"
meta_title: "ping - 故障排除"
meta_description: "学习使用 Linux ping 命令测试网络连通性。本指南解释 ping 输出，包括 icmp_seq、TTL 和往返时间的含义，并介绍如何解读 ping 序列以诊断网络问题。"
meta_keywords: "Linux ping, 网络连通性, ICMP, TTL, ping 命令, icmp_seq, ping 序列, ICMP 序列, icmp_seq 含义, ping icmp_seq, Linux 网络"
---

`ping` 发送 ICMP 回显请求并报告观察到的应答。它测试到某个地址的一条控制消息路径，并不能证明 TCP、UDP、DNS、身份认证或应用程序正常工作。

## 运行有界测试

在常见 iputils 实现中，发送三次 IPv4 请求，并为每个数据包设置两秒超时：

```bash
$ ping -4 -c 3 -W 2 example.com
```

使用 `-6` 选择 IPv6。请记录解析出的地址，因为一个主机名可以返回多个地址，而重复运行时可能选择不同地址。

:::single-choice{#ping-count-option}
`-c 3` 要求什么？

::option[数据包载荷恰好为三兆字节。]{#ping-three-megabytes explanation="数据包大小使用另一个选项。"}
::option[到目的地的三条永久路由。]{#ping-three-routes explanation="ping 探测流量，并不会安装路由。"}
::option[发送三次回显请求后命令正常停止。]{#ping-three-requests .correct explanation="有限次数可使诊断有界且能够复现。"}
:::

## 序列与丢包

`icmp_seq` 标识本次运行中的各次请求。缺失的应答会计入观察到的丢包，而乱序应答可能反映时延变化。小样本的噪声很大；应比较多个有界时间段，并结合应用程序自身的错误率。

丢包可能发生在任一方向，ICMP 速率限制也可能让 ping 丢包率与应用程序丢包率不同。

:::single-choice{#ping-sequence-gap}
缺少某个 `icmp_seq` 应答可能表示什么？

::option[目的地永久更改了 MAC 地址。]{#ping-sequence-mac explanation="单凭序列缺口无法得出这种链路层结论。"}
::option[请求或应答丢失、被过滤、延迟超过等待时间或受到速率限制。]{#ping-sequence-possibilities .correct explanation="序列缺口只表明没有观察到应答，无法确定具体方向或原因。"}
::option[源磁盘没有空闲 inode。]{#ping-sequence-inodes explanation="文件系统 inode 状态与 ICMP 序列应答无关。"}
:::

## 往返时间

`time` 字段是从发送请求到收到应答的往返时间，单位为毫秒。它包含去程时延、远端处理时间和返程时延。没有同步的端点测量，就无法用它得知单向延迟。

:::single-choice{#ping-rtt-meaning}
报告的 `time=23.7 ms` 测量了什么？

::option[只有去程路径的单向延迟。]{#ping-outbound-only explanation="ping 测量完整的请求与应答间隔。"}
::option[目标系统的运行时间。]{#ping-target-uptime explanation="该值是探测计时，而不是开机时长。"}
::option[这次回显的往返时间。]{#ping-round-trip .correct explanation="它包含两个方向和端点处理时间。"}
:::

## TTL 或 Hop Limit

显示的 IPv4 TTL 或 IPv6 Hop Limit 是收到应答时的剩余值。如果不知道发送方的初始值和返回路由，就不能通过减法得到准确跳数。数值变化可能表示响应方、初始值或返回路径发生变化。

:::single-choice{#ping-received-ttl}
IPv4 回显应答中显示的 TTL 是什么？

::option[应答到达本地主机时的剩余值。]{#ping-remaining-ttl .correct explanation="返回路径上的每台路由器都递减了发送方的初始值。"}
::option[两个方向经过的路由器准确总数。]{#ping-exact-hop-count explanation="仅凭该字段无法确定初始 TTL 和各方向路径。"}
::option[DNS 记录的缓存生命周期。]{#ping-dns-ttl explanation="DNS TTL 与 IP 数据包 TTL 是不同字段。"}
:::

## 测试正确的层级

如果 ping 成功但服务失败，应测试实际端口、TLS、协议和请求。如果 ping 失败，应先检查名称解析、`ip route get`、邻居状态、防火墙策略和抓包，再断言主机已停机。

:::single-choice{#ping-success-limit}
ping 成功无法证明什么？

::option[某条 ICMP 请求与应答路径正常。]{#ping-icmp-worked explanation="应答直接提供了这一证据。"}
::option[应答中包含序列号。]{#ping-sequence-present explanation="正常输出会直接报告应答序列。"}
::option[目标应用程序会接受并完成请求。]{#ping-app-not-proven .correct explanation="应用程序和传输行为需要适合该应用的测试。"}
:::

## 总结

现在，你可以把 ping 用作一项有明确边界的 ICMP 测量。

1. 选择地址族并记录解析出的地址。
2. 限制次数和等待时间，以便重复测试。
3. 解读丢包时不要假定方向或原因。
4. 把 RTT 视为双向时间，把 TTL 视为剩余值。
5. 单独测试实际应用程序。
