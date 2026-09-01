---
lesson_id: "network-addressing"
course_id: "network-basics"
lang: "zh"
order_index: 4
title: "网络寻址"
description: "学习链路地址、IP 地址和主机名如何标识网络通信的不同部分。"
meta_title: "网络寻址 - 网络基础"
meta_description: "了解网络寻址基础。本指南介绍 MAC 地址、IP 地址和主机名，这些是理解设备如何在 Linux 网络中通信的关键概念。"
meta_keywords: "网络寻址, MAC 地址, IP 地址, 主机名, 网络标识符, Linux 网络, 网络基础, 初学者, 教程, 指南"
---

网络通信在不同作用范围使用不同标识符。链路层地址在本地链路上传送帧，IP 地址支持经过路由的传送，名称则帮助应用程序和用户选择服务。

## 链路层地址

以太网 MAC 地址为 48 位，通常写成六个十六进制八位组，例如 `00:c4:b5:45:b2:43`。源地址标识当前链路上的接口，目标地址则可以是单播、多播或广播地址。

MAC 地址不保证永久不变或全球唯一。软件可以分配本地管理地址，虚拟接口会生成地址，Wi-Fi 隐私功能也可能将地址随机化。路由器通常在每一跳替换以太网帧，因此远程服务器不会收到原始本地以太网源地址。

:::single-choice{#network-addressing-mac-scope} 在数据包传送中，以太网 MAC 地址的正常作用范围是什么？

::option[当前本地链路。]{#network-addressing-local-link .correct explanation="路由器会为后续跳点创建新的链路层帧。"}
::option[到最终互联网服务器的每个路由跳点。]{#network-addressing-all-hops explanation="原始帧不会原封不动地跨越路由器。"}
::option[仅限应用程序的文本编码。]{#network-addressing-text-encoding explanation="MAC 地址属于链路层帧。"}
:::

## IP 地址与前缀

IPv4 地址为 32 位，即四个八位组；IPv6 地址为 128 位。IP 地址通常分配给接口，并结合 `192.0.2.10/24` 或 `2001:db8::10/64` 这样的前缀长度来解释。前缀标明从开头起多少位用于描述网络。

一个接口可以拥有多个 IP 地址，地址也可能因为 DHCP、隐私寻址、故障转移或管理操作而改变。私有 IPv4 地址可以在不同网络中重复使用；外部可达性由公网路由和 NAT 策略决定。

:::single-choice{#network-addressing-ipv4-size} IPv4 地址有多大？

::option[32 位，由四个八位组组成。]{#network-addressing-thirty-two .correct explanation="显示的每个十进制部分表示八位。"}
::option[4 位，由一个十六进制数字组成。]{#network-addressing-four-bits explanation="四位只能表示一个十六进制数字。"}
::option[128 位，由十六个八位组组成。]{#network-addressing-128-octets explanation="IPv6 是 128 位，而不是 128 个八位组。"}
:::

## 主机名与名称解析

主机名是名称，而不是地址。名称解析可以按照主机的名称服务配置查询 `/etc/hosts`、DNS、多播系统或其他来源。一个名称可以解析为多个地址，多个名称也可以指向同一个服务。

测试应用程序可能看到的结果时，应使用系统解析器路径：

```bash
$ getent ahosts example.com
```

DNS 答案可能改变或被缓存，而且解析成功并不能证明服务可达。

:::single-choice{#network-addressing-getent-purpose} 检查名称解析时为什么使用 `getent ahosts`？

::option[它会把返回的地址永久分配给每个接口。]{#network-addressing-getent-assign explanation="该命令查询数据库，不会配置接口。"}
::option[它通过系统配置的名称服务路径查询地址。]{#network-addressing-system-resolver .correct explanation="根据主机策略，这条路径可以包括本地文件和 DNS。"}
::option[它保证每个返回主机上的应用程序都健康。]{#network-addressing-getent-health explanation="名称查询与应用程序健康是两项不同测试。"}
:::

## 检查 Linux 主机

分别查看链路配置和 IP 配置：

```bash
$ ip -brief link
$ ip -brief address
```

诊断可达性时，再检查路由和邻居状态。绝不要只根据名称推断正确的源接口或地址；路由选择、策略规则、命名空间和隧道都可能改变路径。

:::single-choice{#network-addressing-ip-link-versus-address} 哪个命令视图重点显示已分配的 IP 地址？

::option[`ip -brief address`]{#network-addressing-address-view .correct explanation="address 对象显示接口上的 IPv4 和 IPv6 分配。"}
::option[只使用 `ip -brief link`。]{#network-addressing-link-only explanation="link 视图重点显示接口和链路层状态。"}
::option[`pwd`]{#network-addressing-pwd explanation="pwd 输出 shell 的工作目录。"}
:::

## 总结

现在，你可以根据网络作用范围区分名称和地址。

1. 将 MAC 地址视为可能改变的本地链路标识符。
2. 结合前缀长度读取 IPv4 和 IPv6 地址。
3. 认识到接口可以拥有多个逻辑地址。
4. 通过已配置的系统解析器查询主机名。
