---
lesson_id: "alias-command"
course_id: "command-line"
lang: "zh"
order_index: 18
title: "alias 命令"
description: "学习在 Bash 中创建、检查、持久保存、绕过和删除命令别名。"
meta_title: "alias - 命令行别名"
meta_description: "通过示例学习 Linux alias 命令，包括创建临时别名、在 .bashrc 中保存别名、列出别名以及使用 unalias 删除别名的方法。"
meta_keywords: "linux alias 命令, alias 命令, bash alias, .bashrc alias, unalias 命令, linux 命令快捷方式, shell alias"
---

别名会让交互式 shell 在执行命令行前，把一个命令单词替换为另一段字符串。它可以缩短常用命令，也可以提供一组偏好的选项。

## 在当前 shell 中创建别名

要创建一个仅在当前终端会话中有效的临时别名，只需指定一个名称并将其设置为命令字符串。

例如，创建一个名为 `ll` 的别名，代表 `ls -la`：

```bash
$ alias ll='ls -la'
```

定义后，输入 `ll` 作为命令就会展开为 `ls -la`。引号会在定义别名时把替换内容组合在一起。别名最适合简单的命令前缀替换；需要以更结构化的方式处理参数时，应使用 shell 函数。

:::single-choice{#define-ll-alias}
哪个 Bash 命令会在当前 shell 中把 `ll` 定义为 `ls -la` 的别名？

::option[`alias ll = 'ls -la'`]{#alias-spaces explanation="`=` 周围的空格会把定义拆成多个 shell 单词，Bash 因此收不到有效的别名赋值。"}
::option[`alias ll='ls -la'`]{#alias-ll .correct explanation="它使用必需的 `NAME=REPLACEMENT` 形式，并给含空格的替换内容加上引号。"}
::option[`unalias ll='ls -la'`]{#unalias-definition explanation="`unalias` 用于删除现有别名名称，而不是创建替换内容。"}
:::

## 在未来的 Bash 会话中加载别名

在提示符处定义的别名只属于当前 shell，shell 退出后便会消失。交互式非登录 Bash 会话通常读取 `~/.bashrc`，因此这里是保存个人 Bash 别名的常用位置：

```bash
alias ll='ls -la'
```

要使更改生效，你必须关闭并重新打开终端，或者使用 `source` 命令让 shell 重新加载配置文件：

```bash
$ source ~/.bashrc
```

shell 启动行为可能因 shell、登录模式和发行版配置而异。例如，Zsh 用户通常应使用 Zsh 配置，而不是 Bash 的 `.bashrc`。

:::single-choice{#persist-bash-alias}
个人别名通常应定义在哪里，才能被未来的交互式非登录 Bash 会话加载？

::option[用户的 `~/.bashrc` 文件中。]{#bashrc-alias .correct explanation="交互式非登录 Bash 通常会读取 `~/.bashrc`，因此这里是个人 Bash 别名的惯用位置。"}
::option[被设置别名的命令所用的可执行文件中。]{#edit-executable explanation="修改已安装可执行文件与 shell 别名展开无关，而且可能破坏由软件包管理的系统文件。"}
::option[当前终端的滚动回看历史中。]{#terminal-scrollback explanation="滚动回看只记录显示过的文字；Bash 不会把它作为启动配置执行。"}
:::

## 检查别名和名称解析

运行不带参数的 `alias` 命令可以列出当前 shell 中的别名。

```bash
$ alias
alias ll='ls -la'
alias grep='grep --color=auto'
```

使用 `type` 命令可以查看输入某个命令时实际执行的内容：

```bash
$ type ll
ll is aliased to 'ls -la'
```

:::single-choice{#inspect-command-alias}
哪个命令会显示 Bash 当前把 `ll` 解析为别名、函数、内建命令还是可执行文件？

::option[`file ll`]{#file-ll explanation="`file` 对文件系统路径分类；别名保存在 shell 状态中，不需要对应名为 `ll` 的文件。"}
::option[`type ll`]{#type-ll .correct explanation="`type` 内建命令会报告当前 Bash 会话如何解析名称 `ll`。"}
::option[`whatis ll`]{#whatis-ll explanation="`whatis` 查询手册页描述；个人别名通常没有手册数据库条目。"}
:::

## 绕过和删除别名

要在一条命令行中绕过别名，可以在命令名前加反斜杠，或把它放在 Bash 的 `command` 内建命令之后：

```bash
$ \ls
$ command ls
```

当你需要底层命令的正常行为时，这很有用。别名应保持简短、可预测，不要在熟悉的命令名背后隐藏意外或破坏性行为。

:::single-choice{#bypass-ls-alias}
当前 Bash 会话有一个名为 `ls` 的别名。哪个命令会在一次调用中绕过它？

::option[`alias ls`]{#show-ls-alias explanation="这会打印 `ls` 别名的定义，并不会调用底层命令。"}
::option[`command ls`]{#command-ls .correct explanation="由于 `command` 是命令单词，Bash 不会把其后的 `ls` 展开为别名，而会进行正常命令解析。"}
::option[`source ls`]{#source-ls explanation="`source` 会在当前 shell 中把文件作为 shell 代码读取，不是安全或合适的绕过别名方式。"}
:::

使用 `unalias` 从当前 shell 中删除别名：

```bash
$ unalias ll
```

如果定义仍留在 `~/.bashrc` 中，未来的 shell 还会重新创建它。想永久删除别名时，也要删除或修改相应配置行。

:::single-choice{#remove-current-alias}
哪个命令会从当前 Bash 会话中删除别名 `ll`？

::option[`unalias ll`]{#unalias-ll .correct explanation="`unalias` 会从当前 shell 的别名表中删除指定别名。"}
::option[`alias ll=''`]{#empty-ll explanation="这会把别名替换为空展开，而不是删除它的定义。"}
::option[`command ll`]{#command-ll explanation="`command` 可以在当前命令行中绕过别名展开，但不会从 shell 状态中删除别名。"}
:::

## 总结

现在，你可以用简单且可检查的别名定制 Bash。

1. 使用正确引号定义临时别名。
2. 让未来会话从 `~/.bashrc` 加载个人别名。
3. 检查别名和命令解析结果。
4. 在一次调用中绕过别名。
5. 按需同时删除活动定义和已保存定义。
