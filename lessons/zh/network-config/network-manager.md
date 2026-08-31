---
lesson_id: "network-manager"
course_id: "network-config"
lang: "zh"
order_index: 4
title: "NetworkManager"
description: "学习 NetworkManager 如何区分设备、持久连接配置文件和活动运行时状态。"
meta_title: "NetworkManager - 网络配置"
meta_description: "了解 NetworkManager 守护进程在现代 Linux 网络管理中的作用。学习它如何自动配置网络，以及如何使用 nm-tool 和强大的 nmcli 命令行工具进行交互。"
meta_keywords: "NetworkManager, nm-tool, nmcli, Linux 网络管理器, Linux 网络管理, 网络配置, Linux 网络"
---

NetworkManager 在许多 Linux 桌面和服务器上管理网络设备并激活连接配置文件。它并不普遍存在，因此使用 `nmcli` 更改配置前，应确认它拥有目标接口。

## 设备与连接

设备是 `enp1s0` 或 `wlan0` 等内核接口。连接是存储 IPv4、IPv6、DNS、Wi-Fi、路由和其他设置的配置文件。一个设备可以拥有多个配置文件，但通常一次只有一个适用配置文件处于活动状态。

```bash
$ nmcli device status
$ nmcli connection show
$ nmcli connection show --active
```

:::single-choice{#networkmanager-device-profile}
什么是 NetworkManager 连接配置文件？

::option[焊接在网卡上的物理连接器。]{#networkmanager-physical-connector explanation="这是硬件，不是 NetworkManager 配置文件。"}
::option[可以在设备上激活的一组已存储设置。]{#networkmanager-stored-settings .correct explanation="配置文件独立于内核接口对象持久保存配置。"}
::option[从每个活动流捕获的数据包。]{#networkmanager-packet-capture explanation="配置文件描述配置，并不包含全部流量。"}
:::

## 检查生效状态

显示活动配置文件和设备详情：

```bash
$ nmcli -f GENERAL,IP4,IP6 device show enp1s0
$ nmcli connection show 'Wired connection 1'
```

配置文件设置、运行时 DHCP 结果和内核状态可能不同。应与 `ip address`、`ip route` 和解析器相互比较。已弃用的 `nm-tool` 不应作为现代工作流程的基础。

:::single-choice{#networkmanager-active-command}
哪个命令列出活动的 NetworkManager 配置文件？

::option[`nmcli device delete --all`]{#networkmanager-delete-all explanation="这不是检查命令，而且表达了破坏性意图。"}
::option[`nmcli connection show --active`]{#networkmanager-show-active .correct explanation="它会将已存储连接过滤为当前已激活的连接。"}
::option[`ip route flush table all`]{#networkmanager-flush-routes explanation="它会移除路由状态，而不是列出配置文件。"}
:::

## 修改并激活配置文件

明确修改具名配置文件，再在维护窗口激活：

```bash
$ sudo nmcli connection modify 'Wired connection 1' ipv4.method auto
$ sudo nmcli connection up 'Wired connection 1'
```

修改会改变持久配置文件数据；激活可能替换实时地址、路由和 DNS。远程更改需要控制台访问、保存的原始设置和独立的定时回滚。绝不能依靠正在更改的连接来承载它自己的恢复命令。

:::single-choice{#networkmanager-modify-versus-up}
`connection modify` 与 `connection up` 有什么区别？

::option[modify 重启主机；up 编辑 DNS 源代码。]{#networkmanager-reboot-source explanation="两种描述都不符合这些命令。"}
::option[modify 更改配置文件设置；up 激活配置文件。]{#networkmanager-change-activate .correct explanation="持久性与运行时激活相互关联，但属于不同操作。"}
::option[它们都是永远不会影响连接的只读别名。]{#networkmanager-readonly explanation="在此工作流程中，两者都可能改变状态。"}
:::

## 验证并保护秘密

激活后，应验证配置文件状态、内核地址与路由、DNS、两个地址族及预期应用程序。Wi-Fi、VPN、802.1X 和移动网络配置文件可能包含秘密。应限制配置文件权限，避免把秘密字段打印到共享日志或 shell 记录中。

:::single-choice{#networkmanager-verification}
什么比 NetworkManager 报告“已连接”更能证明连接正常？

::option[配置文件名称包含 Wired 一词。]{#networkmanager-name-proof explanation="标签无法证明路径或服务健康。"}
::option[终端窗口仍然打开。]{#networkmanager-terminal-open explanation="某些部分网络故障不会立即关闭终端。"}
::option[预期的 DNS 和应用程序测试成功。]{#networkmanager-end-to-end .correct explanation="管理器状态必须与内核和服务行为相互印证。"}
:::

## 总结

现在，你可以管理 NetworkManager 配置文件，而不会将其与接口对象混淆。

1. 确认 NetworkManager 拥有目标设备。
2. 区分已存储配置文件与活动运行时状态。
3. 分别检查设备、所有配置文件和活动配置文件。
4. 将修改、激活、恢复和验证作为不同步骤。
