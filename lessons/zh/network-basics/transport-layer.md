---
lesson_id: "transport-layer"
course_id: "network-basics"
lang: "zh"
order_index: 6
title: "传输层"
description: "学习 TCP 和 UDP 如何使用端口，并在应用程序端点之间提供不同的传送语义。"
meta_title: "传输层 - 网络基础"
meta_description: "探索 Linux 网络中的传输层。本课介绍 TCP 和 UDP 等关键协议、网络端口的作用、数据分段，以及用于可靠数据传输的 TCP 握手。"
meta_keywords: "Linux 传输层, TCP, UDP, TCP 握手, 网络端口, 数据分段, Linux 网络, 网络协议, 可靠数据传输"
---

传输层通过 IP 网络连接应用程序端点。TCP 和 UDP 都使用 16 位端口号，但向应用程序公开的通信模型和保证不同。

## 端口与套接字

目标端口帮助操作系统把流量送达监听套接字。标识连接或流量不能只靠一个端口：协议、源地址与目标地址、源端口与目标端口都很重要。因此，同一个服务器端口可以同时服务许多客户端。

:::single-choice{#transport-layer-many-clients} 一个 TCP 服务器端口如何同时处理多个客户端？

::option[每个连接具有不同的端点地址与端口组合。]{#transport-layer-connection-tuple .correct explanation="完整的传输层元组可以区分共享同一监听端口的并发连接。"}
::option[服务器会在每个数据包之后永久重命名端口。]{#transport-layer-renames-port explanation="监听端口可以保持不变，而已接受连接具有不同的对端元组。"}
::option[IP 会在传送前删除所有源地址。]{#transport-layer-removes-source explanation="源地址是标识对端和路径的一部分。"}
:::

## TCP 字节流

只要连接仍然可用，TCP 就会提供有序、可靠的字节流。它使用序列号、确认、重传、流量控制和拥塞控制。TCP 不保留应用程序消息边界：一次写入可能通过多次读取到达，多次写入也可能由一次读取返回。应用程序必须自行定义成帧方式。

可靠并不等于绝对送达。连接可能超时、重置或失败，收到确认也不能证明应用程序已将数据持久提交。

:::single-choice{#transport-layer-tcp-boundaries} TCP 如何处理应用程序消息边界？

::option[TCP 提供有序字节流，但不保留写入边界。]{#transport-layer-byte-stream .correct explanation="应用层协议必须定义消息的分隔或长度。"}
::option[每次写入都会恰好变成一个 IP 数据包和一次读取。]{#transport-layer-one-write-packet explanation="分段、缓冲和接收 API 不会保留这种对应关系。"}
::option[TCP 将每条消息转换成 DNS 记录。]{#transport-layer-tcp-dns explanation="DNS 是独立的应用层协议。"}
:::

## TCP 握手

正常 TCP 连接以三次握手开始：

1. 发起方发送带有初始序列信息的 `SYN`。
2. 监听方回复 `SYN-ACK`，带上自己的序列信息和确认。
3. 发起方返回 `ACK`。

该过程在两个端点中建立传输状态。它不会验证应用服务器的身份，也不能证明所请求的应用操作会成功。

:::single-choice{#transport-layer-handshake-order} 正常的 TCP 三次握手顺序是什么？

::option[SYN、SYN-ACK、ACK。]{#transport-layer-syn-order .correct explanation="这次交换会在两个方向同步并确认初始连接状态。"}
::option[ACK、ACK、SYN。]{#transport-layer-ack-ack-syn explanation="发起方首先请求同步。"}
::option[SYN、FIN、RST。]{#transport-layer-syn-fin-rst explanation="FIN 和 RST 用于关闭或中止状态，而不是完成正常握手。"}
:::

## UDP 数据报

UDP 保留数据报边界，并提供基于校验和的错误检测，但不提供 TCP 式连接状态、排序、重传、流量控制或拥塞控制。应用程序可以自行添加所需的可靠性或拥塞行为。UDP 并不必然更快；性能取决于协议设计、工作负载、路径和实现。

:::single-choice{#transport-layer-udp-boundaries} UDP 向应用程序提供哪项属性？

::option[自动重传的有序字节流。]{#transport-layer-udp-stream explanation="这描述的是类似 TCP 的服务，而不是基础 UDP。"}
::option[保留所提交数据报之间的边界。]{#transport-layer-udp-datagrams .correct explanation="除非丢失，否则收到的一个 UDP 数据报对应发送的一个数据报。"}
::option[保证在固定期限前送达。]{#transport-layer-udp-deadline explanation="UDP 不提供传送期限保证。"}
:::

## 检查传输端点

使用 `ss` 以只读方式检查监听和已连接套接字：

```bash
$ ss -lntup
$ ss -tn state established
```

查看进程详情可能需要特权。监听套接字只能证明传输边界上的本地就绪状态；防火墙、路由、地址族、TLS 和应用程序健康仍需通过适当测试确认。

:::single-choice{#transport-layer-listener-proof} 监听中的 TCP 套接字能确定什么？

::option[每个远程防火墙都允许连接。]{#transport-layer-all-firewalls explanation="本地套接字状态无法反映整条路径上的所有策略。"}
::option[应用程序已通过每项健康检查。]{#transport-layer-all-health explanation="监听状态提供的证据弱于成功完成一次应用程序事务。"}
::option[本地进程已准备好接受匹配的 TCP 连接。]{#transport-layer-local-listener .correct explanation="远程可达性和正确应用响应仍是独立问题。"}
:::

## 总结

现在，你可以区分 TCP 字节流行为与 UDP 数据报行为。

1. 使用协议、地址和端口标识一个流。
2. 将 TCP 视为不保留消息边界的可靠有序字节流。
3. 认识 TCP 握手能够和不能证明的内容。
4. 将 UDP 的可靠性与拥塞行为视为应用程序设计选择。
5. 在本地套接字状态之外验证应用程序健康。
