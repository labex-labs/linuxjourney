---
lesson_id: "tracking-processes-top"
course_id: "process-utilization"
lang: "zh"
order_index: 1
title: "使用 top 跟踪进程"
description: "学习如何使用 top 解读系统负载、CPU、内存和各进程的活动情况。"
meta_title: "使用 top 跟踪进程 - 进程资源利用"
meta_description: "通过掌握 `top` 命令，发现学习 Linux 的最佳方式。本指南解释了如何监控系统资源、跟踪进程以及理解 VIRT 和 RES 等指标。这是理解 Linux 工作原理的关键部分。"
meta_keywords: "Linux top 命令，进程监控，系统利用率，Linux 工作原理，linux top virt res, 学习 Linux 的最佳方法，Linux 性能，进程管理，免费在线 Linux 培训带证书"
---

`top` 会反复更新系统活动和运行进程的视图。它适合用来形成性能问题的假设，但单个繁忙样本本身并不能证明问题原因。应比较多次更新，并结合日志和工作负载特有的指标进行分析。

## 阅读系统摘要

典型显示以几行摘要开头，后面是进程表：

```text
top - 18:06:26 up 6 days, 4:07, 2 users, load average: 0.92, 0.62, 0.59
Tasks: 389 total, 1 running, 387 sleeping, 0 stopped, 1 zombie
%Cpu(s): 1.8 us, 0.4 sy, 0.0 ni, 97.6 id, 0.1 wa, 0.0 hi, 0.0 si, 0.0 st
MiB Mem : 32099.0 total, 5276.3 free, 7031.2 used, 19791.5 buff/cache
MiB Swap: 32700.0 total, 32661.0 free, 39.0 used
```

第一行包含当前时间、系统运行时长、已登录用户数，以及 1、5、15 分钟的平均负载。任务行统计各进程状态的数量。平均负载不是直接的 CPU 百分比；在 Linux 中，它反映可运行任务和不可中断睡眠任务的数量，因此需要结合 CPU 数量、I/O 活动和延迟来解读。

:::single-choice{#top-load-average-periods}
`top` 中的三个平均负载值分别表示什么？

::option[过去 1、5、15 分钟的平均负载。]{#top-one-five-fifteen .correct explanation="这些值依次汇总逐渐变长的近期时间窗口。"}
::option[最繁忙的三个进程各自的 CPU 使用率。]{#top-three-processes explanation="每个进程的 CPU 使用率显示在进程表中，而不是这三个摘要值中。"}
::option[以 MB 为单位的可用内存、缓存和交换空间。]{#top-three-memory-values explanation="内存和交换空间有各自独立的摘要行。"}
:::

## 解读 CPU 时间

常见的 CPU 字段包括：

- `us`：执行用户空间代码的时间。
- `sy`：执行内核代码的时间。
- `ni`：调整过 Nice 值的任务在用户空间执行的时间。
- `id`：空闲时间。
- `wa`：存在尚未完成的 I/O 请求时 CPU 的空闲时间。
- `hi` 和 `si`：处理硬件中断和软件中断的时间。
- `st`：虚拟机管理程序为其他来宾系统占用的虚拟 CPU 时间。

较高的 `wa` 值可以支持“I/O 等待”这一假设，但它既不能指出具体设备，也无法证明存储是唯一瓶颈。下结论前，应检查设备延迟和应用程序行为。

:::single-choice{#top-cpu-wa-meaning}
CPU 的 `wa` 字段报告什么？

::option[执行普通用户代码所花的时间。]{#top-wa-user explanation="用户空间执行时间报告在 `us` 字段中。"}
::option[系统启动以来写入交换空间的内存页数。]{#top-wa-swap explanation="交换活动并不是 CPU 时间类别。"}
::option[存在未完成 I/O 请求时 CPU 的空闲时间。]{#top-wa-io .correct explanation="该字段表示 I/O 等待时间；诊断时还需要设备层证据支持。"}
:::

## 阅读进程表

常见的重要列包括：

- `PID`、`USER` 和 `COMMAND`：标识与所有权。
- `S`：进程状态，例如运行（`R`）、睡眠（`S`）、不可中断睡眠（`D`）、停止（`T`）或僵尸（`Z`）。
- `%CPU` 和 `%MEM`：采样得到的 CPU 活动和物理内存占比。
- `TIME+`：累计 CPU 时间。
- `VIRT`：与任务关联的虚拟地址空间总量。
- `RES`：当前归属于任务、常驻且未换出的物理内存。
- `SHR`：可能与其他进程共享的常驻内存。

`VIRT` 并不是实际消耗的物理 RAM。它可能包括映射文件、共享库、预留的地址空间和已换出的内存页。即使是 `RES` 也要谨慎解读，因为共享内存页会使归属统计变得复杂。

:::single-choice{#top-res-versus-virt}
哪个字段更接近进程当前常驻的物理内存？

::option[`TIME+`]{#top-time-field explanation="该字段累计的是 CPU 时间，而不是内存。"}
::option[`VIRT`]{#top-virt-field explanation="虚拟大小包括不一定驻留在 RAM 中的地址空间。"}
::option[`RES`]{#top-res-field .correct explanation="常驻大小反映当前驻留的进程物理页，但仍需考虑共享页。"}
:::

## 聚焦与排序

可以直接监控已知 PID：

```bash
$ top -p 1234,5678
```

在常见的 procps-ng 实现中，进入 `top` 后按 `P` 可按 CPU 排序，按 `M` 可按内存排序，按 `1` 可切换每 CPU 摘要行，按 `q` 可退出。不同实现的按键和字段可能不同，因此应按 `h` 查看本地交互式帮助。

执行操作前，应记录 PID、命令、时间戳和多个样本。某个进程短暂排在首位可能是正常现象，贸然终止它可能造成数据丢失或服务中断。

:::single-choice{#top-monitor-known-pid}
哪个命令只显示 PID 1234？

::option[`top -u 1234`]{#top-user-filter explanation="`-u` 形式按用户筛选，不会把该值当作 PID。"}
::option[`top -d 1234`]{#top-delay-filter explanation="在常见实现中，`-d` 选项控制刷新间隔。"}
::option[`top -p 1234`]{#top-pid-filter .correct explanation="`-p` 选项用于选择一个或多个进程 ID 进行监控。"}
:::

## 总结

现在，你可以使用 `top` 建立并检验系统性能假设。

1. 将平均负载理解为不同时间窗口内的负载，而不是 CPU 百分比。
2. 在多个样本之间比较 CPU 时间类别。
3. 区分虚拟地址空间与常驻内存。
4. 聚焦已知 PID，并在执行操作前验证证据。
