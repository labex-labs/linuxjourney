---
lesson_id: "general-logging"
course_id: "logging"
lang: "en"
order_index: 3
title: "General Logging"
description: "Learn how to discover, filter, follow, and correlate general Linux system logs."
meta_title: "General Logging - Logging"
meta_description: "A beginner's guide to general Linux logs. Learn about /var/log/messages and syslog for effective system monitoring, log analysis, and Linux troubleshooting."
meta_keywords: "Linux logs, syslog, var/log/messages, Linux troubleshooting, system logs, log analysis, system monitoring, Linux guide, Linux beginner, /var/log"
---

General system logs combine routine notices, warnings, and errors from multiple sources. They are useful starting points, but their filenames and contents are routing-policy choices rather than universal Linux guarantees.

## Finding the Relevant Source

Depending on the distribution and configuration, general messages may appear in `/var/log/syslog`, `/var/log/messages`, the systemd journal, or more than one destination. Begin by identifying the host and incident interval, then inspect available sources:

```bash
$ ls -lh /var/log
$ journalctl --since '2026-08-31 09:00' --until '2026-08-31 09:15'
```

Application logs may live in their own subdirectories or an external service. Authentication, audit, package, database, and web-server records can be intentionally separated from the general stream.

:::single-choice{#general-logs-universal-file} Why should you not assume `/var/log/messages` exists on every Linux host?

::option[General log destinations depend on local collectors and routing policy.]{#general-logs-local-routing .correct explanation="A journal-only system or a different syslog configuration can use other destinations."}
::option[Linux permits only one log file on each disk.]{#general-logs-one-file explanation="Systems routinely maintain many log files and journal stores."}
::option[The path is reserved exclusively for user documents.]{#general-logs-user-documents explanation="The `/var/log` hierarchy is conventionally used for logs."}
:::

## Inspecting Text Logs

Use `less` for controlled navigation and `tail` for the newest records:

```bash
$ sudo less /var/log/syslog
$ sudo tail -n 100 /var/log/messages
```

Follow newly appended lines during a bounded reproduction with `tail -F FILE`. `-F` retries when a file is replaced during rotation, unlike a simple snapshot. Stop following with `Ctrl-C` and avoid leaving broad privileged sessions open.

:::single-choice{#general-logs-tail-f-capability} What is `tail -F` useful for during a controlled reproduction?

::option[Following a named file across common rotation replacement.]{#general-logs-tail-follow .correct explanation="The retry-by-name behavior helps continue after the active file is renamed and recreated."}
::option[Changing every log severity to debug.]{#general-logs-tail-debug explanation="Tail reads file content and does not reconfigure emitters."}
::option[Decrypting compressed archives without another program.]{#general-logs-tail-decrypt explanation="It does not provide general archive decompression or decryption."}
:::

## Filtering Without Losing Context

Search a bounded file or journal interval rather than piping an unbounded live stream immediately:

```bash
$ grep -n -C 3 'connection refused' /var/log/example.log
$ journalctl -u example.service --since '10 minutes ago' --grep='connection refused'
```

Case, wording, rate limits, and localization can make a literal search incomplete. Record both successful and failed events, and keep surrounding lines because the cause may precede the visible error.

:::single-choice{#general-logs-context-lines} Why include lines around a matching error?

::option[The preceding event may explain the later failure.]{#general-logs-preceding-context .correct explanation="Temporal context helps reconstruct a sequence instead of treating one string as the whole incident."}
::option[Context guarantees the first match is the root cause.]{#general-logs-guaranteed-cause explanation="Additional evidence still must be correlated; context does not prove causation."}
::option[It changes the service configuration automatically.]{#general-logs-context-config explanation="Search output is read-only and does not update service settings."}
:::

## Including Rotated and Archived Logs

An incident may cross a rotation boundary. Active files, numbered archives, and compressed files can contain different parts of the same sequence. Tools such as `zgrep` and `zless` read gzip-compressed archives:

```bash
$ sudo zgrep -n 'connection refused' /var/log/example.log*.gz
```

Order results by actual timestamps, not suffix alone. Before copying evidence, preserve metadata and restrict access because logs can contain personal data or credentials.

:::single-choice{#general-logs-rotation-boundary} What should you check when an incident spans a log rotation?

::option[Only the newly created empty active file.]{#general-logs-active-only explanation="Earlier records may have moved into rotated archives."}
::option[Active and archived logs ordered by event time.]{#general-logs-all-intervals .correct explanation="The relevant sequence can be split across current and rotated files."}
::option[Only filenames, regardless of record timestamps.]{#general-logs-filenames-only explanation="Suffix order and event time are not always equivalent."}
:::

## Summary

You can now investigate general logs across files, journals, and rotation boundaries.

1. Discover destinations instead of assuming a universal filename.
2. Read a bounded interval and follow only during reproduction.
3. Keep temporal context around matching records.
4. Include rotated archives and protect sensitive evidence.
