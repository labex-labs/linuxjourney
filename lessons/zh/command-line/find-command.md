---
lesson_id: "find-command"
course_id: "command-line"
lang: "zh"
order_index: 14
title: "find 命令"
description: "学习按名称、类型、大小和时间搜索目录树，并对确认过的匹配项执行操作。"
meta_title: "find 命令 - 命令行教程"
meta_description: "通过示例学习 Linux 中的 find 命令，按名称、类型、大小、修改时间搜索文件，并对匹配文件执行操作。"
meta_keywords: "linux find 命令, find 命令, linux 查找文件, 按名称查找, 按类型查找, 按大小查找, 按修改时间查找, find exec"
---

系统中有无数文件，定位特定文件可能很困难。`find` 命令通过名称、类型、大小和修改时间等条件搜索目录树。

## 选择搜索位置

基本语法是：

```bash
find [PATH] [EXPRESSION]
```

路径用于选择起点，表达式则筛选起点以下的条目，或对它们执行操作。

例如，要在 `/home` 目录及其所有子目录中查找名为 `puppies.jpg` 的文件，可以使用：

```bash
$ find /home -name puppies.jpg
```

默认会递归搜索。要搜索当前目录树，请用 `.` 作为起始路径。

:::single-choice{#search-current-tree}
哪个命令会在当前目录及其后代中搜索名为 `notes.txt` 的条目？

::option[`find . -name notes.txt`]{#find-current-notes .correct explanation="点号选择当前目录作为起始路径，`-name` 会测试每个条目的基本名称。"}
::option[`find / -name notes.txt`]{#find-root-notes explanation="以 `/` 为起点会从文件系统根目录搜索，范围远大于当前目录树。"}
::option[`find notes.txt .`]{#find-operands-reversed explanation="`find` 要求起始路径位于表达式之前；这个顺序没有表达所需搜索。"}
:::

## 匹配名称和类型

`find` 最常用的功能之一是按文件名搜索。`-name` 选项用于精确匹配名称或使用 shell 风格的模式匹配。

```bash
$ find . -name "*.txt"
```

通配符模式需要加引号，让当前 shell 原样把它传给 `find`。不加引号时，shell 可能在 `find` 启动前就依据当前目录展开 `*.txt`。需要忽略字母大小写时，请使用 `-iname`。

你还可以指定搜索的项目类型。`-type` 选项用于此目的。例如，如果你想查找目录而不是文件，可以使用 `d`。

```bash
$ find /home -type d -name MyFolder
```

这里两个测试都必须为真：条目必须是目录，而且基本名称必须为 `MyFolder`。

:::single-choice{#find-text-regular-files}
哪个命令会查找当前目录下名称以 `.txt` 结尾的普通文件？

::option[`find . -type f -name "*.txt"`]{#text-files .correct explanation="`-type f` 选择普通文件，加引号的 `-name` 模式则由 `find` 对每个条目求值。"}
::option[`find . -type d -name "*.txt"`]{#text-directories explanation="模式引号正确，但 `-type d` 选择的是目录而不是普通文件。"}
::option[`find . -type f -name *.txt`]{#unquoted-text-files explanation="未加引号的通配符可能在 `find` 运行前由当前 shell 展开，改变预期表达式。"}
:::

## 匹配大小和修改时间

你可以按文件大小搜索：

```bash
$ find . -type f -size +10M
$ find . -type f -size -1k
```

大写 `M` 表示 1,048,576 字节为一个单位，小写 `k` 表示 1,024 字节为一个单位。`find` 会先按所选单位向上取整文件大小，再进行数值比较，因此边界行为以这些单位为准。

你也可以按修改时间搜索：

```bash
$ find . -type f -mtime -7
$ find . -type f -mtime +30
```

`-mtime` 测试文件修改后经过的完整 24 小时周期数。`-mtime -7` 匹配小于 7 的值，`-mtime +30` 匹配大于 30 的值；由于使用完整的 24 小时周期，边界并不以日历午夜为准。

:::single-choice{#find-recent-regular-files}
哪个命令会查找 `.` 下修改时间不足七个完整 24 小时周期的普通文件？

::option[`find . -type f -mtime -7`]{#recent-files .correct explanation="`-type f` 选择普通文件，`-mtime -7` 选择不足七个完整 24 小时周期的修改时间。"}
::option[`find . -type f -mtime +7`]{#older-than-seven explanation="加号会选择大于七个单位的时间，查找的是较旧而不是较新的文件。"}
::option[`find . -type d -mtime -7`]{#recent-directories explanation="时间测试符合较新条件，但 `-type d` 会把结果限制为目录而非普通文件。"}
:::

## 打印匹配项并执行操作

默认情况下，`find` 会打印匹配的路径。你可以添加操作，如 `-print`、`-delete` 或 `-exec`。

显式打印匹配项：

```bash
$ find . -name "*.log" -print
```

对每个匹配项运行 `ls -l`：

```bash
$ find . -name "*.log" -exec ls -l {} \;
```

在 `\;` 形式中，每次调用命令时，`{}` 会替换为一个匹配路径。分号终止 `-exec` 操作；对它进行转义，是为了让 shell 把它传给 `find`。

使用 `-delete` 或会修改文件的 `-exec` 等破坏性操作前，应对相同测试运行 `-print`，并检查每项结果。更窄的起始路径和 `-maxdepth N` 也能限制搜索范围。

:::single-choice{#verify-before-delete}
你正在编写一个以后可能删除旧 `.log` 文件的 `find` 命令。首先应该做什么？

::option[立即添加 `-delete`，再检查哪些文件消失了。]{#delete-first explanation="删除不是安全预览，也没有内置撤销；添加删除操作前应验证完整匹配集合。"}
::option[用相同测试运行 `-print`，检查每个匹配项。]{#print-first .correct explanation="只读列表可以在加入破坏性操作前验证起始路径和测试条件。"}
::option[从 `/` 开始搜索，确保不会漏掉任何日志。]{#root-first explanation="从 `/` 开始会扩大范围，可能包含无关或受保护路径；应选择足够用的最窄起点。"}
:::

:::single-choice{#run-ls-for-each-match}
在 `find . -name "*.log" -exec ls -l {} \;` 中，`{}` 表示什么？

::option[提供给 `ls -l` 的当前匹配路径。]{#match-placeholder .correct explanation="对于这种 `-exec` 形式，`find` 会在调用 `ls -l` 前用当前匹配项替换 `{}`。"}
::option[启动 `find` 命令时所在的目录。]{#starting-placeholder explanation="起始目录是命令开头附近的点号；花括号在 `-exec` 中承担不同职责。"}
::option[结束 `-exec` 表达式的分号。]{#terminator-placeholder explanation="转义的分号会终止 `-exec` 操作；花括号是路径占位符。"}
:::

出现权限拒绝消息，通常意味着当前账户无法搜索目录树的一部分。应优先选择更窄且相关的起始路径；在尚未理解并明确需要扩展访问范围前，不要提升权限。

要练习构建搜索表达式，可以尝试以下动手实验：

1. **[Linux find 命令：文件搜索](https://labex.io/zh/labs/linux-linux-find-command-file-searching-219191)** - 本实验介绍 `find` 命令，这是一款功能强大的工具，用于根据各种条件搜索和定位文件及目录。你将练习使用 `find` 定位特定文件。
2. **[发现关键系统资源](https://labex.io/zh/labs/linux-discover-critical-system-resources-388032)** - 学习定位文件和可执行文件的基本 Linux 命令，包括 `find`。你将练习高效浏览文件系统并发现关键系统资源。

## 总结

现在，你可以构建范围明确的 `find` 表达式，并在执行操作前验证结果。

1. 选择满足需要的最窄起始路径。
2. 给名称模式加引号，并与类型测试组合。
3. 按大小或完整的 24 小时修改周期筛选。
4. 在适当时限制递归深度。
5. 执行破坏性操作前打印并检查匹配项。
