---
index: 8
lang: "zh"
title: "head"
meta_title: "head - 文本技巧"
meta_description: "学习如何使用 Linux 'head' 命令查看文件的开头。了解 -n 等选项的行数。基本的 Linux 命令教程。"
meta_keywords: "head 命令，Linux head, 查看文件开头，Linux 教程，Linux 命令，Linux 初学者，head -n, Linux 指南"
---

## Lesson Content

假设我们有一个非常长的文件；事实上，我们有很多文件可供选择。继续 `cat /var/log/syslog`。你应该会看到很多页的文本。如果我只想看这个文本文件的前几行怎么办？我们可以使用 `head` 命令来做到这一点。默认情况下，`head` 命令会显示文件的前 10 行。

```bash
head /var/log/syslog
```

你也可以将行数修改为你选择的任何数字。假设我想看前 15 行。

```bash
head -n 15 /var/log/syslog
```

`-n` 标志代表“行数”。

## Exercise

熟能生巧！这里有一些动手实验，可以加深你对查看文件开头和一般文本文件操作的理解：

1. **[Linux head 命令：文件开头显示](https://labex.io/zh/labs/linux-linux-head-command-file-beginning-display-214302)** - 本实验将指导你使用 `head` 命令显示文本文件的初始行，包括修改行数。
2. **[在 Linux 中查看日志和配置文件](https://labex.io/zh/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - 练习基本的 Linux 命令行技能，以高效地查看和导航文本文件，包括系统日志和配置文件，这些文件通常需要 `head` 等命令。
3. **[快速威胁检测](https://labex.io/zh/labs/linux-rapid-threat-detection-387930)** - 应用你对 `head`（和 `tail`）的知识，快速提取和分析最近的日志条目，模拟真实的网络安全分析。

这些实验将帮助你在实际场景中应用这些概念，并增强你在 Linux 中查看和分析文本文件的信心。

## Quiz Question

要更改 `head` 命令要查看的行数，你会使用哪个标志？

## Quiz Answer

-n
