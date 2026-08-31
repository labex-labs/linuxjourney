---
lesson_id: "cpu-monitoring"
course_id: "process-utilization"
lang: "en"
order_index: 4
title: "CPU Monitoring"
description: "Learn how to interpret Linux load averages alongside CPU count, utilization, and task state."
meta_title: "CPU Monitoring - Process Utilization"
meta_description: "Learn the fundamentals of Linux CPU monitoring using the uptime command. This beginner guide explains how to interpret load average, understand process utilization, and assess system performance."
meta_keywords: "uptime command, Linux CPU monitoring, load average, system performance, process utilization, Linux tutorial, beginner guide"
---

CPU troubleshooting starts by separating load, utilization, and responsiveness. No single number establishes a bottleneck, so compare several time windows and relate host metrics to the workload users actually experience.

## Reading uptime

`uptime` provides a compact starting point:

```text
$ uptime
 17:23:35 up 1 day, 5:59, 2 users, load average: 0.00, 0.02, 0.05
```

The final three values are load averages over approximately 1, 5, and 15 minutes. Comparing them shows direction: a much larger 1-minute value can indicate rising load, while a larger 15-minute value can indicate load that is falling.

:::single-choice{#cpu-uptime-windows}
In what order does `uptime` display load-average windows?

::option[15, 5, and 1 seconds.]{#cpu-windows-seconds explanation="The values are minute-scale averages and are not printed longest-first."}
::option[1, 5, and 15 minutes.]{#cpu-windows-one-five-fifteen .correct explanation="The shortest recent window appears first and the longest appears last."}
::option[Current, minimum, and maximum CPU percentages.]{#cpu-windows-percentages explanation="Load average is not a minimum or maximum CPU percentage."}
:::

## Understanding Linux Load

Linux load average counts tasks that are runnable, including those using or waiting for CPU, plus tasks in uninterruptible sleep, commonly associated with I/O. It is therefore not the same as CPU utilization.

A load of `4.0` has different implications on systems with one and sixteen logical CPUs. Find the number of processing units available to the system with:

```bash
$ nproc
```

CPU quotas, affinity, virtualization, and container limits can reduce capacity visible to a particular workload, so host CPU count is only a starting point.

:::single-choice{#cpu-load-not-percentage}
Why is load average not a CPU-utilization percentage?

::option[It reports only the CPU clock frequency.]{#cpu-load-clock explanation="Clock speed is a separate hardware or scaling metric."}
::option[It measures only free physical memory.]{#cpu-load-memory explanation="Memory availability is reported by other metrics."}
::option[It includes runnable tasks and tasks in uninterruptible sleep.]{#cpu-load-task-count .correct explanation="Load is based on task demand and wait state rather than a percentage of elapsed CPU time."}
:::

## Comparing Load with CPU Activity

Collect multiple samples rather than relying on one output. Useful companions include:

```bash
$ top
$ vmstat 1
$ mpstat -P ALL 1
```

`top` combines host and process views. `vmstat` shows runnable and blocked task counts with CPU categories. `mpstat`, supplied by `sysstat` on many distributions, shows per-CPU activity. Availability and exact fields vary, so use local manuals.

High load with busy CPUs can indicate CPU demand. High load with notable blocked tasks, I/O latency, or I/O-wait observations points toward another constrained resource. Low average utilization can also hide one saturated CPU or a brief latency spike.

:::single-choice{#cpu-high-load-next-step}
What is the best next step after observing a high load average?

::option[Compare repeated CPU, task-state, I/O, and workload measurements.]{#cpu-load-correlate .correct explanation="Correlated samples distinguish competing explanations for the load."}
::option[Reboot immediately without collecting any other data.]{#cpu-load-reboot explanation="Rebooting removes evidence and can interrupt services without identifying the cause."}
::option[Assume every CPU is fully utilized.]{#cpu-load-assume explanation="Load can include uninterruptible tasks and may be uneven across CPUs."}
:::

## Evaluating Capacity and Impact

There is no universal rule that load must always remain below CPU count. Batch systems may accept queues, while interactive services may violate latency targets before that point. Establish a baseline for the same host and workload, then compare response time, throughput, error rate, saturation, and resource use.

:::single-choice{#cpu-capacity-threshold}
What should determine whether observed load is acceptable?

::option[A requirement that the value always remain below one.]{#cpu-below-one explanation="Multicore capacity and workload goals make this fixed threshold unreliable."}
::option[The number of users listed by `uptime` alone.]{#cpu-user-count explanation="Logged-in shell users do not represent all workload demand."}
::option[The workload's baseline and service objectives.]{#cpu-baseline-objectives .correct explanation="Acceptability depends on expected behavior and user-visible performance, not a universal threshold."}
:::

## Summary

You can now interpret load average as one part of a CPU investigation.

1. Read the 1-, 5-, and 15-minute load windows.
2. Distinguish task load from CPU-time percentages.
3. Compare load with available processing capacity.
4. Correlate repeated host measurements with service outcomes.
