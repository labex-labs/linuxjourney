---
lesson_id: "ssh-login-events"
course_id: "security-logs"
lang: "zh"
order_index: 2
title: "SSH 登录事件"
description: "学习从 SSH 记录中辨认登录被拒绝或接受的结果，并把同一次连接中的尝试归在一起。"
meta_title: "SSH 登录事件 - 安全日志"
meta_description: "读懂 SSH 日志里的目标账户、远程地址、身份验证方式和登录结果，再用连接标识比较多次尝试。"
meta_keywords: "SSH 登录事件, SSH 日志, 登录成功, 登录失败, 身份验证方式"
---

**SSH** 全称 Secure Shell，可用于通过网络登录另一台电脑。接收连接的机器可以记录每次尝试。记录会显示尝试登录的账户，以及服务器是否接受了用于登录的身份证明。

## 查看登录结果

下面是两条模拟的 SSH 记录。`login` 字段表示登录结果。尝试被拒绝，意味着没有通过登录验证。尝试被接受，意味着验证通过。

```text
t=09:13:48Z source=ssh host=web-01 account=alex login=rejected
t=09:14:02Z source=ssh host=web-01 account=alex login=accepted
```

第一条记录显示 `alex` 的登录尝试被拒绝。第二条显示同一账户的另一次尝试被接受。每条结果只对应各自的尝试。

:::single-choice{#ssh-login-events-outcome-order} 根据这两条记录，哪种说法成立？

::option[较晚的那次尝试通过了登录验证。]{#ssh-login-events-outcome-later .correct explanation="第二条记录在 09:14:02 显示了 login=accepted。"}
::option[两次尝试都通过了登录验证。]{#ssh-login-events-outcome-both explanation="较早的一行记录了被拒绝的尝试。"}
::option[较晚的那次尝试未通过登录验证。]{#ssh-login-events-outcome-failed explanation="被拒绝的是第一次尝试。第二次尝试被接受了。"}
:::

## 读取地址和身份验证方式

在接收连接的机器看来，连接来自哪个地址？这就是远程地址。在这个示例中，它记在 `peer` 字段中。网络地址可能由多人共用，因此单凭地址无法确定是谁在使用它。

```text
t=09:14:02Z source=ssh host=web-01 account=alex login=accepted
peer=192.0.2.10 method=publickey connection=17
```

第二行是同一条记录的后半部分。`method` 字段写明 SSH 检查的身份证明类型。`password` 表示 SSH 检查了密码。`publickey` 表示发起连接的设备证明自己能使用服务器为该账户接受的密钥。

:::single-choice{#ssh-login-events-method-evidence} 对于这次被接受的尝试，记录支持哪项结论？

::option[服务器接受了使用密码的登录。]{#ssh-login-events-method-password explanation="使用密码会有对应的验证方式字段。这里记录的是公钥方式。"}
::option[服务器识别出了操作这个地址的人。]{#ssh-login-events-method-person explanation="地址反映主机看到的连接来源，无法说明当时是谁在操作。"}
::option[服务器接受了使用密钥的登录。]{#ssh-login-events-method-key .correct explanation="记录同时显示 login=accepted 和 method=publickey。"}
:::

## 按连接归组登录尝试

**连接**是 SSH 用来交换消息的网络链路。在这些示例中，主机会给每条连接分配一个标识。同一个连接中可能有多次登录尝试，同一地址也可以建立新的连接。

```text
t=09:13:48Z host=web-01 account=alex peer=192.0.2.10 connection=17 login=rejected
t=09:13:55Z host=web-01 account=alex peer=192.0.2.10 connection=18 login=rejected
t=09:14:02Z host=web-01 account=alex peer=192.0.2.10 connection=17 login=accepted
```

在 `web-01` 上，第一条和最后一条记录的连接编号都是 17。查看这个编号时，要把主机也纳入判断。

![LabEx 终端显示来自同一个地址的模拟 SSH 登录尝试，连接 ID 为 17 和 18](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/security-logs/ssh-login-events/ssh-connections.png)

终端把三次模拟尝试放在一起，方便对比连接编号。

:::single-choice{#ssh-login-events-group-connection} 哪些记录对应 web-01 上的 18 号连接？

::option[09:13:48 和 09:14:02 的两次尝试。]{#ssh-login-events-group-seventeen explanation="这两行的连接编号都是 17。"}
::option[只有 09:13:55 的那次尝试。]{#ssh-login-events-group-eighteen .correct explanation="只有这一行显示 web-01 上的 18 号连接。"}
::option[来自 192.0.2.10 的三次尝试。]{#ssh-login-events-group-address explanation="同一个地址下出现了两个连接编号。"}
:::

## 追踪登录成功之后的活动

登录成功说明 SSH 接受了该账户提供的身份证明。要知道接下来发生了什么，请查找**会话**打开的记录。登录会话用于追踪登录后的活动。单独一条登录成功记录只说明验证结果。

:::single-choice{#ssh-login-events-after-accepted} 哪条记录能帮助你确认登录被接受后是否打开了会话？

::option[另一条显示同一次登录被接受的记录。]{#ssh-login-events-after-accepted-again explanation="这样的记录只会再次确认登录验证结果。"}
::option[另一台主机上该账户更早的一次拒绝记录。]{#ssh-login-events-after-other-host explanation="那是在另一台机器上的另一次尝试。"}
::option[显示该次登录打开了会话的记录。]{#ssh-login-events-after-session .correct explanation="会话打开记录描述了之后发生的事，并可关联到这次被接受的登录。"}
:::

## 总结

现在，你可以读懂 SSH 登录结果，并判断哪些记录属于同一次连接。

1. 区分被接受和被拒绝的登录尝试。
2. 结合远程地址和身份验证方式描述一次尝试。
3. 有连接标识时，按主机和连接将记录归在一起。
4. 查看会话记录，确认成功登录后发生了什么。
