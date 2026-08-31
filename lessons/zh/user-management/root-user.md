---
lesson_id: "root-user"
course_id: "user-management"
lang: "zh"
order_index: 2
title: "root"
description: "学习 su、sudo 和 sudoers 策略如何提供对特权身份的受控访问。"
meta_title: "root - 用户管理"
meta_description: "探索 Linux 中 root 用户的角色。本课程涵盖 su 和 sudo 在获取超级用户权限方面的区别，并解释 /etc/sudoers 文件如何管理访问权限。"
meta_keywords: "linux root 用户，linux root, su, sudo, sudoers, visudo, 超级用户，用户管理，linux 权限"
---

传统上名为 `root` 的账户拥有 UID 0，并在其安全上下文中拥有广泛权限。日常工作应使用非特权账户，只有为了自己理解的特定管理目的才提升权限。

## 使用 su 以另一用户身份启动 shell

`su` 表示 substitute user，它会以另一个账户的身份启动 shell 或命令。不指定用户名时，默认目标是 root：

```bash
$ su
```

认证由 PAM 和本地策略控制。系统可能要求目标账户的密码、限制哪些人可以使用 `su`，也可能锁定 root 密码。不要假设知道密码就是唯一条件。

普通 `su` 会更改身份，同时更多地保留当前环境。`su - USER`（也写作 `su --login USER`）会启动登录式 shell，并初始化更接近目标账户全新登录的环境：

```bash
$ su - operator
```

完成目标用户特定的工作后，应退出这个子 shell。

:::single-choice{#root-su-login-shell}
哪个命令会请求以用户 `operator` 身份启动登录式 shell？

::option[`su - operator`]{#root-su-login-operator .correct explanation="连字符请求登录式 shell 行为，并为 `operator` 设置面向目标用户的环境。"}
::option[`su operator`]{#root-su-preserve-environment explanation="这会切换到目标身份，但不会请求本课介绍的完整登录式初始化。"}
::option[`sudo -l operator`]{#root-sudo-list-operator explanation="`sudo -l` 会按策略列出允许的命令，不会启动所请求的登录 shell。"}
:::

## 使用 sudo 运行特定命令

`sudo COMMAND` 会请求策略授权，以目标用户身份运行一个命令，默认目标通常是 root。使用 `-u USER` 可请求其他目标：

```bash
$ sudo -u postgres id
```

这并不表示请求一定会获准。Sudo 策略控制调用用户、主机、目标身份、命令和其他条件。根据配置，认证可能使用调用用户的密码、其他机制，或者不显示提示。

在可行时，优先提升一个范围明确的管理命令，而不是开启长期存在的特权 shell。较小的范围能降低意外命令在提升权限下运行的可能性。

:::single-choice{#root-sudo-target-user}
`sudo -u postgres id` 请求什么？

::option[把当前账户永久重命名为 `postgres`。]{#root-sudo-rename explanation="`sudo` 使用目标凭据运行命令，不会重命名账户记录。"}
::option[在策略允许的前提下，以 `postgres` 为目标用户运行 `id`。]{#root-sudo-postgres-id .correct explanation="`-u` 选项选择目标身份，而 sudoers 策略决定请求是否获准。"}
::option[列出 UID 大于当前用户的每个用户。]{#root-sudo-list-uids explanation="`id` 命令报告自身进程的身份信息；这种语法不会枚举账户 UID。"}
:::

## 避免持续存在的特权 Shell

策略允许时，`su -`、`sudo -s` 或 `sudo -i` 等命令可以创建特权 shell。在退出前，该 shell 中之后的每个命令都可能具有提升后的影响。路径错误、未经审查的脚本和 shell 展开都会变得更加危险。

审计行为取决于配置。`sudo` 通常记录调用，但一次已记录的 shell 启动不会自动提供在该 shell 中输入的每个命令的完整记录。Shell 历史、系统审计和 sudo I/O 日志是各自拥有独立策略的不同机制。

:::single-choice{#root-persistent-shell-risk}
为什么长期存在的 root shell 比一次提升一个已理解命令的风险更高？

::option[Root shell 会自动从所有审计系统中删除每个命令。]{#root-shell-no-audit explanation="日志行为因配置而异，声称所有审计记录都会自动清除并不准确。"}
::option[该 shell 会禁用包含多于一个组成部分的文件系统路径。]{#root-shell-path-limit explanation="特权不会施加这种路径限制；问题在于普通操作会获得更大权限。"}
::option[之后的命令可以在 shell 退出前一直保持提升后的影响。]{#root-shell-elevated-scope .correct explanation="持续的特权身份扩大了拼写错误或不受信任命令修改受保护资源的时间窗口。"}
:::

## 审查 sudo 授权

运行 `sudo -l`，列出当前账户在活动策略下可以请求的操作：

```bash
$ sudo -l
```

请审查命令路径、获准的目标用户和参数限制。看起来范围较广的规则，也不应被视为执行无关工作的许可。

:::single-choice{#root-list-sudo-rules}
哪个命令会列出当前调用用户可用的 sudo 权限？

::option[`sudo -i`]{#root-sudo-login explanation="这会请求目标用户的登录式 shell，并可能扩大权限范围；它不是只读策略列表。"}
::option[`sudo -l`]{#root-sudo-list .correct explanation="小写 `-l` 选项要求 sudo 列出当前策略允许的命令。"}
::option[`su -l`]{#root-su-login-default explanation="这会为 `su` 调用登录式 shell 行为，而不会列出 sudo 授权。"}
:::

## 安全编辑 sudoers 策略

默认 sudo 策略通常读取 `/etc/sudoers`，也可能包含 `/etc/sudoers.d/` 下的文件。还可能存在其他策略来源。其语法控制的内容远不只是简单的用户和组列表。

请使用 `visudo` 修改策略，因为它会锁定文件，并在安装前验证语法：

```bash
$ sudo visudo
```

对于 drop-in 文件，请指定其确切路径：

```bash
$ sudo visudo -f /etc/sudoers.d/application-admins
```

不要使用普通重定向或未经验证的编辑器流程编辑 sudoers。语法或权限错误可能导致管理访问失效。远程更改授权时，应保留另一条经过验证的恢复路径。

:::single-choice{#root-edit-sudoers-safely}
应使用哪个工具编辑并检查主要 sudoers 策略的语法？

::option[`cat`]{#root-cat-sudoers explanation="`cat` 可以显示可读文本，但不会安全编辑、锁定或验证 sudoers 语法。"}
::option[`visudo`]{#root-visudo .correct explanation="`visudo` 提供专为 sudoers 策略更改设计的锁定和语法验证。"}
::option[使用 `echo` 和 `>`]{#root-echo-sudoers explanation="Shell 重定向可能立即截断策略，而且不提供 sudoers 语法验证。"}
:::

要在受控环境中练习委派管理，可以尝试以下动手实验：

1. **[在 Linux 中配置用户账户和 Sudo 权限](https://labex.io/zh/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - 练习实施密码策略、锁定和解锁用户账户、保护 root 账户及授予管理权限，这些都直接关系到超级用户访问管理。

## 总结

现在，你可以区分身份切换和受策略控制的命令委派。

1. 只有确实需要目标登录 shell 时才使用 `su - USER`。
2. 使用 `-u USER` 请求特定 sudo 目标。
3. 尽量缩短停留在特权 shell 中的时间。
4. 使用 `sudo -l` 审查有效 sudo 规则。
5. 只通过 `visudo` 编辑 sudoers 策略。
