---
lesson_id: "upstart-jobs"
course_id: "init"
lang: "zh"
order_index: 4
title: "Upstart 作业"
description: "学习如何在确认使用旧式 Upstart 的系统上通过 `initctl` 检查和控制作业。"
meta_title: "Upstart 作业 - 初始化系统"
meta_description: "Linux 环境下使用 Upstart 作业管理服务的指南。学习在 Upstart Linux 系统上通过 initctl 工具列出、启动、停止和重启作业。"
meta_keywords: "Upstart 作业, initctl, Upstart Linux, Linux 服务, 系统管理, 初始化系统, Linux 教程"
---

`initctl` 与正在运行的 Upstart 初始化守护进程通信。只有确认相关 PID 命名空间确实运行 Upstart 后，才能使用它；如果当前主机使用 systemd，应改用 systemd 的原生工具。

## 列出并解读作业状态

列出已知的作业及其实例：

```bash
$ initctl list
```

检查单个作业：

```bash
$ initctl status networking
networking start/running
```

Upstart 会同时报告 `start` 或 `stop` 这样的**目标**，以及 `running` 或 `waiting` 这样的当前**状态**。`stop/waiting` 表示该作业没有运行，正在等待启动条件或手动请求；它不一定表示发生了错误。

:::single-choice{#upstart-jobs-stop-waiting} Upstart 状态输出中的 `stop/waiting` 通常表示什么？

::option[作业正在运行，但不消耗 CPU。]{#upstart-jobs-running-idle explanation="正在运行的作业通常会显示 start 目标和 running 状态。"}
::option[作业的目标是停止，且没有进程实例正在运行。]{#upstart-jobs-stopped-waiting .correct explanation="作业定义仍然存在，而 Upstart 正在等待未来的条件或命令。"}
::option[整个操作系统正在等待关机。]{#upstart-jobs-system-poweroff explanation="这组值描述的是该作业实例，而不一定是整个系统的状态。"}
:::

## 启动和停止作业

检查依赖关系和影响后，可执行：

```bash
$ sudo initctl start JOB_NAME
$ sudo initctl stop JOB_NAME
```

作业可以定义由环境变量区分的多个实例。在这种情况下，应提供配置要求的确切变量，并在查询或停止实例时始终带上这些变量。启动网络、存储、身份验证或远程访问作业可能中断当前会话，因此要保留通过控制台恢复的手段。

:::single-choice{#upstart-jobs-start-command} 哪个命令会手动请求启动 `peanuts` 作业？

::option[`sudo initctl start peanuts`]{#upstart-jobs-start-peanuts .correct explanation="start 子命令之后应跟已配置的作业名称以及所有必需的实例变量。"}
::option[`sudo initctl peanuts start`]{#upstart-jobs-name-first explanation="initctl 语法将子命令放在作业名称之前。"}
::option[`sudo systemctl initctl peanuts`]{#upstart-jobs-systemctl-mixed explanation="该命令错误地混用了两套不同的服务管理器接口。"}
:::

## 重启与配置变更

用以下命令请求重启一个正在运行的作业：

```bash
$ sudo initctl restart peanuts
```

在 Upstart 中，编辑作业文件后执行 `restart`，并不总是等同于使用新配置完整执行一次 `stop` 再 `start`：正在运行的作业可能仍以原有配置为准。请先验证修改后的 `.conf` 文件，再按照已安装版本对应的方法让 Upstart 重新加载配置；如果必须让新配置生效，则应遵循文档规定的停止/启动流程。

重启会造成服务中断，而且服务可能无法恢复运行。之后应检查实际服务端点和日志。

:::single-choice{#upstart-jobs-restart-peanuts} 哪个命令会请求重启正在运行的 Upstart 作业 `peanuts`？

::option[`sudo initctl restart peanuts`]{#upstart-jobs-restart-command .correct explanation="restart 子命令通过 Upstart 控制接口操作指定作业。"}
::option[`sudo initctl emit peanuts`]{#upstart-jobs-emit-not-restart explanation="发出事件会影响所有条件匹配的作业，并不是直接的重启请求。"}
::option[`sudo service --status-all peanuts`]{#upstart-jobs-status-all explanation="列出状态不会请求重启作业。"}
:::

## 验证作业配置

安装修改后的作业文件之前，应使用旧发行版提供的验证工具（通常是 `init-checkconf`），并检查所包含的脚本、环境变量、用户/组设置、重新拉起策略以及事件表达式。然后按照相应版本的 `initctl reload-configuration` 流程重新加载定义。

语法验证无法证明路径确实存在、凭据允许执行、事件一定会到达，或进程最终会进入就绪状态。请在具备恢复手段的环境中测试。

:::single-choice{#upstart-jobs-syntax-validation-limit} 作业语法验证无法证明什么？

::option[服务能够成功启动并进入就绪状态。]{#upstart-jobs-runtime-not-proven .correct explanation="运行时路径、权限、依赖关系和事件流都需要通过实际的受控测试来验证。"}
::option[配置文本是否能被解析。]{#upstart-jobs-parse-purpose explanation="解析配置文本正是语法验证的主要目的。"}
::option[是否向验证工具提供了文件。]{#upstart-jobs-file-supplied explanation="工具可以立即报告缺少输入。"}
:::

## 谨慎发出事件

Upstart 可以发出指定名称的事件：

```bash
$ sudo initctl emit EVENT_NAME
```

启动或停止表达式与之匹配的每个作业都可能作出响应。事件并非只发送给某个作业，而且其影响可能通过后续事件层层扩散。发出自定义事件或系统事件前，应检查所有匹配的配置；不要在生产主机上随意重放核心启动事件。

:::single-choice{#upstart-jobs-emit-scope} 运行 `initctl emit EVENT_NAME` 时可能发生什么？

::option[所有与该事件匹配的作业表达式都可能触发状态转换。]{#upstart-jobs-event-matches .correct explanation="事件会广播到 Upstart 的依赖模型中，而不是只发送给某个指定服务。"}
::option[只有名称与事件完全相同的作业才能响应。]{#upstart-jobs-event-name-only explanation="匹配关系由 start on 和 stop on 表达式定义，而不是由作业名称是否相同决定。"}
::option[该事件会作为持久队列消息永久保存。]{#upstart-jobs-event-durable explanation="Upstart 事件是生命周期通知，并不是通用的持久消息队列。"}
:::

## 总结

现在，你可以在明确理解状态和事件作用范围的前提下操作 Upstart 作业。

1. 分别解读 `initctl` 输出中的目标和状态。
2. 评估影响后，启动或停止确切的作业实例。
3. 将重启与作业配置变更视为两个不同的问题。
4. 验证语法后，再测试运行时就绪状态。
5. 发出事件前，检查每一个可能匹配的表达式。
