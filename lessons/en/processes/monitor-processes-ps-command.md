---
lesson_id: "monitor-processes-ps-command"
course_id: "processes"
lang: "en"
order_index: 1
title: "ps (Processes)"
description: "Learn how to take process snapshots with `ps` and monitor changing activity with `top`."
meta_title: "ps (Processes) - Processes"
meta_description: "Explore the Linux ps command with our comprehensive guide. Learn how to use the ps -ef command in Linux and other options to view running processes, understand PIDs, and manage system tasks. A perfect start for your Linux Journey."
meta_keywords: "ps command, ps -ef linux, ps -ef command, linux ps -ef, ps -e linux, Linux processes, process ID, PID, top command, linux journey"
---

A process is a running instance of a program, together with its memory, credentials, open resources, and execution state. Linux identifies each live process with a numeric process ID, or PID. A PID is unique among processes that exist at the same time, but the kernel can reuse it after a process exits.

## Taking a Basic Snapshot

Run `ps` without options to see a snapshot selected by the implementation's defaults, commonly processes associated with your current terminal and user:

```text
$ ps
    PID TTY          TIME CMD
  41230 pts/4    00:00:00 bash
  51224 pts/4    00:00:00 ps
```

Typical fields include:

- `PID`: process ID
- `TTY`: controlling terminal, or `?` when none is associated
- `TIME`: accumulated CPU time, not elapsed wall-clock duration
- `CMD`: command name or command line, depending on the selected format

Exact columns and selection defaults vary between `ps` implementations and environments.

:::single-choice{#ps-command-pid-meaning}
What does the `PID` column identify?

::option[The process's current directory number.]{#ps-command-pid-directory explanation="A current directory is a filesystem reference and is not represented by PID."}
::option[The accumulated CPU time in seconds.]{#ps-command-pid-cpu explanation="CPU usage is shown in a separate field such as `TIME`."}
::option[The process ID assigned by the kernel.]{#ps-command-pid-kernel .correct explanation="PID is the numeric identifier used to refer to a live process."}
:::

## Listing Processes with BSD-Style Options

Linux `ps` accepts several option styles. BSD-style options are commonly written without a leading dash:

```bash
$ ps aux
```

In this combination:

- `a` expands selection to processes belonging to other users that have terminals.
- `x` also includes processes without controlling terminals and broadens the selection when combined with `a`.
- `u` selects a user-oriented output format with fields such as `USER`, `%CPU`, `%MEM`, `VSZ`, and `RSS`.

Because option meanings can interact, interpret the complete combination rather than treating every letter as an independent command.

:::single-choice{#ps-command-aux-user-format}
In `ps aux`, which option requests the user-oriented output format?

::option[`u`]{#ps-command-aux-u .correct explanation="The BSD-style `u` option selects a user-oriented set of output columns."}
::option[`x`]{#ps-command-aux-x explanation="The `x` option affects process selection, particularly processes without controlling terminals."}
::option[`a`]{#ps-command-aux-a explanation="The `a` option expands selection beyond only the current user's terminal processes."}
:::

## Using Standard-Style Options

The widely used standard-style command `ps -ef` writes options with a leading dash:

```bash
$ ps -ef
```

- `-e` selects every process visible to the caller.
- `-f` requests a full-format listing.

The output commonly includes `UID`, `PID`, `PPID`, start time, and command information. `PPID` is the parent process ID. This listing is not inherently hierarchical; use an option such as `--forest` where supported, or a dedicated tree viewer such as `pstree`, when parent-child layout matters.

:::single-choice{#ps-command-ef-selection}
What does `-e` request in `ps -ef`?

::option[An update every second until interrupted.]{#ps-command-e-refresh explanation="`ps` produces a snapshot; continuous refresh is a feature of tools such as `top`."}
::option[A selection containing every process visible to the caller.]{#ps-command-e-every .correct explanation="The standard-style `-e` option broadens the snapshot to all selectable processes."}
::option[Only processes whose command ended with an error.]{#ps-command-e-errors explanation="Process selection is not based on a command's eventual exit status."}
:::

## Monitoring Activity over Time

`ps` exits after producing one snapshot. Use `top` for an interactive view that refreshes periodically:

```bash
$ top
```

`top` helps identify changing CPU and memory consumers, but its values are samples and can fluctuate. Confirm a suspected problem across multiple observations and relate percentages to the machine's CPU count, memory accounting, and workload.

:::single-choice{#ps-command-snapshot-versus-top}
Which tool introduced here refreshes its process display periodically by default?

::option[`top`]{#ps-command-top-refresh .correct explanation="`top` is an interactive monitor that updates its display at intervals."}
::option[`ps -ef`]{#ps-command-ps-ef-snapshot explanation="This command prints a full-format process snapshot and then exits."}
::option[`ls -l`]{#ps-command-ls-files explanation="`ls -l` displays filesystem entries rather than a live process monitor."}
:::

For hands-on practice, use [Manage and Monitor Linux Processes](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864) to compare snapshots with an interactive monitor, or explore sorting and filtering in the [Linux `top` Command](https://labex.io/labs/linux-linux-top-command-real-time-system-monitoring-388500) lab.

## Summary

You can now choose a process view and interpret its basic identifiers.

1. Treat a PID as a reusable identifier for a currently live process.
2. Use plain `ps` for a small default snapshot.
3. Use `ps aux` or `ps -ef` for broader selections and richer columns.
4. Use `top` when changes over time matter.
