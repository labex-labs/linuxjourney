---
lesson_id: "process-niceness"
course_id: "processes"
lang: "en"
order_index: 8
title: "Niceness"
description: "Learn how nice values influence CPU scheduling weight for ordinary Linux processes."
meta_title: "niceness - Processes"
meta_description: "Discover what is niceness in linux and how it affects process priority. This lesson explains linux process niceness, using the nice and renice commands to manage CPU scheduling and improve system performance."
meta_keywords: "niceness linux, linux niceness, what is niceness in linux, linux process niceness, niceness of process, process priority, nice command, renice command, CPU scheduling"
---

Linux can execute threads simultaneously on different CPU cores and time-share a core among more runnable threads than it can run at once. The scheduler makes those choices according to scheduling policy, priority, affinity, and workload. A nice value is one input for ordinary time-sharing policies.

## Interpreting Nice Values

The conventional nice range is `-20` through `19`:

- A lower value gives a task greater scheduling weight relative to comparable tasks.
- A higher value makes it “nicer” by giving it less relative weight.
- The default is commonly `0`.

Niceness does not reserve a percentage of a CPU or guarantee immediate execution. Its effect is most visible when comparable runnable tasks contend for CPU time. Real-time policies, cgroups, CPU affinity, I/O waits, and other controls can dominate observed behavior.

:::single-choice{#process-niceness-lower-value}
Under the same ordinary scheduling policy, which nice value gives greater relative CPU weight?

::option[`10`]{#process-niceness-value-ten explanation="A positive value is nicer and normally carries less weight than zero or a negative value."}
::option[`19`]{#process-niceness-value-nineteen explanation="This is the nicest end of the conventional range and has relatively low weight."}
::option[`-5`]{#process-niceness-value-minus-five .correct explanation="Lower nice values correspond to greater relative weight among comparable ordinary tasks."}
:::

## Viewing Niceness

In `top`, the `NI` column displays the nice value. You can also request it from `ps`:

```bash
$ ps -o pid,ni,pri,stat,cmd -p 3245
```

`NI` is the user-visible nice value. A `PRI` or similar column can be a derived scheduler priority and its scale varies by tool and scheduling class, so do not assume the two columns are interchangeable.

:::single-choice{#process-niceness-top-column}
Which `top` column normally displays the nice value?

::option[`PID`]{#process-niceness-column-pid explanation="`PID` identifies a process rather than showing its scheduling adjustment."}
::option[`TTY`]{#process-niceness-column-tty explanation="`TTY` identifies a controlling terminal association."}
::option[`NI`]{#process-niceness-column-ni .correct explanation="`NI` is the conventional abbreviation for the process or thread nice value."}
:::

## Starting a Command with `nice`

Use `nice` to launch a new command with an adjusted value:

```bash
$ nice -n 5 long-computation
```

The requested adjustment and accepted syntax can be checked in the local manual. A nonprivileged user can normally make a command nicer by increasing its value. Giving it a lower nice value, and therefore more favorable scheduling weight, requires appropriate privilege or configured resource limits.

:::single-choice{#process-niceness-nice-command}
What does `nice -n 5 long-computation` do?

::option[Starts the command with nice value 5, if permitted.]{#process-niceness-start-five .correct explanation="`nice` launches a new command using the requested scheduling adjustment."}
::option[Changes PID 5 to the lowest possible nice value.]{#process-niceness-pid-five explanation="The operand after `-n` is a nice value, not a PID target."}
::option[Guarantees the command exactly five percent of one CPU.]{#process-niceness-five-percent explanation="Nice values express relative weight and do not reserve fixed CPU percentages."}
:::

## Changing an Existing Process with `renice`

Use `renice` for an already running process:

```bash
$ renice -n 10 -p 3245
```

This requests nice value `10` for PID `3245`. Verify the target first because PIDs can be reused, then confirm the resulting value. Permissions depend on ownership, privilege, resource limits, and system policy. Increasing the nice value is usually allowed for a process you own; reversing that change may not be allowed without privilege.

:::single-choice{#process-niceness-renice-purpose}
Which tool changes the nice value of an existing process?

::option[`nice`]{#process-niceness-tool-nice explanation="`nice` primarily starts a new command with an adjusted value."}
::option[`kill`]{#process-niceness-tool-kill explanation="`kill` sends signals and does not serve as the ordinary niceness editor."}
::option[`renice`]{#process-niceness-tool-renice .correct explanation="`renice` targets an existing PID, process group, or user according to its options."}
:::

The [Manage and Monitor Linux Processes](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864) lab offers a controlled environment for viewing and changing nice values. Compare contending CPU-bound tasks rather than expecting a visible difference from an idle system.

## Summary

You can now interpret and adjust niceness without treating it as a CPU guarantee.

1. Read lower nice values as greater relative scheduling weight.
2. Inspect `NI` separately from derived priority fields.
3. Use `nice` when launching a command.
4. Use `renice` for an existing, verified process.
