---
lesson_id: "grep-command"
course_id: "text-fu"
lang: "zh"
order_index: 16
title: "grep"
description: "学习如何使用固定字符串或正则表达式选择行，并解释 grep 的结果。"
meta_title: "grep 命令 - 文本处理利器"
meta_description: "学习如何在 Linux 中使用强大的 grep 命令来搜索文本模式。本指南涵盖基本用法、grep -e 命令、使用 grep -c 进行计数以及其他用于有效文本处理的关键选项。"
meta_keywords: "grep 命令，grep -e 命令，grep -c, grep -f, grep -o, grep -e 示例，linux grep, 文本搜索，模式匹配，文本处理，linux 教程"
---

`grep` 命令会选择与模式匹配的输入行。它可以搜索指定文件或 stdin、输出匹配行的上下文、统计所选行，还能通过退出状态表明是否找到匹配项。

## 匹配文件中的行

先传入模式，再传入一个或多个输入文件：

```bash
$ grep 'fox' sample.txt
```

默认情况下，GNU `grep` 会把模式解释为基本正则表达式，并输出每一条所选行。请为模式加引号，防止空格和 shell 元字符先被 shell 解释。

如果模式应作为固定字符串而不是正则表达式处理，请使用 `-F`：

```bash
$ grep -F 'price: $5.00' products.txt
```

