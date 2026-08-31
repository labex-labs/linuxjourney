---
lesson_id: "regular-expressions-regex"
course_id: "advanced-text-fu"
lang: "zh"
order_index: 1
title: "regex（正则表达式）"
description: "学习锚点、字符集合、重复规则和正则表达式风格如何控制文本模式匹配。"
meta_title: "正则表达式 (Regex) - 高级文本操作"
meta_description: "通过我们的正则表达式 (regex) 指南，掌握 Linux 基础知识。学习使用 ^、$ 和 [] 等语法进行模式匹配。这是学习 Linux 文本操作和提升技能的最佳途径之一。"
meta_keywords: "正则表达式 linux, regex, linux 基础，模式匹配，grep, 文本处理，学习 linux, linux 教程，最快掌握 linux 高级技能"
---

正则表达式通常简称 **regex**，用于描述文本模式。`grep`、`sed` 和 `awk` 等工具都会使用正则表达式，但它们支持的语法可能不同，因此务必先确定所用工具和正则表达式风格。

GNU `grep` 默认使用基本正则表达式（BRE），加上 `-E` 后使用扩展正则表达式（ERE）。本课先介绍两者共有的结构，再说明常见的 ERE 扩展。

以下示例使用这段输入：

```text
sally sells seashells
by the seashore
```

## 匹配字面文本

大多数普通字符会匹配自身。模式 `seashells` 会选择任何位置包含这一确切字符序列的行：

```bash
$ grep 'seashells' sample.txt
sally sells seashells
```

请为正则表达式模式加引号，避免 shell 在匹配工具收到它们之前进行展开或拆分。正则表达式也不同于 shell 路径名展开：在正则表达式中，`*` 重复它前面的原子；在 shell glob 中，`*` 本身就是匹配一串路径名字符的通配符。

