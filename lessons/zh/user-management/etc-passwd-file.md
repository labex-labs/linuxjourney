---
lesson_id: "etc-passwd-file"
course_id: "user-management"
lang: "zh"
order_index: 3
title: "/etc/passwd"
description: "学习如何读取本地 passwd 记录，并将其与完整的 NSS 账户视图区分开来。"
meta_title: "/etc/passwd - 用户管理"
meta_description: "关于 Linux 中 /etc/passwd 文件的全面指南。了解如何解释用户数据字段、理解 UID，并查看 root:x:0:0:root:/root:/bin/bash 等示例。"
meta_keywords: "/etc/passwd, Linux 中的/etc/passwd, root:x:0:0:root:/root:/bin/bash, 用户 ID, UID, 用户管理，Linux 教程"
---

`/etc/passwd` 以冒号分隔的文本格式存储本地账户记录。它把登录名映射到数值 UID，并记录主 GID、描述字段、主目录路径和登录程序。

## 本地记录与解析后的账户

使用只读命令显示本地文件：

```bash
$ cat /etc/passwd
```

这不一定是系统已知的全部账户。名称服务切换（NSS）可以从文件、目录服务、系统数据库或其他配置来源解析账户。使用 `getent` 查询解析后的 passwd 数据库：

```bash
$ getent passwd
$ getent passwd root
```

第一个命令可能披露账户名称和元数据，因此公开分享前应审查输出。

:::single-choice{#passwd-query-resolved-database}
哪个命令会查询 NSS 解析后的 passwd 数据库，而不只是读取本地文件？

::option[`cat /etc/passwd`]{#passwd-cat-local explanation="这只会显示本地文件，不包含仅由其他 NSS 来源提供的账户。"}
::option[`cat /etc/shadow`]{#passwd-cat-shadow explanation="shadow 文件包含受保护的本地密码和期限数据，不应为此目的显示。"}
::option[`getent passwd`]{#passwd-getent-all .correct explanation="`getent` 会通过 NSS 查询已配置的 passwd 数据库来源。"}
:::

## 阅读七个字段

本地记录通常如下所示：

```text
root:x:0:0:root:/root:/bin/bash
```

七个以冒号分隔的字段是：

1. **登录名**：人类可读的账户名称，例如 `root`。
2. **密码字段**：在 shadow 密码系统中通常为 `x`，表示受保护的密码数据另行存储。
3. **UID**：数值用户身份。UID 0 传统上被视为超级用户。
4. **主 GID**：账户主组的数值 ID。
5. **GECOS/注释**：描述性账户信息，内部常用逗号分隔。
6. **主目录**：作为账户主目录设置的路径；该路径在磁盘上可能不存在。
7. **登录 shell/程序**：适用登录会话所请求的程序，例如 `/bin/bash` 或非登录程序。

对于格式错误或有意重复的记录，内核并不要求 UID 值唯一；但共享 UID 的账户在许多所有权和权限决策中无法区分。管理员通常应保持账户 UID 唯一。

:::single-choice{#passwd-uid-field}
在 `root:x:0:0:root:/root:/bin/bash` 中，哪个字段包含 UID？

::option[第二个字段 `x`]{#passwd-second-password explanation="第二个字段是密码占位符，不是数值用户身份。"}
::option[第四个字段，即第二个 `0`]{#passwd-fourth-gid explanation="字段 4 是主 GID，而不是 UID。"}
::option[第三个字段，即第一个 `0`]{#passwd-third-uid .correct explanation="字段 3 是 UID，因此第一个零表示该记录的 UID 为 0。"}
:::

:::single-choice{#passwd-primary-gid-field}
passwd 记录的哪个字段存储账户的主 GID？

::option[字段 5]{#passwd-gecos-five explanation="第五个字段是 GECOS 或注释字段。"}
::option[字段 4]{#passwd-gid-four .correct explanation="第四个冒号分隔字段以数值表示主组。"}
::option[字段 7]{#passwd-shell-seven explanation="第七个字段指定登录 shell 或程序。"}
:::

## 解释密码占位符

在典型 shadow 密码系统中，字段 2 的 `x` 会把密码感知工具指向 `/etc/shadow` 中受保护的数据。`*` 或 `!` 等值不是有效的密码哈希，通常会阻止通过该条目使用 Unix 密码认证。

这并不能证明账户无法通过任何方式认证。SSH 密钥、证书、令牌或服务特定机制可能彼此独立。同样，空密码字段具有取决于认证栈的安全敏感行为；不要手工创建或“修复”它。

:::single-choice{#passwd-x-placeholder}
本地 `/etc/passwd` 记录字段 2 中的 `x` 通常表示什么？

::option[保证该账户没有任何认证方式。]{#passwd-no-auth-guarantee explanation="该占位符并不描述每一种可能的认证方式，本身也不表示账户不可用。"}
::option[该账户的主目录已被删除。]{#passwd-home-deleted explanation="主目录信息位于字段 6，与 `x` 占位符无关。"}
::option[受保护的密码数据保存在 shadow 数据库中。]{#passwd-shadow-placeholder .correct explanation="公开 passwd 记录保存占位符，密码哈希和期限字段则位于受保护的 shadow 数据中。"}
:::

## 识别服务账户

许多记录代表服务而不是人。独立的服务身份有助于把文件和进程限制在某个守护进程所需的权限范围内。它们的主目录路径可能不标准或不存在，登录程序也可能是 `/usr/sbin/nologin`、`/bin/false` 或其他受限程序。

不要只凭 UID 范围推断账户用途，应检查发行版策略。分配范围各不相同，集中管理的账户也可能遵循不同约定。

:::single-choice{#passwd-nologin-shell}
字段 7 中 `/usr/sbin/nologin` 之类的登录程序通常有什么用途？

::option[每当服务停止时删除账户的文件。]{#passwd-nologin-delete explanation="登录程序不会自动删除所有数据或管理服务停止文件。"}
::option[阻止通过遵循该字段的登录路径获得普通交互式 shell。]{#passwd-nologin-purpose .correct explanation="非登录程序常用于不应通过普通登录获得交互式 shell 的服务账户。"}
::option[授予账户与 UID 0 相同的权限。]{#passwd-nologin-root explanation="限制交互式登录不会提升账户权限或改变其数值 UID。"}
:::

## 安全修改账户记录

优先使用 `useradd`、`usermod` 和 `userdel` 等账户管理工具，因为它们会协调相关记录并应用系统默认值。其确切行为可由发行版配置，所以更改账户前应审查选项。

如果确实需要手工修复本地 passwd 数据库，请使用 `vipw`，而不是普通编辑器。它提供用于避免并发编辑的锁定。请使用 `pwck` 等工具验证数据库，并在远程更改认证文件前保留恢复会话。

要在受控环境中练习用户和组记录，可以尝试以下动手实验：

1. **[使用 useradd、usermod 和 userdel 管理 Linux 用户账户](https://labex.io/zh/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - 练习用户管理的完整生命周期，从创建和保护新账户到修改和删除账户。
2. **[使用 groupadd、usermod 和 groupdel 管理 Linux 组](https://labex.io/zh/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - 练习组管理的核心命令行工具，包括创建新组和修改用户成员身份。

## 总结

现在，你可以解释本地 passwd 记录，而不会把它误认为完整身份数据库。

1. 使用 `getent passwd` 查询 NSS 解析的账户。
2. 阅读七个冒号分隔的 passwd 字段。
3. 定位 UID 和主 GID 字段。
4. 解释密码占位符，同时不过度推断登录状态。
5. 使用账户工具或 `vipw`，而不是普通编辑器。
