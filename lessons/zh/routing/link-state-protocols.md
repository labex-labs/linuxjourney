---
lesson_id: "link-state-protocols"
course_id: "routing"
lang: "zh"
order_index: 6
title: "链路状态协议"
description: "学习链路状态协议如何建立邻接关系、泛洪拓扑信息并计算路径。"
meta_title: "链路状态协议 - 路由"
meta_description: "了解适用于大型网络的 OSPF 等链路状态协议，理解它们如何快速收敛和更新路由表，开启 Linux 网络学习之旅。"
meta_keywords: "链路状态协议, OSPF, Linux 网络, 路由协议, 网络拓扑, 初学者"
---

链路状态协议描述本地链路和前缀，在一定路由作用范围内分发这些描述，并让每台路由器根据拓扑数据库计算路径。OSPF 和 IS-IS 是常见示例。

## 建立邻接关系

路由器发现兼容邻居，并根据接口类型、区域、计时器、身份验证和其他参数建立协议邻接关系。看到 hello 数据包并不保证已经形成完整邻接关系；配置不匹配可能让状态机提前停止。

:::single-choice{#link-state-hello-limit} 收到 OSPF hello 无法证明什么？

::option[路由器已经形成完全同步的邻接关系。]{#link-state-not-full .correct explanation="区域、计时器、身份验证、MTU 和其他状态都可能阻止完整数据库交换。"}
::option[邻居至少发送过一条协议消息。]{#link-state-hello-sent explanation="收到 hello 可以直接证明这一有限事实。"}
::option[接口能够接收帧。]{#link-state-frame-received explanation="收到该数据包证明部分本地接收路径正常。"}
:::

## 泛洪链路状态信息

每台路由器都会发出有关自身相关状态的通告。邻居会在规定的区域或域内可靠地泛洪较新的信息，而不只是在最初的一对邻居之间保留更新。序列和老化机制用于区分当前信息并移除过期状态。

:::single-choice{#link-state-flooding-scope} 为什么链路状态信息要泛洪到一个邻居之外？

::option[每个应用程序都需要所有路由器密码的副本。]{#link-state-password-copy explanation="应用程序凭据不是拓扑通告。"}
::option[以太网无法发送单播帧。]{#link-state-no-unicast explanation="以太网支持单播；这里的泛洪是路由协议分发机制。"}
::option[路由作用范围内的路由器需要一致的拓扑数据库。]{#link-state-consistent-database .correct explanation="每台路由器都根据共享的当前链路状态通告集合计算路径。"}
:::

## 计算最短路径

建立链路状态数据库后，路由器以自身为根运行最短路径优先算法，通常是 Dijkstra 算法。OSPF 会累加接口开销；策略和等价开销规则影响最终安装哪些结果。

“最短”指协议开销之和最低，并不一定表示路由器最少或实测应用程序延迟最低。开销设计必须反映运维意图。

:::single-choice{#link-state-shortest-meaning} 链路状态路径计算中的“最短”是什么意思？

::option[前缀书写字符最少的路由。]{#link-state-shortest-text explanation="文本长度与拓扑开销无关。"}
::option[协议开销总和最小的路径。]{#link-state-lowest-cost .correct explanation="开销模型不一定直接对应跳数或当前延迟。"}
::option[始终零丢包的路径。]{#link-state-zero-loss explanation="计算出的路由不能保证应用程序性能。"}
:::

## 区域与收敛

OSPF 区域会限制拓扑泛洪和计算范围，在正常区域间设计中，区域 0 充当骨干。汇总和区域类型可以有意让不同路由器拥有不同的数据库细节。

链路变化后，检测、通告泛洪、SPF 计算、路由安装和转发恢复都需要时间。它可以比简单距离矢量设计更快地收敛，但并非在每种故障或配置下都自动如此。

:::single-choice{#link-state-convergence-stages} 调查 OSPF 收敛时应该测量什么？

::option[只测量管理员打开终端的时间。]{#link-state-terminal-time explanation="这无法隔离协议或转发阶段。"}
::option[只检查路由器名称的字母顺序。]{#link-state-router-names explanation="名称不决定收敛时间。"}
::option[检测、泛洪、计算、安装和转发恢复。]{#link-state-all-stages .correct explanation="分离各阶段可以揭示收敛延迟或故障发生在哪里。"}
:::

## 总结

现在，你可以从邻居发现一直跟踪到链路状态路由安装路径。

1. 区分收到 hello 与形成完整邻接关系。
2. 解释路由作用范围内的可靠泛洪。
3. 将最短路径理解为配置的协议开销最低。
4. 测量控制平面和数据平面的每个收敛阶段。