:::single-choice{#regex-versus-shell-star}
在 `ab*` 这样的正则表达式中，`*` 有什么作用？

::option[匹配当前目录中的任意文件名。]{#regex-shell-glob explanation="这描述的是命令上下文中的 shell 路径名展开，而不是正则表达式里 `*` 的含义。"}
::option[让前面的 `b` 重复零次或多次。]{#regex-repeat-b .correct explanation="正则量词作用于紧邻它之前的原子，因此 `ab*` 可以匹配 `a`、`ab`、`abb` 等。"}
::option[让完整字符串 `ab` 恰好重复两次。]{#regex-repeat-ab-twice explanation="星号只作用于前一个原子，并允许零次或多次重复，而不是让完整字符串恰好重复两次。"}
:::

## 锚定匹配位置

在方括号表达式之外，模式开头的 `^` 会把匹配锚定在行首：

```plaintext
^by
```

`$` 锚点匹配行尾：

```plaintext
seashore$
```

如果整行都必须符合模式，请组合两个锚点：

```text
^by the seashore$
```

:::single-choice{#regex-complete-line}
哪个模式只匹配完整文本为 `by the seashore` 的行？

::option[`^by the seashore$`]{#regex-anchored-line .correct explanation="脱字符要求匹配从行首开始，美元符号要求匹配在行尾结束。"}
::option[`by the seashore`]{#regex-unanchored-line explanation="没有锚点时，该字符序列也可能匹配前后还有其他文本的较长行。"}
::option[`$by the seashore^`]{#regex-reversed-anchors explanation="按预期模式，行尾锚点不能放在待匹配文本之前，行首锚点也不能放在其后。"}
:::

## 匹配一个字符

在普通的面向行正则表达式模式中，点号会匹配一个字符：

```plaintext
b.
```

它能匹配 `by`，也可能匹配 `ba` 或 `b7`。它不能匹配单独的 `b`，因为后面必须还有一个字符。若要匹配字面句点，请写成 `\.`，或把它放入适当的方括号表达式。

:::single-choice{#regex-dot-character}
以下哪个字符串不会被完整行模式 `^b.$` 匹配？

::option[`by`]{#regex-dot-by explanation="点号会匹配 `y`，所以这个两字符行符合模式。"}
::option[`b`]{#regex-dot-b .correct explanation="点号要求 `b` 后面还有一个字符，但该字符串立即结束。"}
::option[`b7`]{#regex-dot-b7 explanation="点号会匹配数字 `7`，所以这个两字符行符合模式。"}
:::

## 使用方括号表达式

方括号表达式会从指定集合中匹配一个字符：

```plaintext
s[ae]lls
```

它可以在相应位置匹配 `sells` 或 `salls`。

当 `^` 是 `[` 后面的第一个字符时，它会对集合取反：

```plaintext
s[^e]lls
```

它会匹配 `salls`，但不会匹配 `sells`，因为第一个 `s` 后面的字符不能是 `e`。

:::single-choice{#regex-negated-bracket}
`[^e]` 会匹配什么？

::option[恰好一个不是 `e` 的字符。]{#regex-not-e .correct explanation="方括号内开头的脱字符会对列出的集合取补集，而方括号表达式仍然消耗一个字符。"}
::option[行首后跟一个 `e`。]{#regex-caret-e-anchor explanation="在方括号表达式内，开头的脱字符会对集合取反，而不是锚定行首。"}
::option[零个或多个字母 `e`。]{#regex-repeat-e explanation="重复需要 `*` 等量词；这个方括号表达式匹配一个非 `e` 字符。"}
:::

范围可以描述两个端点之间的字符：

```plaintext
d[a-c]g
```

它可以匹配 `dag`、`dbg` 或 `dcg`。范围行为可能受 locale 排序规则影响。`[[:lower:]]`、`[[:upper:]]` 和 `[[:digit:]]` 等字符类通常能更清楚地表达意图。

## 重复和组合模式

在 BRE 和 ERE 中，`*` 都表示前一个原子重复零次或多次：

```text
seashells*
```

它会匹配 `seashell` 后跟零个或多个额外的 `s`。在使用 `grep -E` 的 ERE 模式下，常见运算符包括：

- `+`：重复一次或多次。
- `?`：重复零次或一次。
- `|`：匹配左侧或右侧表达式。
- `(...)`：对表达式分组。

例如：

```bash
$ grep -E '^(cat|dog)s?$' animals.txt
```

它会选择完整内容等于 `cat`、`cats`、`dog` 或 `dogs` 的行。在 BRE 模式中，这些运算符的转义规则不同，因此不要在未检查的情况下跨风格复制模式。

:::single-choice{#regex-extended-alternation}
哪个命令会为模式 `^(cat|dog)s?$` 启用扩展正则表达式语法？

::option[`grep -F '^(cat|dog)s?$' animals.txt`]{#regex-fixed-animals explanation="`-F` 会把所有正则运算符视为字面文本，因此分组、选择和可选重复都不会生效。"}
::option[`grep -E '^(cat|dog)s?$' animals.txt`]{#regex-extended-animals .correct explanation="`-E` 选择扩展正则表达式，从而启用这里的分组、选择和可选 `s`。"}
::option[`grep '^(cat|dog)s?$' animals.txt`]{#regex-basic-animals explanation="默认 grep 使用 BRE，其中这些未转义的分组和选择字符不具有预期的 ERE 含义。"}
:::

要练习使用 Linux 文本工具进行正则选择，可以尝试以下动手实验：

1. **[在 Linux 中使用 grep 搜索文本](https://labex.io/zh/labs/comptia-search-text-with-grep-in-linux-590841)** - 学习使用 `grep` 搜索 Linux 文件中的文本，包括基本搜索、显示行号、使用 `^` 和 `$` 锚点，以及运用基本和扩展正则表达式进行复杂模式匹配。
2. **[文本处理与正则表达式](https://labex.io/zh/labs/linux-text-processing-and-regular-expressions-18003)** - 学习强大的文本处理工具 grep、sed 和 awk，并使用正则表达式在 Linux 中高效操作文本和匹配模式。
3. **[提取邮件和数字](https://labex.io/zh/labs/linux-extracting-mails-and-numbers-17991)** - 使用 grep 和正则表达式从文件中提取电子邮件地址与数字，练习重要的 Linux 文本处理技能。

## 总结

现在，你可以阅读和构建基础的面向行正则表达式。

1. 区分正则表达式运算符和 shell 路径名通配符。
2. 把匹配锚定在行首或行尾。
3. 使用点号或方括号表达式匹配一个字符。
4. 对集合取反，并使用 locale 相关的字符类。
5. 有意识地选择 BRE 或 ERE 语法。
