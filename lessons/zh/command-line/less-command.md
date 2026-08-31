---
lesson_id: "less-command"
course_id: "command-line"
lang: "zh"
order_index: 8
title: "less 命令"
description: "学习使用 less 交互式浏览、搜索和跟踪长文本文件。"
meta_title: "less 命令 - 命令行工具"
meta_description: "通过示例学习 Linux 中的 less 命令，用于查看大文件、滚动、搜索、跳转到指定行、跟踪日志以及退出 less。"
meta_keywords: "less 命令, linux less, 查看大文件 linux, less 中搜索, 退出 less, less -N, less +F, 文本查看器 linux"
---

当文本文件长到一屏放不下时，`less` 让你阅读它，而不会让整个文件在终端中一滚而过。它的名称引出了 Unix 中“less is more”的老笑话，因为 `more` 是另一款分页器。

## 打开文件

要开始查看文件，使用 `less` 后跟文件名。

```bash
$ less /home/pete/Documents/text1
```

`less` 运行期间，按键会控制分页器，而不是启动普通 shell 命令。退出分页器后才会返回 shell。

:::single-choice{#open-long-file}
哪个命令会在交互式分页器中打开 `/var/log/syslog`？

::option[`less /var/log/syslog`]{#page-log .correct explanation="`less` 会在分页器中打开文件，供你移动、搜索，再退出回到 shell。"}
::option[`cat /var/log/syslog`]{#print-log explanation="`cat` 会一次把整个文件发送到标准输出，不提供交互式分页控制。"}
::option[`file /var/log/syslog`]{#classify-log explanation="`file` 报告可能的内容类型，并不会打开日志供交互式阅读。"}
:::

## 在 less 中导航

你可以使用多种按键在文档中移动：

- **方向键和翻页键**：使用 `Page Up`、`Page Down`、`Up` 和 `Down` 逐行或逐页导航。
- **跳转到开头**：按 `g` 直接跳转到文本文件开头。
- **跳转到结尾**：按 `G`（Shift + g）跳转到文本文件末尾。
- **移动半页**：按 `u` 向上移动半页，按 `d` 向下移动半页。
- **帮助菜单**：如果在 `less` 中忘记命令，按 `h` 显示帮助摘要。

:::single-choice{#jump-to-file-end}
哪个按键会直接跳到 `less` 中文件的末尾？

::option[`g`]{#lowercase-g explanation="小写 `g` 会跳到文件开头，大写形式则向相反方向移动。"}
::option[`G`]{#uppercase-g .correct explanation="大写 `G` 会跳到输入末尾；该命令区分大小写。"}
::option[`h`]{#help-key explanation="`h` 会打开分页器帮助屏幕，而不会跳到文件末尾。"}
:::

## 在 less 中搜索

`less` 的一个强大功能是搜索文本。输入 `/` 后跟你想查找的文本，然后按回车。

- `/search_term`：向前搜索 "search_term"。
- `?search_term`：向后搜索 "search_term"。
- `n`：按相同方向重复搜索。
- `N`：按相反方向重复搜索。

:::single-choice{#repeat-search-direction}
向前搜索 `error` 后，哪个按键会按相同方向继续搜索？

::option[`n`]{#same-search .correct explanation="小写 `n` 会按原方向重复最近的搜索；这里的方向是向前。"}
::option[`N`]{#opposite-search explanation="大写 `N` 会按相反方向重复最近的搜索；向前搜索后，它会向后查找匹配项。"}
::option[`g`]{#search-to-start explanation="`g` 会跳到输入开头，并不会重复搜索。"}
:::

## 离开 less

查看完文件后，你需要知道如何退出 `less` 并返回命令提示符。

按 `q` 退出 `less` 并返回 shell 提示符。

:::single-choice{#quit-less}
哪个按键会退出 `less` 并返回 shell？

::option[`q`]{#less-quit .correct explanation="`q` 命令会退出分页器并恢复 shell 提示符。"}
::option[`h`]{#less-help explanation="`h` 会在 `less` 中打开帮助，不会直接返回 shell。"}
::option[`G`]{#less-end explanation="大写 `G` 会移动到输入末尾，分页器仍保持打开。"}
:::

## 带选项启动 less

你可以带选项启动 `less`：

```bash
$ less -N file.txt
$ less +G file.txt
$ less +F /var/log/syslog
```

- `-N`：显示行号。
- `+G`：打开时跳转到文件末尾。
- `+F`：跟踪新增内容，类似于 `tail -f`。

在使用 `+F` 跟踪文件时，按 `Ctrl+C` 停止跟踪并返回正常导航，然后按 `q` 退出。使用 `-i` 可在搜索模式不含大写字母时忽略大小写，使用 `-I` 则无论模式如何都忽略大小写。

命令输出也可通过管道发送给 `less`：

```bash
$ dmesg | less
```

:::single-choice{#follow-growing-log}
哪个命令会打开 `/var/log/syslog` 并跟踪随后写入的新内容？

::option[`less +F /var/log/syslog`]{#follow-log .correct explanation="`+F` 初始命令会进入跟踪模式，因此 `less` 会显示追加到日志的新内容。"}
::option[`less +G /var/log/syslog`]{#open-at-log-end explanation="`+G` 初始命令会从末尾打开文件，但不会继续跟踪随后到达的内容。"}
::option[`less -N /var/log/syslog`]{#number-log-lines explanation="`-N` 会显示行号，并不会启用持续跟踪。"}
:::

要练习分页、搜索和阅读系统文本，可以尝试以下动手实验：

1. **[Linux less 命令：文件分页](https://labex.io/zh/labs/linux-linux-less-command-file-paging-214301)** - 学习使用 `less` 高效查看和导航文本文件，包括搜索、行号和模式匹配。
2. **[在 Linux 中查看日志和配置文件](https://labex.io/zh/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - 使用 `cat`、`more` 和 `less` 等命令，高效查看和导航系统日志与配置文件。

## 总结

现在，你可以使用 `less` 查看长文件，而不会让内容淹没终端。

1. 在分页器中打开文件或管道传入的命令输出。
2. 导航到输入中的指定位置。
3. 向前或向后搜索并重复搜索。
4. 显示行号或跟踪持续增长的内容。
5. 安全退出并返回 shell。
