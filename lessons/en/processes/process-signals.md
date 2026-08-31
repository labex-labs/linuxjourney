---
lesson_id: "process-signals"
course_id: "processes"
lang: "en"
order_index: 6
title: "Signals"
description: "Learn how Linux generates, blocks, delivers, and handles signals for process control and event notification."
meta_title: "Signals - Processes"
meta_description: "Explore the fundamentals of Linux signals, a key mechanism for process management. Learn how Linux process signals like SIGTERM (signal 15 linux) and SIGKILL work, and understand their OS signal codes."
meta_keywords: "linux signals, linux process signals, signal 15 linux, os sig code, SIGKILL, SIGTERM, SIGINT, process management, linux tutorial"
---

A signal is an asynchronous notification delivered to a process or a particular thread. Signals report events and request actions, but carry only limited information compared with data-oriented interprocess communication mechanisms.

## Where Signals Come From

Signals can originate in several places:

- A terminal can generate `SIGINT` for `Ctrl-C` or `SIGTSTP` for `Ctrl-Z` and direct it to the foreground process group.
- The kernel can generate a synchronous signal such as `SIGSEGV` when a thread makes an invalid memory reference.
- A process can send an authorized signal to another process or process group.
- Timers, child-state changes, and terminal hangups can generate other signals.

The sender must have appropriate permission, normally based on credentials or capabilities. Signals are therefore a kernel-mediated control interface, not unrestricted messages between arbitrary users.

:::single-choice{#process-signals-ctrl-c}
Which signal does a terminal normally generate for `Ctrl-C`?

::option[`SIGTSTP`]{#process-signals-ctrl-c-tstp explanation="`SIGTSTP` is normally associated with the terminal suspend character such as `Ctrl-Z`."}
::option[`SIGCONT`]{#process-signals-ctrl-c-cont explanation="`SIGCONT` resumes a stopped process rather than representing keyboard interruption."}
::option[`SIGINT`]{#process-signals-ctrl-c-int .correct explanation="The terminal interrupt character normally generates `SIGINT` for the foreground process group."}
:::

## Dispositions and Default Actions

Most signals have a process-wide disposition that selects one of three responses:

- perform the signal's defined default action
- ignore the signal
- invoke a user-installed handler

Default actions differ: a signal may terminate, terminate and create a core dump, stop, continue, or be ignored. Catching `SIGTERM` can let a program begin an orderly shutdown, but a handler must follow strict async-signal-safety rules and the program can still delay or decline to exit.

Signal names are more portable and readable than numbers. Although common Linux architectures use `SIGTERM` as 15, do not assume all signal numbers except those guaranteed by the relevant standard are identical everywhere. Use `kill -l` to inspect the local mapping.

:::single-choice{#process-signals-term-behavior}
Why can a process respond gracefully to `SIGTERM`?

::option[It can install a handler for that signal.]{#process-signals-term-handler .correct explanation="Unlike `SIGKILL`, `SIGTERM` can be caught so a program can initiate its own shutdown logic."}
::option[The kernel always saves every open document automatically.]{#process-signals-term-kernel-save explanation="Application cleanup depends on program code; the kernel does not understand and save arbitrary document state."}
::option[`SIGTERM` cannot cause termination by default.]{#process-signals-term-no-default explanation="Its default action is termination when the process has not changed the disposition."}
:::

## Blocking and Pending Signals

Threads have signal masks that can temporarily block delivery of selected signals. A generated blocked signal remains pending until it can be delivered, subject to the rules for standard and real-time signals. Standard signals of the same type can coalesce rather than queue once per occurrence.

In a multithreaded process, a process-directed signal can be delivered to an eligible thread that does not block it; a thread-directed signal targets the specified thread. Correct signal design therefore requires more than checking whether “the process blocked it.”

:::single-choice{#process-signals-blocked-state}
What normally happens when a blockable signal is generated while its target blocks it?

::option[It remains pending until delivery becomes possible.]{#process-signals-pending .correct explanation="Blocking postpones handling; the pending signal can be delivered after it is unblocked."}
::option[It is converted automatically into `SIGKILL`.]{#process-signals-convert-kill explanation="The kernel does not escalate an ordinary blocked signal into an uncatchable signal."}
::option[It changes the target process's user ID.]{#process-signals-change-uid explanation="Signal masks affect delivery and do not alter process credentials."}
:::

## Signals That Cannot Be Handled

`SIGKILL` terminates a process and `SIGSTOP` stops it. Neither signal can be caught, ignored, or blocked. This guarantees that the kernel retains ultimate control, but it also means `SIGKILL` provides no opportunity for application-level cleanup.

Even `SIGKILL` may not make a task disappear instantly from an observer's perspective. A task can be waiting in an uninterruptible kernel operation, and after termination its parent still must reap its status.

:::single-choice{#process-signals-uncatchable-pair}
Which pair cannot be caught, ignored, or blocked?

::option[`SIGKILL` and `SIGSTOP`]{#process-signals-kill-stop .correct explanation="The kernel reserves these two signals so a process cannot override or postpone their fundamental actions."}
::option[`SIGINT` and `SIGTERM`]{#process-signals-int-term explanation="Both can have user-installed handlers and can be blocked."}
::option[`SIGHUP` and `SIGCONT`]{#process-signals-hup-cont explanation="These signals have special semantics but are not the uncatchable pair."}
:::

## Summary

You can now explain the major stages and constraints of Linux signal handling.

1. Identify terminal, kernel, and process-generated signals.
2. Distinguish default actions, ignored signals, and handlers.
3. Relate blocking to pending delivery and thread masks.
4. Remember that `SIGKILL` and `SIGSTOP` cannot be handled or blocked.
