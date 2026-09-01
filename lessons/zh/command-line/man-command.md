---
lesson_id: "man-command"
course_id: "command-line"
lang: "zh"
order_index: 16
title: "man 命令"
description: "学习打开、浏览、搜索和选择已安装手册页的章节。"
meta_title: "man 命令 - 命令行手册"
meta_description: "通过示例学习 Linux man 命令，了解如何阅读手册页、在手册页中搜索、理解章节以及查找命令选项。"
meta_keywords: "man 命令, linux man 页, 命令手册, man ls, man 章节, 搜索 man 页, 命令行帮助"
---

许多 Linux 命令、接口、配置文件和管理工具都有已安装的参考文档，称为手册页或 man 页。`man` 命令用于查找并显示这些页面。

## 打开手册页

要查看任何命令的手册，使用 `man` 后跟命令名称。例如，要阅读 `ls` 的手册，输入：

```bash
$ man ls
```

手册页通常包含概要、说明、选项、相关文件和交叉引用，但具体章节会有所不同。

:::single-choice{#open-ls-manual} 哪个命令会打开已安装的 `ls` 手册页？

::option[`help ls`]{#help-ls explanation="Bash 的 `help` 记录 shell 内建命令，通常不会打开外部 `ls` 的手册页。"}
::option[`man ls`]{#manual-ls-page .correct explanation="`man` 会在手册数据库中查找主题 `ls`，并显示匹配页面。"}
::option[`ls --help`]{#ls-usage explanation="这会让 `ls` 输出自己的用法摘要，并不会打开已安装的手册页。"}
:::

## 浏览和搜索页面

在许多系统上，`man` 会通过 `less` 等分页器显示页面。页面打开后，可以用方向键或翻页键滚动，并使用以下控制方式：

在 man 页内：

- 按 `/` 并输入搜索词向前搜索。
- 按 `n` 跳转到下一个匹配项。
- 按 `N` 跳转到上一个匹配项。
- 按 `q` 退出。

分页器可能因系统或环境而异，因此这些按键并非处处保证可用；它们适用于常见的 `less` 配置。

:::single-choice{#search-man-page} 手册页在 `less` 中打开时，如何开始向前搜索 `--recursive`？

::option[输入 `?--recursive` 并按 Enter。]{#backward-man-search explanation="问号会开始向后搜索，方向与题目要求相反。"}
::option[输入 `/--recursive` 并按 Enter。]{#forward-man-search .correct explanation="斜杠会在 `less` 中开始向前搜索，按 Enter 提交模式。"}
::option[输入 `n--recursive` 并按 Enter。]{#repeat-man-search explanation="`n` 用于重复已有搜索，不能以这种方式引入新搜索模式。"}
:::

:::single-choice{#leave-man-page} 手册页在常用分页器中打开时，哪个按键会返回 shell？

::option[`G`]{#man-page-end explanation="大写 `G` 会在 `less` 中移到页面末尾，不会关闭分页器。"}
::option[`n`]{#next-man-match explanation="`n` 会重复最近的搜索，手册页仍保持打开。"}
::option[`q`]{#quit-man .correct explanation="`q` 会退出常用分页器，并把控制权还给 shell。"}
:::

## 选择手册章节

手册页按编号章节组织。常见章节包括：

- `1`：用户命令。
- `2`：系统调用。
- `3`：库函数。
- `5`：文件格式。
- `8`：系统管理命令。

有时同一名称会出现在多个章节中。你可以指定章节号：

```bash
$ man 5 passwd
$ man 1 passwd
```

第一条命令打开第 5 节中记录 `passwd` 文件格式的页面，第二条打开第 1 节的用户命令页面。`passwd(5)` 这样的引用使用同样的“主题（章节）”记法。

:::single-choice{#open-passwd-file-format} 哪个命令会打开记录 `passwd` 文件格式的第 5 节页面？

::option[`man passwd 5`]{#section-after-topic explanation="在这种命令形式中，章节选择符应位于主题之前；这个顺序不会请求 `passwd(5)`。"}
::option[`man 5 passwd`]{#passwd-format-page .correct explanation="把章节 `5` 放在 `passwd` 前面，会明确选择文件格式页面。"}
::option[`man 1 passwd`]{#passwd-command-page explanation="第 1 节包含用户命令，因此这里选择的是 `passwd` 命令页面，而不是文件格式页面。"}
:::

## 页面缺失时

并非每个命令名都有单独安装的手册页。如果 `man` 报告没有对应条目：

- 运行 `type NAME` 查看 Bash 如何解析该名称。
- 如果它是 Bash 内建命令，使用 `help NAME`。
- 如果外部程序支持这一约定，尝试 `NAME --help`。
- 检查发行版是否提供单独的文档软件包。

:::single-choice{#missing-builtin-manual} `type cd` 报告 `cd` 是 Bash 内建命令，而且没有单独手册页。接下来应该尝试哪个命令？

::option[`whatis cd`]{#whatis-missing-cd explanation="`whatis` 汇总手册数据库中的条目，无法提供缺失的内建命令专用页面。"}
::option[`file cd`]{#file-cd-name explanation="`file` 对文件系统对象分类，但这里 `cd` 被解析为 shell 内建命令，而不是路径。"}
::option[`help cd`]{#builtin-cd-help .correct explanation="Bash 的 `help` 内建命令会提供 shell 自己为 `cd` 编写的文档。"}
:::

## 总结

现在，你可以查找和浏览已安装的手册文档。

1. 按主题名称打开页面。
2. 在常用分页器中搜索并浏览页面。
3. 退出分页器并返回 shell。
4. 选择带编号的手册章节。
5. 页面不可用时选择其他帮助来源。
