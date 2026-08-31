---
lesson_id: "sticky-bit"
course_id: "permissions"
lang: "en"
order_index: 8
title: "The Sticky Bit"
description: "Learn how the sticky bit protects entries in shared writable directories such as `/tmp`."
meta_title: "The Sticky Bit - Permissions"
meta_description: "Explore the purpose of the sticky bit in Linux and Unix file permissions. Learn how the sticky bit protects files in shared directories like /tmp and how to set it using chmod."
meta_keywords: "sticky bit, sticky bit linux, unix file permissions sticky bit, chmod +t, /tmp directory, file permissions, linux security"
---

A writable directory normally lets an authorized user remove or rename entries within it, even when that user does not own the files themselves. The sticky bit adds an ownership restriction that makes shared writable directories safer.

## How the Sticky Bit Restricts Removal

When a directory has the sticky bit set, Linux generally permits an entry to be removed or renamed only by a suitably privileged process, the directory owner, or the entry owner. Ordinary directory write and search permissions are still required.

The restriction concerns directory entries. It does not prevent a file owner from editing file contents when the file's permissions otherwise allow that operation, and it does not make the directory private.

:::single-choice{#sticky-bit-removal-rule}
In a sticky shared directory, which ordinary user can normally remove a particular entry?

::option[Any user who can list the directory.]{#sticky-bit-any-reader explanation="Directory read permission can expose names but does not bypass the sticky ownership restriction."}
::option[The entry's owner, with required directory access.]{#sticky-bit-entry-owner .correct explanation="The entry owner is one of the identities normally permitted by the sticky-directory rule."}
::option[Only a member of the entry's group.]{#sticky-bit-entry-group explanation="Group membership alone is not the ownership exception defined by the sticky bit."}
:::

## Recognizing the Bit on `/tmp`

The system temporary directory is a common example:

```bash
$ ls -ld /tmp
drwxrwxrwt 17 root root 4096 Dec 15 11:45 /tmp
```

The final lowercase `t` occupies the other execute position. It means that both the sticky bit and other execute permission are present. An uppercase `T` means the sticky bit is set while other execute permission is absent.

Because `/tmp` is commonly writable and searchable by everyone, multiple users can create entries there. The sticky bit prevents an ordinary user from removing another user's entries merely because the directory is world-writable. Applications must still create temporary objects securely because predictable names, unsafe links, and weak file modes create separate risks.

:::single-choice{#sticky-bit-lowercase-t}
What does lowercase `t` at the end of a directory mode indicate?

::option[Sticky is set and other execute is set.]{#sticky-bit-t-with-execute .correct explanation="Lowercase `t` combines the sticky special bit with the ordinary other execute bit."}
::option[Sticky is set but other execute is absent.]{#sticky-bit-t-without-execute explanation="That combination is displayed as uppercase `T`."}
::option[Setgid is set and group execute is set.]{#sticky-bit-setgid-position explanation="Setgid appears in the group execute position, not the final other position."}
:::

## Setting and Removing the Sticky Bit

Set the bit symbolically:

```bash
$ chmod +t shared-directory
```

In a leading special-bits octal digit, sticky contributes `1`:

```bash
$ chmod 1777 shared-directory
```

The leading `1` sets sticky, while `777` supplies the ordinary mode. This mode is appropriate only when the directory is intentionally shared by all local users. For a team directory, narrower group permissions may be preferable. Remove only the sticky bit with `chmod -t shared-directory`.

:::single-choice{#sticky-bit-octal-value}
Which leading octal value represents the sticky bit?

::option[`2`]{#sticky-bit-value-two explanation="A leading `2` represents setgid."}
::option[`1`]{#sticky-bit-value-one .correct explanation="The sticky bit contributes `1` to the leading special-bits digit."}
::option[`4`]{#sticky-bit-value-four explanation="A leading `4` represents setuid."}
:::

## Verifying the Complete Directory Policy

Sticky does not grant write or search access; it only restricts removal and rename after ordinary permissions permit directory modification. Verify the directory's owner, group, ordinary mode, ACLs, and mount context together. Test with nonprivileged accounts in an isolated environment rather than altering `/tmp` on a working system.

:::single-choice{#sticky-bit-access-scope}
Does adding the sticky bit make a nonwritable directory writable to other users?

::option[Yes; sticky automatically adds write for every class.]{#sticky-bit-adds-write explanation="The special bit does not rewrite the owner, group, or other write bits."}
::option[Yes; sticky disables the directory's other permission triplet.]{#sticky-bit-disables-other explanation="The other triplet continues to participate in normal access checks."}
::option[No; ordinary write and search permissions still control access.]{#sticky-bit-no-write-grant .correct explanation="Sticky narrows certain removal and rename operations but does not add missing ordinary permissions."}
:::

For practice, create a disposable shared directory, set an appropriate ordinary mode and sticky bit, then test entry removal as two nonprivileged users. The [Delete and Move Files](https://labex.io/labs/linux-delete-and-move-files-7777) lab can reinforce the underlying rename and deletion operations.

## Summary

You can now explain and verify the sticky bit on shared directories.

1. Relate sticky to ownership restrictions on removal and rename.
2. Recognize lowercase `t` and uppercase `T` in a long listing.
3. Set the bit symbolically or with leading octal value `1`.
4. Evaluate sticky together with ordinary directory permissions.
