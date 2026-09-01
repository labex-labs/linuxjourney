---
lesson_id: "authentication-logging"
course_id: "logging"
lang: "zh"
order_index: 5
title: "身份验证日志"
description: "学习如何查找、解读并安全关联 Linux 身份验证记录。"
meta_title: "身份验证日志 - 日志"
meta_description: "通过检查 /var/log/auth.log 文件探索 Linux 身份验证日志。本指南帮助初学者理解用户登录事件和身份验证方式，并排查访问问题，从而提高 Linux 安全性。"
meta_keywords: "Linux 身份验证, auth.log, Linux 日志, 用户登录, Linux 安全, 系统授权, 登录故障排查, 身份验证方式, 入门, 教程, 指南, secure 日志"
---

身份验证日志有助于解释登录尝试、权限变化和会话活动。它们是安全敏感的证据，但单独一行很少能够证明用户意图或确认账户已被入侵。

## 查找身份验证记录

Debian 系的 syslog 配置通常将身份验证事件路由到 `/var/log/auth.log`，Red Hat 系配置则通常使用 `/var/log/secure`。systemd journal 可以连同单元和进程元数据保留相同事件，而集中式日志系统也可能保存权威副本。

应查明本地目的地并查询相关服务，例如：

```bash
$ sudo journalctl -u ssh.service --since '1 hour ago'
$ sudo less /var/log/auth.log
```

SSH 单元可能名为 `ssh.service` 或 `sshd.service`。这些记录会暴露账户和访问详情，因此其权限通常受到限制。

:::single-choice{#auth-logs-file-location} Linux 身份验证事件必须始终存储在哪里？

::option[存储在本地日志策略选择的目的地。]{#auth-logs-local-policy .correct explanation="不同发行版和配置可能使用文件、journal 或集中式收集器。"}
::option[每个发行版都存储在 `/var/log/auth.log`。]{#auth-logs-auth-only explanation="该路径在 Debian 系系统上很常见，但并不通用。"}
::option[存储在每个用户的 shell 历史文件中。]{#auth-logs-shell-history explanation="shell 历史记录的是用户命令，不是系统身份验证事件。"}
:::

## 解读事件

传统记录可能包含：

```text
Jan 31 10:37:50 icebox pkexec: pam_unix(polkit-1:session): session opened for user root by (uid=1000)
```

该记录标明时间、主机、发出消息的程序、PAM 模块和服务、请求的会话用户以及来源 UID。它本身无法识别 UID 1000 背后的具体人员，也不能证明该操作具有恶意。应根据事件发生时有效的账户记录解析 UID，并关联终端、远程地址、会话和周边事件。

:::single-choice{#auth-logs-uid-inference} 该记录中的 `uid=1000` 能确定什么？

::option[root 密码被错误输入了一千次。]{#auth-logs-thousand-passwords explanation="该值是身份编号，不是尝试次数。"}
::option[与发起进程关联的数字账户身份。]{#auth-logs-numeric-identity .correct explanation="还需要其他会话和账户证据，才能将操作归因到某个人。"}
::option[事件来自 TCP 端口 1000。]{#auth-logs-port explanation="UID 不是网络端口字段。"}
:::

## 调查成功与失败事件

在限定的时间范围内同时搜索已接受和已拒绝的尝试。对于 SSH，还应检查连接来源、身份验证方式、目标账户、会话打开和关闭，以及服务重启。反复失败可能源于用户错误、使用过期凭据的自动化任务、扫描或攻击；仅凭频率无法判断原因。

`last` 和 `lastb` 可以汇总系统维护的 `wtmp` 和 `btmp` 记录，但这些二进制数据库也有自己的保留和完整性限制。应将其与 journal、syslog 记录及集中式来源相互核对。

:::single-choice{#auth-logs-failed-attempts} 反复失败的登录应与哪些信息关联？

::option[只与磁盘总可用空间关联。]{#auth-logs-disk-space explanation="容量无法识别身份验证尝试的来源、目标或方式。"}
::option[来源、目标账户、方式、时间以及成功会话。]{#auth-logs-correlated-fields .correct explanation="这些细节有助于区分配置错误、用户错误、扫描和未授权访问。"}
::option[直接得出账户肯定已被入侵的结论。]{#auth-logs-certain-compromise explanation="失败可能有多种正常或恶意原因。"}
:::

## 保存证据与响应

如果怀疑发生安全事件，应记录主机时间和时区，保留原始日志及元数据，并保护所有导出副本。不要就地编辑证据。锁定账户、更改防火墙和终止会话可能中断合法访问或惊动攻击者，因此要遵循事件响应流程并保留恢复通道。

:::single-choice{#auth-logs-preservation} 调查期间应如何处理身份验证证据？

::option[为了清晰起见，在原始文件中编辑可疑行。]{#auth-logs-edit-original explanation="更改来源会破坏证据完整性。"}
::option[发布完整日志，让任何人都能识别用户。]{#auth-logs-publish explanation="身份验证记录可能暴露敏感身份和基础设施详情。"}
::option[保留原始记录，并保护导出的副本。]{#auth-logs-preserve .correct explanation="安全日志的完整性和机密性都很重要。"}
:::

## 总结

现在，你可以检查身份验证事件，而不会过度解读单条记录所能证明的内容。

1. 查明本地配置的身份验证日志目的地。
2. 结合上下文解读身份、服务、方式和会话字段。
3. 在保留的多个来源中关联失败与成功活动。
4. 保存证据，并协调可能造成中断的响应操作。
