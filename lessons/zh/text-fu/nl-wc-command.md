---
lesson_id: "nl-wc-command"
course_id: "text-fu"
lang: "zh"
order_index: 15
title: "wc 和 nl"
description: "学习使用 wc 统计行、单词、字节或字符，并使用 nl 为行编号。"
meta_title: "wc 和 nl 命令 - Text-Fu"
meta_description: "在此 Linux 教程中掌握 wc 和 nl 命令。学习如何执行 Linux 单词计数、为文件添加行号以及进行基本的文件分析。一份完美的初学者指南，可提升您的命令行技能。"
meta_keywords: "wc 命令，nl 命令，Linux 单词计数，Linux 文件中计数单词，Linux 行号，nl 命令 Linux, 文件分析，Linux 文本处理，Linux 命令行，Linux 初学者教程"
---

`wc` 命令统计文本流的属性，而 `nl` 会写出输入并生成行号。两者都可以读取文件或 stdin，并把结果发送到 stdout。

## 阅读 wc 的默认输出

不指定计数选项时，`wc` 会输出换行符数、单词数和字节数；如果提供了文件名，后面还会显示文件名：

```bash
$ printf 'red blue\ngreen\n' > colors.txt
$ wc colors.txt
 2  3 15 colors.txt
```

从左到右分别是：

1. `2` 个换行符，以行数显示。
2. `3` 个由空白分隔的单词。
3. 这个 ASCII 示例中有 `15` 个字节。

如果最后一行文本没有结尾换行符，`wc -l` 不会把它计入，因为该选项统计的是换行符，而不是视觉上看到的行。

:::single-choice{#wc-default-columns}
`wc file.txt` 的默认输出中，前三个数字分别表示什么？

::option[依次为行数、单词数和字节数。]{#wc-lines-words-bytes .correct explanation="默认的 `wc` 输出会在文件名前依次报告换行符数、单词数和字节数。"}
::option[依次为字节数、单词数和行数。]{#wc-bytes-words-lines explanation="这些是同样的度量，但顺序错误；行数排在第一列。"}
::option[依次为文件数、字符数和段落数。]{#wc-files-characters-paragraphs explanation="默认列不统计文件或段落，第三个默认度量是字节数。"}
:::

## 请求单项计数

只选择需要的度量：

- `-l`：统计换行符。
- `-w`：统计单词。
- `-c`：统计字节。
- `-m`：根据当前 locale 统计字符。

例如：

```bash
$ wc -w colors.txt
3 colors.txt
```

对于 ASCII 文本，字节数和字符数相等；但对于 UTF-8 等多字节编码，两者可能不同。使用 stdin 而没有文件名操作数时，`wc` 通常不显示文件名标签：

```bash
$ printf 'one two\n' | wc -w
2
```

:::single-choice{#wc-word-count-only}
哪个命令只报告 `essay.txt` 的单词数？

::option[`wc -l essay.txt`]{#wc-lines-essay explanation="`-l` 报告换行符数，而不是单词数。"}
::option[`wc -w essay.txt`]{#wc-words-essay .correct explanation="`-w` 选项选择单词计数这一度量。"}
::option[`wc -c essay.txt`]{#wc-bytes-essay explanation="`-c` 报告字节数，而不是由空白分隔的单词数。"}
:::

:::single-choice{#wc-characters-not-bytes}
哪个选项会让 `wc` 根据当前 locale 统计字符而不是字节？

::option[`-m`]{#wc-character-option .correct explanation="`-m` 报告字符数；对于多字节文本，它可能与字节数不同。"}
::option[`-c`]{#wc-byte-option explanation="`-c` 报告字节数。在 UTF-8 等编码中，一个字符可能占用多个字节。"}
::option[`-w`]{#wc-word-option explanation="`-w` 统计单词，而不是字符或字节。"}
:::

指定多个文件时，`wc` 会为每个文件输出一项结果，并增加一行 `total`。GNU `wc -L` 报告输入行的最大显示宽度。

## 使用 nl 为非空行编号

默认情况下，`nl` 会为输入逻辑正文中的非空行编号。假设 `notes.txt` 的第二行为空：

```text
alpha

beta
```

空行会保留，但不会获得编号：

```bash
$ nl notes.txt
	 1	alpha

	 2	beta
```

`nl` 会写出带编号的结果；它不会修改 `notes.txt`。

:::single-choice{#nl-default-blank-lines}
默认情况下，`nl notes.txt` 如何处理正文中的空行？

::option[从输出中完全省略每个空行。]{#nl-omit-blank explanation="空行会保留在输出中，但默认不分配编号。"}
::option[保留空行，但不为其编号。]{#nl-preserve-unnumbered .correct explanation="默认正文样式为非空行编号，并让空行不带编号地通过。"}
::option[按照与非空行相同的序列为其编号。]{#nl-number-blank-default explanation="为每一正文行编号需要使用 `-ba` 等不同样式。"}
:::

## 为每一行编号

使用 `-ba` 可选择正文编号样式 `a`，为所有行编号：

```bash
$ nl -ba notes.txt
	 1	alpha
	 2
	 3	beta
```

其他选项可以控制格式。例如，`-w 3` 设置编号字段宽度，`-s ': '` 更改编号后的分隔符。

:::single-choice{#nl-number-all-lines}
哪个命令会为 `notes.txt` 中的每一正文行编号，包括空行？

::option[`nl -w 3 notes.txt`]{#nl-width-three explanation="这会更改编号字段宽度，但仍保留默认的非空行编号规则。"}
::option[`nl -ba notes.txt`]{#nl-body-all .correct explanation="`-b` 选择正文样式，样式 `a` 会为所有正文行编号。"}
::option[`wc -l notes.txt`]{#wc-lines-notes explanation="这会输出换行符计数，不会重现文件并添加行号。"}
:::

要练习文本计数和行编号，可以尝试以下动手实验：

1. **[Linux wc 命令：文本计数](https://labex.io/zh/labs/linux-linux-wc-command-text-counting-219200)** - 练习使用 `wc` 统计文本文件中的单词、行和字符。
2. **[Linux nl 命令：行编号](https://labex.io/zh/labs/linux-linux-nl-command-line-numbering-210988)** - 学习使用 `nl` 为文本文件中的行编号。
3. **[单词计数和排序](https://labex.io/zh/labs/linux-word-count-and-sorting-388125)** - 运用 `wc` 统计行、单词和字符，并把它与排序结合起来完成实用的文本分析任务。

## 总结

现在，你可以在不编辑源文件的情况下度量文本流并添加可见行号。

1. 理解 `wc` 默认输出中的行、单词和字节列。
2. 使用 `-l`、`-w`、`-c` 或 `-m` 选择单项计数。
3. 区分字节数和字符数。
4. 使用 `nl` 的默认行为为非空行编号。
5. 使用 `nl -ba` 同时为空行编号。
