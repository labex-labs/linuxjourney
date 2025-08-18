---
lang: "zh"
title: "作业控制"
meta_title: "作业控制 - 进程"
meta_description: "学习 Linux 作业控制以管理后台进程。了解 'jobs'、'bg'、'fg' 和 'kill' 命令，以高效使用 shell。开始您的 Linux 之旅！"
meta_keywords: "Linux 作业控制，后台进程，jobs 命令，bg 命令，fg 命令，kill 命令，Linux 教程，Linux 初学者"
---

## Lesson Content

假设您正在一个终端窗口中工作，并且正在运行一个耗时很长的命令。在命令完成之前，您无法与 shell 交互。但是，我们希望继续在我们的机器上工作，所以我们需要保持 shell 打开。幸运的是，我们可以通过作业控制进程的运行方式：

### 将作业发送到后台

在命令后附加一个和号 (`&`) 将使其在后台运行，这样您仍然可以使用 shell。让我们看一个例子：

```bash
sleep 1000 &
sleep 1001 &
sleep 1002 &
```

### 查看所有后台作业

现在您可以查看刚刚发送到后台的作业。

```bash
$ jobs

[1]    Running     sleep 1000 &
[2]-   Running     sleep 1001 &
[3]+   Running     sleep 1002 &
```

这将显示第一列中的作业 ID，然后是状态和运行的命令。作业 ID 旁边的 **+** 表示它是最近启动的后台作业。带有 **-** 的作业是倒数第二个最近的命令。

### 将现有作业发送到后台

如果您已经运行了一个作业并想将其发送到后台，您不必终止它并重新开始。首先，使用 Ctrl-Z 暂停作业，然后运行 **bg** 命令将其发送到后台。

```bash
pete@icebox ~ $ sleep 1003
^Z
[4]+    Stopped     sleep 1003

pete@icebox ~ $ bg
[4]+    sleep 1003 &

pete@icebox ~ $ jobs

[1]    Running     sleep 1000 &
[2]    Running     sleep 1001 &
[3]-   Running     sleep 1002 &
[4]+   Running     sleep 1003 &
```

### 将作业从后台移到前台

要将作业从后台移出，只需指定您想要的作业 ID。如果您不带任何选项运行 `fg`，它将带回最近的后台作业（作业 ID 旁边带有 + 号的作业）。

```bash
fg %1
```

### 终止后台作业

与将作业从后台移出类似，您可以使用相同的形式通过作业 ID 终止进程。

```bash
kill %1
```

## Exercise

在后台和前台之间移动一些作业。

## Quiz Question

用于列出后台作业的命令是什么？

## Quiz Answer

jobs
