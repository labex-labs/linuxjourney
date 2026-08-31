---
lesson_id: "cron-jobs"
course_id: "process-utilization"
lang: "en"
order_index: 8
title: "Cron Jobs"
description: "Learn how to create, inspect, test, and safely operate recurring jobs with cron."
meta_title: "Cron Jobs - Process Utilization"
meta_description: "Learn how to schedule tasks and automate scripts in Linux using cron jobs. This guide covers crontab syntax, essential commands like crontab -e, and practical examples for beginners."
meta_keywords: "cron jobs, crontab, schedule tasks, Linux automation, Linux commands, beginner Linux, Linux tutorial, crontab -e, cron"
---

Cron runs commands on recurring schedules without an interactive shell. Automation repeats both correct behavior and mistakes, so test the command, use explicit paths, constrain privileges, and plan logging and failure notification before scheduling it.

## Reading a Crontab Entry

A user crontab entry contains five time fields followed by a command:

```cron
30 8 * * * /home/pete/scripts/change_wallpaper
```

From left to right, the fields are minute, hour, day of month, month, and day of week. This example runs at 08:30 according to the cron daemon's applicable timezone. An asterisk means every permitted value in that field.

When both day-of-month and day-of-week fields are restricted, many cron implementations run when either field matches. Confirm local semantics before building a schedule that uses both.

:::single-choice{#cron-daily-eight-thirty}
When does `30 8 * * * command` run?

::option[Every 30 minutes for eight hours.]{#cron-every-thirty explanation="The fields are positions in a schedule, not a duration expression."}
::option[At 08:30 each day.]{#cron-eight-thirty .correct explanation="Minute 30 and hour 8 are fixed while the three date fields allow every value."}
::option[At 30:08 on the eighth day of each month.]{#cron-invalid-time explanation="Hours range from 0 through 23, and the example does not restrict day of month."}
:::

## Managing a User Crontab

Edit the current user's crontab with:

```bash
$ crontab -e
```

List the installed entries before and after a change:

```bash
$ crontab -l
```

`crontab -r` removes the user's entire crontab and may do so without an editor. Do not use it to remove one line; edit the crontab and verify the remaining entries.

:::single-choice{#cron-list-current-user}
Which command lists the current user's installed cron entries?

::option[`crontab -l`]{#cron-list .correct explanation="The list option prints the installed entries for inspection."}
::option[`crontab -r`]{#cron-remove-all explanation="This option removes the crontab instead of displaying it."}
::option[`crontab -e`]{#cron-edit explanation="This opens the crontab for editing rather than simply listing it."}
:::

## Accounting for the Cron Environment

Cron commonly supplies a limited environment and a noninteractive shell. Use absolute command and file paths, set required variables explicitly, and do not depend on aliases, a current terminal directory, or shell startup files.

Redirect standard output and error to a controlled log or use a notification mechanism appropriate to the system. Protect credentials with restrictive permissions and avoid embedding secrets directly in a crontab command.

:::single-choice{#cron-absolute-paths}
Why should a cron command use explicit paths and environment settings?

::option[Cron always runs inside the user's current terminal.]{#cron-current-terminal explanation="Scheduled jobs run independently of an interactive session."}
::option[Absolute paths make every command run as root.]{#cron-path-root explanation="Paths select files but do not grant privileges."}
::option[Cron's environment can differ from the interactive shell.]{#cron-limited-environment .correct explanation="Explicit dependencies prevent failures caused by PATH, directory, or startup-file assumptions."}
:::

## Testing and Preventing Overlap

Run the script manually as the same user with a similarly minimal environment. Make it return useful exit statuses and write timestamped results. After installation, wait for a harmless test schedule or controlled run and verify the actual side effect and logs.

If one run might last longer than its interval, design for concurrency or use a locking mechanism such as `flock` where available:

```cron
*/5 * * * * /usr/bin/flock -n /run/user/1000/report.lock /home/pete/bin/report
```

Choose a lock path the job user may safely create, and decide whether skipped runs are acceptable. Cron does not automatically guarantee that only one instance runs.

:::single-choice{#cron-overlapping-runs}
What risk exists when a job takes longer than its schedule interval?

::option[Several instances can overlap and contend for resources.]{#cron-overlap .correct explanation="Cron can start a new occurrence while the previous process is still running."}
::option[The five schedule fields automatically gain a sixth lock field.]{#cron-auto-lock explanation="Crontab syntax does not add automatic mutual exclusion."}
::option[The script is permanently converted into a kernel thread.]{#cron-kernel-thread explanation="Scheduling a command does not change its process model in this way."}
:::

## Choosing the Right Scheduler

Cron is appropriate for simple recurring commands. Systemd timers can provide dependency integration, persistent catch-up behavior, randomized delay, and journal logging on systemd hosts. Application or cluster schedulers may be safer when a job must run exactly once across multiple machines.

:::single-choice{#cron-cluster-exactly-once}
Why might ordinary per-host cron be unsuitable for a clustered exactly-once job?

::option[Every cron entry is limited to one character.]{#cron-one-character explanation="Crontab commands can contain normal command lines."}
::option[Each host can independently start its own copy.]{#cron-each-host .correct explanation="A distributed coordination mechanism is needed to enforce one execution across hosts."}
::option[Cron cannot execute scripts stored on disk.]{#cron-no-scripts explanation="Running scripts is a common cron use case."}
:::

## Summary

You can now operate a recurring cron job with explicit schedule and execution assumptions.

1. Read the five time fields in their defined order.
2. Inspect and edit user crontabs without deleting unrelated jobs.
3. Define paths, environment, logging, and credential handling.
4. Test as the job user and protect against unwanted overlap.
5. Choose a scheduler that matches host and coordination requirements.
