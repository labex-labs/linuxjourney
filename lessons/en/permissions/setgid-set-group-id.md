---
lesson_id: "setgid-set-group-id"
course_id: "permissions"
lang: "en"
order_index: 6
title: "Setgid"
description: "Learn how set-group-ID affects executable credentials and group inheritance in shared directories."
meta_title: "Setgid - Permissions"
meta_description: "Learn about Linux SGID (Set Group ID) permissions, how they work, and how to modify them. Understand this crucial Linux security concept."
meta_keywords: "Linux SGID, Set Group ID, Linux permissions, chmod g+s, Linux security, beginner Linux, Linux tutorial"
---

The set-group-ID bit, commonly called setgid or SGID, has two important uses. On an executable regular file, it can change the effective group ID of the new process. On a directory, it makes newly created entries inherit the directory's group, which is especially useful for collaborative trees.

## Setgid on Executable Files

A long listing can show setgid in the group execute position:

```bash
$ ls -l /path/to/program
-rwxr-sr-x 1 root operators 24576 Jan 10 09:30 /path/to/program
```

Lowercase `s` means that both setgid and group execute are set. Uppercase `S` means setgid is set but group execute is absent.

When the kernel honors this bit during execution, the process receives an effective group ID based on the executable's group owner. The behavior can be suppressed by controls such as a `nosuid` mount, and it must not be treated as a universal guarantee across every file type or environment.

:::single-choice{#setgid-executable-effect}
When setgid on an executable is honored, which credential comes from the executable's group owner?

::option[The process's effective group ID.]{#setgid-effective-group .correct explanation="Set-group-ID execution establishes the executable owner's group as the process's effective group identity."}
::option[The process's real user ID.]{#setgid-real-user explanation="The bit concerns the group credential, not the caller's real user identity."}
::option[The owner of every file the process opens.]{#setgid-opened-owner explanation="Execution credentials do not rewrite ownership metadata on opened files."}
:::

## Setgid on Directories

Setgid on a directory has a different purpose. New files and subdirectories normally inherit the directory's group instead of the creator's default group. New subdirectories also inherit the setgid bit on Linux, helping a shared project tree keep a consistent group.

Setgid does not itself grant group write access. The directory mode, process umask, requested creation mode, default ACLs, and other controls still determine access.

```bash
$ sudo chgrp developers /srv/project
$ sudo chmod g+s /srv/project
$ ls -ld /srv/project
drwxr-sr-x 2 root developers 4096 Jan 10 09:30 /srv/project
```

:::single-choice{#setgid-directory-inheritance}
What does setgid on `/srv/project` normally make a newly created file inherit?

::option[The directory's user owner.]{#setgid-inherit-user explanation="Directory setgid affects group inheritance, not the new entry's user owner."}
::option[The directory's complete permission mode.]{#setgid-inherit-mode explanation="Creation permissions are still calculated from the requested mode, umask, and any ACLs."}
::option[The directory's group owner.]{#setgid-inherit-group .correct explanation="A new entry normally receives the setgid directory's group, supporting consistent shared ownership."}
:::

## Setting and Removing Setgid

Set the bit symbolically with:

```bash
$ sudo chmod g+s myfile
```

Set it together with ordinary mode bits using a leading octal `2`:

```bash
$ sudo chmod 2755 myfile
```

Remove only the special bit with `chmod g-s myfile`.

:::single-choice{#setgid-octal-value}
Which value does setgid contribute to the leading special-bits octal digit?

::option[`4`]{#setgid-value-four explanation="The value `4` represents setuid in the special-bits digit."}
::option[`1`]{#setgid-value-one explanation="The value `1` represents the sticky bit."}
::option[`2`]{#setgid-value-two .correct explanation="Setgid contributes `2`, as in mode `2755`."}
:::

## Using Shared Directories Safely

For a collaborative directory, combine the intended group owner, setgid, and narrowly chosen access bits. Test creation as representative users and inspect results with `ls -ld`. Avoid making a tree world-writable merely to solve group-sharing problems; a dedicated group, appropriate umask or default ACL, and setgid directory usually provide clearer control.

:::single-choice{#setgid-directory-write-access}
Does setting setgid alone give group members permission to create files in a directory?

::option[Yes; setgid always adds group read, write, and execute.]{#setgid-adds-rwx explanation="The special bit does not automatically alter the three ordinary group permission bits."}
::option[Yes; setgid disables all checks for members of the group.]{#setgid-disables-checks explanation="Normal discretionary and additional security checks still apply."}
::option[No; the applicable write and search permissions must also allow creation.]{#setgid-no-automatic-write .correct explanation="Setgid controls group inheritance, while ordinary permissions and other access controls govern directory writes."}
:::

## Summary

You can now distinguish the executable and directory meanings of setgid.

1. Recognize setgid in the group execute position.
2. Relate executable setgid to the effective group ID.
3. Use directory setgid to preserve group ownership in shared trees.
4. Set or remove the bit without confusing it with ordinary write access.
