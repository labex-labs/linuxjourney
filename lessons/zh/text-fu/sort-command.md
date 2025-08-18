---
lang: "zh"
title: "sort"
meta_description: "学习如何使用 Linux sort 命令对文本文件进行排序。探索反向和数值排序等选项。提高你的 Linux 命令行技能！"
meta_keywords: "Linux sort 命令，sort -r, sort -n, Linux 教程，命令行，Linux 初学者，sort 指南"
---

## Lesson Content

`sort` 命令用于对行进行排序。

```plaintext
file1.txt
dog
cow
cat
elephant
bird

$ sort file1.txt
bird
cat
cow
dog
elephant
```

你也可以进行反向排序：

```bash
$ sort -r file1.txt
elephant
dog
cow
cat
bird
```

也可以按数值排序：

```bash
$ sort -n file1.txt
bird
cat
cow
elephant
dog
```

## Exercise

`sort` 命令真正的强大之处在于它能与其他命令结合使用。尝试以下命令，看看会发生什么：

```bash
ls /etc | sort -rn
```

## Quiz Question

你使用哪个标志来执行反向排序？

## Quiz Answer

-r
