---
lesson_id: "systemd-overview"
course_id: "init"
lang: "zh"
order_index: 5
title: "systemd 概述"
description: "学习 systemd 如何加载单元、解析依赖关系、激活目标，以及管理系统和用户资源。"
meta_title: "systemd 概述 - 初始化系统"
meta_description: "学习 systemd 初始化系统的基础知识。本指南介绍 systemd 如何使用单元和目标管理 Linux 启动过程与系统服务，帮助你理解这一现代 Linux 初始化标准的核心概念。"
meta_keywords: "systemd, system d, 初始化系统, systemd 单元, systemd 目标, Linux 启动过程, Linux 服务, 系统管理, 入门, 教程"
---

systemd 是许多现代 Linux 发行版采用的 PID 1 初始化与服务管理器。systemd 项目还提供日志、设备、登录、网络、时间等组件，但发行版可以自行选择部署哪些部分。

## 确认正在运行的管理器

应检查实时状态，而不是只看已安装的目录是否存在：

```bash
$ ps -p 1 -o pid,comm,args=
$ systemctl is-system-running
```

即使某个系统的 PID 1 是其他程序，`/usr/lib/systemd/` 目录也可能存在；容器也可能提供自己的 PID 命名空间。`systemctl` 还支持用户管理器、远程管理器和容器管理器模式，因此要先确定操作所针对的管理器。

:::single-choice{#systemd-overview-detection}
哪项信息最能直接确认 systemd 是系统初始化管理器？

::option[存在名为 `/usr/lib/systemd` 的目录。]{#systemd-overview-directory explanation="即使 systemd 没有充当 PID 1，系统中仍可能保留相关库和单元文件。"}
::option[某个用户执行过一次名为 `systemctl` 的命令。]{#systemd-overview-command-executed explanation="即使没有可用的系统级 systemd 管理器，客户端程序仍可能存在。"}
::option[主机的 PID 1 是 systemd。]{#systemd-overview-pid-one .correct explanation="正在运行的第一个进程，比已安装文件或软件包名称更能说明实际情况。"}
:::

## 作为受管对象的单元

单元是 systemd 对资源或活动建立的具名模型。常见单元类型包括：

- `.service`：进程和守护进程
- `.socket`：套接字激活
- `.mount` 和 `.automount`：文件系统
- `.timer` 和 `.path`：事件驱动的激活
- `.target`：分组与同步
- `.device`、`.swap`、`.slice` 和 `.scope`：其他受管资源

单元的状态并不总是“正在运行”。挂载单元可以处于已挂载状态，定时器可以处于等待状态，设备可以处于已出现状态，而目标在其依赖关系满足后可以处于活动状态。

:::single-choice{#systemd-overview-group-unit}
哪种单元通常用于将其他单元分组，并提供同步点？

::option[`.socket`]{#systemd-overview-socket explanation="套接字单元公开 IPC 或网络端点，并可激活服务。"}
::option[`.target`]{#systemd-overview-target .correct explanation="目标单元汇集依赖关系，并表示启动或运行过程中的里程碑。"}
::option[`.timer`]{#systemd-overview-timer explanation="定时器单元根据日历时间或单调时间安排激活。"}
:::

## 单元加载路径与覆盖配置

系统单元可以从发行版和管理员配置路径加载，例如：

- `/usr/lib/systemd/system/`：许多发行版用于存放软件包提供的单元
- `/run/systemd/system/`：运行时生成的配置或临时配置
- `/etc/systemd/system/`：持久的本地管理员配置与覆盖配置

具体的厂商路径可能不同。具有更高优先级的本地配置会覆盖同名单元的低优先级文件。与其复制并修改完整的厂商文件，不如使用 `systemctl edit UNIT` 创建插入式覆盖配置，这样软件包更新带来的改动仍然可见。

:::single-choice{#systemd-overview-local-override}
持久的本地系统单元覆盖配置通常应放在哪里？

::option[`/proc/systemd/` 内。]{#systemd-overview-proc-systemd explanation="procfs 是运行时内核接口，不用于存放持久单元配置。"}
::option[`/etc/systemd/system/` 下。]{#systemd-overview-etc-system .correct explanation="管理员配置层的优先级高于软件包提供的厂商单元。"}
::option[磁盘 MBR 的启动代码字节中。]{#systemd-overview-mbr-units explanation="服务单元是用户空间中的配置文件。"}
:::

## 依赖关系与顺序

systemd 根据依赖关系构建事务。`Wants=` 和 `Requires=` 会以不同强度将其他单元纳入事务。`Before=` 和 `After=` 规定两个单元都被调度时的执行顺序；它们本身不会促使另一个单元启动。

`After=network.target` 并不能证明网络连接、DNS 或某个远程端点已经可用。服务必须采用适当的 network-online 集成机制，或自行实现重试和就绪检测。

:::single-choice{#systemd-overview-after-semantics}
`After=other.service` 本身规定了什么？

::option[保证另一个服务的应用端点处于健康状态。]{#systemd-overview-after-health explanation="顺序上的完成与应用程序就绪是两个不同的概念。"}
::option[如果两个单元都在事务中，则规定它们的执行顺序。]{#systemd-overview-after-ordering .correct explanation="还需要 Wants 或 Requires 等独立的依赖项才能将另一个单元纳入事务。"}
::option[以后每次启动时自动启用这两个单元。]{#systemd-overview-after-enable explanation="启用属于安装元数据，并不会由顺序关系隐式产生。"}
:::

## 目标与默认启动事务

`default.target` 通常是指向 `multi-user.target` 或 `graphical.target` 等目标的别名。systemd 会为该目标及其依赖项启动一个事务，在强制执行明确顺序的同时，允许互不相关的工作并发进行。

目标只是在粗略的兼容层面上类似运行级别。多个目标可以同时处于活动状态，也可以创建自定义目标；某个目标处于活动状态，并不表示计算机上的每项服务都健康。

:::single-choice{#systemd-overview-default-target}
`default.target` 通常选择什么？

::option[`mkfs` 应擦除的默认块设备。]{#systemd-overview-default-disk explanation="目标描述单元激活，而不是破坏性的存储设备选择。"}
::option[任何时候都只能有这一个目标处于活动状态。]{#systemd-overview-only-target explanation="目标用于分组，一次启动过程中可以有多个活动目标。"}
::option[系统正常启动所使用的目标事务。]{#systemd-overview-normal-boot .correct explanation="它通常是指向管理员所选多用户或图形启动目标的别名。"}
:::

## 总结

现在，你可以从实时管理器、单元和事务的角度描述 systemd。

1. 通过相关命名空间中的 PID 1 和管理器连接来确认 systemd。
2. 将资源类型与对应的单元后缀相匹配。
3. 将本地覆盖配置置于厂商配置之上。
4. 区分依赖强度、执行顺序和应用程序就绪状态。
5. 将目标视为分组和里程碑，而不是互斥状态。
