---
index: 1
lang: "zh"
title: "regex (正则表达式)"
meta_title: "regex (正则表达式) - 高级文本处理"
meta_description: "学习 Linux 模式匹配的正则表达式 (regex)。理解 ^、$、. 和 [] 等 regex 语法，用于文本操作。提高您的 grep 技能！"
meta_keywords: "正则表达式，regex, Linux regex, grep regex, 模式匹配，regex 教程，Linux 命令，初学者"
---

## Lesson Content

正则表达式是基于模式选择的强大工具。它们使用我们已经遇到过的特殊符号，例如 `*` 通配符。

我们将介绍几个最常见的正则表达式；这些正则表达式几乎在任何编程语言中都是通用的。

我们将使用以下短语作为测试字符串：

```plaintext
sally sells seashells
by the seashore
```

### 1. 以 ^ 开头

```plaintext
^by
would match the line "by the seashore"
```

### 2. 以 $ 结尾

```plaintext
seashore$
would match the line "by the seashore"
```

### 3. 匹配任意单个字符

```plaintext
b.
would match by
```

### 4. 使用 [] 和 () 的方括号表示法

这可能有点棘手。方括号允许我们指定方括号内找到的字符。

```plaintext
d[iou]g
would match: dig, dog, dug
```

当在方括号中使用时，前面的锚点 `^` 表示除了方括号内的字符之外的任何字符。

```plaintext
d[^i]g
would match: dog and dug but not dig
```

方括号也可以使用范围来增加您想要使用的字符数量。

```plaintext
d[a-c]g
will match patterns like dag, dbg, and dcg
```

但请注意，方括号是区分大小写的：

```plaintext
d[A-C]g
will match dAg, dBg and dCg but not dag, dbg and dcg
```

这些就是一些基本的正则表达式。

## Exercise

熟能生巧！这里有一些动手实验来巩固您对正则表达式和模式匹配的理解：

1. **[在 Linux 中使用 grep 搜索文本](https://labex.io/zh/labs/comptia-search-text-with-grep-in-linux-590841)** - 在此实验中，您将学习如何使用 `grep` 命令在 Linux 系统中搜索文件中的文本。您将执行基本搜索，显示行号，使用 `^` 和 `$` 等锚点匹配行位置，并利用基本和扩展正则表达式进行复杂的模式匹配。
2. **[文本处理和正则表达式](https://labex.io/zh/labs/linux-text-processing-and-regular-expressions-18003)** - 学习强大的文本处理工具 grep、sed 和 awk。学习使用正则表达式在 Linux 中进行高效的文本操作和模式匹配。
3. **[提取邮件和数字](https://labex.io/zh/labs/linux-extracting-mails-and-numbers-17991)** - 在此挑战中，您将学习如何使用 grep 和正则表达式从文件中提取电子邮件地址和数字，展示基本的 Linux 文本处理技能。

这些实验将帮助您在实际场景中应用概念，并增强对正则表达式和文本处理的信心。

## Quiz Question

您会使用哪个正则表达式来匹配单个字符？

## Quiz Answer

.
