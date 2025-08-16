---
lang: "zh"
title: "head"
description: "学习如何使用 Linux 'head' 命令查看文件的开头。了解 -n 等选项以控制行数。必备的 Linux 命令教程。"
keywords: "head 命令，Linux head, 查看文件开头，Linux 教程，Linux 命令，Linux 初学者，head -n, Linux 指南"
---

## Lesson Content

假设我们有一个很长的文件；事实上，我们有很多文件可供选择。继续 `cat /var/log/syslog`。你应该会看到一页又一页的文本。如果我只想看这个文本文件的前几行怎么办？嗯，我们可以用 `head` 命令来做到这一点。默认情况下，`head` 命令会显示文件的前 10 行。

```bash
head /var/log/syslog
```

你也可以将行数修改为你选择的任何值。假设我想看前 15 行。

```bash
head -n 15 /var/log/syslog
```

`-n` 标志代表“行数”。

## Exercise

以下命令的作用是什么，为什么？

```bash
head -c 15 /var/log/syslog
```

## Quiz Question

你会使用哪个标志来更改 `head` 命令要查看的行数？

## Quiz Answer

-n
