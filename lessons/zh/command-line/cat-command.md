---
lesson_id: "cat-command"
course_id: "command-line"
lang: "zh"
order_index: 7
title: "cat 命令"
description: "学习使用 cat 命令安全地显示、连接和重定向文件内容。"
meta_title: "cat 命令 - 命令行教程"
meta_description: "通过示例学习 Linux cat 命令，用于查看文件、连接文件、给行编号、创建文件以及安全使用重定向。"
meta_keywords: "linux cat 命令, cat 命令, 查看文件 linux, 连接文件, cat -n, cat -b, cat 重定向, linux cat"
---

学会识别文件后，下一步是读取它们的内容。`cat` 命令可以显示文件并连接其内容；它的名称是“concatenate”（连接）的缩写。

## 查看文件内容

`cat` 命令最基本的用法是直接在终端显示单个文件的内容。

```bash
$ cat myfile.txt
```

该命令会把整个文件写入标准输出，此处也就是终端。这很适合短文本，但长文件可能会滚动得太快。

:::single-choice{#display-short-file}
哪个命令会在终端中显示 `myfile.txt` 的全部内容？

::option[`file myfile.txt`]{#classify-myfile explanation="`file` 报告文件可能的类型，不会打印其中保存的完整文本。"}
::option[`touch myfile.txt`]{#update-myfile explanation="`touch` 更新时间戳或创建缺失文件，不会显示文件内容。"}
::option[`cat myfile.txt`]{#display-myfile .correct explanation="`cat` 读取 `myfile.txt` 并把内容写入标准输出，此处标准输出就是终端。"}
:::

## 连接文件

顾名思义，`cat` 可以将多个文件连接起来并显示它们的合并输出。它按照提供的顺序读取文件并依次打印。

```bash
$ cat dogfile birdfile
```

该命令会先显示 `dogfile`，再显示 `birdfile`。

要将合并的输出保存到新文件中，可以使用重定向：

```bash
$ cat dogfile birdfile > animals
```

shell 会在运行 `cat` 前创建或清空 `animals`，再把合并后的输出发送到其中。不要把任何输入文件用作这个目标，否则它可能在 `cat` 读取前就被清空。

:::single-choice{#combine-files-in-order}
哪个命令会把 `part1` 后接 `part2` 的内容写入新建或替换的 `whole`？

::option[`cat whole > part1 part2`]{#reverse-redirection explanation="重定向只能有一个目标，其他单词会成为 `cat` 的操作数；这没有表达所需的输入输出顺序。"}
::option[`cat part1 part2 > whole`]{#ordered-inputs .correct explanation="`cat` 按列出的顺序输出两个文件，`>` 再把合并结果重定向到 `whole`。"}
::option[`cat part2 part1 > whole`]{#reverse-inputs explanation="它会把相同的两个输入写入 `whole`，但先读取 `part2`；操作数顺序决定输出顺序。"}
:::

## 把终端输入写入文件

你也可以使用 `cat` 和输出重定向操作符（`>`）来创建新文件。这是直接从终端写入文本到文件的快捷方式。

```bash
$ cat > newfile.txt
```

运行命令后输入所需文本。按 `Ctrl+D` 发送文件结束信号并返回 shell。请注意，如果 `newfile.txt` 已存在，`>` 会清空其原有内容。

如果想追加内容而不是覆盖，使用 `>>`。

```bash
$ cat >> notes.txt
```

:::single-choice{#append-terminal-input}
你想在现有 `notes.txt` 末尾继续输入文本。哪个命令会开始这一操作而不清空文件？

::option[`cat > notes.txt`]{#overwrite-notes explanation="单个 `>` 会在重定向输入前清空目标，导致 `notes.txt` 中的已有文本丢失。"}
::option[`cat >> notes.txt`]{#append-notes .correct explanation="`>>` 以追加方式打开目标，因此 `cat` 读取的文本会添加到现有内容之后。"}
::option[`cat notes.txt > notes.txt`]{#same-input-output explanation="把同一文件同时作为输入和 `>` 目标，可能在 `cat` 读取前就将其清空；这不是安全的追加方式。"}
:::

## 格式化输出

`cat` 命令有多个选项可以改变其行为。

- `-n`：为所有输出行编号，从 1 开始。
- `-b`：只为非空输出行编号。
- `-s`：将多个空行压缩为一行空行。
- `-A`：显示不可打印字符、制表符和行尾符。

示例：

```bash
$ cat -n script.sh
$ cat -b notes.txt
$ cat -s messy.txt
```

:::single-choice{#number-nonempty-lines}
哪个命令只给 `notes.txt` 输出中的非空行编号？

::option[`cat -b notes.txt`]{#number-nonblank .correct explanation="`-b` 只给非空输出行编号，空行不会获得行号。"}
::option[`cat -n notes.txt`]{#number-all-lines explanation="`-n` 会给包括空行在内的每个输出行编号，不符合只处理非空行的要求。"}
::option[`cat -s notes.txt`]{#squeeze-blank-lines explanation="`-s` 会把连续空行压缩成一行，并不添加行号。"}
:::

## 为长文件选择查看器

`cat` 适合短文件。对于长文件，使用 `less`，这样你可以滚动、搜索并退出，而不会让终端内容泛滥。

```bash
$ less /var/log/syslog
```

:::single-choice{#choose-viewer-for-long-file}
哪个命令更适合交互式阅读很长的日志文件？

::option[`less /var/log/syslog`]{#page-through-log .correct explanation="`less` 支持滚动、搜索和可控退出，适合交互式阅读长文件。"}
::option[`cat /var/log/syslog`]{#print-entire-log explanation="`cat` 会一次把整个日志写到终端，长文件可能在你检查前就滚过屏幕。"}
::option[`touch /var/log/syslog`]{#update-log-time explanation="`touch` 会更改时间戳，而且可能需要权限；它不是读取日志的命令。"}
:::

要练习显示和连接文件内容，可以尝试以下动手实验：

1. **[Linux cat 命令：文件连接](https://labex.io/zh/labs/linux-linux-cat-command-file-concatenating-210986)** - 学习 `cat` 命令用于查看、连接和操作文本文件，提升命令行处理文本文件的效率。
2. **[在 Linux 中查看日志和配置文件](https://labex.io/zh/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - 练习使用 `cat` 等命令高效查看和浏览文本文件，包括系统日志和配置文件，以提取关键信息。

## 总结

现在，你可以使用 `cat` 显示和合并文件内容，并安全选择重定向方式。

1. 显示短文件的完整内容。
2. 按指定顺序连接文件。
3. 有意识地替换目标或向目标追加内容。
4. 为输出行编号或简化输出。
5. 在适合交互式阅读时选择 `less`。
