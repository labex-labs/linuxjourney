---
lesson_id: "sysv-services"
course_id: "init"
lang: "zh"
order_index: 2
title: "System V 服务"
description: "了解如何通过活动系统支持的包装程序检查和操作旧式 SysV 服务脚本。"
meta_title: "System V 服务 - Init"
meta_description: "了解如何在 Linux 中管理传统的 System V (SysV) 服务。本指南涵盖使用 `service` 命令在 System V init 系统上列出、启动、停止和重启服务。"
meta_keywords: "system v, sysv init, linux 服务，service 命令，管理 linux 服务，启动服务，停止服务，重启服务，linux system v"
---

SysV 服务通常由 `/etc/init.d/` 下的可执行脚本表示。脚本会根据自身实现和发行版约定接受 `start`、`stop`、`restart` 或 `status` 等操作。`service` 命令提供一个包装程序，在更受控的环境中运行指定脚本。

## 发现服务与操作

先列出脚本名称：

```bash
$ ls -1 /etc/init.d/
```

某些实现还提供：

```bash
$ service --status-all
```

其中的方括号标记和退出状态取决于包装程序，脚本也可能报告未知状态。对于单个服务，应检查脚本的用法输出或文档，而不要假定每项操作都存在。

:::single-choice{#sysv-services-wrapper-purpose} `service` 命令通常包装什么？

::option[在每个服务文件上运行的磁盘分区编辑器。]{#sysv-services-partition-editor explanation="服务控制与存储分区无关。"}
::option[由脚本动态添加的内核系统调用。]{#sysv-services-new-syscall explanation="Init 脚本是用户空间进程控制程序。"}
::option[一个指定的 init 脚本及其支持的操作。]{#sysv-services-script-action .correct explanation="包装程序定位旧式服务脚本，并在规范化环境中使用指定操作调用它。"}
:::

## 启动与停止

在真正由 SysV 管理的主机上，常见形式如下：

```bash
$ sudo service SERVICE_NAME start
$ sudo service SERVICE_NAME stop
```

只有识别服务、其依赖项、当前状态和运维影响后，才能替换占位符。从远程会话停止网络、远程访问、存储或身份验证服务，可能让你失去连接或破坏正在进行的工作。

直接形式 `/etc/init.d/SERVICE_NAME ACTION` 可能存在，但如果主机的活动管理器提供兼容功能，应使用面向管理器的命令，让它能够跟踪状态和依赖关系。

:::single-choice{#sysv-services-stop-peanut} 哪个命令请求停止 SysV 服务 `peanut`？

::option[`sudo service stop peanut`]{#sysv-services-stop-first explanation="传统操作数顺序先放服务名称，再放操作。"}
::option[`sudo stop --partition peanut`]{#sysv-services-partition-stop explanation="这不是 SysV 服务包装程序语法。"}
::option[`sudo service peanut stop`]{#sysv-services-peanut-stop .correct explanation="包装程序先接收服务名称，再接收请求的停止操作。"}
:::

## 重新加载、重启与状态

`restart` 通常会停止再启动服务，因而造成中断。`reload` 可以请求服务在不完整重启的情况下重新读取配置，但只有脚本和守护进程支持时才有效。某些脚本还提供 `force-reload`，其后备行为由发行版定义。

任何重新加载或重启前都应验证配置；更改远程访问服务时保留第二条管理连接；之后应通过实际端点和日志验证服务，而不能只看“正在运行”状态。

```bash
$ sudo service SERVICE_NAME status
$ sudo service SERVICE_NAME reload
```

:::single-choice{#sysv-services-reload-versus-restart} 为什么不能假定 `reload` 等同于 `restart`？

::option[Reload 总会关闭整个操作系统。]{#sysv-services-reload-shutdown explanation="这不是服务 reload 操作的通常含义。"}
::option[Restart 只打印配置，绝不改变进程状态。]{#sysv-services-restart-readonly explanation="Restart 通常会停止并启动服务。"}
::option[Reload 由服务定义，可以在不停止进程的情况下重新读取配置。]{#sysv-services-reload-specific .correct explanation="支持情况和语义取决于 init 脚本与守护进程，restart 通常会造成生命周期中断。"}
:::

## 运行时控制与启动启用

现在启动服务并不一定会让它在未来运行级别中自动启动。启动启用状态由运行级别链接表示，并通过 `update-rc.d`、`chkconfig` 或服务管理器兼容生成器等发行版专用工具管理。

在理解发行版依赖元数据和管理工具前，不要手动创建 `S` 和 `K` 链接；手动链接可能被覆盖或顺序错误。

:::single-choice{#sysv-services-start-versus-enable} `service SERVICE start` 一定会让服务在以后启动时自动运行吗？

::option[会；每个 start 操作都会自动创建全部运行级别链接。]{#sysv-services-start-links explanation="包装程序不会普遍改变持久启用状态。"}
::option[不会；运行时状态与运行级别启用是分开的。]{#sysv-services-runtime-separate .correct explanation="启动链接或管理器策略独立于当前启动进程，决定未来是否激活。"}
::option[会；运行中的 PID 会永久存储到启动扇区。]{#sysv-services-pid-boot-sector explanation="PID 是运行时标识符，不是启动启用元数据。"}
:::

## 总结

现在，你可以操作旧式服务，而不会混淆运行时控制和启动策略。

1. 发现实际脚本及其支持的操作。
2. 在包装程序语法中，把服务名称放在操作之前。
3. 验证配置，并检查 reload 或 restart 的实际结果。
4. 通过发行版工具管理未来运行级别的启用状态。
