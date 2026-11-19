---
lesson_id: "sudo-events"
course_id: "security-logs"
lang: "zh"
order_index: 3
title: "sudo 事件"
description: "学习如何从 sudo 记录中看出哪个账户提出请求、命令将以哪个账户运行，以及请求是否获准。"
meta_title: "sudo 事件 - 安全日志"
meta_description: "读懂 sudo 日志，区分请求账户、目标账户、请求执行的命令和权限判定。"
meta_keywords: "sudo 事件, sudo 日志, sudo 权限, 目标账户, Linux 权限"
---

用户可能先用普通账户登录，之后需要做一件权限要求更高的事。在使用 `sudo` 的系统上，用户可以请求以另一个账户运行命令。相关记录可以说明用户申请了什么权限，以及系统是否允许。

## 找出两个账户

下面的模拟记录用 `account` 表示提出请求的账户，用 `target` 表示命令将以哪个账户运行。`root` 账户有系统管理权限。`sudo` 也可以指定其他目标账户，例如 `backup`。

```text
t=09:15:10Z source=sudo host=web-01 account=alex target=root
command=systemctl status nginx decision=allowed session=42
```

第二行延续第一行，是同一条记录。这里，`alex` 请求以 `root` 身份运行命令。

:::single-choice{#sudo-events-account-target} 如果记录显示 `account=sam target=backup`，是谁请求以哪个账户运行命令？

::option[backup 请求以 sam 身份运行。]{#sudo-events-target-swapped explanation="account 表示提出请求的账户，target 表示命令将使用的身份。"}
::option[sam 请求以 backup 身份运行。]{#sudo-events-target-backup .correct explanation="account 是请求账户，target 是运行命令时要使用的账户。"}
::option[sam 请求以 root 身份运行。]{#sudo-events-target-root explanation="root 可以作为目标账户，但这条记录写的是 backup。"}
:::

## 找出请求执行的命令

`command` 字段给出请求执行的命令。示例中的 `systemctl status nginx` 请求查看 Nginx Web 服务当前的状态。另一条记录可能出现 `systemctl restart nginx`，表示请求停止并重新启动该服务。两条命令涉及同一个服务，但请求的操作不同。

:::single-choice{#sudo-events-command-scope} 哪个请求要改变 Web 服务的运行状态？

::option[`systemctl restart nginx`]{#sudo-events-command-restart .correct explanation="restart 请求停止并重新启动服务，可能改变运行状态。"}
::option[`systemctl status nginx`]{#sudo-events-command-status explanation="status 只请求显示服务信息，没有要求重启。"}
::option[两个请求都一样，因为都写了 nginx。]{#sudo-events-command-both explanation="服务名称相同。要看请求的具体操作，应读命令中的操作词。"}
:::

## 读懂权限判定

**策略**指 `sudo` 用来判断是否允许请求的一组规则。在这些示例中，`decision=allowed` 表示策略准许了该请求，`decision=denied` 表示 `sudo` 拒绝了它。

```text
t=09:16:00Z source=sudo host=web-01 account=alex target=root
command=systemctl restart nginx decision=denied session=42
```

获准说明请求通过了权限检查。如果想了解命令执行结果，应查找系统提供的结果记录。

![LabEx 终端显示两条模拟 sudo 记录，一条允许查看状态，另一条拒绝重启](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/security-logs/sudo-events/sudo-decisions.png)

对比这两条模拟记录中的命令和权限判定。

:::single-choice{#sudo-events-denied-request} 第二个例子显示，重启请求得到了什么结果？

::option[sudo 拒绝了重启请求。]{#sudo-events-denied-refused .correct explanation="命令写明请求执行什么操作，denied 表示该请求未获授权。"}
::option[服务已经成功重启。]{#sudo-events-denied-success explanation="该记录显示请求被拒绝，无法证明服务成功重启。"}
::option[前面查看状态的请求也被拒绝了。]{#sudo-events-denied-earlier explanation="每个判定只适用于各自的请求。前一条记录显示 allowed。"}
:::

## 结合登录账户和会话看请求

两个例子中的请求账户都是 `alex`，并且都带有 `session=42`。这个编号指的是登录会话，也就是登录之后的一段活动。它可以帮助你找到前后相关的登录记录。每条例子里的目标账户只对应当次命令请求。描述请求时，要结合请求账户和目标账户。

:::single-choice{#sudo-events-session-interpretation} 以下哪项概括符合第一条示例记录？

::option[root 直接登录并打开了 42 号会话。]{#sudo-events-session-root-login explanation="这是一条 sudo 记录。它的目标账户字段没有描述另一次登录。"}
::option[alex 申请在这个会话中以 root 权限执行所有命令。]{#sudo-events-session-all-commands explanation="记录只列出一条命令，无法涵盖会话中的每条命令。"}
::option[alex 在 42 号会话中请求以 root 身份运行一条指定命令。]{#sudo-events-session-one-command .correct explanation="请求账户、目标账户、命令和会话四个字段共同支持这个说法。"}
:::

## 总结

现在，你可以读懂 sudo 记录，并区分权限判定与命令执行结果。

1. 找出请求账户和目标账户。
2. 用命令字段描述具体的请求。
3. 区分获准与被拒绝的请求。
4. 描述请求时结合它所在的登录会话。
