---
lesson_id: "sudo-events"
course_id: "security-logs"
lang: "en"
order_index: 3
title: "sudo Events"
description: "Learn how sudo records identify who requested a command, which account it would run as, and whether it was allowed."
meta_title: "sudo Events - Security Logs"
meta_description: "Read sudo records by separating the requesting account, target account, command, and permission decision."
meta_keywords: "sudo events, sudo logs, sudo authorization, target account, Linux permissions"
---

A user can sign in under an ordinary account and later need to do a task that requires more permissions. On a system that uses `sudo`, the user can ask to run a command as a different account. The record of that request can show which permissions were requested and what the system decided.

## Finding the Two Accounts

The simulated records below use `account` for the account that made the request and `target` for the account the requested command would run as. The `root` account has system administration privileges. A `sudo` request can name a different target account, such as `backup`.

```text
t=09:15:10Z source=sudo host=web-01 account=alex target=root
command=systemctl status nginx decision=allowed session=42
```

The second line continues the record. Here `alex` made the request and asked to run the command as `root`.

:::single-choice{#sudo-events-account-target} In a record with `account=sam target=backup`, who asked to run the command and as which account?

::option[Backup requested it as sam.]{#sudo-events-target-swapped explanation="The account field shows who made the request. The target field shows the requested command identity."}
::option[Sam requested it as backup.]{#sudo-events-target-backup .correct explanation="Read account as the requester and target as the account the command would use."}
::option[Sam requested it as root.]{#sudo-events-target-root explanation="Root is one possible target. This record names backup."}
:::

## Reading the Requested Command

The `command` field names the command covered by the request. In the sample, `systemctl status nginx` asks to display the current status of the Nginx web service. Another record might show `systemctl restart nginx`, a request to stop and start that service again. Both mention the same service and describe different actions.

:::single-choice{#sudo-events-command-scope} Which request asks to change the running state of the web service?

::option[`systemctl restart nginx`]{#sudo-events-command-restart .correct explanation="Restart asks to stop and start the service. It can change the running state."}
::option[`systemctl status nginx`]{#sudo-events-command-status explanation="Status asks to display service information. It does not request a restart."}
::option[Either request, because both name nginx.]{#sudo-events-command-both explanation="The service name is the same. The action word identifies what the requester asked for."}
:::

## Reading the Decision

The **policy** is the set of rules `sudo` uses to decide whether to allow a request. In our samples, `decision=allowed` means the policy permitted that request. `decision=denied` means `sudo` refused it.

```text
t=09:16:00Z source=sudo host=web-01 account=alex target=root
command=systemctl restart nginx decision=denied session=42
```

An allowed decision describes permission. If you need the command result, look for a result record when the system provides one.

![LabEx Terminal displaying simulated sudo records with an allowed status check and a denied restart](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/security-logs/sudo-events/sudo-decisions.png)

Compare the requested commands and decisions in these two simulated records.

:::single-choice{#sudo-events-denied-request} What does the second example say happened to the restart request?

::option[Sudo refused the request to restart it.]{#sudo-events-denied-refused .correct explanation="The command names the requested action and denied gives the permission decision."}
::option[The service restarted successfully.]{#sudo-events-denied-success explanation="This record shows a refusal. It gives no evidence of a successful restart."}
::option[The earlier status request was also refused.]{#sudo-events-denied-earlier explanation="Each decision applies to its own request. The earlier record shows allowed."}
:::

## Keeping the Login Account in View

Both examples name `alex` as the requester and include `session=42`. This number refers to the login session, the period of activity after signing in. It helps you find the surrounding login records. The target in each example applies to that one command request. Use the requester and target fields together when describing it.

:::single-choice{#sudo-events-session-interpretation} Which summary fits the first sample?

::option[Root signed in directly and opened session 42.]{#sudo-events-session-root-login explanation="This is a sudo record. Its target field does not describe a separate sign-in."}
::option[Alex requested root permissions for every command in the session.]{#sudo-events-session-all-commands explanation="The record names one command. It does not cover every command in the session."}
::option[Alex requested to run one named command as root in session 42.]{#sudo-events-session-one-command .correct explanation="The requester, target, command, and session fields together support that statement."}
:::

## Summary

You can now read a sudo record without confusing a permission decision with a command result.

1. Identify the requesting and target accounts.
2. Use the command field to describe the specific request.
3. Distinguish permission granted from permission denied.
4. Keep the login session in view when describing a request.
