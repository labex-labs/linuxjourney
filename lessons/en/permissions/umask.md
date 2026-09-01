---
lesson_id: "umask"
course_id: "permissions"
lang: "en"
order_index: 4
title: "Umask"
description: "Learn how a process umask limits the permission bits requested for newly created files and directories."
meta_title: "Umask - Permissions"
meta_description: "Learn how to use the `umask` command to control default file permissions in Linux. Understand numerical permissions and manage new file access easily."
meta_keywords: "umask, linux permissions, file permissions, linux commands, beginner linux, linux tutorial, default permissions"
---

A process's file-creation mask, or umask, prevents selected permission bits from being set when that process creates a filesystem object. It is a mask, not a complete default mode: the application first requests a mode, and the kernel removes bits prohibited by the umask.

Conceptually:

```text
resulting mode = requested mode AND NOT umask
```

Access control lists and application behavior can add further details, so inspect the result when exact permissions matter.

## Viewing and Setting the Umask

Run `umask` without an operand to display the current shell's mask, often in octal form:

```bash
$ umask
0022
```

Set it for the current shell and the processes subsequently started by that shell:

```bash
$ umask 027
```

Each octal position corresponds to owner, group, and other. A mask bit removes the corresponding requested permission: `2` masks write, `4` masks read, and `1` masks execute.

:::single-choice{#umask-command-purpose} What does `umask 027` change in the current shell?

::option[The permissions of every file that already exists.]{#umask-existing-files explanation="A umask affects creation requests; it does not retroactively run `chmod` on existing objects."}
::option[The mask inherited by commands subsequently started from that shell.]{#umask-current-shell-mask .correct explanation="The shell sets its process umask, and child processes normally inherit that value."}
::option[The owner and group names stored on new files.]{#umask-owner-group explanation="The mask filters permission bits and does not select ownership identities."}
:::

## Calculating New File and Directory Modes

Many ordinary programs request `0666` for new regular files, because creating executable files by default would be unsafe. They commonly request `0777` for new directories, where execute permission is required for traversal.

With umask `0022`:

```text
regular file: 0666 masked by 0022 -> 0644 (rw-r--r--)
directory:    0777 masked by 0022 -> 0755 (rwxr-xr-x)
```

The umask only removes requested bits. It cannot add execute permission when an application did not request it. An application can also request a more restrictive starting mode, producing a more restrictive result.

:::single-choice{#umask-file-mode-022} If a program requests mode `0666` for a regular file and the umask is `0022`, which mode results?

::option[`0666`]{#umask-file-0666 explanation="The group and other write bits requested by `0666` are removed by mask `0022`."}
::option[`0755`]{#umask-file-0755 explanation="Execute bits were not requested for the regular file, so the umask cannot add them."}
::option[`0644`]{#umask-file-0644 .correct explanation="Removing group and other write from `0666` leaves owner read/write and read-only access for group and other."}
:::

:::single-choice{#umask-directory-mode-027} If a program requests `0777` for a directory and the umask is `0027`, which mode results?

::option[`0777`]{#umask-directory-0777 explanation="The requested group-write and other permissions are filtered by the nonzero mask."}
::option[`0640`]{#umask-directory-0640 explanation="That result also removes execute bits that mask `0027` does not remove from owner or group."}
::option[`0750`]{#umask-directory-0750 .correct explanation="The mask removes group write and all permissions for other, leaving `rwxr-x---`."}
:::

## Scope and Persistence

Changing the umask in one shell does not alter its parent process or unrelated sessions. The value applies to future creations by that shell and its descendants; existing files retain their modes.

To make a preferred value persistent, configure it in the appropriate login, shell, PAM, service-manager, or application configuration for your environment. The correct location varies, and services may set their own umask. Avoid assuming that editing one interactive shell file governs every process on the system.

:::single-choice{#umask-existing-file-effect} What happens to an existing file when you set a new umask?

::option[Its current mode remains unchanged.]{#umask-existing-unchanged .correct explanation="A new umask filters later creation requests and does not modify modes already stored on filesystem objects."}
::option[Its mode is recalculated from `0666`.]{#umask-existing-recalculated explanation="Existing objects are not recreated or automatically passed through the new mask."}
::option[Its owner loses the masked permissions immediately.]{#umask-existing-owner-loss explanation="Changing a process umask is not an operation on existing file metadata."}
:::

For hands-on practice, create files and directories under different masks in an isolated environment, then compare their modes with `ls -ld`. The [Linux User Group and File Permissions](https://labex.io/labs/linux-linux-user-group-and-file-permissions-18002) lab offers a suitable permissions workspace.

## Summary

You can now predict how a umask limits newly requested permissions.

1. View or set the current shell's mask with `umask`.
2. Remove masked bits from the mode requested by an application.
3. Distinguish common file requests of `0666` from directory requests of `0777`.
4. Treat umask scope and persistence as process- and environment-specific.
