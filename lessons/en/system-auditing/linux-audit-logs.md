---
lesson_id: "linux-audit-logs"
course_id: "system-auditing"
lang: "en"
order_index: 2
title: "Linux Audit Logs"
description: "Learn to group Linux audit records that describe a single recorded operation."
meta_title: "Linux Audit Logs - System Auditing"
meta_description: "Learn to group Linux audit records that describe a single recorded operation."
meta_keywords: "linux audit logs, system auditing, cybersecurity, Linux Journey"
---

Linux Audit can write several records about one event. One row may describe the operation while another supplies a path. Group related rows before deciding what they show.

## Reading the Shared Event

The values below are abbreviated practice records from the same host and date. The number after the colon in the audit event reference helps group records with the same timestamp and event ID. These lines belong to the same event.

```text
type=SYSCALL msg=audit(1763456400.120:42) success=yes auid=1001 euid=0
type=PATH    msg=audit(1763456400.120:42) name="/etc/journey/site.conf"
```

The first line gives the outcome and account fields. The path line names a file associated with the event.

:::single-choice{#linux-audit-logs-group-rows} Which fields let you connect the operation to the path in this example?

::option[The two record types SYSCALL and PATH alone.]{#linux-audit-logs-group-rows-a explanation="Those types describe the role of each row. Many events can contain the same types."}
::option[The fact that both rows begin with type.]{#linux-audit-logs-group-rows-c explanation="Every row can have a type while describing different events."}
::option[The matching audit reference on the same host.]{#linux-audit-logs-group-rows-b .correct explanation="It groups the rows that describe event 42."}
:::

![Simulated Linux Audit SYSCALL and PATH rows sharing the same audit event reference](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/system-auditing/linux-audit-logs/grouped-event.png)

## Reading Two Identities

In this sample, `auid` is the audit login user ID and `euid` is the effective user ID for the action. A program can use an effective identity different from the login identity. A numeric ID identifies an account on the host. Additional records may be needed to identify the person behind it.

:::single-choice{#linux-audit-logs-identify-login} Which field shows the login audit identity in the sample?

::option[Euid 0.]{#linux-audit-logs-identify-login-b explanation="It gives the program's effective identity for the event."}
::option[Auid 1001.]{#linux-audit-logs-identify-login-a .correct explanation="Auid is the audit login user ID, while euid is the effective identity."}
::option[The event number 42.]{#linux-audit-logs-identify-login-c explanation="That number groups records and is separate from account identities."}
:::

## Keeping the Finding Narrow

The result field reports that the recorded operation succeeded. Inspect the full event to identify the operation. To check whether the file contents changed, compare the file with a known reference.

:::single-choice{#linux-audit-logs-useful-follow-up} What would help determine whether the contents differ from the approved file?

::option[A comparison against an approved reference copy or integrity record.]{#linux-audit-logs-useful-follow-up-c .correct explanation="That evidence can show what changed at the file level."}
::option[A second audit entry reporting another successful operation.]{#linux-audit-logs-useful-follow-up-a explanation="That can establish another recorded action. It does not compare this file's current bytes with the approved copy."}
::option[The login account ID from the same event.]{#linux-audit-logs-useful-follow-up-b explanation="The login ID helps identify the account context. It cannot describe changes to the file bytes."}
:::

## Summary

You can now use a record group to read one audit event.

1. Match records using the host and audit event reference.
2. Read the login and effective identities separately.
3. Choose a follow-up when the recorded outcome leaves a question open.
