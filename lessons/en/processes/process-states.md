---
lesson_id: "process-states"
course_id: "processes"
lang: "en"
order_index: 9
title: "Process States"
description: "Learn how to interpret common Linux process-state codes in `ps` snapshots."
meta_title: "Process States - Processes"
meta_description: "A comprehensive guide to Linux process states. Learn about the different process states in Linux (R, S, D, Z, T) and how to interpret them using the `ps` command."
meta_keywords: "linux process states, process states in linux, linux process state, process state in linux, linux process states explained, ps command, STAT codes, process management"
---

A Linux task moves between execution states as it runs, waits, stops, and exits. The `STAT` field from `ps` captures one moment, so repeated observations are more useful than a single letter when diagnosing behavior.

```bash
$ ps -o pid,ppid,stat,wchan:24,cmd
```

The first character in `STAT` is the primary state. Additional characters are modifiers describing properties such as session leadership or foreground process-group membership. Consult the local `ps` manual for the complete set.

## Running and Interruptible Sleep

- `R` means running or runnable. The task is executing on a CPU or waiting in a run queue for CPU time.
- `S` means interruptible sleep. The task is waiting for an event and can be awakened by an appropriate signal or event.

Sleeping is normal. Interactive programs and services spend much of their time waiting for input, timers, network traffic, locks, or other events rather than consuming CPU continuously.

:::single-choice{#process-states-runnable-code}
What does primary state `R` mean?

::option[Running on a CPU or ready to run.]{#process-states-r-running .correct explanation="`R` combines currently executing and runnable tasks waiting for CPU service."}
::option[Reaped after its parent collected status.]{#process-states-r-reaped explanation="A fully reaped process no longer appears as a normal process-table entry."}
::option[Waiting in uninterruptible sleep.]{#process-states-r-uninterruptible explanation="Uninterruptible sleep is represented by `D`."}
:::

:::single-choice{#process-states-interruptible-code}
Which primary state represents interruptible sleep?

::option[`D`]{#process-states-sleep-d explanation="`D` denotes uninterruptible sleep."}
::option[`Z`]{#process-states-sleep-z explanation="`Z` denotes an exited child whose status has not been reaped."}
::option[`S`]{#process-states-sleep-s .correct explanation="`S` is the conventional `ps` code for interruptible waiting."}
:::

## Uninterruptible Sleep

`D` means uninterruptible sleep, commonly while the task waits in a kernel operation such as some storage or network-filesystem I/O. The task does not act on ordinary signals until it leaves that wait; a signal can remain pending in the meantime.

A brief `D` state can be normal. Persistent or numerous `D` tasks can indicate slow, unavailable, or faulty I/O, but the state alone does not identify the cause. Inspect the wait channel, kernel logs, storage and network health, and the relevant subsystem before drawing conclusions.

:::single-choice{#process-states-uninterruptible-code}
Which primary state denotes uninterruptible sleep?

::option[`T`]{#process-states-d-stopped explanation="`T` identifies a stopped task."}
::option[`D`]{#process-states-d-uninterruptible .correct explanation="`D` is used for a task waiting in an uninterruptible kernel sleep."}
::option[`R`]{#process-states-d-runnable explanation="`R` identifies an executing or runnable task."}
:::

## Stopped and Zombie States

- `T` normally means stopped by job-control action, such as `SIGTSTP`, or by `SIGSTOP`. Some tools use lowercase `t` for a tracing stop.
- `Z` means zombie: the process has exited, but its parent has not yet collected the termination record.

Resume a job-control stop with `SIGCONT` when appropriate. A zombie cannot be resumed or killed because it is no longer executing; its parent or an adopting reaper must collect it.

:::single-choice{#process-states-zombie-code}
What does primary state `Z` identify?

::option[An exited process whose termination record awaits reaping.]{#process-states-z-zombie .correct explanation="A zombie retains minimal parent-visible status after execution has ended."}
::option[A process paused by a terminal suspend signal.]{#process-states-z-terminal-stop explanation="A job-control stop is normally shown as `T`."}
::option[A process currently using an entire CPU core.]{#process-states-z-cpu explanation="An actively running task is represented by `R`, while a zombie executes no instructions."}
:::

## Reading States in Context

State codes are observations, not diagnoses. Combine them with elapsed time, CPU use, wait channels, parent relationships, logs, and repeated samples. A task can switch states between the instant the kernel reports it and the instant you read the screen.

The [Manage and Monitor Linux Processes](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864) lab provides a safe environment for observing foreground, sleeping, stopped, and terminated tasks.

## Summary

You can now interpret the most common primary process states.

1. Read `R` as running or runnable and `S` as interruptible sleep.
2. Investigate persistent `D` as a wait symptom rather than a diagnosis.
3. Distinguish stopped `T` from exited, unreaped `Z`.
4. Use repeated observations and surrounding evidence.
