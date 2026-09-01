---
lesson_id: "systemd-goals"
course_id: "init"
lang: "zh"
order_index: 6
title: "systemd 目标与服务管理"
description: "学习如何检查、覆盖、验证、启动、启用 systemd 服务单元并排查故障。"
meta_title: "systemd 目标与服务管理 - 初始化系统"
meta_description: "探索 systemd 目标，并学习使用常用 systemctl 命令管理 Linux 服务。本指南介绍 systemd 单元文件基础、如何启动、停止和启用服务，以及如何查看其状态。"
meta_keywords: "systemd, systemctl, Linux 服务, 单元文件, systemd 目标, 服务管理, systemd 单元, 入门, 教程, 指南, Linux 命令"
---

`systemctl` 向 systemd 管理器发送请求。本课重点介绍系统服务单元。改变状态之前，应确认确切的单元名称、管理器作用域、依赖关系和操作影响。

## 阅读服务单元

下面是一个用于说明的最小单元：

```ini
[Unit]
Description=Example worker
Wants=network-online.target
After=network-online.target

[Service]
Type=exec
ExecStart=/usr/local/bin/example-worker
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

- `[Unit]` 包含描述和依赖关系。
- `[Service]` 定义进程生命周期和服务特有的行为。
- `[Install]` 告诉启用命令要创建哪些别名或依赖链接；它不会自动成为活动的运行时依赖关系。

默认情况下，`ExecStart=` 不会交给 shell 执行。除非有意显式调用 shell，否则 shell 管道、重定向、变量和引号的行为与交互式命令行不同。

:::single-choice{#systemd-goals-install-section} `WantedBy=` 等 `[Install]` 指令的主要用途是什么？

::option[保证服务进程已经运行。]{#systemd-goals-install-running explanation="运行时激活需要 start 请求或其他触发依赖关系。"}
::option[描述启用单元时创建的链接或关系。]{#systemd-goals-enable-links .correct explanation="启用操作会解释安装元数据，而安装元数据与当前进程状态相互独立。"}
::option[通过用户的交互式 shell 执行每条命令。]{#systemd-goals-install-shell explanation="默认情况下，单元命令解析不会使用交互式 shell。"}
:::

## 检查生效的配置

列出已加载的单元：

```bash
$ systemctl list-units --type=service
```

列出已安装的单元文件及其启用状态：

```bash
$ systemctl list-unit-files --type=service
```

两条命令展示的视角不同：单元文件可能已启用但未活动、已活动但未启用，也可能是静态、生成、临时、已屏蔽状态，或没有出现在其中某个列表里。用以下命令检查合并后的厂商配置和插入式配置：

```bash
$ systemctl cat UNIT.service
$ systemctl show UNIT.service
```

:::single-choice{#systemd-goals-list-units-versus-files} `list-unit-files` 会显示哪项并非 `list-units` 主要展示的信息？

::option[只显示 CPU 占用最高的进程。]{#systemd-goals-cpu-processes explanation="进程资源排名不属于这些单元清单命令的用途。"}
::option[已安装单元文件的启用状态。]{#systemd-goals-unit-file-state .correct explanation="它会报告单元文件处于启用、禁用、静态、屏蔽等安装状态。"}
::option[日志中曾写入的每一行内容。]{#systemd-goals-all-journal explanation="查询日志应使用 journalctl。"}
:::

## 创建本地覆盖配置

应使用插入式配置，而不是编辑软件包提供的单元：

```bash
$ sudo systemctl edit UNIT.service
```

在当前实现中，保存后 systemctl 通常会在该编辑流程中要求管理器重新加载配置；但如果通过其他方式修改文件，则应运行：

```bash
$ sudo systemctl daemon-reload
```

`daemon-reload` 会重新读取单元定义并重建依赖关系。它不会重新加载应用程序配置，也不会重启正在运行的服务。适当时可用 `systemd-analyze verify` 验证单元语法和依赖关系，然后检查合并后实际生效的单元。

:::single-choice{#systemd-goals-daemon-reload} `systemctl daemon-reload` 会做什么？

::option[强制每个守护进程重新读取其应用程序配置。]{#systemd-goals-reload-all-apps explanation="应用程序重新加载是服务特有的操作，与管理器配置相互独立。"}
::option[将内核重启到新版本。]{#systemd-goals-reload-kernel explanation="启用新内核需要启动系统，而不是重新加载单元定义。"}
::option[重新加载 systemd 单元定义和依赖信息。]{#systemd-goals-reload-manager .correct explanation="它会更新管理器看到的配置，但本身不会重启服务。"}
:::

## 服务的运行时状态

验证服务配置并保留恢复通道后，可执行：

```bash
$ sudo systemctl start peanut.service
$ sudo systemctl stop peanut.service
$ sudo systemctl restart peanut.service
$ sudo systemctl reload peanut.service
```

只有单元定义或支持重新加载操作时，`reload` 才会成功。`restart` 会中断进程，而且可能无法恢复服务。操作远程访问、网络、存储或身份验证服务时，应保留独立的控制台通道，并在执行前验证配置。

用以下命令检查状态和日志：

```bash
$ systemctl status peanut.service
$ systemctl is-active peanut.service
$ journalctl -u peanut.service -b
```

“活动”只是管理器状态，不能证明每个应用端点都健康。

:::single-choice{#systemd-goals-start-peanut} 哪个命令会立即启动 `peanut.service`，但本身不改变其未来的启用状态？

::option[`sudo systemctl enable peanut.service`]{#systemd-goals-enable-only explanation="enable 会更改安装链接，但除非同时使用 --now，否则不会启动服务。"}
::option[`sudo systemctl start peanut.service`]{#systemd-goals-start-command .correct explanation="start 请求当前运行时激活，它与启用状态相互独立。"}
::option[`sudo systemctl daemon-reload peanut.service`]{#systemd-goals-daemon-reload-unit explanation="daemon-reload 不接受用于激活的单元操作数，也不会启动该服务。"}
:::

## 启用、禁用与屏蔽

用以下命令管理未来的依赖链接：

```bash
$ sudo systemctl enable peanut.service
$ sudo systemctl disable peanut.service
```

除非添加 `--now`，否则 enable 不会启动单元，disable 也不会停止正在运行的单元。静态单元即使没有安装元数据，也仍可作为另一个单元的依赖项被激活。

屏蔽操作会将单元链接到 `/dev/null`，在取消屏蔽前阻止普通激活，包括依赖关系触发的激活。它比禁用更强，并可能破坏依赖该单元的其他单元；使用前应检查反向依赖关系。

:::single-choice{#systemd-goals-disable-runtime} 对已在运行的服务执行不带 `--now` 的 `systemctl disable UNIT` 后，会发生什么？

::option[服务会立即被 `SIGKILL` 终止。]{#systemd-goals-disable-kills explanation="仅执行 disable 不会请求停止当前服务。"}
::option[服务的可执行文件会从文件系统中删除。]{#systemd-goals-disable-deletes explanation="启用操作管理的是链接，而不是程序包文件。"}
::option[服务通常会继续运行，但未来启动所用的启用链接会被移除。]{#systemd-goals-disable-keeps-running .correct explanation="运行时状态和安装状态是两个相互独立的维度。"}
:::

## 验证服务结果

做出更改后，应检查进程状态、最近的日志、监听端点、依赖单元和应用程序健康状况；如果修改了启动时的启用状态，还应通过一次受控重启检查其行为。可根据情况使用 `systemctl is-failed`、`systemctl list-dependencies` 和应用程序自身的检查工具。

## 总结

现在，你可以在不混淆配置、运行时状态和启用状态的情况下管理 systemd 服务。

1. 按照各自不同的职责理解 `[Unit]`、`[Service]` 和 `[Install]`。
2. 对比已加载单元的状态与已安装单元文件的状态。
3. 使用插入式配置，并在外部文件发生变化后重新加载管理器。
4. 只有在评估影响后，才启动、停止、重新加载或重启服务。
5. 将启用、禁用和屏蔽视为不同的持久性控制手段。
