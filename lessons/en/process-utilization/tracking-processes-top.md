---
lesson_id: "tracking-processes-top"
course_id: "process-utilization"
lang: "en"
order_index: 1
title: "Tracking processes: top"
description: "Learn how to use top to interpret system load, CPU, memory, and per-process activity."
meta_title: "Tracking processes: top - Process Utilization"
meta_description: "Discover the best way to learn Linux by mastering the `top` command. This guide explains how to monitor system resources, track processes, and understand metrics like VIRT and RES. A key part of understanding how Linux works."
meta_keywords: "Linux top command, monitor processes, system utilization, how linux works, linux top virt res, best way to learn linux, linux performance, process management, free online linux training with certificate"
---

`top` provides a repeatedly updated view of system activity and running processes. It is useful for forming a performance hypothesis, but a busy sample alone does not prove the cause of a problem. Compare several updates and correlate them with logs and workload-specific metrics.

## Reading the System Summary

A typical display begins with summary lines followed by a process table:

```text
top - 18:06:26 up 6 days, 4:07, 2 users, load average: 0.92, 0.62, 0.59
Tasks: 389 total, 1 running, 387 sleeping, 0 stopped, 1 zombie
%Cpu(s): 1.8 us, 0.4 sy, 0.0 ni, 97.6 id, 0.1 wa, 0.0 hi, 0.0 si, 0.0 st
MiB Mem : 32099.0 total, 5276.3 free, 7031.2 used, 19791.5 buff/cache
MiB Swap: 32700.0 total, 32661.0 free, 39.0 used
```

The first line contains the current time, uptime, logged-in user count, and 1-, 5-, and 15-minute load averages. The task line counts process states. Load average is not a direct CPU percentage; on Linux it reflects runnable tasks and tasks in uninterruptible sleep, so interpret it alongside CPU count, I/O activity, and latency.

:::single-choice{#top-load-average-periods}
What do the three load-average values in `top` represent?

::option[Average load over 1, 5, and 15 minutes.]{#top-one-five-fifteen .correct explanation="The values summarize progressively longer recent time windows."}
::option[CPU use by the three busiest processes.]{#top-three-processes explanation="Per-process CPU appears in the process table, not in these three summary values."}
::option[Free memory, cache, and swap in megabytes.]{#top-three-memory-values explanation="Memory and swap have separate summary lines."}
:::

## Interpreting CPU Time

Common CPU fields include:

- `us`: user-space execution time.
- `sy`: kernel execution time.
- `ni`: user-space time for niced tasks.
- `id`: idle time.
- `wa`: idle time while an outstanding I/O request exists.
- `hi` and `si`: hardware- and software-interrupt handling.
- `st`: virtual CPU time taken by the hypervisor for other guests.

A high `wa` value can support an I/O-wait hypothesis, but it does not identify a device or prove that storage is the only bottleneck. Inspect device latency and application behavior before concluding.

:::single-choice{#top-cpu-wa-meaning}
What does the `wa` CPU field report?

::option[Time spent executing ordinary user code.]{#top-wa-user explanation="User-space execution is reported under `us`."}
::option[Memory pages written to swap since boot.]{#top-wa-swap explanation="Swap activity is not a CPU-time category."}
::option[Idle CPU time while an I/O request is outstanding.]{#top-wa-io .correct explanation="The field is I/O-wait time and needs supporting device evidence for diagnosis."}
:::

## Reading the Process Table

Important columns commonly include:

- `PID`, `USER`, and `COMMAND`: identity and ownership.
- `S`: state such as running (`R`), sleeping (`S`), uninterruptible sleep (`D`), stopped (`T`), or zombie (`Z`).
- `%CPU` and `%MEM`: sampled CPU activity and share of physical memory.
- `TIME+`: accumulated CPU time.
- `VIRT`: total virtual address space associated with the task.
- `RES`: resident, non-swapped physical memory currently attributed to it.
- `SHR`: resident memory that may be shared with other processes.

`VIRT` is not the amount of physical RAM consumed. It can include mapped files, shared libraries, reserved address space, and swapped pages. Even `RES` should be interpreted carefully because shared pages complicate attribution.

:::single-choice{#top-res-versus-virt}
Which field is closer to a process's currently resident physical memory?

::option[`TIME+`]{#top-time-field explanation="This field accumulates CPU time rather than memory."}
::option[`VIRT`]{#top-virt-field explanation="Virtual size includes address space that need not be resident in RAM."}
::option[`RES`]{#top-res-field .correct explanation="Resident size reflects physical pages currently resident for the process, subject to sharing caveats."}
:::

## Focusing and Sorting

Monitor known PIDs directly:

```bash
$ top -p 1234,5678
```

Inside `top`, press `P` to sort by CPU, `M` to sort by memory, `1` to toggle per-CPU lines, and `q` to quit on common procps-ng implementations. Press `h` for the local interactive help because keys and fields can differ by implementation.

Record the PID, command, timestamp, and several samples before taking action. A process briefly reaching the top can be normal, and terminating it can cause data loss or an outage.

:::single-choice{#top-monitor-known-pid}
Which invocation limits the display to PID 1234?

::option[`top -u 1234`]{#top-user-filter explanation="The `-u` form filters by user rather than treating the value as a PID."}
::option[`top -d 1234`]{#top-delay-filter explanation="The `-d` option controls refresh delay on common implementations."}
::option[`top -p 1234`]{#top-pid-filter .correct explanation="The `-p` option selects one or more process IDs for monitoring."}
:::

## Summary

You can now use `top` to build and test a system-performance hypothesis.

1. Read load averages as time-windowed load, not CPU percentages.
2. Compare CPU categories across multiple samples.
3. Distinguish virtual address space from resident memory.
4. Focus on known PIDs and verify evidence before acting.
