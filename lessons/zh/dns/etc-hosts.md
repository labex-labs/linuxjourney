---
lesson_id: "etc-hosts"
course_id: "dns"
lang: "zh"
order_index: 4
title: "/etc/hosts"
description: "了解本地主机文件映射如何参与 Linux 名称解析，以及如何安全地测试它们。"
meta_title: "/etc/hosts - DNS"
meta_description: "探索 Linux 中 /etc/hosts 文件的用途。了解该文件如何将主机名映射到 IP 地址、它在本地 DNS 解析中的作用，以及如何在 Debian 等系统上进行配置。"
meta_keywords: "/etc/hosts, Linux hosts 文件, Debian hosts, Linux /etc/hosts, 主机映射, Linux 网络, 主机名映射, DNS 解析"
---

`/etc/hosts` 为本地系统的名称服务栈提供静态的地址到名称条目。它适用于回环名称、引导阶段的依赖和范围严格受限的测试，但不会向其他主机发布记录，也不会更新 DNS。

## 读取文件

每行先写一个 IPv4 或 IPv6 地址，后跟一个或多个名称：

```text
127.0.0.1       localhost
192.0.2.25      app-test.example.net app-test
2001:db8::25    app-test-v6.example.net app-test-v6
```

注释以 `#` 开头。按照惯例，一些工具会把第一个名称视为规范名称，后续名称视为别名，但不同应用程序和解析器 API 的行为并不一致。应避免为同一个名称添加重复或冲突的条目。

:::single-choice{#hosts-file-entry-order}
普通 `/etc/hosts` 映射行的第一项是什么？

::option[IP 地址。]{#hosts-file-address-first .correct explanation="同一行中，地址后面跟有一个或多个名称。"}
::option[DNS 记录的 TTL。]{#hosts-file-ttl-first explanation="hosts 文件条目不使用 DNS TTL 字段。"}
::option[传输层端口号。]{#hosts-file-port-first explanation="该文件映射名称与地址，而不是应用程序端口。"}
:::

## 解析器顺序

名称服务切换（Name Service Switch）配置通常位于 `/etc/nsswitch.conf`，它决定系统解析器函数如何组合 `files`、DNS、多播系统和其他来源。常见配置行如下：

```text
hosts: files dns
```

在检查策略前，不要假定文件总是排在第一位。应用程序也可能使用自己的 DNS 库、缓存、代理或加密解析器，从而不遵循系统解析路径。

:::single-choice{#hosts-file-nss-order}
什么决定系统解析器是否先于 DNS 查询 `/etc/hosts`？

::option[`/etc` 中各文件名的字母顺序。]{#hosts-file-alphabetical explanation="文件系统的列出顺序不定义名称服务策略。"}
::option[名称服务切换策略中的来源顺序。]{#hosts-file-nss-policy .correct explanation="`hosts:` 数据库行控制常规 libc 解析器的来源顺序。"}
::option[目标的 TCP 窗口大小。]{#hosts-file-tcp-window explanation="传输层流量控制与本地名称查询无关。"}
:::

## 通过系统解析器测试

使用 `getent` 走一遍已配置的系统名称服务路径：

```bash
$ getent ahosts app-test.example.net
```

`dig` 会直接查询 DNS，通常不显示 `/etc/hosts` 映射。这个差异很有用：如果 `getent` 成功而 `dig` 没有结果，可能意味着本地来源或解析器策略有所不同。

:::single-choice{#hosts-file-getent-versus-dig}
哪种工具更适合检查常规系统解析能否看到 hosts 文件条目？

::option[`dig`，因为它总是先读取 `/etc/hosts`。]{#hosts-file-dig-first explanation="Dig 发送 DNS 查询，绕过 hosts 文件查询路径。"}
::option[`getent ahosts`，因为它使用已配置的名称服务来源。]{#hosts-file-getent .correct explanation="它反映许多原生应用程序使用的解析器路径。"}
::option[`ip route flush`，因为它会重建所有名称。]{#hosts-file-flush-route explanation="清空路由具有破坏性，而且与 hosts 文件查询无关。"}
:::

## 安全编辑

保留必需的 localhost 和主机身份条目，验证目标地址，并通过具备特权的编辑工具进行可恢复的修改。不要为了随手测试而覆盖真实公共域名，这可能意外重定向凭据或应用程序流量。请使用专用测试名称，并在实验结束后删除该条目。

编辑后，应测试实际使用的应用程序，因为它可能保留缓存或采用不同的解析器。记录持久化覆盖项，以免它们在用途结束后仍悄然存在。

:::single-choice{#hosts-file-test-name}
为什么要使用专用测试名称，而不覆盖公共服务名称？

::option[公共名称不能包含点。]{#hosts-file-public-no-dots explanation="域名通常由多个以点分隔的标签组成。"}
::option[专用名称会自动创建权威 DNS 区域。]{#hosts-file-auto-zone explanation="hosts 文件条目只在本地生效，不会发布区域。"}
::option[这能降低重定向真实流量或凭据的风险。]{#hosts-file-reduce-redirection .correct explanation="本地覆盖会影响使用该公共名称的所有系统解析器客户端。"}
:::

## 解析器服务器配置

传统上，`/etc/resolv.conf` 列出 DNS 解析器设置，但它往往由 NetworkManager、systemd-resolved、DHCP 或其他管理器生成。应先检查符号链接和文件注释，然后修改负责生成它的配置源，而不是编辑随后会被覆盖的生成文件。

:::single-choice{#hosts-file-resolv-owner}
编辑 `/etc/resolv.conf` 前应该做什么？

::option[删除 `/etc/hosts` 和所有网络路由。]{#hosts-file-delete-state explanation="这些破坏性操作毫不相关，并且可能导致网络断开。"}
::option[假定每个发行版都直接在该文件中保存永久设置。]{#hosts-file-assume-direct explanation="许多系统会动态生成该文件，或将它链接到受管理的存根文件。"}
::option[确认它是否由其他服务生成和管理。]{#hosts-file-identify-resolver-owner .correct explanation="持久 DNS 服务器变更应写入当前管理器的配置。"}
:::

## 总结

现在，你可以把 `/etc/hosts` 用作受控的本地解析器输入。

1. 以地址开头编写映射，并有意识地选择名称和别名。
2. 检查名称服务切换顺序，不要自行假定。
3. 用 `getent` 测试系统解析，用 `dig` 单独测试 DNS。
4. 使用专用临时名称，并验证实际应用程序。
5. 通过配置所有者修改解析器服务器。
