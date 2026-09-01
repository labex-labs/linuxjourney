---
lesson_id: "user-management-tools"
course_id: "user-management"
lang: "zh"
order_index: 6
title: "用户管理工具"
description: "学习如何使用明确选项创建、修改、保护、验证和删除本地账户。"
meta_title: "用户管理工具 - 用户管理"
meta_description: "使用必备的命令行工具掌握 Linux 用户管理。本指南涵盖 useradd、userdel 和 passwd 的用法，非常适合 Linux 账户管理初学者。"
meta_keywords: "linux 用户管理，linux 账户管理命令行工具，useradd, userdel, passwd, linux 账户，管理 linux 用户"
---

Linux 发行版通常提供 shadow 工具套件中的账户工具，但默认值和更高层封装程序各不相同。更改本地账户前，请确认它不是集中管理的，阅读该命令的本地手册，并保留恢复路径。

本课中的命令会改变认证和所有权状态。只能在获准的可丢弃环境中练习，不要在生产主机上练习。

## 审查账户创建默认值

`useradd` 会使用命令选项和站点默认值创建本地账户。使用以下命令检查编译和配置的默认值：

```bash
$ useradd -D
```

`/etc/default/useradd`、`/etc/login.defs` 和骨架目录内容等文件可能影响行为，但其作用因发行版而异。系统可能提供更高层的 `adduser` 命令，但其界面并未在所有 Linux 系统中标准化。

## 明确创建本地账户

在受控环境中，应指定重要属性，而不是依赖未知默认值：

```bash
$ sudo useradd -m -s /bin/bash -c "Bob Example" bob
```

- `-m` 请求创建主目录。
- `-s /bin/bash` 在确认该路径获准且已安装后选择登录 shell。
- `-c` 提供 GECOS/注释字段。

新账户通常要设置可用的本地密码后才能认证，但确切的初始密码和锁定状态取决于本地工具与策略。应验证记录，而不是想当然：

```bash
$ getent passwd bob
$ sudo passwd -S bob
$ id bob
```

