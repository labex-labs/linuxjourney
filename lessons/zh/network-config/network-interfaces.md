---
lesson_id: "network-interfaces"
course_id: "network-config"
lang: "zh"
order_index: 1
title: "网络接口"
description: "学习如何检查 Linux 接口状态、地址、统计信息和持久配置归属。"
meta_title: "网络接口 - 网络配置"
meta_description: "全面介绍 Linux 网络接口。学习使用 ifconfig 和现代 ip 命令，并了解 Debian 等系统上的 /etc/network/interfaces 配置文件。"
meta_keywords: "Linux 接口, Linux 网络接口, etc network interfaces, Debian 网络接口, ifconfig, ip 命令, 网络配置, Linux 网络"
---

Linux 网络接口将网络命名空间连接到物理设备、环回路径、网桥、隧道、虚拟设备或其他链路。接口状态、地址、路由、DNS 和持久配置相互关联，但彼此不同。

## 发现接口

使用现代 iproute2 工具：

```bash
$ ip -brief link show
$ ip -brief address show
```

接口名称可能是 `enp1s0` 这样基于硬件的可预测名称、`eth0` 这样的传统名称，或管理员定义的名称。绝不要假定 `eth0` 一定存在或标识某个特定适配器。

:::single-choice{#interfaces-name-assumption} 为什么脚本应该发现接口，而不是假定存在 `eth0`？

::option[每个接口都必须命名为 `lo`。]{#interfaces-all-loopback explanation="环回是一个特殊接口，并非每条链路的名称。"}
::option[Linux 系统可以使用多种接口命名方案。]{#interfaces-naming-varies .correct explanation="基于硬件、虚拟和自定义的名称使固定 eth0 假设不可靠。"}
::option[接口名称始终是远程密码。]{#interfaces-name-password explanation="名称标识内核设备，不是凭据。"}
:::

## 管理状态与运行状态

`UP` 表示接口在管理上已启用。`LOWER_UP` 通常表示较低层报告运行就绪，例如检测到以太网载波。任何一个标志都不能单独证明 IP 地址、路由、DNS、防火墙或应用程序路径正常。

```bash
$ ip -details link show dev enp1s0
$ ip -s link show dev enp1s0
```

统计视图可以显示错误、丢弃和计数器，但只有结合时间区间和基线，计数器才有意义。

:::single-choice{#interfaces-up-limit} 管理状态 `UP` 无法证明什么？

::option[端到端连接正常。]{#interfaces-up-not-connectivity .correct explanation="较低层、寻址、路由、过滤、命名和服务故障仍可能存在。"}
::option[管理员启用了该接口。]{#interfaces-up-does-prove explanation="这正是该状态的直接含义。"}
::option[该接口拥有内核对象。]{#interfaces-up-kernel-object explanation="所显示的状态属于一个现有内核接口。"}
:::

## 更改运行时状态

运行时命令包括：

```bash
$ sudo ip link set dev enp1s0 up
$ sudo ip address add 192.0.2.10/24 dev enp1s0
```

这些更改影响当前内核状态，并可能与之后重新应用配置文件的网络管理器冲突。关闭远程管理接口可能立即中断访问。更改前应确认确切设备、保留控制台访问、记录当前状态，并准备定时或经过测试的回滚。

:::single-choice{#interfaces-ip-address-add-persistence} `ip address add` 本身能保证重启后设置仍然存在吗？

::option[不能；活动配置系统还必须保存该设置。]{#interfaces-manager-persistence .correct explanation="NetworkManager、systemd-networkd、ifupdown 或其他所有者负责应用持久策略。"}
::option[能，因为每次内核更改都会编辑所有管理器配置文件。]{#interfaces-runtime-always-persistent explanation="内核运行时更改不会普遍更新持久配置。"}
::option[只有地址是私有 IPv4 时才可以。]{#interfaces-private-persistent explanation="地址作用域不会让运行时命令变成持久配置。"}
:::

## 确定配置归属

不同发行版和安装的持久配置路径各不相同，可能包括 NetworkManager 配置文件、systemd-networkd 单元、netplan 输入、`/etc/network/interfaces`、cloud-init 或编排系统。编辑文件前，应确定哪个服务管理该设备：

```bash
$ systemctl --type=service --state=running | grep -E 'NetworkManager|networkd|networking'
$ networkctl status
$ nmcli device status
```

只使用已确定管理器所提供的命令。两个管理器控制同一条链路时可能相互竞争，并覆盖对方的状态。

:::single-choice{#interfaces-config-owner} 持久更改接口前应该做什么？

::option[编辑每个可能的网络配置文件。]{#interfaces-edit-all explanation="相互竞争的定义会造成冲突和不可预测的重新应用。"}
::option[确定哪个网络管理器拥有该接口。]{#interfaces-identify-owner .correct explanation="正确的配置来源和应用方法取决于归属。"}
::option[检查前删除所有当前路由。]{#interfaces-delete-routes explanation="这具有破坏性，可能移除恢复访问。"}
:::

## 验证更改

应验证链路状态、分配的地址和有效期、所选路由、解析器状态、邻居可达性及实际应用程序。对于持久更改，只有存在恢复通道时，才能通过受控服务重启或系统重启进行测试。

:::single-choice{#interfaces-change-verification} 什么比在 `ip address` 中看到新地址更能证明更改有效？

::option[接口名称中包含数字。]{#interfaces-digit explanation="命名不能提供端到端验证。"}
::option[shell 提示符颜色保持不变。]{#interfaces-prompt-color explanation="终端外观与网络运行无关。"}
::option[路由、解析器状态和预期应用程序也都正常工作。]{#interfaces-end-to-end .correct explanation="可用配置取决于完整路径和服务行为。"}
:::

## 总结

现在，你可以检查和更改接口，而不会混淆运行时状态与持久策略。

1. 发现真实接口名称和地址。
2. 区分管理状态与运行连接。
3. 将直接 `ip` 更改视为当前内核状态。
4. 持久更改前确定活动配置所有者。
5. 之后验证路由、解析和应用程序行为。
