---
lesson_id: "killing-processes"
course_id: "processes"
lang: "zh"
order_index: 7
title: "kill（终止进程）"
description: "学习如何识别进程，并按照安全的升级顺序使用 `kill` 发送合适的信号。"
meta_title: "kill（终止进程）- 进程管理"
meta_description: "掌握 Linux kill 命令以管理和终止进程。本指南涵盖 kill 与 terminate 的区别，并解释了如 kill sigterm (SIGTERM)、SIGKILL 和 kill sighup (SIGHUP) 等信号。"
meta_keywords: "kill 命令，kill sigterm, kill sighup, linux kill -0, kill 与 terminate, kill -15 linux, SIGTERM, SIGKILL, 进程管理，终止进程"
---

`kill` 命令用于向进程或进程组发送信号。它的名称源于历史原因：所请求的信号可能会终止、暂停或继续进程，也可能触发某种由应用程序定义的操作。发送信号前，务必确认目标完全正确，并了解该程序文档中说明的信号行为。

## 请求有序终止

只提供 PID 时，`kill` 默认发送 `SIGTERM`：

```bash
$ kill 12445
```

显式指定信号时，建议使用符号名称：

```bash
$ kill -TERM 12445
```

`SIGTERM` 的默认动作是终止进程，但程序可以捕获或忽略它。设计良好的服务可以通过信号处理程序停止接收新任务、保存适当的状态，并释放应用程序资源。不过，这只是一种可能性，并不保证清理工作一定能立即完成或成功完成。

:::single-choice{#killing-processes-default-signal} `kill PID` 默认请求发送哪个信号？

::option[`SIGKILL`]{#killing-processes-default-kill explanation="必须显式选择这个不可捕获的强制终止信号。"}
::option[`SIGTERM`]{#killing-processes-default-term .correct explanation="未提供其他信号操作数时，`kill` 会发送标准的终止请求。"}
::option[`SIGSTOP`]{#killing-processes-default-stop explanation="暂停进程并不是 `kill` 默认请求的动作。"}
:::

## 核实目标

PID 可以被重复使用，因此某个过时的 PID 之后可能会指向另一个进程。执行操作前，应立即检查当前活动的目标：

```bash
$ ps -p 12445 -o pid,ppid,user,lstart,stat,cmd
```

检查它的用户、启动时间、命令、父进程、所属服务以及实际职责。如果进程由服务管理器管理，应尽可能使用该管理器提供的停止或重新加载命令，使其能够维持正确状态，并避免立即重新启动子进程。

在凭据规则允许的范围内，你可以向自己拥有的进程发送信号。向其他用户的进程发送信号通常需要相应权限。在使用范围宽泛的按名称匹配命令前，必须先检查每一个匹配结果。

:::single-choice{#killing-processes-pid-reuse} 为什么应该在发送信号前立即检查 PID？

::option[进程每读取一次文件，PID 就会改变。]{#killing-processes-pid-read explanation="一个活动进程在其整个生命周期中通常保持同一个 PID。"}
::option[先前的进程退出后，内核可以重复使用它的 PID。]{#killing-processes-pid-reused .correct explanation="记住的数字 PID 之后可能会指向另一个活动进程。"}
::option[`kill` 接受命令名称，但不接受数字标识符。]{#killing-processes-no-numeric explanation="数字 PID 是 `kill` 常规使用的目标操作数。"}
:::

## 使用零号信号检查权限

零号信号只执行错误检查，并不会真正递送信号：

```bash
$ kill -0 12445
```

命令成功表示此刻存在使用该 PID 的进程，并且调用者有权向它发送信号。失败的含义并不唯一：进程可能不存在，也可能是调用者没有权限。应检查错误信息和退出状态，不要把每一次失败都理解成“进程未运行”。这也只是瞬时检查，无法消除之后发生 PID 复用竞态的可能性。

:::single-choice{#killing-processes-signal-zero} `kill -0 PID` 成功时，能够确定当下的什么情况？

::option[进程已完成全部清理并退出。]{#killing-processes-zero-exited explanation="成功表示存在可发送信号的活动目标，而不是进程已经终止。"}
::option[该进程将永久保留这个 PID。]{#killing-processes-zero-permanent explanation="这项检查只反映瞬时状态，进程退出后 PID 仍可能被复用。"}
::option[进程存在，并且调用者可以向它发送信号。]{#killing-processes-zero-permitted .correct explanation="零号信号会检查目标是否存在以及调用者是否有权限，但不会递送普通信号。"}
:::

## 仅在必要时升级手段

如果已获授权的目标收到 `SIGTERM` 后仍未终止，应先等待与工作负载相适应的时限，并调查原因。确认有必要强制终止后，再发送：

```bash
$ kill -KILL 12445
```

`SIGKILL` 无法被捕获、忽略或阻塞，因此程序没有机会执行应用层清理。它可能留下未完成的事务、临时状态，或需要其他组件处理的恢复工作。应把它作为升级手段，而不是例行使用的第一步。

其他信号的意义取决于接收程序的约定。`SIGHUP` 经常用于请求重新加载配置，但有些程序仍保留它默认的终止行为。`SIGSTOP` 会在不清理的情况下暂停进程，而 `SIGCONT` 会让已暂停的进程继续运行。

:::single-choice{#killing-processes-kill-tradeoff} `SIGKILL` 在实际操作中的主要缺点是什么？

::option[只有进程所有者才能处理它。]{#killing-processes-kill-owner-handler explanation="任何目标进程都无法为 `SIGKILL` 安装处理程序。"}
::option[它只会暂停进程，永远不会终止进程。]{#killing-processes-kill-pauses explanation="`SIGSTOP` 用于暂停，而 `SIGKILL` 用于终止。"}
::option[它不给程序执行应用层清理的机会。]{#killing-processes-kill-no-cleanup .correct explanation="内核会直接执行终止，不会调用用户空间的信号处理程序。"}
:::

只应在隔离环境中，对你自己启动的进程练习选择信号。[管理和监控 Linux 进程](https://labex.io/zh/labs/comptia-manage-and-monitor-linux-processes-590864)实验提供了一套受控的检查与终止流程。

## 总结

现在，你可以按照审慎且可验证的流程向进程发送信号。

1. 执行操作前，确认活动目标及其管理程序。
2. 使用 `SIGTERM` 发出常规终止请求。
3. 将零号信号理解为瞬时的存在性与权限检查。
4. 只有经过调查并确认需要升级时，才使用 `SIGKILL`。
