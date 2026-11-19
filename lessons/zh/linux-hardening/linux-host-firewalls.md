---
lesson_id: "linux-host-firewalls"
course_id: "linux-hardening"
lang: "zh"
order_index: 5
title: "主机防火墙"
description: "读懂简单的主机防火墙规则，并确定应该从哪些位置测试。"
meta_title: "主机防火墙 - Linux 安全加固"
meta_description: "根据来源、协议和目标端口读懂主机防火墙，并分别核对规则和服务状态。"
meta_keywords: "主机防火墙, HTTPS, SSH, TCP, Linux 安全加固, Linux Journey"
---

**主机防火墙**可以根据来源地址、协议和目标端口等条件，允许或阻止传入的网络流量。先确认服务实际需要接收哪些流量。

## 阅读一份示例规则

以下是某台主机上的简化规则。`192.0.2.0/24` 中的斜杠写法描述一段 IPv4 地址范围。这段范围包含 `192.0.2.44`，不包含 `198.51.100.8`。

```text
Allow TCP port 443 from any source.
Allow TCP port 22 from 192.0.2.0/24.
Deny other new inbound connections.
```

443 端口供公开网站使用。22 端口留给维护网络。默认规则描述的是不符合这两条允许规则的连接。

:::single-choice{#linux-host-firewalls-match-trusted-network} 以下哪个新连接符合维护规则？

::option[来自 198.51.100.8、目标为 TCP 22 端口的连接。]{#linux-host-firewalls-match-trusted-network-b explanation="目标端口符合条件，但来源不在维护网络内。"}
::option[来自 192.0.2.44、目标为 TCP 443 端口的连接。]{#linux-host-firewalls-match-trusted-network-c explanation="该连接符合公开网站的规则。"}
::option[来自 192.0.2.44、目标为 TCP 22 端口的连接。]{#linux-host-firewalls-match-trusted-network-a .correct explanation="目标端口和来源地址范围都符合规则。"}
:::

![模拟的主机防火墙规则允许公开 HTTPS 访问，并限制维护入口](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/linux-hardening/linux-host-firewalls/sample-policy.png)

## 分别检查规则和监听状态

防火墙允许的连接也可能失败，比如没有程序在对应端口监听。反过来，即使程序正在正常监听，请求所走的路径也可能被防火墙挡住。请分别核查防火墙规则和监听情况。

:::single-choice{#linux-host-firewalls-allowed-but-failed} 规则允许 443 端口，但主机上没有程序在这个端口监听。应该检查什么？

::option[客户端是否应该使用维护用的 SSH。]{#linux-host-firewalls-allowed-but-failed-a explanation="那是另一项服务。"}
::option[公开的 Web 服务是否在预期端口监听。]{#linux-host-firewalls-allowed-but-failed-b .correct explanation="防火墙放行不会让程序开始监听。"}
::option[请求是否来自维护网络。]{#linux-host-firewalls-allowed-but-failed-c explanation="这个示例的公开站点规则接受任何来源。"}
:::

## 规划安全的验证方式

核查受控的规则变更时，应保留合法的维护通道。先在维护网络内测试应该允许的路径，再从该网络以外获准测试的位置确认连接被阻止。记录每次测试的来源、目标和预期结果。

:::single-choice{#linux-host-firewalls-verification-pair} 哪组测试能验证预期的 SSH 访问限制？

::option[从维护网络内和网络外获准的位置，分别测试 22 端口。]{#linux-host-firewalls-verification-pair-c .correct explanation="这两次请求分别验证了规则应当允许和应当阻止的情况。"}
::option[从同一台允许访问的机器发起两次 SSH 请求。]{#linux-host-firewalls-verification-pair-a explanation="这只会重复测试允许访问的情况。"}
::option[用浏览器请求两次公开主页。]{#linux-host-firewalls-verification-pair-b explanation="这两次请求测试的是公开端口，和维护访问无关。"}
:::

## 总结

现在，你可以结合服务状态解读主机防火墙规则。

1. 按协议、目标和来源匹配防火墙规则。
2. 确认允许访问的服务确实在监听。
3. 验证预期的访问权限和限制。
