---
lesson_id: "security-events"
course_id: "security-logs"
lang: "en"
order_index: 1
title: "Security Events"
description: "Learn to distinguish a security event, the record that describes it, and an alert that calls for review."
meta_title: "Security Events - Security Logs"
meta_description: "Read a short Linux security record, compare it with an alert, and choose what to check when the available records leave a question open."
meta_keywords: "security events, security logs, log records, alerts, Linux logging"
---

A server reports a failed sign-in. What happened, and what does that tell you? Start by separating what the machine recorded from any conclusion you might draw.

## Events and Log Records

An **event** is something that happened, such as a rejected sign-in attempt. A **log record** is a saved description of an event. A **log** is a collection of records. The examples in this course use simulated records with consistent field names so you can practice reading them. Real tools label and store their records in different ways.

```text
t=08:55:00Z source=ssh host=web-01 account=alex login=rejected
```

This record reports a rejected remote sign-in for the account `alex`. You can read the saved record after the attempt. Later lessons show how timestamps from different sources can be compared.

![LabEx Terminal displaying a simulated rejected SSH sign-in record for alex on web-01](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/security-logs/security-events/event-fields.png)

The LabEx terminal displays the same simulated record from a text file.

:::single-choice{#security-events-event-versus-record} Which part of the example is the event itself?

::option[The saved line describing the rejection.]{#security-events-event-line explanation="The line is the record you can read after the event."}
::option[The later review of the saved line.]{#security-events-event-review explanation="Reading the line is a later action. The event described in it is the rejected sign-in."}
::option[The sign-in attempt was rejected.]{#security-events-event-attempt .correct explanation="The rejection took place on the server. The log line records what happened."}
:::

## Reading Fields

A **field** is one piece of information in a record. In these examples, `t` gives the recorded time, `host` names the computer where it happened, and `source` identifies the tool that reported it. The `account` field names the account in the record. The `login` field gives the outcome of the sign-in attempt.

:::single-choice{#security-events-field-host} You want to know which machine recorded the rejected sign-in. Which value identifies it?

::option[`alex` from the account field.]{#security-events-field-host-account explanation="The account field names the account involved in the attempt."}
::option[`web-01` from the host field.]{#security-events-field-host-web .correct explanation="The host field identifies the machine where the event occurred."}
::option[`ssh` from the source field.]{#security-events-field-host-tool explanation="The source field identifies the tool that reported the event."}
:::

## Alerts and Their Rules

An **alert** draws attention to something that may need review. A monitoring rule can generate an alert after seeing three rejected sign-ins for the same account on the same host within five minutes. That rule groups records by account, host, and time. An alert means the rule matched. A person might simply have mistyped a password several times.

:::single-choice{#security-events-alert-interpretation} The rule alerts on three failures for alex on web-01. What does the alert support?

::option[The recorded failures met the rule's conditions.]{#security-events-alert-condition .correct explanation="The alert points to a pattern worth reviewing. Its rule makes no claim about who caused it."}
::option[Three different people tried to sign in.]{#security-events-alert-people explanation="Three attempts can come from one person or several. The rule counts records."}
::option[Someone successfully signed in after three tries.]{#security-events-alert-success explanation="The rule counts rejected sign-ins. It says nothing about a later success."}
:::

## Choosing What to Check Next

If the question is whether `alex` later signed in, look for a sign-in outcome on `web-01` after the failures. Check what time period the records cover before drawing a conclusion. A log export, which is a copy of selected records, may end before the period you need.

:::single-choice{#security-events-next-record} Your export ends at 09:00. You need to check for a successful sign-in at 09:05. What should you look for?

::option[The same export sorted from newest to oldest.]{#security-events-next-sort explanation="Sorting changes the order. It cannot add coverage after 09:00."}
::option[Sign-in records covering 09:05 on web-01.]{#security-events-next-window .correct explanation="You need the relevant source and a time window that includes the event you are checking."}
::option[Another count of the failures before 09:00.]{#security-events-next-count explanation="The count describes a different result in an earlier time window."}
:::

## Summary

You can now read a security record and decide what to check after an alert.

1. Distinguish an event from the line that records it.
2. Find the account, host, and outcome in a sample record.
3. Use an alert rule to understand what was observed.
4. Check that the source and time window answer your question.
