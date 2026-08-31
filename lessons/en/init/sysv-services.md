---
lesson_id: "sysv-services"
course_id: "init"
lang: "en"
order_index: 2
title: "System V Service"
description: "Learn how to inspect and operate legacy SysV service scripts through the active system's supported wrapper."
meta_title: "System V Service - Init"
meta_description: "Learn to manage traditional System V (SysV) services in Linux. This guide covers using the `service` command to list, start, stop, and restart services on a System V init system."
meta_keywords: "system v, sysv init, linux services, service command, manage linux services, start service, stop service, restart service, linux system v"
---

SysV services are commonly represented by executable scripts under `/etc/init.d/`. A script accepts actions such as `start`, `stop`, `restart`, or `status` according to its implementation and distribution conventions. The `service` command provides a wrapper that runs a named script in a more controlled environment.

## Discovering Services and Actions

List script names first:

```bash
$ ls -1 /etc/init.d/
```

Some implementations provide:

```bash
$ service --status-all
```

Its bracket markers and exit statuses are wrapper-specific, and a script can report unknown status. For one service, inspect the script's usage output or documentation rather than assuming every action exists.

:::single-choice{#sysv-services-wrapper-purpose}
What does the `service` command commonly wrap?

::option[A disk partition editor running on every service file.]{#sysv-services-partition-editor explanation="Service control is unrelated to storage partitioning."}
::option[A kernel system call added dynamically by the script.]{#sysv-services-new-syscall explanation="Init scripts are user-space process-control programs."}
::option[A named init script and one of its supported actions.]{#sysv-services-script-action .correct explanation="The wrapper locates a legacy service script and invokes it with a normalized environment."}
:::

## Starting and Stopping

On an actual SysV-managed host, these forms are common:

```bash
$ sudo service SERVICE_NAME start
$ sudo service SERVICE_NAME stop
```

Replace the placeholder only after identifying the service, its dependents, current state, and operational impact. Stopping networking, remote access, storage, or authentication from a remote session can lock you out or corrupt active work.

The direct form `/etc/init.d/SERVICE_NAME ACTION` can exist, but on a host whose active manager provides compatibility, use the manager-facing command so it can track state and dependencies.

:::single-choice{#sysv-services-stop-peanut}
Which command requests that SysV service `peanut` stop?

::option[`sudo service stop peanut`]{#sysv-services-stop-first explanation="The conventional operand order places the service name before the action."}
::option[`sudo stop --partition peanut`]{#sysv-services-partition-stop explanation="This is not the SysV service wrapper syntax."}
::option[`sudo service peanut stop`]{#sysv-services-peanut-stop .correct explanation="The wrapper receives the service name followed by the requested stop action."}
:::

## Reload, Restart, and Status

`restart` normally stops then starts a service, causing interruption. `reload` can ask a service to reread configuration without a full restart, but only when the script and daemon support it. Some scripts offer `force-reload` with distribution-defined fallback behavior.

Validate configuration before any reload or restart, preserve a second administrative connection for remote-access changes, and verify the service afterward through its actual endpoint and logs—not only a “running” status.

```bash
$ sudo service SERVICE_NAME status
$ sudo service SERVICE_NAME reload
```

:::single-choice{#sysv-services-reload-versus-restart}
Why should `reload` not be assumed equivalent to `restart`?

::option[Reload always shuts down the entire operating system.]{#sysv-services-reload-shutdown explanation="That is not the normal meaning of a service reload action."}
::option[Restart only prints configuration and never changes process state.]{#sysv-services-restart-readonly explanation="Restart commonly stops and starts the service."}
::option[Reload is service-specific and can reread configuration without stopping the process.]{#sysv-services-reload-specific .correct explanation="Support and semantics belong to the init script and daemon, while restart normally causes a lifecycle interruption."}
:::

## Runtime Control versus Boot Enablement

Starting a service now does not necessarily enable it for future runlevels. Boot enablement is represented by runlevel links and managed with distribution-specific tools such as `update-rc.d`, `chkconfig`, or service-manager compatibility generators.

Do not create `S` and `K` links manually until you understand the distribution's dependency metadata and management tool; manual links can be overwritten or ordered incorrectly.

:::single-choice{#sysv-services-start-versus-enable}
Does `service SERVICE start` necessarily enable the service at future boots?

::option[Yes; every start action creates all runlevel links automatically.]{#sysv-services-start-links explanation="The wrapper does not universally change persistent enablement."}
::option[No; runtime state and runlevel enablement are separate.]{#sysv-services-runtime-separate .correct explanation="Boot links or manager policy determine future activation independently of starting the process now."}
::option[Yes; a running PID is stored permanently in the boot sector.]{#sysv-services-pid-boot-sector explanation="PIDs are runtime identifiers and are not boot enablement metadata."}
:::

## Summary

You can now operate a legacy service without confusing runtime control and boot policy.

1. Discover the actual script and supported actions.
2. Use the service name before the action in wrapper syntax.
3. Validate and verify reload or restart behavior.
4. Manage future runlevel enablement through distribution tooling.
