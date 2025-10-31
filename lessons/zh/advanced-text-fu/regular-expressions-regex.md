---
index: 1
lang: "zh"
title: "正则表达式 (Regex)"
meta_title: "正则表达式 (Regex) - 高级文本操作"
meta_description: "通过我们的正则表达式 (regex) 指南，掌握 Linux 基础知识。学习使用 ^、$ 和 [] 等语法进行模式匹配。这是学习 Linux 文本操作和提升技能的最佳途径之一。"
meta_keywords: "正则表达式 linux, regex, linux 基础，模式匹配，grep, 文本处理，学习 linux, linux 教程，最快掌握 linux 高级技能"
---

## Lesson Content

正则表达式，通常简称为 regex，是一种强大的基于模式的文本选择工具。理解它们是掌握 Linux 文本操作的基础。虽然有很多学习 Linux 的应用程序，但深入研究“regular expression linux”等核心概念是快速达到 Linux 高级熟练度的途径。它们使用特殊的表示法，其中一些类似于 `*` 这样的通配符。

让我们探索一些最常见的 regex 运算符，它们在几乎所有编程语言中都是通用的。我们将使用以下文本作为示例：

```plaintext
sally sells seashells
by the seashore
```

### 锚定到行首

脱字符 `^` 符号匹配一行的开头。它确保你的模式只出现在起始位置。

```plaintext
^by
```

此模式将匹配“by the seashore”这一行，但不会匹配“sally sells seashells”。

### 锚定到行尾

美元符号 `$` 匹配一行的末尾。它是 `^` 锚的对应项。

```plaintext
seashore$
```

此模式将匹配“by the seashore”这一行，因为它以“seashore”结尾。

### 匹配任意单个字符

句点 `.` 是一个通配符，匹配任何单个字符。

```plaintext
b.
```

在我们的示例中，这将匹配“by”。

### 使用方括号进行字符集匹配

方括号 `[]` 允许你指定一组要匹配的字符。这比 `.` 通配符提供了更多的控制。

```plaintext
s[ae]lls
```

这将匹配“sells”，也会匹配“salls”。

你也可以使用方括号来指定 _不_ 匹配什么。当脱字符 `^` 是方括号内的第一个字符时，它会否定该集合，匹配除列出的字符 _之外_ 的任何字符。

```plaintext
s[^e]lls
```

这将匹配“salls”但不会匹配“sells”。

最后，方括号支持范围，可以有效地定义一组较大的字符。

```plaintext
d[a-c]g
```

此模式将匹配“dag”、“dbg”和“dcg”。请注意，范围是区分大小写的。例如，`[a-c]` 不会匹配 `A`、`B` 或 `C`。

学习这些运算符是提高 Linux 命令行效率的最佳方法之一。

## Exercise

将你的知识付诸实践。这里有一些实践实验，以加强你对正则表达式和模式匹配的理解：

1. **[在 Linux 中使用 grep 搜索文本](https://labex.io/zh/labs/comptia-search-text-with-grep-in-linux-590841)** - 在此实验中，你将学习如何使用 `grep` 命令在 Linux 系统上的文件中搜索文本。你将执行基本搜索、显示行号、使用 `^` 和 `$` 等锚点来匹配行位置，并利用基本和扩展正则表达式进行复杂的模式匹配。
2. **[文本处理与正则表达式](https://labex.io/zh/labs/linux-text-processing-and-regular-expressions-18003)** - 学习强大的文本处理工具 grep、sed 和 awk。学习在 Linux 中使用正则表达式进行高效的文本操作和模式匹配。
3. **[提取邮件和数字](https://labex.io/zh/labs/linux-extracting-mails-and-numbers-17991)** - 在此挑战中，你将学习如何使用 grep 和正则表达式从文件中提取电子邮件地址和数字，展示基本的 Linux 文本处理技能。

这些实验将帮助你在真实场景中应用这些概念，并增强你对正则表达式和文本处理的信心。

## Quiz Question

你会使用哪个正则表达式来匹配任何单个字符？

## Quiz Answer

.
