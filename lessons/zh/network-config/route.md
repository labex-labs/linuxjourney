---
lesson_id: "route"
course_id: "network-config"
lang: "zh"
order_index: 2
title: "route"
description: "学习如何使用 ip 检查、添加、替换、删除并安全验证 Linux 路由。"
meta_title: "route - 网络配置"
meta_description: "学习管理 Linux 路由表。本指南介绍如何使用现代 Linux ip route 命令和旧式 route 命令添加与删除网络路由。"
meta_keywords: "Linux ip route 命令, 添加路由, 删除路由, 路由表, 网络路由, Linux 网络, ip route"
---

手动路由会改变内核选择传出接口和下一跳的方式。错误可能断开主机连接或重定向敏感流量，因此更改状态前应检查生效路由、配置所有者和恢复通道。

## 检查当前决策

记录相关路由，并询问内核当前如何到达目标：

```bash
$ ip -4 route show
$ ip route get 192.168.2.25
```

如果存在策略规则和备用路由表，也要一并检查。路由查找只是本地证据，不会发送流量。

:::single-choice{#route-get-before-change} 为什么在更改路由前运行 `ip route get DESTINATION`？

::option[记录当前本地决策，以便比较和回滚。]{#route-get-baseline .correct explanation="所选接口、下一跳和源地址有助于定义预期变更。"}
::option[在每台路由器上永久保留该目标。]{#route-get-reserves explanation="该命令执行本地查找，不改变任何远程状态。"}
::option[禁用所有策略路由规则。]{#route-get-disables-policy explanation="该查找会评估策略，而不是移除策略。"}
:::

## 添加或替换路由

通过可达下一跳添加指向规范前缀的路由：

```bash
$ sudo ip route add 192.168.2.0/23 via 10.11.12.3 dev enp1s0
```

根据相关链路或明确有效的链路内设计，网关必须可达。当等效路由已经存在时，`add` 会失败。`replace` 会创建或更改路由，适合幂等配置，但可能覆盖正常状态；应先预览确切目标。

:::single-choice{#route-add-existing} 如果 `ip route add` 的目标路由已经存在，通常会发生什么？

::option[它会静默删除旧目标前缀。]{#route-add-deletes explanation="add 通常会报告对象已存在错误，而不是替换它。"}
::option[它会失败，而不是替换现有路由。]{#route-add-fails .correct explanation="只有审查将更改哪个条目后，才能有意使用 replace。"}
::option[它会重启所选网关。]{#route-add-reboots explanation="本地路由配置无法以这种方式请求远程重启。"}
:::

## 精确删除

当可能存在多个候选项或路由表时，应指定确切路由属性进行删除：

```bash
$ sudo ip route del 192.168.2.0/23 via 10.11.12.3 dev enp1s0
```

只指定目标的删除可能匹配范围过宽或存在歧义。移除前，应记录恢复原路由所需的命令。

:::single-choice{#route-delete-precision} 删除路由时为什么要包含下一跳和设备？

::option[更精确地标识预期条目。]{#route-delete-exact .correct explanation="明确属性可以降低删除同一前缀下其他路由的风险。"}
::option[同时删除物理网络适配器。]{#route-delete-adapter explanation="删除路由不会移除内核链路对象。"}
::option[擦除目标的 DNS 区域。]{#route-delete-dns explanation="路由与权威 DNS 数据属于不同系统。"}
:::

## 持久性与远程安全

`ip route` 命令只更改当前内核状态。NetworkManager、systemd-networkd、netplan、ifupdown、DHCP、路由守护进程或编排系统以后可能替换它。只有测试运行时行为后，才应将路由存入活动所有者。

对于远程主机，应保留独立控制台，并使用不依赖待更改路由的回滚方式。随后验证路由查找、邻居状态、双向流量和实际服务。

:::single-choice{#route-runtime-persistence} 网络管理器重新加载后，手动添加的路由可能发生什么？

::option[它会永久成为不可变的内核功能。]{#route-manual-immutable explanation="运行时路由可以被移除或替换。"}
::option[它会自动出现在子网的每台主机上。]{#route-manual-all-hosts explanation="该命令只更改当前网络命名空间。"}
::option[如果持久策略中没有它，它可能消失。]{#route-manual-disappears .correct explanation="管理器会根据配置文件协调内核状态。"}
:::

## 总结

现在，你可以采用可恢复的工作流程，对 Linux 路由进行范围明确的更改。

1. 记录当前路由、规则和生效查找。
2. 使用规范前缀和可达下一跳。
3. 区分添加与有意替换。
4. 删除确切路由并保留恢复命令。
5. 通过活动管理器持久保存，并验证双向流量。
