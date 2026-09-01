---
lesson_id: "user-management-tools"
course_id: "user-management"
lang: "en"
order_index: 6
title: "User Management Tools"
description: "Learn how to create, modify, secure, verify, and remove local accounts with explicit options."
meta_title: "User Management Tools - User Management"
meta_description: "Master Linux user management with essential command-line tools. This guide covers using useradd, userdel, and passwd for managing accounts in Linux, perfect for beginners."
meta_keywords: "linux user management, the command-line tool for managing accounts in linux, useradd, userdel, passwd, linux accounts, manage users linux"
---

Linux distributions commonly provide account tools from the shadow utilities suite, but defaults and higher-level wrappers vary. Before changing a local account, confirm that it is not centrally managed, review the command's local manual, and maintain a recovery path.

The commands in this lesson change authentication and ownership state. Practice only in an authorized disposable environment, not on a production host.

## Reviewing Account-Creation Defaults

`useradd` creates a local account using command options plus site defaults. Inspect compiled and configured defaults with:

```bash
$ useradd -D
```

Files such as `/etc/default/useradd`, `/etc/login.defs`, and skeleton content can influence behavior, but their roles vary by distribution. A higher-level `adduser` command may exist, but its interface is not standardized across all Linux systems.

## Creating a Local Account Explicitly

In a controlled environment, specify important properties rather than relying on unknown defaults:

```bash
$ sudo useradd -m -s /bin/bash -c "Bob Example" bob
```

- `-m` requests creation of the home directory.
- `-s /bin/bash` chooses the login shell after confirming that path is permitted and installed.
- `-c` supplies the GECOS/comment field.

The new account usually cannot authenticate with a usable local password until one is set, but exact initial password and lock state depend on local tooling and policy. Verify the records instead of assuming:

```bash
$ getent passwd bob
$ sudo passwd -S bob
$ id bob
```

