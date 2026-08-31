---
lesson_id: "netstat"
course_id: "troubleshooting"
lang: "zh"
order_index: 4
title: "netstat"
description: "了解如何使用 ss 检查 Linux 套接字、监听器、队列和 TCP 状态。"
meta_title: "netstat - 故障排除"
meta_description: "掌握 Linux netstat 命令，分析网络连接、端口和套接字。本指南介绍 SYN-SENT 和 CLOSE-WAIT 等常见状态，帮助你有效排查故障。"
meta_keywords: "Linux netstat, netstat, netstat 命令, SYN-SENT netstat, netstat CLOSE-WAIT, 网络连接, Linux 网络, 网络分析, Linux 教程"
---

传统的 `netstat` 工具显示套接字、路由和接口统计信息。在现代 Linux 中，`ss` 是首选的套接字检查工具，因为它能高效显示内核套接字状态，并随 iproute2 持续维护。

## 列出监听套接字

以数字形式显示监听中的 TCP 和 UDP 套接字，并在权限允许时显示所属进程：

```bash
$ sudo ss -lntup
```

`-l` 选择监听器，`-n` 避免名称查询，`-t` 和 `-u` 分别选择 TCP 与 UDP，`-p` 请求进程数据。UDP 是无连接协议，因此未连接但已绑定的 UDP 套接字没有 TCP 风格的 `LISTEN` 握手。

:::single-choice{#netstat-ss-numeric}
排查套接字问题时为什么使用 `-n`？

::option[它会创建新的网络命名空间。]{#netstat-new-namespace explanation="该选项控制输出中的名称解析。"}
::option[它会阻止地址和端口名称查询。]{#netstat-numeric-output .correct explanation="数字输出避免把服务名映射与观察到的协议身份混淆。"}
::option[它会关闭所有非监听套接字。]{#netstat-close-sockets explanation="检查操作不会终止套接字。"}
:::

## 端口、端点与服务

本地套接字端点由地址、传输协议和端口组合而成。一个 TCP 连接由协议、源地址与端口以及目的地址与端口共同区分。`/etc/services` 把约定俗成的名称映射为数字，但不能证明当前由哪个进程占用某个端口，也不能证明该进程实际使用哪种应用层协议。

:::single-choice{#netstat-services-file-limit}
`/etc/services` 中的 `https 443/tcp` 条目能确定什么？

::option[当前有一台健康的 HTTPS 服务器正在监听。]{#netstat-healthy-listener explanation="静态名称数据库无法证明运行时状态。"}
::option[该端口约定俗成的服务名映射。]{#netstat-conventional-name .correct explanation="套接字所有者与实际协议行为需要运行时检查和测试。"}
::option[所有 443 端口流量都已正确加密。]{#netstat-all-encrypted explanation="端口号无法验证 TLS 行为。"}
:::

## 解读 TCP 状态

常见状态包括：

- `SYN-SENT`：本地端点已发送连接请求，正在等待后续进展。
- `ESTAB`：TCP 连接已经建立。
- `CLOSE-WAIT`：对端已关闭其发送方向，但本地应用程序尚未关闭套接字。
- `TIME-WAIT`：主动关闭连接的端点等待延迟报文段过期，并确保最终交换得到安全处理。

大量或持续增长的 `CLOSE-WAIT` 往往指向本地应用程序的清理行为。`TIME-WAIT` 是正常的协议状态；其数量和资源影响决定它在运维上是否值得担忧。

:::single-choice{#netstat-close-wait-owner}
套接字处于 `CLOSE-WAIT` 时，哪一方仍需将其关闭？

::option[互联网上的每一台路由器。]{#netstat-all-routers-close explanation="路由器并不拥有端点套接字。"}
::option[DNS 权威服务器。]{#netstat-dns-close explanation="名称服务与本地 TCP 关闭处理无关。"}
::option[本地应用程序。]{#netstat-local-close .correct explanation="TCP 已收到对端的 FIN，正在等待本地进程关闭己方套接字。"}
:::

## 解读队列

`Recv-Q` 和 `Send-Q` 的含义取决于状态与协议。在已建立的 TCP 套接字上，它们可以表示等待应用程序接收或等待确认传输的数据；在监听套接字上，队列字段描述的是连接积压状态，含义不同于应用程序载荷字节。

单次快照无法证实泄漏或瓶颈。应持续采样，并结合进程行为、应用程序延迟、重传和资源限制进行分析。

:::single-choice{#netstat-queue-snapshot}
为什么单次出现较大的套接字队列不足以完成诊断？

::option[Linux 从不在套接字队列中存储数据。]{#netstat-no-queues explanation="内核网络功能依赖发送和接收队列。"}
::option[每个队列值都是一种文件系统权限。]{#netstat-queue-permission explanation="这些字段描述网络状态。"}
::option[评估队列影响需要状态、趋势和工作负载上下文。]{#netstat-queue-context .correct explanation="短暂突发不同于持续的应用程序或网络瓶颈。"}
:::

## 筛选调查范围

将输出限制到相关协议、状态、端点或进程：

```bash
$ ss -tn state established
$ ss -ltn 'sport = :443'
```

监听器只能证明本地传输层已经就绪，无法证明远程可达性或应用程序健康。随后应根据症状执行适当的路由、防火墙、数据包、TLS 和应用程序测试。

:::single-choice{#netstat-listener-limit}
443 端口上的 TCP 监听器无法证明什么？

::option[某个本地套接字成功执行了绑定和监听操作。]{#netstat-listen-local explanation="这正是所显示的本地状态。"}
::option[远程客户端可以完成有效的 HTTPS 请求。]{#netstat-not-remote-proof .correct explanation="路径策略、TLS 和应用程序行为都尚未经过测试。"}
::option[TCP 含有数字端口字段。]{#netstat-port-field explanation="监听器输出会直接显示该字段。"}
:::

## 总结

现在，你可以使用 `ss` 检查套接字状态，而不会把端口与应用程序混为一谈。

1. 以数字形式列出监听器及进程上下文。
2. 区分约定俗成的服务名称与运行时所有者。
3. 从本地端点视角解读 TCP 关闭状态。
4. 结合工作负载上下文持续采样队列。
5. 越过本地监听器，验证远程应用程序行为。
