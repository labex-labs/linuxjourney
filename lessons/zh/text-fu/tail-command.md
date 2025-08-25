---
index: 9
lang: "zh"
title: "tail"
meta_title: "tail - 文本技巧"
meta_description: "学习如何在 Linux 中使用 `tail` 命令查看文件末尾和监控日志。了解 `tail -f` 以获取实时更新。开始你的 Linux 之旅！"
meta_keywords: "tail 命令，Linux tail, tail -f, 查看日志，Linux 教程，Linux 初学者，Linux 指南"
---

## Lesson Content

与 `head` 命令类似，`tail` 命令默认显示文件的最后 10 行。

```bash
tail /var/log/syslog
```

与 `head` 一样，你可以更改你想要查看的行数。

```bash
tail -n 10 /var/log/syslog
```

另一个很棒的选项是使用 `-f` (follow) 标志；这会随着文件的增长而跟踪文件。试一试，看看会发生什么。

```bash
tail -f /var/log/syslog
```

当你与系统交互时，你的 `syslog` 文件会不断变化，使用 `tail -f` 你可以看到所有添加到该文件中的内容。

## Exercise

熟能生巧！这里有一些动手实验来巩固你对 `tail` 命令及其应用的理解：

1. **[Linux tail 命令：文件末尾显示](https://labex.io/zh/labs/linux-linux-tail-command-file-end-display-214303)** - 学习 Linux `tail` 命令，用于查看和监控文本文件末尾，包括用于实时更新的 `-f` 选项。
2. **[在 Linux 中查看日志和配置文件](https://labex.io/zh/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - 练习使用 `tail`（以及 `cat` 和 `more`）来高效地查看和导航日志和配置文件，这对于系统监控至关重要。
3. **[快速威胁检测](https://labex.io/zh/labs/linux-rapid-threat-detection-387930)** - 运用你对 `tail` 的知识，快速提取和分析最近的日志条目，模拟网络安全环境中的快速威胁检测。

这些实验将帮助你在实际场景中应用查看和监控文件内容的概念，并增强对 `tail` 命令的信心。

## Quiz Question

在 `tail` 中用于跟踪文件的标志是什么？

## Quiz Answer

-f
