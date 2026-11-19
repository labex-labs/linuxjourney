---
lesson_id: "linux-service-accounts"
course_id: "linux-hardening"
lang: "en"
order_index: 2
title: "Service Accounts"
description: "Learn to identify the account a Linux process runs under and reason about its access."
meta_title: "Service Accounts - Linux Hardening"
meta_description: "Learn to identify the account a Linux process runs under and reason about its access."
meta_keywords: "service accounts, linux hardening, cybersecurity, Linux Journey"
---

A web server starts as a process. Linux associates each process with an identity that helps determine what the program can read or change. A **service account** is an identity set aside for a program.

## Reading the Process Identity

In a normal terminal, `$$` gives the shell's process ID. Use it to see the identity of your own shell. The `-p` option selects that process and `-o` chooses the displayed columns. The equals signs omit the column headings.

```bash
$ ps -p "$$" -o user=,comm=
```

On a LabEx terminal the account might be `labex`. The command column names the shell program. The corresponding fields for a service process tell you which account it uses, regardless of who launched it.

:::single-choice{#linux-service-accounts-process-user} Which field tells you the account associated with the selected process?

::option[The process ID supplied with -p.]{#linux-service-accounts-process-user-a explanation="A process ID selects one running process."}
::option[The command name in the last column.]{#linux-service-accounts-process-user-c explanation="That names the running program."}
::option[The user field printed by ps.]{#linux-service-accounts-process-user-b .correct explanation="The user field displays the process identity."}
:::

![Ps output showing the LabEx shell process and its labex account](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/linux-hardening/linux-service-accounts/shell-identity.png)

## Choosing a Dedicated Identity

Consider a web service whose only jobs are reading pages and writing its own log. A dedicated `site-web` account can be given those permissions. Running it with an administrator's broader access would give the program more ways to change the host than it needs.

:::single-choice{#linux-service-accounts-isolate-service} Which access plan fits that service's work?

::option[Let site-web edit every user's files.]{#linux-service-accounts-isolate-service-b explanation="The service has no task that requires that scope."}
::option[Let site-web read pages and write its own log.]{#linux-service-accounts-isolate-service-a .correct explanation="These rights match the two stated jobs."}
::option[Let site-web act as the administrator for every request.]{#linux-service-accounts-isolate-service-c explanation="Most requests need only the service's narrow access."}
:::

## Checking Multiple Processes

Some services use separate processes for different responsibilities. Check the process that handles the request before explaining which permissions apply to it. If you change the running identity, confirm the service can still read its inputs and write only what it needs.

:::single-choice{#linux-service-accounts-verify-identity} A maintenance tool reports a supervisor as root. What tells you which account serves the web requests?

::option[The identity of the worker process that handles requests.]{#linux-service-accounts-verify-identity-c .correct explanation="Inspecting the relevant process matches the account to the actual work."}
::option[The filename of the service configuration alone.]{#linux-service-accounts-verify-identity-a explanation="The filename does not identify the worker's runtime identity."}
::option[The name of the person who opened the terminal.]{#linux-service-accounts-verify-identity-b explanation="The terminal user can differ from the running service."}
:::

## Summary

You can now connect a Linux process to its runtime identity.

1. Find a process's user in ps output.
2. Choose permissions that fit a service's job.
3. Inspect the relevant process in a multi-process service.
