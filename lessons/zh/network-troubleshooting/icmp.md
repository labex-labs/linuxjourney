---
title: "ICMP"
description: "了解 ICMP 协议基础知识、消息类型和代码，用于网络故障排除。理解 ICMP 如何工作以调试网络问题。"
keywords: "ICMP, ICMP 协议，网络故障排除，ICMP 类型，Linux 网络，初学者，教程，指南"
---

## Lesson Content

互联网控制消息协议（ICMP）是 TCP/IP 协议套件的一部分。它用于发送更新和错误消息，是一种对调试网络问题（例如数据包传输失败）非常有用的协议。

每个 ICMP 消息都包含类型、代码和校验和字段。类型字段指示 ICMP 消息的类型，代码是提供有关消息更多信息的子类型，校验和用于检测消息完整性方面的任何问题。

让我们看一些常见的 ICMP 类型：

- Type 0 - Echo Reply
- Type 3 - Destination Unreachable
- Type 8 - Echo Request
- Type 11 - Time Exceeded

当数据包无法到达目的地时，会生成一个 Type 3 ICMP 消息。在 Type 3 中，有 16 个代码值进一步描述了为什么无法到达目的地：

- Code 0 - Network Unreachable
- Code 1 - Host Unreachable
  等等...

当我们使用一些网络故障排除工具时，这些消息会更有意义。

## Exercise

本课程没有练习。

## Quiz Question

回显请求的 ICMP 类型是什么？

## Quiz Answer

8
