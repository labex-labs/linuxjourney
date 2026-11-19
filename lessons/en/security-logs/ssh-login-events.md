---
lesson_id: "ssh-login-events"
course_id: "security-logs"
lang: "en"
order_index: 2
title: "SSH Login Events"
description: "Learn how SSH records describe rejected and accepted sign-ins and how to group attempts from one connection."
meta_title: "SSH Login Events - Security Logs"
meta_description: "Read SSH log fields for the target account, remote address, sign-in method, and outcome, then use a connection identifier to compare attempts."
meta_keywords: "SSH login events, SSH logs, accepted login, rejected login, authentication methods"
---

**SSH**, short for Secure Shell, lets you sign in to another computer over a network. The receiving machine can log each attempt. Those records tell you which account was presented and whether the server accepted the proof offered to sign in.

## Reading the Outcome

Here are two simulated SSH records. The `login` field gives the outcome. A rejected attempt failed the sign-in check. An accepted attempt passed it.

```text
t=09:13:48Z source=ssh host=web-01 account=alex login=rejected
t=09:14:02Z source=ssh host=web-01 account=alex login=accepted
```

The first record describes a rejection for `alex`. The second describes an accepted attempt for the same account. Each outcome applies to its own attempt.

:::single-choice{#ssh-login-events-outcome-order} Which statement follows from these two records?

::option[The later attempt passed the sign-in check.]{#ssh-login-events-outcome-later .correct explanation="The second record shows login=accepted at 09:14:02."}
::option[Both attempts passed the sign-in check.]{#ssh-login-events-outcome-both explanation="The earlier line records a rejected attempt."}
::option[The later attempt failed the sign-in check.]{#ssh-login-events-outcome-failed explanation="Rejected describes the first attempt. The second was accepted."}
:::

## Reading Addresses and Methods

A remote address tells you where the receiving machine saw the connection come from. In this sample, it appears as `peer`. A network address can be shared, so the field alone gives no name for the person using it.

```text
t=09:14:02Z source=ssh host=web-01 account=alex login=accepted
peer=192.0.2.10 method=publickey connection=17
```

The second line continues the same record. The `method` field describes the kind of proof SSH checked. `password` means SSH checked a password. `publickey` means the connecting device proved it could use a key the server accepts for that account.

:::single-choice{#ssh-login-events-method-evidence} Which finding is supported for the accepted attempt?

::option[The server accepted a sign-in using a password.]{#ssh-login-events-method-password explanation="The password method would be shown separately. This record names the public key method."}
::option[The server identified the person at that address.]{#ssh-login-events-method-person explanation="The address describes the connection as seen by the host. It does not establish who was at the keyboard."}
::option[The server accepted a sign-in using a key.]{#ssh-login-events-method-key .correct explanation="The record shows both login=accepted and method=publickey."}
:::

## Grouping Attempts by Connection

A **connection** is the network link SSH uses to exchange messages. In these samples the host assigns an identifier to each connection. Multiple sign-in attempts can occur over one connection, and a new connection can come from the same address.

```text
t=09:13:48Z host=web-01 account=alex peer=192.0.2.10 connection=17 login=rejected
t=09:13:55Z host=web-01 account=alex peer=192.0.2.10 connection=18 login=rejected
t=09:14:02Z host=web-01 account=alex peer=192.0.2.10 connection=17 login=accepted
```

On `web-01`, the first and last records share connection 17. Read that identifier together with the host.

![LabEx Terminal displaying simulated SSH attempts from one address with connection IDs 17 and 18](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/security-logs/ssh-login-events/ssh-connections.png)

This terminal view puts the three simulated attempts together so you can compare their connection numbers.

:::single-choice{#ssh-login-events-group-connection} Which records refer to connection 18 on web-01?

::option[The attempts at 09:13:48 and 09:14:02.]{#ssh-login-events-group-seventeen explanation="Those two rows carry connection 17."}
::option[Only the attempt at 09:13:55.]{#ssh-login-events-group-eighteen .correct explanation="Only that row shows connection 18 on web-01."}
::option[All three attempts from 192.0.2.10.]{#ssh-login-events-group-address explanation="Both connection numbers appear under the same address."}
:::

## Following an Accepted Sign-In

A successful sign-in tells you that SSH accepted the account's proof. To learn what happened after that, look for a record that a **session** opened. A login session tracks activity after the sign-in. A successful sign-in record alone describes the sign-in check.

:::single-choice{#ssh-login-events-after-accepted} Which record would help you check whether an accepted sign-in led to an open session?

::option[Another record that the same sign-in was accepted.]{#ssh-login-events-after-accepted-again explanation="It would repeat the result of the sign-in check."}
::option[An earlier rejection for the account on another host.]{#ssh-login-events-after-other-host explanation="That record describes a separate attempt on a different machine."}
::option[A record that the session opened for that sign-in.]{#ssh-login-events-after-session .correct explanation="An opening record describes the next stage and can connect it to the accepted sign-in."}
:::

## Summary

You can now read the outcome of an SSH attempt and decide which records belong together.

1. Distinguish accepted and rejected sign-ins.
2. Use the remote address and method fields to describe the attempt.
3. Group records by host and connection when identifiers are available.
4. Look for a session record to check what followed a successful sign-in.
