---
index: 5
lang: "en"
title: "I/O Monitoring"
meta_title: "I/O Monitoring - Process Utilization"
meta_description: "Master Linux I/O monitoring with the iostat command. This guide explains how to analyze CPU and disk usage metrics to optimize your system's performance."
meta_keywords: "i/o monitoring, iostat, linux i/o monitoring, cpu usage, disk usage, system performance, iowait, linux commands"
---

## Lesson Content

Effective **I/O monitoring** is crucial for maintaining a healthy and responsive Linux system. A powerful command-line tool for this task is **iostat**, which provides detailed reports on both CPU and disk activity.

Running the `iostat` command generates a snapshot of your system's performance metrics.

```bash
pete@icebox:~$ iostat
Linux 3.13.0-39-lowlatency (icebox)     01/28/2016      _i686_  (1 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.13    0.03    0.50    0.01    0.00   99.33

Device:            tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               0.17         3.49         1.92     385106     212417
```

The output is divided into two main sections. Let's break them down.

### Understanding CPU Metrics

The first report details CPU utilization, providing insight into how the processor is spending its time.

- **%user**: Percentage of CPU time spent executing user-level (application) processes.
- **%nice**: Percentage of CPU time spent on user-level processes with a modified (nice) priority.
- **%system**: Percentage of CPU time spent executing system-level (kernel) processes.
- **%iowait**: Percentage of time the CPU was idle while waiting for an outstanding disk I/O request to complete. High values here can indicate a storage bottleneck.
- **%steal**: In a virtualized environment, this is the percentage of time a virtual CPU waits for a real CPU while the hypervisor is servicing another virtual processor.
- **%idle**: Percentage of time the CPU was idle and not waiting for any disk I/O requests.

### Analyzing Disk Utilization

The second report focuses on device-level **I/O monitoring**, showing how data is being transferred to and from your storage devices.

- **tps**: Transfers per second issued to the device. A transfer is an I/O request, and multiple logical requests can be combined into a single one.
- **kB_read/s**: The amount of data read from the device, expressed in kilobytes per second.
- **kB_wrtn/s**: The amount of data written to the device, expressed in kilobytes per second.
- **kB_read**: The total number of kilobytes read from the device since the last reboot.
- **kB_wrtn**: The total number of kilobytes written to the device since the last reboot.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of system monitoring and disk usage:

1. **[Linux df Command: Disk Space Reporting](https://labex.io/labs/linux-linux-df-command-disk-space-reporting-219188)** - Practice reporting disk space usage on mounted file systems, a key aspect of monitoring.
2. **[Linux du Command: File Space Estimating](https://labex.io/labs/linux-linux-du-command-file-space-estimating-219190)** - Learn to estimate disk space usage for directories and subdirectories, complementing the disk I/O information from `iostat`.
3. **[Linux top Command: Real-time System Monitoring](https://labex.io/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - Explore real-time system monitoring, including CPU and memory usage, which provides a broader context for the CPU metrics seen in `iostat`.

These labs will help you apply the concepts in real scenarios and build confidence with monitoring Linux system resources.

## Quiz Question

What command can be used to view I/O and CPU usage? (Please answer in lowercase English characters only)

## Quiz Answer

iostat
