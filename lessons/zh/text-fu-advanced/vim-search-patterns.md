---
index: 4
lang: "zh"
title: "Vim 搜索模式"
meta_title: "Vim 搜索模式 - 高级文本技巧"
meta_description: "学习 Vim 搜索模式：向前 (/) 和向后 (?) 搜索。使用 'n' 和 'N' 导航结果。立即提升您的 Vim 技能！"
meta_keywords: "Vim 搜索，Vim 命令，Linux 文本编辑器，Vim 教程，Vim 指南，Vim 初学者"
---

## Lesson Content

要在 Vim 会话中搜索表达式，只需键入 `/` 键，然后输入您的搜索词。按下 Enter 键后，您可以按 `n` 向前或按 `N` 向后浏览搜索结果。

```plaintext
My pretty file is very pretty.

/pretty

will find the pretty words in the text file.
```

`?` 搜索命令将向后搜索文本文件。因此，在前面的示例中，最后一个“pretty”将首先出现。

```plaintext
My pretty file is very pretty.

?pretty

will find the pretty words in the text file.
```

## Exercise

熟能生巧！以下是一些动手实验，以巩固您对 Linux 中文本编辑和搜索的理解：

1. **[使用 Vim 和 Nano 在 Linux 中编辑文本文件](https://labex.io/zh/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - 练习使用 Vim 和 Nano 创建、编辑、保存和导航文本文件。本实验将帮助您熟练掌握基本的文本编辑工具，包括搜索功能。

本实验将帮助您在实际场景中应用这些概念，并增强在 Linux 中操作文本文件的信心。

## Quiz Question

在 Vim 中用于搜索的键是什么？

## Quiz Answer

/
