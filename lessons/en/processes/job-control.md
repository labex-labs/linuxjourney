---
lesson_id: "job-control"
course_id: "processes"
lang: "en"
order_index: 11
title: "Job Control"
description: "Learn how an interactive shell manages foreground, background, and stopped jobs."
meta_title: "Job Control - Processes"
meta_description: "Explore our Linux tutorial on job control to effectively manage background processes. Learn to use the jobs, bg, fg, and kill commands for powerful shell multitasking."
meta_keywords: "Linux job control, background processes, jobs command, bg command, fg command, kill command, Linux tutorial, beginner Linux"
---

Interactive shells use job control to coordinate pipelines within one terminal session. A job can contain one process or an entire pipeline, normally grouped into a process group so the terminal and shell can act on it as a unit.

## Starting a Background Job

Append `&` to start a pipeline asynchronously:

```bash
$ sleep 1000 &
[1] 18420
```

The shell returns a prompt without waiting for the job to finish. Background status does not automatically redirect output, detach the controlling terminal, or make the job survive logout. Redirect input and output explicitly when required, and use a service manager, scheduler, or terminal multiplexer for work that must outlive the interactive shell.

A background job that attempts to read from the controlling terminal is normally stopped with `SIGTTIN` because it is not the terminal's foreground process group.

:::single-choice{#job-control-ampersand-effect} What does a trailing `&` ask an interactive shell to do?

::option[Guarantee that the job survives logout and system restart.]{#job-control-survive-restart explanation="Backgrounding alone provides neither durable supervision nor restart persistence."}
::option[Run the pipeline as a background job without waiting before the next prompt.]{#job-control-background-job .correct explanation="The shell starts the job asynchronously and remains available for more commands."}
::option[Discard the job's standard output and errors.]{#job-control-discard-output explanation="Unless redirected, a background job can still write to the terminal."}
:::

## Listing Shell Jobs

The `jobs` builtin lists jobs known to the current shell:

```text
$ jobs
[1]    Running    sleep 1000 &
[2]-   Running    sleep 1001 &
[3]+   Stopped    sleep 1002
```

The bracketed number is a shell job ID, not a PID. A `%` prefix forms a job specification such as `%1`. The `+` marker identifies the current job selected by many commands when no operand is given; `-` identifies the previous job.

Because the job table belongs to one shell, another terminal's shell normally cannot list or address these jobs through its own `jobs`, `fg`, or `bg` builtins.

:::single-choice{#job-control-jobs-scope} What does the `jobs` builtin list?

::option[Jobs tracked by the current shell session.]{#job-control-jobs-current-shell .correct explanation="Job IDs and state are maintained by the interactive shell that started or adopted those jobs."}
::option[Every process currently visible on the system.]{#job-control-jobs-all-processes explanation="System-wide process inspection belongs to tools such as `ps`; the shell job table is narrower."}
::option[Only services started during system boot.]{#job-control-jobs-boot-services explanation="Boot services are normally supervised by a service manager, not the interactive shell job table."}
:::

## Stopping and Continuing a Job

While a job is in the foreground, pressing `Ctrl-Z` normally makes the terminal send `SIGTSTP` to its foreground process group. The shell regains control after the job stops:

```text
$ sleep 1002
^Z
[3]+  Stopped    sleep 1002
```

Continue the current stopped job in the background with:

```bash
$ bg
```

`bg` sends a continuation signal and leaves the job outside the terminal foreground. It is useful only for a stopped job; a command already running in the background does not need to be resumed.

:::single-choice{#job-control-bg-purpose} What does `bg %3` do to stopped job 3?

::option[Moves its files into a directory named `bg`.]{#job-control-bg-files explanation="`bg` is a shell job-control builtin and does not move filesystem objects."}
::option[Continues it as a background job.]{#job-control-bg-continue .correct explanation="The shell resumes the selected stopped job without assigning it the terminal foreground."}
::option[Terminates it with `SIGKILL`.]{#job-control-bg-kill explanation="The builtin continues the job rather than terminating it."}
:::

## Moving a Job to the Foreground

Use `fg` with a job specification to make a job the terminal's foreground process group and wait for it:

```bash
$ fg %1
```

Without an operand, `fg` normally selects the current job marked `+`. A stopped job is continued as it enters the foreground.

:::single-choice{#job-control-fg-effect} What does `fg %1` do?

::option[Assigns job 1 to the terminal foreground and waits for it.]{#job-control-fg-foreground .correct explanation="The shell foregrounds the selected job so it can interact with the terminal."}
::option[Changes job 1 into PID 1.]{#job-control-fg-pid-one explanation="A shell job ID does not replace or rewrite process IDs."}
::option[Starts a second copy of job 1 in the background.]{#job-control-fg-copy explanation="`fg` operates on the existing job rather than creating a duplicate."}
:::

## Signaling a Job

Shells let `kill` accept a job specification:

```bash
$ kill -TERM %1
```

This normally signals the job's process group rather than just one pipeline member. Inspect the selected job first and use `SIGTERM` before considering forceful escalation. Job specifications are shell syntax; scripts and external tools more commonly work with verified PIDs or process-group IDs.

:::single-choice{#job-control-job-specification} Which operand refers to shell job 1 rather than process ID 1?

::option[`1`]{#job-control-plain-one explanation="A plain numeric operand to `kill` is normally interpreted as a PID."}
::option[`#1`]{#job-control-hash-one explanation="A hash prefix is not the introduced syntax for a shell job ID."}
::option[`%1`]{#job-control-percent-one .correct explanation="The percent prefix identifies a shell job specification."}
:::

Practice these operations with harmless commands such as `sleep` in the [Manage and Monitor Linux Processes](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864) lab.

## Summary

You can now move jobs deliberately between shell-controlled states.

1. Use `&` to start a background job without automatic detachment.
2. Use `jobs` to inspect the current shell's job table.
3. Stop with `Ctrl-Z` and continue in the background with `bg`.
4. Return a selected job to the terminal with `fg`.
5. Address shell jobs with `%JOB_ID` when sending signals.