:::single-choice{#user-tools-create-home} 哪个 `useradd` 选项会明确请求创建新账户的主目录？

::option[`-M`]{#user-tools-no-home-option explanation="大写 `-M` 会明确告诉常见 `useradd` 实现不要创建主目录。"}
::option[`-s`]{#user-tools-shell-option explanation="`-s` 选项选择登录 shell，本身不会创建主目录。"}
::option[`-m`]{#user-tools-home-option .correct explanation="小写 `-m` 会请求 `useradd` 按本地默认值创建并填充主目录。"}
:::

## 设置或更改密码

普通用户使用交互式命令更改自己的本地密码：

```bash
$ passwd
```

获准的管理员可以设置另一个本地账户的密码：

```bash
$ sudo passwd bob
```

只能在受保护的提示中输入密码，不要把密码放入命令参数、shell 历史、课程笔记或聊天。PAM 策略可能拒绝弱密码或重复使用的密码。目录服务管理的账户可能需要其他工具。

:::single-choice{#user-tools-change-own-password} 哪个命令通常让当前用户通过交互式提示更改自己的密码？

::option[`useradd`]{#user-tools-add-not-password explanation="`useradd` 创建账户记录，不是普通的交互式密码更改命令。"}
::option[`userdel`]{#user-tools-delete-not-password explanation="`userdel` 删除本地账户，与更改调用用户的密码无关。"}
::option[`passwd`]{#user-tools-passwd-self .correct explanation="不带用户名操作数时，`passwd` 会在 PAM 策略下处理调用用户的本地密码。"}
:::

## 修改账户属性和组

`usermod` 会更改本地账户字段。例如：

```bash
$ sudo usermod -s /bin/zsh bob
$ sudo usermod -d /srv/home/bob -m bob
$ sudo usermod -aG developers bob
```

移动主目录前，应验证目标、所有权、可用空间、正在运行的进程、挂载和服务。对于附加组，`-aG` 表示追加到当前列表。使用 `-G` 而省略 `-a` 会替换整个附加组列表，并可能意外移除访问权限。

组更改通常影响新的登录会话，而不是已在旧凭据集合下运行的进程。

:::single-choice{#user-tools-append-group} 哪个命令会把 `bob` 加入附加组 `developers`，而不替换他的其他附加成员身份？

::option[`usermod -G developers bob`]{#user-tools-replace-groups explanation="没有 `-a` 时，`-G` 会替换附加组列表，并可能移除现有成员身份。"}
::option[`usermod -aG developers bob`]{#user-tools-append-groups .correct explanation="`-a` 选项会追加 `-G` 指定的组，同时保留其他附加成员身份。"}
::option[`groupdel developers bob`]{#user-tools-delete-group explanation="`groupdel` 会删除组定义，并不会追加用户成员身份。"}
:::

## 锁定本地密码

管理员可以使用 `passwd -l USER` 锁定本地密码哈希，并用 `passwd -S USER` 检查状态。只有审查锁定原因并确认仍有有效哈希后，才能使用 `passwd -u USER` 解锁。

密码锁定不一定会阻止 SSH 密钥、令牌、计划任务、已经运行的进程或服务特定认证。要全面禁用账户，应先定义威胁和访问路径，再应用协调策略，其中可能包括账户过期、登录 shell、服务访问、密钥和会话终止。

:::single-choice{#user-tools-password-lock-scope} `passwd -l bob` 主要锁定什么？

::option[该账户的每一种可能认证和执行路径。]{#user-tools-lock-everything explanation="密钥、令牌、任务、服务和现有会话可能需要单独控制。"}
::option[当前由 Bob 的 UID 拥有的所有文件。]{#user-tools-lock-files explanation="密码状态不会改变文件系统所有权，也不会自动使所有数据无法访问。"}
::option[密码认证所用的本地 Unix 密码哈希。]{#user-tools-lock-local-password .correct explanation="该命令会为本地密码哈希添加前缀或以其他方式禁用它，阻止通过该路径进行普通验证。"}
:::

## 有意删除本地账户

普通 `userdel bob` 会删除本地账户记录，但通常会保留主目录。`userdel -r bob` 还会尝试删除主目录和邮件 spool，因此属于破坏性操作。

执行任何删除前：

1. 使用 `getent passwd bob` 和 `id bob` 确认准确账户。
2. 找出正在运行的进程、计划任务、服务、密钥和委派访问。
3. 盘点预期文件系统中由该 UID 拥有的文件。
4. 决定数据应转移、归档、保留还是安全删除。
5. 确认仍有孤立文件时不会重新分配该 UID。

`userdel -r` 不保证删除配置主目录和邮件位置之外的文件。账户删除也可能留下文件的数值所有权、数据库权限、应用身份和远程目录记录。

:::single-choice{#user-tools-userdel-r-scope} 与普通 `userdel bob` 相比，常见的 `userdel -r bob` 还会请求删除什么？

::option[每个已挂载文件系统中具有 Bob UID 的所有文件。]{#user-tools-delete-all-owned explanation="该工具不会普遍发现并擦除所有存储中由该 UID 拥有的文件。"}
::option[用户名同样为 `bob` 的每个远程账户。]{#user-tools-delete-remote explanation="`userdel` 操作相应的本地账户数据库，不会删除无关的目录服务身份。"}
::option[除账户记录外，还包括 Bob 的主目录和本地邮件 spool。]{#user-tools-delete-home-mail .correct explanation="递归账户删除选项以配置的主目录和邮件 spool 为目标，但不会删除 Bob 在其他位置拥有的每个对象。"}
:::

要在隔离环境中练习账户生命周期，可以尝试以下动手实验：

1. **[使用 useradd、usermod 和 userdel 管理 Linux 用户账户](https://labex.io/zh/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - 练习用户管理的完整生命周期，从创建和保护新账户到修改和删除账户。
2. **[使用 groupadd、usermod 和 groupdel 管理 Linux 组](https://labex.io/zh/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - 练习添加、修改和删除组的核心组管理命令行工具。
3. **[在 Linux 中配置用户账户和 Sudo 权限](https://labex.io/zh/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - 学习管理用户账户和 sudo 权限的重要技术，增强 Linux 系统安全性。

## 总结

现在，你可以用明确范围和验证来管理本地账户。

1. 创建前审查 `useradd` 默认值。
2. 明确请求主目录、shell 和元数据设置。
3. 只通过受保护的提示更改密码。
4. 追加附加组，而不替换现有列表。
5. 执行破坏性删除前盘点身份依赖关系。
