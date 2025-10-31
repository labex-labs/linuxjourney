---
index: 9
lang: "zh"
title: "DHCP 概述"
meta_title: "DHCP 概述 - 网络基础知识"
meta_description: "了解 DHCP（动态主机配置协议）的基础知识。本指南涵盖 DHCP 如何分配 IP 地址、其四步过程 (DORA) 及其在网络 DHCP 层中的作用。非常适合 Linux 网络初学者。"
meta_keywords: "DHCP, 动态主机配置协议，dhcp 层，IP 地址，Linux 网络，DHCP 过程，DORA, 网络配置"
---

## Lesson Content

动态主机配置协议（DHCP）是一种基本的网络协议，用于自动为网络上的设备分配 IP 地址和其他网络配置参数。

### 什么是 DHCP？

将 DHCP 视为设备的“电话公司”。当您拿到一部新手机时，需要一个号码才能开始通信。您联系运营商，他们会分配给您一个号码。同样，当设备连接到网络时，它需要一个 IP 地址才能与其他设备通信。DHCP 就是提供此 IP 地址的服务。

此 IP 地址通常会“租用”特定时间。在租约到期之前，设备可以续订它，从而确保持续连接。此自动化过程对于管理任何网络上的设备至关重要。

### DHCP 服务器的作用

DHCP 服务器负责管理一个 IP 地址池并将其租借给客户端设备。在典型的家庭网络中，您的路由器通常充当 DHCP 服务器。在更大的网络中，专用的服务器处理此任务。

使用 DHCP 有明显的优势：

- **自动化：** 网络管理员无需手动配置每台设备，节省了时间和精力。
- **准确性：** 它可以防止分配重复 IP 地址等常见错误，这可能导致网络冲突。

每个物理网络都应该有自己的 DHCP 服务器，以简化主机请求和接收 IP 地址的过程。该协议在应用层运行，构成了网络配置服务的一个关键部分，有时在概念上被称为 `dhcp layer`（DHCP 层）。

### 四步 DHCP 过程

设备通过 DHCP 获取 IP 地址的过程涉及四步交换，通常用首字母缩写 DORA 来记忆：

1.  **DHCP 发现 (DHCP Discover)：** 客户端设备在网络上广播一个 `DISCOVER` 消息，以查找可用的 DHCP 服务器。
2.  **DHCP 提供 (DHCP Offer)：** 任何收到发现消息的 DHCP 服务器都可以用 `OFFER` 消息进行响应。此消息包含提议的 IP 地址、子网掩码、网关地址和租约期限。
3.  **DHCP 请求 (DHCP Request)：** 客户端接收到一个或多个提议，并选择一个。然后它广播一个 `REQUEST` 消息，告知所有 DHCP 服务器它接受了哪个提议。
4.  **DHCP 确认 (DHCP Acknowledgment - ACK)：** 做出被接受提议的服务器向客户端发送最终的 `ACK` 消息，确认租约并最终确定配置。

虽然完整协议更为复杂，但这四个步骤代表了 DHCP 如何动态配置网络上主机的核心。

## Exercise

熟能生巧！以下是一些实践实验，以加强您对动态 IP 地址分配和网络配置的理解：

1.  **[在 Linux 中管理 IP 地址](https://labex.io/zh/labs/comptia-manage-ip-addressing-in-linux-592736)** - 练习使用 `ip` 命令检查接口，并专门使用 `dhclient` 来获取动态 IP 地址，直接应用您对 DHCP 的知识。
2.  **[在 Linux 中识别 MAC 和 IP 地址](https://labex.io/zh/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - 学习使用 `ip a` 命令来识别网络寻址信息，包括 DHCP 分配的 IP 地址，并检查网络接口。
3.  **[在 Linux 中探索 IP 地址类型和可达性](https://labex.io/zh/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - 使用 `ping` 和 `ip a` 探索 IP 地址和网络可达性，帮助您了解动态分配的 IP 在网络中如何工作。

这些实验将帮助您在实际场景中应用动态 IP 分配和网络配置的概念，并增强您对 Linux 网络操作的信心。

## Quiz Question

DHCP 过程中的四个步骤按顺序是什么？请用英文回答，使用大写单词，并用逗号和空格分隔。

## Quiz Answer

DISCOVER, OFFER, REQUEST, ACK
