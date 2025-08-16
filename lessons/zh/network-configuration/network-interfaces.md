---
lang: "zh"
title: "网络接口"
description: "了解 Linux 网络接口、ifconfig 和 ip 命令。理解如何配置和管理网络设置。开始你的 Linux 网络之旅！"
keywords: "Linux 网络接口，ifconfig, ip 命令，网络配置，Linux 网络，初学者，教程，指南"
---

## Lesson Content

网络接口是内核将网络软件端与硬件端连接起来的方式。我们已经看到了一个例子：

```plaintext
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
```

### The ifconfig command

**ifconfig** 工具允许我们配置网络接口。如果我们没有设置任何网络接口，内核的设备驱动程序和网络将不知道如何相互通信。ifconfig 在启动时运行，并通过配置文件配置我们的接口，但我们也可以手动修改它们。ifconfig 的输出显示接口名称在左侧，右侧显示详细信息。你最常看到的接口名称是 eth0（机器中的第一块以太网卡）、wlan0（无线接口）和 lo（回环接口）。回环接口用于表示你的计算机；它只是将你循环回自己。这对于调试或连接到本地运行的服务器很有用。

接口的状态可以是 up 或 down。正如你所猜测的，如果你想“关闭”一个接口，你可以将其设置为 down。你最可能在 ifconfig 输出中查看的字段是 HWaddr（接口的 MAC 地址）、inet address（IPv4 地址）和 inet6（IPv6 地址）。当然，你也可以看到子网掩码和广播地址也在那里。你还可以在 /etc/network/interfaces 查看接口信息。

### To create an interface and bring it up

```bash
ifconfig eth0 192.168.2.1 netmask 255.255.255.0 up
```

这将为 eth0 接口分配一个 IP 地址和子网掩码，并将其启动。

### To bring up or down an interface

```bash
ifup eth0
ifdown eth0
```

### The ip command

**ip** 命令也允许我们操作系统的网络堆栈。根据你使用的发行版，它可能是操作网络设置的首选方法。

以下是一些使用示例：

### To show interface information for all interfaces

```bash
ip link show
```

### To show the statistics of an interface

```bash
ip -s link show eth0
```

### To show IP addresses allocated to interfaces

```bash
ip address show
```

### To bring interfaces up and down

```bash
ip link set eth0 up
ip link set eth0 down
```

### To add an IP address to an interface

```bash
ip address add 192.168.1.1/24 dev eth0
```

## Exercise

尝试将网络接口的状态更改为 up 或 down，并观察会发生什么。

你能同时使用 ifconfig 和 ip 命令更改网络接口吗？

## Quiz Question

配置网络接口的命令是什么？

## Quiz Answer

ifconfig
