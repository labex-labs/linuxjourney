---
lang: "zh"
title: "uniq (唯一)"
description: "学习如何使用 Linux `uniq` 命令从文本文件中删除重复行。探索 -c、-u、-d 等选项，并结合 `sort` 进行有效的数据清理。"
keywords: "uniq 命令，Linux uniq, 删除重复项，sort uniq, Linux 教程，文本处理，Linux 初学者，Linux 指南"
---

## Lesson Content

`uniq` (unique) 命令是另一个用于解析文本的有用工具。

假设你有一个包含许多重复内容的文档：

```plaintext
reading.txt
book
book
paper
paper
article
article
magazine
```

如果你想删除重复项，可以使用 `uniq` 命令：

```bash
$ uniq reading.txt
book
paper
article
magazine
```

让我们获取每行出现的次数：

```bash
$ uniq -c reading.txt
2 book
2 paper
2 article
1 magazine
```

让我们只获取唯一值：

```bash
$ uniq -u reading.txt
magazine
```

让我们只获取重复值：

```bash
$ uniq -d reading.txt
book
paper
article
```

**注意**：`uniq` 只有在重复行相邻时才能检测到它们。例如：

假设你有一个包含不相邻重复内容的文档：

```plaintext
reading.txt
book
paper
book
paper
article
magazine
article
```

```bash
$ uniq reading.txt
reading.txt
book
paper
book
paper
article
magazine
article
```

`uniq` 返回的结果将包含所有条目，与第一个示例不同。

为了克服 `uniq` 的这个限制，我们可以将 `sort` 与 `uniq` 结合使用：

```bash
$ sort reading.txt | uniq
article
book
magazine
paper
```

## Exercise

如果你尝试 `uniq -uc` 会得到什么结果？

## Quiz Question

你会使用什么命令来删除文件中的重复项？

## Quiz Answer

uniq
