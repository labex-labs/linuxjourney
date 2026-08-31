---
lesson_id: "dhcp-overview"
course_id: "network-basics"
lang: "zh"
order_index: 9
title: "DHCP 概述"
description: "学习 DHCPv4 如何通过发现、选择和续租来租用地址与网络选项。"
meta_title: "DHCP 概述 - 网络基础"
meta_description: "学习 DHCP（动态主机配置协议）基础。本指南介绍 DHCP 如何分配 IP 地址、DORA 四步流程，以及它在网络中的作用，适合 Linux 网络初学者。"
meta_keywords: "DHCP, 动态主机配置协议, DHCP 层, IP 地址, Linux 网络, DHCP 流程, DORA, 网络配置"
---

动态主机配置协议向客户端提供有租期的网络配置。在 DHCPv4 中，这些配置可以包括 IPv4 地址、子网掩码、默认路由器、DNS 服务器、租期，以及本地策略选择的其他选项。

## 客户端、服务器与中继

DHCP 服务器管理作用域或地址池以及租约状态。服务器不必位于每个物理网段；DHCP 中继可以在子网与集中式服务器之间转发客户端交换。只使用静态配置的网络可能根本不提供 DHCP。

DHCP 是通过 UDP 承载的应用层协议。DHCPv4 服务器通常使用 UDP 端口 67，客户端使用端口 68。

:::single-choice{#dhcp-relay-purpose}
DHCP 中继实现了什么？

::option[让每个客户端不受策略限制地选择任意地址。]{#dhcp-client-any-address explanation="服务器仍然应用作用域和租约策略。"}
::option[让另一个子网中的客户端访问集中式 DHCP 服务器。]{#dhcp-central-server .correct explanation="中继跨越路由边界转发 DHCP 交换，并标识客户端所在网络。"}
::option[让以太网交换机取代所有 IP 路由器。]{#dhcp-switch-router explanation="中继 DHCP 不会消除路由网络边界。"}
:::

## 初始 DHCPv4 交换

常见的初始过程可记为 DORA：

1. `DHCPDISCOVER`：客户端搜索可用服务器。
2. `DHCPOFFER`：服务器提出地址和选项。
3. `DHCPREQUEST`：客户端选择并请求所提供的租约。
4. `DHCPACK`：所选服务器确认租约和选项。

广播与单播细节取决于客户端状态、中继使用情况和服务器能力。要约尚不是最终可用的租约；确认消息会完成正常选择交换。

:::single-choice{#dhcp-dora-order}
DHCPv4 正常的初始顺序是什么？

::option[OFFER、DISCOVER、ACK、REQUEST。]{#dhcp-wrong-order-one explanation="客户端先发现，服务器再提供；客户端先请求，服务器再确认。"}
::option[DISCOVER、OFFER、REQUEST、ACK。]{#dhcp-correct-order .correct explanation="该序列依次执行搜索、提议、选择和确认。"}
::option[REQUEST、ACK、DISCOVER、OFFER。]{#dhcp-wrong-order-two explanation="新客户端通常需要先发现服务器并收到要约，才能选择租约。"}
:::

## 租约续期

租约如果不续期就会过期。客户端通常会在到期前开始续租，往往先直接联系原服务器。如果续租失败，它会在之后扩大重新绑定尝试。具体计时器由协议提供或根据协议推导。

显示为动态分配的地址并不能证明租约永久有效。排查变化时，应记录当前租约、有效期、服务器和选项。

:::single-choice{#dhcp-lease-expiration}
DHCP 地址租约未成功续期时会发生什么？

::option[它会变成永久硬件 MAC 地址。]{#dhcp-lease-mac explanation="IP 租约不会改变链路层身份。"}
::option[它最终会过期，客户端必须停止将其视为有效地址。]{#dhcp-lease-expires .correct explanation="租赁机制允许服务器根据策略回收或更改地址和选项。"}
::option[它会把客户端转换成权威 DNS 根服务器。]{#dhcp-lease-dns-root explanation="DHCP 租约不会授予 DNS 权限。"}
:::

## 检查结果

客户端应用 DHCP 配置后，应验证所有必需状态，而不只是地址：

```bash
$ ip address show
$ ip route show
$ resolvectl status
```

解析器命令因系统而异。还应检查活动网络管理器的租约数据和日志。恶意服务器、地址池内的静态分配、过期状态或手动配置仍可能造成地址重复；DHCP 可以减少错误，但本身无法阻止所有冲突。

:::single-choice{#dhcp-result-verification}
接受 DHCP 租约后应该检查什么？

::option[只检查接口显示名称。]{#dhcp-interface-name-only explanation="接口名称不能确定寻址、路由或解析状态。"}
::option[只检查键盘是否响应。]{#dhcp-keyboard explanation="键盘输入与网络租约配置无关。"}
::option[检查地址、路由、DNS 和租约详情。]{#dhcp-check-complete-state .correct explanation="可用配置取决于多个选项及其在系统中应用后的状态。"}
:::

## DHCPv6 与 IPv6 配置

IPv6 主机可以使用无状态地址自动配置、DHCPv6、静态配置或这些方式的组合。DHCPv6 不使用 IPv4 的 DORA 交换，默认路由器信息通常来自 IPv6 路由器通告，而不是 DHCPv6。

:::single-choice{#dhcp-ipv6-default-router}
IPv6 主机通常从哪里获得默认路由器信息？

::option[IPv6 路由器通告。]{#dhcp-router-advertisement .correct explanation="DHCPv6 可以提供其他配置，但路由器通过邻居发现通告自身。"}
::option[以太网 FCS 尾部。]{#dhcp-ipv6-fcs explanation="FCS 用于检测链路损坏，不承载路由器配置。"}
::option[仅来自 IPv4 DHCPACK。]{#dhcp-ipv4-ack explanation="IPv4 DHCP 消息不会配置 IPv6 路由。"}
:::

## 总结

现在，你可以解释 DHCPv4 如何租用并续订主机网络配置。

1. 区分 DHCP 服务器、中继和客户端子网。
2. 理解 DISCOVER、OFFER、REQUEST 和 ACK 交换。
3. 将地址和选项视为有期限的租约状态。
4. 一并验证地址、路由、DNS 和租约元数据。
5. 将 DHCPv4 行为与 IPv6 自动配置区分开。
