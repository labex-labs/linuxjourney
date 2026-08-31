---
lesson_id: "power-states"
course_id: "init"
lang: "zh"
order_index: 7
title: "电源状态"
description: "学习如何安排、取消并安全验证 Linux 关机和重启操作。"
meta_title: "电源状态 - 初始化系统"
meta_description: "学习如何管理 Linux 系统的电源状态。本指南介绍安全关闭或重启 Linux 系统所需的 shutdown、reboot 和 halt 命令，帮助你掌握系统管理中的基础 Linux 命令。"
meta_keywords: "Linux 电源状态, shutdown 命令, reboot 命令, halt 命令, Linux 关机, Linux 重启, Linux 系统管理, Linux 入门, Linux 命令, systemd, init"
---

关机或重启会改变整个系统的可用性。执行前应确认目标主机、获得授权、通知已连接的用户，并确保重要的写入、备份和维护任务能够完成。在远程系统上，还要保留独立的控制台或恢复通道，以防计算机无法重新上线。

## 安全关闭电源

在基于 systemd 的发行版上，可用以下命令请求有序关闭电源：

```bash
$ sudo systemctl poweroff
```

传统的 `shutdown` 接口也很常见：

```bash
$ sudo shutdown -h now
```

有序关机会要求服务停止、卸载文件系统，然后改变计算机的电源状态。不要把强制重启或按下物理电源开关当作普通的快捷方式；两者都可能中断写入，使数据或服务处于不一致状态。

:::single-choice{#power-states-orderly-poweroff}
关闭远程生产主机的电源之前应该做什么？

::option[执行命令前断开其管理控制台。]{#power-states-remove-console explanation="管理控制台是很有用的恢复通道，应保持可用。"}
::option[强制关机，避免服务延迟操作。]{#power-states-force-first explanation="强制操作可能中断写入，不应作为常规方法。"}
::option[确认目标主机并保留恢复访问通道。]{#power-states-confirm-and-recover .correct explanation="确认目标可以避免操作错误主机，而恢复通道能在主机未重新上线时提供帮助。"}
:::

## 安排和取消关机

通过安排关机时间，给用户和工作负载留出准备时间。`+m` 形式表示从现在起多少分钟：

```bash
$ sudo shutdown -h +4
```

该命令安排在四分钟后停止系统或关闭电源，并向已登录用户发送警告。如果维护延期，应在截止时间前取消待执行的关机：

```bash
$ sudo shutdown -c
```

不要认为发出警告就意味着操作必然安全。应检查活动会话和系统特有的工作负载；如果服务或集群有规定的排空流程，也要遵循该流程。

:::single-choice{#power-states-four-minute-schedule}
哪个命令会安排在四分钟后关机？

::option[`sudo shutdown -h +4`]{#power-states-relative-four .correct explanation="-h 操作与 +4 结合，会请求从现在起四分钟后关机。"}
::option[`sudo shutdown -h 4`]{#power-states-absolute-four explanation="没有加号时，时间参数并不是文档规定的相对分钟形式。"}
::option[`sudo shutdown -c +4`]{#power-states-cancel-four explanation="-c 选项会取消待执行的关机，而不是安排新的关机。"}
:::

## 重启系统

需要让计算机停止后再次启动时，应进行有序重启：

```bash
$ sudo systemctl reboot
```

常见的等效兼容命令包括：

```bash
$ sudo shutdown -r now
$ sudo reboot
```

重启前，应确认加密磁盘、启动配置、网络和必需服务能够在没有当前交互式会话的情况下恢复。如果其他系统依赖该主机，应先协调故障转移或迁移工作负载。

:::single-choice{#power-states-reboot-action}
哪个命令会通过 `shutdown` 请求立即进行有序重启？

::option[`sudo shutdown -c now`]{#power-states-cancel-now explanation="-c 选项会取消待执行的关机。"}
::option[`sudo shutdown -r now`]{#power-states-reboot-now .correct explanation="-r 选项选择重启，now 则将操作安排为立即执行。"}
::option[`sudo shutdown -h now`]{#power-states-halt-now explanation="-h 操作会停止系统或关闭电源，而不是重启。"}
:::

## 区分停止系统与关闭电源

`halt`、`poweroff` 和 `reboot` 可能是初始化系统的兼容前端，但它们请求的最终状态不同。停止系统会终止正常系统运行；视平台和实现而定，此时可能仍然供电。关闭电源还会请求受支持的硬件切断供电。应优先选择能准确表达预期结果的命令，并查阅本地手册，因为兼容行为可能不同。

:::single-choice{#power-states-halt-versus-poweroff}
为什么应该区分 `halt` 和 `poweroff`？

::option[关闭电源会请求切断供电，而停止系统可能仍保持供电。]{#power-states-power-distinction .correct explanation="即使两者都会停止正常运行，请求的最终硬件状态仍可能不同。"}
::option[停止系统后总会重新启动服务。]{#power-states-halt-restarts explanation="停止系统是一种停止状态，并不是重启服务的请求。"}
::option[关闭电源只会注销当前终端用户。]{#power-states-power-logout explanation="关闭电源是整个系统的状态转换，而不是 shell 注销。"}
:::

## 验证结果

对于已安排的操作，应确认用户已收到通知，而且关键工作已经排空。重启后，应检查预期的内核和启动状态、失败单元、应用程序健康状况、存储挂载、网络可达性以及最近的启动日志。仅仅能够成功登录，并不能证明整个服务已经恢复。

```bash
$ uptime
$ systemctl --failed
$ journalctl -b -p warning
```

这些命令只是起点；对于实际工作负载，还应使用应用程序自身的健康检查。

:::single-choice{#power-states-post-reboot-check}
什么最能证明重启后的应用程序已经就绪？

::option[服务状态、日志和应用程序健康检查全部正常。]{#power-states-health-evidence .correct explanation="结合多项系统和应用检查，才能验证工作负载，而不只是主机访问能力。"}
::option[机箱电源指示灯亮起。]{#power-states-light-on explanation="硬件已通电并不能证明应用程序健康。"}
::option[管理员能够登录 shell。]{#power-states-shell-open explanation="shell 访问只证明系统可用性的一部分。"}
:::

## 总结

现在，你可以经过充分准备，以明确意图改变 Linux 电源状态，并验证操作结果。

1. 确认目标、影响、授权和恢复通道。
2. 正常操作时使用有序关机或重启命令。
3. 当用户和工作负载需要提前通知时，安排延时关机。
4. 维护计划变化时，取消待执行的关机。
5. 计算机重新上线后，验证系统和应用程序健康状况。
