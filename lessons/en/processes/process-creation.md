---
lesson_id: "process-creation"
course_id: "processes"
lang: "en"
order_index: 4
title: "Process Creation"
description: "Learn how fork, exec, PIDs, and parent relationships participate in Linux process creation."
meta_title: "Process Creation - Processes"
meta_description: "Explore the fundamentals of process creation in Linux. This guide covers the fork and execve system calls, parent/child relationships (PID and PPID), and the role of the init process. Learn how to create a process in Linux and understand the core concepts of process creation in the operating system."
meta_keywords: "process creation in linux, linux process creation, create a process in linux, process creation in operating system, process creation, fork, execve, PID, PPID, init process, Linux processes"
---

Linux processes form parent-child relationships. A shell commonly starts an external command by creating a child process and arranging for that child to execute the requested program. The classic explanation separates this work into `fork` and `exec` operations.

## Creating a Child with `fork`

The `fork()` system call creates a child process based on the calling process. Parent and child continue from the return point of `fork`, but receive different return values and have different PIDs.

The child gets logically separate process state. Linux can initially share physical memory pages using copy-on-write, copying a page only when one process modifies it. Open file descriptors are inherited and refer to the same underlying open file descriptions, so details such as file offsets can remain shared.

:::single-choice{#process-creation-fork-result}
What does a successful `fork()` create?

::option[A replacement program inside the same process only.]{#process-creation-fork-replacement explanation="Replacing the current program image is the role of an `exec` operation."}
::option[A child process with a new PID.]{#process-creation-fork-child .correct explanation="`fork()` establishes a separate child process and parent-child relationship."}
::option[A permanent copy of every physical memory page immediately.]{#process-creation-fork-full-copy explanation="Linux commonly uses copy-on-write rather than eagerly duplicating all physical pages."}
:::

## Replacing a Program with `execve`

An `execve()` call loads a new program into the calling process. On success, it replaces the process image and does not return to the old program. The PID remains the same because `execve()` does not create a new process.

Many shell commands therefore follow a fork-exec pattern:

1. The shell creates a child.
2. The child prepares redirections and other execution state.
3. The child executes the requested program.
4. The shell waits or continues, depending on foreground or background execution.

Libraries and applications can expose higher-level interfaces such as `posix_spawn()`, and Linux has additional primitives such as `clone()`. The familiar fork-exec model remains useful without being the only possible interface.

:::single-choice{#process-creation-exec-pid}
What happens to a process's PID after a successful `execve()`?

::option[It becomes identical to the parent PID.]{#process-creation-exec-parent-pid explanation="Parent and child retain separate process IDs."}
::option[It remains the same while the program image is replaced.]{#process-creation-exec-same-pid .correct explanation="`execve()` transforms the calling process rather than creating another process."}
::option[It is removed before the new program starts.]{#process-creation-exec-pid-removed explanation="The existing process continues under its PID with new code, data, stack, and related program state."}
:::

## Inspecting Parent and Child IDs

`PID` identifies the process, while `PPID` identifies its parent. Request those fields explicitly:

```bash
$ ps -o pid,ppid,stat,cmd
```

If a shell starts `ps`, the shell's PID will normally appear as the `PPID` of that `ps` process. Timing matters: short-lived processes may exit before a separate observation captures them.

:::single-choice{#process-creation-ppid}
What does `PPID` represent in a process listing?

::option[The previous PID formerly assigned to the process.]{#process-creation-previous-pid explanation="PIDs can be reused, but `PPID` does not record identifier history."}
::option[The process's scheduling priority identifier.]{#process-creation-priority-id explanation="Scheduling priority is represented by other fields such as priority or nice value."}
::option[The process ID of the parent process.]{#process-creation-parent-pid .correct explanation="PPID records the process's current parent relationship."}
:::

## PID 1 and Reparenting

The kernel starts the first user-space process with PID 1. Depending on the system, it may be `systemd`, another init implementation, or a small init inside a container or PID namespace. PID 1 starts and supervises parts of the user-space environment and has special signal and orphan-reaping responsibilities.

When a parent exits before its child, the child is reparented to an appropriate subreaper or the init process in its PID namespace. It does not need to terminate merely because its original parent ended.

:::single-choice{#process-creation-pid-one}
Which statement about PID 1 is accurate?

::option[It must always be a program whose executable name is exactly `init`.]{#process-creation-pid-one-name explanation="The implementation can be `systemd`, another init, or a container-specific program."}
::option[It is the parent that directly created every process currently running.]{#process-creation-pid-one-direct explanation="Most processes are created through many generations of intermediate parents."}
::option[It is the first process in its PID namespace and has init-like responsibilities.]{#process-creation-pid-one-init .correct explanation="PID 1 anchors user-space process supervision and reaping within a PID namespace."}
:::

The [Manage and Monitor Linux Processes](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864) lab lets you observe parent and child IDs while running foreground and background commands.

## Summary

You can now trace the classic Linux process-creation sequence.

1. Use `fork()` to create a child with a distinct PID.
2. Use `execve()` to replace a process image without changing its PID.
3. Read PID and PPID to identify parent-child relationships.
4. Recognize PID 1 and subreapers as destinations for reparented children.