:::single-choice{#grep-fixed-string}
哪个命令会在 `products.txt` 中搜索字面文本 `price: $5.00`，而不把模式字符视为正则表达式语法？

::option[`grep -F 'price: $5.00' products.txt`]{#grep-fixed-price .correct explanation="`-F` 选择固定字符串匹配，单引号则防止 shell 展开美元符号。"}
::option[`grep -E 'price: $5.00' products.txt`]{#grep-extended-price explanation="`-E` 启用扩展正则表达式，其中 `$` 和 `.` 具有特殊含义，不再是字面字符。"}
::option[`grep -v 'price: $5.00' products.txt`]{#grep-invert-price explanation="`-v` 选择不匹配的行，而且默认仍使用正则表达式解释。"}
:::

## 选择模式语法

GNU `grep` 常用的模式有三种：

- 默认：基本正则表达式。
- `-E`：扩展正则表达式，其中 `|`、`+` 和 `?` 等运算符无需反斜杠。
- `-F`：固定字符串，不使用正则表达式运算符。

`^` 和 `$` 等锚点分别匹配行首和行尾。如果要在文本列表中匹配以字面后缀 `.txt` 结尾的文件名：

```bash
$ grep -E '\.txt$' filenames.txt
```

反斜杠使点号按字面含义匹配；在正则表达式中，未转义的 `.` 会匹配任意单个字符。

:::single-choice{#grep-literal-txt-suffix}
哪个扩展正则表达式会匹配以字面后缀 `.txt` 结尾的行？

::option[`'.txt$'`]{#grep-anychar-txt explanation="点号未转义，所以它会匹配 `txt` 前面的任意单个字符，而不一定是字面句点。"}
::option[`'\.txt$'`]{#grep-dot-txt-end .correct explanation="`\.` 匹配字面句点，`$` 把匹配锚定在行尾。"}
::option[`'^.txt'`]{#grep-start-anychar-txt explanation="它锚定在行首，而且仍使用未转义的点号，所表达的是另一种匹配。"}
:::

## 安全提供模式

使用 `-e PATTERN` 可以明确提供模式。当模式以 `-` 开头时，这尤其有用，因为只加引号并不能阻止选项解析：

```bash
$ grep -e '-v' settings.conf
```

可以重复使用 `-e`，选择与任一所给模式匹配的行。使用 `-f patterns.txt` 可从文件中每行读取一个模式。

:::single-choice{#grep-hyphen-pattern}
哪个命令会在 `settings.conf` 中搜索模式 `-v`，而不是把它解释为选项？

::option[`grep '-v' settings.conf`]{#grep-quoted-v explanation="引号会防止 shell 展开字符，但 `grep` 仍可能把得到的 `-v` 参数解释为反向匹配选项。"}
::option[`grep -v settings.conf`]{#grep-invert-settings explanation="这会启用反向匹配，并没有按题目要求同时提供模式和输入文件。"}
::option[`grep -e '-v' settings.conf`]{#grep-explicit-v .correct explanation="`-e` 选项明确声明后一个参数是模式，即使它以连字符开头。"}
:::

## 控制所选输出

- `-i`：忽略大小写差异。
- `-n`：在所选行前加上行号。
- `-v`：选择不匹配的行。
- `-c`：为每个输入文件输出所选行数。
- `-o`：只输出每个非空匹配部分，而不是完整的所选行。

例如，忽略大小写并统计包含 `fox` 的行：

```bash
$ grep -ic 'fox' sample.txt
```

`-c` 统计的是所选行，不是这些行中的匹配总次数。包含 `fox fox` 的一行只会贡献一次计数。如果确实需要使用 GNU `grep` 统计非重叠匹配次数，`grep -o PATTERN | wc -l` 是一种可选管道。

:::single-choice{#grep-count-lines}
`data.txt` 有一行包含 `error error`，另有两行不匹配。`grep -c 'error' data.txt` 会报告什么？

::option[`2`，因为该单词在一行中出现两次。]{#grep-count-occurrences explanation="`-c` 统计所选行，而不是一行内的单独匹配次数。"}
::option[`1`，因为恰好有一行匹配。]{#grep-count-one-line .correct explanation="即使模式在该行中出现两次，这一行也只会被选择一次。"}
::option[`3`，因为文件共有三行。]{#grep-count-total-lines explanation="只有所选行会计入 `grep -c`；不匹配的行会被排除。"}
:::

## 筛选 stdin 和搜索目录

未指定输入文件时，`grep` 会读取 stdin，因此很适合用于管道：

```bash
$ env | grep '^USER='
```

使用 `-r` 可递归搜索目录下可读的文件：

```bash
$ grep -r 'listen_port' config/
```

权限错误等诊断信息会写入 stderr，不属于匹配输入。应缩小搜索路径并了解权限，而不是立即提升访问权限。

:::single-choice{#grep-pipeline-input}
在 `generate-report | grep 'failed'` 中，`grep` 搜索的输入是什么？

::option[当前目录中名为 `generate-report` 的文件。]{#grep-report-file explanation="左侧的名称会作为命令执行，不会作为文件操作数传给 `grep`。"}
::option[`generate-report` 产生的 stdout 流。]{#grep-report-stdout .correct explanation="管道会把生产者的 stdout 连接到 `grep` 的 stdin。"}
::option[`generate-report` 产生的 stderr 流。]{#grep-report-stderr explanation="普通管道传递 stdout；除非明确重定向，否则 stderr 保持独立。"}
:::

## 解释退出状态

对于普通搜索，GNU `grep` 在至少选择一行时返回状态 `0`，没有选择任何行时返回 `1`，发生错误时返回 `2`。因此，脚本可以检测匹配，同时不把“没有匹配”与文件不可读或模式无效混为一谈。

`-q` 等选项会抑制正常输出，并在找到匹配后停止，适合用于条件检查。不要仅根据屏幕上没有内容来推断成功与否：`-q`、重定向、没有匹配和发生错误都可能不产生或只产生很少 stdout，但它们的状态不同。

要练习固定字符串和正则表达式搜索，可以尝试以下动手实验：

1. **[在 Linux 中使用 grep 搜索文本](https://labex.io/zh/labs/comptia-search-text-with-grep-in-linux-590841)** - 练习基本搜索、显示行号、使用锚点，以及运用基本与扩展正则表达式完成复杂的 `grep` 模式匹配。
2. **[Linux grep 命令：模式搜索](https://labex.io/zh/labs/linux-linux-grep-command-pattern-searching-219192)** - 学习使用 `grep` 搜索和匹配文本文件中的模式，并探索如何用正则表达式定义复杂搜索模式。
3. **[大海捞针](https://labex.io/zh/labs/linux-needle-in-the-haystack-388109)** - 学习使用 `grep` 搜索特定模式、统计出现次数、提取唯一值，以及在多个日志文件中组合搜索条件。

## 总结

现在，你可以搜索面向行的文本，并区分匹配结果与错误。

1. 选择基本正则、扩展正则或固定字符串匹配。
2. 为模式加引号，并使用 `-e` 处理开头的连字符。
3. 统计所选行，不要将其与匹配次数混淆。
4. 筛选 stdin，或在明确范围的目录中递归搜索。
5. 解释匹配、无匹配和错误对应的退出状态。
