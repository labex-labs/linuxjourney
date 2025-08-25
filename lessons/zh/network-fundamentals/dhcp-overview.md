---
index: 9
lang: "zh"
title: "DHCP 概述"
meta_title: "DHCP 概述 - 网络基础"
meta_description: "了解 Linux 中的 DHCP (动态主机配置协议)。理解 DHCP 如何分配 IP 地址及其四步过程。开始您的 Linux 网络之旅！"
meta_keywords: "DHCP, 动态主机配置协议，Linux 网络，IP 地址，DHCP 教程，初学者，指南"
---

## Lesson Content

我们还没有讲到的一个重要网络概念是 DHCP (Dynamic Host Configuration Protocol)。

DHCP 为我们的机器分配 IP 地址、子网掩码和网关。例如，假设你有一部手机，你想获得一个手机号码来开始与人通话。你必须打电话给你的运营商，他们会给你一个号码。只要你支付账单，你就可以继续使用你的手机。在这种情况下，DHCP 就是电话运营商；它给你一个 IP 地址，这样你就可以与其他 IP 地址通信。你也会租用一个 IP 地址；这些地址会持续一定时间，然后根据你的租约设置进行续订。

DHCP 有很多优点：它让网络管理员无需担心分配 IP 地址，也防止了重复 IP 地址的设置。每个物理网络都应该有自己的 DHCP 服务器，以便主机可以请求 IP 地址。在普通的家庭环境中，路由器通常充当 DHCP 服务器。

DHCP 获取所有动态主机信息的方式是：

1. DHCP DISCOVER - 此消息以广播形式发送，用于搜索 DHCP 服务器。
2. DHCP OFFER - 网络中的 DHCP 服务器回复一个提供消息。该提供消息包含一个数据包，其中包含 DHCP 租约时间、子网掩码、IP 地址等。
3. DHCP REQUEST - 客户端发出另一个广播，让所有 DHCP 服务器知道它接受了哪个提供。
4. DHCP ACK - 服务器发送确认。

DHCP 比这更复杂，但这只是它的要点。

## Exercise

熟能生巧！以下是一些动手实验，以加强您对动态 IP 寻址和网络配置的理解：

1. **[在 Linux 中管理 IP 寻址](https://labex.io/zh/labs/linux-manage-ip-addressing-in-linux-592736)** - 练习使用 `ip` 命令检查接口，并专门使用 `dhclient` 获取动态 IP 地址，直接应用您对 DHCP 的知识。
2. **[在 Linux 中识别 MAC 和 IP 地址](https://labex.io/zh/labs/linux-identify-mac-and-ip-addresses-in-linux-592731)** - 学习使用 `ip a` 命令识别网络寻址信息，包括 DHCP 分配的 IP 地址，并检查网络接口。
3. **[在 Linux 中探索 IP 地址类型和可达性](https://labex.io/zh/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** - 使用 `ping` 和 `ip a` 探索 IP 寻址和网络可达性，帮助您了解动态分配的 IP 如何在网络中发挥作用。

这些实验将帮助您在实际场景中应用动态 IP 分配和网络配置的概念，并增强您对 Linux 网络的信心。

## Quiz Question

DHCP 请求的步骤是什么？

## Quiz Answer

DISCOVER, OFFER, REQUEST, ACK
