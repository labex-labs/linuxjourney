---
lesson_id: "vim-inserting-appending-text"
course_id: "advanced-text-fu"
lang: "zh"
order_index: 6
title: "Vim 插入和追加文本"
description: "学习 Vim 如何在当前光标位置之前、之后、上方或下方进入插入模式。"
meta_title: "Vim 插入和追加文本 - 高级文本技巧"
meta_description: "学习 Vim 插入模式与追加模式的区别。掌握 'i'、'a' 和 'o' 等命令，高效编辑文本、追加内容和添加新行。"
meta_keywords: "vim 追加，vim 追加与插入的区别，vim 插入与追加，vim 添加行，vim 文本编辑，vim 命令，vim 教程，插入模式，追加模式"
---

在普通模式中，Vim 会把按键解释为命令；插入模式则把输入的文本插入缓冲区。多个普通模式命令可以在不同位置进入插入模式，让你无需另行导航即可开始输入。

按 `Esc` 可离开插入模式并返回普通模式。如果不确定当前处于哪个模式，按 `Esc` 是重新确立普通模式的安全方法，不过它可能取消尚未完成的操作。

:::single-choice{#vim-insert-return-normal}
哪个按键通常会从插入模式返回普通模式？

::option[`Esc`]{#vim-insert-escape .correct explanation="Escape 会结束当前插入并让 Vim 返回普通模式。"}
::option[`Enter`]{#vim-insert-enter explanation="Enter 会插入换行，同时仍停留在插入模式。"}
::option[`Tab`]{#vim-insert-tab explanation="Tab 会插入缩进或触发配置好的补全行为，通常不会离开插入模式。"}
:::

## 在光标前后插入

在普通模式中：

- `i`：在光标之前进入插入模式。
- `a`：在光标之后进入插入模式。

例如，如果光标位于 `abc` 中的 `b` 上，`i` 会从 `b` 之前开始，而 `a` 会从 `b` 之后开始。两个命令都会切换模式；随后输入的文本才会执行插入。

:::single-choice{#vim-insert-before-cursor}
普通模式中的哪个按键会在光标紧前方进入插入模式？

::option[`a`]{#vim-insert-a-after explanation="小写 `a` 会在光标之后追加，而不是在之前插入。"}
::option[`o`]{#vim-insert-o-below explanation="小写 `o` 会在当前行下方打开新行，然后进入插入模式。"}
::option[`i`]{#vim-insert-i-before .correct explanation="小写 `i` 会在当前光标位置开始插入，也就是光标下字符之前。"}
:::

## 在行边界插入

大写命令会定位当前行中有意义的位置：

- `I`：在第一个非空白字符之前进入插入模式。
- `A`：在行尾进入插入模式。

在有缩进的行上，`I` 会跳过缩进，从第一个非空白文本之前开始。如果确实需要在第零列插入，请使用 `0i`。

:::single-choice{#vim-insert-first-nonblank}
普通模式中的哪个命令会从当前行第一个非空白字符之前开始插入？

::option[`i`]{#vim-insert-lower-i explanation="小写 `i` 使用当前光标位置，不会先定位该行开头的文本。"}
::option[`A`]{#vim-insert-capital-a explanation="大写 `A` 会从当前行末尾开始插入。"}
::option[`I`]{#vim-insert-capital-i .correct explanation="大写 `I` 会移动到第一个非空白字符，并在它之前进入插入模式。"}
:::

:::single-choice{#vim-append-line-end}
普通模式中的哪个命令会移动到当前行末尾并进入插入模式？

::option[`A`]{#vim-append-capital-a .correct explanation="大写 `A` 把跳转到行尾和进入插入模式组合在一起。"}
::option[`$`]{#vim-move-line-end explanation="美元符号移动命令会到达行尾，但仍停留在普通模式。"}
::option[`a`]{#vim-append-one-position explanation="小写 `a` 会从当前光标之后开始，而不会跳转到行尾。"}
:::

## 打开新行

在普通模式中：

- `o`：在当前行下方打开新行并进入插入模式。
- `O`：在当前行上方打开新行并进入插入模式。

Vim 会根据当前设置和文件类型规则应用缩进。计数可以重复打开行的操作，但请先学会单行形式，使最终光标位置可以预测。

:::single-choice{#vim-open-line-above}
普通模式中的哪个命令会在当前行上方打开新行并进入插入模式？

::option[`o`]{#vim-open-lower-o explanation="小写 `o` 会在当前行下方打开新行。"}
::option[`O`]{#vim-open-upper-o .correct explanation="大写 `O` 会在上方打开新行，并在那里开始插入。"}
::option[`A`]{#vim-open-upper-a explanation="大写 `A` 会在已有行末尾追加，不会在其上方打开新行。"}
:::

要练习在普通模式和插入模式之间切换，可以尝试以下动手实验：

1. **[在 Linux 中使用 Vim 和 Nano 编辑文本文件](https://labex.io/zh/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - 使用 vi/vim 和 nano 练习创建文件、编辑文本、保存文件和导航，掌握 Vim 普通模式与插入模式的基本技能。

## 总结

现在，你可以在新文本应出现的位置进入插入模式。

1. 使用 `Esc` 返回普通模式。
2. 使用 `i` 或 `a` 在光标前后插入。
3. 使用 `I` 或 `A` 在第一个文本处或行尾插入。
4. 使用 `o` 在下方打开新行。
5. 使用 `O` 在上方打开新行。
