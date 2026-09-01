---
lesson_id: "sysv-overview"
course_id: "init"
lang: "en"
order_index: 1
title: "System V Overview"
description: "Learn how traditional System V init uses runlevels and ordered service-script links."
meta_title: "System V Overview - Init"
meta_description: "Explore the traditional System V init system, also known as SysV or init v. This guide covers how systemv manages processes, its sequential startup, and the role of runlevels in Linux. Learn the fundamentals of the classic initv process."
meta_keywords: "System V, systemv, SysV init, systemv init, init v, initv, Linux runlevels, init system, process management, Linux tutorial"
---

System V init, usually called SysV init or sysvinit, is a traditional PID 1 and service-startup design. It remains important on legacy systems and through compatibility scripts, but installed SysV-style files do not prove that sysvinit is the running PID 1.

## Identifying the Active Init System

Inspect live PID 1:

```bash
$ ps -p 1 -o pid,comm,args=
$ readlink /proc/1/exe
```

An `/etc/inittab` file or `/etc/init.d/` directory is only supporting evidence. systemd and other init systems can retain these files for compatibility, and containers can show a different PID namespace from the host.

:::single-choice{#sysv-overview-detection} What is the strongest evidence that sysvinit is active?

::option[The live PID 1 executable is sysvinit or its init program.]{#sysv-overview-live-pid-one .correct explanation="Inspecting the running first process is more direct than inferring from compatibility files."}
::option[An `/etc/init.d/` directory exists.]{#sysv-overview-init-d-only explanation="Other init systems commonly preserve SysV scripts or wrappers."}
::option[A package description contains the word service.]{#sysv-overview-package-word explanation="Package text does not identify the process currently acting as PID 1."}
:::

## Runlevels

A runlevel is a named numeric operating mode. SysV configurations traditionally use levels `0` through `6` plus special levels, but meanings are distribution policy rather than a universal law. Common conventions include:

- `0`: halt or poweroff transition
- `1` or `S`: single-user or rescue mode
- `2` through `5`: distribution-defined multiuser modes
- `6`: reboot transition

Debian-family systems historically treat levels 2–5 similarly, while Red Hat-family conventions distinguish text and graphical modes. Inspect `/etc/inittab`, init documentation, and runlevel directories on the actual host.

:::single-choice{#sysv-overview-shutdown-runlevel} Which runlevel conventionally requests halt or poweroff on many SysV systems?

::option[`3`]{#sysv-overview-runlevel-three explanation="This is commonly a multiuser operating mode rather than shutdown."}
::option[`0`]{#sysv-overview-runlevel-zero .correct explanation="Level zero is conventionally the shutdown transition, though local init policy remains authoritative."}
::option[`6`]{#sysv-overview-runlevel-six explanation="Level six conventionally requests reboot."}
:::

## Init Scripts and Runlevel Links

Service scripts commonly reside under `/etc/init.d/`. Runlevel directories such as `/etc/rc2.d/` or `/etc/rc.d/rc2.d/` contain links whose names encode transition action and order:

- `SNNname` links request a start action.
- `KNNname` links request a stop action.
- `NN` provides lexical ordering among links for that transition.

The exact algorithm and directories vary. Dependencies can also be expressed in script headers and processed by distribution tools, and some implementations parallelize work. SysV should not be reduced to a guarantee that every service starts strictly one at a time.

:::single-choice{#sysv-overview-start-link} What does an `S20networking` link conventionally request during entry into a runlevel?

::option[Send signal 20 directly to every network process.]{#sysv-overview-signal-twenty explanation="The digits are ordering metadata, not a signal number."}
::option[Store twenty network configuration backups.]{#sysv-overview-twenty-backups explanation="Runlevel links do not provide backup retention."}
::option[Run the linked service script with its start action in the `S` ordering.]{#sysv-overview-start-action .correct explanation="The prefix distinguishes startup links, with the number contributing to sequence."}
:::

## Transitioning Between Runlevels

When init changes runlevel, the distribution's rc machinery stops services no longer needed and starts services required in the new mode. Scripts must be idempotent enough to handle repeated status or transition operations and return meaningful statuses.

Requesting runlevel 0 or 6 is a system-wide destructive availability action. Use the system's shutdown interface, notify users, preserve active work, and verify remote console access rather than invoking raw init transitions casually.

:::single-choice{#sysv-overview-runlevel-six-meaning} What does runlevel `6` conventionally request?

::option[Creation of six additional user accounts.]{#sysv-overview-six-users explanation="Runlevels describe operating modes, not account counts."}
::option[A system reboot transition.]{#sysv-overview-reboot .correct explanation="Classic SysV policy reserves level six for stopping services and restarting the system."}
::option[Mounting every filesystem read-only forever.]{#sysv-overview-six-readonly explanation="That is not the conventional runlevel-six purpose."}
:::

## Limits of Compatibility

On a systemd host, SysV scripts can be wrapped as generated units, but systemd dependencies, timeouts, logging, and state semantics still apply. Running a legacy script directly can bypass the service manager's tracking. Identify the active manager and use its native interface when possible.

:::single-choice{#sysv-overview-compatibility-script} Why should a SysV-style script on a systemd host normally be invoked through the service manager?

::option[Direct execution can bypass dependency and state tracking.]{#sysv-overview-manager-tracking .correct explanation="The manager needs to coordinate process ownership, ordering, timeouts, and status."}
::option[Shell scripts cannot execute on a systemd system.]{#sysv-overview-scripts-impossible explanation="They can execute, but bypassing supervision can create inconsistent state."}
::option[Systemd converts every service script into a kernel module.]{#sysv-overview-script-module explanation="Compatibility units remain user-space service management."}
:::

## Summary

You can now interpret a traditional SysV layout without assuming it is active.

1. Identify the live PID 1 before choosing init commands.
2. Treat runlevel meanings as distribution-defined conventions.
3. Read `S`, `K`, and numeric ordering in runlevel links.
4. Use controlled shutdown procedures for levels 0 and 6.
5. Respect the active manager when compatibility scripts are present.
