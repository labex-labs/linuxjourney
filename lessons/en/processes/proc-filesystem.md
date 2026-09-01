---
lesson_id: "proc-filesystem"
course_id: "processes"
lang: "en"
order_index: 10
title: "/proc Filesystem"
description: "Learn how Linux exposes live process and kernel information through the virtual `/proc` filesystem."
meta_title: "/proc filesystem - Processes"
meta_description: "Discover the Linux /proc filesystem, a virtual directory that provides a dashboard-like view into the kernel and running processes. Learn how to access extra process details beyond standard commands."
meta_keywords: "/proc filesystem, linux proc, process information, linux proc extras, system dashboard, Linux processes, kernel information"
---

Linux commonly mounts `procfs` at `/proc`. This virtual filesystem presents kernel-generated interfaces as files and directories; its contents are not ordinary persistent files stored on disk. It exposes process state as well as selected system-wide kernel information.

## Finding Process Directories

List the mount and top-level entries with:

```bash
$ findmnt /proc
$ ls /proc
```

Numeric directory names correspond to process IDs visible in the caller's PID namespace. For example, `/proc/12345` represents PID 12345 at the instant it exists. `/proc/self` is a symbolic link that resolves to the observing process's own directory, and `/proc/thread-self` identifies the current thread.

Visibility and access depend on credentials, namespaces, security policy, and procfs mount options such as `hidepid`. A process can exit between listing a directory and opening one of its files, so disappearance is a normal race that inspection tools must handle.

:::single-choice{#proc-filesystem-numeric-directory} What does numeric directory `/proc/12345` normally represent?

::option[The disk block numbered 12345.]{#proc-filesystem-disk-block explanation="`/proc` is a virtual kernel interface, not a directory of raw disk blocks."}
::option[The process currently visible with PID 12345.]{#proc-filesystem-pid-directory .correct explanation="Per-process procfs data is grouped under a directory named for the visible PID."}
::option[The user account whose UID is 12345.]{#proc-filesystem-user-directory explanation="The numeric top-level process directories are keyed by PID rather than UID."}
:::

## Reading Process Information

Inspect a process status file when permissions allow:

```bash
$ less /proc/12345/status
```

It includes fields such as process name, state, IDs, credentials, memory counters, capabilities, and signal masks. Other useful entries include:

- `/proc/12345/cmdline`: command-line arguments separated by null bytes
- `/proc/12345/environ`: environment entries, access-controlled and potentially sensitive
- `/proc/12345/fd/`: symbolic links representing open file descriptors
- `/proc/12345/maps`: current memory mappings
- `/proc/12345/cwd`: symbolic link to the current working directory

Treat these as changing observations. Fields can differ by kernel version, a process can change state during a multi-file read, and some counters have subtleties not captured by their names alone.

:::single-choice{#proc-filesystem-status-file} Which path contains a readable field-oriented summary for PID 12345?

::option[`/proc/status/12345`]{#proc-filesystem-status-reversed explanation="Per-process files live inside the PID-named directory, not under a top-level `status` directory."}
::option[`/proc/12345/status`]{#proc-filesystem-process-status .correct explanation="The per-process `status` interface presents identifiers, state, memory, signal, and credential fields."}
::option[`/proc/cpuinfo/12345`]{#proc-filesystem-cpuinfo-pid explanation="`/proc/cpuinfo` is a system-wide interface and not a directory of per-PID status files."}
:::

## Reading System-Wide Interfaces

Not every `/proc` entry belongs to a process. Examples include:

- `/proc/cpuinfo` for kernel-reported CPU information
- `/proc/meminfo` for system memory counters
- `/proc/mounts` for the current process's view of mounts
- `/proc/loadavg` for load-average and runnable-task information
- `/proc/sys/` for runtime kernel parameters

Some files, especially under `/proc/sys`, are writable configuration interfaces. Do not write to them merely because they look like regular files. Understand the parameter, scope, persistence mechanism, and rollback before making an authorized system change.

:::single-choice{#proc-filesystem-system-interface} Which entry provides system-wide memory counters rather than one process's status?

::option[`/proc/self/status`]{#proc-filesystem-self-status explanation="This resolves to the observing process's own per-process status."}
::option[`/proc/meminfo`]{#proc-filesystem-memory-info .correct explanation="`meminfo` contains kernel-reported system memory statistics."}
::option[`/proc/1/fd`]{#proc-filesystem-one-fd explanation="This directory represents file descriptors belonging to PID 1, subject to access controls."}
:::

## Using `/proc` through Tools

Linux implementations of tools such as `ps`, `top`, and `free` obtain much of their data from procfs and other kernel interfaces, then label, calculate, and format it. Prefer those tools for routine work when they provide the needed field; read `/proc` directly for specific details or scripting only after studying the interface documentation.

Direct readers must parse formats correctly, tolerate missing processes, protect sensitive output, and avoid assuming one read is an atomic system snapshot.

:::single-choice{#proc-filesystem-live-data} Why can `/proc/PID` disappear between two inspection commands?

::option[Every procfs file is automatically renamed once per second.]{#proc-filesystem-renamed explanation="There is no periodic renaming rule for all procfs entries."}
::option[Reading `status` deletes the process directory.]{#proc-filesystem-read-delete explanation="Status inspection is read-only and does not terminate or remove the process."}
::option[The process can exit while it is being observed.]{#proc-filesystem-process-exit .correct explanation="Procfs reflects live state, so the kernel removes a per-process directory after that process is gone."}
:::

## Summary

You can now use procfs as a live, access-controlled kernel interface.

1. Associate numeric `/proc` directories with visible PIDs.
2. Read selected per-process files while accounting for races and sensitivity.
3. Distinguish process directories from system-wide interfaces.
4. Prefer documented tools and formats for reliable routine inspection.
