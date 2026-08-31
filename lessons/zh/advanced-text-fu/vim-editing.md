---
lesson_id: "vim-editing"
course_id: "advanced-text-fu"
lang: "zh"
order_index: 7
title: "Vim 编辑"
description: "学习 Vim 如何组合操作符、移动命令、寄存器、放置和撤销命令来编辑文本。"
meta_title: "Vim 编辑 - 高级文本技巧"
meta_description: "关于基本编辑命令的 Vim 入门教程。学习如何在 Vim 文本编辑器中删除、更改、复制（复制）和粘贴文本，以提高您的 Linux 工作流程。"
meta_keywords: "Vim 编辑，Vim 命令，Linux 文本编辑器，Vim 教程，Vim 指南，Vim 入门，dd 命令，Vim 删除"
---

Vim 编辑命令通常把操作符与移动命令或文本对象组合起来。这种语法让同一种操作可以作用于字符、单词、行及更大范围。练习前请按 `Esc` 返回普通模式。

## 组合操作符与移动命令

一般形式为：

```text
[count] operator [count] motion
```

常用操作符包括：

- `d`：删除文本。
- `c`：更改文本，然后进入插入模式。
- `y`：抽取（yank），也就是复制文本。

例如，`dw` 会删除 `w` 移动命令覆盖的范围，`d$` 则从光标删除到行尾。`2dw` 会把删除操作应用于两次单词移动。

:::single-choice{#vim-edit-operator-motion}
在普通模式中，`d$` 会做什么？

::option[从光标开始删除整个文件。]{#vim-edit-delete-file-end explanation="美元符号移动命令指向当前行末尾，而不是整个缓冲区末尾。"}
::option[从光标删除到行尾。]{#vim-edit-delete-line-end .correct explanation="`d` 操作符会作用于 `$` 表示的行尾移动范围。"}
::option[移动到行尾而不更改文本。]{#vim-edit-move-line-end explanation="单独使用 `$` 只会移动，但前面的 `d` 会把覆盖范围变为删除操作。"}
:::

## 编辑字符和行

以下命令是方便的快捷形式：

- `x`：删除光标下的字符。
- `dd`：按整行删除当前行。
- `3dd`：从当前行开始删除三行。
- `cc`：更改当前行并进入插入模式。
- `r{char}`：用 `{char}` 替换光标下的字符。
- `R`：进入替换模式，直到按下 `Esc`。

像 `dd` 这样重复操作符会使其按行工作。添加计数可以扩大行数。

:::single-choice{#vim-edit-delete-three-lines}
普通模式中的哪个命令会删除当前行及其后两行？

::option[`dd3`]{#vim-edit-dd-three explanation="在这种命令形式中，计数应位于重复操作符之前。"}
::option[`3x`]{#vim-edit-three-x explanation="这会删除光标下及其后的三个字符，而不是三整行。"}
::option[`3dd`]{#vim-edit-three-dd .correct explanation="该计数作用于按行执行的 `dd` 命令，从当前行起删除三行。"}
:::

## 更改文本并进入插入模式

`c` 操作符会删除选定文本并进入插入模式，以便输入替代内容：

- `ce`：更改到单词末尾。
- `c$`：更改到行尾。
- `cc`：更改完整的当前行。
- `ciw`：更改光标下的内部单词。
- `caw`：更改一个单词文本对象，包括 Vim 所定义的周围空白。

`cw` 的行为有一个历史特例，通常与 `ce` 相似。`iw` 等文本对象可以更清楚地表达预期边界。

:::single-choice{#vim-edit-change-inner-word}
普通模式中的哪个命令会删除光标下的内部单词，并进入插入模式以进行替换？

::option[`diw`]{#vim-edit-delete-inner-word explanation="这会删除内部单词，但仍停留在普通模式，不会开始输入替代文本。"}
::option[`yiw`]{#vim-edit-yank-inner-word explanation="这会抽取内部单词，不更改缓冲区，也不进入插入模式。"}
::option[`ciw`]{#vim-edit-change-inner-word-answer .correct explanation="`c` 操作符会更改 `iw` 文本对象，然后进入插入模式。"}
:::

## 抽取和放置文本

Vim 把复制称为**抽取（yank）**，把粘贴称为**放置（put）**：

- `yw`：抽取单词移动覆盖的范围。
- `yy`：抽取当前行。
- `p`：字符式文本放在光标之后，行式文本放在当前行下方。
- `P`：放在光标之前或当前行上方。

删除和更改也会把文本存入寄存器，因此后续的 `p` 可能会放置最近删除的文本，而不是更早抽取的内容。具名寄存器可以保留特定文本，但开始时应先留意最近一次操作存储了什么。

:::single-choice{#vim-edit-yank-put-line}
使用 `yy` 抽取当前行后，哪个命令会把该行放在当前行下方？

::option[`p`]{#vim-edit-put-below .correct explanation="对于按行抽取的文本，小写 `p` 会把存储的行放在当前行下方。"}
::option[`P`]{#vim-edit-put-above explanation="大写 `P` 会把行式文本放在当前行上方。"}
::option[`u`]{#vim-edit-undo-not-put explanation="小写 `u` 会撤销更改，不会放置抽取的行。"}
:::

## 撤销、重做和重复

在普通模式中：

- `u`：撤销最近一次更改。
- `Ctrl+R`：重做已撤销的更改。
- `.`：在适用时于当前位置重复最近一次更改。
- `J`：连接当前行和下一行。

撤销历史适用于缓冲区更改，而不只是光标移动。应保存检查点并审查编辑结果，不要依赖无限或永久的撤销历史。

:::single-choice{#vim-edit-redo-change}
普通模式中的哪个命令会重做刚刚撤销的更改？

::option[`Ctrl+U`]{#vim-edit-control-u explanation="在普通模式中，`Ctrl+U` 会向上滚动大约半屏，并不是重做。"}
::option[`.`]{#vim-edit-dot-repeat explanation="点号会把最近一次更改作为新操作重复，而不是在撤销历史中向前移动。"}
::option[`Ctrl+R`]{#vim-edit-control-r .correct explanation="Vim 在普通模式中使用 `Ctrl+R` 沿撤销历史向前移动。"}
:::

要在可丢弃文本上练习操作符、移动命令和恢复，可以尝试以下动手实验：

1. **[在 Linux 中使用 Vim 和 Nano 编辑文本文件](https://labex.io/zh/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - 使用 vi/vim 和 nano 练习创建文件、编辑文本、保存文件和导航，并在真实场景中应用删除、更改、抽取和放置文本等概念。

## 总结

现在，你可以在普通模式中组合 Vim 编辑操作并从错误中恢复。

1. 把操作符与移动命令、文本对象和计数组合。
2. 按选定范围删除字符或完整行。
3. 更改文本并进入插入模式输入替代内容。
4. 抽取和放置字符式或行式文本。
5. 有意识地撤销、重做或重复更改。
