---
lesson_id: "modifying-permissions"
course_id: "permissions"
lang: "en"
order_index: 2
title: "Modifying Permissions"
description: "Learn how to change Linux permission bits with symbolic and octal `chmod` modes."
meta_title: "Modifying Permissions - Permissions"
meta_description: "Learn how to change permissions in Linux using the chmod command. This guide covers both symbolic and numerical methods to help you manage file and directory access securely. Master the linux change permission process for better system administration."
meta_keywords: "linux change permission, change permission linux, how to change permissions in linux, how to change file permissions linux, chmod, file permissions, linux security, symbolic permissions, numerical permissions"
---

The `chmod` command changes the mode bits of files and directories. Normally, only the file owner or a process with the necessary privilege can make this change. Inspect the current mode with `ls -l` before and after running `chmod`.

## Using Symbolic Mode

A symbolic mode states which permission class to change, how to change it, and which permissions are involved.

- `u` selects the owner class.
- `g` selects the group class.
- `o` selects the other class.
- `a` selects all three classes.
- `+` adds permissions, `-` removes them, and `=` sets the selected class exactly.

For example, add execute permission for the owner:

```bash
$ chmod u+x myfile
```

Remove write permission from the group:

```bash
$ chmod g-w myfile
```

Add write permission for both the owner and group:

```bash
$ chmod ug+w myfile
```

Multiple clauses can be separated with commas. This command sets the owner to read and write, the group to read only, and other to no permissions:

```bash
$ chmod u=rw,g=r,o= myfile
```

If the class is omitted, as in `chmod +x myfile`, the process umask affects which classes are changed. Naming the class explicitly makes the intended result easier to review.

:::single-choice{#modifying-permissions-remove-group-write}
Which symbolic mode removes group write permission without changing the other group bits?

::option[`chmod u-w myfile`]{#modifying-permissions-user-minus-write explanation="This removes write permission from the owner class rather than the group class."}
::option[`chmod g-w myfile`]{#modifying-permissions-group-minus-write .correct explanation="The `g` selects the group class, `-` removes a bit, and `w` identifies write permission."}
::option[`chmod g=w myfile`]{#modifying-permissions-group-equals-write explanation="The `=` operator replaces the selected class with write-only permission instead of removing write."}
:::

## Using Octal Mode

An octal mode sets each basic permission triplet with a digit. Add these values within each class:

- `4` for read
- `2` for write
- `1` for execute
- `0` for no permissions

The three rightmost digits represent owner, group, and other in that order. For example:

```bash
$ chmod 755 myfile
```

The mode `755` expands as follows:

- Owner `7` is `4 + 2 + 1`, or `rwx`.
- Group `5` is `4 + 1`, or `r-x`.
- Other `5` is `4 + 1`, or `r-x`.

Unlike `+` or `-` symbolic operations, an octal mode supplies the complete ordinary permission set. A later lesson covers the optional leading digit used for special mode bits.

:::single-choice{#modifying-permissions-octal-read-value}
Which octal value represents read permission?

::option[`1`]{#modifying-permissions-value-one explanation="The value `1` represents execute permission."}
::option[`2`]{#modifying-permissions-value-two explanation="The value `2` represents write permission."}
::option[`4`]{#modifying-permissions-value-four .correct explanation="Read permission contributes the octal value `4` to a class digit."}
:::

:::single-choice{#modifying-permissions-mode-640}
What ordinary permissions does `chmod 640 report` set?

::option[Owner read, group write, other execute.]{#modifying-permissions-640-separated explanation="Octal digits are sums for each class, not separate read, write, and execute columns."}
::option[Owner read/execute, group write, other none.]{#modifying-permissions-640-wrong-sums explanation="Owner value `6` is read plus write, while group value `4` is read."}
::option[Owner read/write, group read, other none.]{#modifying-permissions-640-correct .correct explanation="The digits expand to owner `6` (`rw-`), group `4` (`r--`), and other `0` (`---`)."}
:::

## Applying Changes Safely

Grant only the access that users and services require. Avoid using `chmod 777` as a troubleshooting shortcut because it grants read, write, and execute to every class, often creating more risk without addressing ownership, directory traversal, ACLs, or service policy.

Recursive changes deserve extra care. Preview the target tree, account for symbolic links and mounted filesystems, and test on a small scope before using `chmod -R`. After a change, verify the resulting mode rather than assuming the command affected the intended objects.

:::single-choice{#modifying-permissions-least-privilege}
Why is `chmod 777` usually a poor general fix for an access problem?

::option[It removes all permissions from the owner.]{#modifying-permissions-777-removes explanation="Each `7` grants read, write, and execute; it does not remove the owner's permissions."}
::option[It grants every basic permission to owner, group, and other.]{#modifying-permissions-777-grants-all .correct explanation="All three classes receive `rwx`, which commonly exceeds the access actually required."}
::option[It changes only the file's group ownership.]{#modifying-permissions-777-group explanation="`chmod` changes mode bits; group ownership is changed with a tool such as `chgrp` or `chown`."}
:::

For hands-on practice in an isolated environment, use the [Linux User Group and File Permissions](https://labex.io/labs/linux-linux-user-group-and-file-permissions-18002) lab and inspect each mode before and after changing it.

## Summary

You can now change ordinary Linux mode bits with deliberate `chmod` expressions.

1. Use symbolic mode for targeted additions, removals, or assignments.
2. Build octal digits from read `4`, write `2`, and execute `1`.
3. Read octal classes in owner, group, and other order.
4. Verify changes and apply the least privilege needed.
