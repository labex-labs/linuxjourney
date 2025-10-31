---
index: 4
lang: "zh"
title: "Vim 搜索模式"
meta_title: "Vim 搜索模式 - 高级文本操作"
meta_description: "学习如何使用模式在 Vim 中执行向前和向后搜索。掌握 Vim 查找技巧以快速定位文本，并使用 'n' 和 'N' 导航结果。"
meta_keywords: "Vim 搜索，vim 查找，Vim 命令，Linux 文本编辑器，Vim 教程，Vim 指南，搜索模式"
---

## Lesson Content

在任何编辑器中搜索文本都是一项基本任务。Vim 提供了非常强大且快速的方法，可以直接在普通模式下执行 `vim search`（Vim 搜索）。让我们探索如何使用这些搜索模式来改进您的工作流程。

### 向前搜索

要在普通模式下执行标准的向前 `vim search`，只需按 `/` 键，然后输入您的搜索词。按下 Enter 后，Vim 将跳转到光标后该词的第一个匹配项。

```plaintext
My pretty file is very pretty.

/pretty

这将找到光标后的第一个“pretty”单词。
```

### 向后搜索

类似地，您可以从光标位置向后搜索。使用 `?` 键，后跟您的搜索词。Vim 将找到光标前的第一个匹配项。

```plaintext
My pretty file is very pretty.

?pretty

这将首先找到文件中最后一个“pretty”单词。
```

### 导航搜索结果

一旦启动搜索，您可以轻松地在文件中的所有匹配项之间导航。

- 按 `n` 跳转到原始搜索方向的**下一个**匹配项。
- 按 `N` 跳转到**上一个**匹配项，沿与原始搜索相反的方向移动。

### 高效的 Vim 查找

`/` 和 `?` 命令是任何 `vim lookup`（Vim 查找）操作的核心。无论您是需要查找特定的函数名、变量，还是仅仅一个单词，此搜索机制都是您的主要工具。掌握这个简单的 `vim lookup` 过程对于高效导航和编辑至关重要。

## Exercise

为了应用这些概念，请尝试以下实践实验。它将帮助您熟练掌握基本的文本编辑工具，包括搜索功能。

1. **[使用 Vim 和 Nano 在 Linux 中编辑文本文件](https://labex.io/zh/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - 练习使用 Vim 和 Nano 创建、编辑、保存和导航文本文件。

## Quiz Question

在 Vim 中启动向前搜索使用哪个键？

## Quiz Answer

/
