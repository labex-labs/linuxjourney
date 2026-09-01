---
lesson_id: "power-states"
course_id: "init"
lang: "en"
order_index: 7
title: "Power States"
description: "Learn how to schedule, cancel, and safely verify Linux shutdown and reboot operations."
meta_title: "Power States - Init"
meta_description: "Learn how to manage Linux system power states. This guide covers the essential shutdown, reboot, and halt commands to safely power off or restart your Linux system. Master these fundamental Linux commands for system administration."
meta_keywords: "linux power states, shutdown command, reboot command, halt command, poweroff linux, restart linux, linux system administration, linux for beginners, linux commands, systemd, init"
---

Shutting down or rebooting changes the availability of the entire system. Before acting, confirm the target host, obtain authorization, warn connected users, and make sure important writes, backups, and maintenance tasks can finish. On a remote system, preserve an independent console or recovery path in case the machine does not return.

## Powering Off Safely

On a systemd-based distribution, request an orderly power-off with:

```bash
$ sudo systemctl poweroff
```

The traditional `shutdown` interface is also widely available:

```bash
$ sudo shutdown -h now
```

An orderly shutdown asks services to stop, unmounts filesystems, and then changes the machine's power state. Do not treat a forced reboot or the physical power switch as an ordinary shortcut; either can interrupt writes and leave data or services inconsistent.

:::single-choice{#power-states-orderly-poweroff} What should you do before powering off a remote production host?

::option[Disconnect its management console before issuing the command.]{#power-states-remove-console explanation="A management console is useful recovery access and should remain available."}
::option[Force the power off so services cannot delay the operation.]{#power-states-force-first explanation="A forced operation can interrupt writes and should not be the normal method."}
::option[Confirm the host and preserve a recovery access path.]{#power-states-confirm-and-recover .correct explanation="Target confirmation prevents acting on the wrong host, while recovery access helps if it does not return."}
:::

## Scheduling and Cancelling a Shutdown

Give users and workloads time to prepare by scheduling the operation. The `+m` form means a number of minutes from now:

```bash
$ sudo shutdown -h +4
```

This schedules a halt or power-off in four minutes and sends warnings to logged-in users. If the maintenance is postponed, cancel a pending shutdown before its deadline:

```bash
$ sudo shutdown -c
```

Do not assume that a warning makes the operation safe. Check active sessions and system-specific workloads, and follow the service or cluster's documented drain procedure when one exists.

:::single-choice{#power-states-four-minute-schedule} Which command schedules a shutdown four minutes from now?

::option[`sudo shutdown -h +4`]{#power-states-relative-four .correct explanation="The `-h` action combined with `+4` requests shutdown four minutes from now."}
::option[`sudo shutdown -h 4`]{#power-states-absolute-four explanation="Without the plus sign, the time argument is not the documented relative-minute form."}
::option[`sudo shutdown -c +4`]{#power-states-cancel-four explanation="The `-c` option cancels a pending shutdown rather than creating one."}
:::

## Rebooting the System

Use an orderly reboot when the machine must stop and start again:

```bash
$ sudo systemctl reboot
```

Equivalent compatibility commands commonly include:

```bash
$ sudo shutdown -r now
$ sudo reboot
```

Before rebooting, verify that encrypted disks, boot configuration, networking, and required services can recover without the current interactive session. Coordinate failover or workload migration first when other systems depend on the host.

:::single-choice{#power-states-reboot-action} Which command requests an immediate orderly reboot through `shutdown`?

::option[`sudo shutdown -c now`]{#power-states-cancel-now explanation="The `-c` option cancels a pending shutdown."}
::option[`sudo shutdown -r now`]{#power-states-reboot-now .correct explanation="The `-r` option selects reboot, and `now` schedules it immediately."}
::option[`sudo shutdown -h now`]{#power-states-halt-now explanation="The `-h` action halts or powers off instead of rebooting."}
:::

## Distinguishing Halt from Power-Off

`halt`, `poweroff`, and `reboot` may be compatibility front ends to the init system, but their requested end states differ. A halt stops normal system operation; depending on the platform and implementation, it might leave power supplied. A power-off additionally requests that supported hardware remove power. Prefer the command that names the intended outcome, and consult the local manual because compatibility behavior can vary.

:::single-choice{#power-states-halt-versus-poweroff} Why should you distinguish `halt` from `poweroff`?

::option[Power-off requests removal of power, while halt may leave it supplied.]{#power-states-power-distinction .correct explanation="The requested final hardware state can differ even when both stop normal operation."}
::option[Halt always restarts services after they stop.]{#power-states-halt-restarts explanation="Halt is a stopping state, not a request to restart services."}
::option[Power-off only logs out the current terminal user.]{#power-states-power-logout explanation="Power-off is a system-wide state transition, not a shell logout."}
:::

## Verifying the Outcome

For a scheduled operation, confirm that users received notice and that critical work has drained. After a reboot, verify the expected kernel and boot state, failed units, application health, storage mounts, network reachability, and recent boot logs. A successful login alone does not prove that the whole service recovered.

```bash
$ uptime
$ systemctl --failed
$ journalctl -b -p warning
```

These are starting points; use application-native health checks for the actual workload.

:::single-choice{#power-states-post-reboot-check} What provides the strongest evidence that a rebooted application is ready?

::option[Service state, logs, and its health check all succeed.]{#power-states-health-evidence .correct explanation="Multiple system and application checks verify the workload rather than only host access."}
::option[The chassis power indicator is illuminated.]{#power-states-light-on explanation="Hardware power does not establish application health."}
::option[An administrator can log in to a shell.]{#power-states-shell-open explanation="Shell access proves only part of system availability."}
:::

## Summary

You can now change Linux power states with preparation, clear intent, and verification.

1. Confirm the target, impact, authorization, and recovery path.
2. Use orderly power-off or reboot commands for normal operations.
3. Schedule a shutdown when users and workloads need warning.
4. Cancel a pending shutdown when the maintenance plan changes.
5. Verify system and application health after the machine returns.
