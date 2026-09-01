---
lesson_id: "syslog"
course_id: "logging"
lang: "en"
order_index: 2
title: "syslog"
description: "Learn how syslog facilities, severities, routing rules, and the logger command work."
meta_title: "syslog - Logging"
meta_description: "Learn about syslog and rsyslog in Linux, how to manage system logs, and use the logger command. Get started with this beginner-friendly tutorial!"
meta_keywords: "syslog, rsyslog, Linux logs, logger command, /var/log/syslog, Linux tutorial, beginner Linux, system logging"
---

Syslog defines a message model and transport conventions used by many Unix-like systems. Rsyslog is one implementation that can receive, filter, transform, store, and forward messages. It may coexist with `systemd-journald`; neither name means that every application uses that path.

## Facilities and Severities

A syslog message carries a facility describing its broad source category and a severity from emergency through debug. Common facilities include `auth`, `cron`, `daemon`, `kern`, `mail`, `user`, and `local0` through `local7`.

Severities are ordered. In classic selector syntax, `daemon.warning` normally matches daemon messages at warning and all more severe levels, not warning alone. Exact matching uses an equals modifier in implementations that support the classic syntax, such as `daemon.=warning`.

:::single-choice{#syslog-warning-selector} What does a classic selector such as `daemon.warning` normally match?

::option[Only messages whose text contains the word daemon.]{#syslog-text-daemon explanation="Facility metadata, not message-text search, drives this selector."}
::option[Every debug message from every facility.]{#syslog-all-debug explanation="The selector is limited to the daemon facility and a severity threshold."}
::option[Warning messages and more severe daemon messages.]{#syslog-warning-or-higher .correct explanation="The priority selector includes the named severity and levels of greater urgency."}
:::

## Reading rsyslog Rules

Rsyslog commonly loads a main file and snippets under `/etc/rsyslog.d/`. A traditional rule has a selector followed by an action:

```text
auth,authpriv.*          /var/log/auth.log
*.*;auth,authpriv.none  -/var/log/syslog
kern.*                  /var/log/kern.log
```

The first line routes all priorities from two authentication facilities. The second broadly selects messages and excludes those facilities. The third routes kernel-facility messages. A leading `-` on a file action commonly requests asynchronous writes; it does not mean exclusion.

Inspect all included files and validate the exact syntax used by the installed version before changing production routing.

:::single-choice{#syslog-selector-action} In a traditional rsyslog rule, what is the action?

::option[The facility and severity expression on the left.]{#syslog-left-selector explanation="That part selects messages."}
::option[The destination or operation on the right.]{#syslog-right-action .correct explanation="The action determines whether selected records go to a file, remote target, or another output."}
::option[The comment describing the package version.]{#syslog-comment-version explanation="Comments do not perform message routing."}
:::

## Sending a Test Message

Use `logger` to submit a controlled test with an identifiable tag and priority:

```bash
$ logger -p user.notice -t lesson-test 'routing check 2026-08-31T10:00'
```

Then query the expected destination, for example:

```bash
$ journalctl -t lesson-test --since '5 minutes ago'
```

The same event can appear in the journal and a text file, depending on forwarding and routing. `logger -s` also copies the message to standard error; it does not prove durable storage.

:::single-choice{#syslog-logger-tag} What does `logger -t lesson-test` add to the submitted message?

::option[A request to erase older test records.]{#syslog-tag-delete explanation="The option sets an identifying tag and does not manage retention."}
::option[The identifier `lesson-test` as the message tag.]{#syslog-tag-identifier .correct explanation="A unique tag makes the controlled event easier to locate in configured destinations."}
::option[A five-minute delivery delay.]{#syslog-tag-delay explanation="No delivery interval is encoded by the tag option."}
:::

## Changing and Verifying Routing

Before a change, save the current configuration and identify downstream consumers. Validate syntax with the implementation's configuration-check mode, commonly:

```bash
$ sudo rsyslogd -N1
```

Only after validation should you reload the service through its manager. Send a new tagged message, verify every required destination, and check service status and internal error logs. A syntactically valid rule can still route too broadly, duplicate records, or expose sensitive data.

Remote forwarding should use authenticated, encrypted transport when logs cross untrusted networks. UDP delivery has no end-to-end acknowledgement; critical audit requirements need a design that accounts for queues, loss, integrity, access control, and receiver outages.

:::single-choice{#syslog-change-verification} What is sufficient evidence that a new routing rule works?

::option[The configuration file has a recent modification time.]{#syslog-mtime explanation="A timestamp does not prove valid syntax or delivery."}
::option[The sender can reach the receiver with a ping.]{#syslog-ping explanation="Network reachability alone does not verify the logging protocol or storage path."}
::option[Validation passes and a tagged test reaches every intended destination.]{#syslog-validate-and-test .correct explanation="Both static validation and an observed end-to-end event are needed."}
:::

## Summary

You can now test syslog routing from message metadata to its configured destination.

1. Distinguish facilities from ordered severity levels.
2. Read selectors separately from their actions.
3. Send a tagged, prioritized event with `logger`.
4. Validate configuration and verify delivery end to end.
