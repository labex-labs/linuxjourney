---
index: 18
lang: "zh"
title: "alias 命令"
meta_title: "alias - 命令行别名"
meta_description: "通过示例学习 Linux alias 命令，包括创建临时别名、在 .bashrc 中保存别名、列出别名以及使用 unalias 删除别名的方法。"
meta_keywords: "linux alias 命令, alias 命令, bash alias, .bashrc alias, unalias 命令, linux 命令快捷方式, shell alias"
---

## Lesson Content

输入冗长或重复的命令可能很乏味。别名是一种 shell 快捷方式，允许你为命令或命令序列定义自定义名称。

### 创建临时别名

要创建一个仅在当前终端会话中有效的临时别名，只需指定一个名称并将其设置为命令字符串。

例如，创建一个名为 `ll` 的别名，代表 `ls -la`：

```bash
$ alias ll='ls -la'
```

现在，你可以只输入 `ll` 来代替 `ls -la`，它会执行相同的命令。这是一种简单而强大的自定义 shell 的方法。

### 使别名永久生效

临时别名在关闭终端或重启系统后会消失。要使 `command alias in linux` 永久生效，需要将其添加到 shell 的配置文件中。对于 Bash shell，通常是 `~/.bashrc` 文件。

1. 用文本编辑器打开该文件：`nano ~/.bashrc`
2. 将你的别名定义添加到文件中，就像你在命令行中输入的一样：

```bash
alias ll='ls -la'
alias update='sudo apt update && sudo apt upgrade'
```

3. 保存文件并退出编辑器。

要使更改生效，你必须关闭并重新打开终端，或者使用 `source` 命令让 shell 重新加载配置文件：

```bash
$ source ~/.bashrc
```

现在，每次启动新的 Bash 会话时，你的别名都会生效。

### 删除别名

如果你不再需要某个别名，可以使用 `unalias` 命令将其删除。这只会删除当前会话中的别名。

```bash
$ unalias ll
```

要删除永久别名，还必须从 `~/.bashrc` 文件中删除对应的定义。

### 列出现有别名

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

### 有用的别名示例

```bash
$ alias la='ls -la'
$ alias ..='cd ..'
$ alias grep='grep --color=auto'
```

保持别名简短且易于预测。除非非常确定，否则避免用别名替换具有破坏性的命令或产生意外行为。

### 常见问题

**别名在脚本中有效吗？** 通常不行，默认情况下脚本应使用完整命令或函数。

**Bash 别名应该放在哪里？** 交互式 Bash 会话的别名应放在 `~/.bashrc` 中。

**如果别名与真实命令冲突怎么办？** 在交互式 shell 中，别名通常优先。使用 `command name` 或 `\name` 可以绕过别名。

## Exercise

虽然本主题没有特定的实验，但我们推荐探索全面的 [Linux 学习路径](https://labex.io/zh/learn/linux) 来练习相关的 Linux 技能和概念。

## Quiz Question

创建别名使用什么命令？请用小写英文回答。

## Quiz Answer

alias
