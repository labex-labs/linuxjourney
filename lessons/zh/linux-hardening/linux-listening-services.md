---
lesson_id: "linux-listening-services"
course_id: "linux-hardening"
lang: "zh"
order_index: 4
title: "监听服务"
description: "学习如何读懂 Linux 的监听地址，并判断从什么位置测试能否访问服务。"
meta_title: "监听服务 - Linux 安全加固"
meta_description: "从 ss 输出识别 TCP 监听地址，区分回环与所有接口，并验证用户实际使用的路径。"
meta_keywords: "监听服务, ss, TCP 端口, 回环地址, Linux 安全加固, Linux Journey"
---

服务可以在特定地址和端口等待连接。准备接收传入连接的**监听套接字**就叫监听项。它使用的地址可以帮助判断哪些设备有可能访问到服务。

## 列出 TCP 监听项

在 Linux 练习主机上运行下面这条只读命令。选项要求 `ss` 显示处于监听状态的 TCP 套接字，用数字表示地址和端口。

```bash
$ ss -lnt
```

查看本地地址列。下面的例子用 `127.0.0.1:8091` 提供网页预览。端口是 8091，这个地址是**回环地址**，指向主机本身。

:::single-choice{#linux-listening-services-local-listener} 这个例子中，同一台主机上的浏览器要打开预览。应该尝试哪个地址？

::option[0.0.0.0:8091。]{#linux-listening-services-local-listener-a explanation="这种写法描述监听范围，而示例中的本地目标有一个具体地址。"}
::option[127.0.0.1:8091。]{#linux-listening-services-local-listener-b .correct explanation="服务正在这个回环地址和端口上监听。"}
::option[另一台不相关服务器的 80 端口。]{#linux-listening-services-local-listener-c explanation="示例中的监听项在其本机使用 8091 端口。"}
:::

![记录自 LabEx 的 ss 输出显示练习服务在回环地址的 8091 端口监听](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/linux-hardening/linux-listening-services/loopback-listener.png)

## 理解监听所有接口

IPv4 本地地址显示为 `0.0.0.0:8091`，意味着服务在主机的所有 IPv4 接口上监听。这些接口可以包括其他计算机能够访问的接口。监听列表只描述进程在本机接受哪些连接。防火墙规则和网络路由还会限制另一台计算机能访问哪些地址。

:::single-choice{#linux-listening-services-all-interfaces} 服务在同一个端口上把监听地址从 127.0.0.1 改为 0.0.0.0。什么发生了变化？

::option[它可以在更多 IPv4 接口上监听。]{#linux-listening-services-all-interfaces-a .correct explanation="这个设置扩大了服务能接受入站连接的本地地址范围。"}
::option[现在监听的端口不同了。]{#linux-listening-services-all-interfaces-b explanation="端口号没有变化。"}
::option[任何网络现在都能立刻访问它。]{#linux-listening-services-all-interfaces-c explanation="哪些路径能访问服务，仍取决于网络规则和路由。"}
:::

## 检查预期的访问路径

供员工使用的内部服务可能只允许从某个网络访问。请先在该网络中验证。如果需要证明限制有效，再从获准测试的外部位置核查。监听状态和实际路径都要确认。只看本地列表，无法知道远端客户端会遇到什么。

:::single-choice{#linux-listening-services-verify-from-client} 你看到某个服务在所有本地接口上监听。哪项检查能告诉你员工电脑是否可以访问它？

::option[再读一遍主机名。]{#linux-listening-services-verify-from-client-a explanation="主机名无法测试网络路径。"}
::option[数一下机器上有多少监听项。]{#linux-listening-services-verify-from-client-b explanation="数量无法说明员工电脑能不能访问。"}
::option[从员工网络发出经批准的测试请求。]{#linux-listening-services-verify-from-client-c .correct explanation="这样可以测试员工实际使用的路径。"}
:::

要检查 Linux 主机上有哪些服务在监听，可以从 [面向 DevSecOps 的 Linux 安全](https://labex.io/courses/linux-security-for-devsecops)中的监听服务审计实验开始。

## 总结

现在，你可以先读懂监听地址，再决定从哪里测试访问。

1. 安全地列出本机的 TCP 监听项。
2. 区分仅监听回环地址和监听所有 IPv4 接口。
3. 从相关客户端位置验证连接。
