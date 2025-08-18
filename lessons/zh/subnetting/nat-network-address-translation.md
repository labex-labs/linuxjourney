---
index: 6
lang: "zh"
title: "NAT"
meta_title: "NAT - 子网划分"
meta_description: "了解 Linux 中的 NAT（网络地址转换），它的工作原理及其在网络安全中的作用。理解私有 IP 与公共 IP。Linux 网络指南。"
meta_keywords: "NAT, 网络地址转换，Linux 网络，私有 IP, 公共 IP, Linux 教程，初学者指南"
---

## Lesson Content

我们之前提到过 NAT (网络地址转换)，但没有深入探讨。当我们在自己的网络中工作时，这是否意味着互联网可以看到我们的 IP 地址？不完全是。

NAT 使我们的路由器等设备充当互联网和私有网络之间的中介。因此，只需要一个唯一的 IP 地址就可以代表整个计算机组。

将 NAT 想象成一个大型办公室的接待员。如果有人想联系你，他们只知道整个办公室的电话号码。然后接待员必须查找你的分机号码并将电话转接给你。

### 它是如何工作的？

一个简单的例子是这样的：

1. Patty 想连接到 <www.google.com>，所以她的机器通过路由器发送此请求。
2. 路由器接收该请求并打开自己与 google.com 的连接，然后一旦建立连接就发送 Patty 的请求。
3. 路由器是 Patty 和 <www.google.com> 之间的中介。Google 不知道 Patty；相反，它只能看到路由器。

NAT 和一般的包路由可能会变得相当复杂，但我们不会深入探讨具体细节。

## Exercise

No exercises for this lesson.

## Quiz Question

什么用于将单个私有地址表示给互联网？

## Quiz Answer

NAT
