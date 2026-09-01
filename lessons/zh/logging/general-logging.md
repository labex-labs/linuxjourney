---
lesson_id: "general-logging"
course_id: "logging"
lang: "zh"
order_index: 3
title: "通用日志"
description: "学习如何查找、过滤、跟踪并关联常见的 Linux 系统日志。"
meta_title: "通用日志 - 日志"
meta_description: "面向初学者的 Linux 通用日志指南。了解 /var/log/messages 和 syslog，以便有效进行系统监控、日志分析和 Linux 故障排查。"
meta_keywords: "Linux 日志, syslog, var/log/messages, Linux 故障排查, 系统日志, 日志分析, 系统监控, Linux 指南, Linux 初学者, /var/log"
---

通用系统日志汇集多个来源的日常通知、警告和错误。它们是很有用的起点，但文件名和内容取决于路由策略，并不是 Linux 的统一保证。

## 查找相关来源

根据发行版和配置的不同，通用消息可能出现在 `/var/log/syslog`、`/var/log/messages`、systemd journal 或多个目的地中。首先确定主机和事件时间范围，然后检查可用来源：

```bash
$ ls -lh /var/log
$ journalctl --since '2026-08-31 09:00' --until '2026-08-31 09:15'
```

应用程序日志可能位于自己的子目录或外部服务中。身份验证、审计、软件包、数据库和 Web 服务器记录也可能有意与通用日志流分开。

:::single-choice{#general-logs-universal-file} 为什么不应假定每台 Linux 主机上都有 `/var/log/messages`？

::option[通用日志目的地取决于本地收集器和路由策略。]{#general-logs-local-routing .correct explanation="只使用 journal 的系统或采用不同 syslog 配置的系统可以使用其他目的地。"}
::option[Linux 只允许每块磁盘有一个日志文件。]{#general-logs-one-file explanation="系统通常会维护许多日志文件和 journal 存储。"}
::option[该路径仅供用户文档使用。]{#general-logs-user-documents explanation="/var/log 层次结构通常用于存放日志。"}
:::

## 检查文本日志

使用 `less` 进行可控浏览，使用 `tail` 查看最新记录：

```bash
$ sudo less /var/log/syslog
$ sudo tail -n 100 /var/log/messages
```

在有限时间的重现过程中，可用 `tail -F FILE` 跟踪新追加的行。与简单快照不同，当文件在轮转期间被替换时，`-F` 会重试。使用 `Ctrl-C` 停止跟踪，避免长时间保持范围过大的特权会话。

:::single-choice{#general-logs-tail-f-capability} 在受控重现过程中，`tail -F` 有什么用途？

::option[在常见轮转替换期间持续跟踪指定文件。]{#general-logs-tail-follow .correct explanation="按名称重试的行为有助于在活动文件被重命名并重新创建后继续跟踪。"}
::option[将每条日志的严重级别改为调试。]{#general-logs-tail-debug explanation="tail 读取文件内容，不会重新配置事件来源。"}
::option[无需其他程序即可解密压缩归档。]{#general-logs-tail-decrypt explanation="它不提供通用归档解压或解密功能。"}
:::

## 过滤时保留上下文

应搜索有边界的文件或 journal 时间段，而不是一开始就通过管道处理无限的实时流：

```bash
$ grep -n -C 3 'connection refused' /var/log/example.log
$ journalctl -u example.service --since '10 minutes ago' --grep='connection refused'
```

大小写、措辞、速率限制和本地化都可能让字面搜索遗漏内容。既要记录成功事件，也要记录失败事件，并保留周边行，因为原因可能早于可见错误。

:::single-choice{#general-logs-context-lines} 为什么要包含匹配错误周围的日志行？

::option[之前发生的事件可能解释后来的故障。]{#general-logs-preceding-context .correct explanation="时间上下文有助于还原事件序列，而不是把一个字符串当作整个事件。"}
::option[上下文保证第一个匹配项就是根本原因。]{#general-logs-guaranteed-cause explanation="仍需关联其他证据；上下文并不能证明因果关系。"}
::option[它会自动更改服务配置。]{#general-logs-context-config explanation="搜索输出是只读的，不会更新服务设置。"}
:::

## 包含轮转和归档日志

一次事件可能跨越日志轮转边界。活动文件、编号归档和压缩文件可能分别包含同一事件序列的不同部分。`zgrep` 和 `zless` 等工具可以读取 gzip 压缩归档：

```bash
$ sudo zgrep -n 'connection refused' /var/log/example.log*.gz
```

应按实际时间戳排列结果，而不是只看文件后缀。复制证据前，应保留元数据并限制访问，因为日志可能包含个人数据或凭据。

:::single-choice{#general-logs-rotation-boundary} 事件跨越一次日志轮转时应该检查什么？

::option[只检查新创建的空活动文件。]{#general-logs-active-only explanation="较早的记录可能已经移入轮转归档。"}
::option[按事件时间排列的活动日志和归档日志。]{#general-logs-all-intervals .correct explanation="相关事件序列可能分散在当前文件和轮转文件中。"}
::option[只检查文件名，不考虑记录时间戳。]{#general-logs-filenames-only explanation="后缀顺序并不总是等同于事件时间顺序。"}
:::

## 总结

现在，你可以跨文件、journal 和轮转边界调查通用日志。

1. 查明日志目的地，而不是假定存在统一文件名。
2. 阅读有边界的时间段，只在重现问题时进行跟踪。
3. 保留匹配记录周围的时间上下文。
4. 包含轮转归档，并保护敏感证据。
