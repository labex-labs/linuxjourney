---
lesson_id: "etc-group-file"
course_id: "user-management"
lang: "zh"
order_index: 5
title: "/etc/group"
description: "学习本地组记录如何把名称映射到 GID，并列出附加成员。"
meta_title: "/etc/group - 用户管理"
meta_description: "探索 Linux 中的 /etc/group 文件以了解组管理。学习如何使用 cat /etc/group 查看组数据，并理解包括 GID 和用户列表在内的结构。本指南涵盖 etc group linux 文件的要点。"
meta_keywords: "/etc/group, /etc/group linux, linux 中的/etc/group 文件，cat /etc/group, etc group linux, 组管理，GID, Linux 权限，Linux 组"
---

`/etc/group` 存储本地组记录。它把组名映射到数值 GID，并列出显式成员，从而支持多个账户共享的访问控制。

## 本地组与解析后的组

该文件只是可能的组来源之一。NSS 可以从本地文件、目录服务或其他已配置数据库解析组。使用以下命令显示本地记录：

```bash
$ cat /etc/group
```

使用 `getent` 查询解析后的组数据库：

```bash
$ getent group
$ getent group developers
```

组列表可能披露内部账户和角色名称，因此分享前应审查输出。

:::single-choice{#group-query-resolved-database} 哪个命令会查询 NSS 解析后的组数据库？

::option[`getent group`]{#group-getent-all .correct explanation="`getent` 会查询已配置的 NSS 组记录来源。"}
::option[`cat /etc/group`]{#group-cat-local explanation="这只会读取本地组文件，可能遗漏其他来源提供的组。"}
::option[`groups /etc/group`]{#group-groups-file explanation="`groups` 需要用户名并报告成员关系，不会把本地数据库路径视为 NSS 查询。"}
:::

## 阅读四个字段

本地记录包含四个冒号分隔字段：

```text
developers:x:1500:alice,bob
```

1. **组名**：`developers`。
2. **密码字段**：通常是 `x`、`*` 或其他占位符；受保护的组密码数据可以存储在 `/etc/gshadow` 中。
3. **GID**：数值组身份，此处为 `1500`。
4. **成员列表**：以逗号分隔的显式成员名称，此处为 `alice` 和 `bob`。

组密码是一项旧功能，在某些配置中由 `newgrp` 等工具使用。它不是授予 sudo 授权的常规机制，也不应通过手工字段编辑引入。

:::single-choice{#group-gid-field} 在 `developers:x:1500:alice,bob` 中，哪个字段包含 GID？

::option[第二个字段 `x`]{#group-second-password explanation="字段 2 是组密码占位符，而不是数值身份。"}
::option[第四个字段 `alice,bob`]{#group-fourth-members explanation="字段 4 列出显式成员名称，而不是 GID。"}
::option[第三个字段 `1500`]{#group-third-gid .correct explanation="第三个冒号分隔字段是数值组 ID。"}
:::

:::single-choice{#group-explicit-member-field} 本地组记录如何表示显式成员名称？

::option[在字段 4 中用逗号分隔。]{#group-members-field-four .correct explanation="最后一个字段包含以逗号分隔的显式附加成员名称。"}
::option[在字段 2 中用空格分隔。]{#group-members-field-two explanation="字段 2 保留给密码相关数据或占位符，不是成员列表。"}
::option[把数值 UID 嵌入组名。]{#group-members-in-name explanation="组名和成员名称是不同字段；普通成员条目是登录名，不是嵌入的 UID 数字。"}
:::

## 计入主组成员身份

`/etc/group` 中的成员列表通常不会重复列出 passwd 记录把该 GID 设为主组的用户。因此，即使字段 4 中没有某位用户的名称，该用户也可能是成员。

例如，如果 Alice 的 passwd 记录把 1500 设为主 GID，那么即使本地组记录以空成员字段结尾，她仍属于 `developers`：

```text
developers:x:1500:
```

因此，只解析字段 4 会得到不完整的成员视图。

:::single-choice{#group-primary-membership-visibility} Alice 的 passwd 记录使用 GID 1500 作为主 GID，但她的名称不在组 1500 的字段 4 中。她是该组成员吗？

::option[不是，每一项成员关系都必须出现在 `/etc/group` 字段 4 中。]{#group-field-four-only explanation="这忽略了主 GID 成员身份，会漏算组成员。"}
::option[是，主组成员身份来自 passwd 记录的 GID 字段。]{#group-primary-from-passwd .correct explanation="组文件的显式列表主要用于附加成员身份；主成员身份记录在账户中。"}
::option[只有组密码字段包含她的用户名时才是。]{#group-password-member explanation="密码字段与声明主组成员身份无关。"}
:::

## 检查用户的组

使用 `id USER` 或 `groups USER` 获取解析后的账户视图：

```bash
$ id alice
$ groups alice
```

对于当前进程，普通 `id` 会报告其凭据中实际存在的组。新配置的附加成员身份通常不会出现在已经运行的登录会话中；应启动新的已认证会话，或在合适时使用 `newgrp` 等有意配置的机制。

:::single-choice{#group-current-process-credentials} 哪个命令会报告当前进程的 UID、主 GID 和附加组？

::option[`id`]{#group-current-id .correct explanation="不带用户操作数时，`id` 会报告当前进程的身份凭据。"}
::option[`cat /etc/group`]{#group-current-cat explanation="本地文件列出记录，但不会显示哪些解析后的组已在当前进程中生效。"}
::option[`getent passwd`]{#group-current-passwd explanation="这会查询账户记录，并不专门报告当前进程的附加组列表。"}
:::

## 安全更改本地组

应使用 `groupadd`、`groupmod`、`groupdel`、`gpasswd` 和 `usermod` 等工具，而不是用通用编辑器修改记录。尤其需要注意：

- `usermod -aG GROUP USER` 会追加附加组成员身份。
- 省略 `-a` 时，`usermod -G ...` 会替换附加组列表。

如果无法避免手工修复本地数据库，请使用 `vigr` 提供锁定，并使用 `grpck` 验证。远程更改身份前应保留恢复路径。

要在受控环境中练习本地组管理，可以尝试以下动手实验：

1. **[使用 useradd、usermod 和 userdel 管理 Linux 用户账户](https://labex.io/zh/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - 练习用户管理的完整生命周期，从创建和保护新账户到修改和删除账户。
2. **[使用 groupadd、usermod 和 groupdel 管理 Linux 组](https://labex.io/zh/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - 练习 `groupadd`、`usermod` 和 `groupdel` 等核心组管理命令行工具。
3. **[添加新用户和组](https://labex.io/zh/labs/linux-add-new-user-and-group-17987)** - 通过创建新用户账户、设置自定义组和管理组成员身份，模拟向服务器环境添加新团队成员。

## 总结

现在，你可以解释本地组记录，并更准确地解析完整成员关系。

1. 使用 `getent group` 查询已配置的组来源。
2. 阅读四个冒号分隔的组字段。
3. 定位数值 GID 和显式成员列表。
4. 计入 passwd 记录中的主组成员身份。
5. 依赖已更改成员身份前，先检查活动凭据。
