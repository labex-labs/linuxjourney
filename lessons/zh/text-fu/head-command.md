---
index: 8
lang: "zh"
title: "head 命令"
meta_title: "head 命令 - Text-Fu"
meta_description: "一份关于如何使用 head 命令查看文件开头的初学者 Linux 指南。学习如何使用 head -n 选项控制行数，这是任何 Linux 教程中的基本技能。"
meta_keywords: "head 命令，Linux head, 查看文件开头，Linux 教程，Linux 命令，初学者 Linux, head -n, Linux 指南，文本文件，命令行"
---

## Lesson Content

在 Linux 中，您经常需要检查非常大的文件内容，例如系统日志。例如，如果您运行 `cat /var/log/syslog`，您会看到几页文本滚动而过，很难快速了解概况。那么，如果您只想**查看文件开头**怎么办呢？`head` 命令是完成此任务的完美工具。

### head 命令的默认行为

默认情况下，`head` 命令会显示任何给定文件的前 10 行。这是我们处理文本的**Linux 入门指南**中的基本部分。要查看其实际效果，只需提供一个文件名作为参数即可：

```bash
head /var/log/syslog
```

此命令将输出 `/var/log/syslog` 的前 10 行，使您无需在编辑器中打开文件即可快速检查文件的初始内容。

### 自定义行数

**Linux head** 命令非常灵活。您可以使用 `-n` 标志轻松更改它显示的行数，该标志代表“行数”（number of lines）。例如，如果您想查看文件的前 15 行，您将像这样使用 `head -n` 选项：

```bash
head -n 15 /var/log/syslog
```

这使得 `head` 成为快速检查文件头或日志条目时最有用的**Linux 命令**之一。

## Exercise

熟能生巧！以下是一些实践操作实验，以加强您对查看文件开头和一般文本文件操作的理解：

1. **[Linux head 命令：文件开头显示](https://labex.io/zh/labs/linux-linux-head-command-file-beginning-display-214302)** - 此实验将指导您使用 `head` 命令显示文本文件的初始行，包括修改行数。
2. **[在 Linux 中查看日志和配置文件](https://labex.io/zh/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - 练习基本的 Linux 命令行技能，以有效地查看和导航文本文件，包括系统日志和配置文件，这些文件通常需要 `head` 等命令。
3. **[快速威胁检测](https://labex.io/zh/labs/linux-rapid-threat-detection-387930)** - 应用您对 `head`（和 `tail`）的知识，快速提取和分析最近的日志条目，模拟现实世界中的网络安全分析。

这些实验将帮助您在实际场景中应用这些概念，并增强您在 Linux 中进行文本文件查看和分析的信心。

## Quiz Question

您会使用 `head` 命令的哪个标志来更改您想要查看的行数？请仅使用英文标志回答，注意区分大小写。

## Quiz Answer

-n
