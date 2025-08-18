---
lang: "zh"
title: "I/O 监控"
meta_description: "学习如何使用 iostat 进行 Linux I/O 监控。通过这个基本命令了解 CPU 和磁盘使用情况指标。提高系统性能！"
meta_keywords: "iostat, Linux I/O 监控，CPU 使用率，磁盘使用率，Linux 命令，初学者，教程，指南"
---

## Lesson Content

我们可以使用一个方便的工具 **iostat** 来监控 CPU 使用率以及磁盘使用率。

```bash
pete@icebox:~$ iostat
Linux 3.13.0-39-lowlatency (icebox)     01/28/2016      _i686_  (1 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.13    0.03    0.50    0.01    0.00   99.33

Device:            tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               0.17         3.49         1.92     385106     212417
```

第一部分是 CPU 信息：

- **%user** - 显示在用户级别（应用程序）执行时 CPU 利用率的百分比。
- **%nice** - 显示在用户级别以 nice 优先级执行时 CPU 利用率的百分比。
- **%system** - 显示在系统级别（内核）执行时 CPU 利用率的百分比。
- **%iowait** - 显示 CPU 或 CPU 处于空闲状态，但系统有未完成的磁盘 I/O 请求的时间百分比。
- **%steal** - 显示虚拟 CPU 或 CPU 在管理程序为另一个虚拟处理器提供服务时，被迫等待的时间百分比。
- **%idle** - 显示 CPU 或 CPU 处于空闲状态，且系统没有未完成的磁盘 I/O 请求的时间百分比。

第二部分是磁盘利用率：

- **tps** - 表示每秒向设备发出的传输次数。传输是对设备的 I/O 请求。多个逻辑请求可以合并为一个对设备的 I/O 请求。传输的大小是不确定的。
- **kB_read/s** - 表示从设备读取的数据量，以千字节每秒表示。
- **kB_wrtn/s** - 表示写入设备的数据量，以千字节每秒表示。
- **kB_read** - 读取的总千字节数。
- **kB_wrtn** - 写入的总千字节数。

## Exercise

使用 iostat 查看您的磁盘使用情况。

## Quiz Question

可以使用什么命令来查看 I/O 和 CPU 使用情况？

## Quiz Answer

iostat
