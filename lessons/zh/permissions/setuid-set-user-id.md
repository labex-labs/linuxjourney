---
lesson_id: "setuid-set-user-id"
course_id: "permissions"
lang: "zh"
order_index: 5
title: "Setuid"
description: "学习 set-user-ID 模式位如何影响可执行程序，以及它为何需要谨慎的安全审查。"
meta_title: "Setuid - 权限"
meta_description: "了解 Linux Setuid (SUID) 权限、它们的工作原理以及如何修改它们。理解 SUID 在 Linux 中安全文件访问的重要性。"
meta_keywords: "Linux Setuid, SUID, Linux 权限，chmod, passwd 命令，Linux 安全，Linux 初学者，Linux 教程"
---

有些程序需要调用者通常没有的、范围严格受控的访问权限。对于可执行普通文件，set-user-ID 位可以让新进程获得文件所有者的用户 ID 作为有效用户 ID。随后，程序可以执行该身份获准的操作，同时保留调用者的信息。

Setuid 并不是“以 root 身份运行”的通用指令。其效果取决于可执行文件的所有者、操作系统、文件系统和挂载选项，以及程序管理凭据的方式。

## 识别 Setuid

在使用 setuid `passwd` 可执行文件的系统上，长列表可能如下所示：

```bash
$ ls -l /usr/bin/passwd
-rwsr-xr-x 1 root root 68248 Jan 10 09:30 /usr/bin/passwd
```

所有者执行位置的小写 `s` 表示 setuid 和所有者执行都已设置。如果有 setuid 但没有所有者执行，`ls -l` 会在该位置显示大写 `S`。

不要假设每个发行版都有相同模式或认证设计。应检查实际系统，而不是依赖示例。

:::single-choice{#setuid-lowercase-s}
所有者执行位置的小写 `s` 表示什么？

::option[已设置 setuid，但没有所有者执行。]{#setuid-s-without-execute explanation="这种组合显示为大写 `S`，而不是小写 `s`。"}
::option[文件有 sticky bit 和组执行。]{#setuid-sticky-group explanation="sticky bit 出现在其他执行位置，而 setuid 出现在所有者位置。"}
::option[已设置 setuid，同时也设置了所有者执行。]{#setuid-s-with-execute .correct explanation="小写 `s` 表示 setuid 位与普通所有者执行位同时存在。"}
:::

## 理解凭据变化

当内核在执行时采用 setuid，新进程通常会根据可执行文件所有者获得有效用户 ID。对于 root 拥有的程序，这可以提供 root 获准的访问，但只在程序运行期间有效，而且仅限代码执行的操作。

这种机制可以让经过谨慎编写的程序验证请求，再对受保护状态进行受限更改。例如，本地密码更改工具可能需要受控访问普通用户无法直接编辑的认证数据。现代实现还依赖 PAM、文件锁、策略和其他保护措施；仅凭 setuid 无法解释完整工作流。

:::single-choice{#setuid-effective-identity}
采用 setuid 可执行文件时，主要从文件所有者取得哪个身份？

::option[存储在 `/etc/passwd` 中的登录名。]{#setuid-login-name explanation="执行文件不会重写调用者的账户记录或登录名。"}
::option[进程的有效用户 ID。]{#setuid-effective-user .correct explanation="set-user-ID 执行机制会改变许多授权检查使用的有效用户身份。"}
::option[每个已打开文件的组所有者。]{#setuid-opened-file-group explanation="Setuid 影响进程凭据，不会改变无关文件的所有权元数据。"}
:::

## 设置和移除该位

使用符号形式设置 setuid：

```bash
$ sudo chmod u+s myfile
```

在八进制记法中，setuid 在开头的特殊位数字中贡献 `4`：

```bash
$ sudo chmod 4755 myfile
```

这里，开头的 `4` 设置 setuid，`755` 设置普通所有者、组和其他权限位。使用 `chmod u-s myfile` 可移除 setuid，而不改变其他模式位。

:::single-choice{#setuid-octal-value}
哪个开头的八进制值表示 setuid 特殊位？

::option[`4`]{#setuid-octal-four .correct explanation="Setuid 在开头的特殊位数字中贡献值 `4`。"}
::option[`1`]{#setuid-octal-one explanation="开头的 `1` 表示 sticky bit。"}
::option[`2`]{#setuid-octal-two explanation="开头的 `2` 表示 setgid 位。"}
:::

## 把 Setuid 视为安全敏感机制

特权 setuid 程序中的缺陷可能成为权限提升路径。这类程序必须验证输入、控制其信任的环境和文件路径、避免不安全的子进程行为、尽量减少特权代码，并尽早放弃提升后的凭据。

Linux 通常不会在解释型脚本上采用 setuid，因为安全实现会遇到竞态和解释器相关问题。使用 `nosuid` 挂载的文件系统也会抑制 setuid 和 setgid 效果。需求合适时，应优先选择由服务中介的操作、范围严格的 `sudo` 策略或 capabilities 等更窄的机制。

绝不要为了在共享系统上试验，就给任意 shell、解释器或复制的程序添加 setuid。应审计现有 setuid 文件，并只在隔离的可丢弃环境中练习。

:::single-choice{#setuid-nosuid-mount}
使用 `nosuid` 挂载文件系统有什么作用？

::option[移除该文件系统中所有文件存储的执行位。]{#setuid-nosuid-remove-execute explanation="该选项不会重写文件元数据中的普通执行位。"}
::option[抑制该文件系统上的 setuid 和 setgid 执行效果。]{#setuid-nosuid-suppress .correct explanation="`nosuid` 挂载选项会阻止这些特殊模式位授予通常的凭据变更执行行为。"}
::option[让该文件系统中的所有文件归 root 所有。]{#setuid-nosuid-root-owner explanation="使用 `nosuid` 挂载不会更改用户或组所有权字段。"}
:::

## 总结

现在，你可以识别 setuid，并说明它对凭据和安全性的影响。

1. 在所有者执行位置查找 `s` 或 `S`。
2. 把 setuid 执行与可执行文件所有者的有效用户身份联系起来。
3. 使用符号或八进制 `chmod` 模式设置或移除该位。
4. 把每个特权可执行文件都视为安全敏感代码。
