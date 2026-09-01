---
lesson_id: "emacs-exiting-and-help"
course_id: "advanced-text-fu"
lang: "zh"
order_index: 13
title: "Emacs 退出和帮助"
description: "学习如何安全退出 Emacs、取消待处理命令、查看帮助主题和撤销更改。"
meta_title: "Emacs 退出和帮助 - 高级文本技巧"
meta_description: "学习 Emacs 退出命令以及如何访问帮助。通过这个适合初学者的教程，了解基本的 Emacs 导航和撤销功能。"
meta_keywords: "Emacs 退出，Emacs 帮助，Emacs 撤销，Emacs 教程，Linux 文本编辑器，初学者指南"
---

Emacs 为按键、函数、变量和活动模式提供上下文帮助。它还会在退出时保护已修改且访问文件的缓冲区，让你有机会保存或拒绝每次写入。

## 退出 Emacs

使用运行 `save-buffers-kill-terminal` 的 `C-x C-c`，请求关闭 Emacs 会话或终端连接：

```text
C-x C-c
```

Emacs 会检查相关的已修改文件缓冲区，并询问是否保存。请阅读每个缓冲区名称并谨慎回答。它也可能询问活动进程。如果决定前需要检查工作，请取消退出。

在 `emacsclient` 工作流或 Emacs 服务器中，具体的框架和服务器行为可能不同，但仍应认真处理已修改缓冲区的提示。

:::single-choice{#emacs-exit-key} 哪个按键序列会请求正常退出 Emacs，并检查已修改缓冲区？

::option[`C-x k`]{#emacs-exit-kill-buffer explanation="这会终止一个所选缓冲区，不会请求退出 Emacs 会话。"}
::option[`C-g`]{#emacs-exit-keyboard-quit explanation="这会取消待处理命令或提示，而不是关闭 Emacs。"}
::option[`C-x C-c`]{#emacs-exit-save-buffers .correct explanation="这会运行正常的保存缓冲区并退出流程，包括针对相关未保存工作的提示。"}
:::

## 打开帮助分派器

标准帮助前缀是 `C-h`。使用运行 help for help 的 `C-h C-h`，可以显示可用帮助命令的指引：

```text
C-h C-h
```

第二个按键会选择需要的帮助类型。

:::single-choice{#emacs-help-for-help} 哪个按键序列会说明如何使用 Emacs 帮助系统？

::option[`C-h C-h`]{#emacs-help-help .correct explanation="帮助前缀后再输入一个 `C-h`，会打开关于帮助分派器本身的帮助。"}
::option[`C-x C-h`]{#emacs-help-prefix-list explanation="这不是本课介绍的 help-for-help 序列。"}
::option[`C-h t`]{#emacs-help-tutorial-other explanation="这会直接打开教程，而不是说明更广泛的帮助菜单。"}
:::

## 描述按键和编辑器状态

常用帮助命令包括：

- `C-h k KEY`：说明某个按键序列运行什么。
- `C-h f FUNCTION`：说明 Emacs Lisp 函数。
- `C-h v VARIABLE`：说明 Emacs Lisp 变量。
- `C-h m`：说明当前主模式和次模式。
- `C-h t`：打开交互式教程。

例如，输入 `C-h k C-x C-s` 可以查看 save-buffer 按键绑定的文档。

:::single-choice{#emacs-describe-key} 你想了解 `C-x C-s` 的作用。应在该按键序列前输入哪个帮助前缀？

::option[`C-h k`]{#emacs-describe-key-answer .correct explanation="`describe-key` 会等待一个按键序列，并说明绑定到它的命令。"}
::option[`C-h f`]{#emacs-describe-function explanation="这会提示输入函数名，而不是读取按键序列来识别其绑定。"}
::option[`C-h v`]{#emacs-describe-variable explanation="这会提示输入变量名，不会检查按键绑定。"}
:::

## 取消待处理命令

如果卡在提示、输入到一半的按键序列、增量搜索或其他想取消的命令中，请使用绑定到 `keyboard-quit` 的 `C-g`：

```text
C-g
```

它不会撤销已经发生的缓冲区更改，也不会退出 Emacs。它会停止当前交互，并在可能时把控制权交还给普通编辑。

:::single-choice{#emacs-cancel-pending-command} 哪个按键通常会取消当前 Emacs 提示或待处理命令？

::option[`C-x C-c`]{#emacs-cancel-exit explanation="这会启动 Emacs 退出流程，而不只是取消当前提示。"}
::option[`C-y`]{#emacs-cancel-yank explanation="这会从 kill ring 中 yank 文本，不会取消命令。"}
::option[`C-g`]{#emacs-keyboard-quit-answer .correct explanation="`keyboard-quit` 会中止当前命令交互，并把控制权交还给 Emacs。"}
:::

## 撤销缓冲区更改

在常见 Emacs 配置中，使用 `C-/`、`C-_` 或 `C-x u` 调用撤销：

```text
C-/
```

重复撤销命令会沿最近的缓冲区更改向后移动。单纯移动光标通常不属于缓冲区更改。不同 Emacs 版本和配置可能提供 `undo-redo` 及更高级的历史工具；请对实际的撤销和重做绑定使用 `C-h k`，验证本地行为。

:::single-choice{#emacs-undo-change} 哪个按键序列是撤销最近 Emacs 缓冲区更改的标准绑定？

::option[`C-/`]{#emacs-undo-control-slash .correct explanation="`C-/` 是标准撤销绑定；常见配置中还有 `C-_` 和 `C-x u`。"}
::option[`C-x C-s`]{#emacs-undo-save explanation="这会保存当前缓冲区，而不是遍历其撤销历史。"}
::option[`C-w`]{#emacs-undo-kill explanation="这会 kill 活动区域并产生另一次更改，而不是撤销。"}
:::

请打开 `*scratch*`，做一次可丢弃更改并撤销；使用 `C-h k` 查询陌生按键；使用 `C-g` 取消迷你缓冲区提示；最后再正常退出。

## 总结

现在，你可以获取帮助并离开 Emacs，同时不忽略未保存的工作。

1. 使用 `C-x C-c` 经过已修改缓冲区检查后退出。
2. 使用 `C-h C-h` 打开关于帮助的帮助。
3. 描述按键、函数、变量或活动模式。
4. 使用 `C-g` 取消待处理命令。
5. 使用经过本地验证的绑定撤销最近的缓冲区更改。
