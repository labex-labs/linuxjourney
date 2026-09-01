---
lesson_id: "expand-unexpand-command"
course_id: "text-fu"
lang: "zh"
order_index: 10
title: "expand 和 unexpand"
description: "学习制表位如何控制 expand 和 unexpand 在制表符与空格之间进行转换。"
meta_title: "expand 和 unexpand - Text-Fu"
meta_description: "使用我们的 expand 和 unexpand 命令指南，掌握 Linux 中的文本格式设置。了解如何将制表符转换为空格，以及将空格转换回制表符，以实现一致的文件布局。"
meta_keywords: "expand 命令，unexpand 命令，Linux 制表符，Linux 空格，文本格式化，Linux 教程，Linux 入门，Linux 指南"
---

制表符记录的是移动到制表位的操作，而不是固定数量的可见空格。它显示出的宽度取决于当前列和制表位设置。`expand` 和 `unexpand` 命令会根据这些位置，在制表符和空格之间进行转换。

## 将制表符转换为空格

`expand` 读取输入，把制表符替换为到达相应制表位所需的空格，然后将结果写入 stdout：

```bash
$ expand sample.txt
```

默认情况下，制表位每隔 8 列出现一次。因此，位于第 1 列的制表符与位于第 6 列的制表符会展开成不同数量的空格；它并非总是替换为八个空格。

:::single-choice{#expand-default-tab-stops} 使用默认设置时，`expand` 如何替换一个制表符？

::option[插入足够的空格，使位置到达下一个默认制表位。]{#expand-next-stop .correct explanation="`expand` 会根据当前列计算所需的空格数，从而保持制表位对齐。"}
::option[始终插入恰好八个空格。]{#expand-eight-spaces explanation="默认制表位相隔八列，但所需空格数取决于当前列。"}
::option[删除制表符而不添加任何字符。]{#expand-remove-tab explanation="该命令会用空格替换制表符，使后面的文本仍与所选制表位对齐。"}
:::

## 选择制表位

使用 `-t NUMBER` 可按指定的列间隔设置制表位。若要每四列设置一个制表位：

```bash
$ expand -t 4 sample.txt
```

GNU `expand` 也接受以逗号分隔的明确制表位列表。如果只想转换每行第一个非空白字符之前的制表符，请使用 `-i`。

:::single-choice{#expand-four-column-stops} 哪个命令会使用每四列一个的制表位来转换制表符？

::option[`expand -i 4 sample.txt`]{#expand-initial-four explanation="`-i` 选项把转换限制在行首制表符，而且不把 `4` 作为制表位间隔。"}
::option[`unexpand -t 4 sample.txt`]{#unexpand-tabs-four explanation="`unexpand` 把适合的空格转换为制表符，方向与题目要求相反。"}
::option[`expand -t 4 sample.txt`]{#expand-tabs-four .correct explanation="`-t` 选项设置制表位间隔，`4` 表示每四列一个制表位。"}
:::

## 安全保存转换结果

`expand` 不会编辑输入文件。需要保存转换后的文本时，请将 stdout 重定向到另一个路径：

```bash
$ expand sample.txt > result.txt
```

不要使用 `expand sample.txt > sample.txt`。shell 会在 `expand` 读取文件之前截断目标文件，因而可能丢失源数据。确认另行写出的结果正确后，再通过适当的文件管理操作有意替换原文件。

:::single-choice{#expand-safe-output-file} 哪个命令能保存展开后的文本，又不会在读取 `sample.txt` 之前将其截断？

::option[`expand sample.txt > sample.txt`]{#expand-same-file explanation="shell 会在启动 `expand` 前打开并截断 `sample.txt` 作为输出，这可能清空输入。"}
::option[`expand sample.txt > result.txt`]{#expand-separate-result .correct explanation="输入和输出路径不同，shell 可以创建 `result.txt` 而不破坏源文件。"}
::option[`> sample.txt expand result.txt`]{#expand-leading-redirection explanation="这仍会截断 `sample.txt`，也没有表达从原文件进行安全转换的操作。"}
:::

## 将空格转换为制表符

`unexpand` 会把符合条件的空格替换为制表符，同时保持它们在所选制表位上的对齐。默认情况下，GNU `unexpand` 只转换每行第一个非空白字符之前的行首空白：

```bash
$ unexpand result.txt
```

使用 `-a` 可让命令检查每行各处符合条件的空白：

```bash
$ unexpand -a result.txt
```

这并不是简单地把每一串八个空格都替换掉。和 `expand` 一样，转换取决于列位置和制表位。如果文件采用其他约定，请使用 `-t 4` 或其他制表位设置。

:::single-choice{#unexpand-default-scope} 不使用 `-a` 时，GNU `unexpand` 通常会考虑转换哪些空格？

::option[文件中任何位置的每一组空格。]{#unexpand-every-group explanation="要检查整行中的空白，需要使用 `-a`，而且转换仍取决于制表位位置。"}
::option[只转换最后一个单词之后的空格。]{#unexpand-trailing-blanks explanation="默认范围是行首空白，并非特指行尾空白。"}
::option[只转换第一个非空白字符之前的行首空白。]{#unexpand-initial-blanks .correct explanation="GNU `unexpand` 的默认行为仅处理每行开头的空白。"}
:::

:::single-choice{#unexpand-all-blanks} 哪个选项会让 GNU `unexpand` 也考虑第一个非空白字符之后的空白？

::option[`-i`]{#unexpand-initial-option explanation="对于 `expand`，`-i` 会把处理范围限制为行首制表符；它不是 `unexpand` 的全空白选项。"}
::option[`-a`]{#unexpand-all-option .correct explanation="`-a` 选项允许转换每一输入行中所有符合条件的空白。"}
::option[`-t`]{#unexpand-tab-list-option explanation="`-t` 用于设置制表位。尽管 GNU 的相关行为可能隐含更广的转换范围，明确请求所有空白应使用 `-a`。"}
:::

未指定文件时，这两个命令都会读取 stdin，因此可以在管道中使用。请记住，即使显示出的对齐方式没有变化，先转换为空格再转回制表符，也不一定能还原原本对制表符和空格的选择。

## 总结

现在，你可以在保持制表位对齐的同时转换制表符和空格。

1. 将制表符展开到下一个配置好的制表位。
2. 使用 `-t` 设置自定义制表位。
3. 先把输出保存到另一个文件，再替换输入文件。
4. 默认使用 `unexpand` 转换行首空白。
5. 需要考虑每行各处的空白时使用 `-a`。
