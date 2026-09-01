---
lesson_id: "upstart-overview"
course_id: "init"
lang: "zh"
order_index: 3
title: "Upstart 概述"
description: "了解旧式 Upstart init 系统如何把事件表达式与作业生命周期目标连接起来。"
meta_title: "Upstart 概述 - Init"
meta_description: "了解 Upstart、其事件驱动模型以及它如何在 Linux 中管理服务。理解 Upstart 作业配置及其作为 init 系统的作用。"
meta_keywords: "Upstart, init 系统，Linux 服务，Ubuntu, SysV, 初学者教程，Linux 指南"
---

Upstart 是由 Canonical 开发的旧式事件驱动 init 与服务管理系统。旧版 Ubuntu 和其他一些发行版曾使用它，但当前 Ubuntu 使用 systemd。只有维护已经确认的旧主机时才应研究 Upstart，不能把它当作现代安装的默认假设。

## 确认旧式 Upstart 主机

检查 PID 1 和活动控制接口：

```bash
$ ps -p 1 -o pid,comm,args=
$ readlink /proc/1/exe
$ initctl version
```

最后一条命令只有在 Upstart 控制服务和客户端存在时才会返回有意义的结果。`/usr/share/upstart` 等目录或 `/etc/init` 下残留文件是较弱证据，因为其他 init 系统接管后，软件包和迁移残留仍可能存在。

:::single-choice{#upstart-overview-active-evidence} 主机确实使用 Upstart 的最有力证据是什么？

::option[某个目录名称包含 `upstart`。]{#upstart-overview-directory-only explanation="已安装文档或残留内容可能保留在使用其他 init 的系统上。"}
::option[系统至少有一个 shell 脚本。]{#upstart-overview-shell-script explanation="Shell 脚本在所有 init 环境中都很常见。"}
::option[PID 1 和活动 `initctl` 接口都表明是 Upstart。]{#upstart-overview-live-interface .correct explanation="运行时进程和控制证据比旧文件是否存在更有力。"}
:::

## 作业与事件

Upstart **作业**描述一个服务或任务，包括其进程命令和生命周期条件。**事件**是带有可选环境变量的命名通知。作业配置可以表达其目标何时应转向启动或停止。

系统作业文件通常位于 `/etc/init/` 下，并以 `.conf` 结尾。例如：

```text
description "Example worker"
start on runlevel [2345]
stop on runlevel [016]
exec /usr/local/sbin/example-worker
```

该示例把运行级别事件用作兼容输入。Upstart 还可以响应文件系统、设备、网络或应用程序定义的事件，具体取决于系统会发出什么。

:::single-choice{#upstart-overview-start-on} Upstart 的 `start on` 段定义什么？

::option[接下来必须编译的内核版本。]{#upstart-overview-kernel-version explanation="作业事件条件不选择内核构建。"}
::option[让作业目标转向启动的事件表达式。]{#upstart-overview-start-condition .correct explanation="表达式满足时，Upstart 会尝试执行配置的作业启动转换。"}
::option[每个作业存储数据的磁盘分区。]{#upstart-overview-partition explanation="存储位置与 Upstart 事件语法无关。"}
:::

## 事件驱动启动

启动期间，Upstart 加载作业定义并接收事件。匹配的 `start on` 或 `stop on` 表达式会更新作业目标；作业转换又可以发出其他事件，解锁后续工作。互不依赖的作业可以并发推进。

该模型避免使用一套硬编码的全局脚本顺序，但事件名称、顺序和条件隐含时可能难以诊断。事件默认不是持久消息队列，因此后来新增作业或更改条件时，不能假定所有过去事件都会重放。

:::single-choice{#upstart-overview-event-chain} 一个 Upstart 作业如何促使另一个作业启动？

::option[在内存中重写另一个作业的可执行二进制文件。]{#upstart-overview-rewrite-binary explanation="协调通过事件完成，而不是修改代码。"}
::option[每个作业总是严格按照文件名顺序启动。]{#upstart-overview-filename-order explanation="Upstart 使用事件表达式，而不是一份按文件名排序的启动列表。"}
::option[其转换可以发出另一个作业所匹配的事件。]{#upstart-overview-emitted-event .correct explanation="事件表达式把原本独立的作业生命周期转换连接起来。"}
:::

## 迁移与兼容

Systemd 可以为某些旧式服务脚本提供有限兼容性，但不会把 Upstart 作业语法作为原生 systemd 单元执行。迁移时，应翻译生命周期条件、环境、重生策略、日志、依赖和就绪语义，而不是机械地重命名文件。

:::single-choice{#upstart-overview-current-ubuntu} 当前标准 Ubuntu 版本使用哪种 init 系统？

::option[每次安装都只使用 Upstart。]{#upstart-overview-current-upstart explanation="这只适用于历史时期的版本和配置。"}
::option[systemd。]{#upstart-overview-current-systemd .correct explanation="Upstart 属于较早 Ubuntu 世代，当前版本使用 systemd 作为 PID 1。"}
::option[完全没有 init 进程。]{#upstart-overview-no-init explanation="完整 Ubuntu 系统仍需要 PID 1 服务管理器。"}
:::

## 总结

现在，你可以把 Upstart 解读为旧式事件与作业模型。

1. 确认活动 PID 1 和控制接口。
2. 区分作业定义与事件通知。
3. 把 `start on` 和 `stop on` 解读为生命周期表达式。
4. 显式迁移语义，而不是重命名配置文件。
