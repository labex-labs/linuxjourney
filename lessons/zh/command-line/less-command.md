---
index: 8
lang: "zh"
title: "less 命令"
meta_title: "less 命令 - 命令行工具"
meta_description: "通过示例学习 Linux 中的 less 命令，用于查看大文件、滚动、搜索、跳转到指定行、跟踪日志以及退出 less。"
meta_keywords: "less 命令, linux less, 查看大文件 linux, less 中搜索, 退出 less, less -N, less +F, 文本查看器 linux"
---

## Lesson Content

当查看过大无法在单屏显示的文本文件时，`less` 命令是一个非常有用的工具。正如老 Unix 谚语所说，“less is more”（少即是多）。这句话也暗指存在一个功能类似的 `more` 命令。

`less` 工具以分页格式显示文本，允许你在不淹没终端的情况下浏览文件。

### 使用 less 命令入门

要开始查看文件，使用 `less` 后跟文件名。

```bash
$ less /home/pete/Documents/text1
```

进入 `less` 查看器后，标准的 shell 命令将无法使用。你需要使用一组特定的按键来导航和操作文本。

### 导航和控制

你可以使用多种按键在文档中移动：

- **方向键和翻页键**：使用 `Page Up`、`Page Down`、`Up` 和 `Down` 逐行或逐页导航。
- **跳转到开头**：按 `g` 直接跳转到文本文件开头。
- **跳转到结尾**：按 `G`（Shift + g）跳转到文本文件末尾。
- **移动半页**：按 `u` 向上移动半页，按 `d` 向下移动半页。
- **帮助菜单**：如果在 `less` 中忘记命令，按 `h` 显示帮助摘要。

### 在 less 中搜索

`less` 的一个强大功能是搜索文本。输入 `/` 后跟你想查找的文本，然后按回车。

- `/search_term`：向前搜索 "search_term"。
- `?search_term`：向后搜索 "search_term"。
- `n`：跳转到搜索词的下一个匹配项。
- `N`：跳转到搜索词的上一个匹配项。

### 如何退出 less

查看完文件后，你需要知道如何退出 `less` 并返回命令提示符。

- **退出**：只需按 `q` 退出 `less` 查看器，返回 shell。

### 有用的 less 选项

你可以带选项启动 `less`：

```bash
$ less -N file.txt
$ less +G file.txt
$ less +F /var/log/syslog
```

- `-N`：显示行号。
- `+G`：打开时跳转到文件末尾。
- `+F`：跟踪新增内容，类似于 `tail -f`。

在使用 `+F` 跟踪文件时，按 `Ctrl-C` 停止跟踪并返回正常导航，然后按 `q` 退出。

### 常见问题

**less 比 cat 更好吗？** 对于短文件使用 `cat`，对于长文件或需要搜索的文件使用 `less`。

**如何进行不区分大小写的搜索？** 启动 `less` 时加 `-i`，或者在许多系统中，当搜索模式没有大写字母时，搜索默认不区分大小写。

**less 能打开命令输出吗？** 可以。将输出通过管道传入，例如 `dmesg | less`。

## Exercise

实践出真知！以下是一些动手实验，帮助你巩固在 Linux 中查看和导航文本文件的理解：

1. **[Linux less 命令：文件分页](https://labex.io/zh/labs/linux-linux-less-command-file-paging-214301)** - 学习 Linux 中的 'less' 命令，实现高效的文本文件查看和导航，包括搜索、行号和模式匹配。
2. **[Linux more 命令：文件滚动](https://labex.io/zh/labs/linux-linux-more-command-file-scrolling-214299)** - 学习 Linux 中的 'more' 命令，实现高效的文本文件查看，涵盖基本用法、从特定行开始以及自定义显示。
3. **[在 Linux 中查看日志和配置文件](https://labex.io/zh/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - 学习必备的 Linux 命令行技能，高效查看和导航文本文件，包括系统日志和配置文件，使用 `cat`、`more` 和 `less` 等命令。

这些实验将帮助你在实际场景中应用概念，增强对文本文件操作和导航的信心。

## Quiz Question

如何退出 `less` 命令？请提供单个字符键作为答案。注意：答案区分大小写。

## Quiz Answer

q
