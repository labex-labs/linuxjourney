---
lesson_id: "cut-command"
course_id: "text-fu"
lang: "zh"
order_index: 6
title: "剪切"
description: "学习使用 cut 从每行中选择字符位置或带分隔符的字段。"
meta_title: "cut 命令 - 文本处理工具"
meta_description: "学习如何使用 Linux `cut` 命令从文件中提取特定文本部分。本指南涵盖按字符和字段（`cut f`）进行剪切，包括如何使用自定义分隔符进行字段剪切。是掌握 Linux 文本处理的理想选择。"
meta_keywords: "cut 命令，Linux 文本处理，提取文本，cut f, 如何使用 cut f, Linux 教程，cut 示例，Linux 指南，字段剪切"
---

`cut` 命令从每个输入行中选择指定的字符位置或字段。它最适合处理分隔符和字段位置已知且结构一致的文本。

为示例创建一个以制表符分隔的小文件。`printf` 会把 `\t` 解释为字面制表符，把 `\n` 解释为换行符：

```bash
$ printf 'name\trole\nalice\tadmin\nbob\tviewer\n' > team.tsv
```

## 选择字符位置

使用 `-c LIST` 从每行选择位置。位置从 1 开始：

```bash
$ cut -c 1 team.tsv
n
a
b
```

列表可以包含单个位置和范围：

```bash
$ cut -c 1-4 team.tsv
name
alic
bob
$ cut -c 1,3 team.tsv
nm
ai
bb
```

空格、制表符和标点符号同样会占用位置。`cut` 会独立处理每一行。

:::single-choice{#cut-first-character} 哪个命令会打印 `names.txt` 每一行的第一个字符？

::option[`cut -c 1 names.txt`]{#cut-character-one .correct explanation="`-c` 选择字符位置，而位置 1 就是每行的第一个字符。"}
::option[`cut -f 1 names.txt`]{#cut-field-one explanation="`-f` 选择第一个制表符分隔字段，其中可能包含多个字符。"}
::option[`cut -d 1 names.txt`]{#cut-delimiter-one explanation="`-d` 用于指定字段分隔符，必须与字段选择配合使用，并不选择字符位置。"}
:::

## 选择制表符分隔的字段

使用 `-f LIST` 选择字段。默认分隔符是制表符：

```bash
$ cut -f 2 team.tsv
role
admin
viewer
```

与字符选择一样，列表可以使用 `1`、`1,3`、`2-4`、`-3` 或 `2-` 等值。

:::single-choice{#cut-second-tab-field} 哪个命令会打印 `team.tsv` 每一行中以制表符分隔的第二个字段？

::option[`cut -c 2 team.tsv`]{#cut-second-character explanation="这会选择每行的第二个字符位置，而不是第二个制表符分隔字段。"}
::option[`cut -f 2 team.tsv`]{#cut-second-field .correct explanation="没有 `-d` 时，字段模式使用制表符作为分隔符，`-f 2` 选择第二个字段。"}
::option[`cut -d 2 team.tsv`]{#cut-delimiter-two explanation="这会尝试把 `2` 设为分隔符，却没有提供字段列表，并不会选择字段 2。"}
:::

## 选择自定义分隔符

字段使用制表符之外的分隔符时，请把 `-d CHARACTER` 与 `-f` 结合使用。下面创建以分号分隔的数据：

```bash
$ printf 'alice;admin\nbob;viewer\n' > team.txt
$ cut -d ';' -f 1 team.txt
alice
bob
```

这种形式的分隔符是一个字符。需要给 `;` 加引号，因为未加引号的分号在 shell 中具有控制含义。

:::single-choice{#cut-semicolon-role-field} 哪个命令会打印 `team.txt` 中以分号分隔的第二个字段？

::option[`cut -d ':' -f 2 team.txt`]{#cut-colon-second explanation="这会选择以冒号分隔的字段，但该文件使用分号。"}
::option[`cut -d ';' -f 2 team.txt`]{#cut-semicolon-second .correct explanation="加引号的分号设置分隔符，`-f 2` 选择每行的第二个字段。"}
::option[`cut -c 2 -f ';' team.txt`]{#cut-mixed-options explanation="这混用了字符选择和无效字段参数；分隔符应跟在 `-d` 后，字段编号应跟在 `-f` 后。"}
:::

## 处理不含分隔符的行

在字段模式下，如果某行不含分隔符，`cut` 通常会原样打印该行。添加 `-s` 可以抑制这些行：

```bash
$ printf 'alice;admin\nheader\nbob;viewer\n' | cut -s -d ';' -f 2
admin
viewer
```

这并不能验证通用 CSV 文件。CSV 可能包含加引号的分隔符、嵌入换行符和转义规则，单字符切分无法理解这些结构；此类数据应使用支持 CSV 的工具。

:::single-choice{#cut-suppress-undelimited} 在 `cut -d ':' -f 1` 中，`-s` 有什么作用？

::option[打印前对选中的字段排序。]{#cut-s-sort explanation="`cut` 不会对输入排序，`-s` 也与顺序无关。"}
::option[把连续分隔符视为一个分隔符。]{#cut-s-squeeze explanation="`cut` 不会用 `-s` 合并分隔符；空字段仍是有意义的位置。"}
::option[抑制不含所选分隔符的行。]{#cut-s-suppress .correct explanation="在字段模式下，`-s` 会防止不含分隔符的行被原样传出。"}
:::

## 从 stdin 读取

未指定文件或使用 `-` 作为输入操作数时，`cut` 会读取 stdin，因此很适合作为管道的一环：

```bash
$ printf 'red:1\nblue:2\n' | cut -d ':' -f 1
red
blue
```

:::single-choice{#cut-pipeline-input} 在 `generate-data | cut -d ':' -f 1` 中，`cut` 从哪里读取输入？

::option[通过管道读取 `generate-data` 的 stdout。]{#cut-pipe-stdin .correct explanation="管道把生产者的 stdout 连接到 `cut` 的 stdin，而且没有指定其他输入文件。"}
::option[从字面名称为 `generate-data` 的文件读取。]{#cut-pipe-file explanation="`generate-data` 会作为管道左侧命令执行，并不会作为文件名传给 `cut`。"}
::option[从 `cut` 的标准错误流读取。]{#cut-pipe-stderr explanation="普通管道把前一条命令的 stdout 送入标准输入，而不是从 `cut` 的 stderr 读取。"}
:::

要练习位置和字段选择，可以尝试以下动手实验：

1. **[Linux cut 命令：文本切割](https://labex.io/zh/labs/linux-linux-cut-command-text-cutting-219187)** - 直接练习使用 `cut` 从文本文件中提取指定列或字段。
2. **[序列控制和管道](https://labex.io/zh/labs/linux-sequence-control-and-pipeline-17994)** - 学习控制命令执行序列、使用管道，并结合 `cut`、`grep`、`wc`、`sort` 和 `uniq` 等文本工具。

## 总结

现在，你可以使用 `cut` 从面向行的文本中选择可预测的位置。

1. 选择单个字符位置或范围。
2. 使用 `-f` 提取制表符分隔字段。
3. 使用 `-d` 提供单字符分隔符。
4. 在适当时抑制不含分隔符的行。
5. 从文件或 stdin 读取结构化文本。
