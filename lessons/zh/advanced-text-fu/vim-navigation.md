---
lesson_id: "vim-navigation"
course_id: "advanced-text-fu"
lang: "zh"
order_index: 5
title: "Vim 导航"
description: "学习如何在 Vim 普通模式中按字符、单词、行和文件位置移动。"
meta_title: "Vim 导航 - 高级文本操作"
meta_description: "学习使用 h、j、k、l 键进行 Vim 导航基础知识。了解对初学者至关重要的 Vim 移动操作，并提高您的 Linux 命令行技能。"
meta_keywords: "Vim 导航，Vim 教程，Linux Vim, Vim 移动，Vim 基础，初学者 Vim, Linux 文本编辑器，Vim 指南"
---

Vim 提供无需鼠标即可在终端中使用的键盘移动命令。有些 Vim 配置也支持鼠标输入，但学会移动命令后，就能把导航与编辑命令组合起来。

练习前请按 `Esc` 返回普通模式。

## 按字符和屏幕行移动

普通模式中最基本的移动命令是：

- `h`：向左移动一个字符。
- `j`：向下移动一行。
- `k`：向上移动一行。
- `l`：向右移动一个字符。

方向键通常也能完成类似移动，但 `h`、`j`、`k` 和 `l` 能让双手靠近其他命令。在发生换行显示的行上，`j` 和 `k` 通常按文件行移动；`gj` 和 `gk` 则按屏幕上显示的行移动。

:::single-choice{#vim-navigation-down} 在普通模式中，哪个按键会让光标向下移动一行？

::option[`k`]{#vim-nav-k-up explanation="`k` 移动命令会向上移动一行。"}
::option[`l`]{#vim-nav-l-right explanation="`l` 移动命令会向右移动一个字符。"}
::option[`j`]{#vim-nav-j-down .correct explanation="在普通模式中，`j` 移动命令会向下移动一行。"}
:::

## 在移动命令前添加计数

在许多移动命令前输入正整数，可以重复该移动。例如：

```text
5j
3l
```

`5j` 向下移动五行；如果位置允许，`3l` 向右移动三个字符。计数也可以与单词移动和编辑命令组合。

:::single-choice{#vim-navigation-count} 普通模式中的 `4k` 会做什么？

::option[如果可以，向下移动四行。]{#vim-nav-four-down explanation="向下移动使用 `j`；`k` 的方向相反。"}
::option[如果可以，向上移动四行。]{#vim-nav-four-up .correct explanation="计数 `4` 会把向上的 `k` 移动重复四次。"}
::option[删除光标上方的四行。]{#vim-nav-delete-four explanation="移动命令本身只改变光标位置；删除需要 `d` 等操作符。"}
:::

## 按单词移动

常用的单词移动命令包括：

- `w`：移动到下一个单词的开头。
- `b`：移动到当前或上一个单词的开头。
- `e`：移动到当前或下一个单词的末尾。

大写的 `W`、`B` 和 `E` 使用由空白分隔的 WORD，对标点的处理方式不同。可以添加计数来跨越多个单词，例如 `3w`。

:::single-choice{#vim-navigation-next-words} 普通模式中的哪个命令会向前移动到第三个后续单词位置的开头？

::option[`3w`]{#vim-nav-three-words .correct explanation="该计数会把“下一个单词”移动重复三次。"}
::option[`w3`]{#vim-nav-word-three explanation="这种命令形式要求计数位于移动命令之前；把 `3` 放在后面不能表达所需移动。"}
::option[`3b`]{#vim-nav-three-back explanation="`b` 会朝更早的单词开头移动，而不是向前。"}
:::

## 在行内移动

以下移动命令定位当前行中的位置：

- `0`：移动到第零列。
- `^`：移动到第一个非空白字符。
- `$`：移动到行尾。

对于有缩进的行，`0` 和 `^` 的区别很重要。

:::single-choice{#vim-navigation-first-nonblank} 哪个移动命令会到达缩进行的第一个非空白字符？

::option[`0`]{#vim-nav-column-zero explanation="零会移动到第一列，其中可能包含缩进空白。"}
::option[`$`]{#vim-nav-line-end explanation="美元符号移动命令的目标是行尾。"}
::option[`^`]{#vim-nav-first-nonblank .correct explanation="脱字符移动命令会跳过行首空白，落在第一个非空白字符上。"}
:::

## 在文件中移动

普通模式中的以下命令可用于较大范围的跳转：

- `gg`：移动到第一行。
- `G`：移动到最后一行。
- `42G`：移动到第 42 行。
- `Ctrl+F`：向前移动大约一屏。
- `Ctrl+B`：向后移动大约一屏。

输入命令 `:42` 后按 Enter，也可以跳转到第 42 行。

:::single-choice{#vim-navigation-file-end} 普通模式中的哪个命令会移动到缓冲区最后一行？

::option[`gg`]{#vim-nav-first-line explanation="小写 `gg` 会移动到第一行，而不是最后一行。"}
::option[`$`]{#vim-nav-current-line-end explanation="美元符号移动命令会到达当前行末尾，而不是文件末尾。"}
::option[`G`]{#vim-nav-last-line .correct explanation="不带计数的大写 `G` 会跳转到最后一行。"}
:::

要在编辑可丢弃文件时练习键盘导航，可以尝试以下动手实验：

1. **[在 Linux 中使用 Vim 和 Nano 编辑文本文件](https://labex.io/zh/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - 在真实 Linux 环境中使用 Vim 和 Nano 练习创建文件、编辑文本、保存文件和导航。

## 总结

现在，你可以按多种实用尺度在 Vim 缓冲区中导航。

1. 使用 `h`、`j`、`k` 和 `l` 按字符或行移动。
2. 使用数字前缀重复移动。
3. 使用 `w`、`b` 和 `e` 在单词边界之间移动。
4. 定位行首、第一个文本或行尾。
5. 使用 `gg`、`G` 或行号跳转到文件位置。
