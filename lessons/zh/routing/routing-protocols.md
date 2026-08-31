---
lesson_id: "routing-protocols"
course_id: "routing"
lang: "zh"
order_index: 4
title: "路由协议"
description: "学习动态路由协议如何交换可达性信息，并收敛到可用的转发路径。"
meta_title: "路由协议 - 路由"
meta_description: "探索 Linux 网络中的路由协议基础。本指南介绍距离矢量和链路状态协议、网络收敛，以及路由器如何构建和维护路由表，适合初学者。"
meta_keywords: "路由协议, 网络收敛, 距离矢量, 链路状态, Linux 网络, 路由表, 网络教程, 初学者指南, 路由器通信"
---

静态路由由管理员直接配置，动态路由协议则交换可达性和拓扑信息，使路由器能够适应变化。动态学习可以减少手工工作，但也会引入必须监控的协议状态、信任边界、计时器和故障模式。

## 控制平面与转发平面

路由协议在自己的数据库中学习候选路由。路由器将路由选入路由信息库，再把可用下一跳安装到转发表。随后，硬件或内核根据该表转发数据包。

协议邻接关系已经建立，并不能证明所需前缀已经学习、选中、安装，或已获得转发策略允许。

:::single-choice{#routing-protocols-adjacency-limit}
路由邻接关系已经建立，无法证明什么？

::option[每条所需路由都已安装并成功转发。]{#routing-protocols-not-full-proof .correct explanation="路由通告、选择、安装、过滤和数据平面运行是不同阶段。"}
::option[两个协议发言者交换过控制消息。]{#routing-protocols-no-messages explanation="建立邻接关系通常需要协议通信。"}
::option[存在控制平面。]{#routing-protocols-no-control explanation="邻接关系本身就是控制平面状态。"}
:::

## 内部路由与外部路由

内部网关协议在一个管理路由域内运行，例如 RIP、OSPF 和 IS-IS。BGP 在自治系统内部及自治系统之间交换受策略控制的可达性，是互联网的外部路由协议。

度量值具有协议特有的含义。OSPF 开销、RIP 跳数和 BGP 属性集不能像共享统一数值尺度一样直接比较。实现会在协议特定选择之前或同时，使用路由偏好或管理距离在不同来源之间作出选择。

:::single-choice{#routing-protocols-metric-comparison}
可以直接比较 RIP 跳数与 OSPF 开销吗？

::option[可以，因为所有路由度量都使用相同单位。]{#routing-protocols-universal-metric explanation="每种协议都定义自己的度量和选择过程。"}
::option[可以，但仅当两个值都为零时。]{#routing-protocols-zero-metric explanation="无论显示的数字是什么，其语义都不相同。"}
::option[不可以；它们具有协议特有的含义。]{#routing-protocols-specific-metric .correct explanation="不同来源之间的选择使用实现策略，而不是把不同度量当作同一尺度。"}
:::

## 距离矢量与链路状态

距离矢量协议通过邻居通告可达性和距离，并根据邻居报告推导路径。链路状态协议建立邻接关系、在一定作用范围内泛洪链路状态信息、构建拓扑数据库，再计算最短路径树。现代协议包含许多改进，简单的类别概述无法涵盖全部细节。

:::single-choice{#routing-protocols-link-state-input}
链路状态路由器使用什么进行路径计算？

::option[只使用默认网关的主机名。]{#routing-protocols-hostname-only explanation="拓扑计算需要链路和前缀信息。"}
::option[描述路由作用范围内链路的同步数据库。]{#routing-protocols-link-database .correct explanation="路由器在学习到的拓扑上运行最短路径算法。"}
::option[每台主机的应用层密码。]{#routing-protocols-passwords explanation="路由拓扑交换不需要最终用户凭据。"}
:::

## 收敛

拓扑或策略变化后，路由器会检测变化、传播控制信息、计算路径并更新转发状态。收敛是网络为受影响目标达到稳定且彼此可用路由的过程和结果。它不要求每台路由器拥有完全相同的完整路由表；角色和策略可以有意造成差异。

收敛期间可能出现短暂丢包、环路或黑洞。应分别测量检测、传播、计算和安装过程，并使用数据平面探测进行验证。

:::single-choice{#routing-protocols-convergence}
什么是路由收敛？

::option[变化后达到稳定可用路由的过程。]{#routing-protocols-stable-routing .correct explanation="它包括控制信息传播以及最终的转发更新。"}
::option[要求每台路由器存储完全相同的全局路由表。]{#routing-protocols-identical-table explanation="策略、区域和角色可以造成有意差异。"}
::option[永久防止一切可能的路由故障。]{#routing-protocols-no-failure explanation="已收敛的网络仍可能存在策略或容量问题。"}
:::

## 总结

现在，你可以理解动态路由信息从协议交换到转发的完整过程。

1. 区分学习到的候选项、选中的路由和转发条目。
2. 区分内部路由与 BGP 策略交换。
3. 只在协议自身语义内比较度量值。
4. 在控制平面和数据平面中验证收敛。
