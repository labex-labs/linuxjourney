---
lesson_id: "managing-log-files"
course_id: "logging"
lang: "zh"
order_index: 6
title: "管理日志文件"
description: "学习如何使用 logrotate 配置、测试并验证安全的文本日志轮转。"
meta_title: "管理日志文件 - 日志"
meta_description: "通过这篇面向初学者的 logrotate 指南掌握 Linux 日志管理。了解日志轮转如何节省磁盘空间、如何进行配置，以及如何保持系统日志井然有序。"
meta_keywords: "logrotate, Linux 日志, 日志管理, 日志轮转, Linux 教程, 初学者, 指南, 磁盘空间"
---

无限增长的文本日志可能耗尽文件系统，而过于激进的删除也可能清除运维或合规所需的证据。`logrotate` 会把配置好的大小、时间、压缩、所有权和保留策略应用到文件日志。

## 理解轮转

典型的轮转会重命名活动文件、创建替代文件、按需要求应用程序重新打开文件、压缩较早的版本，并删除超过保留期限的文件。这些步骤取决于配置；轮转不是备份，因为保留副本仍可能被删除、损坏，或随同一台主机一起丢失。

:::single-choice{#logrotate-not-backup} 为什么日志轮转不能替代备份或归档？

::option[轮转文件仍受本地保留策略和主机故障影响。]{#logrotate-local-retention .correct explanation="轮转控制工作日志的各代文件，但不会创建独立的持久副本。"}
::option[轮转只能处理图像文件。]{#logrotate-images explanation="该工具主要用于日志文件。"}
::option[每次轮转都会永久保留所有版本。]{#logrotate-forever explanation="保留规则通常会移除较早版本。"}
:::

## 查找配置

主文件通常是 `/etc/logrotate.conf`，软件包或应用程序配置片段位于 `/etc/logrotate.d/` 下。简化的策略可能如下：

```text
/var/log/example/app.log {
    daily
    rotate 7
    compress
    delaycompress
    missingok
    notifempty
    create 0640 example adm
}
```

该配置要求每天评估，保留七代轮转文件，延迟一代后再压缩，允许日志缺失或为空，并以明确的模式和所有权新建文件。实际是否轮转还取决于记录的状态以及调度器调用 logrotate 的方式。

:::single-choice{#logrotate-rotate-seven} `rotate 7` 指定了什么？

::option[按照策略最多保留七代轮转文件。]{#logrotate-seven-generations .correct explanation="超过配置的保留数量后，较早版本会被移除。"}
::option[每天运行应用程序七次。]{#logrotate-run-seven explanation="该指令控制保留的文件代数，而不是应用程序执行次数。"}
::option[将每个轮转文件的权限设为模式 0007。]{#logrotate-mode-seven explanation="文件模式由 create 等指令控制。"}
:::

## 与写入程序协调

重命名日志后，守护进程仍可能通过保持打开的文件描述符继续写入旧文件。`postrotate` 脚本通常会发送应用程序文档规定的重新加载或重新打开信号。应验证具体应用程序行为，并让脚本作用范围保持最小。

当应用程序无法重新打开日志时，`copytruncate` 会复制文件，然后就地截断原文件。在复制和截断的时间窗口内，写入可能丢失或重复，因此这是一种折中方案，而不是普遍安全的默认选择。

:::single-choice{#logrotate-open-descriptor} 为什么轮转后可能需要向应用程序发送重新打开信号？

::option[它保持打开的描述符可能仍指向已重命名文件。]{#logrotate-descriptor-renamed .correct explanation="重新打开后，后续写入才会使用新创建的活动路径。"}
::option[压缩会自动停止每个应用程序进程。]{#logrotate-compression-stops explanation="压缩本身不会管理写入进程的生命周期。"}
::option[内核禁止创建第二个日志文件。]{#logrotate-kernel-forbids explanation="可以存在多个日志文件；问题在于写入程序打开了哪个 inode。"}
:::

## 激活前测试

使用调试模式检查决策，而不轮转文件：

```bash
$ sudo logrotate -d /etc/logrotate.conf
```

调试输出不能证明真实运行期间权限、脚本、可用空间或应用程序重新打开一定成功。应在受控环境中测试新规则，执行后检查活动文件、轮转版本、所有权、压缩、应用程序输出和 logrotate 状态。`-f` 会强制轮转并改变状态，不要把它误认为试运行。

:::single-choice{#logrotate-debug-mode} `logrotate -d` 提供什么？

::option[永久删除所有过期日志。]{#logrotate-debug-delete explanation="调试模式报告预期决策，而不实际执行轮转。"}
::option[无视策略强制进行生产环境轮转。]{#logrotate-debug-force explanation="强制选项是会改变状态的 -f。"}
::option[不修改日志文件或状态的诊断评估。]{#logrotate-debug-dry .correct explanation="它适合首先检查语法和决策，之后再进行受控的真实验证。"}
:::

## 考虑其他存储

Logrotate 只管理其策略指定的文件。systemd journal 有自己的大小和保留配置，数据库和远程日志服务也有各自的生命周期控制。应监控文件系统容量和日志功能健康状况，以便在写入程序卡住或轮转失败耗尽空间前发现问题。

:::single-choice{#logrotate-journal-retention} logrotate 规则会自动实施 systemd journal 保留策略吗？

::option[不会，journal 存储有自己的配置和限制。]{#logrotate-journal-separate .correct explanation="logrotate 只管理其文件策略选中的路径。"}
::option[会，因为所有日志共享同一个保留引擎。]{#logrotate-all-logs explanation="文件轮转和 journal 保留是两个独立机制。"}
::option[会，但仅在没有文本日志时。]{#logrotate-journal-fallback explanation="是否存在文本日志不会合并这两个保留系统。"}
:::

## 总结

现在，你可以设计并验证文件日志轮转策略，而不会把它误认为归档。

1. 平衡空间、运维和保留要求。
2. 定义代数、压缩、所有权和空文件处理方式。
3. 与保持文件描述符打开的应用程序安全协调。
4. 在受控真实轮转前调试配置。
5. 分别管理 journal 和外部存储的保留策略。
