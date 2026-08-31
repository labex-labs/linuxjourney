---
lesson_id: "traceroute"
course_id: "troubleshooting"
lang: "zh"
order_index: 3
title: "traceroute"
description: "了解 traceroute 如何发现作出响应的跳点，以及如何解读缺口、时延和路径变化。"
meta_title: "traceroute - 故障排除"
meta_description: "掌握 Linux traceroute 命令，用它追踪网络路由并排查连通性问题。本教程解释 traceroute 如何利用 TTL 映射数据包到达目的地的路径。"
meta_keywords: "traceroute, Linux traceroute, Linux 网络, 网络故障排除, TTL, 数据包路由, Linux 命令, 初学者, 教程"
---

`traceroute` 发送 IPv4 TTL 或 IPv6 Hop Limit 逐步递增的探测包。数值耗尽处的路由器可以返回超时消息，从而显示去程路径上部分会响应的节点。

## 跳点发现的工作方式

探测从跳数限制 1 开始逐步增加。第一台路由器将数值从 1 减到 0，并可以返回 ICMP 错误。限制为 2 时，探测会到达第二台路由器后才过期。此过程持续到目的地响应或达到最大值。

:::single-choice{#traceroute-expiring-field}
哪个字段使连续探测包在越来越远的路由器处过期？

::option[目的名称的 DNS 缓存 TTL。]{#traceroute-dns-ttl explanation="DNS 记录生命周期不控制数据包经过的转发跳数。"}
::option[以太网源 MAC 地址。]{#traceroute-source-mac explanation="链路地址不携带端到端跳数计数器。"}
::option[IPv4 TTL 或 IPv6 Hop Limit。]{#traceroute-hop-field .correct explanation="逐步增加这个有界转发计数，就能显示作出响应的路由跳点。"}
:::

## 探测方法

传统 Linux traceroute 通常向较高的目的端口发送 UDP 探测包。目的地可以用 ICMP 端口不可达消息表示探测完成。选项也可改用 ICMP 回显或 TCP SYN 探测，它们穿过过滤规则的效果可能不同：

```bash
$ traceroute -n example.com
$ traceroute -I -n example.com
$ traceroute -T -p 443 -n example.com
```

所需权限和支持的选项因实现而异。只对获准目标采用相应方法，并在比较结果时记录使用的探测方法。

:::single-choice{#traceroute-default-destination-response}
传统 Linux UDP traceroute 通常由什么响应结束？

::option[目的地返回的 ICMP 端口不可达响应。]{#traceroute-port-unreachable .correct explanation="较高的 UDP 端口通常未被使用，因此目的地可以通过该错误表明自己的身份。"}
::option[每台路由器必须返回的 HTTP 200 响应。]{#traceroute-http-every-router explanation="路由器返回网络控制错误，而不是 HTTP 响应。"}
::option[目的地跨互联网发送的以太网广播。]{#traceroute-ethernet-broadcast explanation="链路广播无法跨越路由路径。"}
:::

## 解读星号

星号表示在超时前没有观察到该探测包的响应。路由器可能继续转发过境流量，却过滤诊断响应或限制其速率。如果后续跳点作出响应，那么沉默的跳点显然至少转发了部分探测包。

:::single-choice{#traceroute-asterisk-meaning}
某一跳的 `*` 能证明什么？

::option[该路由器永久丢弃了所有过境数据包。]{#traceroute-star-all-drop explanation="后续响应可以证明转发仍在继续。"}
::option[只能证明探测超时前没有收到匹配的响应。]{#traceroute-star-no-response .correct explanation="过滤、速率限制、丢包和返回路径问题都可能造成沉默。"}
::option[目的地没有 IP 地址。]{#traceroute-star-no-address explanation="探测已经以某个地址为目标，一个沉默跳点并不会让该地址消失。"}
:::

## 时延与路径变化

每跳时间测量的是到控制响应的往返时间，并不是相邻两行之间链路增加的时延。路由器可能降低控制平面响应的优先级；负载均衡可能让各探测包走不同路径；名称解析还可能增加显示延迟，而 `-n` 可以避免反向查询。

每个 ICMP 响应的返回路径也可能与去程路径不同。在认定瓶颈之前，应重复测试，并与端点应用程序的计时互相印证。

:::single-choice{#traceroute-hop-rtt-limit}
为什么不能把相邻跳点的 RTT 相减，当作准确的链路延迟？

::option[traceroute 以字节而不是毫秒报告所有时间。]{#traceroute-times-bytes explanation="显示的探测时间通常以毫秒为单位。"}
::option[响应可能走不同返回路径，并经历不同的控制平面处理。]{#traceroute-rtt-asymmetry .correct explanation="这些测量是彼此独立的源端到各跳点往返时间，而不是同步的单向链路样本。"}
::option[每台路由器的时钟都与源主机相同。]{#traceroute-router-clock explanation="该测量不依赖远端时钟同步。"}
:::

## 与应用程序比较

traceroute 可以到达目的地而服务仍被阻止；服务也可能正常工作，而中间路由器隐藏自己的响应。请测试与应用程序相同的地址族、目的地、传输协议和端口，再把 traceroute 作为辅助路径证据。

:::single-choice{#traceroute-service-proof}
一次完成的 traceroute 能证明 HTTPS 服务健康吗？

::option[能，因为每一跳都会验证服务器证书。]{#traceroute-validates-cert explanation="路由器不会执行客户端的 TLS 验证。"}
::option[不能；传输、TLS 和 HTTP 行为需要各自测试。]{#traceroute-not-app-proof .correct explanation="路径发现与应用程序健康属于不同诊断层级。"}
::option[能，但前提是打印出反向 DNS 名称。]{#traceroute-rdns-proof explanation="名称不能证明应用程序正常工作。"}
:::

## 总结

现在，你可以把 traceroute 解读为一系列跳数有界的探测，而不是无所不知的完整路径工具。

1. 解释如何通过 TTL 或 Hop Limit 过期发现跳点。
2. 记录使用的是 UDP、ICMP 还是 TCP 探测。
3. 把星号视为响应缺失，而不是已经证实的中断。
4. 不要从相邻跳点的 RTT 推导准确链路延迟。
5. 将路径证据与实际应用程序相互印证。
