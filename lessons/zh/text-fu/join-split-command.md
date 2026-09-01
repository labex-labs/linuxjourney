---
lesson_id: "join-split-command"
course_id: "text-fu"
lang: "zh"
order_index: 11
title: "join 和 split"
description: "学习如何按键连接两个已排序的文本文件，以及如何把一个文件拆分成命名片段。"
meta_title: "join 和 split - Text-Fu"
meta_description: "掌握如何使用 Linux 的 join 和 split 命令。学习如何根据共同的字段高效地连接文件，以及将大文件分割成更小的部分。本指南涵盖了用于连接名为 cat、dog、cow 的文件以及其他实用示例的命令。"
meta_keywords: "linux 连接文件，用于连接文件的命令是什么，linux join 命令，linux split 命令，文件操作，命令行，文本处理"
---

`join` 和 `split` 命令解决的是不同的文件处理问题。`join` 合并两个已排序文本输入中的相关记录，而 `split` 把一个输入划分成一系列较小的文件。

## 按第一字段连接两个文件

默认情况下，`join` 会比较恰好两个输入文件中以空白分隔的第一个字段。假设有以下两个已经排序的文件。

`people.txt`：

```text
1 John
2 Jane
3 Mary
```

`surnames.txt`：

```text
1 Doe
2 Doe
3 Sue
```

连接键字段相等的记录：

```bash
$ join people.txt surnames.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

输出先包含一次共享键，然后依次是第一个和第二个文件中的其余字段。`join` 一次处理两个文件；它不接受三个普通文件操作数来执行三路关系连接。

:::single-choice{#join-default-key} 不指定字段选项时，`join first.txt second.txt` 会合并哪些记录？

::option[以空白分隔的第一个字段相等的行。]{#join-first-fields .correct explanation="`join` 默认比较两个已排序输入的第 1 个字段。"}
::option[物理行号相同的行。]{#join-line-numbers explanation="匹配依据是键字段的值，而不只是记录所在的位置。"}
::option[第一个文件的每一行与第二个文件的每一行。]{#join-all-pairs explanation="`join` 输出键匹配的记录，而不是所有行组成的不受限制的笛卡尔积。"}
:::

## 对连接键排序

每个输入都必须按照各自的连接字段排序，并使用兼容的比较规则。对于默认的第 1 字段，可使用 `sort -k 1,1` 准备副本：

```bash
$ LC_ALL=C sort -k 1,1 people-raw.txt > people.txt
$ LC_ALL=C sort -k 1,1 surnames-raw.txt > surnames.txt
$ LC_ALL=C join people.txt surnames.txt
```

排序和连接使用同一 locale，可以让排序规则保持一致。不要把排序结果重定向回原输入路径，因为 shell 会先截断该文件。

:::single-choice{#join-sort-requirement} 为了可靠匹配，`join` 通常要求进行什么准备？

::option[两个文件必须包含完全相同数量的物理行。]{#join-equal-line-count explanation="输入长度可以不同。连接输出取决于键是否匹配，而不是行数是否相等。"}
::option[两个文件的文件名必须在字母排序中彼此相邻。]{#join-filename-order explanation="需要排序的是内容中的键；两个文件名在词法上的关系无关紧要。"}
::option[两个文件都必须按各自的连接字段使用兼容的顺序排序。]{#join-sorted-keys .correct explanation="`join` 会沿着有序键向前处理，因此每个输入的顺序都必须与其比较规则一致。"}
:::

## 选择不同的连接字段

使用 `-1 FIELD` 指定第一个文件的键，使用 `-2 FIELD` 指定第二个文件的键。假设第一个输入包含：

```text
John 1
Jane 2
Mary 3
```

第二个输入包含：

```text
1 Doe
2 Doe
3 Sue
```

先按字段 2 对第一个文件排序，按字段 1 对第二个文件排序，然后运行：

```bash
$ join -1 2 -2 1 people.txt surnames.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

如果字段由 `:` 之类的单个非空白字符分隔，请使用 `-t CHARACTER`。`-a 1` 或 `-a 2` 等选项可以包含某个输入中未配对的行；默认输出只包含匹配的键。

