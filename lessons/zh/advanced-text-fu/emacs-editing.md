---
lesson_id: "emacs-editing"
course_id: "advanced-text-fu"
lang: "zh"
order_index: 12
title: "Emacs 编辑"
description: "学习如何移动 point、激活区域，并使用 Emacs kill ring 命令编辑文本。"
meta_title: "Emacs 编辑 - 高级文本操作"
meta_description: "通过本入门指南掌握 Emacs 编辑的基础知识。学习这款强大的 Linux 文本编辑器中用于文本导航、剪切和粘贴的基本 Emacs 命令。"
meta_keywords: "Emacs, Emacs 教程，Emacs 命令，文本编辑器，Linux 编辑器，Emacs 导航，Emacs 入门，Emacs 指南"
---

Emacs 把当前光标位置称为 **point**。移动命令会重新定位 point；编辑命令则在其周围插入、删除、kill、复制或 yank 文本。在以下按键记法中，`C-` 表示 Control，`M-` 表示 Meta，通常是 Alt。

## 按字符和行移动

方向键和其他平台导航键可能可用，但 Emacs 的标准移动命令在终端和图形会话中都可以使用：

- `C-f`：向前移动一个字符。
- `C-b`：向后移动一个字符。
- `C-n`：移动到下一行。
- `C-p`：移动到上一行。
- `C-a`：移动到行首。
- `C-e`：移动到行尾。

:::single-choice{#emacs-edit-next-line} 哪个 Emacs 按键会把 point 移动到下一行？

::option[`C-p`]{#emacs-edit-previous-line explanation="`C-p` 会移动到上一行，方向相反。"}
::option[`C-n`]{#emacs-edit-next-line-answer .correct explanation="`C-n` 表示 next-line，会把 point 向下移动到下一屏幕行的位置。"}
::option[`C-f`]{#emacs-edit-forward-character explanation="`C-f` 会向前移动一个字符，而不是到下一行。"}
:::

## 按单词和缓冲区边界移动

Meta 命令可以跨越更大的单位：

- `M-f`：向前移动一个单词。
- `M-b`：向后移动一个单词。
- `M-<`：移动到缓冲区开头。
- `M->`：移动到缓冲区末尾。

在许多键盘上，Alt 充当 Meta。如果无法使用这个组合键，先按 `Esc` 再按后续按键通常能发送等效的 Meta 命令。

:::single-choice{#emacs-edit-buffer-end} 哪个 Emacs 按键会把 point 移动到缓冲区末尾？

::option[`C-e`]{#emacs-edit-line-end explanation="`C-e` 会移动到当前行末尾，而不是整个缓冲区末尾。"}
::option[`M-<`]{#emacs-edit-buffer-start explanation="`M-<` 会移动到缓冲区开头。"}
::option[`M->`]{#emacs-edit-buffer-end-answer .correct explanation="`M->` 会把 point 移动到当前缓冲区末尾。"}
:::

## 定义区域

**mark** 是已保存的缓冲区位置。point 与 mark 之间的文本称为**区域**。按 `C-SPC`（有些文档写作 `C-space`）运行 `set-mark-command`，然后移动 point 以扩展活动区域。

在终端中，`C-SPC` 可能编码为 `C-@`。是否高亮取决于 transient-mark 设置，但 point 和 mark 仍会定义一个区域。

:::single-choice{#emacs-edit-set-mark} 哪个按键会在 point 处设置 mark，从而开始定义区域？

::option[`C-w`]{#emacs-edit-kill-region-before-mark explanation="`C-w` 会 kill 已经定义的区域，不是最初设置 mark 的命令。"}
::option[`C-y`]{#emacs-edit-yank-before-mark explanation="`C-y` 会插入 kill ring 中的文本，不会开始选择。"}
::option[`C-SPC`]{#emacs-edit-control-space .correct explanation="`set-mark-command` 会放置 mark，之后移动即可改变 mark 与 point 之间的区域。"}
:::

## Kill 或复制区域

Emacs 把被 kill 和复制的文本存入 **kill ring**：

- `C-w`：kill 活动区域，将其移除并加入 kill ring。
- `M-w`：把活动区域复制到 kill ring，而不移除它。
- `C-k`：从 point kill 到行尾；重复使用可以包含换行符。

Kill 不只是普通删除，因为被移除的文本会保留供之后 yank。

:::single-choice{#emacs-edit-copy-region} 哪个按键会把活动区域复制到 kill ring，而不移除它？

::option[`M-w`]{#emacs-edit-copy-active-region .correct explanation="绑定到 `M-w` 的 `kill-ring-save` 会复制区域而不删除它。"}
::option[`C-w`]{#emacs-edit-kill-active-region explanation="`C-w` 会移除区域，同时把它保存到 kill ring。"}
::option[`C-k`]{#emacs-edit-kill-line explanation="`C-k` 会朝行尾 kill 文本，而不是原样复制所选区域。"}
:::

## 从 Kill Ring 中 Yank

使用 `C-y` 在 point 处 yank 最近的 kill ring 条目。紧接着 yank 操作使用 `M-y`，会用更早的 kill ring 条目替换刚插入的文本；重复 `M-y` 可以循环选择条目。

```text
C-y
M-y
```

如果在 `C-y` 之后执行了其他无关命令，`M-y` 就不再拥有相同的 yank-pop 上下文。

:::single-choice{#emacs-edit-yank-latest} 哪个按键会在 point 处插入最近的 kill ring 条目？

::option[`C-y`]{#emacs-edit-yank-answer .correct explanation="绑定到 `C-y` 的 `yank` 会把最新的 kill ring 文本插入当前缓冲区。"}
::option[`M-y`]{#emacs-edit-yank-pop explanation="`M-y` 通常会用更早的条目替换刚 yank 的条目；它依赖之前的 yank 上下文。"}
::option[`C-d`]{#emacs-edit-delete-character explanation="`C-d` 会删除 point 之后的字符，不会取回 kill ring 文本。"}
:::

请在 `*scratch*` 或可丢弃文件中练习：移动 point、设置 mark、复制一个区域、kill 另一个区域，再把两者 yank 回来。只有结果值得保留时才保存。

## 总结

现在，你可以使用 point、mark 和 kill ring 导航并重新排列 Emacs 文本。

1. 使用 Control 命令按字符或行移动。
2. 使用 Meta 命令按单词或缓冲区边界移动。
3. 使用 `C-SPC` 设置 mark 以定义区域。
4. 使用 `C-w` kill，或使用 `M-w` 复制。
5. 使用 `C-y` yank，并紧接着使用 `M-y` 循环选择。
