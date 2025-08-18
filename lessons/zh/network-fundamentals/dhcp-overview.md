---
lang: "zh"
title: "DHCP 概述"
meta_description: "了解 Linux 中的 DHCP（动态主机配置协议）。理解 DHCP 如何分配 IP 地址及其四步过程。开始您的 Linux 网络之旅！"
meta_keywords: "DHCP, 动态主机配置协议，Linux 网络，IP 地址，DHCP 教程，初学者，指南"
---

## Lesson Content

我们之前没有讲过的一个重要网络概念是 DHCP (Dynamic Host Configuration Protocol)。

DHCP 为我们的机器分配 IP 地址、子网掩码和网关。例如，假设你有一部手机，你想获得一个手机号码来开始与人通话。你必须打电话给你的运营商，他们会给你一个号码。只要你支付账单，你就可以继续使用你的手机。DHCP 在这种情况下就是电话运营商；它给你一个 IP 地址，这样你就可以与其他 IP 地址通信。你也会被租用一个 IP 地址；这些地址会持续一段时间，然后根据你的租约设置进行续订。

DHCP 有很多优点：它让网络管理员不必担心分配 IP 地址，也防止他们设置重复的 IP 地址。每个物理网络都应该有自己的 DHCP 服务器，以便主机可以请求 IP 地址。在普通的家庭环境中，路由器通常充当 DHCP 服务器。

DHCP 获取所有动态主机信息的方式是：

1. DHCP DISCOVER - 此消息被广播以搜索 DHCP 服务器。
2. DHCP OFFER - 网络中的 DHCP 服务器回复一个提供消息。该提供消息包含一个数据包，其中包含 DHCP 租约时间、子网掩码、IP 地址等。
3. DHCP REQUEST - 客户端发送另一个广播，告知所有 DHCP 服务器它接受了哪个提供。
4. DHCP ACK - 服务器发送确认。

DHCP 比这更复杂，但这就是它的要点。

## Exercise

本课程没有练习。

## Quiz Question

DHCP 请求的步骤是什么？

## Quiz Answer

DISCOVER, OFFER, REQUEST, ACK
