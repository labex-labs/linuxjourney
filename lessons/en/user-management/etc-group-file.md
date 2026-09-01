---
lesson_id: "etc-group-file"
course_id: "user-management"
lang: "en"
order_index: 5
title: "/etc/group"
description: "Learn how local group records map names to GIDs and list supplementary members."
meta_title: "/etc/group - User Management"
meta_description: "Explore the /etc/group file in Linux to understand group management. Learn how to view group data with cat /etc/group, and understand the structure including GID and user lists. This guide covers the essentials of the etc group linux file."
meta_keywords: "/etc/group, /etc/group linux, /etc/group file in linux, cat /etc/group, etc group linux, group management, GID, Linux permissions, Linux groups"
---

`/etc/group` stores local group records. It maps group names to numeric GIDs and lists explicit members, supporting access control shared by several accounts.

## Local Groups versus Resolved Groups

The file is only one possible group source. NSS can resolve groups from local files, directory services, or other configured databases. Display the local records with:

```bash
$ cat /etc/group
```

Query the resolved group database with `getent`:

```bash
$ getent group
$ getent group developers
```

Group lists can disclose internal account and role names, so review output before sharing it.

:::single-choice{#group-query-resolved-database} Which command queries the NSS-resolved group database?

::option[`getent group`]{#group-getent-all .correct explanation="`getent` consults the configured NSS sources for group records."}
::option[`cat /etc/group`]{#group-cat-local explanation="This reads only the local group file and can omit groups supplied by other sources."}
::option[`groups /etc/group`]{#group-groups-file explanation="`groups` expects user names and reports memberships; it does not treat the local database pathname as an NSS query."}
:::

## Reading the Four Fields

A local record has four colon-separated fields:

```text
developers:x:1500:alice,bob
```

1. **Group name**: `developers`.
2. **Password field**: Commonly `x`, `*`, or another placeholder; protected group-password data can be stored in `/etc/gshadow`.
3. **GID**: The numeric group identity, `1500` here.
4. **Member list**: Comma-separated explicit member names, `alice` and `bob` here.

Group passwords are a legacy feature used by tools such as `newgrp` in some configurations. They are not the normal mechanism for granting sudo authorization and should not be introduced through manual field edits.

:::single-choice{#group-gid-field} In `developers:x:1500:alice,bob`, which field contains the GID?

::option[The second field, `x`]{#group-second-password explanation="Field 2 is the group-password placeholder rather than the numeric identity."}
::option[The fourth field, `alice,bob`]{#group-fourth-members explanation="Field 4 lists explicit member names rather than the GID."}
::option[The third field, `1500`]{#group-third-gid .correct explanation="The third colon-separated field is the numeric group ID."}
:::

:::single-choice{#group-explicit-member-field} How are explicit member names represented in a local group record?

::option[As a comma-separated list in field 4.]{#group-members-field-four .correct explanation="The final field contains explicit supplementary member names separated by commas."}
::option[As a space-separated list in field 2.]{#group-members-field-two explanation="Field 2 is reserved for password-related data or a placeholder, not the member list."}
::option[As numeric UIDs embedded in the group name.]{#group-members-in-name explanation="The group name and member names are separate fields; ordinary member entries are login names, not embedded UID digits."}
:::

## Accounting for Primary Group Membership

The member list in `/etc/group` does not normally repeat users whose passwd record names that GID as their primary group. A user can therefore be a member even when their name is absent from field 4.

For example, if Alice's passwd record has primary GID 1500, she belongs to `developers` even if the local group record ends with an empty member field:

```text
developers:x:1500:
```

This is why parsing field 4 alone produces an incomplete membership view.

:::single-choice{#group-primary-membership-visibility} Alice's passwd record uses GID 1500 as its primary GID, but her name is absent from group 1500's field 4. Is she a member of that group?

::option[No, every membership must appear in `/etc/group` field 4.]{#group-field-four-only explanation="This ignores primary GID membership and would undercount group members."}
::option[Yes, primary membership comes from the passwd record's GID field.]{#group-primary-from-passwd .correct explanation="The group file's explicit list is mainly for supplementary memberships; primary membership is recorded with the account."}
::option[Only if the group password field contains her username.]{#group-password-member explanation="The password field is unrelated to declaring primary membership."}
:::

## Inspecting a User's Groups

Use `id USER` or `groups USER` for a resolved account view:

```bash
$ id alice
$ groups alice
```

For the current process, plain `id` reports the groups actually present in its credentials. A newly configured supplementary membership usually does not appear in an already running login session; start a new authenticated session or use a deliberately configured mechanism such as `newgrp` when appropriate.

:::single-choice{#group-current-process-credentials} Which command reports the UID, primary GID, and supplementary groups of the current process?

::option[`id`]{#group-current-id .correct explanation="With no user operand, `id` reports identity credentials for the current process."}
::option[`cat /etc/group`]{#group-current-cat explanation="The local file lists records but does not show which resolved groups are active in the current process."}
::option[`getent passwd`]{#group-current-passwd explanation="This queries account records and does not specifically report the current process's supplementary group list."}
:::

## Changing Local Groups Safely

Use tools such as `groupadd`, `groupmod`, `groupdel`, `gpasswd`, and `usermod` rather than editing records with a general-purpose editor. Be especially careful with:

- `usermod -aG GROUP USER`, which appends supplementary membership.
- `usermod -G ...`, which replaces the supplementary group list when `-a` is omitted.

If manual local database repair is unavoidable, use `vigr` for locking and `grpck` for validation. Keep a recovery path before remote identity changes.

To practice local group management in a controlled environment, try these hands-on labs:

1. **[Manage Linux User Accounts with useradd, usermod, and userdel](https://labex.io/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Practice the complete lifecycle of user administration, from creating and securing new accounts to modifying and deleting them.
2. **[Manage Linux Groups with groupadd, usermod, and groupdel](https://labex.io/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Gain hands-on experience with core command-line utilities for group administration, including `groupadd`, `usermod`, and `groupdel`.
3. **[Add New User and Group](https://labex.io/labs/linux-add-new-user-and-group-17987)** - Simulate adding new team members to a server environment by creating new user accounts, setting up custom groups, and managing group memberships.

## Summary

You can now interpret local group records and resolve complete membership more accurately.

1. Query configured group sources with `getent group`.
2. Read the four colon-separated group fields.
3. Locate the numeric GID and explicit member list.
4. Include primary membership from passwd records.
5. Inspect active credentials before relying on a changed membership.
