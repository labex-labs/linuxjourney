---
lesson_id: "security-session-records"
course_id: "security-logs"
lang: "zh"
order_index: 4
title: "会话记录"
description: "学习如何把会话打开和关闭的记录配对，并判断一段日志能说明哪些会话。"
meta_title: "会话记录 - 安全日志"
meta_description: "读懂 Linux 会话记录，将会话打开与关闭事件配对，并判断缺少关闭记录时如何核查。"
meta_keywords: "Linux 会话记录, 会话打开, 会话关闭, 登录会话 ID, 日志保留"
---

登录验证确认有人通过了某个账户的登录检查。**会话**是从登录开始，到退出或断开连接为止的一段活动。如果开始和结束都被记下来，会话记录就能告诉你这段活动何时开始、何时结束。

## 读取会话打开记录

会话管理系统可以分配**会话 ID**，用于识别一台机器上的会话。下面两条模拟记录都来自 ``web-01`)，记录了同一个账户打开的两次会话。本课所有时间均使用同一时区。

```text
t=09:14:05Z source=session host=web-01 account=alex session=42 state=opened
t=09:17:00Z source=session host=web-01 account=alex session=43 state=opened
```

第一行记录了 42 号会话的开始。第二行记录的是同一主机上另一次会话，即 43 号会话。

:::single-choice{#security-session-records-two-openings} 根据这两条打开记录，哪种说法成立？

::option[第一次会话在第二次会话开始时结束了。]{#security-session-records-open-ended explanation="第二条记录说明另一次会话开始了，没有给出第一次会话何时关闭。"}
::option[两个不同的账户登录了这台主机。]{#security-session-records-open-accounts explanation="两行的账户相同。会话字段把两段活动区分开来。"}
::option[同一个账户打开了两个独立的会话。]{#security-session-records-open-two .correct explanation="两行都记录了 alex，而且在 web-01 上各有自己的会话 ID。"}
:::

## 将打开与关闭记录配对

配对之前，先同时查看主机和会话 ID。把下面的关闭记录与前面的打开记录对照一下。

```text
t=09:20:05Z source=session host=web-01 account=alex session=42 state=closed
```

在 `web-01` 上，42 号会话的打开和关闭记录相隔六分钟。这一对记录给出了有记载的开始和结束时间，未列出这段期间执行了哪些操作。

![LabEx 终端显示 42 号和 43 号会话的模拟打开记录，以及 42 号会话的关闭记录](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/security-logs/security-session-records/session-records.png)

这个终端画面把模拟的打开和关闭记录放在一起，方便对比。

:::single-choice{#security-session-records-pair-ids} 假设关闭记录改为 `session=43`，主机和时间不变，那么这次会话何时开始？

::option[09:14:05。]{#security-session-records-pair-forty-two explanation="那条打开记录的账户相同，但属于 42 号会话。"}
::option[09:17:00。]{#security-session-records-pair-forty-three .correct explanation="用 web-01 和 43 号会话匹配第二条打开记录，开始时间为 09:17:00。"}
::option[09:20:05。]{#security-session-records-pair-end-time explanation="这是记录里的关闭时间。开始时间应从匹配的打开记录中读取。"}
:::

## 核查缺少的关闭记录

回到 42 号会话的原始关闭记录。这段日志截至 09:21，仍然没有 43 号会话的关闭记录。日志片段结束时，这次会话可能还在进行。关闭记录也可能落在片段的时间范围以外，或者没有保存到这个来源。日志的**保留期限**指记录能保存多久、供人查阅。

:::single-choice{#security-session-records-missing-close} 只看这段日志，关于 43 号会话能得出什么结论？

::option[日志片段结束时，会话仍处于活动状态。]{#security-session-records-missing-active explanation="这有可能，但缺少关闭记录无法确定会话的实际状态。"}
::option[片段没有记录它的关闭时间。]{#security-session-records-missing-unknown .correct explanation="这只描述当前拿到的记录。关闭时间可能出现在后续记录或其他来源中。"}
::option[它和 42 号会话一起关闭了。]{#security-session-records-missing-together explanation="现有的关闭记录属于 42 号会话，这里没有能与 43 号会话配对的关闭记录。"}
:::

## 根据问题选择数据来源

要查历史上的关闭时间，请在同一主机的后续日志中找对应的关闭记录。如果想知道会话现在是否还在进行，应查看那台主机当前的会话列表。保存下来的日志和当前列表能回答不同时间点的问题。

:::single-choice{#security-session-records-current-status} 你要知道 43 号会话现在是否仍在进行。以下哪个来源最有用？

::option[web-01 的当前会话列表。]{#security-session-records-current-list .correct explanation="当前列表能显示主机此刻报告为活动状态的会话。"}
::option[会话打开记录的旧副本。]{#security-session-records-current-opening explanation="它能说明这次会话曾经开始，无法说明现在是否仍在进行。"}
::option[web-01 上 42 号会话的关闭记录。]{#security-session-records-current-other explanation="另一场会话的关闭记录无法回答 43 号会话的问题。"}
:::

## 总结

现在，你可以用会话记录说明已经记下来的开始和结束时间。

1. 找出会话打开记录及其主机和会话 ID。
2. 将关闭记录与正确的打开记录配对。
3. 说明缺少关闭记录时哪些情况还无法确定。
4. 根据要回答的问题选择历史记录或当前会话列表。
