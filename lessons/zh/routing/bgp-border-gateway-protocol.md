---
lesson_id: "bgp-border-gateway-protocol"
course_id: "routing"
lang: "zh"
order_index: 7
title: "边界网关协议"
description: "学习 BGP 如何在自治系统之间和内部交换受策略控制的 IP 可达性。"
meta_title: "边界网关协议 - 路由"
meta_description: "探索互联网路由核心协议边界网关协议（BGP）的基础。了解 BGP 如何促进自治系统之间的通信，以及边界网关协议路由的原理。"
meta_keywords: "BGP, 边界网关协议, 边界网关协议路由, 互联网路由, 自治系统, Linux 网络, BGP 教程, 网络协议"
---

边界网关协议是互联网的路径矢量路由协议。它交换 IP 前缀可达性和路径属性，使网络能够应用管理策略，而不是只根据物理距离选择路由。

## 自治系统与会话

自治系统是在共同路由管理下的一组网络，BGP 使用自治系统编号标识它。外部 BGP 在自治系统之间交换路由；内部 BGP 则在同一个 AS 内分发 BGP 可达性。

BGP 对等方通过 TCP 端口 179 建立会话。正常工作的 TCP 会话只是传输基础；BGP 能力、策略和路由交换也必须成功。

:::single-choice{#bgp-external-session} 外部 BGP 交换什么？

::option[一台交换机内部的以太网帧校验和。]{#bgp-ethernet-fcs explanation="BGP 运行在 TCP 之上，交换网络层可达性。"}
::option[Web 浏览器之间的用户密码。]{#bgp-browser-passwords explanation="应用程序凭据不是路由属性。"}
::option[自治系统之间的可达性和路径信息。]{#bgp-between-as .correct explanation="eBGP 连接不同的路由管理域，并应用域间策略。"}
:::

## 路径矢量信息

一条通告包含前缀和属性。`AS_PATH` 列出经过的自治系统，并帮助检测环路。其他常见属性包括 `LOCAL_PREF`、`MED`、起源、下一跳和团体属性。其作用取决于方向、实现和策略。

:::single-choice{#bgp-as-path-loop} `AS_PATH` 如何帮助防止自治系统间环路？

::option[AS 可以拒绝已经包含自身编号的路径。]{#bgp-own-as-reject .correct explanation="路径矢量公开到达所通告前缀时经过的 AS 序列。"}
::option[它会加密穿越这些系统的每个数据包。]{#bgp-aspath-encryption explanation="该属性描述路由路径，不提供载荷加密。"}
::option[它为每个 AS 分配 MAC 地址。]{#bgp-aspath-mac explanation="自治系统编号与链路地址属于不同命名空间。"}
:::

## 基于策略的选择

BGP 的“最佳”路径是配置的决策流程中胜出的路径。运营方可以偏好客户路由、更改本地偏好、过滤前缀、使用团体属性并应用流量工程策略。较短的 `AS_PATH` 可能在某一步有影响，但不会普遍覆盖优先级更高的属性。

BGP 选出候选项后，普通 IP 转发仍使用最长前缀匹配。对于相应目标，选中的 `/24` 会优先于覆盖它的 `/16`。

:::single-choice{#bgp-best-path-meaning} BGP 最佳路径表示什么？

::option[在本地属性与策略决策流程中胜出的路由。]{#bgp-policy-winner .correct explanation="管理意图是域间路径选择的核心。"}
::option[在每种情况下物理电缆距离最短的路由。]{#bgp-shortest-cable explanation="BGP 没有完整的物理距离图。"}
::option[保证当前应用程序延迟最低。]{#bgp-lowest-latency explanation="BGP 选择默认不会持续优化最终用户延迟。"}
:::

## 通告与可达性

通告前缀是在策略下声明可达性；它不会创建底层路由，也不能确保返回路径。发起前缀前，应确保转发有效、聚合行为正确、过滤与故障转移就绪，并且拥有授权。

:::single-choice{#bgp-advertisement-limit} 通告前缀无法保证什么？

::option[对等方能够收到控制平面路由。]{#bgp-peers-control explanation="成功通告并被接受可以确定这一有限的控制平面事实。"}
::option[前缀包含地址位。]{#bgp-prefix-bits explanation="IP 前缀由地址位和长度定义。"}
::option[能够为整个前缀传送数据包。]{#bgp-data-plane-not-guaranteed .correct explanation="底层路由、下一跳、过滤和服务健康仍需验证。"}
:::

## 路由安全与变更控制

路由泄漏和劫持可能影响远超一台路由器的流量。运营方会使用严格的导入和导出过滤器、最大前缀限制、对等策略、监控，以及适当的资源公钥基础设施起源验证。RPKI 起源验证检查某个 AS 是否有权发起前缀，但不会验证完整 AS 路径。

BGP 变更需要分阶段推出、审查路由差异、保留带外访问和回滚，并验证控制平面与数据平面。

:::single-choice{#bgp-rpki-limit} RPKI 起源验证检查什么？

::option[每个数据包载荷是否不含恶意软件。]{#bgp-payload-malware explanation="RPKI 不检查应用程序内容。"}
::option[完整 AS 路径是否具有最低延迟。]{#bgp-path-latency explanation="起源验证不是性能选择或完整路径验证。"}
::option[起源 AS 是否获得授权。]{#bgp-origin-authorized .correct explanation="它验证起源授权，而不是 AS 路径中的每项传输关系。"}
:::

## 总结

现在，你可以将 BGP 描述为受策略控制的路径矢量路由。

1. 区分外部与内部 BGP 会话。
2. 使用 `AS_PATH` 获取路径和环路信息。
3. 通过本地属性和策略解释最佳路径。
4. 验证每个通告前缀背后的转发。
5. 应用过滤、起源验证、监控和回滚。
