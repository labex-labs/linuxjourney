---
lesson_id: "security-event-correlation"
course_id: "security-logs"
lang: "en"
order_index: 5
title: "Event Correlation"
description: "Learn how to connect security records using time, host, account, and session information."
meta_title: "Event Correlation - Security Logs"
meta_description: "Compare SSH and sudo records in a short example, align timestamps, and decide what evidence supports a link between events."
meta_keywords: "event correlation, security logs, SSH login records, sudo events, timestamps, session IDs"
---

A login record tells you someone signed in to a machine. Another record tells you a command was approved. Can you connect the two? **Event correlation** means comparing records to see whether they describe related activity.

## Reading Two Records

SSH lets you sign in to another machine. After signing in, a user can request permission to run a command as another account using `sudo`. Below are two simulated records from the same date, written with matching field names for practice. Real logs can use different names or leave some fields out.

```text
t=09:14:02Z      source=ssh   host=web-01 account=alex session=42 login=accepted
t=11:15:10+02:00 source=sudo  host=web-01 account=alex session=42 decision=allowed
```

The `source` field names the tool reporting an event. The `host` field names the machine where it occurred. Both records report activity under the account `alex`. Identifying the person who used that account would take more evidence.

:::single-choice{#security-event-correlation-account-evidence} A teammate says that Alex personally made the sudo request. What do the records establish so far?

::option[Alex personally made the sudo request.]{#security-event-correlation-account-person explanation="An account name alone cannot identify the person who used it."}
::option[The records report activity from two different accounts.]{#security-event-correlation-account-different explanation="Both account fields show alex. The different source fields identify the tools reporting the activity."}
::option[Both events name the same account.]{#security-event-correlation-account-shared .correct explanation="Both records name alex. More evidence would be needed to identify the person using that account."}
:::

## Comparing Event Times

The `t` field contains the recorded time. In the first record, `Z` marks UTC, a common reference for comparing clocks. The second record uses `+02:00`, two hours ahead of UTC. Subtract two hours from `11:15:10` to get `09:15:10` in UTC.

Now compare `09:14:02` and `09:15:10`. The login was recorded first. Events close in time may still come from separate logins.

:::single-choice{#security-event-correlation-time-order} On another day, a login is recorded at `09:14Z` and a request at `11:13+02:00`. What is the order?

::option[The request comes first by one minute.]{#security-event-correlation-time-request-first .correct explanation="Subtract two hours to get 09:13 UTC for the request. The login is at 09:14 UTC."}
::option[The login comes first by one minute.]{#security-event-correlation-time-login-first explanation="The request converts to 09:13 UTC, which is one minute before the login at 09:14 UTC."}
::option[The login comes first by nearly two hours.]{#security-event-correlation-time-unadjusted explanation="This compares the displayed clock readings directly. Convert both to UTC before ordering the events."}
:::

## Checking the Host and Session

A **session** is the period of activity from signing in to signing out or disconnecting. In these practice records, the SSH entry includes the session ID linked to the accepted login. The two sources use the same session ID for that login on the same host. The first two records show `host=web-01` and `session=42`, which links the sign-in and the request to one session.

A session number is local to its host in these samples. The following record has the same account and session number and appears just seconds later.

```text
t=09:15:18Z source=sudo host=web-02 account=alex session=42 decision=allowed
```

![LabEx Terminal displaying simulated records from web-01 and web-02 and a UTC conversion to 09:15:10](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/security-logs/security-event-correlation/utc-correlation.png)

The terminal displays the three simulated records and uses Ubuntu’s `date` command to confirm the UTC conversion.

:::single-choice{#security-event-correlation-host-scope} How does the third record relate to the original SSH session?

::option[It belongs to that session because the account and time are close.]{#security-event-correlation-host-scope-account explanation="Two hosts can record activity under the same account name within seconds of each other."}
::option[It belongs to a separate session because the host differs.]{#security-event-correlation-host-scope-machine .correct explanation="Session 42 on web-02 is local to that host. The original login was on web-01."}
::option[It belongs to that session because the session number matches.]{#security-event-correlation-host-scope-session explanation="A session number is meaningful on its own host in this example. Here the two host names differ."}
:::

## Stating What the Records Support

On `web-01`, the login was accepted and `sudo` gave permission to run a command during that session. That is where the available evidence ends. To learn how the command finished, look for a record that reports its result. A session can contain several commands, so match the result to the specific request. Keep the outcome unknown if you cannot find a matching record.

:::single-choice{#security-event-correlation-completion-evidence} Which new record could resolve whether that command finished successfully?

::option[A result for another command run in the same session.]{#security-event-correlation-completion-other-command explanation="Several commands can run in one session. The result must match the request you are checking."}
::option[A second record showing that the request was allowed.]{#security-event-correlation-completion-permission explanation="This confirms permission to run the command. The outcome still requires a result record."}
::option[A result for the command from that specific request.]{#security-event-correlation-completion-result .correct explanation="A matching result can tell you how the command ended."}
:::

To practice filtering and comparing another set of authentication and sudo records, try [System Log Analysis](https://labex.io/tutorials/linux-system-log-analysis-656124).

## Summary

You can now use more than one security record to make a claim and identify what still needs checking.

1. Identify the account recorded for an event.
2. Convert timestamps to a common time zone before comparing them.
3. Use the host and session together to link activity.
4. State what the records establish and look for evidence that answers the remaining question.
