---
index: 5
lang: "en"
title: "I/O Monitoring"
meta_title: "I/O Monitoring - Process Utilization"
meta_description: "Learn how to use iostat for Linux I/O monitoring. Understand CPU and disk usage metrics with this essential command. Improve system performance!"
meta_keywords: "iostat, Linux I/O monitoring, CPU usage, disk usage, Linux commands, beginner, tutorial, guide"
---

## Lesson Content

We can monitor CPU usage as well as disk usage with a handy tool known as **iostat**.

```bash
pete@icebox:~$ iostat
Linux 3.13.0-39-lowlatency (icebox)     01/28/2016      _i686_  (1 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.13    0.03    0.50    0.01    0.00   99.33

Device:            tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               0.17         3.49         1.92     385106     212417
```

The first part is the CPU information:

- **%user** - Shows the percentage of CPU utilization that occurred while executing at the user level (application).
- **%nice** - Shows the percentage of CPU utilization that occurred while executing at the user level with nice priority.
- **%system** - Shows the percentage of CPU utilization that occurred while executing at the system level (kernel).
- **%iowait** - Shows the percentage of time that the CPU or CPUs were idle during which the system had an outstanding disk I/O request.
- **%steal** - Shows the percentage of time spent in involuntary wait by the virtual CPU or CPUs while the hypervisor was servicing another virtual processor.
- **%idle** - Shows the percentage of time that the CPU or CPUs were idle and the system did not have an outstanding disk I/O request.

The second part is the disk utilization:

- **tps** - Indicates the number of transfers per second that were issued to the device. A transfer is an I/O request to the device. Multiple logical requests can be combined into a single I/O request to the device. A transfer is of indeterminate size.
- **kB_read/s** - Indicates the amount of data read from the device, expressed in kilobytes per second.
- **kB_wrtn/s** - Indicates the amount of data written to the device, expressed in kilobytes per second.
- **kB_read** - The total number of kilobytes read.
- **kB_wrtn** - The total number of kilobytes written.

## Exercise

Use iostat to view your disk usage.

## Quiz Question

What command can be used to view I/O and CPU usage?

## Quiz Answer

iostat
