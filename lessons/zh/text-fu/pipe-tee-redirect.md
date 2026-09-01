---
lesson_id: "pipe-tee-redirect"
course_id: "text-fu"
lang: "zh"
order_index: 4
title: "管道和 tee"
description: "学习管道如何连接命令，以及 tee 如何保存数据流并继续向后传递。"
meta_title: "管道和 tee - Text-Fu"
meta_description: "探索 Linux 中强大的管道 (pipe) 和 tee 命令。学习如何使用 Linux 管道 tee 组合链接命令，并将输出重定向到屏幕和文件。本指南涵盖如何将管道连接到 tee 以实现高级命令行数据流。"
meta_keywords: "linux 中的 pipe 和 tee 命令，linux 管道 tee, 管道到 tee, Linux 管道，tee 命令，stdout, stdin, 命令行重定向，Linux 教程"
---

管道把小型命令连接起来，让数据无需中间文件即可在命令之间流动。`tee` 命令可以把这段流复制到文件，同时继续向后发送。

## 使用 | 连接命令

让我们从一个产生大量输出的命令开始：

```bash
$ ls -la /etc
```

列表项可能太长，无法在屏幕上显示，难以阅读。虽然您可以将此输出重定向到文件，但更有效的方法是将其直接发送到另一个命令，例如 `less`，以便于查看。

```bash
$ ls -la /etc | less
```

shell 会启动管道中的命令并建立数据流连接。命令可以并发工作：`ls` 还没生成完整列表时，`less` 就能开始读取。

