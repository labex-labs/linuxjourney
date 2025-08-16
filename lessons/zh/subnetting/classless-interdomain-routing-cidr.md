---
title: "CIDR"
description: "学习 Linux 网络中的 CIDR 表示法。通过这个初学者友好的指南，了解子网掩码、IP 寻址和主机计算。提升您的网络技能！"
keywords: "CIDR, 子网掩码，IP 寻址，网络前缀，Linux 网络，初学者，教程，指南"
---

## Lesson Content

CIDR（无类别域间路由）用于以更紧凑的方式表示子网掩码。您可能会看到以 CIDR 表示法标记的子网，例如 10.42.3.0/255.255.255.0 这样的子网被写成 10.42.3.0/24。这种表示法同时包含了子网前缀和子网掩码。

请记住，一个 IP 地址由 4 个字节或 32 位组成。CIDR 表示用作网络前缀的位数。因此，123.12.24.0/23 意味着前 23 位被使用。这意味着什么？有多少主机？

一个简单的技巧是从 IP 地址总位数（32）中减去 CIDR 地址（23）。这剩下 9 位。因此，2^9 = 512。但是，我们必须移除 2 个地址（子网地址和广播地址），所以我们有 510 个可用主机。

## Exercise

No exercises for this lesson.

## Quiz Question

No questions, move along!

## Quiz Answer
