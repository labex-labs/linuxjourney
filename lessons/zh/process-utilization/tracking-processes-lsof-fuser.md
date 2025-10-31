---
index: 2
lang: "zh"
title: "lsof 和 fuser"
meta_title: "lsof 和 fuser - 进程占用情况"
meta_description: "探索 Linux 中的 lsof 和 fuser 命令，以识别哪些进程正在使用特定文件。学习如何解决“设备或资源忙碌”错误，比较 fuser 与 lsof，并使用 fuser -k 等选项有效管理打开的文件。"
meta_keywords: "lsof, fuser, fuser 命令，linux fuser, fuser 与 lsof, lsof 与 fuser, fuser -k linux, 打开文件，进程管理，设备忙碌，Linux 命令"
---

## Lesson Content

您是否曾尝试卸载 USB 驱动器时收到“设备或资源忙 (Device or Resource Busy)”错误？这个常见问题发生时，是因为某个进程仍在占用设备上的文件或目录。要解决此问题，您需要找出是哪个进程占用了该资源。用于此任务的两个强大工具是 `lsof` 和 `fuser`。

### 使用 lsof 列出打开的文件

在 Linux 中，几乎所有内容都被视为文件，包括磁盘、管道、网络套接字和设备。`lsof` 命令（“list open files”的缩写）会向您显示所有打开的文件及其使用它们的进程的详细列表。

要查看哪些进程正在使用当前目录（`.`），您可以运行：

```bash
pete@icebox:~$ lsof .
COMMAND    PID  USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
lxsession 1491 pete  cwd    DIR    8,6     4096  131 .
update-no 1796 pete  cwd    DIR    8,6     4096  131 .
nm-applet 1804 pete  cwd    DIR    8,6     4096  131 .
xterm     2205 pete  cwd    DIR    8,6     4096  131 .
bash      2207 pete  cwd    DIR    8,6     4096  131 .
lsof      5914 pete  cwd    DIR    8,6     4096  131 .
```

输出显示了与每个打开文件相关的命令（`COMMAND`）、进程 ID（`PID`）和用户（`USER`）。有了这些信息，您就可以识别出阻止您卸载设备的进程。

### fuser 命令

另一个优秀的工具是 `fuser` 命令（“file user”的缩写）。此实用程序用于识别哪些进程正在使用特定的文件、套接字或文件系统。`linux fuser` 命令是快速查看访问特定资源的进程 PID 的方法。

使用 `-v`（详细）选项会提供更详细的输出：

```bash
pete@icebox:~$ fuser -v .
                     USER        PID ACCESS COMMAND
/home/pete:         pete  1491 ..c.. lxsession
                     pete  1796 ..c.. update-notifier
                     pete  1804 ..c.. nm-applet
                     pete  2205 ..c.. xterm
                     pete  2207 ..c.. bash
```

在这里，我们可以清楚地看到哪些进程正在使用我们的当前目录。`ACCESS` 列显示了文件是如何被使用的（例如，`c` 代表当前目录）。

### 使用 fuser 终止进程

`fuser` 命令的一个关键特性是它能够终止正在使用资源的进程。`fuser -k` 选项会向访问指定文件或文件系统的每个进程发送 `SIGKILL` 信号。这对于卸载忙碌的设备特别有用。

例如，要杀死所有使用挂载点 `/mnt/usb` 的进程，您将运行：

```bash
sudo fuser -k /mnt/usb
```

在 Linux 中使用 `fuser -k` 是一种快速有效释放资源的方法。

### fuser 与 lsof 的比较

那么，您应该何时使用 `fuser` 而不是 `lsof` 呢？

- **`lsof`** 非常适合详细调查。它提供了关于所有打开文件的广泛信息，是复杂故障排除的理想选择。
- **`fuser`** 更直接。它非常适合快速识别并（如果需要）终止特定文件或挂载点上的进程。`fuser command` 通常是解决“设备或资源忙”错误的更快选择。

这两个工具对任何 Linux 用户来说都是必不可少的。熟悉它们可以帮助您高效地管理文件和进程。

## Exercise

实践出真知！以下是一些实践实验，以加强您对管理进程和解决资源冲突的理解：

1.  **[管理和监控 Linux 进程](https://labex.io/zh/labs/comptia-manage-and-monitor-linux-processes-590864)** - 练习与前台和后台进程交互，使用 `ps` 检查它们，使用 `top` 监控资源，并使用 `kill` 终止它们。此实验将帮助您识别和管理可能占用资源的进程，例如 USB 驱动器上的文件。

此实验将帮助您在实际场景中应用这些概念，并建立识别和管理系统进程的信心。

## Quiz Question

什么命令用于列出打开的文件及其相关的进程信息？ (请用英文回答，只使用小写字母)

## Quiz Answer

lsof
