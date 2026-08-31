---
lesson_id: "dhclient"
course_id: "network-config"
lang: "zh"
order_index: 3
title: "dhclient"
description: "学习何时以及如何使用 dhclient，同时避免与系统网络管理器冲突。"
meta_title: "dhclient - 网络配置"
meta_description: "了解 dhclient 如何使用 DHCP 获取 IP 地址和管理网络租约，并认识 dhclient.conf 与 dhclient.leases 文件。Linux 初学者指南。"
meta_keywords: "dhclient, DHCP, Linux 网络, IP 地址, 网络配置, Linux 教程, 初学者指南"
---

`dhclient` 是部分 Linux 系统提供的 ISC DHCP 客户端。许多现代安装会改由 NetworkManager、systemd-networkd 或其他服务运行自己的 DHCP 客户端。在已管理接口上启动第二个客户端，可能造成相互竞争的地址、路由、DNS 设置和租约状态。

## 确定活动客户端

调用 `dhclient` 前，应检查配置所有者和进程：

```bash
$ nmcli device status
$ networkctl status
$ ps -ef | grep '[d]hclient'
```

应使用主机上实际存在的工具。如果某个管理器拥有接口，应通过该管理器请求 DHCP，而不是启动单独的客户端。

:::single-choice{#dhclient-second-client-risk}
为什么要避免在已受管理的接口上启动 `dhclient`？

::option[DHCP 只能分配环回地址。]{#dhclient-loopback-only explanation="DHCP 通常会分配非环回网络配置。"}
::option[两个客户端可能会争用地址、路由、DNS 和租约。]{#dhclient-competing-state .correct explanation="通常只应由已经确定的配置所有者协调接口。"}
::option[每个 DHCP 请求都会重新格式化本地磁盘。]{#dhclient-reformats explanation="该协议改变网络状态，而不是磁盘格式。"}
:::

## 显式请求租约

在以 `dhclient` 为预期所有者的非托管测试接口上，应指定接口并使用详细输出：

```bash
$ sudo dhclient -v enp1s0
```

不指定接口运行时，可能会影响多个符合条件的接口。配置和租约路径因软件包与调用方式而异；常见名称包括 `dhclient.conf` 和 `dhclient.leases`，但不要假定固定位置。

:::single-choice{#dhclient-interface-operand}
手动请求时为什么要指定 `enp1s0`？

::option[只针对预期网络接口。]{#dhclient-scope-interface .correct explanation="未限定的客户端调用可能考虑超出预期的接口。"}
::option[为 DHCP 选择 TCP 端口 1。]{#dhclient-tcp-port explanation="DHCP 使用 UDP，接口名称不是端口。"}
::option[让租约永久有效。]{#dhclient-permanent explanation="DHCP 配置仍然是有期限的租约状态。"}
:::

## 释放租约

`dhclient -r INTERFACE` 会请求释放租约，并可能移除可用配置。该操作会造成中断，而且不能保证服务器可达并收到释放消息。不要仅仅为了检查租约而释放它，尤其不能在远程管理路径上这样做。

:::single-choice{#dhclient-release-effect}
`dhclient -r enp1s0` 有什么运维风险？

::option[它只打印当前租约，不作更改。]{#dhclient-release-readonly explanation="释放是会改变状态的操作。"}
::option[它会无限期续订每个租约。]{#dhclient-release-renews explanation="释放与续订是相反的操作。"}
::option[它可能移除当前 DHCP 连接。]{#dhclient-release-connectivity .correct explanation="释放流程会放弃租约状态，并可能终止远程访问。"}
:::

## 验证已应用租约

完成受控请求后，不能只验证地址：

```bash
$ ip address show dev enp1s0
$ ip route show
$ resolvectl status
```

应检查管理器或客户端日志及租约有效期，再测试预期的名称解析和应用程序。DHCPACK 可能携带错误选项，成功分配地址也不能证明网关或 DNS 可达。

:::single-choice{#dhclient-verify-state}
获得租约后应该验证什么？

::option[地址、路由、DNS、租约及应用程序行为。]{#dhclient-complete-verify .correct explanation="租约会配置多个必须协同工作的相关组件。"}
::option[只验证地址字符串是否出现。]{#dhclient-address-only explanation="路由、DNS、有效期和端到端功能仍可能有误。"}
::option[只检查桌面背景。]{#dhclient-wallpaper explanation="桌面外观与 DHCP 状态无关。"}
:::

## 总结

现在，你可以只在 `dhclient` 是接口预期所有者时使用它。

1. 发现活动网络管理器和 DHCP 客户端。
2. 避免一个接口上存在相互竞争的客户端。
3. 将手动请求限制到具名测试接口。
4. 将释放视为中断操作，并验证完整租约结果。
