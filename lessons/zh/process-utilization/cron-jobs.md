---
lesson_id: "cron-jobs"
course_id: "process-utilization"
lang: "zh"
order_index: 8
title: "Cron 作业"
description: "学习如何使用 cron 创建、检查、测试并安全运行周期性作业。"
meta_title: "Cron 作业 - 进程资源利用"
meta_description: "了解如何使用 cron 作业在 Linux 中调度任务和自动化脚本。本指南涵盖 crontab 语法、crontab -e 等基本命令以及适合初学者的实用示例。"
meta_keywords: "cron 作业，crontab, 调度任务，Linux 自动化，Linux 命令，Linux 入门，Linux 教程，crontab -e, cron"
---

Cron 会按照周期性计划运行命令，不依赖交互式 shell。自动化既会重复正确行为，也会重复错误，因此在加入计划前，应测试命令、使用明确路径、限制权限，并规划日志记录和失败通知。

## 阅读 Crontab 条目

用户 crontab 条目包含五个时间字段，后跟一条命令：

```cron
30 8 * * * /home/pete/scripts/change_wallpaper
```

从左到右依次是分钟、小时、月中日期、月份和星期。这个示例按照 cron 守护进程适用的时区，每天 08:30 运行。星号表示该字段允许的每一个值。

如果月中日期和星期字段都受到限制，许多 cron 实现会在其中任意一个字段匹配时运行。构建同时使用这两个字段的计划前，应确认本地语义。

:::single-choice{#cron-daily-eight-thirty}
`30 8 * * * command` 何时运行？

::option[连续八小时，每 30 分钟运行一次。]{#cron-every-thirty explanation="各字段表示计划中的位置，而不是持续时间表达式。"}
::option[每天 08:30 运行。]{#cron-eight-thirty .correct explanation="分钟固定为 30，小时固定为 8，三个日期字段则允许每个值。"}
::option[每月第八天的 30:08 运行。]{#cron-invalid-time explanation="小时范围是 0 到 23，而且示例并未限制月中日期。"}
:::

## 管理用户 Crontab

使用以下命令编辑当前用户的 crontab：

```bash
$ crontab -e
```

变更前后都可以列出已安装的条目：

```bash
$ crontab -l
```

`crontab -r` 会删除用户的整个 crontab，而且可能不会打开编辑器。不要用它删除某一行；应编辑 crontab，并验证其余条目仍然存在。

:::single-choice{#cron-list-current-user}
哪个命令列出当前用户已安装的 cron 条目？

::option[`crontab -l`]{#cron-list .correct explanation="列出选项会打印已安装条目以供检查。"}
::option[`crontab -r`]{#cron-remove-all explanation="该选项会删除 crontab，而不是显示内容。"}
::option[`crontab -e`]{#cron-edit explanation="该选项会打开 crontab 进行编辑，而不只是列出内容。"}
:::

## 考虑 Cron 运行环境

Cron 通常只提供有限的环境和非交互式 shell。应使用命令和文件的绝对路径，显式设置必需变量，不要依赖别名、当前终端目录或 shell 启动文件。

把标准输出和错误重定向到受控日志，或使用适合系统的通知机制。用严格权限保护凭据，避免把密钥直接嵌入 crontab 命令。

:::single-choice{#cron-absolute-paths}
为什么 cron 命令应该使用明确路径和环境设置？

::option[Cron 总是在用户当前终端内运行。]{#cron-current-terminal explanation="计划作业独立于交互式会话运行。"}
::option[绝对路径会让所有命令以 root 身份运行。]{#cron-path-root explanation="路径用于选择文件，并不会授予权限。"}
::option[Cron 的环境可能与交互式 shell 不同。]{#cron-limited-environment .correct explanation="明确依赖可以避免因 PATH、目录或启动文件假设导致的失败。"}
:::

## 测试并防止重叠

应使用相同用户，在类似的最小环境中手动运行脚本。让脚本返回有意义的退出状态，并写入带时间戳的结果。安装后，等待一个无害的测试计划或受控运行，再验证实际副作用和日志。

如果一次运行可能超过计划间隔，应让程序能够安全并发，或在可用时使用 `flock` 等锁定机制：

```cron
*/5 * * * * /usr/bin/flock -n /run/user/1000/report.lock /home/pete/bin/report
```

锁文件路径应允许作业用户安全创建，还要确定能否接受跳过运行。Cron 不会自动保证同一时刻只有一个实例运行。

:::single-choice{#cron-overlapping-runs}
作业执行时间超过计划间隔时会有什么风险？

::option[多个实例可能重叠运行并争用资源。]{#cron-overlap .correct explanation="上一个进程仍在运行时，Cron 可以启动下一次执行。"}
::option[五个计划字段会自动增加第六个锁字段。]{#cron-auto-lock explanation="Crontab 语法不会自动增加互斥机制。"}
::option[脚本会永久转换为内核线程。]{#cron-kernel-thread explanation="计划运行命令不会以这种方式改变其进程模型。"}
:::

## 选择合适的调度器

Cron 适合简单的周期性命令。在 systemd 主机上，systemd 定时器可以提供依赖集成、错过时间后的补跑、随机延迟和日志集成。如果作业必须在多台机器上全局只执行一次，应用或集群调度器可能更安全。

:::single-choice{#cron-cluster-exactly-once}
为什么普通的逐主机 cron 可能不适合需要集群全局恰好执行一次的作业？

::option[每个 cron 条目只能包含一个字符。]{#cron-one-character explanation="Crontab 命令可以包含普通命令行。"}
::option[每台主机都可能独立启动自己的副本。]{#cron-each-host .correct explanation="要确保跨主机只执行一次，需要分布式协调机制。"}
::option[Cron 无法执行磁盘上的脚本。]{#cron-no-scripts explanation="运行脚本是 cron 的常见用途。"}
:::

## 总结

现在，你可以在明确计划和运行前提下管理周期性 cron 作业。

1. 按定义顺序阅读五个时间字段。
2. 检查和编辑用户 crontab，而不删除无关作业。
3. 明确定义路径、环境、日志和凭据处理方式。
4. 以作业用户身份测试，并防止意外重叠。
5. 选择符合主机环境和协调需求的调度器。
