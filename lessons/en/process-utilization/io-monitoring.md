---
lesson_id: "io-monitoring"
course_id: "process-utilization"
lang: "en"
order_index: 5
title: "I/O Monitoring"
description: "Learn how to use iostat samples to investigate CPU and block-device activity."
meta_title: "I/O Monitoring - Process Utilization"
meta_description: "Master Linux I/O monitoring with the iostat command. This guide explains how to analyze CPU and disk usage metrics to optimize your system's performance."
meta_keywords: "i/o monitoring, iostat, linux i/o monitoring, cpu usage, disk usage, system performance, iowait, linux commands"
---

`iostat`, commonly provided by the `sysstat` package, reports CPU and block-device activity. Use repeated samples and application latency together: throughput or utilization alone does not establish whether storage is causing a user-visible problem.

## Collecting Useful Samples

Run extended device statistics at one-second intervals:

```bash
$ iostat -xz 1
```

On common implementations, the first report contains averages since boot and later reports cover each interval. The `-x` option adds extended fields, while `-z` suppresses inactive devices. Allow several intervals to capture normal and problematic periods.

:::single-choice{#iostat-first-report}
What does the first `iostat` report commonly represent?

::option[Only operations from the final second of the command.]{#iostat-final-second explanation="That does not describe the initial cumulative report."}
::option[Activity averages since the system booted.]{#iostat-since-boot .correct explanation="Later reports are usually interval-specific, so the first must be interpreted separately."}
::option[A forecast of tomorrow's device utilization.]{#iostat-forecast explanation="The tool reports observed statistics rather than future demand."}
:::

## Reading CPU Fields

The CPU section commonly includes user (`%user`), system (`%system`), idle (`%idle`), I/O wait (`%iowait`), and virtual-machine steal (`%steal`) time. I/O wait is CPU idle time during which the system has an outstanding I/O request; it is not the percentage of a disk that is busy.

:::single-choice{#iostat-iowait-meaning}
What does `%iowait` describe?

::option[The percentage of disk capacity already filled.]{#iostat-capacity explanation="Filesystem capacity and CPU time are different measurements."}
::option[CPU idle time while an I/O request is outstanding.]{#iostat-iowait-cpu .correct explanation="It is a CPU-time category and cannot identify a device by itself."}
::option[The number of files waiting to be deleted.]{#iostat-delete-queue explanation="File deletion counts are not represented by this field."}
:::

## Reading Device Fields

Field names vary by sysstat version, but useful concepts include:

- Read and write operations or data per second show workload rate.
- `await` reports average request latency, including queue and service time.
- Average queue-size fields show requests waiting or being serviced.
- `%util` reports the percentage of elapsed time during which the device had I/O in progress.

High `%util` can indicate saturation for a simple serial device, but it does not translate directly into performance capacity for parallel storage, arrays, or virtual devices. Compare latency with the device design, workload pattern, and service objective.

:::single-choice{#iostat-await-purpose}
Which field is most directly associated with average I/O request latency?

::option[Device name.]{#iostat-device-name explanation="The name identifies the device but does not measure request duration."}
::option[`await`]{#iostat-await .correct explanation="Await reflects average time for requests, including queue and service time."}
::option[`%idle`]{#iostat-idle explanation="This is a CPU field rather than device request latency."}
:::

## Correlating the Evidence

Map device names to mounts and backing devices before drawing conclusions:

```bash
$ lsblk -o NAME,TYPE,SIZE,FSTYPE,MOUNTPOINTS
$ findmnt
```

Then correlate `iostat` intervals with application response time, database or filesystem metrics, and process-level I/O. Device-mapper, RAID, containers, and network-backed storage can add layers that require their own tools.

:::single-choice{#iostat-high-util-conclusion}
What should you do after seeing high `%util` on a device?

::option[Assume every filesystem is out of free space.]{#iostat-assume-full explanation="Busy time does not report filesystem capacity."}
::option[Delete files before identifying the mounted workload.]{#iostat-delete-first explanation="Deletion is a state-changing action unrelated to proving an I/O bottleneck."}
::option[Correlate latency and workload behavior with the storage design.]{#iostat-correlate .correct explanation="Device parallelism and workload goals determine whether the observation is harmful."}
:::

## Summary

You can now use `iostat` as evidence in an I/O investigation.

1. Collect multiple extended-statistics intervals.
2. Distinguish CPU I/O wait from device busy time.
3. Interpret latency, queueing, throughput, and utilization together.
4. Map devices to workloads and verify application impact.
