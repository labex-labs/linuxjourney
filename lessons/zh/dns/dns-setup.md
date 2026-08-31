---
lesson_id: "dns-setup"
course_id: "dns"
lang: "zh"
order_index: 5
title: "DNS 设置"
description: "了解如何选择、保护、验证和运维权威或递归 DNS 服务。"
meta_title: "DNS 设置 - DNS"
meta_description: "了解 BIND、dnsmasq 和 PowerDNS 等常用 Linux DNS 服务器。通过初学者友好指南，为你的网络配置选择合适的 DNS 服务器。"
meta_keywords: "Linux DNS, BIND, dnsmasq, PowerDNS, DNS 服务器设置, Linux 网络, DNS 教程, 初学者"
---

应根据角色和运维需求选择 DNS 软件，而不是寻找一个放之四海而皆准的“最佳服务器”。权威服务发布区域；递归服务通过解析和缓存回答客户端；转发解析器则把查询发送给另一个解析器。组合多种角色会改变攻击面。

## 选择角色与实现

- BIND 可以提供权威和递归服务，并广泛支持各项标准。
- Unbound 常被部署为执行验证的递归解析器。
- dnsmasq 为规模较小且受控的网络提供轻量级转发、缓存和 DHCP 功能。
- PowerDNS 分别提供权威产品与递归产品，并支持多种数据后端。

功能和软件包会发生变化，因此请查阅已安装版本的官方文档。只部署需要的角色，并禁用非预期的递归查询或区域服务。

:::single-choice{#dns-setup-authoritative-role}
哪种角色会为其服务的区域发布最终记录？

::option[权威 DNS 服务器。]{#dns-setup-authoritative .correct explanation="它从已配置的区域权威中作答，而不是递归查找任意名称。"}
::option[以太网交换机。]{#dns-setup-switch explanation="交换机转发链路层帧，并不发布 DNS 区域。"}
::option[回答任意客户端查询的递归解析器。]{#dns-setup-stub explanation="存根解析器向递归服务发送查询，并不托管权威区域。"}
:::

## 安装前设计

明确区域、客户端、查询量、更新机制、DNSSEC 需求、日志、监控、备份与恢复方案。权威区域需要冗余服务器和正确注册的委派。递归服务需要明确的客户端访问控制、缓存策略、上游或迭代查询连通性，以及防滥用措施。

绝不要向互联网开放不受限制的递归查询。开放解析器可能被用于反射攻击，并消耗本地资源。

:::single-choice{#dns-setup-open-recursion}
为什么要将递归查询限制给获准客户端？

::option[递归 DNS 无法缓存任何记录。]{#dns-setup-no-cache explanation="缓存是递归解析器的核心功能。"}
::option[权威委派要求每位用户都是 root。]{#dns-setup-all-root explanation="DNS 委派不会授予操作系统权限。"}
::option[开放递归查询可能被用于放大攻击和资源消耗。]{#dns-setup-recursion-abuse .correct explanation="访问控制可以减少解析器被用作公共攻击基础设施的风险。"}
:::

## 验证配置与区域数据

重新加载前，使用相应实现的语法检查工具和区域检查工具。对于 BIND，常见示例如下：

```bash
$ named-checkconf
$ named-checkzone example.com /etc/bind/zones/db.example.com
```

请使用适合该主机的权限和路径运行。解析器检查成功并不能证明委派、序列号传播、DNSSEC 信任链、防火墙连通性或回答正确，因此还要进行受控查询。

:::single-choice{#dns-setup-zone-validation-limit}
区域语法检查成功无法证明什么？

::option[委派和端到端权威回答正常工作。]{#dns-setup-not-end-to-end .correct explanation="父区域数据、服务激活、网络策略和运行时加载仍是彼此独立的环节。"}
::option[检查器可以解析区域文本。]{#dns-setup-parser-proves explanation="这正是检查器直接提供的证据。"}
::option[文件中的记录含有所有者字段。]{#dns-setup-record-owner explanation="解析有效记录时已经检查了结构层面。"}
:::

## 安全应用与测试

保留当前配置和恢复访问通道，完成验证，并在支持时采用重新加载而不是重启。关闭递归，直接查询每一台权威服务器，比较 SOA 序列号、NS 集合、正面记录、不存在的名称，以及 UDP 和 TCP 行为：

```bash
$ dig @192.0.2.53 example.com SOA +norecurse
$ dig @192.0.2.53 missing.example.com A +norecurse
$ dig @192.0.2.53 example.com SOA +norecurse +tcp
```

对于递归服务，应测试允许和拒绝的客户端网络、DNSSEC 验证、缓存行为，以及上游依赖失效时的表现。

:::single-choice{#dns-setup-norecurse-test}
为什么使用 `+norecurse` 查询权威服务器？

::option[在不请求递归的情况下测试权威回答。]{#dns-setup-authority-only .correct explanation="这样可以把区域服务与任何递归行为区分开来。"}
::option[删除其区域中的每一条记录。]{#dns-setup-remove-records explanation="查询不会编辑权威数据。"}
::option[强制所有响应都通过 HTTP。]{#dns-setup-force-http explanation="该选项控制 DNS 的期望递归标志。"}
:::

## 运维服务

监控查询失败、延迟、缓存行为、资源使用、区域传送、序列号一致性、DNSSEC 到期和委派健康状况。安全备份源配置和签名材料，同时验证全新实例能够加载区域并提供正确回答。及时修补仍受支持的版本，并限制控制接口、动态更新和区域传送访问权限。

:::single-choice{#dns-setup-redundancy-verification}
权威 DNS 冗余测试应包括什么？

::option[查询每台服务器，并测试其中一台不可用时的运行情况。]{#dns-setup-test-each-server .correct explanation="列出多条 NS 记录并不能证明每项独立服务都可访问且数据是最新的。"}
::option[只检查所有服务器是否拥有相似的主机名。]{#dns-setup-hostname-similarity explanation="名称不能证明数据同步或服务可用。"}
::option[让所有对外公布的服务器共用一个进程和磁盘。]{#dns-setup-shared-failure explanation="共享故障域会削弱冗余能力。"}
:::

## 总结

现在，你可以围绕明确的权威或递归角色设计 DNS 部署。

1. 先定义所需角色，再选择软件。
2. 限制递归查询和管理接口。
3. 重新加载前验证配置与区域。
4. 直接测试权威、否定回答、传输和客户端策略。
5. 监控冗余、DNSSEC、数据一致性和恢复能力。
