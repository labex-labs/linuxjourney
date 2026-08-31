---
lesson_id: "sysv-overview"
course_id: "init"
lang: "zh"
order_index: 1
title: "System V 概述"
description: "了解传统 System V init 如何使用运行级别和有序服务脚本链接。"
meta_title: "System V 概述 - Init"
meta_description: "探索传统的 System V 初始化系统，也称为 SysV 或 init v。本指南涵盖 systemv 如何管理进程、其顺序启动以及运行级别在 Linux 中的作用。了解经典 initv 进程的基础知识。"
meta_keywords: "System V, systemv, SysV init, systemv init, init v, initv, Linux 运行级别，init 系统，进程管理，Linux 教程"
---

System V init 通常称为 SysV init 或 sysvinit，是一种传统的 PID 1 和服务启动设计。它在旧系统及兼容脚本中仍然重要，但存在 SysV 风格文件并不能证明正在运行的 PID 1 就是 sysvinit。

## 识别活动 Init 系统

检查正在运行的 PID 1：

```bash
$ ps -p 1 -o pid,comm,args=
$ readlink /proc/1/exe
```

`/etc/inittab` 文件或 `/etc/init.d/` 目录只能作为辅助证据。Systemd 和其他 init 系统可能为兼容性保留这些文件，容器显示的 PID 命名空间也可能与主机不同。

:::single-choice{#sysv-overview-detection}
什么是 sysvinit 正在活动的最有力证据？

::option[正在运行的 PID 1 可执行文件是 sysvinit 或其 init 程序。]{#sysv-overview-live-pid-one .correct explanation="检查正在运行的第一个进程，比从兼容文件推断更直接。"}
::option[存在 `/etc/init.d/` 目录。]{#sysv-overview-init-d-only explanation="其他 init 系统通常也会保留 SysV 脚本或包装程序。"}
::option[某个软件包描述中包含 service 一词。]{#sysv-overview-package-word explanation="软件包文本不能标识当前充当 PID 1 的进程。"}
:::

## 运行级别

运行级别是一种以数字命名的运行模式。SysV 配置传统上使用 `0` 到 `6` 以及特殊级别，但其含义属于发行版策略，并非通用定律。常见约定包括：

- `0`：关机或断电转换
- `1` 或 `S`：单用户或救援模式
- `2` 到 `5`：由发行版定义的多用户模式
- `6`：重启转换

Debian 家族系统历史上对级别 2–5 采用相似处理，Red Hat 家族约定则区分文本和图形模式。应检查实际主机的 `/etc/inittab`、init 文档和运行级别目录。

:::single-choice{#sysv-overview-shutdown-runlevel}
在许多 SysV 系统上，哪个运行级别传统上请求关机或断电？

::option[`3`]{#sysv-overview-runlevel-three explanation="这通常是多用户运行模式，而不是关机。"}
::option[`0`]{#sysv-overview-runlevel-zero .correct explanation="级别零传统上是关机转换，但仍以本地 init 策略为准。"}
::option[`6`]{#sysv-overview-runlevel-six explanation="级别六传统上请求重启。"}
:::

## Init 脚本与运行级别链接

服务脚本通常位于 `/etc/init.d/` 下。`/etc/rc2.d/` 或 `/etc/rc.d/rc2.d/` 等运行级别目录包含链接，其名称编码转换动作与顺序：

- `SNNname` 链接请求启动操作。
- `KNNname` 链接请求停止操作。
- `NN` 提供该次转换中链接的字典序顺序。

具体算法和目录会有差异。依赖关系也可以在脚本头中表达，并由发行版工具处理，某些实现还会并行运行工作。不能把 SysV 简化为所有服务一定严格一次只启动一个。

:::single-choice{#sysv-overview-start-link}
进入运行级别时，`S20networking` 链接传统上请求什么？

::option[直接向每个网络进程发送信号 20。]{#sysv-overview-signal-twenty explanation="数字是排序元数据，而不是信号编号。"}
::option[保存二十份网络配置备份。]{#sysv-overview-twenty-backups explanation="运行级别链接不提供备份保留功能。"}
::option[按照 `S` 的顺序，以 start 操作运行链接的服务脚本。]{#sysv-overview-start-action .correct explanation="前缀区分启动链接，数字则参与决定顺序。"}
:::

## 在运行级别之间转换

Init 更改运行级别时，发行版的 rc 机制会停止新模式不再需要的服务，并启动新模式要求的服务。脚本应具有足够的幂等性，能够处理重复的状态或转换操作，并返回有意义的状态。

请求运行级别 0 或 6 是影响整个系统可用性的破坏性操作。应使用系统的关机接口、通知用户、保存活动工作并验证远程控制台访问，而不要随意调用原始 init 转换。

:::single-choice{#sysv-overview-runlevel-six-meaning}
运行级别 `6` 传统上请求什么？

::option[创建六个额外用户账户。]{#sysv-overview-six-users explanation="运行级别描述运行模式，而不是账户数量。"}
::option[系统重启转换。]{#sysv-overview-reboot .correct explanation="经典 SysV 策略把级别六保留给停止服务并重新启动系统。"}
::option[永久以只读方式挂载所有文件系统。]{#sysv-overview-six-readonly explanation="这不是运行级别六的传统用途。"}
:::

## 兼容性的局限

在 systemd 主机上，SysV 脚本可以包装成生成的单元，但 systemd 的依赖、超时、日志和状态语义仍然适用。直接运行旧脚本可能绕过服务管理器的跟踪。应识别活动管理器，并尽可能使用其原生接口。

:::single-choice{#sysv-overview-compatibility-script}
为什么 systemd 主机上的 SysV 风格脚本通常应该通过服务管理器调用？

::option[直接执行可能绕过依赖与状态跟踪。]{#sysv-overview-manager-tracking .correct explanation="管理器需要协调进程所有权、顺序、超时和状态。"}
::option[Shell 脚本无法在 systemd 系统上执行。]{#sysv-overview-scripts-impossible explanation="脚本可以执行，但绕过监管可能产生不一致状态。"}
::option[Systemd 会把每个服务脚本转换成内核模块。]{#sysv-overview-script-module explanation="兼容单元仍属于用户空间服务管理。"}
:::

## 总结

现在，你可以解读传统 SysV 布局，而不会假定它正在活动。

1. 选择 init 命令前识别正在运行的 PID 1。
2. 把运行级别含义视为发行版定义的约定。
3. 解读运行级别链接中的 `S`、`K` 与数字顺序。
4. 对级别 0 和 6 使用受控关机流程。
5. 存在兼容脚本时，仍应尊重活动管理器。
