---
lesson_id: "systemd-goals"
course_id: "init"
lang: "en"
order_index: 6
title: "Systemd Goals"
description: "Learn how to inspect, override, validate, start, enable, and troubleshoot systemd service units."
meta_title: "Systemd Goals - Init"
meta_description: "Explore systemd goals and learn to manage Linux services using essential systemctl commands. This guide covers systemd unit file basics, how to start, stop, and enable services, and view their status."
meta_keywords: "systemd, systemctl, Linux services, unit files, systemd goals, service management, systemd units, beginner, tutorial, guide, Linux commands"
---

`systemctl` sends requests to a systemd manager. This lesson focuses on system service units. Confirm the exact unit name, manager scope, dependencies, and operational impact before changing state.

## Reading a Service Unit

A minimal illustrative unit can look like:

```ini
[Unit]
Description=Example worker
Wants=network-online.target
After=network-online.target

[Service]
Type=exec
ExecStart=/usr/local/bin/example-worker
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

- `[Unit]` contains description and dependency relationships.
- `[Service]` defines process lifecycle and service-specific behavior.
- `[Install]` tells enablement commands which aliases or dependency links to create; it is not automatically an active runtime dependency.

`ExecStart=` is not passed through a shell by default. Shell pipelines, redirections, variables, and quoting do not behave like an interactive command line unless an explicit shell is intentionally invoked.

:::single-choice{#systemd-goals-install-section} What is the primary purpose of `[Install]` directives such as `WantedBy=`?

::option[Guarantee that the service process is already running.]{#systemd-goals-install-running explanation="Runtime activation requires start or another triggering dependency."}
::option[Describe links or relationships created when the unit is enabled.]{#systemd-goals-enable-links .correct explanation="Install metadata is interpreted by enablement operations and is separate from current process state."}
::option[Execute every command through the user's interactive shell.]{#systemd-goals-install-shell explanation="Unit command parsing does not use an interactive shell by default."}
:::

## Inspecting Effective Configuration

List loaded units with:

```bash
$ systemctl list-units --type=service
```

List installed unit files and enablement states with:

```bash
$ systemctl list-unit-files --type=service
```

These are different views: a unit file can be enabled but inactive, active but disabled, static, generated, transient, masked, or absent from one listing. Inspect merged vendor and drop-in content with:

```bash
$ systemctl cat UNIT.service
$ systemctl show UNIT.service
```

:::single-choice{#systemd-goals-list-units-versus-files} What does `list-unit-files` show that `list-units` does not primarily show?

::option[Only processes consuming the most CPU.]{#systemd-goals-cpu-processes explanation="Process resource ranking is outside these unit inventory commands."}
::option[Installed unit-file enablement states.]{#systemd-goals-unit-file-state .correct explanation="It reports whether unit files are enabled, disabled, static, masked, and related installation states."}
::option[Every line ever written to the journal.]{#systemd-goals-all-journal explanation="Journal queries use `journalctl`."}
:::

## Creating a Local Override

Use a drop-in rather than editing a packaged unit:

```bash
$ sudo systemctl edit UNIT.service
```

After saving, systemctl normally asks the manager to reload as part of this edit workflow on current implementations, but when files are changed by another method, run:

```bash
$ sudo systemctl daemon-reload
```

`daemon-reload` rereads unit definitions and rebuilds dependencies. It does not reload application configuration or restart running services. Validate unit syntax and dependencies with `systemd-analyze verify` where appropriate, then review the effective merged unit.

:::single-choice{#systemd-goals-daemon-reload} What does `systemctl daemon-reload` do?

::option[Forces every daemon to reread its application configuration.]{#systemd-goals-reload-all-apps explanation="Application reload is service-specific and separate from manager configuration."}
::option[Reboots the kernel into a new release.]{#systemd-goals-reload-kernel explanation="Kernel activation requires a boot, not a unit-definition reload."}
::option[Reloads systemd unit definitions and dependency information.]{#systemd-goals-reload-manager .correct explanation="It updates the manager's configuration view without inherently restarting services."}
:::

## Runtime Service State

After validating service configuration and preserving recovery access:

```bash
$ sudo systemctl start peanut.service
$ sudo systemctl stop peanut.service
$ sudo systemctl restart peanut.service
$ sudo systemctl reload peanut.service
```

`reload` succeeds only when the unit defines or supports a reload action. `restart` interrupts the process and can fail to restore service. For remote access, networking, storage, or authentication, keep a separate console path and verify configuration before acting.

Check state and logs with:

```bash
$ systemctl status peanut.service
$ systemctl is-active peanut.service
$ journalctl -u peanut.service -b
```

“Active” is manager state, not proof that every application endpoint is healthy.

:::single-choice{#systemd-goals-start-peanut} Which command starts `peanut.service` now without changing future enablement by itself?

::option[`sudo systemctl enable peanut.service`]{#systemd-goals-enable-only explanation="Enable changes installation links but does not start the service unless combined with `--now`."}
::option[`sudo systemctl start peanut.service`]{#systemd-goals-start-command .correct explanation="Start requests current runtime activation and is separate from enablement."}
::option[`sudo systemctl daemon-reload peanut.service`]{#systemd-goals-daemon-reload-unit explanation="Daemon-reload takes no unit activation operand and does not start this service."}
:::

## Enablement, Disablement, and Masking

Manage future dependency links with:

```bash
$ sudo systemctl enable peanut.service
$ sudo systemctl disable peanut.service
```

Enable does not start the unit unless `--now` is added. Disable does not stop a running unit unless `--now` is added. A static unit can lack install metadata and still be activated as another unit's dependency.

Masking links the unit to `/dev/null` and blocks ordinary activation, including dependency activation, until unmasked. It is stronger than disable and can break dependents; inspect reverse dependencies before using it.

:::single-choice{#systemd-goals-disable-runtime} What happens to an already running service after `systemctl disable UNIT` without `--now`?

::option[It is immediately killed with `SIGKILL`.]{#systemd-goals-disable-kills explanation="Disable alone does not request a current stop."}
::option[Its executable is deleted from the filesystem.]{#systemd-goals-disable-deletes explanation="Enablement operations manage links, not program package files."}
::option[It normally keeps running while future enablement links are removed.]{#systemd-goals-disable-keeps-running .correct explanation="Runtime state and installation state are separate dimensions."}
:::

## Verify the Service Outcome

After a change, verify process state, recent logs, listening endpoints, dependent units, application health, and behavior across a controlled reboot if boot enablement changed. Use `systemctl is-failed`, `systemctl list-dependencies`, and application-native checks as appropriate.

## Summary

You can now manage a systemd service without confusing configuration, runtime, and enablement.

1. Read `[Unit]`, `[Service]`, and `[Install]` by their distinct roles.
2. Compare loaded unit state with installed unit-file state.
3. Use drop-ins and reload the manager after external file changes.
4. Start, stop, reload, or restart only after impact review.
5. Treat enable, disable, and mask as separate persistence controls.
