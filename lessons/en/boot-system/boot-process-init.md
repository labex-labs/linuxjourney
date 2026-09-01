---
lesson_id: "boot-process-init"
course_id: "boot-system"
lang: "en"
order_index: 5
title: "Boot Process: Init"
description: "Learn how PID 1 initializes user space, supervises services, reaps children, and coordinates shutdown."
meta_title: "Boot Process: Init - Boot the System"
meta_description: "Explore the core of the Linux boot process in this beginner-friendly Linux guide. Learn about the different Linux init systems, including the traditional System V, Upstart, and the modern standard, systemd. Understand how these systems start and manage services on your machine."
meta_keywords: "Linux init, systemd, System V init, Upstart, Linux boot process, Linux tutorial, beginner Linux, Linux guide"
---

The kernel starts the first user-space process as PID 1 in a PID namespace. On a full Linux system, this init process establishes the service environment. In a container, PID 1 can instead be a small init wrapper or the application itself, but it still has special signal and child-reaping responsibilities.

## Responsibilities of PID 1

An init system commonly:

- starts and supervises services, logins, mounts, and other units of work
- orders work according to dependencies and configured target state
- adopts and reaps orphaned child processes
- responds to service failures according to policy
- coordinates orderly shutdown and reboot

The exact boundary varies. Device management, networking, logging, and scheduled tasks can be separate programs supervised by init rather than code built into PID 1.

:::single-choice{#boot-init-pid-one-role} Which responsibility is special for PID 1 in its PID namespace?

::option[Compiling every application from source at each boot.]{#boot-init-compile-apps explanation="Normal service startup uses installed programs rather than rebuilding all software."}
::option[Defining the disk's physical sector size.]{#boot-init-sector-size explanation="Storage hardware and drivers expose sector geometry before init manages services."}
::option[Adopting and reaping orphaned child processes.]{#boot-init-reap-orphans .correct explanation="PID 1 is the final parent and must collect termination status so zombie records do not accumulate."}
:::

## System V Init and Runlevels

Traditional sysvinit uses configuration such as `/etc/inittab` and runlevel-specific startup and shutdown scripts. A runlevel represents an operating mode, but the meaning of numbered levels can differ by distribution. Script ordering is convention-driven and can be extended or parallelized by distribution tooling.

Do not infer a host's active init system merely because `/etc/init.d/` exists; compatibility scripts can remain on systems whose PID 1 is another implementation.

:::single-choice{#boot-init-sysv-runlevel} What does a System V runlevel represent?

::option[A kernel version number selected by the bootloader.]{#boot-init-runlevel-kernel explanation="Kernel selection is a loader concern and not encoded by an init runlevel."}
::option[A configured operating mode associated with service actions.]{#boot-init-runlevel-mode .correct explanation="SysV layouts associate levels with sets and ordering of startup or shutdown scripts."}
::option[A filesystem's current inode usage percentage.]{#boot-init-runlevel-inodes explanation="Filesystem metadata capacity is unrelated to service operating modes."}
:::

## Event- and Dependency-Based Systems

Upstart introduced an event-driven job model and was used by older Ubuntu releases and some other systems. It is now primarily of historical or legacy operational interest.

systemd is widely used by current general-purpose distributions. It models services, sockets, mounts, timers, devices, targets, and other resources as units. Declarative dependencies and activation mechanisms let independent work proceed concurrently while preserving required ordering.

Other active init and supervision designs include OpenRC, runit, s6, and BusyBox init. “Newest” is not a useful compatibility rule; identify what the actual system runs and use its documentation.

:::single-choice{#boot-init-systemd-unit-model} How does systemd represent managed resources such as services and mounts?

::option[As MBR primary partition entries.]{#boot-init-systemd-partitions explanation="Disk partition metadata is unrelated to service-manager units."}
::option[As hard links to PID 1's executable only.]{#boot-init-systemd-hard-links explanation="Units are configuration and runtime objects, not merely inode aliases."}
::option[As units with dependencies and activation relationships.]{#boot-init-systemd-units .correct explanation="Unit types provide a shared model for ordering, state, and supervision."}
:::

## Identifying the Running Init

Inspect PID 1 rather than guessing from installed files:

```bash
$ ps -p 1 -o pid,comm,args=
$ readlink /proc/1/exe
```

Permissions, containers, and namespaces affect what you see. A command run inside a container reports that namespace's PID 1, not necessarily the host init. Once identified, use its native status and log tools instead of mixing commands from another init family.

:::single-choice{#boot-init-detect-running} Why is inspecting PID 1 better than checking whether a legacy script directory exists?

::option[PID 1 always has the same executable name on every Linux system.]{#boot-init-same-name explanation="Systemd, sysvinit, BusyBox, container init programs, and others can occupy PID 1."}
::option[Compatibility files can exist even when another init implementation is running.]{#boot-init-compatibility-files .correct explanation="The live PID 1 executable is stronger evidence of the active init system."}
::option[Legacy directories are automatically deleted at every boot.]{#boot-init-directories-deleted explanation="Installed compatibility files can persist across boots."}
:::

## Summary

You can now explain init as a role rather than one mandatory implementation.

1. Relate PID 1 to service initialization, reaping, and shutdown.
2. Recognize System V runlevels as distribution-defined operating modes.
3. Relate systemd resources and dependencies to units.
4. Inspect the live PID 1 in the relevant namespace before choosing tools.
