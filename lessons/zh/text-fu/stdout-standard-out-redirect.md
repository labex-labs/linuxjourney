---
lesson_id: "stdout-standard-out-redirect"
course_id: "text-fu"
lang: "zh"
order_index: 1
title: "标准输出 (stdout)"
description: "了解标准输出如何流向终端，以及 Bash 如何把它重定向到文件。"
meta_title: "标准输出 (stdout) - Text-Fu"
meta_description: "通过掌握标准输出 (stdout) 和 I/O 重定向，开始您的 Linux 学习之旅。本课程介绍如何使用 > 和 >> 运算符将命令输出重定向到文件，这是任何 Linux 用户的基础技能。"
meta_keywords: "Linux, 学习 Linux, stdout, I/O 重定向，标准输出，重定向输出，bash, shell 脚本，Linux 命令，Linux 教程"
---

程序通过输入/输出流通信。标准输出简称 **stdout**，是程序通常用来传递正常结果的数据流。在终端中，shell 最初会把这条流连接到终端显示区域。

## 写入标准输出

```bash
$ echo Hello World
Hello World
```

stdout 的文件描述符是 `1`；重定向多条流时，这个数字会很有用。程序还可以拥有标准输入 stdin 和标准错误 stderr，后续课程会介绍它们。

:::single-choice{#stdout-default-destination} 没有重定向时，交互式终端中的 `echo Hello World` 通常会把正常输出发送到哪里？

::option[发送到当前目录中名为 `stdout` 的文件。]{#stdout-file explanation="标准输出是一条流，并不会自动创建名为 `stdout` 的文件；只有重定向时才会使用文件。"}
::option[通过标准输出发送到终端。]{#stdout-terminal .correct explanation="shell 通常会把命令的 stdout 连接到终端，因此 `echo` 的结果会显示在那里。"}
::option[发送到命令的标准输入流。]{#stdout-to-stdin explanation="标准输入把数据送入程序；`echo` 会通过 stdout 向外发送正常结果。"}
:::

## 使用 > 替换文件

Bash 会把 `>` 解释为输出重定向运算符。它打开目标文件，并把命令的 stdout 连接到该文件：

```bash
$ echo Hello World > peanuts.txt
```

文字不再显示在终端，因为 stdout 流向了 `peanuts.txt`。如果文件不存在，shell 会创建它；如果文件已经存在，shell 会在命令写入前清空它，原内容会丢失。

使用 `cat` 检查结果：

```bash
$ cat peanuts.txt
Hello World
```

:::single-choice{#stdout-replace-file} `notes.txt` 已经包含文字。`echo new > notes.txt` 会做什么？

::option[用 `new` 替换文件内容。]{#stdout-replace-existing .correct explanation="对于 `>`，shell 会先清空现有目标，再把 `echo` 的输出写入空文件。"}
::option[把 `new` 添加到现有文字之后。]{#stdout-add-existing explanation="追加需要使用 `>>`；单个 `>` 不会保留目标的原有内容。"}
::option[显示 `new`，但不改变文件。]{#stdout-display-only explanation="重定向会把 stdout 发送到 `notes.txt`，因此正常输出不再留在终端上。"}
:::

因为 shell 会在命令运行前打开目标，所以按 Enter 前必须确认路径。即使命令随后失败，拼错或选错的现有文件也可能已被清空。

## 使用 >> 追加到文件

需要把新的 stdout 添加到文件现有内容之后时，请使用 `>>`：

```bash
$ echo Another line >> peanuts.txt
$ cat peanuts.txt
Hello World
Another line
```

与 `>` 一样，`>>` 也会创建缺失的目标。区别在于打开现有文件的方式：`>>` 会追加，而不是清空。

:::single-choice{#stdout-append-file} 哪个命令会把 `Finished` 添加到 `status.log` 末尾，而不擦除现有内容？

::option[`echo Finished > status.log`]{#stdout-truncate-status explanation="单个 `>` 会在写入前清空现有目标，导致原日志内容丢失。"}
::option[`echo Finished >> status.log`]{#stdout-append-status .correct explanation="`echo` 产生文字，`>>` 再把这段 stdout 追加到目标文件。"}
::option[`cat Finished >> status.log`]{#stdout-cat-filename explanation="这会让 `cat` 读取名为 `Finished` 的文件，并不会产生题目要求的文字。"}
:::

## 重定向由 shell 处理

shell 会识别 `>` 和 `>>`，不把这些运算符作为参数传给程序，而是打开文件并建立数据流连接。命令本身仍照常向 stdout 写入。

因此，相同的重定向语法适用于许多命令：

```bash
$ pwd > current-directory.txt
$ ls -la >> directory-list.txt
```

:::single-choice{#stdout-shell-role} 在 `pwd > current-directory.txt` 中，通常由谁解释 `>`？

::option[`pwd` 命令在收到 `>` 参数后解释。]{#stdout-pwd-redirection explanation="shell 会消化重定向语法，因此 `pwd` 通常不会把 `>` 或目标当作普通参数收到。"}
::option[Bash shell 在启动 `pwd` 前解释。]{#stdout-bash-redirection .correct explanation="Bash 会在执行命令前打开目标，并连接文件描述符 1。"}
::option[终端在 `pwd` 已把路径显示到屏幕后解释。]{#stdout-terminal-redirection explanation="数据流会在写出前重定向，因此终端一开始就不会收到这段 stdout。"}
:::

要练习标准流重定向，可以尝试这个动手实验：

1. **[在 Linux 中重定向输入和输出](https://labex.io/zh/labs/comptia-redirecting-input-and-output-in-linux-590840)** - 通过使用 `>`、`>>`、`2>` 等运算符以及 `tee` 命令来操作标准输出 (stdout)、标准错误 (stderr) 和标准输入 (stdin)，练习控制命令的数据流。

## 总结

现在，你可以重定向命令的标准输出，并正确区分替换与追加行为。

1. 知道 stdout 是承载命令正常结果的数据流。
2. 使用 `>` 替换文件内容。
3. 使用 `>>` 保留现有内容并追加。
4. 在 shell 打开目标前确认路径。
