---
lesson_id: "system-calls"
course_id: "kernel"
lang: "zh"
order_index: 3
title: "系统调用"
description: "学习用户空间代码如何调用 Linux 内核服务，以及如何使用 `strace` 安全地检查调用。"
meta_title: "系统调用 - 内核"
meta_description: "探索 Linux 系统调用的基础知识。了解用户空间进程如何通过系统调用向内核请求服务、切换模式，以及系统调用表如何工作，并使用 strace 观察实际调用。"
meta_keywords: "Linux 系统调用, 系统调用, syscall 表, 内核模式, 用户模式, strace, Linux 内核, syscall API"
---

系统调用是进入内核的一种规定入口，用户空间代码通过它请求打开文件、映射内存、创建进程或发送网络数据等操作。执行请求前，内核会验证参数、凭据、对象状态和安全策略。

## 库与系统调用 ABI

应用程序通常调用 C 库函数，而不是自行编写与架构相关的进入指令。库包装函数按照系统调用 ABI 准备寄存器和内存，进入内核，再将结果转换成该语言层面的约定。

函数与系统调用并不总是一一对应：

- 一个库函数可以组合多个系统调用
- 有些函数完全在用户空间中运行
- 经过优化的 vDSO 函数可以在不进行完整模式切换的情况下取得某些由内核维护的数据
- 一个系统调用可以支持许多高层 API

:::single-choice{#system-calls-library-wrapper} 典型的 libc 系统调用包装函数会做什么？

::option[准备 ABI 参数、进入内核并转换返回结果。]{#system-calls-wrapper-role .correct explanation="包装函数在普通库接口背后隐藏了与架构相关的调用约定。"}
::option[让应用程序不受限制地访问内核内存。]{#system-calls-wrapper-unrestricted explanation="进入内核的过程仍受控制，内核会验证请求。"}
::option[每次调用函数时重新编译内核。]{#system-calls-wrapper-compile explanation="运行时调用使用的是已经运行的内核。"}
:::

## 进入和退出内核

包装函数将系统调用号和参数放在架构规定的位置，然后执行进入指令，例如 x86-64 上的 `syscall` 或 AArch64 上的 `svc`。处理器切换到配置好的特权入口点，内核随后分派该请求。

操作完成后，内核返回一个值或错误指示。C 库包装函数通常在出错时返回 `-1`，并设置线程局部的 `errno`。其他语言和运行时会公开不同的错误类型。

把每个入口都称为“软件中断”并不能准确描述现代架构；陷阱、快速系统调用指令和监管者调用以不同方式实现相近的受控转换。

:::single-choice{#system-calls-entry-result} 谁负责验证系统调用的参数和授权？

::option[进程启动前的 shell 提示符。]{#system-calls-shell-validates explanation="进程可以不依赖 shell 发出系统调用，而且内核检查始终不可或缺。"}
::option[所请求服务的内核实现。]{#system-calls-kernel-validates .correct explanation="特权处理程序在执行前检查指针、对象状态、凭据和策略。"}
::option[磁盘分区表。]{#system-calls-partition-validates explanation="存储布局元数据不会为任意内核服务授权。"}
:::

## 编号与兼容性

系统调用号和调用约定与架构相关。同一个符号调用在另一种 ABI 上可能具有不同的编号或结构布局。内核版本可以添加系统调用，而稳定的用户空间 ABI 则以保留现有行为为目标。

非特权进程不能向正在运行的内核系统调用表中任意插入新处理程序。扩展接口需要编写内核代码并谨慎设计 ABI。seccomp 等功能可以过滤允许进程发出的调用，但不能创建新的内核实现。

:::single-choice{#system-calls-number-portability} 为什么应用程序不应硬编码来自另一种架构的系统调用号？

::option[编号和调用约定由 ABI 决定。]{#system-calls-abi-specific .correct explanation="在一种架构上有意义的编号，在另一种架构上可能表示其他操作或根本不存在。"}
::option[系统调用根据当前工作目录命名。]{#system-calls-directory-names explanation="路径名并不定义系统调用编号 ABI。"}
::option[每个进程启动时都会获得随机的系统调用表。]{#system-calls-random-table explanation="运行中内核的 ABI 对特定架构保持稳定，并不会按进程随机化。"}
:::

## 使用 `strace` 跟踪

跟踪一条简单命令，并将输出单独保存：

```bash
$ strace -o trace.log -- ls
```

在获得授权的情况下，可用 `-f` 跟踪子进程，也可以使用表达式缩小输出范围：

```bash
$ strace -f -e trace=%file -o trace.log -- command
```

`strace` 可能暴露路径、参数、来自环境的数据、网络地址、文件内容片段，以及被错误放入参数的凭据。应使用严格权限保存跟踪记录，并按照事件数据管理策略将其删除。

:::single-choice{#system-calls-strace-purpose} `strace` 主要观察什么？

::option[只观察应用程序内部执行的源代码行。]{#system-calls-strace-source-lines explanation="源代码级跟踪需要带有符号的调试器或插桩工具。"}
::option[用户空间与内核边界上的系统调用和信号。]{#system-calls-strace-boundary .correct explanation="它会报告被跟踪进程的请求、参数、结果和信号事件。"}
::option[每个 CPU 核心的物理电压。]{#system-calls-strace-voltage explanation="硬件遥测不属于系统调用跟踪。"}
:::

## 谨慎解读跟踪记录

跟踪会改变时序，并可能产生很大开销。失败的调用可能只是预期的探测，最终可见的错误也可能源于更早的操作或应用程序策略。应解析文件描述符、跟踪进程关系，并与应用程序日志相互印证。

权限和 ptrace 安全策略会限制可以跟踪哪些进程。未经授权，不要附加到其他用户的进程或生产进程；暂停和时序变化都可能影响服务行为。

:::single-choice{#system-calls-strace-failure} 跟踪记录中出现一次失败的系统调用，是否一定表示应用程序已损坏？

::option[是；每个非零返回值都会立即终止 Linux。]{#system-calls-nonzero-terminates explanation="应用程序通常会处理系统调用错误，而不会导致系统故障。"}
::option[不是；程序经常探测替代方案并处理预期错误。]{#system-calls-expected-failure .correct explanation="应结合控制流和应用程序上下文解读返回值，而不是孤立看待。"}
::option[是；内核绝不会返回预期错误。]{#system-calls-no-expected-errors explanation="路径不存在或操作不受支持等错误都是正常的 API 结果。"}
:::

## 总结

现在，你可以从库 API 一直追踪到经过验证的内核工作。

1. 区分高层函数和系统调用 ABI。
2. 理解架构进入指令与受控内核分派的关系。
3. 将系统调用号和结构视为架构特有内容。
4. 使用过滤后的 `strace` 输出，同时保护敏感数据。
5. 结合应用程序上下文解读失败和跟踪开销。
