---
lesson_id: "paste-command"
course_id: "text-fu"
lang: "zh"
order_index: 7
title: "paste"
description: "学习使用 paste 合并对应行，或用可配置的分隔符把多行串成一行。"
meta_title: "paste - 文本处理"
meta_description: "了解如何使用 Linux paste 命令合并文件行。通过本基本的 Linux 命令教程，探索分隔符并合并文件。"
meta_keywords: "Linux paste 命令，paste 命令教程，合并文件行，Linux 命令，Linux 初学者，Linux 指南"
---

`paste` 命令把多行组合成多列。默认情况下，它从每个输入文件各取一行，用制表符连接，再重复此过程，直到所有输入都到达文件末尾。

## 并排合并文件

创建两个小文件：

```bash
$ printf 'alice\nbob\n' > names.txt
$ printf 'admin\nviewer\n' > roles.txt
```

把两个文件传给 `paste`：

```bash
$ paste names.txt roles.txt
alice	admin
bob	viewer
```

列之间看见的空白是制表符。`cat` 会依次写出每个完整文件，而 `paste` 会组合各输入中的对应行。

:::single-choice{#paste-corresponding-lines}
`first.txt` 依次包含 `A`、`B`，`second.txt` 依次包含 `1`、`2`。`paste first.txt second.txt` 默认会产生什么？

::option[`A`、`B`、`1`、`2` 分别位于连续四行。]{#paste-concatenated-files explanation="这更像依次写出两个文件；`paste` 会组合对应行。"}
::option[`A`、`B`、`1`、`2` 不带分隔符地位于一行。]{#paste-one-line-no-separator explanation="串成一行需要使用 `-s`，而且默认分隔符是制表符，并非无分隔符。"}
::option[`A` 与 `1` 同行，`B` 与 `2` 同行，字段以制表符分隔。]{#paste-parallel-result .correct explanation="默认并行模式为每个输出行从各文件取一行，并用制表符分隔字段。"}
:::

## 选择分隔符

使用 `-d LIST` 替换默认制表符。例如改为冒号：

```bash
$ paste -d ':' names.txt roles.txt
alice:admin
bob:viewer
```

具有 shell 含义的分隔符需要加引号。列表包含多个字符时，`paste` 可以循环使用它们；构建两列时，单个字符最容易理解。

:::single-choice{#paste-colon-delimiter}
哪个命令会用冒号连接 `names.txt` 与 `roles.txt` 中的对应行？

::option[`paste -d ':' names.txt roles.txt`]{#paste-colon-files .correct explanation="`-d` 会把每对字段间的默认制表符替换为指定的冒号。"}
::option[`paste -s ':' names.txt roles.txt`]{#paste-serial-colon-operand explanation="`-s` 选择串行模式，而 `:` 会被视为另一个输入路径，不是分隔符。"}
::option[`paste names.txt ':' roles.txt`]{#paste-colon-file-operand explanation="没有 `-d` 时，每个操作数都会被视为输入文件，这会尝试打开名为 `:` 的文件。"}
:::

## 把一个文件中的多行串成一行

`-s` 会串行处理每个输入文件，把其中各行连接为一个输出行。创建一个每行一个单词的文件：

```bash
$ printf 'The\nquick\nbrown\nfox\n' > words.txt
$ paste -s words.txt
The	quick	brown	fox
```

把 `-s` 与 `-d` 组合，可以选择分隔符：

```bash
$ paste -s -d ' ' words.txt
The quick brown fox
```

在 `-s` 模式下提供多个文件时，每个文件都会成为一个输出行。

:::single-choice{#paste-serialize-with-spaces}
哪个命令会把 `words.txt` 中的所有行连接成一个以空格分隔的输出行？

::option[`paste -d ' ' words.txt`]{#paste-parallel-one-file explanation="在默认并行模式中，单个输入文件仍会让每个输入行对应一个输出行；没有跨文件字段可供分隔。"}
::option[`paste -s words.txt roles.txt`]{#paste-two-serial-files explanation="这会用默认制表符分别串行处理两个文件，产生两个输出行，而非所需的单文件空格分隔结果。"}
::option[`paste -s -d ' ' words.txt`]{#paste-serial-spaces .correct explanation="`-s` 把文件各行串起来，`-d ' '` 在行之间使用空格。"}
:::

## 处理长度不同的输入

并行输入文件行数不同时，`paste` 会继续运行到最长文件结束。较短文件缺失的值会成为空字段：

```bash
$ printf 'A\nB\nC\n' > letters.txt
$ printf '1\n2\n' > numbers.txt
$ paste -d ':' letters.txt numbers.txt
A:1
B:2
C:
```

:::single-choice{#paste-unequal-files}
并行传给 `paste` 的某个文件比其他文件更早结束时，会发生什么？

::option[`paste` 会让该文件贡献空字段，直到最长输入结束。]{#paste-empty-fields .correct explanation="并行模式会持续到所有文件耗尽，较短输入中缺失的行表示为空字段。"}
::option[`paste` 会立即停止并丢弃剩余行。]{#paste-stop-shortest explanation="`paste` 会继续处理最长输入，不会仅因另一个文件结束就丢弃剩余行。"}
::option[`paste` 会从头重复较短的文件。]{#paste-repeat-shorter explanation="该命令不会循环输入记录；已经耗尽的输入会贡献空字段。"}
:::

## 从 stdin 读取一个输入

使用 `-` 作为文件操作数，可以让该位置从 stdin 读取：

```bash
$ printf 'admin\nviewer\n' | paste -d ':' names.txt -
alice:admin
bob:viewer
```

:::single-choice{#paste-stdin-operand}
在 `producer | paste names.txt -` 中，`-` 操作数表示什么？

::option[把合并结果写入 stderr。]{#paste-write-stderr explanation="此处的连字符表示输入来源，并不会重定向输出流。"}
::option[删除两列之间的分隔符。]{#paste-remove-delimiter explanation="分隔符由 `-d` 控制；连字符不会改变分隔符。"}
::option[从 stdin 读取这一输入列。]{#paste-read-stdin .correct explanation="连字符告诉 `paste` 在这个操作数位置使用标准输入。"}
:::

要练习合并面向行的数据，可以尝试这个动手实验：

1. **[简单文本处理](https://labex.io/zh/labs/linux-simple-text-processing-18004)** - 学习使用 `tr`、`col`、`join` 和 `paste` 等命令高效操作和分析文本数据。

## 总结

现在，你可以使用可预测的对齐方式和分隔符组合面向行的输入。

1. 合并多个文件中的对应行。
2. 使用 `-d` 替换默认制表符。
3. 使用 `-s` 把一个文件中的各行串起来。
4. 理解较短输入产生的空字段。
5. 在某个输入来自 stdin 时使用 `-`。
