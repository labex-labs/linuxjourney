---
lesson_id: "dns-tools"
course_id: "dns"
lang: "zh"
order_index: 6
title: "DNS 工具"
description: "了解如何使用 getent、resolvectl 和 dig 比较系统解析与直接 DNS 查询。"
meta_title: "DNS 工具 - DNS"
meta_description: "探索 nslookup 和强大的 dig 命令等重要 Linux DNS 工具。这份初学者友好的 Linux 教程介绍 DNS 查询与 DNS 故障排除技术。"
meta_keywords: "nslookup, dig 命令, DNS 工具, Linux DNS, DNS 故障排除, 名称服务器查询, Linux 教程, 初学者 Linux"
---

DNS 故障排除首先要明确正在测试哪一层。系统解析器工具会纳入本地文件和策略，而 `dig` 与 `nslookup` 会发送 DNS 查询，并可直接指定某台服务器。

## 测试系统解析器

使用以下命令走正常的主机名称服务路径：

```bash
$ getent ahosts www.example.com
```

在使用 systemd-resolved 的主机上，可以用以下命令检查每条链路的服务器、搜索域和协议状态：

```bash
$ resolvectl status
$ resolvectl query www.example.com
```

应用程序仍可能使用私有解析器库或代理，所以当输出不同时，还应通过该应用程序重现问题。

:::single-choice{#dns-tools-system-resolver}
哪个命令会使用已配置的系统名称服务路径？

::option[只有 `dig @SERVER NAME`。]{#dns-tools-dig-direct explanation="Dig 发送 DNS 查询，通常不会读取 hosts 文件映射。"}
::option[`ip link set down`]{#dns-tools-link-down explanation="这会中断接口，而不是测试解析。"}
::option[`getent ahosts NAME`]{#dns-tools-getent .correct explanation="它可以反映 `/etc/hosts`、DNS 和其他名称服务切换来源。"}
:::

## 使用 dig 查询

指定名称和记录类型：

```bash
$ dig www.example.com A
$ dig www.example.com AAAA
$ dig example.com MX
```

输出会标识响应服务器、状态、标志、问题、回答、权威数据、附加数据、查询时间和传输元数据。`+short` 便于脚本使用，却隐藏了诊断所需的证据。

:::single-choice{#dns-tools-record-type}
哪条查询请求 IPv6 地址记录？

::option[`dig NAME AAAA`]{#dns-tools-aaaa .correct explanation="AAAA 记录包含 IPv6 地址。"}
::option[`dig NAME MX`]{#dns-tools-mx explanation="MX 请求邮件交换器记录。"}
::option[对正向名称执行 `dig NAME PTR`。]{#dns-tools-ptr-forward explanation="PTR 通常通过反向查询名称进行查询。"}
:::

## 选择服务器

明确指定某个解析器或权威服务器：

```bash
$ dig @192.0.2.53 www.example.com A
```

在区分缓存与权威时，应比较已配置的递归解析器、第二个获准解析器和每台权威服务器。`NOERROR` 状态也可能没有所请求的回答；`NXDOMAIN` 表示查询的名称不存在，而 `SERVFAIL` 表示服务器无法完成查询。

:::single-choice{#dns-tools-noerror-empty}
`NOERROR` 的回答区可以为空吗？

::option[可以，名称存在但缺少所请求的记录数据时便会如此。]{#dns-tools-noerror-nodata .correct explanation="必须结合状态与回答数量进行解释。"}
::option[不可以，它保证至少有一条地址记录。]{#dns-tools-noerror-always-answer explanation="名称可能存在，但没有请求类型的数据。"}
::option[不可以，空回答始终是以太网故障。]{#dns-tools-empty-ethernet explanation="有效的无数据响应由 DNS 语义解释，而不是链路成帧故障。"}
:::

## 检查递归与权威

查询中的 `rd` 表示请求递归；响应中的 `ra` 表示服务器提供递归服务；`aa` 表示回答具有权威性。使用 `+norecurse` 查询权威服务器，以免把递归缓存与服务器提供的区域数据混淆。

`dig +trace NAME` 从根提示开始自行执行迭代查询。它可能与生产解析器得出不同结果，因为它绕过了该解析器的缓存、转发、策略、DNSSEC 验证和网络位置。

:::single-choice{#dns-tools-aa-flag}
`aa` 响应标志表示什么？

::option[查询使用了两个相同的 IPv4 地址。]{#dns-tools-two-addresses explanation="该标志与回答数量或地址族无关。"}
::option[响应使用应用程序凭据加密。]{#dns-tools-aa-encrypted explanation="DNS 标志无法建立加密传输。"}
::option[回答具有权威性。]{#dns-tools-authoritative-answer .correct explanation="响应服务器声明自己对回答数据具有权威。"}
:::

## 测试反向查询与 TCP 查询

使用 `-x` 构造反向 PTR 查询：

```bash
$ dig -x 192.0.2.25
```

调查截断、区域传送或防火墙差异时，测试基于 TCP 的 DNS：

```bash
$ dig +tcp @192.0.2.53 example.com SOA
```

现代 DNS 可以使用 UDP 或 TCP 53 端口；需要时应同时放行两者。带有截断标志的 UDP 回答会促使合规客户端通过合适的传输方式重试。

:::single-choice{#dns-tools-tcp-test}
`dig +tcp` 改变了什么？

::option[它使用 TCP 发送 DNS 查询，而不是默认先尝试 UDP。]{#dns-tools-use-tcp .correct explanation="这有助于区分传输过滤问题，以及需要更大可靠字节流的响应。"}
::option[它只请求 TCP 服务名称记录。]{#dns-tools-tcp-records explanation="请求的 DNS 类型仍需另行指定。"}
::option[它会永久更改服务器的解析器配置。]{#dns-tools-tcp-persistent explanation="查询不会编辑服务器设置。"}
:::

## 总结

现在，你可以选择与待调查解析器层级相匹配的 DNS 工具。

1. 使用 `getent` 测试已配置的系统解析器路径。
2. 使用 `dig` 明确指定记录类型和服务器。
3. 结合状态、标志、各区段和响应服务器进行解释。
4. 将递归缓存与权威数据区分开来。
5. 测试反向查询和两种必需的 DNS 传输方式。
