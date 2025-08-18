---
lang: "zh"
title: "regex (正则表达式)"
meta_description: "学习 Linux 模式匹配的正则表达式 (regex)。理解正则表达式语法，如 ^、$、. 和 []，用于文本操作。提高您的 grep 技能！"
meta_keywords: "正则表达式，regex, Linux regex, grep regex, 模式匹配，regex 教程，Linux 命令，初学者"
---

## Lesson Content

正则表达式是用于基于模式选择的强大工具。它们使用我们已经遇到过的特殊符号，例如 `*` 通配符。

我们将介绍几种最常见的正则表达式；这些几乎在任何编程语言中都是通用的。

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

### 4. 方括号 `[]` 和圆括号 `()`

这可能有点棘手。方括号允许我们指定括号内找到的字符。

```plaintext
d[iou]g
would match: dig, dog, dug
```

前面的锚点标签 `^` 在方括号中使用时，表示除方括号内字符以外的任何字符。

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

尝试将正则表达式与 `grep` 结合使用，并搜索一些文件。

```bash
grep [regular expression here] [file]
```

## Quiz Question

您会使用哪个正则表达式来匹配单个字符？

## Quiz Answer

.
