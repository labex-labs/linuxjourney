---
lesson_id: "uniq-unique-command"
course_id: "text-fu"
lang: "zh"
order_index: 14
title: "uniq（去重）"
description: "学习如何使用 uniq 折叠、计数或筛选相邻的相同行组。"
meta_title: "uniq（唯一） - Text-Fu"
meta_description: "探索 Linux 中的 uniq 命令，用于筛选和删除文本中相邻的重复行。学习使用 -c、-u、-d 等选项，并将 uniq 与 sort 结合进行强大的文本处理。"
meta_keywords: "uniq 命令，Linux uniq, uniq linux, 删除重复项，sort uniq, 文本处理，数据清理，Linux 教程"
---

`uniq` 命令会把每一输入行与前一行比较。它可以折叠、计数或选择相邻的相同行组，但不会在整个文件中查找彼此分隔的重复项。

## 折叠相邻重复行

假设 `reading.txt` 包含已经分组的值：

```plaintext
book
book
paper
paper
article
article
magazine
```

不带筛选选项运行 `uniq`，会从每个相邻组中输出一行作为代表：

```bash
$ uniq reading.txt
book
paper
article
magazine
```

结果写入 stdout，因此输入文件保持不变。

:::single-choice{#uniq-collapse-adjacent} 默认情况下，`uniq reading.txt` 会做什么？

::option[对整个文件排序，然后删除所有重复值。]{#uniq-auto-sort explanation="`uniq` 保持输入顺序且不会排序；彼此分隔的相同值仍属于不同的组。"}
::option[从每一组相邻相同行中输出一行。]{#uniq-one-per-group .correct explanation="默认情况下，`uniq` 会把连续的相同行折叠为一行输出。"}
::option[直接从 `reading.txt` 中删除重复行。]{#uniq-edit-file explanation="该命令默认把筛选后的文本写入 stdout，不会编辑输入文件。"}
:::

## 对相邻组计数

使用 `-c` 可在每个输出组前加上该组连续输入行的数量：

```bash
$ uniq -c reading.txt
      2 book
      2 paper
      2 article
      1 magazine
```

这些数字是连续组的长度；只有先让所有相同行相邻，它们才是全局总数。

:::single-choice{#uniq-count-groups} `uniq -c` 输出的计数表示什么？

::option[每一输入行中的字符数。]{#uniq-character-count explanation="`uniq -c` 并不统计字符；字符数和字节数等总计由 `wc` 等工具处理。"}
::option[每组连续相同行的数量。]{#uniq-consecutive-count .correct explanation="`-c` 会在每个折叠后的相邻组前加上该组包含的行数。"}
::option[文件中任何位置的匹配行总数。]{#uniq-global-count explanation="彼此分隔的相同行会形成不同的组，除非先对数据排序或以其他方式分组。"}
:::

## 选择唯一组或重复组

使用 `-u` 只输出恰好包含一行的组：

```bash
$ uniq -u reading.txt
magazine
```

使用 `-d` 从每个包含多于一行的相邻组中输出一行作为代表：

```bash
$ uniq -d reading.txt
book
paper
article
```

GNU `uniq -D` 会输出重复组中的每一行，而小写的 `-d` 只输出每个重复组的值一次。

:::single-choice{#uniq-only-singletons} 哪个命令只输出恰好出现一次的相邻组？

::option[`uniq -c reading.txt`]{#uniq-count-reading explanation="这会输出包括重复组和单行组在内的每个组，并附加计数。"}
::option[`uniq -d reading.txt`]{#uniq-duplicate-reading explanation="小写 `-d` 会为每个重复组输出一行，选择范围正好相反。"}
::option[`uniq -u reading.txt`]{#uniq-single-reading .correct explanation="`-u` 选项选择相邻连续长度恰好为一的组。"}
:::

:::single-choice{#uniq-one-per-duplicate-group} 哪个命令会为每个出现多于一次的相邻组输出一行？

::option[`uniq -d reading.txt`]{#uniq-duplicate-groups .correct explanation="`-d` 选项选择相邻重复组，并从每组输出一行作为代表。"}
::option[`uniq -D reading.txt`]{#uniq-all-duplicate-lines explanation="GNU 的大写 `-D` 会输出重复组中的所有行，而不只是一个代表。"}
::option[`uniq -u reading.txt`]{#uniq-unique-groups explanation="`-u` 选择的是单行组，而不是重复组。"}
:::

## 对彼此分隔的重复项分组

如果相同行彼此分隔，它们会形成不同的组：

```plaintext
book
paper
book
paper
article
magazine
article
```

对该文件运行 `uniq` 会得到看似意外的结果：

```bash
$ uniq reading.txt
book
paper
book
paper
article
magazine
article
```

由于相邻的值都不同，没有任何行被折叠。如果允许改变顺序，并希望把完全相同的行聚在一起，请先排序：

```bash
$ sort reading.txt | uniq
article
book
magazine
paper
```

两个步骤应使用一致的 locale 和比较规则。`sort -u reading.txt` 也可以在一个命令中完成排序，并为每个相等的排序键保留一行。

:::single-choice{#uniq-separated-duplicates} `reading.txt` 中的相同行散布在不同位置，且允许改变输出顺序。哪个管道会为每个不同的完整行生成一份已排序副本？

::option[`sort reading.txt | uniq`]{#sort-then-uniq .correct explanation="排序会把完全相同的行聚在一起，然后 `uniq` 把每个相邻组折叠为一行。"}
::option[`uniq reading.txt | sort`]{#uniq-before-sort explanation="在彼此分隔的相同行变得相邻之前，`uniq` 已经运行，因此之后排序仍可能留下重复输出行。"}
::option[`uniq -c reading.txt | head`]{#uniq-count-head explanation="这只统计现有相邻组并限制输出，不会在全局范围内聚合彼此分隔的重复项。"}
:::

未指定输入文件时，`uniq` 会读取 stdin，因此它很适合接在 `sort` 后面。GNU 的 `-i` 可以忽略大小写，而 `-f`、`-s` 和 `-w` 可以跳过或限制比较区域；只有当相等关系应由每行的一部分定义时才使用它们。

要练习对重复项进行分组、计数和筛选，可以尝试以下动手实验：

1. **[Linux uniq 命令：重复项筛选](https://labex.io/zh/labs/linux-linux-uniq-command-duplicate-filtering-219199)** - 学习结合使用 Linux `uniq` 与 `sort` 命令，识别、筛选和分析文本文件中的重复行。
2. **[Linux sort 命令：文本排序](https://labex.io/zh/labs/linux-linux-sort-command-text-sorting-219196)** - 练习使用 `sort` 整理文本文件中的行，这是有效使用 `uniq` 前的关键步骤。
3. **[单词计数和排序](https://labex.io/zh/labs/linux-word-count-and-sorting-388125)** - 在动手挑战中学习重要的 Linux 文本处理工具 `wc` 和 `sort`，统计行、单词和字符，查找常见模式并高效排列数据。

## 总结

现在，你可以使用 `uniq` 分析相邻的相同行组。

1. 把每个相邻重复组折叠为一行。
2. 使用 `-c` 统计连续出现次数。
3. 使用 `-u` 选择单行组。
4. 使用 `-d` 或 GNU `-D` 选择重复组。
5. 需要聚合彼此分隔的重复项时先排序。