:::single-choice{#pipe-stream-connection} 在 `ls -la /etc | less` 中，`|` 默认连接哪两条流？

::option[`ls` 的 stdin 到 `less` 的 stdout。]{#pipe-reversed-streams explanation="这颠倒了生产者、消费者及两条流；数据从左侧命令的输出流向右侧命令的输入。"}
::option[`ls` 的 stderr 到 `less` 的两条流。]{#pipe-stderr-both explanation="普通管道不连接左侧命令的 stderr，也不会同时指向右侧命令的两条流。"}
::option[`ls` 的 stdout 到 `less` 的 stdin。]{#pipe-stdout-stdin .correct explanation="标准管道把左侧命令的文件描述符 1 连接到右侧命令的文件描述符 0。"}
:::

## 保持 stderr 独立

普通 `|` 只传递 stdout。左侧命令的 stderr 保持原目标，通常是终端：

```bash
$ find /etc -name "*.conf" | less
```

匹配路径通过管道传递，权限诊断信息仍可能直接显示在终端。需要不同处理方式时，请单独重定向 stderr：

```bash
$ find /etc -name "*.conf" 2> find-errors.log | less
```

:::single-choice{#pipe-left-stderr} 在 `find /etc -name "*.conf" | less` 中，如果没有其他重定向，`find` 的 stderr 通常去哪里？

::option[通过与 stdout 相同的管道进入 `less`。]{#pipe-errors-to-less explanation="普通管道只连接 stdout，不会自动把 stderr 合并进去。"}
::option[进入当前目录中名为 `stderr` 的文件。]{#pipe-errors-to-file explanation="命令中没有错误文件重定向，因此 shell 不会创建这样的文件。"}
::option[进入原有目标，通常是终端。]{#pipe-errors-terminal .correct explanation="由于描述符 2 未改变，诊断信息通常仍连接到终端。"}
:::

## 使用 tee 复制数据流

如果您想同时在屏幕上查看输出并将其保存到文件中怎么办？这时 `tee` 命令就派上用场了。`linux 中的 pipe and tee 命令` 是用于日志记录和监控的经典组合。

```bash
$ ls | tee listing.txt
```

这里 `listing.txt` 会收到列表，`tee` 的 stdout 仍连接到终端。默认情况下，`tee` 会像 `>` 一样创建或清空指定文件。

:::single-choice{#tee-display-and-save} 哪个命令会显示 `generate-report` 的输出，同时用相同输出替换 `report.txt`？

::option[`generate-report > report.txt`]{#redirect-report-only explanation="普通输出重定向会写入文件，但不会让副本继续流向终端。"}
::option[`generate-report | tee report.txt`]{#tee-report .correct explanation="`tee` 会把 stdin 复制到 `report.txt` 和自己的 stdout；在这个管道中，stdout 仍是终端。"}
::option[`tee generate-report | report.txt`]{#tee-operands-reversed explanation="这会把 `generate-report` 当作目标文件名，并尝试把 `report.txt` 作为命令执行；生产者应位于左侧。"}
:::

需要追加文件而不是替换时，请使用 `-a`：

```bash
$ date | tee -a activity.log
```

:::single-choice{#tee-append-log} 哪个命令会显示当前日期，并把它追加到 `activity.log`？

::option[`date | tee -a activity.log`]{#tee-append-activity .correct explanation="`-a` 让 `tee` 追加文件，同时继续把输入复制到 stdout。"}
::option[`date | tee activity.log`]{#tee-replace-activity explanation="没有 `-a` 时，`tee` 会替换现有文件，而不是保留早先记录。"}
::option[`date > activity.log`]{#redirect-replace-activity explanation="这会替换文件，也不会把副本送到终端，既不满足追加也不满足显示要求。"}
:::

## 保存中间结果

通过链接这些命令，您可以创建更高级的工作流程。一种常见模式是在较长的命令链中间使用 `pipe to tee`。这允许您在继续处理数据之前保存中间结果。

例如，您可以使用 `linux pipe tee` 组合来在进一步过滤之前查看和保存输出：

```bash
$ ls -la /etc | tee etc-listing.txt | grep "conf"
```

此命令执行三件事：

1. 生成完整的长格式列表。
2. 把完整数据流保存到 `etc-listing.txt`。
3. 把相同数据流发送给 `grep`，由它只打印包含 `conf` 的行。

文件包含 `grep` 过滤前的数据。如果只想把筛选出的行写入文件，应把 `tee` 放在 `grep` 后面。

:::single-choice{#tee-before-filter-result} `produce | tee all.txt | grep error` 成功结束后，`all.txt` 包含什么？

::option[只包含 `grep` 匹配的行。]{#tee-filtered-only explanation="`tee` 位于 `grep` 之前，因此写入的是未过滤输入，而不是下游匹配集合。"}
::option[只包含 `produce` 的 stderr。]{#tee-producer-stderr explanation="普通管道传递 `produce` 的 stdout；其 stderr 并不是 `tee` 的输入。"}
::option[过滤前产生的全部 stdout。]{#tee-complete-intermediate .correct explanation="`tee` 会保存收到的每个字节，再把相同数据流传给 `grep` 过滤。"}
:::

要练习管道和数据流复制，可以尝试以下动手实验：

1. **[在 Linux 中重定向输入和输出](https://labex.io/zh/labs/comptia-redirecting-input-and-output-in-linux-590840)** - 通过操作标准输出 (stdout)、标准错误 (stderr) 和标准输入 (stdin)，并使用 `>`, `>>`, `2>` 和 `tee` 命令等操作符，练习控制命令的数据流。
2. **[序列控制和管道](https://labex.io/zh/labs/linux-sequence-control-and-pipeline-17994)** - 学习控制命令执行序列，利用管道，并利用强大的文本处理工具，如 `cut`、`grep`、`wc`、`sort` 和 `uniq`。
3. **[数据流重定向](https://labex.io/zh/labs/linux-data-stream-redirection-17995)** - 学习 Linux 流重定向的艺术，包括操作标准输入、输出和错误流，组合输出以及利用 `/dev/null`。

## 总结

现在，你可以连接命令，并保留数据流中的指定节点。

1. 把一个命令的 stdout 通过管道送入另一个命令的 stdin。
2. 按需单独重定向 stderr。
3. 使用 `tee` 把输入同时复制到文件和 stdout。
4. 使用 `tee -a` 追加而不是替换文件。
5. 有意识地把 `tee` 放在过滤器之前或之后。
