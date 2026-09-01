---
lesson_id: "process-niceness"
course_id: "processes"
lang: "zh"
order_index: 8
title: "进程的 Nice 值"
description: "了解 Nice 值如何影响普通 Linux 进程的 CPU 调度权重。"
meta_title: "进程的 Nice 值 - 进程管理"
meta_description: "了解 Linux 中的进程优先级（Nice 值）及其如何影响进程调度。本教程解释了 Linux 进程的 Nice 值，并介绍使用 nice 和 renice 命令来管理 CPU 调度和提高系统性能。"
meta_keywords: "Linux Nice 值，Linux 进程优先级，Linux Nice 值是什么，Linux 进程 Nice 值，进程优先级，nice 命令，renice 命令，CPU 调度"
---

Linux 可以在不同的 CPU 核心上同时执行线程，也可以在可运行线程数超过单个核心承载能力时，让这些线程分时使用该核心。调度器会根据调度策略、优先级、CPU 亲和性和工作负载作出选择。对于普通的分时调度策略，Nice 值是其中一项输入。

## 理解 Nice 值

传统的 Nice 值范围是 `-20` 到 `19`：

- 数值越低，任务相对于同类任务拥有的调度权重越大。
- 数值越高，任务越“友好”，获得的相对权重也越小。
- 默认值通常是 `0`。

Nice 值不会预留一定比例的 CPU，也不保证任务立即执行。当多个相近的可运行任务争用 CPU 时间时，它的作用最明显。实时调度策略、cgroup、CPU 亲和性、I/O 等待以及其他控制机制都可能对实际表现产生更大的影响。

:::single-choice{#process-niceness-lower-value} 在相同的普通调度策略下，哪个 Nice 值会获得更大的相对 CPU 权重？

::option[`10`]{#process-niceness-value-ten explanation="正数值更“友好”，其权重通常小于零或负数值。"}
::option[`19`]{#process-niceness-value-nineteen explanation="这是传统范围中最“友好”的一端，相对权重很小。"}
::option[`-5`]{#process-niceness-value-minus-five .correct explanation="对于可比较的普通任务，Nice 值越低，相对权重越大。"}
:::

## 查看 Nice 值

在 `top` 中，`NI` 列显示 Nice 值。也可以用 `ps` 明确请求该字段：

```bash
$ ps -o pid,ni,pri,stat,cmd -p 3245
```

`NI` 是用户可见的 Nice 值。`PRI` 或类似的列可能是由调度器派生出的优先级，而且其取值尺度会随工具和调度类别而变化，因此不要假定这两列可以互换。

:::single-choice{#process-niceness-top-column} `top` 中通常由哪一列显示 Nice 值？

::option[`PID`]{#process-niceness-column-pid explanation="`PID` 用于标识进程，不显示其调度调整值。"}
::option[`TTY`]{#process-niceness-column-tty explanation="`TTY` 表示进程与控制终端的关联。"}
::option[`NI`]{#process-niceness-column-ni .correct explanation="`NI` 是进程或线程 Nice 值的常用缩写。"}
:::

## 使用 `nice` 启动命令

使用 `nice` 可以按调整后的 Nice 值启动新命令：

```bash
$ nice -n 5 long-computation
```

具体能够请求的调整幅度以及所接受的语法，应查看本机手册。非特权用户通常可以增大 Nice 值，让命令变得更加“友好”。如果要降低 Nice 值，从而获得更有利的调度权重，则需要相应权限或已配置的资源限制。

:::single-choice{#process-niceness-nice-command} `nice -n 5 long-computation` 会执行什么操作？

::option[在权限允许时，以 Nice 值 5 启动该命令。]{#process-niceness-start-five .correct explanation="`nice` 会使用请求的调度调整值启动一个新命令。"}
::option[把 PID 5 的进程改为最低的 Nice 值。]{#process-niceness-pid-five explanation="`-n` 后面的操作数是 Nice 值，而不是目标 PID。"}
::option[保证该命令恰好获得一个 CPU 的百分之五。]{#process-niceness-five-percent explanation="Nice 值表示相对权重，并不预留固定比例的 CPU。"}
:::

## 使用 `renice` 更改现有进程

对于已经运行的进程，应使用 `renice`：

```bash
$ renice -n 10 -p 3245
```

这条命令请求把 PID `3245` 的 Nice 值设为 `10`。由于 PID 可以被重复使用，应先核实目标，再确认最终生效的值。所需权限取决于进程所有权、特权、资源限制和系统策略。通常可以增大自己所拥有进程的 Nice 值；若想撤销这一更改，没有相应权限时可能无法做到。

:::single-choice{#process-niceness-renice-purpose} 哪个工具用于更改现有进程的 Nice 值？

::option[`nice`]{#process-niceness-tool-nice explanation="`nice` 主要用于以调整后的值启动新命令。"}
::option[`kill`]{#process-niceness-tool-kill explanation="`kill` 用于发送信号，并不是常规的 Nice 值修改工具。"}
::option[`renice`]{#process-niceness-tool-renice .correct explanation="`renice` 可以根据选项指定现有 PID、进程组或用户。"}
:::

[管理和监控 Linux 进程](https://labex.io/zh/labs/comptia-manage-and-monitor-linux-processes-590864)实验提供了查看和修改 Nice 值的受控环境。应比较相互争用 CPU 的计算密集型任务，而不要期待在系统空闲时看到明显差异。

## 总结

现在，你可以理解和调整进程的 Nice 值，而不会把它误认为 CPU 使用保证。

1. Nice 值越低，表示相对调度权重越大。
2. 应将 `NI` 与派生的优先级字段分开理解。
3. 启动命令时使用 `nice`。
4. 对已经存在且核实过的进程使用 `renice`。
