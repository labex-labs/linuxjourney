---
lesson_id: "udev"
course_id: "devices"
lang: "en"
order_index: 5
title: "udev"
description: "Learn how udev processes kernel device events to apply policy, permissions, and persistent links."
meta_title: "udev - Devices"
meta_description: "Learn about udev, how it dynamically manages Linux device files, and use udevadm. Understand device node creation for beginners."
meta_keywords: "udev, udevadm, Linux device management, device files, Linux tutorial, beginner Linux, udev rules, Linux guide"
---

The Linux kernel reports device changes to user space through uevents. On many current distributions, `systemd-udevd` processes those events using udev rules and a device database. Together with kernel-populated `devtmpfs`, this produces the ownership, permissions, properties, and symbolic links applications see around `/dev`.

## From Kernel Event to Device Policy

When a device is added, changed, moved, or removed, udev can:

- read attributes from sysfs and event properties
- apply owner, group, and mode policy to a device node
- add stable symbolic links such as `/dev/disk/by-id/...`
- tag devices for other services
- run narrowly defined helper processing

The kernel remains responsible for the actual device and its driver. Deleting a node from `/dev` does not physically remove hardware, and manually creating a node with `mknod` does not make unsupported hardware exist or bind a driver.

:::single-choice{#udev-kernel-event-input}
What normally triggers udev processing for a device change?

::option[A package repository refresh performed by APT.]{#udev-apt-refresh explanation="Package metadata updates are unrelated to live device event processing."}
::option[A user renaming every file under `/dev` manually.]{#udev-manual-renaming explanation="Dynamic policy is driven by kernel events and rules, not bulk manual renaming."}
::option[A kernel uevent describing the device action.]{#udev-kernel-uevent .correct explanation="Udev receives device events from the kernel and applies matching user-space rules."}
:::

## Rule Locations and Precedence

Rules commonly reside in:

- `/usr/lib/udev/rules.d/` for vendor or package-provided rules
- `/run/udev/rules.d/` for volatile runtime rules
- `/etc/udev/rules.d/` for local administrator policy

Files are processed in lexical filename order, with same-named files in higher-priority directories replacing lower-priority versions according to the installed udev implementation. Local rules should use a deliberate filename and match stable properties rather than enumeration names.

A rule can affect every matching device, so test scope carefully. Do not edit packaged rules directly when a local override or supplementary rule is appropriate.

:::single-choice{#udev-local-rules-directory}
Which directory is intended for persistent local administrator udev rules?

::option[`/proc/udev/rules.d/`]{#udev-proc-rules explanation="Procfs does not provide the persistent local rule directory."}
::option[`/etc/udev/rules.d/`]{#udev-etc-rules .correct explanation="Local policy belongs under `/etc`, separate from package-managed vendor rules."}
::option[`/dev/udev/rules.d/`]{#udev-dev-rules explanation="`/dev` contains runtime device-facing objects rather than persistent rule configuration."}
:::

## Inspecting a Device with `udevadm`

Query udev properties for an existing node:

```bash
$ udevadm info --query=all --name=/dev/sda
```

Use a node that exists on the current system. `udevadm info --attribute-walk --name=...` can display attributes along the sysfs parent chain, which helps construct a rule. `udevadm monitor --kernel --udev --property` observes kernel and processed events; it may expose device identifiers, so handle captured output appropriately.

:::single-choice{#udev-info-purpose}
What does `udevadm info --query=all --name=/dev/sda` request?

::option[A destructive rewrite of the disk's partition table.]{#udev-info-partition-write explanation="The query is an inspection operation and does not format or repartition storage."}
::option[Installation of a missing kernel driver from the internet.]{#udev-info-install-driver explanation="Udevadm inspection does not act as a package downloader."}
::option[Known udev properties for the named device node.]{#udev-info-properties .correct explanation="The info command queries the device database and associated sysfs information."}
:::

## Applying Rule Changes Carefully

Reloading rule files affects future event processing; it does not automatically reconstruct every existing device state. Triggering events manually can affect many devices and services, so narrow the target and use the installed `udevadm` documentation. A testing command can simulate rule evaluation but may not reproduce every real event side effect.

Back up local rules, validate syntax, observe one known test device, and keep a recovery path before changing permissions or names. Avoid long-running work directly in udev event processing; delegate it to an appropriate service.

:::single-choice{#udev-reload-effect}
What does reloading udev rules primarily change?

::option[How subsequent matching device events are processed.]{#udev-future-events .correct explanation="Reloading updates the in-memory rules; an event must still occur or be deliberately triggered for a device to be reevaluated."}
::option[The physical wiring of every attached device.]{#udev-physical-wiring explanation="Software rule loading cannot change hardware connections."}
::option[Every existing device node regardless of events or matches.]{#udev-all-existing explanation="A reload alone does not guarantee immediate reevaluation of all current devices."}
:::

Use [Explore Hardware Devices in Linux](https://labex.io/labs/comptia-explore-hardware-devices-in-linux-590861) to correlate `udevadm` properties, sysfs paths, and `/dev` links in a controlled environment.

## Summary

You can now place udev between kernel events and user-space device policy.

1. Relate uevents and sysfs attributes to udev rule matching.
2. Separate vendor, runtime, and local rule locations.
3. Inspect properties and event flow with `udevadm`.
4. Reload and trigger rules only with a narrow, tested scope.
