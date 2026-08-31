---
lesson_id: "network-basics"
course_id: "network-basics"
lang: "zh"
order_index: 1
title: "网络基础"
description: "学习主机、链路、交换机、路由器和数据包如何构成本地网络与广域网。"
meta_title: "网络基础 - 网络基础"
meta_description: "从网络基础开始学习 Linux。本指南面向初学者，介绍 WAN、LAN、路由器和主机等基本网络组件。"
meta_keywords: "网络基础, Linux 基础, 学习 Linux 的最佳方式, Linux 基础知识, WAN, LAN, WLAN, 网络教程, 网络指南"
---

网络连接各个接口，使不同主机上的应用程序能够交换数据。理解路径中每一部分由哪个设备、地址和链路处理，会让后续 Linux 命令更容易解读。

## 主机与接口

主机是端点或联网系统，例如笔记本电脑、服务器、手机或虚拟机。一台主机可以有多个接口：以太网、Wi-Fi、环回、隧道、网桥或虚拟适配器。每个接口都可以具有适合其技术的链路层和网络层配置。

使用以下命令检查 Linux 主机的接口和地址：

```bash
$ ip address show
```

接口存在或在管理上处于启用状态，并不能证明端到端连接正常。

:::single-choice{#network-basics-host-interface}
什么是网络接口？

::option[互联网上每个数据包的永久副本。]{#network-basics-interface-copy explanation="接口发送和接收流量，并不是全局数据包归档。"}
::option[主机连接到网络或虚拟链路的接入点。]{#network-basics-interface-attachment .correct explanation="一台主机可以拥有多个物理或虚拟接口，并分别进行配置。"}
::option[ISP 账单的易读别名。]{#network-basics-interface-invoice explanation="计费标签与主机网络接入无关。"}
:::

## 局域网

局域网（LAN）覆盖家庭、办公室或数据中心网段等有限环境。以太网交换机在本地链路的端口之间转发帧。无线局域网（WLAN）使用无线链路技术。当网桥或接入点连接有线和无线接口时，它们仍可以属于同一个 IP 子网。

:::single-choice{#network-basics-wlan-relationship}
WLAN 与 LAN 有什么关系？

::option[WLAN 始终是一个独立的全球互联网。]{#network-basics-wlan-global explanation="它是使用无线链路技术的本地网络。"}
::option[WLAN 是路由器使用的磁盘分区。]{#network-basics-wlan-disk explanation="该术语描述网络，而不是存储布局。"}
::option[WLAN 是局域网的无线形式。]{#network-basics-wlan-local .correct explanation="无线与有线链路甚至可以桥接到同一个本地广播域。"}
:::

## 路由器与更广的网络

路由器按照路由表在 IP 网络之间转发网络层数据包。家用设备通常会组合路由、交换、Wi-Fi 接入、防火墙、NAT 和 DHCP，但这些仍是不同功能。

广域网（WAN）跨越较大的地理或管理边界。互联网服务提供商可以把客户网络连接到其他网络，但“WAN”并不只是指某个家庭之外的每台设备。

:::single-choice{#network-basics-router-role}
路由器的核心职责是什么？

::option[在网络层网络之间转发数据包。]{#network-basics-forward-networks .correct explanation="路由会跨越 IP 网络边界选择下一跳。"}
::option[将每个用户的文件存储为强制备份。]{#network-basics-router-backup explanation="文件保留不是路由的核心功能。"}
::option[不查询 DNS 就转换每个主机名。]{#network-basics-router-hostnames explanation="名称解析与数据包转发是不同功能。"}
:::

## 数据包、帧与流

应用程序产生数据，协议层会将其分段并封装以便传输。IP 跨网络承载数据包；本地链路则将每个数据包放在与具体技术相关的帧中传输。路由器转发 IP 数据包时，通常会在每一跳替换链路层帧。

一次通信可能包含双向传输的许多数据包。丢失、乱序、分片、重传和路径变化意味着，捕获到的单个数据包很少能描述完整的应用程序事务。

:::single-choice{#network-basics-router-frame}
在路由器这一跳，链路层帧通常会发生什么？

::option[路由器移除传入帧，并为下一条链路创建新帧。]{#network-basics-reframe .correct explanation="转发的 IP 数据包会装入适合传出接口的新链路层帧中。"}
::option[同一个以太网帧原封不动地穿越整个互联网。]{#network-basics-same-frame explanation="帧的作用范围限于所在链路，并会在路由跳点被替换。"}
::option[应用程序永久删除 IP 地址。]{#network-basics-delete-ip explanation="路由依赖网络层地址。"}
:::

## 总结

现在，你可以描述一条基本网络路径的主要组成部分。

1. 区分主机及其物理和虚拟接口。
2. 识别局域网的有线和无线形式。
3. 将组合式家用设备中的路由与其他功能分开理解。
4. 区分链路帧与经过路由的 IP 数据包。
