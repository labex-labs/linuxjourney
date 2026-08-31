---
lesson_id: "head-command"
course_id: "text-fu"
lang: "zh"
order_index: 8
title: "head 命令"
description: "学习从输入开头显示指定数量的行或字节。"
meta_title: "head 命令 - Text-Fu"
meta_description: "一份关于如何使用 head 命令查看文件开头的初学者 Linux 指南。学习如何使用 head -n 选项控制行数，这是任何 Linux 教程中的基本技能。"
meta_keywords: "head 命令，Linux head, 查看文件开头，Linux 教程，Linux 命令，初学者 Linux, head -n, Linux 指南，文本文件，命令行"
---

`head` 命令显示文件或输入流的开头。它适合检查表头、预览结构化数据，或在不打印全部内容的情况下对输出取样。

## 显示前十行

没有计数选项时，`head` 会打印每个指定文件的前 10 行：

```bash
$ head events.log
```

文件不会被修改。如果不足 10 行，则打印所有现有行。

:::single-choice{#head-default-lines}
`head events.log` 默认会打印什么？

::option[最后 10 行；文件较短时打印所有行。]{#head-last-ten explanation="显示输入末尾是 `tail` 的职责；`head` 从开头选择内容。"}
::option[前 10 行；文件较短时打印所有行。]{#head-first-ten .correct explanation="没有计数选项时，`head` 最多选择输入的前十行。"}
::option[无论文件多长，都只打印第一行。]{#head-first-one explanation="只显示一行需要明确指定 `-n 1` 等计数；默认计数是十。"}
:::

## 选择行数

使用 `-n NUMBER` 选择要打印的行数：

```bash
$ head -n 15 events.log
```

GNU `head` 也接受紧凑形式 `-15`，但 `-n 15` 更清楚地表达了选项含义。

:::single-choice{#head-five-lines}
哪个命令会显示 `report.txt` 的前五行？

::option[`head -c 5 report.txt`]{#head-five-bytes explanation="`-c` 统计字节而不是行，可能会停在第一行中间。"}
::option[`head -n 5 report.txt`]{#head-report-five .correct explanation="`-n` 选择行数，`5` 表示前五行。"}
::option[`tail -n 5 report.txt`]{#tail-five-lines explanation="它显示文件最后五行，而不是开头。"}
:::

## 选择字节数

需要字节而不是完整行时，请使用 `-c NUMBER`：

```bash
$ head -c 20 archive.bin
```

这会打印前 20 个字节。输出可能在文本行中间结束；对于多字节文本，甚至可能停在一个编码字符中间。普通文本预览应使用行模式。

:::single-choice{#head-first-bytes}
哪个命令会把 `payload.bin` 的前 100 个字节写入 stdout？

::option[`head -c 100 payload.bin`]{#head-hundred-bytes .correct explanation="`-c` 选择字节数，因此请求的是现有内容中的前 100 个字节。"}
::option[`head -n 100 payload.bin`]{#head-hundred-lines explanation="`-n` 统计行而不是字节，产生的数据可能远多于或少于 100 字节。"}
::option[`cut -c 100 payload.bin`]{#cut-hundredth-character explanation="它会选择每一行中的第 100 个位置，而不是整个输入的前 100 个字节。"}
:::

## 读取 stdin 和多个文件

未提供文件操作数时，`head` 会读取 stdin：

```bash
$ generate-report | head -n 5
```

指定多个文件时，`head` 通常会添加标题，标识每段输出来自哪个文件：

```bash
$ head -n 2 january.txt february.txt
==> january.txt <==
...

==> february.txt <==
...
```

使用 `-q` 抑制标题；使用 `-v` 则会让单个文件也显示标题。

:::single-choice{#head-pipeline-preview}
在 `generate-report | head -n 5` 中，`head` 读取什么？

::option[通过 stdin 读取 `generate-report` 的 stdout。]{#head-pipe-input .correct explanation="管道把生产者的 stdout 连接到 `head` 的 stdin，`head` 再从中选择前五行。"}
::option[当前目录中的前五个文件名。]{#head-directory-names explanation="这里没有目录列举命令；`head` 通过管道收到一条数据流。"}
::option[名为 `generate-report` 的文件中的五个字节。]{#head-producer-file explanation="左侧会作为命令执行，而且 `-n` 统计的是行而非字节。"}
:::

:::single-choice{#head-suppress-filename-headers}
`head` 读取多个文件时，哪个选项会抑制文件名标题？

::option[`-v`]{#head-verbose explanation="`-v` 会要求即使只有一个文件也显示标题，与抑制相反。"}
::option[`-c`]{#head-byte-option explanation="`-c` 会把选择单位改为字节，并不控制文件名标题。"}
::option[`-q`]{#head-quiet .correct explanation="`-q` 即安静选项，会阻止 `head` 打印每个文件的标题标签。"}
:::

要练习预览文件开头，可以尝试以下动手实验：

1. **[Linux head 命令：文件开头显示](https://labex.io/zh/labs/linux-linux-head-command-file-beginning-display-214302)** - 练习使用 `head` 显示文本文件开头，并修改行数。
2. **[在 Linux 中查看日志和配置文件](https://labex.io/zh/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - 练习高效查看和导航系统日志、配置文件等文本文件。
3. **[快速威胁检测](https://labex.io/zh/labs/linux-rapid-threat-detection-387930)** - 结合 `head` 和 `tail` 快速提取并分析日志条目。

## 总结

现在，你可以使用 `head` 预览文件和命令输出的开头。

1. 使用默认的前十行视图。
2. 使用 `-n` 选择行数。
3. 在适当时使用 `-c` 选择字节数。
4. 在管道中读取 stdin。
5. 显示多个文件时控制标题。
