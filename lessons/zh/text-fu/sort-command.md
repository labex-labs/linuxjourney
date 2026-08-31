---
lesson_id: "sort-command"
course_id: "text-fu"
lang: "zh"
order_index: 12
title: "sort"
description: "学习如何使用 sort 按词法、数值或所选字段值排列文本行。"
meta_title: "sort - 文本高手"
meta_description: "学习如何使用 Linux sort 命令对文本文件进行排序。探索反向和数值排序等选项。提高你的 Linux 命令行技能！"
meta_keywords: "Linux sort 命令，sort -r, sort -n, Linux 教程，命令行，Linux 初学者，sort 指南"
---

`sort` 命令读取完整的行，根据所选比较规则排列它们，并将结果写入 stdout。除非明确选择输出操作，否则它不会更改输入文件。

## 对完整行排序

假设 `animals.txt` 包含：

```text
dog
cow
cat
elephant
bird
```

按升序排列这些行：

```bash
$ sort animals.txt
bird
cat
cow
dog
elephant
```

文本顺序遵循当前 locale，这会影响大小写、重音字符和标点符号。如果脚本需要可复现的按字节排序，请使用 `LC_ALL=C` 等一致的 locale：

```bash
$ LC_ALL=C sort animals.txt
```

:::single-choice{#sort-lines-ascending}
不使用键或数值选项时，`sort animals.txt` 会做什么？

::option[根据当前 locale 排列完整的输入行。]{#sort-locale-lines .correct explanation="默认情况下，`sort` 使用当前 locale 的排序规则比较完整的行。"}
::option[排列每行内部的单词，但保持各行顺序不变。]{#sort-words-within-lines explanation="`sort` 把每一行视为一条记录，不会重新排列单行内部的单词。"}
::option[自动就地重写 `animals.txt`。]{#sort-auto-rewrite explanation="默认情况下，排序结果写入 stdout，输入文件保持不变。"}
:::

## 反转结果

添加 `-r` 可反转比较结果：

```bash
$ sort -r animals.txt
elephant
dog
cow
cat
bird
```

:::single-choice{#sort-reverse-order}
哪个命令会按反向顺序排列 `animals.txt`？

::option[`sort -n animals.txt`]{#sort-numeric-animals explanation="`-n` 请求数值比较，并不表示反向顺序。"}
::option[`sort -u animals.txt`]{#sort-unique-animals explanation="`-u` 会抑制重复键，并不反转输出。"}
::option[`sort -r animals.txt`]{#sort-reverse-animals .correct explanation="`-r` 选项会反转其他比较规则选出的顺序。"}
:::

## 比较数字

词法顺序比较字符，所以 `10` 通常会排在 `2` 前面。普通数值比较应使用 `-n`：

```bash
$ printf '10\n2\n30\n' | sort -n
2
10
30
```

需要时可以组合选项。`sort -nr scores.txt` 会按数值比较，并把较大的值放在前面。

:::single-choice{#sort-numbers-descending}
哪个命令会把 `scores.txt` 中的数值行按从大到小排列？

::option[`sort -n scores.txt`]{#sort-numeric-ascending explanation="它选择数值比较，但默认方向会把较小的值放在前面。"}
::option[`sort -nr scores.txt`]{#sort-numeric-reverse .correct explanation="`-n` 选择数值比较，`-r` 将其反转，从而得到数值降序。"}
::option[`sort -r scores.txt`]{#sort-lexical-reverse explanation="这会反转文本排序，却没有请求数值比较，因此 `10` 和 `2` 等值的顺序可能不符合预期。"}
:::

## 按字段排序

使用 `-k START[,END]` 选择键。默认情况下，字段由连续的空白分隔。对于以冒号分隔的记录，请使用 `-t ':'`：

```bash
$ printf 'alice:30\nbob:8\ncarol:20\n' | sort -t ':' -k 2,2n
bob:8
carol:20
alice:30
```

这里，`-t ':'` 选择分隔符，`-k 2,2` 把键限制在字段 2，附加的 `n` 则对该键进行数值比较。如果没有末尾的 `,2`，从字段 2 开始的键通常会一直延续到行尾。

:::single-choice{#sort-second-colon-field}
哪个命令会只按 `users.txt` 中以冒号分隔的第二个字段进行数值排序？

::option[`sort -n -k 1,1 users.txt`]{#sort-first-blank-field explanation="这使用默认的空白分隔字段，并选择字段 1，而不是以冒号分隔的第二字段。"}
::option[`cut -d ':' -f 2 users.txt`]{#cut-second-user-field explanation="`cut` 会提取字段 2，但不会按该键对原始记录排序。"}
::option[`sort -t ':' -k 2,2n users.txt`]{#sort-colon-field-two .correct explanation="冒号确定字段边界，`2,2` 把键限制为字段 2，`n` 对该键进行数值比较。"}
:::

## 删除重复项并保存输出

使用 `-u` 可为每个相等的比较键输出一行：

```bash
$ sort -u names.txt
```

它会根据所选比较规则同时排序和删除重复项。如果只想从已经排序的数据中删除相邻重复行，可以使用后续课程介绍的 `uniq` 命令。

如果目标路径与输入不同，可以使用普通重定向把结果写入文件：

```bash
$ sort names.txt > names-sorted.txt
```

不要运行 `sort names.txt > names.txt`；shell 会在 `sort` 读取输入前将其截断。在有意使用同一路径时，GNU `sort -o names.txt names.txt` 可以安全安排自己的输出：

```bash
$ sort -o names.txt names.txt
```

如果原始数据很重要，请保留备份，或先写入另一个文件并验证结果。

:::single-choice{#sort-safe-same-file}
在 GNU/Linux 上，哪个命令会让 `sort` 把排序结果安全地写回 `names.txt`，而不会先被 shell 重定向截断？

::option[`sort -o names.txt names.txt`]{#sort-output-same-file .correct explanation="GNU `sort` 会在按需读取后管理 `-o` 输出，因此 shell 不会通过 `>` 预先截断输入。"}
::option[`sort names.txt > names.txt`]{#sort-redirection-same-file explanation="shell 会在启动 `sort` 前截断 `names.txt`，所以该命令可能丢失输入。"}
::option[`sort -u names.txt`]{#sort-unique-stdout explanation="这会把去重后的排序行写入 stdout，并让输入文件保持不变。"}
:::

要练习排列和分析面向行的数据，可以尝试以下动手实验：

1. **[Linux sort 命令：文本排序](https://labex.io/zh/labs/linux-linux-sort-command-text-sorting-219196)** - 这个实验直接介绍 `sort` 命令，让你练习以包括升序和降序在内的多种方式排列文本文件中的行。
2. **[单词计数和排序](https://labex.io/zh/labs/linux-word-count-and-sorting-388125)** - 在这个挑战中，你会把排序知识与单词计数结合起来分析文本数据，找出常见模式并高效排列数据。

## 总结

现在，你可以为排序后的文本选择比较规则和输出目标。

1. 需要可复现结果时，在明确的 locale 下对完整行排序。
2. 使用 `-r` 反转结果。
3. 使用 `-n` 比较数值。
4. 使用 `-t` 和 `-k` 选择有边界的字段键。
5. 删除重复项或保存输出，同时避免截断输入。
