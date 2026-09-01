---
lesson_id: "kernel-logging"
course_id: "logging"
lang: "en"
order_index: 4
title: "Kernel Logging"
description: "Learn how to query current and retained Linux kernel messages with dmesg and journalctl."
meta_title: "Kernel Logging - Logging"
meta_description: "Explore the Linux kernel log, including /var/log/kern.log and dmesg. Learn how to check the kern log for boot messages, hardware driver information, and troubleshoot system issues. A guide to kernel log linux files."
meta_keywords: "kernel log, kern.log, /var/log/kern.log, kernel log linux, kern log, dmesg, linux logging, boot messages, kernel events"
---

The kernel emits messages about boot, drivers, devices, filesystems, networking, memory, and failures. These records can explain low-level symptoms, but a warning string alone does not prove that hardware is defective.

## Reading the Kernel Ring Buffer

`dmesg` reads messages from the kernel ring buffer:

```bash
$ dmesg --human
```

The buffer has finite capacity, so newer messages can overwrite older ones. Access may also be restricted to privileged users. `dmesg --follow` follows new kernel messages on implementations that support it; stop after a bounded reproduction.

:::single-choice{#kernel-log-ring-buffer-limit} Why might an older kernel event be absent from current `dmesg` output?

::option[Kernel events can only contain one character.]{#kernel-log-one-character explanation="Kernel messages can contain normal diagnostic text and metadata."}
::option[`dmesg` permanently deletes every line after displaying it.]{#kernel-log-display-deletes explanation="A normal read does not consume all displayed kernel messages."}
::option[The finite ring buffer may have overwritten it.]{#kernel-log-overwritten .correct explanation="The in-memory buffer retains a limited amount of kernel message data."}
:::

## Using Readable Timestamps

Raw kernel timestamps are commonly relative to boot. `dmesg --ctime` or `--human` can render wall-clock times, but converted values depend on clock history and can be inaccurate if the clock changed after boot. Preserve boot-relative timing when precise sequencing matters.

:::single-choice{#kernel-log-timestamp-caution} Why should converted `dmesg` wall-clock timestamps be treated carefully?

::option[They always refer to a different machine.]{#kernel-log-other-machine explanation="They are derived locally, though clock changes can affect conversion."}
::option[They depend on mapping boot-relative time to a clock that may change.]{#kernel-log-clock-change .correct explanation="Time synchronization or manual clock changes can make the rendered wall time misleading."}
::option[They show filesystem free space instead of time.]{#kernel-log-free-space explanation="Timestamp options still display times, not storage capacity."}
:::

## Querying Persistent Kernel Records

On a systemd host, query kernel records from the current boot with:

```bash
$ journalctl -k -b
```

If persistent journal storage retained earlier boots, inspect the boot list and select one:

```bash
$ journalctl --list-boots
$ journalctl -k -b -1
```

Traditional syslog routing may create `/var/log/kern.log` or another file, but this is configuration-dependent. A saved `/var/log/dmesg` file is also not universal and may represent only a boot-time snapshot.

:::single-choice{#kernel-log-previous-boot} Which command requests kernel messages from the previous retained boot?

::option[`journalctl -u kernel -f`]{#kernel-log-unit-follow explanation="Kernel messages are selected with `-k`, and following does not choose the previous boot."}
::option[`dmesg --clear`]{#kernel-log-clear explanation="Clearing changes buffer state and does not retrieve an earlier boot."}
::option[`journalctl -k -b -1`]{#kernel-log-previous .correct explanation="The kernel filter combined with boot offset minus one selects the prior retained boot."}
:::

## Investigating a Kernel Event

Identify the boot, timestamp, device, subsystem, and the action occurring at that moment. Query surrounding kernel and service records, then compare hardware inventory and current state:

```bash
$ journalctl -k -b --since '10 minutes ago'
$ lspci -k
$ lsblk
```

Use only tools relevant to the subsystem. Before reloading a driver, unbinding a device, or rebooting, assess storage, network, console, and service impact and preserve recovery access.

:::single-choice{#kernel-log-warning-response} What is the best response to one kernel warning line?

::option[Immediately unload every loaded driver.]{#kernel-log-unload-all explanation="This can disrupt critical devices and does not isolate the warning's cause."}
::option[Assume the entire machine must be replaced.]{#kernel-log-replace-machine explanation="A single record is insufficient evidence for that conclusion."}
::option[Correlate it with surrounding events and current subsystem state.]{#kernel-log-correlate .correct explanation="Context and repeatable impact are needed before selecting a corrective action."}
:::

## Summary

You can now distinguish live kernel-buffer messages from retained kernel logs.

1. Read the finite ring buffer with `dmesg`.
2. Interpret boot-relative and converted timestamps carefully.
3. Query current or previous boots with `journalctl -k`.
4. Correlate kernel messages before making disruptive changes.
