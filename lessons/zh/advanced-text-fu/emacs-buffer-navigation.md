---
lesson_id: "emacs-buffer-navigation"
course_id: "advanced-text-fu"
lang: "zh"
order_index: 11
title: "Emacs 缓冲区导航"
description: "学习如何切换和终止 Emacs 缓冲区，以及如何拆分、选择和关闭显示窗口。"
meta_title: "Emacs 缓冲区导航 - 高级文本操作"
meta_description: "Emacs 缓冲区导航综合指南。学习如何使用核心 Emacs 命令高效切换缓冲区、分割窗口和管理工作流程。掌握 emacs 切换缓冲区命令，提升您的文本编辑技能。"
meta_keywords: "emacs 导航，emacs 切换缓冲区，emacs 缓冲区管理，emacs 命令，C-x b, C-x k, C-x 2, 文本编辑器，linux"
---

Emacs 缓冲区保存文本或编辑器状态，而窗口负责显示缓冲区。缓冲区可以存在而不显示，多个窗口也可以显示同一个缓冲区。管理其中一个对象不会自动管理另一个。

## 切换缓冲区

使用运行 `switch-to-buffer` 的 `C-x b`，在当前窗口中按名称选择缓冲区：

```text
C-x b
```

迷你缓冲区会为已有名称提供补全。输入新名称可以创建该名称的非文件缓冲区；这不会访问文件路径。

默认情况下，`C-x Right` 运行 `next-buffer`，`C-x Left` 运行 `previous-buffer`，在所选窗口中循环切换缓冲区。

:::single-choice{#emacs-switch-buffer-key}
哪个按键序列会提示输入要在当前窗口中显示的缓冲区名称？

::option[`C-x C-f`]{#emacs-buffer-find-file explanation="这会提示输入并访问文件路径，与按名称选择已有缓冲区是不同操作。"}
::option[`C-x b`]{#emacs-switch-buffer .correct explanation="`switch-to-buffer` 会读取缓冲区名称，并在所选窗口中显示该缓冲区。"}
::option[`C-x k`]{#emacs-buffer-kill explanation="这会提示终止缓冲区，而不是把所选窗口切换到该缓冲区。"}
:::

## 拆分所选窗口

使用 `C-x 2` 把所选窗口拆分为上下两个窗口：

```text
C-x 2
```

使用 `C-x 3` 把它拆分为左右两个窗口：

```text
C-x 3
```

新窗口起初会显示一个缓冲区，通常与原窗口相同。可以在任一窗口中独立切换缓冲区。

:::single-choice{#emacs-split-side-by-side}
哪个按键序列会把所选 Emacs 窗口拆分为左右两个窗口？

::option[`C-x 1`]{#emacs-window-one explanation="这会删除其他窗口，让所选窗口成为框架中唯一的窗口。"}
::option[`C-x 2`]{#emacs-window-below explanation="这会创建上下窗口，而不是左右并排拆分。"}
::option[`C-x 3`]{#emacs-window-right .correct explanation="绑定到 `C-x 3` 的 `split-window-right` 会创建左右窗口。"}
:::

## 选择和关闭窗口

使用运行 `other-window` 的 `C-x o` 选择下一个窗口：

```text
C-x o
```

使用以下命令移除窗口显示：

- `C-x 0`：删除所选窗口。
- `C-x 1`：删除当前框架中的其他窗口。

删除窗口通常会让它所显示的缓冲区继续存在。你可以在另一个窗口中再次显示该缓冲区。

:::single-choice{#emacs-select-other-window}
哪个按键序列会把 point 和键盘焦点移动到另一个 Emacs 窗口？

::option[`C-x 0`]{#emacs-delete-selected-window explanation="这会删除所选窗口，而不是把焦点移到另一个窗口。"}
::option[`C-x o`]{#emacs-other-window .correct explanation="`other-window` 会在框架中循环选择另一个窗口。"}
::option[`C-x b`]{#emacs-switch-in-window explanation="这会改变当前窗口显示的缓冲区，而不是改变所选窗口。"}
:::

:::single-choice{#emacs-keep-one-window}
哪个按键序列会保留所选窗口，并删除其框架中的其他窗口？

::option[`C-x 1`]{#emacs-delete-other-windows .correct explanation="`delete-other-windows` 会让所选窗口成为框架中唯一的窗口。"}
::option[`C-x 0`]{#emacs-delete-current-window explanation="这会删除所选窗口本身，而不是保留它。"}
::option[`C-x 2`]{#emacs-add-lower-window explanation="这会增加另一个窗口，而不是把框架缩减为一个窗口。"}
:::

## 终止缓冲区

使用运行 `kill-buffer` 的 `C-x k`，提示选择要从 Emacs 中移除的缓冲区：

```text
C-x k
```

默认选择是当前缓冲区。如果访问文件的缓冲区有未保存更改，Emacs 会在终止前发出警告。请阅读提示；终止已修改缓冲区可能丢弃编辑。

终止缓冲区与删除窗口不同。Emacs 会在任何显示该缓冲区的窗口中替换已终止缓冲区，而删除窗口可以让其缓冲区保持不变。

:::single-choice{#emacs-kill-buffer-key}
哪个按键序列会提示终止 Emacs 缓冲区？

::option[`C-x 0`]{#emacs-kill-window-only explanation="这会删除窗口显示，但通常让缓冲区继续存在。"}
::option[`C-x k`]{#emacs-kill-buffer-answer .correct explanation="`kill-buffer` 会在完成必要的已修改缓冲区确认后，从 Emacs 中移除所选缓冲区。"}
::option[`C-x b`]{#emacs-kill-switch explanation="这会把当前窗口切换到具名缓冲区，而不会终止它。"}
:::

请使用 `*scratch*` 和可丢弃缓冲区练习这些命令。终止任何访问文件的缓冲区前，应确认其已修改标记是否表示存在未保存工作。

## 总结

现在，你可以管理 Emacs 存储的内容以及各窗口显示的内容。

1. 使用 `C-x b` 在所选窗口中切换缓冲区。
2. 使用 `C-x 2` 向下拆分，或使用 `C-x 3` 向右拆分。
3. 使用 `C-x o` 选择另一个窗口。
4. 使用 `C-x 0` 或 `C-x 1` 移除窗口显示。
5. 只有审查未保存更改后，才使用 `C-x k` 终止缓冲区。
