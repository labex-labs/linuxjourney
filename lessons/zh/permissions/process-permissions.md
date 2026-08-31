---
lesson_id: "process-permissions"
course_id: "permissions"
lang: "zh"
order_index: 7
title: "进程权限"
description: "学习实际、有效和保存的用户 ID 如何帮助 Linux 进程跟踪调用者并管理权限。"
meta_title: "进程权限 - 权限"
meta_description: "了解 Linux 进程权限，包括真实用户 ID、有效用户 ID 和保存的用户 ID。理解 UID 如何影响安全性和命令执行。立即开始学习！"
meta_keywords: "Linux 进程权限，真实用户 ID, 有效用户 ID, 保存的用户 ID, Linux 安全，passwd 命令，Linux 教程，Linux 初学者"
---

Linux 授权检查作用于进程凭据，而不是直接作用于输入的用户名。进程拥有多个相互关联的用户和组 ID，各自承担不同角色。大多数普通程序启动时各身份相同，而特权程序可以有意使用不同值。

## 实际用户 ID

实际用户 ID 标识启动进程的账户，或其上级登录会话。程序可以查询它，以区分调用者和提升后的有效身份。

对于用户 Bob 启动的普通命令，实际用户 ID 通常等于 Bob 的 UID。创建另一个进程本身不会创建新账户或改变该身份。

:::single-choice{#process-permissions-real-uid}
进程的实际用户 ID 通常标识什么？

::option[最近打开文件的所有者。]{#process-permissions-real-opened-file explanation="打开文件不会用该文件所有者替换进程的实际 UID。"}
::option[与进程原始调用者关联的账户。]{#process-permissions-real-caller .correct explanation="实际 UID 记录进程启动时继承的调用用户身份。"}
::option[每次访问检查所选择的组。]{#process-permissions-real-group explanation="UID 是用户身份；组检查使用独立的组凭据。"}
:::

## 有效用户 ID

有效用户 ID 是许多文件系统和权限检查所用的用户凭据。通常它与实际 UID 相同。执行受到采用的 setuid 程序时，也可以从可执行文件所有者初始化它。

例如，经过谨慎设计的密码工具可以使用提升后的有效 UID 运行，以更新受保护的认证数据。程序仍必须根据调用者、请求的账户、PAM 结果和其他上下文实施策略。拥有有效 UID 并不自动表示每项请求操作都合理。

:::single-choice{#process-permissions-effective-uid}
代表进程进行的许多访问控制决策使用哪个用户 ID？

::option[有效用户 ID。]{#process-permissions-effective-active .correct explanation="有效 UID 是许多授权检查查询的活动用户凭据。"}
::option[只使用保存的用户 ID。]{#process-permissions-effective-saved-only explanation="保存的 ID 支持凭据转换，但通常不是访问检查的活动身份。"}
::option[存储在当前目录上的 UID。]{#process-permissions-effective-directory explanation="文件系统所有权是对象元数据，不是进程的活动用户凭据。"}
:::

## 保存的 Set-User-ID

保存的 set-user-ID 让程序保留一个身份，并在系统调用规则允许时恢复它。特权程序可以暂时把有效 UID 切换为权限较低的值，以降低后的权限执行普通工作，只在范围严格的操作中恢复保存的身份。

如果实现正确，这比整个程序始终保留提升权限更安全。不再需要权限时，程序应永久放弃它，并检查每一次改变凭据的调用是否失败。

:::single-choice{#process-permissions-saved-uid}
为什么特权程序可以保留保存的 set-user-ID？

::option[在受控的特权与非特权阶段之间切换有效身份。]{#process-permissions-saved-switch .correct explanation="保存的身份可以支持暂时降低权限，以及之后获准的恢复。"}
::option[自动把该 UID 分配给它读取的每个文件。]{#process-permissions-saved-file-owner explanation="读取文件不会把其所有权改为进程保存的 UID。"}
::option[为该进程替换系统账户数据库。]{#process-permissions-saved-database explanation="进程凭据不会取代账户记录或名称服务数据。"}
:::

## 用户 ID 只是凭据集合的一部分

进程也拥有实际、有效、保存和附加组凭据。文件系统 ID、capabilities、命名空间、安全模块、ACL、挂载选项和服务策略还可能进一步影响授权。因此，“UID 允许它”往往只是完整解释的一部分。

在 Linux 上，可以使用 `ps` 和 `/proc/PROCESS/status` 等工具检查凭据。可用字段和显示格式各不相同，因此应查阅本地文档，不要只为在共享系统上实验就改变凭据。

:::single-choice{#process-permissions-ordinary-identities}
对于大多数没有权限转换的普通命令，实际 UID 和有效 UID 有何关系？

::option[有效 UID 始终为零。]{#process-permissions-effective-root explanation="普通命令不会自动获得 root 的 UID。"}
::option[实际 UID 始终等于可执行文件所有者。]{#process-permissions-real-file-owner explanation="可执行文件所有者影响 setuid 行为，而不影响普通实际 UID。"}
::option[它们通常都与调用用户的 UID 相同。]{#process-permissions-uids-match .correct explanation="没有 setuid 或明确的凭据更改时，普通进程通常以相同的实际和有效身份运行。"}
:::

## 总结

现在，你可以说明 Linux 进程为何能携带多个用户身份。

1. 使用实际 UID 标识原始调用者。
2. 把有效 UID 与活动授权检查联系起来。
3. 使用保存的身份理解受控权限转换。
4. 把组 ID 和其他安全机制视为完整决策的一部分。
