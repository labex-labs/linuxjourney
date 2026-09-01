---
lesson_id: "vim-search-patterns"
course_id: "advanced-text-fu"
lang: "zh"
order_index: 4
title: "Vim 搜索模式"
description: "学习如何在 Vim 中向前或向后搜索，以及如何重复、细化或清除模式匹配。"
meta_title: "Vim 搜索模式 - 高级文本操作"
meta_description: "学习如何使用模式在 Vim 中执行向前和向后搜索。掌握 Vim 查找技巧以快速定位文本，并使用 'n' 和 'N' 导航结果。"
meta_keywords: "Vim 搜索，vim 查找，Vim 命令，Linux 文本编辑器，Vim 教程，Vim 指南，搜索模式"
---

Vim 会从当前光标位置开始按模式搜索。先进入普通模式并开始向前或向后搜索，之后无需重新输入模式即可重复查找匹配项。

## 向前搜索

在普通模式中输入 `/`，键入模式，然后按 Enter。Vim 会移动到光标之后的下一个匹配项：

```vim
/pretty
```

搜索使用 Vim 的正则表达式语法，因此 `.`、`*`、`[` 和 `\` 等字符可能具有特殊含义。如果模式的其余部分应以 very nomagic 方式处理，请在开头使用 `\V`；也可以有意转义特殊字符。

:::single-choice{#vim-search-forward-key} 在普通模式中，哪个命令会开始向前搜索 `pretty`？

::option[输入 `?pretty` 后按 Enter]{#vim-backward-pretty explanation="问号会从当前光标位置开始向后搜索。"}
::option[输入 `/pretty` 后按 Enter]{#vim-forward-pretty .correct explanation="斜杠开始向前搜索，Enter 提交模式。"}
::option[输入 `:pretty` 后按 Enter]{#vim-command-pretty explanation="冒号会进入命令行模式以输入 Ex 命令；这里不能用 `pretty` 开始搜索。"}
:::

## 向后搜索

输入 `?`、键入模式并按 Enter，会移动到光标之前的上一个匹配项：

```vim
?pretty
```

这并不天然表示“文件中的最后一个匹配项”。结果取决于当前光标位置。在 Vim 默认的 `wrapscan` 设置下，搜索可以在文件开头或末尾回绕；`:set nowrapscan` 会禁用这种回绕。

:::single-choice{#vim-search-backward-key} 普通模式中的哪个搜索前缀会从光标向前面的文本查找？

::option[`/`]{#vim-slash-forward explanation="斜杠会从光标向后面的文本搜索，而不是查找之前的内容。"}
::option[`?`]{#vim-question-backward .correct explanation="问号会从当前光标位置开始向后进行模式搜索。"}
::option[`:`]{#vim-colon-command explanation="冒号会开始 Ex 命令行，并不是向后搜索前缀。"}
:::

## 重复搜索

完成任一种搜索后：

- 按 `n` 沿原来的搜索方向重复。
- 按 `N` 沿相反方向重复。

因此，在 `/pretty` 之后，`n` 向前移动，`N` 向后移动；在 `?pretty` 之后，`n` 向后移动，`N` 向前移动。

:::single-choice{#vim-repeat-backward-search} 运行 `?error` 后，哪个按键会沿同一向后方向重复搜索？

::option[`n`]{#vim-same-question-search .correct explanation="小写 `n` 会沿最近一次搜索的原始方向重复，此处原始方向是向后。"}
::option[`N`]{#vim-opposite-question-search explanation="大写 `N` 会反转原始搜索方向，因此在 `?` 搜索后会向前移动。"}
::option[`/`]{#vim-new-forward-search explanation="斜杠会开始新的向前搜索并等待输入模式，而不会重复上一搜索。"}
:::

## 搜索光标下的单词

在普通模式中，把光标放在一个单词上，然后使用：

- `*` 向前搜索该完整单词。
- `#` 向后搜索该完整单词。

这些命令会设置最近搜索模式，因此可以继续使用 `n` 和 `N`。

:::single-choice{#vim-current-word-forward} 普通模式中的哪个按键会向前搜索光标下的完整单词？

::option[`#`]{#vim-hash-current-word explanation="井号会向后搜索光标下的单词。"}
::option[`*`]{#vim-star-current-word .correct explanation="星号命令会根据光标下的单词构建全词模式，并向前搜索。"}
::option[`n`]{#vim-repeat-current-pattern explanation="`n` 会重复已有搜索，不会先根据当前单词创建模式。"}
:::

## 控制大小写和高亮

Vim 选项可以改变大小写行为：

- `:set ignorecase` 让搜索忽略大小写。
- 同时设置 `ignorecase` 时，`:set smartcase` 会让包含大写字符的模式恢复区分大小写。
- 模式中的 `\c` 强制该次搜索忽略大小写。
- `\C` 强制该次搜索区分大小写。

例如，无论当前大小写选项如何，`/\cerror` 都会匹配 `error`、`Error` 和 `ERROR`。

启用搜索高亮时，`:nohlsearch` 会清除当前可见高亮，但不会删除搜索模式。下一次搜索或重复操作仍可再次高亮匹配项。

:::single-choice{#vim-force-case-insensitive} 哪个模式会强制一次针对 `error` 的 Vim 搜索忽略大小写，而不受当前大小写选项影响？

::option[`/\Cerror`]{#vim-pattern-match-case explanation="大写 `\C` 会强制区分大小写，行为正好相反。"}
::option[`/:error`]{#vim-pattern-colon-error explanation="这里模式内的冒号是字面字符，并不控制大小写处理。"}
::option[`/\cerror`]{#vim-pattern-ignore-case .correct explanation="`\c` 原子会让该次搜索不区分大小写，因此不同大写形式均可匹配。"}
:::

要在可控文件中练习 Vim 导航和搜索，可以尝试以下动手实验：

1. **[在 Linux 中使用 Vim 和 Nano 编辑文本文件](https://labex.io/zh/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - 练习使用 Vim 和 Nano 创建、编辑、保存和导航文本文件。

## 总结

现在，你可以搜索 Vim 缓冲区，并可预测地在匹配项之间移动。

1. 使用 `/` 开始向前搜索，使用 `?` 开始向后搜索。
2. 使用 `n` 沿相同方向重复，使用 `N` 沿相反方向重复。
3. 使用 `*` 或 `#` 搜索光标下的完整单词。
4. 为单个模式或通过选项控制大小写行为。
5. 清除高亮，同时保留当前搜索模式。
