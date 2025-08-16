---
lang: "zh"
title: "Vim 搜索模式"
description: "学习 Vim 搜索模式：向前 (/) 和向后 (?) 搜索。使用'n'和'N'导航结果。立即提高您的 Vim 技能！"
keywords: "Vim 搜索，Vim 命令，Linux 文本编辑器，Vim 教程，Vim 指南，Vim 初学者"
---

## Lesson Content

要在 Vim 会话中搜索表达式，只需键入`/`键，然后输入您的搜索词。按下 Enter 键后，您可以按`n`向前或按`N`向后浏览搜索结果。

```plaintext
My pretty file is very pretty.

/pretty

will find the pretty words in the text file.
```

`?`搜索命令将向后搜索文本文件。因此，在前面的示例中，最后一个“pretty”将首先出现。

```plaintext
My pretty file is very pretty.

?pretty

will find the pretty words in the text file.
```

## Exercise

尝试使用搜索键。使用`vim [textfile]`在 Vim 中打开一个文本文件并开始搜索！

## Quiz Question

在 Vim 中用于搜索的键是什么？

## Quiz Answer

/
