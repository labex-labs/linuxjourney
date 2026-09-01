---
lesson_id: "application-layer"
course_id: "network-basics"
lang: "zh"
order_index: 5
title: "应用层"
description: "学习应用层协议如何定义服务消息、状态、命名和安全行为。"
meta_title: "应用层 - 网络基础"
meta_description: "探索 TCP/IP 模型的最高层——应用层。了解什么是应用层协议，通过 SMTP 示例理解应用层标头如何为网络通信准备数据。"
meta_keywords: "应用层, TCP/IP 应用层, 应用层协议, 应用层协议示例, 应用层标头, TCP/IP 模型, SMTP, 网络协议"
---

TCP/IP 应用层包含应用程序用来请求和提供网络服务的协议。它涵盖 OSI 术语中分别归入应用层、表示层和会话层的许多功能。

## 协议消息与语义

应用层协议定义对等方如何解读消息和状态。HTTP 定义请求、响应、方法、状态码和字段；DNS 定义查询和资源记录；SMTP 定义邮件传输所用的命令和回复。

并非每种应用层协议都会添加一个固定的“应用层标头”。有些使用文本字段，有些使用二进制记录，有些包含多层嵌套格式，还有些在一个传输连接上承载连续的消息序列。

:::single-choice{#application-layer-protocol-role} 应用层协议主要定义什么？

::option[服务消息的含义和交换规则。]{#application-layer-message-semantics .correct explanation="对等方需要共享语法、语义和状态行为才能互操作。"}
::option[每根以太网电缆上的电压。]{#application-layer-voltage explanation="物理信号属于较低层技术。"}
::option[每台互联网路由器独立选择的路由。]{#application-layer-router-choice explanation="路由决策属于网络层行为。"}
:::

## 客户端、服务器与对等方

客户端向服务发起请求或连接；服务器监听或以其他方式接受请求。这些是一次交互中的角色，而不是永久的设备类别。同一台主机可以同时作为 DNS 客户端和 SSH 服务器，有些协议还采用点对点角色。

:::single-choice{#application-layer-client-role} 在典型的请求-响应交换中，什么使程序成为客户端？

::option[它向服务发起请求。]{#application-layer-client-initiates .correct explanation="客户端与服务器描述交互角色，同一台主机可同时为不同服务承担不同角色。"}
::option[它必须运行在笔记本电脑而不是服务器上。]{#application-layer-client-laptop explanation="硬件类别不决定协议角色。"}
::option[它拥有目标 IP 前缀。]{#application-layer-client-prefix explanation="网络所有权与发起应用程序请求无关。"}
:::

## 名称、端口与服务选择

应用程序可以将服务名称解析为一个或多个 IP 地址，并选择传输端点。知名端口提供默认约定，并不能成为协议的固定证明。HTTP 通常使用 TCP 端口 80，HTTPS 通常使用 TCP 端口 443，但两者都可以运行在其他端口。SMTP 的邮件中继和邮件提交会使用不同端口与策略。

:::single-choice{#application-layer-port-limit} 仅凭 TCP 端口 443 开放能证明什么？

::option[有进程在此接受 TCP 端点，但其应用行为仍需测试。]{#application-layer-port-endpoint .correct explanation="协议交换和 TLS 验证能提供更可靠的应用层证据。"}
::option[该服务肯定是配置正确的 HTTPS 应用程序。]{#application-layer-port-proves-https explanation="端口号不能验证协议行为、身份或健康状况。"}
::option[DNS 无法返回 IPv6 地址。]{#application-layer-port-dns explanation="传输端口不会限制 DNS 记录的地址族。"}
:::

## 安全与端到端测试

在证书验证和端点命名正确时，TLS 可以提供机密性、完整性和经过身份验证的对端身份。它不会自动授权每项应用程序操作。测试时应使用与真实客户端相同的名称、地址族、端口、协议、凭据和请求。

例如，诊断 HTTPS 时可以分别检查名称解析、TCP 连接、TLS 证书和名称、HTTP 响应以及应用程序内容。某一步成功可以缩小问题范围，但不能证明后续所有步骤都成功。

:::single-choice{#application-layer-tls-limit} TLS 证书验证成功能确定什么？

::option[每个用户都有权访问每项资源。]{#application-layer-tls-all-users explanation="传输身份验证不能取代应用程序访问策略。"}
::option[经过验证名称的对端身份，以及一条经过身份验证的安全通道。]{#application-layer-tls-identity .correct explanation="应用程序授权和内容正确性仍需各自检查。"}
::option[任何路由器以后都不可能丢弃数据包。]{#application-layer-tls-routing explanation="TLS 无法保证未来的网络传送。"}
:::

## 总结

现在，你可以超越端口号或程序名称来描述应用层行为。

1. 将协议语法、语义和状态识别为应用层问题。
2. 将客户端和服务器视为一次交换中的角色。
3. 将端口视为端点约定，而不是协议证明。
4. 对命名、安全和应用程序响应进行端到端测试。
