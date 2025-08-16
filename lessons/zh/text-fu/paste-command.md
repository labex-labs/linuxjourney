---
lang: "zh"
title: "paste"
description: "学习如何使用 Linux paste 命令合并文件行。通过这个重要的 Linux 命令教程，了解分隔符并组合文件。"
keywords: "Linux paste 命令，paste 命令教程，合并文件行，Linux 命令，Linux 初学者，Linux 指南"
---

## Lesson Content

`paste` 命令类似于 `cat` 命令；它将文件中的行合并在一起。让我们创建一个包含以下内容的新文件：

```
sample2.txt
The
quick
brown
fox
```

让我们将所有这些行合并到一行中：

```bash
paste -s sample2.txt
```

`paste` 的默认分隔符是 TAB，所以现在有一行，每个单词之间用 TAB 分隔。

让我们将此分隔符 (`-d`) 更改为更具可读性的内容：

```bash
paste -d ' ' -s sample2.txt
```

现在所有内容都应该在一行中，并由空格分隔。

## Exercise

尝试将多个文件粘贴在一起。会发生什么？

## Quiz Question

使用 `paste` 命令时，您使用哪个标志将所有内容放在一行上？

## Quiz Answer

-s
