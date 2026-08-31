---
lesson_id: "tracking-processes-lsof-fuser"
course_id: "process-utilization"
lang: "zh"
order_index: 2
title: "lsof 和 fuser"
description: "学习如何识别正在使用文件、目录、挂载点和网络套接字的进程。"
meta_title: "lsof 和 fuser - 进程资源利用"
meta_description: "探索 Linux 中的 lsof 和 fuser 命令，以识别哪些进程正在使用特定文件。学习如何解决“设备或资源忙碌”错误，比较 fuser 与 lsof，并使用 fuser -k 等选项有效管理打开的文件。"
meta_keywords: "lsof, fuser, fuser 命令，linux fuser, fuser 与 lsof, lsof 与 fuser, fuser -k linux, 打开文件，进程管理，设备忙碌，Linux 命令"
---

进程打开文件、把文件映射到内存，或把某个目录用作当前工作目录，都可能让文件系统保持忙碌状态。`lsof` 和 `fuser` 可以帮助识别这些关系。应先检查；是否停止进程是另一项会产生实际运行影响的决定。

## 使用 lsof 列出打开的文件

`lsof` 意为“列出打开的文件”（list open files）。查询路径可以看到匹配的打开文件记录：

```bash
$ sudo lsof -- /mnt/usb
```

若要递归查询同一文件系统中的整棵目录树，常见实现支持 `+D`，但递归扫描可能代价很高：

```bash
$ sudo lsof +D /mnt/usb
```

常用列包括 `COMMAND`、`PID`、`USER`、文件描述符（`FD`）、类型、设备和 `NAME`。`FD` 为 `cwd` 的记录表示进程把该目录用作当前工作目录。对于其他用户拥有的进程，非特权用户看到的输出可能不完整。

:::single-choice{#lsof-cwd-record}
`FD` 列中的 `cwd` 表示什么？

::option[进程把该目录用作当前工作目录。]{#lsof-current-directory .correct explanation="进程的当前目录可能使已挂载文件系统保持忙碌。"}
::option[文件在写入过程中被关闭。]{#lsof-closed-write explanation="这个标记描述的是目录关系，而不是关闭事件。"}
::option[进程拥有该文件系统设备。]{#lsof-device-owner explanation="文件系统所有权并不由 `cwd` 描述符标签表示。"}
:::

## 使用 fuser 识别使用者

`fuser` 会报告正在使用指定文件或文件系统的进程 ID。详细输出还会显示用户、访问类型和命令名称：

```bash
$ sudo fuser -v /mnt/usb
```

如果要把参数视为已挂载文件系统，并查找访问其中任意文件的进程，可以使用 procps `fuser` 支持的挂载选项：

```bash
$ sudo fuser -vm /mnt/usb
```

应使用 `findmnt --target /mnt/usb` 等工具确认该路径确实是目标挂载点。绑定挂载、命名空间、权限和竞态都会影响单次查询能够发现的内容。

:::single-choice{#fuser-verbose-purpose}
调查时为什么要使用 `fuser -v`，而不是普通的 `fuser`？

::option[它会自动卸载选中的文件系统。]{#fuser-verbose-unmount explanation="详细模式只报告更多信息，不会请求卸载。"}
::option[它会增加用户、访问类型和命令等上下文。]{#fuser-verbose-details .correct explanation="额外字段有助于判断应该与哪些进程协调，以及哪些进程可以安全停止。"}
::option[它会永久阻止进程再次打开文件。]{#fuser-verbose-prevent explanation="报告信息并不会创建访问控制规则。"}
:::

## 处理忙碌的文件系统

不要立即杀死所有匹配的 PID，而应遵循审慎的顺序：

1. 确认主机、路径、挂载源和计划进行的维护。
2. 实际可行时，同时使用这两个工具识别进程。
3. 判断每个进程能否停止、移出该目录，或等待其自行完成。
4. 如果服务管理器或应用接口可用，应通过它们停止进程。
5. 再次查询，然后卸载并验证结果。

`fuser -k` 会向匹配的进程发送信号。在常见的 procps 实现中，它默认发送 `SIGKILL`，因此无法实现有序关闭。如果确实需要执行已明确批准的终止操作，应选择适当信号、核实 PID 和所有者，并认识到从检查到执行操作期间，匹配的进程集合可能发生变化。

:::single-choice{#fuser-k-risk}
为什么 `fuser -k /mnt/usb` 不适合作为排障的第一步？

::option[它只会打印文件系统的可用空间。]{#fuser-k-space explanation="该选项针对进程，而不是报告容量。"}
::option[它可能在没有有序清理的情况下杀死多个匹配进程。]{#fuser-k-kills .correct explanation="这种宽泛的信号操作可能中断写入或服务，因此应先调查并协调。"}
::option[它会更改每个匹配进程的工作目录。]{#fuser-k-chdir explanation="它发送信号，不会移动进程目录。"}
:::

## 选择工具

需要查看详细的打开文件记录、描述符或套接字信息时，使用 `lsof`。需要从路径出发查看匹配 PID 和访问类型时，使用 `fuser`。任何一个工具的结果都不能单独说明某个进程可以安全终止。

对于网络套接字，应为 `fuser` 指定明确的协议命名空间，或使用 `ss` 等专用套接字工具：

```bash
$ sudo fuser -v 22/tcp
$ sudo ss -lntp
```

:::single-choice{#lsof-fuser-tool-choice}
哪个工具适合详细列出打开的文件描述符及其所属进程？

::option[`lsof`]{#lsof-detailed-records .correct explanation="它的输出围绕打开文件记录及其进程元数据组织。"}
::option[`uptime`]{#lsof-uptime explanation="`uptime` 报告运行时间和平均负载，而不是打开的描述符。"}
::option[`free`]{#lsof-free explanation="`free` 汇总内存，而不是文件使用情况。"}
:::

## 总结

现在，你可以调查文件和文件系统的使用情况，而不会把终止进程当作默认处理方式。

1. 使用 `lsof` 查看详细的打开文件记录。
2. 使用 `fuser` 获取以路径为中心的 PID 和访问信息。
3. 确认挂载点，并考虑权限和竞态。
4. 在考虑发送信号前，先协调有序停止。
5. 再次查询，并验证卸载或服务操作的结果。
