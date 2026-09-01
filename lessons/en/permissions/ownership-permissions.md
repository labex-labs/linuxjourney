---
lesson_id: "ownership-permissions"
course_id: "permissions"
lang: "en"
order_index: 3
title: "Ownership Permissions"
description: "Learn how to inspect and change the user and group ownership of Linux filesystem objects."
meta_title: "Ownership Permissions - Permissions"
meta_description: "Master Linux file ownership by learning how to use the chown and chgrp Linux commands. This Linux tutorial explains how to change user and group ownership for files, a key skill for managing Linux permissions."
meta_keywords: "chown, chgrp, linux file ownership, change file owner, change file group, linux permissions, linux commands, linux tutorial, linux guide, user ownership, group ownership"
---

Every Linux filesystem object records a user owner and a group owner. These identities determine which owner or group permission triplet applies, but they do not themselves grant a particular permission. Inspect both ownership and mode with `ls -l`.

## Changing the User Owner

Use `chown`, short for change owner, to assign a different user owner:

```bash
$ sudo chown patty myfile
```

This changes the user owner of `myfile` to `patty` and leaves its group unchanged. Changing a file's user owner normally requires appropriate privilege, even if you currently own the file. This restriction prevents users from transferring files to evade quotas or other ownership-based controls.

:::single-choice{#ownership-permissions-change-user} Which command changes the user owner of `myfile` to `patty` while leaving its group unchanged?

::option[`chown patty myfile`]{#ownership-permissions-user-with-chown .correct explanation="A username alone as the `chown` ownership operand changes the user owner and preserves the group."}
::option[`chgrp patty myfile`]{#ownership-permissions-user-with-chgrp explanation="`chgrp` changes the group owner rather than the user owner."}
::option[`chmod patty myfile`]{#ownership-permissions-user-with-chmod explanation="`chmod` changes mode bits and does not accept a username as the new owner."}
:::

## Changing the Group Owner

Use `chgrp` to assign a different group owner:

```bash
$ chgrp whales myfile
```

On typical systems, an unprivileged owner can change a file's group only to a group of which that user is a member. Privileged processes can make broader changes. The equivalent `chown` form begins with a colon:

```bash
$ chown :whales myfile
```

Afterward, the group's mode bits apply when the kernel selects the group class; changing the group does not automatically add read, write, or execute bits.

:::single-choice{#ownership-permissions-change-group} What does `chgrp whales myfile` change?

::option[The user owner recorded for `myfile`.]{#ownership-permissions-group-not-user explanation="The user owner is changed with `chown`, not `chgrp`."}
::option[The members listed in the `whales` group.]{#ownership-permissions-group-members explanation="The command changes file metadata; it does not edit the system's group membership database."}
::option[The group owner recorded for `myfile`.]{#ownership-permissions-group-owner .correct explanation="`chgrp` assigns the named group as the filesystem object's group owner."}
:::

## Changing User and Group Together

Supply `USER:GROUP` to `chown` to update both fields in one operation:

```bash
$ sudo chown patty:whales myfile
```

The command assigns `patty` as the user owner and `whales` as the group owner. Verify the result rather than assuming it succeeded:

```bash
$ ls -l myfile
```

:::single-choice{#ownership-permissions-change-both} Which ownership specification assigns user `patty` and group `whales` in one `chown` command?

::option[`patty:whales`]{#ownership-permissions-both-colon .correct explanation="A colon separates the user and group names in the combined ownership specification."}
::option[`patty/whales`]{#ownership-permissions-both-slash explanation="A slash is not the introduced separator for a `chown` user and group operand."}
::option[`patty+whales`]{#ownership-permissions-both-plus explanation="A plus sign is not used to combine the two ownership fields for `chown`."}
:::

## Handling Recursive Changes Carefully

The `-R` option changes ownership recursively, but a broad recursive command can cross unexpected directory trees or affect service data. Confirm the exact target, understand symbolic-link behavior for your implementation, preview the tree, and verify a small sample before changing a large hierarchy. Avoid copying privileged ownership commands from examples onto real systems without reviewing their scope.

:::single-choice{#ownership-permissions-mode-separate} After changing a file's group owner, what happens to its ordinary group permission bits?

::option[They always become read and write automatically.]{#ownership-permissions-mode-read-write explanation="`chgrp` does not automatically select a fixed group mode."}
::option[They are copied from the owner's permission triplet.]{#ownership-permissions-mode-copied explanation="The owner and group triplets remain independent when ownership changes."}
::option[They remain as set unless a separate operation changes them.]{#ownership-permissions-mode-unchanged .correct explanation="Ownership fields and mode bits are separate metadata; changing the group does not inherently grant new group bits."}
:::

For practice in an isolated environment, the [Linux User Group and File Permissions](https://labex.io/labs/linux-linux-user-group-and-file-permissions-18002) lab covers inspecting and modifying ownership alongside file modes.

## Summary

You can now distinguish ownership metadata from permission bits and change it deliberately.

1. Use `chown USER FILE` to change the user owner.
2. Use `chgrp GROUP FILE` or `chown :GROUP FILE` to change the group owner.
3. Use `chown USER:GROUP FILE` to set both fields.
4. Verify results and scope recursive changes carefully.
