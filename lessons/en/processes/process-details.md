---
lesson_id: "process-details"
course_id: "processes"
lang: "en"
order_index: 3
title: "Process Details"
description: "Learn what state and resources distinguish a running process from a program stored on disk."
meta_title: "Process Details - Processes"
meta_description: "Explore the fundamentals of Linux process details. This guide for beginners explains what a process is, how the Linux kernel handles process management, and allocates system resources like CPU and memory."
meta_keywords: "Linux process, process details, kernel, process management, system resources, ps aux, CPU, memory, Linux tutorial, beginner guide"
---

A program is executable code and data stored in a file. A process is a live execution context: it includes mapped code, memory, credentials, open file descriptors, signal state, scheduling information, and one or more threads. The same program can have many independent process instances.

## Program Instances and PIDs

For example, start `cat` without operands in two terminals. Each instance waits for input and has its own process ID:

```bash
$ pgrep -a cat
18420 cat
18457 cat
```

Both processes execute the same program, but they can have different input streams, memory contents, credentials, working directories, and lifetimes. A PID identifies one live process at a time and can later be reused after that process exits.

:::single-choice{#process-details-program-versus-process} What distinguishes two running instances of the same program?

::option[The executable file must be copied once for each instance.]{#process-details-copied-executable explanation="Multiple processes can map and share the same executable file's code pages without duplicating the file."}
::option[Only one instance can have memory or open files.]{#process-details-one-instance-resources explanation="Every process can have its own memory mappings and file-descriptor table."}
::option[Each instance has its own process context and PID.]{#process-details-independent-context .correct explanation="Separate executions receive distinct live process state even when their executable code originates from the same file."}
:::

## State Tracked by the Kernel

The kernel maintains the information required to schedule and control each process, including:

- process and parent identifiers
- user and group credentials
- virtual memory mappings
- open file descriptors and current directory
- signal dispositions and pending signals
- scheduling policy, priority, and execution state
- accounting data such as CPU time

Some underlying resources can be shared. Related processes may share mapped memory, and threads in one process share an address space and many process-wide resources. A process therefore provides isolation boundaries without implying that every byte or kernel object is physically private.

:::single-choice{#process-details-kernel-state} Which component maintains scheduling and credential state for Linux processes?

::option[The kernel.]{#process-details-kernel .correct explanation="The kernel tracks process state and applies scheduling, memory, signal, and access-control rules."}
::option[The executable file's directory.]{#process-details-directory explanation="A directory stores a name-to-inode mapping and does not schedule running processes."}
::option[The user's terminal emulator alone.]{#process-details-terminal explanation="A terminal can interact with processes, but process management remains a kernel responsibility."}
:::

## CPU Scheduling and Memory

Runnable threads compete for CPU time. The kernel scheduler chooses which thread runs on which CPU according to scheduling class, priority, CPU affinity, load, and policy. This is not a promise that every process receives an equal share.

Each process normally sees a virtual address space. The kernel and hardware map virtual addresses to physical memory or other backing storage, enforce protections, and can share pages where appropriate. A memory figure in `ps` or `top` is therefore not automatically the amount of unique physical RAM attributable to that process.

:::single-choice{#process-details-scheduler-role} What does the Linux scheduler select?

::option[Which runnable thread executes on an available CPU.]{#process-details-runnable-thread .correct explanation="Scheduling policy chooses among runnable execution contexts and assigns CPU time."}
::option[Which file owner is recorded when a disk is formatted.]{#process-details-format-owner explanation="Filesystem ownership is unrelated to CPU scheduling."}
::option[Which command line a user is allowed to type.]{#process-details-command-entry explanation="The scheduler manages execution time rather than interactive command syntax."}
:::

## Process Exit and Resource Cleanup

When a process exits, the kernel releases most of its private resources, closes remaining descriptors, and records termination information for its parent. A small process-table record can remain as a zombie until the parent retrieves the exit status. This means “the process has finished executing” and “every trace has disappeared from the process table” are not always simultaneous.

:::single-choice{#process-details-exit-status} Why can an exited process briefly remain as a zombie?

::option[It is still executing instructions with full memory allocated.]{#process-details-zombie-running explanation="A zombie has completed execution and no longer retains a normal running address space."}
::option[Its parent has not yet collected the recorded termination status.]{#process-details-parent-wait .correct explanation="The kernel retains minimal exit information until the parent performs a wait operation."}
::option[Its executable file is permanently locked by the kernel.]{#process-details-zombie-file-lock explanation="Zombie state is about parent-child exit accounting, not a permanent executable lock."}
:::

Use the [Manage and Monitor Linux Processes](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864) lab to start multiple instances and compare their PIDs and states. The [Linux `top` Command](https://labex.io/labs/linux-linux-top-command-real-time-system-monitoring-388500) lab provides a changing view of scheduling and resource metrics.

## Summary

You can now describe a process as more than a program file.

1. Distinguish stored executable code from a live process instance.
2. Identify the state and resources tracked by the kernel.
3. Relate scheduling to runnable threads rather than equal shares.
4. Recognize that exit status can remain until the parent collects it.
