---
lesson_id: "security-events"
course_id: "security-logs"
lang: "zh"
order_index: 1
title: "安全事件"
description: "区分实际发生的安全事件、描述事件的日志记录，以及提示你进一步核查的告警。"
meta_title: "安全事件 - 安全日志"
meta_description: "读懂简短的 Linux 安全日志和告警，并判断已有记录不足时应该查什么。"
meta_keywords: "安全事件, 安全日志, 日志记录, 告警, Linux 日志"
---

服务器报告了一次登录失败。发生了什么？这条记录又能说明什么？先把机器记录下来的信息和你据此作出的判断分开。

## 事件与日志记录

**事件**是实际发生的事，例如一次登录尝试被拒绝。**日志记录**描述该事件，并将信息保存下来。**日志**由多条记录组成。课程用字段名称统一的模拟记录帮助你练习读日志。不同工具给字段命名和保存记录的方式可能各不相同。

```text
t=08:55:00Z source=ssh host=web-01 account=alex login=rejected
```

这条记录显示，账户 `alex` 的远程登录尝试被拒绝。尝试结束后，仍可查看保存下来的记录。后面会介绍怎样比较来自不同来源的时间戳。

![LabEx 终端显示模拟的 SSH 登录失败记录，账户为 alex，主机为 web-01](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/security-logs/security-events/event-fields.png)

LabEx 终端从文本文件中显示了同一条模拟记录。

:::single-choice{#security-events-event-versus-record} 例子里的哪一项是事件本身？

::option[保存下来、描述拒绝结果的那一行。]{#security-events-event-line explanation="这一行是日志记录，事件发生后仍可查看。"}
::option[之后查看已经保存的那一行。]{#security-events-event-review explanation="打开日志查看是后续操作。日志描述的事件是登录被拒绝。"}
::option[登录尝试被拒绝。]{#security-events-event-attempt .correct explanation="拒绝发生在服务器上。日志记录的是当时发生了什么。"}
:::

## 读懂字段

**字段**是记录中的一项信息。这里的 `t` 给出记录到的时间，`host` 是事件发生的机器，`source` 表示报告事件的工具。`account` 是涉及的账户，`login` 则给出登录尝试的结果。

:::single-choice{#security-events-field-host} 想知道哪台机器记录了这次登录失败，应该看哪个值？

::option[account 字段中的 `alex`。]{#security-events-field-host-account explanation="account 字段表示这次尝试涉及的账户。"}
::option[host 字段中的 `web-01`。]{#security-events-field-host-web .correct explanation="host 字段标明事件发生的机器。"}
::option[source 字段中的 `ssh`。]{#security-events-field-host-tool explanation="source 字段标明报告该事件的工具。"}
:::

## 告警与触发规则

**告警**会提示人员查看某个可能需要关注的情况。例如，监控规则发现同一账户在同一主机上五分钟内有三次登录失败，就可以发出告警。这条规则根据账户、主机和时间把记录归在一起。收到告警说明有记录符合规则。也可能只是有人连续输错了几次密码。

:::single-choice{#security-events-alert-interpretation} 规则因 alex 在 web-01 上的三次登录失败而发出告警。告警能说明什么？

::option[日志中的登录失败记录符合触发条件。]{#security-events-alert-condition .correct explanation="告警指出一种值得核查的情况。规则并未判断是谁导致了这些失败。"}
::option[有三个人分别尝试过登录。]{#security-events-alert-people explanation="三次尝试可能来自同一个人，也可能来自多人。规则统计的是记录数。"}
::option[有人试了三次之后成功登录。]{#security-events-alert-success explanation="规则统计的是被拒绝的登录尝试，没有说明之后是否有人登录成功。"}
:::

## 决定接下来查什么

要确认 `alex` 后来是否登录，应查看失败之后 `web-01` 上的登录结果。下结论前，先核对记录覆盖的时间段。日志导出文件是选定记录的副本，可能在你要查的时间之前就结束了。

:::single-choice{#security-events-next-record} 日志只导出到 09:00。要确认 09:05 是否成功登录，应该找什么？

::option[把同一份导出记录按从新到旧的顺序排列。]{#security-events-next-sort explanation="排序只会改变记录的顺序，无法补上 09:00 之后的记录。"}
::option[覆盖 09:05 的 web-01 登录记录。]{#security-events-next-window .correct explanation="需要找到相关的数据来源，而且它的记录时段必须覆盖正在核查的时间。"}
::option[重新统计 09:00 之前的登录失败次数。]{#security-events-next-count explanation="这个统计针对的是之前时段里的另一种登录结果。"}
:::

## 总结

现在，你可以读懂一条安全日志，并判断收到告警后该查什么。

1. 区分事件与记录该事件的日志行。
2. 在示例记录中找出账户、主机和结果。
3. 根据告警规则理解监控系统看到了什么。
4. 确认数据来源和时间范围是否能回答你的问题。
