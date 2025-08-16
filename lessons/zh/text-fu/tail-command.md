---
lang: "zh"
title: "tail"
description: "学习如何在 Linux 中使用 `tail` 命令查看文件末尾并监控日志。了解 `tail -f` 以获取实时更新。开始你的 Linux 之旅！"
keywords: "tail 命令，Linux tail, tail -f, 查看日志，Linux 教程，Linux 初学者，Linux 指南"
---

## Lesson Content

与 `head` 命令类似，`tail` 命令默认显示文件的最后 10 行。

```bash
tail /var/log/syslog
```

与 `head` 命令一样，你可以更改想要查看的行数。

```bash
tail -n 10 /var/log/syslog
```

另一个你可以使用的很棒的选项是 `-f` (follow) 标志；这会随着文件增长而持续跟踪文件。尝试一下，看看会发生什么。

```bash
tail -f /var/log/syslog
```

当你与系统交互时，你的 `syslog` 文件会不断变化，使用 `tail -f` 你可以看到所有添加到该文件的内容。

## Exercise

查看 `tail` 的手册页，阅读我们没有讨论过的一些其他命令。

```bash
man tail
```

## Quiz Question

在 `tail` 中用于跟踪文件的标志是什么？

## Quiz Answer

-f
