---
lesson_id: "env-environment"
course_id: "text-fu"
lang: "zh"
order_index: 5
title: "env (环境变量)"
description: "学习 Bash 如何展开、导出、检查和临时覆盖环境变量。"
meta_title: "env (环境变量) - Text-Fu"
meta_description: "了解 Linux 中的 env 命令的作用。本指南解释了如何使用 env linux 命令查看和使用 PATH、HOME 和 USER 等 Linux 环境变量。"
meta_keywords: "env, linux env, env linux, env 命令 linux, linux env 命令，env 在 linux 中做什么，环境变量，PATH 变量，shell 变量"
---

每个进程都有一个环境，即从父进程继承的一组名称—值字符串。shell 使用环境变量，把语言设置、可执行文件搜索路径等配置传递给它启动的程序。

## 在 Bash 中展开变量值

Bash 会在运行命令前把 `$NAME` 或 `${NAME}` 展开为变量值。为保留完整值作为一个参数，应给展开式加引号：

```bash
$ printf '%s\n' "$HOME"
/home/pete
```

常见环境变量包括：

- `HOME`：当前用户的主目录路径。
- `USER`：许多系统的登录环境所提供的用户名。
- `PWD`：shell 的当前工作目录。
- `PATH`：用于搜索命令名的目录。

值取决于当前进程环境，并不是通用常量。除非启用了更严格的 shell 行为，未设置变量会展开为空字符串。

