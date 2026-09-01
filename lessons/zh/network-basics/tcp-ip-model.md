---
lesson_id: "tcp-ip-model"
course_id: "network-basics"
lang: "zh"
order_index: 3
title: "TCP/IP 模型"
description: "学习 TCP/IP 模型中的应用层、传输层、网际层和链路层如何协同工作。"
meta_title: "TCP/IP 模型 - 网络基础"
meta_description: "探索现代网络基础 TCP/IP 模型中的各个层次。了解应用层、传输层、网络层和链路层，以便有效使用 TCP/IP 进行联网。"
meta_keywords: "TCP/IP 模型, TCP/IP 模型层次, TCP/IP 网络, TCP 协议层次, 网络层次, TCP, IP, Linux 网络, 实际协议项目"
---

TCP/IP 模型将互联网主机使用的协议划分为不同功能层。常见的四层形式包括应用层、传输层、网际层和链路层。有些教学模型会将物理介质与链路层分开，因此呈现五层。

## 应用层

应用层协议为 HTTP、DNS、SSH 和 SMTP 等服务定义消息与行为。该层还包含许多在 OSI 模型中单独讨论的表示层和会话层职责。

:::single-choice{#tcpip-http-layer} HTTP 通常归入 TCP/IP 的哪一层？

::option[网际层。]{#tcpip-http-internet explanation="网际层处理 IP 寻址和数据包转发。"}
::option[链路层。]{#tcpip-http-link explanation="链路层在本地介质上传输流量。"}
::option[应用层。]{#tcpip-http-application .correct explanation="HTTP 定义应用程序请求和响应语义。"}
:::

## 传输层

传输层协议提供应用程序端点之间的通信。TCP 提供具有拥塞控制和流量控制的可靠有序字节流。UDP 提供独立数据报，不具备 TCP 的连接、排序或重传保证。端口号有助于标识传输端点，但仅凭端口号不能证明哪个应用程序正在监听。

:::single-choice{#tcpip-udp-property} 哪项属性属于 UDP 而不是 TCP？

::option[独立数据报，且没有内置重传保证。]{#tcpip-udp-datagrams .correct explanation="使用 UDP 的应用程序自行决定是否以及如何增加可靠性。"}
::option[保证一个字节流按顺序送达。]{#tcpip-udp-ordered explanation="这是 TCP 的服务属性，前提是连接成功。"}
::option[在不同 IP 网络之间路由数据包。]{#tcpip-udp-routing explanation="网络间路由属于网际层功能。"}
:::

## 网际层

互联网协议使用源 IP 地址和目标 IP 地址承载数据包。路由器在向目标转发数据包时检查路由信息并递减跳数限制。ICMP 为 IP 操作传递控制和错误信息。传送仍然是尽力而为；所需的恢复由更高层或应用程序处理。

:::single-choice{#tcpip-router-layer} 哪一层提供路由器使用的 IP 目标地址？

::option[网际层。]{#tcpip-router-internet .correct explanation="IP 标头包含用于路由转发的网络层目标。"}
::option[应用层。]{#tcpip-router-application explanation="应用程序消息承载在较低层协议数据中。"}
::option[链路层。]{#tcpip-router-link explanation="链路地址选择下一条本地跳点帧的目标。"}
:::

## 链路层与封装

链路层使用以太网、Wi-Fi、点对点协议或其他技术，在一条本地链路上传送 IP 数据包。应用程序数据向下移动时，每一层都会添加其作用范围所需的信息。在接收端，各层验证并移除自己的封装，再将数据向上传递。

链路标头通常会在每个路由跳点改变；除非中间设备终止或转换通信，否则传输层和应用层会话是端到端的。

:::single-choice{#tcpip-link-scope} 链路层帧的正常作用范围是什么？

::option[一条本地链路或一跳。]{#tcpip-one-link .correct explanation="路由器移除传入帧，并为下一条链路创建新帧。"}
::option[全球互联网上的每个应用程序会话。]{#tcpip-global-frame explanation="帧不会原封不动地跨越经过路由的网络。"}
::option[仅限源进程的内存。]{#tcpip-process-memory explanation="帧会通过网络链路传输。"}
:::

## 总结

现在，你可以将常见互联网功能放到 TCP/IP 模型的对应层次。

1. 将服务协议与应用层相关联。
2. 区分 TCP 字节流与 UDP 数据报。
3. 将 IP 寻址和路由归入网际层。
4. 将链路帧视为本地跳点的封装。
