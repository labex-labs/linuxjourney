---
lesson_id: "process-permissions"
course_id: "permissions"
lang: "en"
order_index: 7
title: "Process Permissions"
description: "Learn how real, effective, and saved user IDs help Linux processes track callers and manage privilege."
meta_title: "Process Permissions - Permissions"
meta_description: "Learn about Linux process permissions, including Real, Effective, and Saved User IDs. Understand how UIDs impact security and command execution. Start learning today!"
meta_keywords: "Linux process permissions, Real UID, Effective UID, Saved UID, Linux security, passwd command, Linux tutorial, beginner Linux"
---

Linux authorization checks act on process credentials rather than directly on a typed username. A process has several related user and group IDs, each serving a different role. Most ordinary programs start with matching identities, while privileged programs can use distinct values deliberately.

## Real User ID

The real user ID identifies the account that started the process or its ancestor login session. Programs can consult it to distinguish the caller from an elevated effective identity.

For an ordinary command started by user Bob, the real user ID normally equals Bob's UID. Creating another process does not create a new account or change this identity by itself.

:::single-choice{#process-permissions-real-uid}
What does a process's real user ID normally identify?

::option[The owner of the most recently opened file.]{#process-permissions-real-opened-file explanation="Opening a file does not replace the process's real UID with that file's owner."}
::option[The account associated with the process's original caller.]{#process-permissions-real-caller .correct explanation="The real UID records the calling user identity inherited when the process is launched."}
::option[The group selected for every access check.]{#process-permissions-real-group explanation="A UID is a user identity; group checks use separate group credentials."}
:::

## Effective User ID

The effective user ID is the user credential used for many filesystem and privilege checks. Ordinarily it matches the real UID. Executing an honored setuid program can instead initialize it from the executable's owner.

For example, a carefully designed password utility may run with an elevated effective UID so it can update protected authentication data. The program must still enforce policy based on the caller, requested account, PAM results, and other context. Possessing an effective UID does not automatically make every requested operation legitimate.

:::single-choice{#process-permissions-effective-uid}
Which user ID is used for many access-control decisions made on behalf of a process?

::option[The effective user ID.]{#process-permissions-effective-active .correct explanation="The effective UID is the active user credential consulted for many authorization checks."}
::option[The saved user ID only.]{#process-permissions-effective-saved-only explanation="The saved ID supports credential transitions but is not generally the active identity for access checks."}
::option[The UID stored on the current directory.]{#process-permissions-effective-directory explanation="Filesystem ownership is object metadata, not the process's active user credential."}
:::

## Saved Set-User-ID

The saved set-user-ID lets a program retain an identity it may later restore, subject to the system-call rules. A privileged program can temporarily switch its effective UID to a less privileged value, perform ordinary work with reduced authority, and restore the saved identity only for a narrowly scoped operation.

This is safer than retaining elevated authority throughout the entire program, but only when implemented correctly. Programs should permanently discard privilege when it is no longer needed and check every credential-changing call for failure.

:::single-choice{#process-permissions-saved-uid}
Why can a privileged program retain a saved set-user-ID?

::option[To switch its effective identity for controlled privileged and unprivileged phases.]{#process-permissions-saved-switch .correct explanation="The saved identity can support temporary privilege reduction and a permitted later restoration."}
::option[To assign that UID automatically to every file it reads.]{#process-permissions-saved-file-owner explanation="Reading a file does not change its ownership to the process's saved UID."}
::option[To replace the system account database for the process.]{#process-permissions-saved-database explanation="Process credentials do not substitute for account records or name-service data."}
:::

## User IDs Are Only Part of the Credential Set

Processes also have real, effective, saved, and supplementary group credentials. Filesystem IDs, capabilities, namespaces, security modules, ACLs, mount options, and service policies can further affect authorization. Therefore, “the UID allows it” is often only part of a complete explanation.

Use tools such as `ps` and `/proc/PROCESS/status` to inspect credentials on Linux. Field availability and display formats vary, so consult the local documentation and avoid changing credentials merely to experiment on a shared system.

:::single-choice{#process-permissions-ordinary-identities}
For most ordinary commands without a privilege transition, how do the real and effective UIDs compare?

::option[The effective UID is always zero.]{#process-permissions-effective-root explanation="Ordinary commands do not automatically receive root's UID."}
::option[The real UID always equals the executable file owner.]{#process-permissions-real-file-owner explanation="The executable owner affects setuid behavior, not the ordinary real UID."}
::option[They normally match the invoking user's UID.]{#process-permissions-uids-match .correct explanation="Without setuid or an explicit credential change, ordinary processes usually run with matching real and effective identities."}
:::

## Summary

You can now explain why a Linux process can carry several user identities.

1. Use the real UID to identify the original caller.
2. Relate the effective UID to active authorization checks.
3. Use the saved identity to understand controlled privilege transitions.
4. Consider group IDs and additional security mechanisms as part of the full decision.