:::single-choice{#env-print-home-value} 哪个 Bash 命令会打印 `HOME` 的值，同时保留它作为一个参数？

::option[`printf '%s\n' '$HOME'`]{#env-literal-home explanation="单引号会阻止参数展开，因此打印的是字面字符 `$HOME`。"}
::option[`printf '%s\n' "$HOME"`]{#env-quoted-home .correct explanation="Bash 会在双引号内展开 `$HOME`，`printf` 收到完整值作为一个参数。"}
::option[`printf '%s\n' HOME`]{#env-name-home explanation="没有美元符号或参数语法时，`HOME` 是普通文字，不是变量展开式。"}
:::

## 检查当前环境

要查看当前为您的会话设置的所有环境变量，您可以使用 `env` 命令。`linux env command` 是检查 shell 配置的基本工具。

```bash
env
```

输出由 `NAME=value` 记录组成，例如：

```plaintext
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/bin
PWD=/home/user
USER=pete
```

环境变量可能包含凭据、令牌、内部路径或其他敏感数据。把完整 `env` 输出粘贴到公开问题或日志前，必须先审查并遮盖敏感值。

:::single-choice{#env-list-exported-values} 哪个命令会打印新启动进程能够看到的环境？

::option[`env`]{#env-print-all .correct explanation="不带命令和赋值时，`env` 会打印它收到的名称—值环境。"}
::option[`alias`]{#env-alias-list explanation="`alias` 列出 shell 别名定义；它们属于 shell 状态，而不是已导出的环境记录。"}
::option[`history`]{#env-history-list explanation="`history` 显示 shell 记住的命令行，并不会列举已导出的变量。"}
:::

## 通过 PATH 查找命令

在您的 `env linux` 输出中最重要的变量之一是 `PATH`。您可以使用以下命令专门查看其内容：

```bash
$ printf '%s\n' "$PATH"
```

`PATH` 是以冒号分隔的目录列表。当命令名不含斜杠时，Bash 会搜索这些目录。

顺序很重要：Bash 会根据名称解析规则使用第一个合适命令。可用 `type -a NAME` 检查当前 shell 如何解析名称。

要在当前 shell 及其未来子进程中把 `/opt/coolapp/bin` 加到现有搜索路径前面：

```bash
$ export PATH="/opt/coolapp/bin:$PATH"
```

不要意外用新目录完全替换 `PATH`，也不要加入不受信任的可写目录。前者可能让正常命令无法解析，后者可能导致运行意外的可执行文件。

:::single-choice{#env-prepend-path-directory} 哪个命令会在当前 Bash 进程及其未来子进程中，把 `/opt/coolapp/bin` 加到现有 `PATH` 前面？

::option[`export PATH="/opt/coolapp/bin"`]{#env-replace-path explanation="这会丢弃所有现有搜索目录，可能导致普通命令难以找到。"}
::option[`export PATH="/opt/coolapp/bin:$PATH"`]{#env-export-path .correct explanation="这会把新目录放在前面，保留旧值，并把结果导出给子进程。"}
::option[`PATH='$PATH:/opt/coolapp/bin'`]{#env-literal-path explanation="单引号会保留字面文字 `$PATH`，而且该赋值没有导出给未来子进程。"}
:::

## 把变量导出给子进程

Bash 变量不会自动成为传给子进程的环境。使用 `export` 标记要导出的名称：

```bash
export TEST=test
```

当前 Bash 进程现在拥有名为 `TEST` 的变量，它启动的命令会继承 `TEST=test`。子进程不能借此改变父进程的环境。

```bash
$ printenv TEST
test
```

该赋值通常持续到取消设置或 shell 退出为止，并不会修改系统级环境。

:::single-choice{#env-export-inheritance} 在 Bash 中，`export TEST=test` 的主要效果是什么？

::option[把 `TEST` 写入所有用户的系统配置。]{#env-system-wide explanation="赋值影响当前 shell 和其子进程的继承，而不是所有用户或整个操作系统。"}
::option[标记 `TEST=test`，供未来子进程继承。]{#env-child-inheritance .correct explanation="`export` 会把 shell 变量加入 Bash 传给所启动命令的环境。"}
::option[改变已经运行的进程的环境。]{#env-existing-processes explanation="已经存在的无关进程或子进程会保留各自环境；导出只影响之后启动的进程。"}
:::

## 为单条命令设置值

把赋值放在命令前，只向该命令的环境提供值：

```bash
$ LANG=C sort names.txt
```

当前 shell 的 `LANG` 不会永久改变。`env` 工具也提供另一种显式形式：

```bash
$ env LANG=C sort names.txt
```

使用 `env -i COMMAND` 可让命令从初始空环境启动，再添加所需赋值。许多程序依赖环境值，因此应谨慎使用。

:::single-choice{#env-one-command-value} 哪个命令会以 `LANG=C` 运行 `sort names.txt`，但不永久改变当前 shell 的 `LANG`？

::option[`env LANG=C sort names.txt`]{#env-lang-sort .correct explanation="`env` 会把赋值加入所启动命令的环境，父 shell 保留原值。"}
::option[`export LANG=C; sort names.txt`]{#env-export-lang explanation="这会在当前 shell 中导出 `LANG=C`，并在 `sort` 结束后继续保留改动。"}
::option[`env -i sort names.txt`]{#env-empty-sort explanation="这会从空环境启动，但没有设置题目要求的 `LANG=C`。"}
:::

## 在未来会话中加载个人变量

要让未来的交互式 Bash 会话重新创建导出变量，应把合适的 `export` 行放在这些会话实际读取的启动文件中；对于交互式非登录 Bash，通常是 `~/.bashrc`：

```bash
export TEST=test
```

Zsh 通常使用 `~/.zshrc`，Fish 则采用不同语法和配置。登录 shell 与非交互式 shell 还可能读取其他文件，因此应先确定 shell 和会话类型，不要假定一个文件能配置所有进程。

要练习环境继承和 shell 配置，可以尝试以下动手实验：

1. **[在 Linux 中管理 Shell 环境和配置](https://labex.io/zh/labs/comptia-manage-shell-environment-and-configuration-in-linux-590838)** - 练习创建和管理本地变量和环境变量，理解继承，并通过修改 `.bashrc` 文件使配置持久化。
2. **[Linux 中的环境变量](https://labex.io/zh/labs/linux-environment-variables-in-linux-385274)** - 学习环境变量的概念和用法，如何创建、修改和管理它们，以及它们在系统配置中的作用。

## 总结

现在，你可以检查并控制 Bash 传给子进程的环境。

1. 使用恰当的引号展开变量值。
2. 查看已导出值，同时避免泄露秘密。
3. 保留并排列 `PATH` 中的命令目录。
4. 导出 shell 变量供未来子进程继承。
5. 为单条命令覆盖值，而不改变父 shell。
