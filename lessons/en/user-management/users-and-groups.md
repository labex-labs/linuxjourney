---
lesson_id: "users-and-groups"
course_id: "user-management"
lang: "en"
order_index: 1
title: "Users and Groups"
description: "Learn how Linux identifies users and groups and how process credentials affect access decisions."
meta_title: "Users and Groups - User Management"
meta_description: "A key part of the basics of linux is understanding user and group management. This guide covers linux users and groups, the root superuser, and using the sudo command for elevated privileges. One of the best linux tutorial lessons for beginners."
meta_keywords: "linux users and groups, basics of linux, sudo, root user, UID, GID, user management, best linux tutorial, quickest way to linux advanced"
---

Linux uses user and group identities to label processes, own filesystem objects, and make access-control decisions. Human-readable names help administrators, while the kernel primarily works with numeric identifiers and process credentials.

## Identifying Users with UIDs

Each account has a numeric user ID, or **UID**. Usernames map to UIDs through the system's account databases. Files store numeric ownership, which tools normally display as a corresponding name.

Run `id` to inspect the current process identity information:

```bash
$ id
uid=1000(alice) gid=1000(alice) groups=1000(alice),27(sudo)
```

Values differ by system. Human login accounts commonly have home directories such as `/home/alice`, but accounts can use another path or no ordinary home at all. Service accounts often exist to run software with limited identity rather than to support interactive login.

:::single-choice{#users-uid-purpose}
Which identifier does the kernel primarily use to represent a user identity?

::option[A home-directory pathname]{#users-home-path explanation="A home path is account configuration and can vary or be absent; it is not the kernel's user identifier."}
::option[A numeric UID]{#users-numeric-uid .correct explanation="Account databases map names to numeric UIDs, which are used in process credentials and ownership records."}
::option[A terminal window number]{#users-terminal-number explanation="Terminal devices and sessions are separate from numeric user identities."}
:::

## Organizing Access with Groups

A group has a numeric group ID, or **GID**. An account normally has one primary group and can belong to supplementary groups. Group membership lets administrators grant access to a set of users without assigning permissions one account at a time.

Inspect memberships with:

```bash
$ id alice
$ groups alice
```

These commands report configured or resolved identity information. Directory services and caches can participate, so directly reading `/etc/group` does not always show the complete effective membership picture.

:::single-choice{#users-primary-supplementary-groups}
How can one Linux account normally participate in groups?

::option[It can belong to exactly one group for its entire lifetime.]{#users-single-group explanation="Linux processes can carry a primary group plus a list of supplementary groups."}
::option[It belongs to every group whose files it can read.]{#users-readable-groups explanation="File readability follows permissions and credentials; it does not automatically create group membership."}
::option[It has one primary group and may have supplementary groups.]{#users-group-memberships .correct explanation="The primary GID is part of the account record, while supplementary memberships provide additional group identities."}
:::

## Understanding Process Credentials

A process has credentials such as real and effective UIDs and GIDs plus supplementary groups. The effective credentials are central to many permission checks. A process started by a user usually inherits credentials from its parent, but controlled mechanisms can change them.

This is more precise than saying a process always runs only “as the user who started it.” Set-user-ID executables, service managers, containers, namespaces, and privilege-changing system calls can affect the identities visible or effective in a particular context.

:::single-choice{#users-process-access-identity}
Which information is commonly considered when the kernel checks a process against file permissions?

::option[The process's effective UID, effective GID, and supplementary groups.]{#users-effective-credentials .correct explanation="These credentials are compared with ownership and permission data during ordinary discretionary access checks."}
::option[The color theme of the terminal that launched the process.]{#users-terminal-theme explanation="Display preferences have no role in filesystem permission checks."}
::option[The spelling length of the account's username.]{#users-username-length explanation="The kernel works with numeric credentials; username length does not grant access."}
:::

## Recognizing the Root Identity

The account traditionally named `root` has UID 0. UID 0 is treated specially by many Linux permission mechanisms and carries broad administrative power. Modern Linux can also divide privileges through capabilities, namespaces, mandatory access controls, and service confinement, so “unlimited power in every context” is an oversimplification.

Routine work should use an unprivileged account. Administrative authority increases the impact of path mistakes, untrusted commands, and compromised software.

:::single-choice{#users-root-uid}
What numeric UID traditionally identifies the root account?

::option[`0`]{#users-uid-zero .correct explanation="Linux and Unix-like systems traditionally reserve UID 0 for the superuser identity."}
::option[`1000`]{#users-uid-thousand explanation="Many distributions assign a value near 1000 to the first regular human account, but this is not the root UID."}
::option[`1`]{#users-uid-one explanation="UID 1 can belong to a system account and is not the traditional superuser identity."}
:::

## Using sudo under a Policy

`sudo` asks its configured policy whether the invoking user may run a command as a target user. The default target is often root, but a policy or `-u USER` can select another account. Authentication prompts and logging also depend on configuration.

List the commands the current account is allowed to run:

```bash
$ sudo -l
```

Only use an allowed administrative command when the task requires it and you understand its effects. Do not use `sudo` merely to silence a permission error, and do not display password-hash databases such as `/etc/shadow` as a casual exercise.

:::single-choice{#users-sudo-policy}
What does `sudo` do before running a requested command?

::option[Consults configured policy for permission to use the requested target identity.]{#users-sudo-policy-check .correct explanation="`sudo` authorizes according to policy and then establishes the configured target credentials when permitted."}
::option[Always grants every local user unrestricted root access.]{#users-sudo-always-root explanation="Authorization is policy-controlled, and denied users or commands do not receive blanket root access."}
::option[Changes the invoking account's permanent UID to 0.]{#users-sudo-permanent-uid explanation="`sudo` runs a command with target credentials; it does not permanently rewrite the caller's account identity."}
:::

To practice account and group administration in a controlled environment, try these hands-on labs:

1. **[Manage Linux User Accounts with useradd, usermod, and userdel](https://labex.io/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Practice the complete lifecycle of user administration, from creating and securing new accounts to modifying and deleting them.
2. **[Manage Linux Groups with groupadd, usermod, and groupdel](https://labex.io/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Gain hands-on experience with core command-line utilities for group administration, including creating new groups, modifying user memberships, and removing groups.
3. **[Configure User Accounts and Sudo Privileges in Linux](https://labex.io/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Learn essential techniques for managing user accounts and `sudo` privileges to enhance the security of a Linux system, including granting administrative permissions.

## Summary

You can now describe how Linux represents identities and delegates administrative commands.

1. Identify accounts by UID and groups by GID.
2. Distinguish primary and supplementary group membership.
3. Relate process credentials to access checks.
4. Recognize UID 0 as the traditional root identity.
5. Treat `sudo` as a policy-controlled delegation tool.
