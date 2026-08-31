---
lesson_id: "continuous-monitoring"
course_id: "process-utilization"
lang: "en"
order_index: 7
title: "Continuous Monitoring"
description: "Learn how sysstat collection and sar reports support historical Linux performance analysis."
meta_title: "Continuous Monitoring - Process Utilization"
meta_description: "Learn continuous Linux system monitoring with sar. Understand installation, data collection, and how to analyze historical resource usage for performance. Get started!"
meta_keywords: "sar, sysstat, Linux monitoring, system performance, continuous monitoring, beginner, tutorial, guide"
---

Interactive tools show what is happening while you watch them. Historical monitoring is needed when a slowdown has already ended. The `sysstat` suite collects periodic system counters, and `sar` reads either current counters or saved activity files.

## Enabling Data Collection

Install the distribution's `sysstat` package, then confirm that its collector and retention mechanism are enabled. The exact service, timer, and configuration paths differ by distribution; installing the package does not guarantee collection has started.

On a systemd host, inspect the package-provided units rather than guessing their names:

```bash
$ systemctl list-unit-files | grep sysstat
$ systemctl list-timers --all | grep sysstat
```

Verify that new activity files are being created in the distribution's sysstat data directory and review their permissions and retention policy.

:::single-choice{#sar-installation-verification}
What should you verify after installing `sysstat`?

::option[That collection is enabled and activity files are updating.]{#sar-collector-updating .correct explanation="Package installation and active periodic collection are separate conditions."}
::option[That every process has been restarted manually.]{#sar-restart-processes explanation="Installing a monitoring collector does not require restarting every workload."}
::option[That all historical files are world-writable.]{#sar-world-writable explanation="Monitoring data should retain appropriate access controls."}
:::

## Reading Current Samples

Ask `sar` to collect three CPU reports at one-second intervals:

```bash
$ sar -u 1 3
```

Other common reports include run queue and load (`-q`), memory (`-r`), paging (`-B`), block devices (`-d`), and per-CPU activity (`-P ALL`). Options and fields vary with sysstat version, so consult `sar --help` or the local manual.

:::single-choice{#sar-one-second-count}
What does `sar -u 1 3` request?

::option[Three CPU reports at one-second intervals.]{#sar-three-cpu-samples .correct explanation="The first number is interval seconds and the second is report count."}
::option[One report covering exactly three days.]{#sar-three-days explanation="The operands specify sampling interval and count, not a date range."}
::option[Deletion of three saved CPU files.]{#sar-delete-files explanation="The command reads counters and does not request deletion."}
:::

## Reading Historical Files

Saved file locations and names vary, often under `/var/log/sysstat` or `/var/log/sa`. Pass a selected activity file with `-f`:

```bash
$ sar -q -f /var/log/sysstat/sa02
```

Confirm the file's full date from report headers; a two-digit suffix commonly refers to a day of the month and can be ambiguous across retention periods. Saved binary formats can also require a compatible sysstat version.

:::single-choice{#sar-historical-file-option}
Which option tells `sar` to read a specified activity file?

::option[`-P`]{#sar-option-p explanation="This selects processor reporting rather than an input file."}
::option[`-q`]{#sar-option-q explanation="This selects queue and load reporting."}
::option[`-f`]{#sar-option-f .correct explanation="The file option selects the saved activity data to read."}
:::

## Correlating an Incident

Establish the incident time and timezone, then compare several signals across the same interval. Look for changes in load, CPU, run queue, paging, device activity, network traffic, and application latency. Counter changes show correlation, not necessarily causation; deployment records and application logs may explain the trigger.

Gaps can mean the host was down, the collector failed, or retention removed data. Monitor the monitoring pipeline itself so missing evidence is visible before an incident.

:::single-choice{#sar-incident-method}
How should historical `sar` data be used during an incident review?

::option[Treat the highest single counter as the proven root cause.]{#sar-single-root explanation="One correlation does not establish causation."}
::option[Compare multiple metrics over the same verified time window.]{#sar-correlate-window .correct explanation="Aligned signals help distinguish hypotheses and connect system behavior to the incident."}
::option[Ignore gaps because collection is guaranteed after installation.]{#sar-ignore-gaps explanation="Collection can fail or be disabled, and gaps require explanation."}
:::

## Summary

You can now use `sar` to investigate performance outside an interactive session.

1. Verify that collection and retention are actually active.
2. Request bounded current samples with an interval and count.
3. Select historical activity files explicitly.
4. Align several metrics with incident time and workload evidence.
