---
lesson_id: "osi-model"
course_id: "network-basics"
lang: "zh"
order_index: 2
title: "OSI 模型"
description: "学习七层 OSI 参考模型如何组织网络功能和故障排查术语。"
meta_title: "OSI 模型 - 网络基础"
meta_description: "探索网络基础框架 OSI 七层模型。了解这一理论概念如何影响 TCP/IP 模型，以及它在 Linux 网络领域中的重要性。"
meta_keywords: "Linux OSI, OSI 模型, 网络概念, TCP/IP, Linux 网络, 网络层, 理论模型, 七层模型"
---

开放系统互连模型是一个七层参考框架。它为工程师提供共同词汇，用于定位职责、接口和故障；它并不是每种实现的字面描述。

## 七个层次

OSI 各层从低到高依次为：

1. 物理层：信号、介质、连接器和比特传输。
2. 数据链路层：本地帧、链路寻址和介质访问。
3. 网络层：逻辑寻址和网络间转发。
4. 传输层：端点或进程之间的通信。
5. 会话层：管理通信会话。
6. 表示层：数据表示、转换和编码。
7. 应用层：应用程序使用的网络服务。

:::single-choice{#osi-network-layer-number}
OSI 的哪一层处理逻辑寻址和网络间转发？

::option[第 3 层，网络层。]{#osi-layer-three .correct explanation="网络层描述逻辑寻址和网络间转发。"}
::option[第 1 层，物理层。]{#osi-layer-one explanation="物理层关注信号和介质。"}
::option[第 7 层，应用层。]{#osi-layer-seven explanation="应用层描述向网络应用程序公开的服务。"}
:::

## 将模型用作共同词汇

“二层环路”或“四层端口”等说法会指出一个功能领域，但不会解释每个实现细节。实际协议可能跨越边界，加密、隧道、代理或覆盖网络也可能创建多个嵌套层。

:::single-choice{#osi-model-purpose}
在日常故障排查中，OSI 模型最主要的用途是什么？

::option[保证每个协议都恰好有七个标头。]{#osi-seven-headers explanation="实际实现不会一一对应到七个线上标头。"}
::option[用一张图取代所有数据包捕获。]{#osi-replace-captures explanation="模型可以指导调查，但不能替代证据。"}
::option[提供一种对网络功能进行分类的共同方式。]{#osi-shared-vocabulary .correct explanation="该框架帮助团队缩小所讨论的功能范围。"}
:::

## 比较 OSI 与 TCP/IP

互联网协议族与 OSI 参考模型源于不同的标准化历程。实用的 TCP/IP 模型通常将 OSI 的会话层和表示层职责归入应用层，并将物理层和数据链路层相关内容合并为链路层或网络接入层。这些映射只是近似比较，不能证明某个协议栈直接按照另一个模型实现。

:::single-choice{#osi-tcpip-mapping}
应如何理解 OSI 到 TCP/IP 的层次映射？

::option[将其视为每个协议都必须遵守的精确规则。]{#osi-exact-rule explanation="协议职责经常跨越概念边界。"}
::option[将其视为 TCP/IP 在线路上使用七个必需层次的证据。]{#osi-tcp-seven explanation="TCP/IP 通常使用四层或五层模型来讨论。"}
::option[将其视为两个功能模型之间的近似比较。]{#osi-approximate-map .correct explanation="两个模型对某些职责的分组方式不同。"}
:::

## 跨层故障排查

应从症状出发测试假设，而不是机械地按数字顺序检查各层。Web 故障可能涉及本地链路状态、IP 路由、传输层可达性、TLS、名称解析、身份验证或应用程序行为。某一层的证据可以指导下一项测试，但不能证明更高层一定正常。

:::single-choice{#osi-link-success-limit}
正常工作的本地以太网链路能证明什么？

::option[每个远程 HTTP 服务都健康。]{#osi-link-proves-http explanation="本地链路状态无法证明远程应用程序健康。"}
::option[DNS 中没有任何错误记录。]{#osi-link-proves-dns explanation="名称数据与基本链路连接相互独立。"}
::option[只能证明相关的本地链路条件正常。]{#osi-link-limited-proof .correct explanation="路由、传输、命名、安全和应用程序故障仍可能存在。"}
:::

## 总结

现在，你可以把 OSI 模型用作分层诊断词汇。

1. 按顺序说出七个层次。
2. 将每一层与其大致职责关联起来。
3. 将与 TCP/IP 的映射视为近似比较。
4. 使用各层证据指导端到端测试，而不是取代它。
