---
lesson_id: "whatis-command"
course_id: "command-line"
lang: "zh"
order_index: 17
title: "whatis 命令"
description: "学习获取简洁的手册页描述，并理解其中的章节编号。"
meta_title: "whatis 命令 - 命令行指南"
meta_description: "学习 Linux whatis 命令，通过示例了解如何从手册页获取命令的一行描述，以及理解多个手册章节。"
meta_keywords: "whatis 命令, linux whatis, 命令描述 linux, 手册页摘要, 命令行帮助, apropos"
---

当你认得一个命令名，却忘了它的用途时，`whatis` 可以从手册页数据库中提供简短提示。

## 查找准确名称

使用 `whatis` 非常简单。输入 `whatis` 后跟你想了解的命令。

```bash
$ whatis cat
cat (1)              - concatenate files and print on the standard output
```

输出是描述，而不是命令选项或示例列表。需要更多细节时，请使用 `man cat` 或 `cat --help`。

:::single-choice{#describe-known-command} 你知道名称 `cat`，并想查看它的一行手册页描述。应该运行哪个命令？

::option[`man cat`]{#manual-cat explanation="`man cat` 会打开完整手册页，提供的内容多于所需的一行提示。"}
::option[`apropos cat`]{#apropos-cat explanation="`apropos` 会按关键词搜索描述，可能返回许多相关主题，范围比准确名称查找更广。"}
::option[`whatis cat`]{#whatis-cat .correct explanation="`whatis` 会查找准确主题名称，并打印手册数据库中的简洁描述。"}
:::

## 读取章节编号

如果同一主题在多个章节中都有手册页，`whatis` 可能显示多条结果：

```bash
$ whatis passwd
passwd (1)           - change user password
passwd (5)           - the password file
```

括号中的数字是手册章节。这里 `passwd(1)` 说明用户命令，`passwd(5)` 说明文件格式。可以用 `man 1 passwd` 或 `man 5 passwd` 明确打开其中一页。

:::single-choice{#interpret-whatis-section} 在输出 `passwd (5) - the password file` 中，`(5)` 表示什么？

::option[`passwd` 命令接受的第五个选项。]{#fifth-option explanation="该数字不是选项位置；选项记录在所选手册页内部。"}
::option[包含文件格式页面的手册章节。]{#section-five .correct explanation="第 5 节用于记录文件格式和约定，因此 `passwd(5)` 指向该手册章节。"}
::option[共有五个名为 `passwd` 的手册页。]{#five-pages explanation="同名页面可以有多个，但括号中的值表示章节，而不是页面数量。"}
:::

## 在 whatis、man 和 apropos 之间选择

- `whatis ls`：显示精确命令名称的一行描述。
- `man ls`：打开完整的手册页。
- `apropos 关键词`：搜索手册页描述中的关键词。

例如：

```bash
$ apropos password
```

不知道命令名但知道任务时，请使用 `apropos`；已经知道名称时，请使用 `whatis`。

:::single-choice{#search-by-purpose} 你不知道命令名，但想在手册描述中搜索关键词 `password`。哪个命令适合这项任务？

::option[`apropos password`]{#apropos-password .correct explanation="`apropos` 会在手册页名称和描述中搜索关键词，帮助发现相关主题。"}
::option[`whatis password`]{#exact-password explanation="`whatis` 会查找准确名为 `password` 的手册主题，并不是通用关键词搜索接口。"}
::option[`man password`]{#manual-password explanation="`man` 会尝试打开该主题名的页面，不会执行所需的描述搜索。"}
:::

## 没有显示描述时

如果 `whatis` 报告没有合适条目，该主题可能没有已安装的手册页，或者手册数据库已经过期。这个结果并不能证明不存在同名可执行文件、别名、函数或内建命令。请用 `type NAME` 查看 Bash 如何解析命令名，再选择合适的帮助来源。

:::single-choice{#whatis-versus-type} `whatis deploy` 找不到手册描述。哪个命令会检查 Bash 是否把 `deploy` 解析为别名、函数、内建命令或可执行文件？

::option[`whatis -r deploy`]{#whatis-regex-deploy explanation="改变手册数据库查询方式，并不能显示 Bash 中所有别名、函数、内建命令和路径解析结果。"}
::option[`man 5 deploy`]{#manual-five-deploy explanation="这会尝试打开第 5 节页面，并不能确定 Bash 如何解析命令名。"}
::option[`type deploy`]{#resolve-deploy .correct explanation="Bash 的 `type` 会报告当前 shell 如何解析命令名，不受是否安装手册描述影响。"}
:::

## 总结

现在，你可以从手册数据库中获取并理解简洁描述。

1. 使用 `whatis` 查找准确主题。
2. 读取括号中显示的手册章节。
3. 需要完整页面时使用 `man`。
4. 知道关键词而非名称时使用 `apropos`。
