---
lesson_id: "system-logging"
course_id: "logging"
lang: "zh"
order_index: 1
title: "系统日志"
description: "学习 Linux 日志源、收集器、存储和查看工具如何协同工作。"
meta_title: "系统日志 - 日志"
meta_description: "通过理解系统日志来学习 Linux。本指南介绍 syslog、rsyslogd，以及如何在 /var/log 中查找和阅读日志文件，是免费在线 Linux 课程的重要组成部分。"
meta_keywords: "如何学习 Linux, 学习 Linux 的最佳方式, Linux 系统日志, syslog, rsyslogd, var log, 系统日志, 学习 Linux 命令行, Linux 学习资源"
---

日志记录由内核、服务、应用程序和安全组件发出的事件。它们可以帮助排查问题和审计，但前提是收集功能正常、时间戳得到正确理解，并且相关来源已包含在内。

## 跟踪一条日志消息

一条日志路径包含几个不同的环节：

1. 来源发出事件。
2. 收集器接收事件并补充信息。
3. 路由和保留规则选择存储位置或转发目的地。
4. 查看工具查询已存储的记录。

在 systemd 主机上，`systemd-journald` 通常会收集服务标准输出、内核消息，以及 journal 原生消息或 syslog 消息。rsyslog 等 syslog 守护进程也可以接收消息，将其写入传统文本文件或转发出去。应用程序也可能自行维护文件或外部遥测数据。

:::single-choice{#system-logging-distinct-roles}
哪个部分决定已接收的消息存储到哪里或转发到哪里？

::option[终端的当前工作目录。]{#system-logging-cwd explanation="shell 目录不会定义系统范围的日志路由。"}
::option[正在运行的内核映像文件名。]{#system-logging-kernel-file explanation="内核可以发出消息，但其映像文件名并不是路由策略。"}
::option[路由和保留配置。]{#system-logging-routing .correct explanation="收集与存储之间的规则决定目的地和保留行为。"}
:::

## 查找可用日志

不要假定每台主机都有相同的文件。应检查活动的日志服务和本地配置：

```bash
$ systemctl --type=service --state=running | grep -E 'journal|syslog'
$ ls -la /var/log
$ journalctl --disk-usage
```

在使用兼容路由的 Debian 系发行版上，`/var/log/syslog` 很常见；其他系统则常使用 `/var/log/messages`。只使用 journal 的主机可能没有这两个文件。应用程序文档和单元配置可以指出其他目的地。

:::single-choice{#system-logging-file-absence}
缺少 `/var/log/syslog` 文件必然意味着什么？

::option[主机可能使用了另一个已配置的日志目的地。]{#system-logging-other-destination .correct explanation="只使用 journal 的系统和采用不同 syslog 策略的系统不一定创建该文件。"}
::option[内核从未产生过消息。]{#system-logging-no-kernel explanation="内核记录可能位于 journal 或其他目的地。"}
::option[所有应用程序都已停止运行。]{#system-logging-apps-stopped explanation="无法根据一个路径不存在来推断应用程序状态。"}
:::

## 查询 journal

应先使用有边界的查询，而不是倾倒整个 journal：

```bash
$ journalctl -b -p warning
$ journalctl -u ssh.service --since '1 hour ago'
```

`-b` 选择当前启动，`-p` 按优先级过滤，`-u` 按单元过滤。不同主机上的单元名称和保留启动记录并不相同。使用 `journalctl --list-boots` 查看可用的启动记录；重现问题时，可用 `journalctl -f` 跟踪新记录。

:::single-choice{#system-logging-current-boot}
哪个选项将 `journalctl` 查询限制在当前启动？

::option[`-b`]{#system-logging-boot-option .correct explanation="不带参数时，启动选择器会选择当前启动。"}
::option[`-u`]{#system-logging-unit-option explanation="该选项按 systemd 单元过滤。"}
::option[`-f`]{#system-logging-follow-option explanation="该选项跟踪新追加的记录。"}
:::

## 结合上下文阅读记录

传统 syslog 风格的日志行可能如下：

```text
Jan 27 07:41:32 icebox anacron[4650]: Job `cron.weekly' started
```

其中包含时间戳、主机、程序和 PID，最后是消息。应把消息文本视为应用程序输出，而不是有保证的结构化事实。检查时区、时钟同步、启动 ID、PID 重用，以及事件前后的记录。与单独渲染出的文本相比，journal 字段可以提供更可靠的标识符。

日志可能包含用户名、地址、路径、令牌或其他敏感数据。调查时应采用最小权限访问，对导出内容进行脱敏，并保留原始记录和时间戳。

:::single-choice{#system-logging-export-safety}
向外部分享日志摘录前应该做什么？

::option[把每个时间戳替换成随机值。]{#system-logging-random-time explanation="破坏时间信息会妨碍关联分析，并不是合理的脱敏方式。"}
::option[检查其中是否含有秘密和敏感标识符。]{#system-logging-review-sensitive .correct explanation="日志经常包含需要受控脱敏的运维数据或个人数据。"}
::option[让所有人都能写入原始日志。]{#system-logging-world-writable explanation="削弱访问控制可能破坏完整性，并暴露更多数据。"}
:::

## 总结

现在，你可以在不假定统一存储路径的情况下查找和查询 Linux 日志。

1. 区分事件来源、收集器、路由、存储和查看工具。
2. 查明主机当前使用的日志配置。
3. 按单元、启动、时间或优先级使用有边界的 journal 查询。
4. 结合上下文关联记录，并保护日志中的敏感数据。
