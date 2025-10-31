---
index: 1
lang: "zh"
title: "网络接口"
meta_title: "网络接口 - 网络配置"
meta_description: "Linux 网络接口的综合指南。学习使用 ifconfig 和现代的 ip 命令，并了解/etc/network/interfaces 等配置文件，尤其是在 Debian 系统上。"
meta_keywords: "linux 接口，linux 网络接口，etc network interfaces, debian 网络接口，ifconfig, ip 命令，网络配置，linux 网络"
---

## Lesson Content

一个 **linux 网络接口** 是内核软件网络堆栈与物理网络硬件之间的关键连接点。它允许您的操作系统通过网络发送和接收数据。我们已经看到了一个已配置的 `linux 接口` 是什么样子的示例：

```plaintext
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
```

### 理解网络接口

当您查看网络设置时，您会看到名称如 `eth0`（第一个以太网卡）、`wlan0`（无线接口）或 `lo`（回环接口）的接口。回环接口是一个特殊的虚拟接口，代表您自己的计算机，允许您连接到本地运行的服务。

接口可以处于“up”（启动）或“down”（关闭）状态。“up”状态意味着它处于活动状态并准备好传输数据，而“down”则停用了它。每个接口显示的关键信息包括 `HWaddr`（其唯一的 MAC 地址）、`inet` 地址（其 IPv4 地址）和 `inet6` 地址（其 IPv6 地址），以及子网掩码和广播地址。

### 遗留的 ifconfig 命令

**ifconfig** 命令是配置 `linux 网络接口` 的经典工具。在系统启动时，它通常会运行以根据配置文件设置接口。虽然它在许多系统上仍然可用，但现在被认为是一个遗留工具。

您可以使用 `ifconfig` 手动分配 IP 地址并启动一个接口：

```bash
ifconfig eth0 192.168.2.1 netmask 255.255.255.0 up
```

您还可以使用相关的 `ifup` 和 `ifdown` 命令轻松激活或停用接口：

```bash
ifup eth0
ifdown eth0
```

### 现代的 ip 命令

**ip** 命令是 `ifconfig` 的现代且功能更强大的替代品。它是大多数当前 Linux 发行版中管理网络堆栈的首选方法。

以下是一些常见的用法示例：

**显示所有接口的信息：**

```bash
ip link show
```

**显示特定接口的详细统计信息：**

```bash
ip -s link show eth0
```

**显示分配给接口的 IP 地址：**

```bash
ip address show
```

**启动或关闭接口：**

```bash
ip link set eth0 up
ip link set eth0 down
```

**向接口添加 IP 地址：**

```bash
ip address add 192.168.1.1/24 dev eth0
```

### 网络配置文件

虽然像 `ip` 和 `ifconfig` 这样的命令配置了接口的实时状态，但这些更改不是永久性的，重启后会丢失。要使设置持久化，您必须编辑配置文件。

这些文件的常见位置是 `/etc/network/interfaces`。`etc network interfaces` 文件在基于 Debian 的系统（如 Ubuntu）上尤其常见。通过此文件管理 **debian 网络接口** 允许您定义静态 IP 地址、网关和其他在启动时自动应用的设置。`debian network/interfaces` 中的结构简单且文档记录良好。

## Exercise

通过这些实践实验将您的知识付诸实践。它们将帮助您巩固对网络接口和 IP 地址的理解。

1. **[在 Linux 中识别 MAC 和 IP 地址](https://labex.io/zh/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - 练习使用 `ip a` 命令来识别 Linux 系统上的网络寻址信息，包括 MAC 地址、IPv4 地址和 IPv6 地址。
2. **[在 Linux 中管理 IP 地址](https://labex.io/zh/labs/comptia-manage-ip-addressing-in-linux-592736)** - 学习使用 `ip` 命令配置静态和动态 IP 地址、设置默认网关以及验证网络配置。
3. **[在 Linux 中探索 IP 地址类型和可达性](https://labex.io/zh/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - 探索不同的 IP 地址类型（私有、公共、多播）并使用 `ping` 和 `ip a` 测试网络可达性。

这些实验将帮助您在真实场景中应用网络接口识别和 IP 寻址的概念，并增强您对 Linux 网络的信心。

## Quiz Question

用于配置 Linux 网络接口的遗留命令是什么？请用英文回答，只使用小写字母。

## Quiz Answer

ifconfig
