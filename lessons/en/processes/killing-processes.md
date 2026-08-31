---
lesson_id: "killing-processes"
course_id: "processes"
lang: "en"
order_index: 7
title: "kill (Terminate)"
description: "Learn how to identify a process and send an appropriate signal with `kill` using a safe escalation sequence."
meta_title: "kill (Terminate) - Processes"
meta_description: "Master the Linux kill command to manage and terminate processes. This guide covers the differences between kill vs terminate, and explains signals like kill sigterm (SIGTERM), SIGKILL, and kill sighup (SIGHUP)."
meta_keywords: "kill command, kill sigterm, kill sighup, linux kill -0, kill vs terminate, kill -15 linux, SIGTERM, SIGKILL, process management, terminate process"
---

The `kill` command sends a signal to a process or process group. Its name is historical: the requested signal might terminate, stop, continue, or prompt some application-defined action. Always confirm the exact target and understand the program's documented signal behavior before sending one.

## Requesting an Orderly Termination

With only a PID, `kill` sends `SIGTERM` by default:

```bash
$ kill 12445
```

Prefer the symbolic name when specifying a signal explicitly:

```bash
$ kill -TERM 12445
```

`SIGTERM` has a default action of termination, but a program can catch or ignore it. A well-designed service can use a handler to stop accepting work, save appropriate state, and release application resources. That is a possibility, not a guarantee of immediate or successful cleanup.

:::single-choice{#killing-processes-default-signal}
Which signal does `kill PID` request by default?

::option[`SIGKILL`]{#killing-processes-default-kill explanation="The forceful uncatchable signal must be selected explicitly."}
::option[`SIGTERM`]{#killing-processes-default-term .correct explanation="Without another signal operand, `kill` sends the standard termination request."}
::option[`SIGSTOP`]{#killing-processes-default-stop explanation="Stopping a process is not the default action requested by `kill`."}
:::

## Verifying the Target

PIDs can be reused, so a stale PID can identify a different process later. Inspect the live target immediately before acting:

```bash
$ ps -p 12445 -o pid,ppid,user,lstart,stat,cmd
```

Check its user, start time, command, parent, service ownership, and operational role. If a service manager owns the process, use that manager's stop or reload command when possible so it can maintain correct state and avoid immediately restarting the child.

You may signal processes you own, subject to credential rules. Signaling another user's process normally requires appropriate privilege. Do not use a broad name-based command until you have reviewed every match.

:::single-choice{#killing-processes-pid-reuse}
Why should you inspect a PID immediately before signaling it?

::option[A PID changes every time the process reads a file.]{#killing-processes-pid-read explanation="A live process normally retains the same PID throughout its lifetime."}
::option[The kernel can reuse a PID after its earlier process exits.]{#killing-processes-pid-reused .correct explanation="A remembered numeric PID can later refer to a different live process."}
::option[`kill` accepts command names but not numeric identifiers.]{#killing-processes-no-numeric explanation="A numeric PID is the ordinary target operand for `kill`."}
:::

## Checking Signal Permission with Signal Zero

Signal number zero performs error checking without delivering a real signal:

```bash
$ kill -0 12445
```

A successful result means a process with that PID exists and the caller is permitted to signal it at that instant. Failure is ambiguous: the process might not exist, or the caller might lack permission. Examine the error and exit status rather than translating every failure into “not running.” It is also only a momentary check and cannot eliminate a later PID-reuse race.

:::single-choice{#killing-processes-signal-zero}
What does successful `kill -0 PID` establish at that moment?

::option[The process has completed all cleanup and exited.]{#killing-processes-zero-exited explanation="Success indicates a signalable live target, not completed termination."}
::option[The process will retain that PID permanently.]{#killing-processes-zero-permanent explanation="The check is instantaneous and PIDs can be reused after exit."}
::option[The process exists and the caller may signal it.]{#killing-processes-zero-permitted .correct explanation="Signal zero checks target existence and authorization without delivering a normal signal."}
:::

## Escalating Only When Necessary

If an authorized target does not terminate after `SIGTERM`, allow a workload-appropriate timeout and investigate why. Then, when forced termination is justified, send:

```bash
$ kill -KILL 12445
```

`SIGKILL` cannot be caught, ignored, or blocked, so the program cannot perform application-level cleanup. It can leave incomplete transactions, temporary state, or recovery work for other components. Use it as an escalation, not a routine first step.

Other signals are meaningful only according to the receiving program's contract. `SIGHUP` often requests configuration reload, but some programs retain its default termination behavior. `SIGSTOP` pauses without cleanup and `SIGCONT` resumes a stopped process.

:::single-choice{#killing-processes-kill-tradeoff}
What is the main operational drawback of `SIGKILL`?

::option[It can be handled only by the process owner.]{#killing-processes-kill-owner-handler explanation="No target process can install a handler for `SIGKILL`."}
::option[It pauses the process but never terminates it.]{#killing-processes-kill-pauses explanation="`SIGSTOP` pauses; `SIGKILL` terminates."}
::option[It gives the program no opportunity for application-level cleanup.]{#killing-processes-kill-no-cleanup .correct explanation="The kernel enforces termination without invoking a user-space signal handler."}
:::

Practice signal selection only on processes you started in an isolated environment. The [Manage and Monitor Linux Processes](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864) lab provides a controlled workflow for inspection and termination.

## Summary

You can now send process signals with a deliberate, verifiable workflow.

1. Confirm the live target and its supervisor before acting.
2. Use `SIGTERM` as the normal termination request.
3. Interpret signal zero as a momentary existence-and-permission check.
4. Reserve `SIGKILL` for justified escalation after investigation.