:::single-choice{#join-different-fields} 哪些选项会把第一个文件的字段 2 与第二个文件的字段 1 连接起来？

::option[`-1 1 -2 2`]{#join-fields-reversed explanation="这会选择第一个输入的字段 1 和第二个输入的字段 2，与题目要求相反。"}
::option[`-1 2 -2 1`]{#join-fields-two-one .correct explanation="`-1 2` 选择文件一的字段 2，`-2 1` 选择文件二的字段 1。"}
::option[`-f 2 -d 1`]{#join-cut-style-options explanation="这些更像其他文本工具的字段和分隔符选项，并不是 `join` 的字段选择器。"}
:::

## 按行数拆分

`split` 会把一个输入中连续的片段写入不同的输出文件。它不是按键执行的 `join` 操作的逆过程。

```bash
$ split large.txt
```

GNU 的默认行为是每个输出文件最多写入 1000 行，并使用前缀 `x`，生成 `xaa`、`xab` 和 `xac` 等名称。

使用 `-l NUMBER` 选择行数，并添加最后一个操作数来选择输出前缀：

```bash
$ split -l 500 large.txt part-
```

这会生成 `part-aa`、`part-ab` 等文件，每个片段最多包含 500 行。

:::single-choice{#split-lines-with-prefix} 哪个命令会把 `large.txt` 拆成最多 500 行一份、名称以 `part-` 为前缀的片段？

::option[`split -b 500 large.txt part-`]{#split-five-hundred-bytes explanation="`-b` 选择的是字节；对于普通文本，这些片段会远小于 500 行。"}
::option[`split -l 500 large.txt part-`]{#split-five-hundred-lines .correct explanation="`-l 500` 设置最大行数，最后一个操作数提供输出文件名前缀。"}
::option[`join -l 500 large.txt part-`]{#join-split-lines explanation="`join` 合并两个文件中带键的记录，不会把一个输入拆成多个片段。"}
:::

## 按大小拆分

使用 `-b SIZE` 可按字节大小划分输入。在这里，GNU 的 `K`、`M` 和 `G` 等后缀表示 1024 的幂：

```bash
$ split -b 10M archive.bin chunk-
```

这会请求大小为 10 MiB 的片段，最后一片可能更小。`split` 不会创建归档清单或重组元数据；需要重建时，请保留后缀顺序，并按顺序拼接各片段。

:::single-choice{#split-ten-mebibytes} 哪个命令会把 `archive.bin` 拆成 10 MiB 一份、使用 `chunk-` 前缀的片段？

::option[`split -l 10M archive.bin chunk-`]{#split-lines-ten-m explanation="`-l` 选项需要行数，不能用字节大小后缀来指定二进制片段。"}
::option[`join -b 10M archive.bin chunk-`]{#join-bytes explanation="`join` 不会拆分二进制输入，也不支持这种片段大小操作。"}
::option[`split -b 10M archive.bin chunk-`]{#split-ten-mib .correct explanation="`-b` 选择片段大小，`10M` 表示 10×1024×1024 字节，`chunk-` 是输出前缀。"}
:::

要练习按键连接和结构化数据处理，可以尝试以下动手实验：

1. **[Linux join 命令：文件连接](https://labex.io/zh/labs/linux-linux-join-command-file-joining-219193)** - 这个实验直接介绍 `join` 命令，让你练习根据共同字段合并两个已排序文本文件中的行，正如本课所讲。
2. **[处理员工数据](https://labex.io/zh/labs/linux-processing-employees-data-388132)** - 运用 `join` 以及 `awk` 等其他强大的 Linux 命令行工具，组合并处理来自多个来源的数据，模拟真实的数据分析场景。

## 总结

现在，你可以合并已排序的记录，也可以把一个输入拆分成有序片段。

1. 按相等的键字段连接恰好两个文件。
2. 按连接键以一致方式排序两个输入。
3. 使用 `-1` 和 `-2` 选择非默认键字段。
4. 使用 `-l` 按行数拆分。
5. 使用 `-b` 和清晰的前缀按字节大小拆分。
