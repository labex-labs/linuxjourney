---
index: 3
lang: "zh"
title: "系统调用"
meta_title: "系统调用 - 内核"
meta_description: "探索 Linux 中系统调用的基础知识。了解用户空间进程如何使用系统调用（syscalls）向内核请求服务、切换模式以及系统调用表的工作原理。使用 `strace` 查看实际的系统调用。"
meta_keywords: "系统调用 linux, 系统调用，syscall 表，内核模式，用户模式，strace, linux 内核，syscall API"
---

## Lesson Content

想象你正在参加一场大型音乐会。要从普通观众区进入专属的后台区域，你不能随便走过去。你需要一张特殊的通行证，它允许你通过一个特定的、有守卫的门。在计算的世界里，**系统调用**就是那些特殊的通行证。

### 什么是系统调用？

系统调用，通常缩写为 syscalls，为用户空间进程提供了一种直接向内核请求服务的方式。内核通过系统调用 API 暴露了一组服务。这些服务对于读取或写入文件、管理内存或处理网络连接等操作至关重要。可用系统调用的数量是固定的；你不能随意添加新的。你的系统维护一个 `syscall table`（系统调用表），其中每个系统调用都用唯一的 ID 注册。

### Linux 中的系统调用机制

当你运行像 `ls` 这样的程序时，其中的代码不会直接执行 **system call linux** 命令。相反，它会使用一个充当包装器的库函数。这个包装器函数会设置必要的参数，然后触发一个软件中断，或者说一个“陷阱”（trap）。

这个陷阱会指示处理器从非特权的**用户模式**切换到特权的**内核模式**。进入内核模式后，系统调用处理程序会接管。它使用唯一的 ID 在 `syscall table` 中查找请求的函数并执行它。例如，用于查询文件状态的 `stat()` 系统调用就是以这种方式找到并运行的。内核完成任务后，会将上下文切换回用户模式，并向你的进程返回一个状态码，指示成功或错误。

### 使用 strace 查看系统调用

你可以使用 `strace` 命令实时观察进程发出的系统调用。这个工具对于调试和理解程序如何与内核交互非常有用。

要查看 `ls` 命令发出的系统调用，你可以运行：

```bash
strace ls
```

这将输出 `ls` 在执行期间执行的每一个系统调用的详细列表。

## Exercise

实践造就完美！虽然系统调用的内部工作原理很复杂，但理解用户空间程序如何与内核交互是基础性的。掌握这种交互的最佳方法是练习执行这些底层操作的命令。以下是一些实践实验室，用于加强你对严重依赖系统调用的文件系统交互的理解：

1. **[在 Linux 中导航文件系统](https://labex.io/zh/labs/comptia-navigate-the-filesystem-in-linux-590971)** - 练习 `ls`、`cd` 和 `pwd` 等基本命令，以便在 Linux 文件系统中移动和检查，直接与内核的文件系统服务交互。
2. **[在 Linux 中管理文件和目录](https://labex.io/zh/labs/comptia-manage-files-and-directories-in-linux-590835)** - 学习使用 `mkdir`、`rm`、`cp` 和 `mv` 等命令创建、删除、复制和移动文件和目录，所有这些操作都涉及系统调用来执行其动作。
3. **[在 Linux 中查找文件和命令](https://labex.io/zh/labs/comptia-find-files-and-commands-in-linux-590834)** - 掌握使用 `find`、`whereis` 和 `which` 定位文件和命令的技巧，进一步说明用户命令如何利用内核服务与文件系统进行交互。

这些实验室将帮助你在真实场景中应用文件系统交互的概念，并增强你对隐含依赖于系统调用的基本 Linux 操作的信心。

## Quiz Question

What is used to switch from user mode to kernel mode? Please answer in English, using two words.

## Quiz Answer

System call
