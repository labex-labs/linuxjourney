---
lesson_id: "managing-log-files"
course_id: "logging"
lang: "en"
order_index: 6
title: "Managing Log Files"
description: "Learn how to configure, test, and verify safe text-log rotation with logrotate."
meta_title: "Managing Log Files - Logging"
meta_description: "Master Linux log management with this beginner's guide to logrotate. Learn how log rotation saves disk space, how to configure it, and keep your system's logs organized."
meta_keywords: "logrotate, Linux logs, log management, log rotation, Linux tutorial, beginner, guide, disk space"
---

Unbounded text logs can exhaust a filesystem, while overly aggressive deletion can remove evidence required for operations or compliance. `logrotate` applies configured size, time, compression, ownership, and retention policies to file-based logs.

## Understanding Rotation

A typical rotation renames the active file, creates a replacement, optionally asks the application to reopen it, compresses older generations, and removes files beyond retention. These steps depend on configuration; rotation is not a backup because retained copies can still be deleted, corrupted, or lost with the same host.

:::single-choice{#logrotate-not-backup} Why is log rotation not a substitute for backup or archival?

::option[Rotated files remain subject to local retention and host failure.]{#logrotate-local-retention .correct explanation="Rotation controls working log generations but does not create an independent durable copy."}
::option[Rotation can only process image files.]{#logrotate-images explanation="The utility is designed primarily for log files."}
::option[Every rotation keeps all generations forever.]{#logrotate-forever explanation="Retention rules normally remove older generations."}
:::

## Finding Configuration

The main file is commonly `/etc/logrotate.conf`, with package or application snippets under `/etc/logrotate.d/`. A simplified policy can look like:

```text
/var/log/example/app.log {
    daily
    rotate 7
    compress
    delaycompress
    missingok
    notifempty
    create 0640 example adm
}
```

This requests daily evaluation, seven retained rotations, compression delayed by one generation, tolerance for a missing or empty log, and a newly created file with explicit mode and ownership. Actual rotation also depends on recorded state and how the scheduler invokes logrotate.

:::single-choice{#logrotate-rotate-seven} What does `rotate 7` specify?

::option[Keep up to seven rotated generations under the policy.]{#logrotate-seven-generations .correct explanation="Older generations are removed when the configured retention is exceeded."}
::option[Run the application seven times per day.]{#logrotate-run-seven explanation="The directive controls retained generations rather than application execution."}
::option[Set every rotated file's permissions to mode 0007.]{#logrotate-mode-seven explanation="File mode is controlled by directives such as `create`."}
:::

## Coordinating with the Writer

After renaming a log, a daemon can continue writing through its still-open file descriptor. A `postrotate` script often sends a documented reload or reopen signal. Validate the exact application behavior and keep the script narrowly scoped.

`copytruncate` copies a file and truncates the original in place when an application cannot reopen logs. Writes can be lost or duplicated during the copy-and-truncate window, so it is a compromise rather than a universally safe default.

:::single-choice{#logrotate-open-descriptor} Why might an application need a reopen signal after rotation?

::option[Its open descriptor can still reference the renamed file.]{#logrotate-descriptor-renamed .correct explanation="Reopening makes future writes use the newly created active path."}
::option[Compression automatically stops every application process.]{#logrotate-compression-stops explanation="Compression does not inherently manage the writer's process lifecycle."}
::option[The kernel forbids creating a second log file.]{#logrotate-kernel-forbids explanation="Multiple log files can exist; the issue is which inode the writer has open."}
:::

## Testing Before Activation

Use debug mode to inspect decisions without rotating files:

```bash
$ sudo logrotate -d /etc/logrotate.conf
```

Debug output does not prove that permissions, scripts, free space, or application reopening will succeed during a real run. Test a new rule in a controlled environment, then inspect the active file, rotated generation, ownership, compression, application output, and logrotate status after execution. `-f` forces rotation and is state-changing; do not confuse it with a dry run.

:::single-choice{#logrotate-debug-mode} What does `logrotate -d` provide?

::option[A permanent deletion of all expired logs.]{#logrotate-debug-delete explanation="Debug mode reports intended decisions without performing rotation."}
::option[A forced production rotation regardless of policy.]{#logrotate-debug-force explanation="The force option is `-f`, which is state-changing."}
::option[Diagnostic evaluation without modifying log files or state.]{#logrotate-debug-dry .correct explanation="It is the appropriate first syntax and decision review, followed by controlled real verification."}
:::

## Accounting for Other Stores

Logrotate manages files named by its policies. The systemd journal has its own size and retention configuration, while databases and remote logging services have separate lifecycle controls. Monitor filesystem capacity and logging health so a stuck writer or failed rotation is detected before space is exhausted.

:::single-choice{#logrotate-journal-retention} Does a logrotate rule automatically enforce systemd journal retention?

::option[No, journal storage has its own configuration and limits.]{#logrotate-journal-separate .correct explanation="Logrotate only manages paths selected by its file policies."}
::option[Yes, because all logs share one retention engine.]{#logrotate-all-logs explanation="File rotation and journal retention are separate mechanisms."}
::option[Yes, but only when no text log exists.]{#logrotate-journal-fallback explanation="The presence of text logs does not merge the two retention systems."}
:::

## Summary

You can now design and verify a file-log rotation policy without mistaking it for archival.

1. Balance space, operational, and retention requirements.
2. Define generations, compression, ownership, and empty-file behavior.
3. Coordinate safely with applications that keep descriptors open.
4. Debug configuration before a controlled real rotation.
5. Manage journal and external-store retention separately.