:::single-choice{#user-tools-create-home} Which `useradd` option explicitly requests creation of the new account's home directory?

::option[`-M`]{#user-tools-no-home-option explanation="Uppercase `-M` explicitly tells common `useradd` implementations not to create the home directory."}
::option[`-s`]{#user-tools-shell-option explanation="The `-s` option chooses a login shell and does not itself create a home directory."}
::option[`-m`]{#user-tools-home-option .correct explanation="The lowercase `-m` option requests that `useradd` create and populate the home directory according to local defaults."}
:::

## Setting or Changing a Password

A regular user changes their own local password interactively with:

```bash
$ passwd
```

An authorized administrator can set another local account's password with:

```bash
$ sudo passwd bob
```

Enter passwords only at the protected prompt, not in command arguments, shell history, lesson notes, or chat. PAM policy can reject weak or reused passwords. Directory-managed accounts can require a different tool.

:::single-choice{#user-tools-change-own-password} Which command normally lets the current user change their own password through an interactive prompt?

::option[`useradd`]{#user-tools-add-not-password explanation="`useradd` creates an account record and is not the ordinary interactive password-change command."}
::option[`userdel`]{#user-tools-delete-not-password explanation="`userdel` removes a local account and is unrelated to changing the caller's password."}
::option[`passwd`]{#user-tools-passwd-self .correct explanation="With no username operand, `passwd` operates on the invoking user's local password under PAM policy."}
:::

## Modifying Account Properties and Groups

`usermod` changes local account fields. Examples include:

```bash
$ sudo usermod -s /bin/zsh bob
$ sudo usermod -d /srv/home/bob -m bob
$ sudo usermod -aG developers bob
```

For the home move, verify the destination, ownership, available space, running processes, mounts, and services first. For supplementary groups, `-aG` means append to the current list. Using `-G` without `-a` replaces the entire supplementary group list and can remove access unexpectedly.

Group changes normally affect new login sessions rather than processes already running under the old credential set.

:::single-choice{#user-tools-append-group} Which command adds `bob` to supplementary group `developers` without replacing his other supplementary memberships?

::option[`usermod -G developers bob`]{#user-tools-replace-groups explanation="Without `-a`, `-G` replaces the supplementary group list and can remove existing memberships."}
::option[`usermod -aG developers bob`]{#user-tools-append-groups .correct explanation="The `-a` option appends the group named by `-G`, preserving other supplementary memberships."}
::option[`groupdel developers bob`]{#user-tools-delete-group explanation="`groupdel` removes a group definition and does not append a user membership."}
:::

## Locking a Local Password

An administrator can lock the local password hash with `passwd -l USER` and inspect status with `passwd -S USER`. Unlocking is performed with `passwd -u USER` only after reviewing why the lock exists and whether a valid hash remains.

A password lock does not necessarily stop SSH keys, tokens, scheduled jobs, already running processes, or service-specific authentication. To disable an account comprehensively, define the threat and access paths, then apply a coordinated policy that can include account expiration, login shell, service access, keys, and session termination.

:::single-choice{#user-tools-password-lock-scope} What does `passwd -l bob` primarily lock?

::option[Every possible authentication and execution path for the account.]{#user-tools-lock-everything explanation="Keys, tokens, jobs, services, and existing sessions can require separate controls."}
::option[All files currently owned by Bob's UID.]{#user-tools-lock-files explanation="Password state does not change filesystem ownership or automatically make owned data inaccessible."}
::option[The local Unix password hash used by password authentication.]{#user-tools-lock-local-password .correct explanation="The command prefixes or otherwise disables the local password hash, preventing normal verification through that path."}
:::

## Removing a Local Account Deliberately

Plain `userdel bob` removes the local account records but normally leaves the home directory. `userdel -r bob` also attempts to remove the home directory and mail spool, making it a destructive operation.

Before any removal:

1. Confirm the exact account with `getent passwd bob` and `id bob`.
2. Identify running processes, scheduled tasks, services, keys, and delegated access.
3. Inventory files owned by the UID across the intended filesystems.
4. Decide whether data must be transferred, archived, retained, or securely deleted.
5. Confirm that the UID will not be reassigned while orphaned files remain.

`userdel -r` does not guarantee removal of files outside the configured home and mail locations. Account deletion can also leave numeric ownership on files, database permissions, application identities, and remote directory records.

:::single-choice{#user-tools-userdel-r-scope} What extra removal does common `userdel -r bob` request compared with plain `userdel bob`?

::option[Every file with Bob's UID on every mounted filesystem.]{#user-tools-delete-all-owned explanation="The tool does not universally discover and erase all UID-owned files across all storage."}
::option[Every remote account whose username is also `bob`.]{#user-tools-delete-remote explanation="`userdel` operates on the applicable local account databases and does not delete unrelated directory-service identities."}
::option[Bob's home directory and local mail spool, in addition to account records.]{#user-tools-delete-home-mail .correct explanation="The recursive account-removal option targets the configured home and mail spool, but not every object Bob may own elsewhere."}
:::

To practice the account lifecycle in an isolated environment, try these hands-on labs:

1. **[Manage Linux User Accounts with useradd, usermod, and userdel](https://labex.io/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Practice the complete lifecycle of user administration, from creating and securing new accounts to modifying and deleting them.
2. **[Manage Linux Groups with groupadd, usermod, and groupdel](https://labex.io/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Gain hands-on experience with core command-line utilities for group administration, including adding, modifying, and deleting groups.
3. **[Configure User Accounts and Sudo Privileges in Linux](https://labex.io/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Learn essential techniques for managing user accounts and sudo privileges to enhance the security of a Linux system.

## Summary

You can now manage local accounts with explicit scope and verification.

1. Review `useradd` defaults before creation.
2. Request home, shell, and metadata settings explicitly.
3. Change passwords only through protected prompts.
4. Append supplementary groups without replacing the existing list.
5. Inventory identity dependencies before destructive removal.
