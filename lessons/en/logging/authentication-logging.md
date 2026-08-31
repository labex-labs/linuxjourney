---
lesson_id: "authentication-logging"
course_id: "logging"
lang: "en"
order_index: 5
title: "Authentication Logging"
description: "Learn how to locate, interpret, and safely correlate Linux authentication records."
meta_title: "Authentication Logging - Logging"
meta_description: "Explore Linux authentication logging by examining the /var/log/auth.log file. This guide helps beginners understand user login events, authentication methods, and how to troubleshoot access issues for better Linux security."
meta_keywords: "Linux authentication, auth.log, Linux logging, user login, Linux security, system authorization, troubleshoot login, authentication methods, beginner, tutorial, guide, secure log"
---

Authentication logs help explain login attempts, privilege changes, and session activity. They are security-sensitive evidence, but one line rarely establishes a user's intent or proves that an account was compromised.

## Locating Authentication Records

Debian-family syslog configurations commonly route authentication events to `/var/log/auth.log`; Red Hat-family configurations commonly use `/var/log/secure`. A systemd journal may retain the same events with unit and process metadata, and centralized logging may hold the authoritative copy.

Discover the local destination and query the relevant service, for example:

```bash
$ sudo journalctl -u ssh.service --since '1 hour ago'
$ sudo less /var/log/auth.log
```

The SSH unit can be named `ssh.service` or `sshd.service`. Permissions commonly restrict these records because they expose account and access details.

:::single-choice{#auth-logs-file-location}
Where must Linux authentication events always be stored?

::option[In the destination selected by local logging policy.]{#auth-logs-local-policy .correct explanation="Files, the journal, and centralized collectors vary by distribution and configuration."}
::option[In `/var/log/auth.log` on every distribution.]{#auth-logs-auth-only explanation="That path is common on Debian-family systems but is not universal."}
::option[Inside each user's shell history file.]{#auth-logs-shell-history explanation="Shell history is user-command history, not the system authentication event store."}
:::

## Interpreting an Event

A traditional record might contain:

```text
Jan 31 10:37:50 icebox pkexec: pam_unix(polkit-1:session): session opened for user root by (uid=1000)
```

This identifies the time, host, emitting program, PAM module and service, requested session user, and originating UID. It does not by itself identify the human behind UID 1000 or prove that the action was malicious. Resolve the UID against account records valid at the incident time and correlate terminal, remote address, session, and surrounding events.

:::single-choice{#auth-logs-uid-inference}
What does `uid=1000` establish in this record?

::option[That the root password was typed incorrectly one thousand times.]{#auth-logs-thousand-passwords explanation="The value is an identity number, not an attempt count."}
::option[The numeric account identity associated with the initiating process.]{#auth-logs-numeric-identity .correct explanation="Additional session and account evidence is needed to attribute the action to a person."}
::option[That the event originated from TCP port 1000.]{#auth-logs-port explanation="A UID is not a network port field."}
:::

## Investigating Success and Failure

Search for both accepted and rejected attempts in a bounded time range. For SSH, also examine connection source, authentication method, target account, session open and close, and service restarts. Repeated failures can be user error, automation with stale credentials, scanning, or an attack; rate alone does not select one explanation.

`last` and `lastb` can summarize records from `wtmp` and `btmp` where maintained, but those binary databases have their own retention and integrity limits. Cross-check them with journal or syslog records and centralized sources.

:::single-choice{#auth-logs-failed-attempts}
What should repeated failed logins be correlated with?

::option[Only the total free disk space.]{#auth-logs-disk-space explanation="Capacity does not identify the source, target, or method of an authentication attempt."}
::option[Source, target account, method, timing, and successful sessions.]{#auth-logs-correlated-fields .correct explanation="These details help distinguish misconfiguration, user error, scanning, and unauthorized access."}
::option[A conclusion that the account is certainly compromised.]{#auth-logs-certain-compromise explanation="Failures can have several benign or hostile causes."}
:::

## Preserving and Responding

If an incident is suspected, record host time and timezone, preserve original logs and metadata, and secure any exported copy. Avoid editing evidence in place. Account locks, firewall changes, and session termination can interrupt legitimate access or alert an attacker, so follow the incident-response process and retain a recovery path.

:::single-choice{#auth-logs-preservation}
How should authentication evidence be handled during an investigation?

::option[Edit suspicious lines in the original file for clarity.]{#auth-logs-edit-original explanation="Changing the source damages evidence integrity."}
::option[Publish the complete log so anyone can identify users.]{#auth-logs-publish explanation="Authentication records can expose sensitive identities and infrastructure details."}
::option[Preserve originals and protect exported copies.]{#auth-logs-preserve .correct explanation="Integrity and confidentiality are both important for security logs."}
:::

## Summary

You can now examine authentication events without overclaiming what one record proves.

1. Discover the locally configured authentication-log destination.
2. Interpret identity, service, method, and session fields in context.
3. Correlate failed and successful activity across retained sources.
4. Preserve evidence and coordinate disruptive response actions.
