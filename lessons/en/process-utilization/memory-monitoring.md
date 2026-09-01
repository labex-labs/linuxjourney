---
lesson_id: "memory-monitoring"
course_id: "process-utilization"
lang: "en"
order_index: 6
title: "Memory Monitoring"
description: "Learn how to interpret vmstat memory, paging, process, I/O, and CPU samples."
meta_title: "Memory Monitoring - Process Utilization"
meta_description: "Master Linux memory monitoring with the vmstat command. This guide explains how to use this powerful memory utilization monitor to analyze system performance metrics."
meta_keywords: "memory monitoring, memory utilization monitor, vmstat, linux memory, system performance, memory usage, linux tutorial"
---

Linux intentionally uses otherwise idle memory for caches, so a small `free` value alone does not prove memory pressure. `vmstat` helps relate memory to runnable tasks, paging, I/O, and CPU activity.

## Sampling with vmstat

Collect one sample per second:

```bash
$ vmstat 1
```

The first data row generally reports averages since boot; subsequent rows cover each interval. Stop with `Ctrl-C` after capturing a representative period. Units and available fields vary, so check `vmstat --unit` and the local manual.

:::single-choice{#vmstat-interval-rows} Which rows are best for observing second-by-second changes from `vmstat 1`?

::option[Later rows after the initial report.]{#vmstat-later-rows .correct explanation="Later rows describe each requested interval rather than the cumulative period."}
::option[Only the headings above the first data row.]{#vmstat-headings explanation="Headings define fields but contain no activity samples."}
::option[Only a row copied from a different host.]{#vmstat-other-host explanation="A different system does not represent the current workload."}
:::

## Processes and Memory

Common process fields are `r`, runnable tasks, and `b`, tasks blocked in uninterruptible sleep. Memory fields include used swap (`swpd`), idle memory (`free`), buffers (`buff`), and cache (`cache`). These are system-wide values, not per-process consumption.

For an easier view of currently available memory, compare with:

```bash
$ free -h
```

The `available` estimate is generally more useful than `free` alone because reclaimable cache can satisfy new allocations.

:::single-choice{#vmstat-free-memory} Why can a low `free` value be normal on Linux?

::option[The value always excludes all physical RAM.]{#vmstat-excludes-ram explanation="It is a memory field, though its exact unit should be checked."}
::option[The kernel can use idle memory for reclaimable caches.]{#vmstat-reclaimable-cache .correct explanation="Cached memory can often be reclaimed when applications need it."}
::option[Low free memory proves the CPU is powered off.]{#vmstat-cpu-off explanation="Memory allocation and CPU power state are unrelated conclusions."}
:::

## Paging and I/O

`si` and `so` show swap-in and swap-out rates. Sustained paging combined with latency and memory reclaim activity can indicate pressure, but nonzero swap use (`swpd`) does not by itself prove a current problem. `bi` and `bo` report block input and output rates and are not limited to swap traffic.

:::single-choice{#vmstat-swap-pressure} Which evidence better supports current memory-pressure diagnosis?

::option[A nonzero `swpd` value with no other observations.]{#vmstat-swpd-alone explanation="Pages can remain in swap after earlier pressure, so the amount alone is insufficient."}
::option[Sustained paging correlated with reclaim activity and workload latency.]{#vmstat-correlated-pressure .correct explanation="Repeated, correlated evidence connects memory behavior to current impact."}
::option[The hostname printed at login.]{#vmstat-hostname explanation="A hostname does not measure reclaim or paging activity."}
:::

## CPU and System Activity

CPU columns commonly include user (`us`), system (`sy`), idle (`id`), I/O wait (`wa`), and steal (`st`) percentages. System columns include interrupts (`in`) and context switches (`cs`) per second. Interpret spikes against a baseline; high context-switch rates can be normal for some workloads.

:::single-choice{#vmstat-r-column} What does the `r` process field represent?

::option[Read-only mounted filesystems.]{#vmstat-readonly explanation="Filesystem mount flags are not represented by the process field."}
::option[Remote users with active shells.]{#vmstat-remote-users explanation="Login sessions are reported by other tools."}
::option[Tasks that are runnable or waiting for CPU.]{#vmstat-runnable .correct explanation="Comparing this count with CPU capacity can help identify CPU demand."}
:::

## Summary

You can now interpret `vmstat` as a time-correlated system view.

1. Separate the initial cumulative report from interval samples.
2. Treat cache as potentially reclaimable memory.
3. Correlate paging with reclaim and application impact.
4. Read process, I/O, system, and CPU fields together.
