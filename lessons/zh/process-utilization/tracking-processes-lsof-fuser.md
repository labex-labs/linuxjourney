---
index: 2
lang: "zh"
title: "lsof 和 fuser"
meta_title: "lsof 和 fuser - 进程利用率"
meta_description: "学习如何在 Linux 中使用 lsof 和 fuser 命令来识别正在使用文件的进程。理解“设备或资源忙”错误并有效管理打开的文件。"
meta_keywords: "lsof, fuser, Linux 命令，打开文件，进程管理，Linux 教程，初学者指南，设备忙"
---

## Lesson Content

假设您插入了一个 USB 驱动器并开始处理一些文件。完成后，您尝试卸载 USB 设备，但收到一个错误：“Device or Resource Busy.”您将如何找出 USB 驱动器上哪些文件仍在使用中？您可以使用以下两种工具：

### lsof

请记住，文件不仅仅是文本文件、图像等；它们是系统上的一切：磁盘、管道、网络套接字、设备等。要查看进程正在使用什么，您可以使用 `lsof` 命令（“list open files”的缩写）。这将显示所有打开的文件及其关联进程的列表。

```bash
pete@icebox:~$ lsof .
COMMAND    PID  USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
lxsession 1491 pete  cwd    DIR    8,6     4096  131 .
update-no 1796 pete  cwd    DIR    8,6     4096  131 .
nm-applet 1804 pete  cwd    DIR    8,6     4096  131 .
indicator 1809 pete  cwd    DIR    8,6     4096  131 .
xterm     2205 pete  cwd    DIR    8,6     4096  131 .
bash      2207 pete  cwd    DIR    8,6     4096  131 .
lsof      5914 pete  cwd    DIR    8,6     4096  131 .
lsof      5915 pete  cwd    DIR    8,6     4096  131 .
```

现在我可以看到哪些进程当前正在占用设备/文件。在我们的 USB 示例中，您还可以终止这些进程，以便您可以卸载这个麻烦的驱动器。

### fuser

另一种跟踪进程的方法是使用 `fuser` 命令（“file user”的缩写）。这将显示有关正在使用文件或文件用户的进程的信息。

```bash
pete@icebox:~$ fuser -v .
                     USER        PID ACCESS COMMAND
/home/pete:         pete  1491 ..c.. lxsession
                     pete  1796 ..c.. update-notifier
                     pete  1804 ..c.. nm-applet
                     pete  1809 ..c.. indicator-power
                     pete  2205 ..c.. xterm
                     pete  2207 ..c.. bash
```

我们可以看到哪些进程当前正在使用我们的 `/home/pete` 目录。`lsof` 和 `fuser` 工具非常相似。熟悉这些工具，并在下次需要跟踪文件或进程时尝试使用它们。

## Exercise

Read the man pages for `lsof` and `fuser`. There is a lot of information that we didn't cover that allows you to have greater flexibility with these tools.

## Quiz Question

列出打开文件及其进程信息的命令是什么？

## Quiz Answer

lsof
