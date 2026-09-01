---
lesson_id: "syslog"
course_id: "logging"
lang: "zh"
order_index: 2
title: "syslog"
description: "学习 syslog 的设施、严重级别、路由规则以及 logger 命令如何工作。"
meta_title: "syslog - 日志"
meta_description: "了解 Linux 中的 syslog 和 rsyslog、如何管理系统日志以及如何使用 logger 命令。本教程适合初学者入门。"
meta_keywords: "syslog, rsyslog, Linux 日志, logger 命令, /var/log/syslog, Linux 教程, Linux 初学者, 系统日志"
---

Syslog 定义了许多类 Unix 系统采用的消息模型和传输惯例。Rsyslog 是其中一种实现，可以接收、过滤、转换、存储和转发消息。它可以与 `systemd-journald` 共存；无论哪一个名称，都不意味着每个应用程序都使用这条路径。

## 设施与严重级别

一条 syslog 消息带有设施字段，用来描述大致来源类别，同时带有从紧急到调试的严重级别。常见设施包括 `auth`、`cron`、`daemon`、`kern`、`mail`、`user`，以及 `local0` 到 `local7`。

严重级别具有顺序。在经典选择器语法中，`daemon.warning` 通常会匹配 daemon 设施中 warning 及所有更严重级别的消息，而不只是 warning。支持经典语法的实现可以使用等号修饰符进行精确匹配，例如 `daemon.=warning`。

:::single-choice{#syslog-warning-selector} `daemon.warning` 这样的经典选择器通常匹配什么？

::option[只匹配文本中包含 daemon 一词的消息。]{#syslog-text-daemon explanation="该选择器依据设施元数据，而不是搜索消息文本。"}
::option[来自所有设施的每条 debug 消息。]{#syslog-all-debug explanation="该选择器仅限 daemon 设施和指定的严重级别阈值。"}
::option[warning 及更严重的 daemon 消息。]{#syslog-warning-or-higher .correct explanation="优先级选择器包含指定严重级别和紧急程度更高的级别。"}
:::

## 阅读 rsyslog 规则

Rsyslog 通常加载一个主文件和 `/etc/rsyslog.d/` 下的配置片段。传统规则由选择器和其后的操作组成：

```text
auth,authpriv.*          /var/log/auth.log
*.*;auth,authpriv.none  -/var/log/syslog
kern.*                  /var/log/kern.log
```

第一行路由两个身份验证设施的所有优先级。第二行广泛选择消息，但排除这两个设施。第三行路由内核设施消息。文件操作前的 `-` 通常表示请求异步写入，并不表示排除。

更改生产环境路由前，应检查所有被包含的文件，并验证已安装版本所用的确切语法。

:::single-choice{#syslog-selector-action} 在传统 rsyslog 规则中，哪一部分是操作？

::option[左侧的设施和严重级别表达式。]{#syslog-left-selector explanation="这部分负责选择消息。"}
::option[右侧的目的地或操作。]{#syslog-right-action .correct explanation="操作决定将选中的记录发送到文件、远程目标还是其他输出。"}
::option[描述软件包版本的注释。]{#syslog-comment-version explanation="注释不会执行消息路由。"}
:::

## 发送测试消息

使用 `logger` 提交一条带有可识别标签和优先级的受控测试消息：

```bash
$ logger -p user.notice -t lesson-test 'routing check 2026-08-31T10:00'
```

然后查询预期目的地，例如：

```bash
$ journalctl -t lesson-test --since '5 minutes ago'
```

根据转发和路由配置，同一个事件可能同时出现在 journal 和文本文件中。`logger -s` 还会将消息复制到标准错误，但这不能证明消息已被持久存储。

:::single-choice{#syslog-logger-tag} `logger -t lesson-test` 会向提交的消息添加什么？

::option[删除较早测试记录的请求。]{#syslog-tag-delete explanation="该选项设置标识标签，不管理保留策略。"}
::option[将标识符 `lesson-test` 作为消息标签。]{#syslog-tag-identifier .correct explanation="唯一标签使受控事件更容易在已配置的目的地中找到。"}
::option[五分钟的传送延迟。]{#syslog-tag-delay explanation="标签选项不会编码传送间隔。"}
:::

## 更改并验证路由

更改前，应保存当前配置并确定下游使用者。使用当前实现的配置检查模式验证语法，通常为：

```bash
$ sudo rsyslogd -N1
```

只有验证通过后，才能通过服务管理器重新加载服务。发送一条新的带标签消息，验证每个必需目的地，并检查服务状态和内部错误日志。语法有效的规则仍可能路由范围过宽、产生重复记录或暴露敏感数据。

日志跨越不可信网络时，远程转发应使用经过身份验证的加密传输。UDP 传送没有端到端确认；关键审计要求需要采用能够处理队列、丢失、完整性、访问控制和接收端中断的设计。

:::single-choice{#syslog-change-verification} 什么足以证明新路由规则可以正常工作？

::option[配置文件的修改时间很新。]{#syslog-mtime explanation="时间戳不能证明语法有效或消息已经送达。"}
::option[发送端可以通过 ping 访问接收端。]{#syslog-ping explanation="仅有网络可达性不能验证日志协议或存储路径。"}
::option[验证通过，而且带标签的测试消息到达每个预期目的地。]{#syslog-validate-and-test .correct explanation="静态验证与观察到的端到端事件缺一不可。"}
:::

## 总结

现在，你可以从消息元数据一直测试到 syslog 配置的目的地。

1. 区分设施与有序的严重级别。
2. 分别阅读选择器及其操作。
3. 使用 `logger` 发送带标签和优先级的事件。
4. 验证配置，并端到端确认传送结果。
