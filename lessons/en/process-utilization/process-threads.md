---
lesson_id: "process-threads"
course_id: "process-utilization"
lang: "en"
order_index: 3
title: "Process Threads"
description: "Learn how Linux threads share process resources and how to inspect them with ps."
meta_title: "Process Threads - Process Utilization"
meta_description: "A guide to Linux process threads. Learn the difference between single-threaded and multi-threaded processes and how to use the ps command to show threads."
meta_keywords: "Linux threads, process threads, ps show threads, ps m, multi-threaded, single-threaded, lightweight process, Linux process management"
---

A thread is an execution flow scheduled within a process. Every running process has at least one thread, and a multithreaded process has several flows that can make progress concurrently.

## Processes and Threads

Threads in one process share resources such as the virtual address space and open file descriptors. Each thread still has its own execution state, including registers and a stack. Sharing makes communication efficient, but it also means an unsynchronized change by one thread can affect the others.

Separate processes normally have distinct address spaces and communicate through explicit interprocess mechanisms. Neither design is automatically faster or safer; the workload and implementation determine the trade-off.

:::single-choice{#threads-shared-resource} Which resource is normally shared by threads in the same process?

::option[The process virtual address space.]{#threads-shared-address-space .correct explanation="Threads can access the same process memory, subject to program synchronization."}
::option[A separate kernel installation for each thread.]{#threads-separate-kernel explanation="All threads use the running system kernel."}
::option[A different filesystem root for every thread.]{#threads-different-root explanation="Threads normally share process filesystem context rather than receiving separate roots."}
:::

## Thread Identifiers

Linux represents each thread as a schedulable task with its own thread ID. The thread-group leader's ID is commonly presented as the process ID, while all members share a thread-group ID. Tools use labels such as `PID`, `TID`, `LWP`, and `SPID`; check the tool's field definitions instead of assuming every label means the same thing.

:::single-choice{#threads-own-scheduling-state} What does each thread maintain independently?

::option[The process's complete open-file table.]{#threads-open-files-shared explanation="Threads in a process normally share open file descriptors."}
::option[The machine's system-wide user database.]{#threads-user-database explanation="Account databases are not private thread state."}
::option[Its execution state and stack.]{#threads-stack-state .correct explanation="A thread needs its own execution context even though process resources are shared."}
:::

## Listing Threads with ps

Use explicit output fields to avoid ambiguous default layouts:

```bash
$ ps -eLo pid,tid,psr,stat,comm
```

On procps `ps`, `-L` shows threads and `-e` selects all processes. `pid` identifies the thread group, `tid` identifies an individual thread, `psr` shows the CPU on which it last ran, and `stat` reports state. To inspect one process:

```bash
$ ps -L -p 1234 -o pid,tid,stat,pcpu,comm
```

Thread listings are snapshots. A thread can exit or change state immediately afterward.

:::single-choice{#threads-ps-one-process} Which command lists threads belonging to PID 1234 with explicit fields?

::option[`ps -p 1234 -o pid,ppid,stat,pcpu,comm`]{#threads-process-only explanation="This output does not request per-thread rows."}
::option[`ps -L -p 1234 -o pid,tid,stat,pcpu,comm`]{#threads-ps-l .correct explanation="The `-L` option requests thread rows for the selected process."}
::option[`ps -e -o pid,user,stat,pcpu,comm`]{#threads-all-processes explanation="This selects processes system-wide without thread IDs."}
:::

## Interpreting Thread Activity

High CPU in one thread can be hidden by a process-wide average. Combine thread-level CPU samples with application logs, stack traces, and profiling tools. Do not attach debuggers or send signals to production tasks without understanding pause, permission, and service impacts.

:::single-choice{#threads-snapshot-limit} Why should a `ps` thread listing not be treated as permanent state?

::option[`ps` creates a replacement thread for every row.]{#threads-ps-creates explanation="The command observes tasks; it does not clone each one it lists."}
::option[Thread IDs are identical on every Linux host.]{#threads-identical-ids explanation="Identifiers are assigned within a running system and are not universal."}
::option[Threads can change state or exit after the snapshot.]{#threads-change-after-snapshot .correct explanation="Process inspection observes a moment in a continuously changing system."}
:::

## Summary

You can now distinguish process resources from per-thread execution state.

1. Recognize that every process has at least one thread.
2. Identify resources shared by threads in one process.
3. List explicit process and thread IDs with `ps -L`.
4. Treat thread output as a snapshot and correlate it with other evidence.
