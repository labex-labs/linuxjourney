---
lesson_id: "systemd-overview"
course_id: "init"
lang: "en"
order_index: 5
title: "Systemd Overview"
description: "Learn how systemd loads units, resolves dependencies, activates targets, and manages system and user resources."
meta_title: "Systemd Overview - Init"
meta_description: "Learn the fundamentals of the systemd init system. This guide covers how systemd (or system d) uses units and targets to manage the Linux boot process and system services. Understand the core concepts of the modern standard for Linux initialization."
meta_keywords: "systemd, system d, init system, systemd units, systemd targets, linux boot process, linux services, system management, beginner, tutorial"
---

Systemd is the PID 1 init and service manager used by many current Linux distributions. The systemd project also provides logging, device, login, network, time, and other components, but distributions can choose which parts to deploy.

## Confirming the Running Manager

Inspect live state rather than the existence of installed directories:

```bash
$ ps -p 1 -o pid,comm,args=
$ systemctl is-system-running
```

`/usr/lib/systemd/` can exist on a system where another program is PID 1, and a container can expose its own PID namespace. `systemctl` also has user-manager and remote/container modes, so identify which manager an operation targets.

:::single-choice{#systemd-overview-detection}
What most directly identifies systemd as the system init manager?

::option[A directory named `/usr/lib/systemd` exists.]{#systemd-overview-directory explanation="Libraries and unit files can remain installed without systemd acting as PID 1."}
::option[A user has executed one command named `systemctl`.]{#systemd-overview-command-executed explanation="A client binary can exist even when no system systemd manager is available."}
::option[The host's PID 1 is systemd.]{#systemd-overview-pid-one .correct explanation="The running first process is stronger evidence than installed files or package names."}
:::

## Units as Managed Objects

A unit is systemd's named model of a resource or activity. Common unit types include:

- `.service` for processes and daemons
- `.socket` for socket activation
- `.mount` and `.automount` for filesystems
- `.timer` and `.path` for event-driven activation
- `.target` for grouping and synchronization
- `.device`, `.swap`, `.slice`, and `.scope` for other managed resources

Unit state is not always “running.” A mount can be mounted, a timer waiting, a device present, and a target active after its dependencies are reached.

:::single-choice{#systemd-overview-group-unit}
Which unit type commonly groups other units and provides a synchronization point?

::option[`.socket`]{#systemd-overview-socket explanation="Socket units expose IPC or network endpoints and can activate services."}
::option[`.target`]{#systemd-overview-target .correct explanation="Target units collect dependencies and represent boot or operational milestones."}
::option[`.timer`]{#systemd-overview-timer explanation="Timer units schedule activation based on calendar or monotonic time."}
:::

## Unit Load Paths and Overrides

System units can be loaded from distribution and administrator paths such as:

- `/usr/lib/systemd/system/` for package-provided units on many distributions
- `/run/systemd/system/` for runtime-generated or transient configuration
- `/etc/systemd/system/` for persistent local administrator configuration and overrides

Exact vendor paths can differ. Higher-priority local configuration overrides lower-priority files with the same unit name. Prefer drop-in overrides created with `systemctl edit UNIT` over copying and modifying a complete vendor file, so package updates remain visible.

:::single-choice{#systemd-overview-local-override}
Where should persistent local system-unit overrides normally reside?

::option[Inside `/proc/systemd/`.]{#systemd-overview-proc-systemd explanation="Procfs is a runtime kernel interface, not persistent unit configuration."}
::option[Under `/etc/systemd/system/`.]{#systemd-overview-etc-system .correct explanation="The administrator configuration layer takes precedence over packaged vendor units."}
::option[In the disk's MBR boot-code bytes.]{#systemd-overview-mbr-units explanation="Service units are user-space configuration files."}
:::

## Dependencies and Ordering

Systemd builds a transaction from dependency relationships. `Wants=` and `Requires=` pull other units into a transaction with different strength. `Before=` and `After=` specify ordering when both units are scheduled; they do not by themselves cause another unit to start.

An `After=network.target` line does not prove that usable connectivity, DNS, or a specific remote endpoint is ready. Services must use the appropriate network-online integration or implement their own retry and readiness behavior.

:::single-choice{#systemd-overview-after-semantics}
What does `After=other.service` specify by itself?

::option[A guarantee that the other service's application endpoint is healthy.]{#systemd-overview-after-health explanation="Ordering completion and application readiness are different concepts."}
::option[Ordering if both units are part of the transaction.]{#systemd-overview-after-ordering .correct explanation="A separate requirement such as Wants or Requires is needed to pull the other unit in."}
::option[Automatic enablement of both units at every future boot.]{#systemd-overview-after-enable explanation="Enablement is installation metadata and is not implied by ordering."}
:::

## Targets and the Default Boot Transaction

`default.target` is commonly an alias to a target such as `multi-user.target` or `graphical.target`. Systemd starts a transaction for that target and its dependencies, allowing unrelated work to proceed concurrently while enforcing explicit ordering.

Targets resemble runlevels only at a broad compatibility level. Multiple targets can be active simultaneously, custom targets can be created, and target activity does not mean every service on the machine is healthy.

:::single-choice{#systemd-overview-default-target}
What does `default.target` normally select?

::option[The default block device that `mkfs` should erase.]{#systemd-overview-default-disk explanation="Targets describe unit activation, not destructive storage selection."}
::option[The only target that can ever be active.]{#systemd-overview-only-target explanation="Targets are groupings, and many can be active in one boot."}
::option[The target transaction used for a normal system boot.]{#systemd-overview-normal-boot .correct explanation="It is commonly an alias to the administrator-selected multiuser or graphical boot target."}
:::

## Summary

You can now describe systemd in terms of live managers, units, and transactions.

1. Confirm systemd through the relevant PID 1 and manager connection.
2. Match resource types to unit suffixes.
3. Place local overrides above vendor configuration.
4. Separate dependency strength, ordering, and application readiness.
5. Treat targets as groupings and milestones rather than exclusive states.
