---
lesson_id: "security-event-correlation"
course_id: "security-logs"
lang: "zh"
order_index: 5
title: "事件关联"
description: "学习如何利用时间、主机、账户和会话信息关联安全日志。"
meta_title: "事件关联 - 安全日志"
meta_description: "比较 SSH 和 sudo 日志，统一时间戳，再判断哪些证据支持两起事件有关联。"
meta_keywords: "事件关联, 安全日志, SSH 登录记录, sudo 事件, 时间戳, 会话 ID"
---

一条登录记录显示有人登录了机器，另一条记录显示某条命令获准执行。两条记录有关联吗？**事件关联**就是比较不同记录，判断它们描述的活动是否有关联。

## 读懂两条记录

SSH 可以让你登录另一台机器。登录后，用户可以用 `sudo` 请求以另一个账户运行命令。下面两条模拟记录出自同一天。为了便于练习，两条记录使用一致的字段名。实际日志的字段名可能不同，有些字段也可能缺失。

```text
t=09:14:02Z      source=ssh   host=web-01 account=alex session=42 login=accepted
t=11:15:10+02:00 source=sudo  host=web-01 account=alex session=42 decision=allowed
```

`source` 字段表示报告事件的工具，`host` 字段表示事件发生的机器。两条记录涉及的账户都是 `alex`。如果要确认究竟是谁用了这个账户，还需要其他证据。

:::single-choice{#security-event-correlation-account-evidence} 同事说 sudo 请求是 Alex 本人发出的。现有记录能证明什么？

::option[sudo 请求是 Alex 本人发出的。]{#security-event-correlation-account-person explanation="仅凭账户名称，无法确定实际使用账户的人。"}
::option[两条记录分别对应两个账户。]{#security-event-correlation-account-different explanation="两个 account 字段都是 alex。不同的 source 字段表示报告活动的工具不同。"}
::option[两起事件中的账户相同。]{#security-event-correlation-account-shared .correct explanation="两条记录中的账户都是 alex。要确定谁在使用它，还需要更多证据。"}
:::

## 比较事件时间

`t` 字段保存了记录到的时间。第一条记录中的 `Z` 表示 UTC，可以用它统一比较不同的时钟。第二条记录使用 `+02:00`，比 UTC 快两小时。把 `11:15:10` 减去两小时，就得到 UTC 时间 `09:15:10`。

现在比较 `09:14:02` 和 `09:15:10`。登录先被记录下来。即使两个事件时间接近，也可能来自不同的登录。

:::single-choice{#security-event-correlation-time-order} 另一天的登录时间是 `09:14Z`，一个请求的记录时间是 `11:13+02:00`。两件事的先后顺序是什么？

::option[请求早一分钟。]{#security-event-correlation-time-request-first .correct explanation="请求时间减去两小时后是 09:13 UTC。登录发生在 09:14 UTC。"}
::option[登录早一分钟。]{#security-event-correlation-time-login-first explanation="请求换算后是 09:13 UTC，比 09:14 UTC 的登录早一分钟。"}
::option[登录早了将近两小时。]{#security-event-correlation-time-unadjusted explanation="这样比较的是时间戳上直接显示的数字。判断先后之前，应统一换算成 UTC。"}
:::

## 核对主机和会话

**会话**是从登录到退出或断开连接的一段活动。在这些练习记录中，SSH 日志带有与成功登录关联的会话 ID。两个数据来源都使用同一主机上这次登录的会话 ID。前两条记录都显示 `host=web-01` 和 `session=42`，因此这次登录和这个请求可以关联到同一个会话。

在这些例子里，会话编号只在对应的主机上有意义。下面这条记录的账户和会话编号相同，时间也只晚了几秒。

```text
t=09:15:18Z source=sudo host=web-02 account=alex session=42 decision=allowed
```

![LabEx 终端显示 web-01 和 web-02 的模拟记录，并把时间换算为 UTC 09:15:10](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/security-logs/security-event-correlation/utc-correlation.png)

终端展示了三条模拟记录，并用 Ubuntu 的 `date` 命令确认了 UTC 换算结果。

:::single-choice{#security-event-correlation-host-scope} 第三条记录与最初的 SSH 会话有什么关系？

::option[账户相同、时间接近，所以属于同一个会话。]{#security-event-correlation-host-scope-account explanation="两台主机可能在几秒内记录到同名账户的活动。"}
::option[主机不同，所以属于另一个会话。]{#security-event-correlation-host-scope-machine .correct explanation="web-02 上的 42 号会话只在那台主机上有效。最初的登录发生在 web-01。"}
::option[会话编号相同，所以属于同一个会话。]{#security-event-correlation-host-scope-session explanation="这里的会话编号只能结合所在主机来理解，而两条记录的主机名不同。"}
:::

## 说明证据支持的结论

在 `web-01` 上，登录被接受，会话期间 `sudo` 准许执行一条命令。现有证据只能说明到这里。要知道命令执行效果，应查找记录该命令结果的日志。一次会话可以包含多个命令，因此必须把结果和这条请求对应起来。如果找不到匹配的记录，就保留结果未知的结论。

:::single-choice{#security-event-correlation-completion-evidence} 哪种新记录能帮助确定那条命令是否执行成功？

::option[同一会话中另一条命令的结果。]{#security-event-correlation-completion-other-command explanation="一个会话可以运行多个命令。结果必须对应正在核查的这条请求。"}
::option[另一条显示请求已获准的记录。]{#security-event-correlation-completion-permission explanation="这只能确认命令获准执行。执行结果仍需另查。"}
::option[这条特定请求所对应的命令结果。]{#security-event-correlation-completion-result .correct explanation="匹配的结果记录可以说明命令是怎样结束的。"}
:::

想练习筛选和比较另一组身份验证及 sudo 记录，可以试试 [系统日志分析](https://labex.io/tutorials/linux-system-log-analysis-656124)。

## 总结

现在，你可以结合多条安全记录作出判断，并确定还需要核实什么。

1. 识别事件记录中涉及的账户。
2. 先把时间戳统一到一个时区，再比较先后。
3. 同时用主机和会话标识关联活动。
4. 说明现有记录能证明什么，并找出回答其余问题所需的证据。
