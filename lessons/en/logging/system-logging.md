---
lesson_id: "system-logging"
course_id: "logging"
lang: "en"
order_index: 1
title: "System Logging"
description: "Learn how Linux log sources, collectors, storage, and viewing tools fit together."
meta_title: "System Logging - Logging"
meta_description: "Discover the best way to learn Linux by understanding system logging. This guide covers syslog, rsyslogd, and how to find and read log files in /var/log. A key part of any free online Linux course."
meta_keywords: "how to learn linux, best way to learn linux, linux system logging, syslog, rsyslogd, var log, system logs, learn linux command line, best resources to learn linux"
---

Logs record events emitted by the kernel, services, applications, and security components. They support troubleshooting and auditing, but only when collection is working, timestamps are understood, and the relevant source is included.

## Following a Log Message

A logging path has several distinct parts:

1. A source emits an event.
2. A collector accepts and enriches it.
3. Routing and retention rules choose storage or forwarding destinations.
4. A viewer queries the stored records.

On a systemd host, `systemd-journald` commonly collects service standard output, kernel messages, and journal-native or syslog messages. A syslog daemon such as rsyslog may also receive messages and write traditional text files or forward them. Applications can instead maintain their own files or external telemetry.

:::single-choice{#system-logging-distinct-roles}
Which component decides where accepted messages are stored or forwarded?

::option[The terminal's current working directory.]{#system-logging-cwd explanation="A shell directory does not define system-wide logging routes."}
::option[The filename of the running kernel image.]{#system-logging-kernel-file explanation="The kernel can emit messages, but its image filename is not the routing policy."}
::option[The routing and retention configuration.]{#system-logging-routing .correct explanation="Rules between collection and storage determine destinations and retention behavior."}
:::

## Discovering Available Logs

Do not assume every host has the same files. Inspect the active logging services and local configuration:

```bash
$ systemctl --type=service --state=running | grep -E 'journal|syslog'
$ ls -la /var/log
$ journalctl --disk-usage
```

`/var/log/syslog` is common on Debian-family systems using compatible routing, while `/var/log/messages` is common elsewhere. Either may be absent on a journal-only host. Application documentation and unit configuration can identify additional destinations.

:::single-choice{#system-logging-file-absence}
What does a missing `/var/log/syslog` file necessarily mean?

::option[The host may use another configured logging destination.]{#system-logging-other-destination .correct explanation="Journal-only systems and different syslog policies need not create this file."}
::option[The kernel has never produced a message.]{#system-logging-no-kernel explanation="Kernel records may be present in the journal or another destination."}
::option[Every application has stopped running.]{#system-logging-apps-stopped explanation="Application state cannot be inferred from one absent path."}
:::

## Querying the Journal

Start with a bounded query instead of dumping the entire journal:

```bash
$ journalctl -b -p warning
$ journalctl -u ssh.service --since '1 hour ago'
```

`-b` selects the current boot, `-p` filters by priority, and `-u` filters by a unit. Unit names and retained boots differ by host. Use `journalctl --list-boots` to see available boots and `journalctl -f` to follow new records while reproducing an issue.

:::single-choice{#system-logging-current-boot}
Which option limits a `journalctl` query to the current boot?

::option[`-b`]{#system-logging-boot-option .correct explanation="Without an argument, the boot selector chooses the current boot."}
::option[`-u`]{#system-logging-unit-option explanation="This filters by a systemd unit."}
::option[`-f`]{#system-logging-follow-option explanation="This follows newly appended records."}
:::

## Reading Records in Context

A traditional syslog-style line can look like:

```text
Jan 27 07:41:32 icebox anacron[4650]: Job `cron.weekly' started
```

It contains a timestamp, host, program and PID, then a message. Treat message text as application output, not a guaranteed structured fact. Check timezone, clock synchronization, boot ID, PID reuse, and records immediately before and after the event. Journal fields can provide stronger identifiers than the rendered text alone.

Logs may contain usernames, addresses, paths, tokens, or other sensitive data. Use least-privilege access, redact exports, and preserve originals and timestamps during an investigation.

:::single-choice{#system-logging-export-safety}
What should you do before sharing a log excerpt externally?

::option[Replace every timestamp with a random value.]{#system-logging-random-time explanation="Destroying timing information can prevent correlation and is not a sound redaction method."}
::option[Review it for secrets and sensitive identifiers.]{#system-logging-review-sensitive .correct explanation="Logs often contain operational or personal data that requires controlled redaction."}
::option[Make the original log world-writable.]{#system-logging-world-writable explanation="Weakening access controls can damage integrity and expose additional data."}
:::

## Summary

You can now locate and query Linux logs without assuming one universal storage path.

1. Separate event sources, collectors, routing, storage, and viewers.
2. Discover the host's active logging configuration.
3. Use bounded journal queries for a unit, boot, time, or priority.
4. Correlate records in context and protect sensitive log data.
