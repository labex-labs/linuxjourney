---
index: 5
lang: "zh"
title: "I/O 监控"
meta_title: "I/O 监控 - 进程利用率"
meta_description: "使用 iostat 命令掌握 Linux I/O 监控。本指南解释了如何分析 CPU 和磁盘使用率指标以优化系统性能。"
meta_keywords: "i/o 监控，iostat, linux i/o 监控，cpu 使用率，磁盘使用率，系统性能，iowait, linux 命令"
---

## Lesson Content

有效的**I/O 监控**对于维护一个健康且响应迅速的 Linux 系统至关重要。一个强大的命令行工具是 **iostat**，它提供有关 CPU 和磁盘活动的详细报告。

运行 `iostat` 命令会生成系统性能指标的快照。

```bash
pete@icebox:~$ iostat
Linux 3.13.0-39-lowlatency (icebox)     01/28/2016      _i686_  (1 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.13    0.03    0.50    0.01    0.00   99.33

Device:            tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               0.17         3.49         1.92     385106     212417
```

输出分为两个主要部分。我们来分解一下。

### 理解 CPU 指标

第一个报告详细说明了 CPU 利用率，提供了有关处理器如何分配时间的见解。

- **%user**: 用于执行用户级（应用程序）进程的 CPU 时间百分比。
- **%nice**: 用于执行具有修改（nice）优先级的用户级进程的 CPU 时间百分比。
- **%system**: 用于执行系统级（内核）进程的 CPU 时间百分比。
- **%iowait**: CPU 在等待待处理的磁盘 I/O 请求完成而处于空闲状态的时间百分比。这里的高值可能表明存储瓶颈。
- **%steal**: 在虚拟化环境中，这是虚拟 CPU 在等待真实 CPU 期间，而管理程序正在为另一个虚拟处理器提供服务的时间百分比。
- **%idle**: CPU 处于空闲状态且未等待任何磁盘 I/O 请求的时间百分比。

### 分析磁盘利用率

第二个报告侧重于设备级别的**I/O 监控**，显示数据是如何在存储设备之间传输的。

- **tps**: 发送到设备的每秒传输次数。一次传输是一个 I/O 请求，多个逻辑请求可以合并为一个请求。
- **kB_read/s**: 从设备读取的数据量，以每千字节/秒为单位。
- **kB_wrtn/s**: 写入到设备的字节量，以每千字节/秒为单位。
- **kB_read**: 自上次重新启动以来从设备读取的总千字节数。
- **kB_wrtn**: 自上次重新启动以来写入到设备的字节总数。

## Exercise

实践造就完美！以下是一些实践实验，以加强您对系统监控和磁盘使用的理解：

1. **[Linux df 命令：磁盘空间报告](https://labex.io/zh/labs/linux-linux-df-command-disk-space-reporting-219188)** - 练习报告挂载文件系统的磁盘空间使用情况，这是监控的关键方面。
2. **[Linux du 命令：文件空间估算](https://labex.io/zh/labs/linux-linux-du-command-file-space-estimating-219190)** - 学习估算目录和子目录的磁盘空间使用情况，补充 `iostat` 提供的磁盘 I/O 信息。
3. **[Linux top 命令：实时系统监控](https://labex.io/zh/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - 探索实时系统监控，包括 CPU 和内存使用情况，为 `iostat` 中看到的 CPU 指标提供更广泛的背景。

这些实验将帮助您在真实场景中应用这些概念，并建立对监控 Linux 系统资源的信心。

## Quiz Question

可以使用哪个命令来查看 I/O 和 CPU 使用情况？（请仅使用小写英文字符回答）

## Quiz Answer

iostat
