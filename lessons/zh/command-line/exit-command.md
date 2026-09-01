---
lesson_id: "exit-command"
course_id: "command-line"
lang: "zh"
order_index: 19
title: "exit 命令"
description: "学习离开当前 shell，并选择它返回给调用者的状态。"
meta_title: "exit 命令 - 命令行"
meta_description: "学习 Linux exit 命令，如何关闭 shell 会话，logout 与 exit 的区别，以及退出状态值的工作原理。"
meta_keywords: "exit 命令, linux exit, logout 命令, shell 会话, 终端退出, 退出状态, bash exit"
---

shell 可以嵌套：图形终端会启动 shell，SSH 连接会启动远程 shell，而 shell 又可以启动另一个 shell。离开当前 shell 后，控制权通常会返回给启动它的对象。

## 离开当前 shell

结束 shell 会话最常用的方法是使用 `exit` 命令。当你输入 `exit` 并按回车时，当前的 shell 进程将终止。这个命令几乎适用于任何 shell 环境。

```bash
$ exit
```

如果该 shell 是图形终端标签页中的主进程，标签页可能会按终端设置关闭。在 SSH 会话中，离开远程 shell 通常会返回本地 shell。如果启动了嵌套 shell，`exit` 会返回其父 shell。

:::single-choice{#leave-current-shell} 你在另一个 shell 内启动了 Bash，现在想返回父 shell。应在嵌套 Bash 会话中运行哪个命令？

::option[`clear`]{#clear-nested explanation="`clear` 会刷新可见终端区域，但当前 shell 仍会运行。"}
::option[`exit`]{#exit-nested .correct explanation="`exit` 会终止当前 shell，让父 shell 恢复运行。"}
::option[`history -c`]{#clear-nested-history explanation="这会清空 Bash 的内存历史列表，不会终止当前 shell。"}
:::

## 返回退出状态

`exit` 命令还可以返回一个状态码。状态码为 `0` 通常表示成功，非零状态码通常表示错误或特殊情况。

```bash
$ exit 0
```

按约定，`0` 表示成功，非零值表示失败或程序定义的其他情况。如果 Bash 没有收到数字参数，它会使用运行 `exit` 前最后一条命令的状态退出。

:::single-choice{#return-success-status} 哪个命令会终止当前 shell，并明确向调用者报告成功？

::option[`exit 0`]{#exit-zero .correct explanation="状态 `0` 按约定向调用者报告成功完成。"}
::option[`exit 1`]{#exit-one explanation="非零状态按约定表示失败或其他异常结果，而不是成功。"}
::option[`logout 0`]{#logout-zero explanation="Bash 的 `logout` 用于登录 shell，并不使用这种形式设置所需状态。"}
:::

:::single-choice{#exit-without-number} 在 Bash 中，不提供数字时，`exit` 会返回什么状态？

::option[始终返回成功状态 `0`。]{#always-zero explanation="成功约定并不会强制不带参数的 `exit` 返回零；此时 Bash 会保留此前的状态。"}
::option[始终返回失败状态 `1`。]{#always-one explanation="Bash 不会让每个裸 `exit` 都返回失败状态 `1`；返回值由前一条命令决定。"}
::option[返回前一条命令的退出状态。]{#last-command-status .correct explanation="没有明确数字参数时，Bash 会使用最近一条命令的状态退出。"}
:::

## 在登录 shell 中使用 logout

Bash 的 `logout` 内建命令用于退出登录 shell：

```bash
$ logout
```

在非登录 Bash shell 中，`logout` 会报告它不是登录 shell；此时应使用 `exit`。

:::single-choice{#leave-login-shell} 哪个 Bash 内建命令专门用于离开登录 shell？

::option[`logout`]{#logout-login .correct explanation="Bash 提供 `logout` 来终止登录 shell。"}
::option[`unalias`]{#unalias-login explanation="`unalias` 会从当前 shell 删除别名定义，并不会结束会话。"}
::option[`source`]{#source-login explanation="`source` 会把文件中的命令读入当前 shell，不会终止该 shell。"}
:::

## 使用 Ctrl+D 或关闭终端

在空的交互式提示符下按 `Ctrl+D`，通常会提供终端的文件结束输入字符。Bash 一般把这种情况解释为退出请求。它不是信号，而且 Bash 的 `ignoreeof` 等 shell 设置可以改变这一行为。

关闭图形终端窗口会要求终端应用关闭其中的进程，也可能影响正在运行的任务。条件允许时应优先有序执行 `exit`，关闭会话前先检查是否还有活动工作。

## 总结

现在，你可以离开当前 shell，并传达它的完成状态。

1. 使用 `exit` 返回当前 shell 的调用者。
2. 用 `0` 表示成功，或按定义使用非零状态。
3. 理解不带参数的 `exit` 使用什么状态。
4. 只在登录 shell 中使用 `logout`。
5. 知道 `Ctrl+D` 表示文件结束输入，而不是信号。
