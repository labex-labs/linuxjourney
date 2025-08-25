---
index: 1
lang: "zh"
title: "网络接口"
meta_title: "网络接口 - 网络配置"
meta_description: "了解 Linux 网络接口、ifconfig 和 ip 命令。理解如何配置和管理网络设置。开始您的 Linux 网络之旅！"
meta_keywords: "Linux 网络接口，ifconfig, ip 命令，网络配置，Linux 网络，初学者，教程，指南"
---

## Lesson Content

网络接口是内核将网络软件端连接到硬件端的方式。我们已经看到了一个例子：

```plaintext
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
```

### ifconfig 命令

**ifconfig** 工具允许我们配置网络接口。如果我们没有设置任何网络接口，内核的设备驱动程序和网络将不知道如何相互通信。Ifconfig 在启动时运行并通过配置文件配置我们的接口，但我们也可以手动修改它们。ifconfig 的输出显示左侧是接口名称，右侧显示详细信息。您最常看到的接口名称是 eth0（机器中的第一块以太网卡）、wlan0（无线接口）和 lo（回环接口）。回环接口用于表示您的计算机；它只是将您循环回自己。这对于调试或连接到本地运行的服务器很有用。

接口的状态可以是 up 或 down。正如您所猜测的，如果您想“关闭”一个接口，可以将其设置为 down。您在 ifconfig 输出中最常查看的字段可能是 HWaddr（接口的 MAC 地址）、inet address（IPv4 地址）和 inet6（IPv6 地址）。当然，您可以看到子网掩码和广播地址也在那里。您还可以在 /etc/network/interfaces 中查看接口信息。

### 创建接口并启用它

```bash
ifconfig eth0 192.168.2.1 netmask 255.255.255.0 up
```

这会为 eth0 接口分配一个 IP 地址和子网掩码，并将其启用。

### 启用或禁用接口

```bash
ifup eth0
ifdown eth0
```

### ip 命令

**ip** 命令也允许我们操作系统的网络堆栈。根据您使用的发行版，它可能是操作网络设置的首选方法。

以下是一些使用示例：

### 显示所有接口的接口信息

```bash
ip link show
```

### 显示接口的统计信息

```bash
ip -s link show eth0
```

### 显示分配给接口的 IP 地址

```bash
ip address show
```

### 启用和禁用接口

```bash
ip link set eth0 up
ip link set eth0 down
```

### 为接口添加 IP 地址

```bash
ip address add 192.168.1.1/24 dev eth0
```

## Exercise

熟能生巧！这里有一些动手实验来巩固您对网络接口和 IP 寻址的理解：

1. **[在 Linux 中识别 MAC 和 IP 地址](https://labex.io/zh/labs/linux-identify-mac-and-ip-addresses-in-linux-592731)** - 练习使用 `ip a` 命令在 Linux 系统上识别网络寻址信息，包括 MAC、IPv4 和 IPv6 地址。
2. **[在 Linux 中管理 IP 寻址](https://labex.io/zh/labs/linux-manage-ip-addressing-in-linux-592736)** - 学习配置静态和动态 IP 地址，设置默认网关，并使用 `ip` 命令验证网络配置。
3. **[在 Linux 中探索 IP 地址类型和可达性](https://labex.io/zh/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** - 探索不同的 IP 地址类型（私有、公共、多播）并使用 `ping` 和 `ip a` 测试网络可达性。

这些实验将帮助您在实际场景中应用网络接口识别和 IP 寻址的概念，并增强您对 Linux 网络的信心。

## Quiz Question

配置网络接口的命令是什么？

## Quiz Answer

ifconfig
