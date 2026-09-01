---
lesson_id: "tail-command"
course_id: "text-fu"
lang: "zh"
order_index: 9
title: "tail 命令"
description: "学习查看输入末尾，并在文件追加新内容时持续跟踪。"
meta_title: "tail 命令 - Linux 文本工具"
meta_description: "Linux tail 命令初学者指南。学习如何使用 Linux tail 查看文件末尾内容，并使用强大的 tail -f 选项实时监控日志。"
meta_keywords: "tail 命令，Linux tail, tail -f, 查看日志，监控日志，Linux 教程，Linux 初学者，Linux 指南，文件监控"
---

`tail` 命令显示文件或输入流的末尾。它还可以保持运行，并显示追加到文件中的数据，因此很适合观察日志。

## 显示最后十行

没有计数选项时，`tail` 会打印每个指定文件的最后 10 行：

```bash
$ tail application.log
```

如果文件不足 10 行，则打印所有现有行。文件本身不会改变。

:::single-choice{#tail-default-lines} `tail application.log` 默认显示什么？

::option[最多显示文件开头的 10 行。]{#tail-first-ten explanation="选择文件开头是 `head` 的职责；`tail` 从末尾选择。"}
::option[显示命令启动后添加的每一行。]{#tail-follow-only explanation="持续跟踪需要 `-f` 或相关选项；普通 `tail` 会打印一次快照后退出。"}
::option[最多显示文件末尾的 10 行。]{#tail-last-ten .correct explanation="没有计数选项时，`tail` 选择最后十行；不足十行时显示所有行。"}
:::

## 选择行数或字节数

使用 `-n NUMBER` 选择不同数量的末尾行：

```bash
$ tail -n 20 application.log
```

需要末尾字节时，请使用 `-c NUMBER`：

```bash
$ tail -c 100 payload.bin
```

字节模式可能从文本行或编码字符中间开始，因此文本通常使用行模式更清楚。

:::single-choice{#tail-twenty-lines} 哪个命令会显示 `application.log` 的最后 20 行？

::option[`tail -n 20 application.log`]{#tail-twenty-end .correct explanation="`-n` 选择行数，`tail` 会从末尾取出这些行。"}
::option[`head -n 20 application.log`]{#head-twenty-start explanation="它从开头而不是末尾选择 20 行。"}
::option[`tail -c 20 application.log`]{#tail-twenty-bytes explanation="`-c` 选择末尾 20 个字节，并不等同于 20 行。"}
:::

## 从指定行开始

计数前加 `+` 会改变含义：`tail -n +N` 从第 N 行开始，一直打印到末尾。

```bash
$ tail -n +5 report.txt
```

这会跳过前四行，从第 5 行开始。它适合从数据流中去掉已知数量的表头行。

:::single-choice{#tail-start-line-five} 哪个命令会从第 5 行开始打印 `report.txt`？

::option[`tail -n +5 report.txt`]{#tail-from-five .correct explanation="`+5` 会让 `tail` 从第 5 行开始，一直输出到末尾。"}
::option[`tail -n 5 report.txt`]{#tail-final-five explanation="没有加号时，它会选择最后五行，而不考虑它们的绝对行号。"}
::option[`head -n +5 report.txt`]{#head-plus-five explanation="这不是 `tail` 从指定行开始的形式；题目要求应使用 `tail -n +5`。"}
:::

## 跟踪追加的数据

使用 `-f` 时，`tail` 会先打印当前末尾，然后保持运行，继续显示追加的数据：

```bash
$ tail -f application.log
```

按 `Ctrl+C` 中断 `tail` 并返回 shell。跟踪文件只会显示新内容，并不能保证生成日志的应用程序运行正常，也不能保证所有相关事件都写入该文件。

:::single-choice{#tail-follow-file} 哪个命令会显示 `application.log` 当前末尾，并继续等待追加内容？

::option[`tail -f application.log`]{#tail-follow-app .correct explanation="`-f` 会让 `tail` 保持运行，并显示追加到文件中的数据。"}
::option[`tail -n 0 application.log`]{#tail-zero-lines explanation="它最初不打印任何行，而且没有跟踪选项，因此会直接退出。"}
::option[`less application.log`]{#less-log explanation="`less` 提供交互式分页，但这种形式不会保持 `tail` 式的跟踪模式。"}
:::

## 按名称跟踪轮转日志

日志轮转可能重命名旧文件，再在原路径创建新文件。GNU `tail -F` 等同于按名称跟踪并重试，因此能重新打开被替换或暂时缺失的文件：

```bash
$ tail -F application.log
```

需要跟踪当前已打开文件时使用 `-f`；指定名称的日志预计会轮转时使用 `-F`。这些是 GNU 行为，其他实现可能不同。

:::single-choice{#tail-follow-rotated-name} 在 GNU/Linux 上，哪个选项更适合在常见的重命名并重建式日志轮转过程中持续跟踪 `application.log`？

::option[`-n`]{#tail-rotation-lines explanation="`-n` 改变显示行数，不会重试被替换的路径。"}
::option[`-c`]{#tail-rotation-bytes explanation="`-c` 把选择单位改为字节，并不提供感知轮转的跟踪。"}
::option[`-F`]{#tail-follow-name .correct explanation="GNU `-F` 会按名称跟踪并重试，使 `tail` 能重新打开被替换或暂时缺失的日志。"}
:::

未指定文件时，`tail` 会读取 stdin，因此可以选择命令输出的末尾。与 `head` 一样，指定多个文件时默认会显示标识标题。

要练习查看和跟踪文件末尾，可以尝试以下动手实验：

1. **[Linux tail 命令：文件末尾显示](https://labex.io/zh/labs/linux-linux-tail-command-file-end-display-214303)** - 学习使用 `tail` 查看和监控文本文件末尾，包括使用 `-f` 获取实时更新。
2. **[在 Linux 中查看日志和配置文件](https://labex.io/zh/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - 结合 `tail`、`cat` 和 `more` 高效查看日志与配置文件。
3. **[快速威胁检测](https://labex.io/zh/labs/linux-rapid-threat-detection-387930)** - 使用 `tail` 快速提取和分析最近的日志条目。

## 总结

现在，你可以使用 `tail` 检查文件末尾并观察新追加的内容。

1. 默认显示最后十行。
2. 明确选择行数或字节数。
3. 使用 `-n +N` 从编号行开始输出。
4. 使用 `-f` 跟踪追加内容，并用 `Ctrl+C` 停止。
5. 指定名称的日志可能轮转时使用 GNU `-F`。
