---
lesson_id: "help-command"
course_id: "command-line"
lang: "zh"
order_index: 15
title: "help 命令"
description: "学习根据命令类型选择内建帮助、程序用法输出或手册页。"
meta_title: "help - 命令行帮助"
meta_description: "学习如何通过 Bash help、--help 输出、man 手册页和 type 命令获取 Linux 命令行帮助，包括 shell 内置命令和外部命令。"
meta_keywords: "linux help 命令, bash help, 命令行帮助, --help, shell 内置命令, man 命令, type 命令"
---

你不必记住每个命令选项。Bash 和许多已安装程序都能直接在终端中说明自己的语法，但应根据所使用的命令类型选择帮助来源。

## 获取 Bash 内建命令的帮助

最直接的工具之一是 `help`，这是一个直接内置在 Bash shell 中的命令。它专门用于提供其他 Bash 内置命令的信息。内置命令是 shell 自身的一部分，而不是独立的程序。示例包括 `echo`、`cd` 和 `pwd`。

使用 `help` 时，输入它后跟内置命令的名称。

```bash
$ help echo
```

输出会说明内建命令的语法和行为。不带参数运行 `help` 会列出 Bash 能够提供帮助的内建命令。

:::single-choice{#help-for-bash-cd} 哪个命令会显示 Bash 为其内建 `cd` 命令提供的帮助条目？

::option[`cd --help`]{#cd-help-option explanation="某些内建命令可能识别选项，但 Bash 的专用文档接口是 `help` 后接内建命令名。"}
::option[`help cd`]{#help-cd .correct explanation="Bash 的 `help` 内建命令会查找指定内建命令的文档，这里指定的是 `cd`。"}
::option[`type cd`]{#type-cd explanation="`type` 说明 Bash 如何解析名称 `cd`，能识别命令类型，但不会显示完整帮助条目。"}
:::

## 请求程序的用法摘要

对于大多数不是内置于 shell 的其他可执行程序，`help` 命令不起作用。相反，常见的约定是提供一个 `--help` 选项。该选项会让程序打印使用说明摘要，然后退出。

```bash
$ ls --help
```

这是常见约定，但并非所有程序都支持。应阅读输出和退出状态，不要假定每个程序都接受相同选项。

:::single-choice{#quick-ls-usage} 哪个命令通常会打印外部程序 `ls` 自己提供的快速用法摘要？

::option[`help ls`]{#bash-help-ls explanation="Bash 的 `help` 记录 shell 内建命令；在典型系统上，它不提供外部 `ls` 程序的用法页面。"}
::option[`ls --help`]{#ls-help .correct explanation="GNU `ls` 遵循常见的 `--help` 约定，会打印用法和选项。"}
::option[`type --help ls`]{#type-help-ls explanation="这会询问 `type` 内建命令如何处理自己的选项，而不是让 `ls` 说明其用法。"}
:::

## 查明 Bash 如何解析名称

如果你不确定某个命令是 Bash 内置命令还是外部程序，可以使用 `type`。

```bash
$ type cd
cd is a shell builtin
$ type ls
ls is /usr/bin/ls
```

具体结果会随别名、函数、已安装程序和 `PATH` 而变化。要让 Bash 显示所有已知解析结果，而不是只显示优先使用的第一个，请使用 `type -a NAME`。

:::single-choice{#identify-command-resolution} 你不知道 `deploy` 是别名、函数、内建命令还是可执行文件。哪个 Bash 命令会检查这个名称如何解析？

::option[`type deploy`]{#type-deploy .correct explanation="`type` 内建命令会报告 Bash 在当前 shell 环境中如何解释这个命令名。"}
::option[`help deploy`]{#help-deploy explanation="`help` 会查找 Bash 内建文档，通常不能识别别名、函数和外部文件。"}
::option[`deploy --help`]{#deploy-help explanation="这会尝试运行命令，并依赖它自身对选项的支持，不能先说明 Bash 如何解析该名称。"}
:::

## 选择详细程度

- 对于 Bash 内置命令如 `cd`、`echo` 和 `history`，使用 `help COMMAND`。
- 对于许多外部命令，使用 `COMMAND --help` 获取快速摘要。
- 使用 `man COMMAND` 查看详细的手册页。
- 使用 `whatis COMMAND` 获取一行描述。

下一课会更详细地介绍手册页和单行描述。

:::single-choice{#choose-detailed-manual} 你需要外部命令 `ls` 的详细文档，而不只是简短用法摘要。应该尝试哪个命令？

::option[`man ls`]{#man-ls .correct explanation="`man ls` 会打开已安装的手册页，通常更完整地说明语法、选项和行为。"}
::option[`whatis ls`]{#whatis-ls explanation="`whatis` 用于显示简洁的手册页描述，并非这里要求的详细文档。"}
::option[`type ls`]{#type-ls explanation="`type` 会报告 Bash 如何解析 `ls`，但不会显示程序的详细手册。"}
:::

## 总结

现在，你可以根据 Bash 解析命令的方式选择合适的帮助来源。

1. 对 Bash 内建命令使用 `help`。
2. 尝试用 `--help` 获取程序的快速用法输出。
3. 使用 `type` 检查名称解析结果。
4. 使用 `man` 打开详细文档。
