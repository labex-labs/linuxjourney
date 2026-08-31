---
lesson_id: "etc-passwd-file"
course_id: "user-management"
lang: "en"
order_index: 3
title: "/etc/passwd"
description: "Learn how to read local passwd records and distinguish them from the complete NSS account view."
meta_title: "/etc/passwd - User Management"
meta_description: "A comprehensive guide to the /etc/passwd file in Linux. Learn to interpret user data fields, understand UIDs, and see examples like root:x:0:0:root:/root:/bin/bash."
meta_keywords: "/etc/passwd, /etc/passwd in linux, root:x:0:0:root:/root:/bin/bash, user ID, UID, user management, Linux tutorial"
---

`/etc/passwd` stores local account records in a colon-separated text format. It maps login names to numeric UIDs and records a primary GID, descriptive field, home path, and login program.

## Local Records versus Resolved Accounts

Display the local file with a read-only command:

```bash
$ cat /etc/passwd
```

This is not necessarily every account known to the system. The Name Service Switch (NSS) can resolve accounts from files, directory services, system databases, or other configured sources. Use `getent` to query the resolved passwd database:

```bash
$ getent passwd
$ getent passwd root
```

The first command can disclose account names and metadata, so review output before sharing it publicly.

:::single-choice{#passwd-query-resolved-database}
Which command queries the NSS-resolved passwd database rather than reading only the local file?

::option[`cat /etc/passwd`]{#passwd-cat-local explanation="This displays only the local file and does not include accounts supplied solely by other NSS sources."}
::option[`cat /etc/shadow`]{#passwd-cat-shadow explanation="The shadow file contains protected local password-aging data and should not be displayed for this purpose."}
::option[`getent passwd`]{#passwd-getent-all .correct explanation="`getent` consults the configured passwd database sources through NSS."}
:::

## Reading the Seven Fields

A local record commonly looks like this:

```text
root:x:0:0:root:/root:/bin/bash
```

The seven colon-separated fields are:

1. **Login name**: The human-readable account name, such as `root`.
2. **Password field**: Usually `x` on a shadow-password system, indicating protected password data is stored separately.
3. **UID**: The numeric user identity. UID 0 has traditional superuser treatment.
4. **Primary GID**: The numeric ID of the account's primary group.
5. **GECOS/comment**: Descriptive account information, often internally comma-separated.
6. **Home directory**: The path used as the account's home setting; it may be absent on disk.
7. **Login shell/program**: The program requested for applicable login sessions, such as `/bin/bash` or a non-login program.

The kernel does not require UID values to be unique across malformed or deliberately duplicated records, but accounts that share a UID are indistinguishable for many ownership and permission decisions. Administrators should normally keep account UIDs unique.

:::single-choice{#passwd-uid-field}
In `root:x:0:0:root:/root:/bin/bash`, which field contains the UID?

::option[The second field, `x`]{#passwd-second-password explanation="The second field is the password placeholder, not the numeric user identity."}
::option[The fourth field, the second `0`]{#passwd-fourth-gid explanation="Field 4 is the primary GID rather than the UID."}
::option[The third field, the first `0`]{#passwd-third-uid .correct explanation="Field 3 is the UID, so the first zero identifies this record as UID 0."}
:::

:::single-choice{#passwd-primary-gid-field}
Which field of a passwd record stores the account's primary GID?

::option[Field 5]{#passwd-gecos-five explanation="The fifth field is the GECOS or comment field."}
::option[Field 4]{#passwd-gid-four .correct explanation="The fourth colon-separated field identifies the primary group numerically."}
::option[Field 7]{#passwd-shell-seven explanation="The seventh field specifies the login shell or program."}
:::

## Interpreting the Password Placeholder

On typical shadow-password systems, `x` in field 2 directs password-aware tools to protected data in `/etc/shadow`. Values such as `*` or `!` are not valid password hashes and generally prevent authentication with a Unix password through that entry.

That does not prove the account cannot authenticate by every method. SSH keys, certificates, tokens, or service-specific mechanisms may be independent. Likewise, an empty password field has security-sensitive behavior that depends on the authentication stack; do not create or “fix” it manually.

:::single-choice{#passwd-x-placeholder}
What does `x` commonly mean in field 2 of a local `/etc/passwd` record?

::option[The account is guaranteed to have no authentication method.]{#passwd-no-auth-guarantee explanation="The placeholder does not describe every possible authentication method and does not itself mean the account is unusable."}
::option[The account's home directory has been deleted.]{#passwd-home-deleted explanation="Home-directory information is stored in field 6 and is unrelated to the `x` placeholder."}
::option[Protected password data is kept in the shadow database.]{#passwd-shadow-placeholder .correct explanation="The public passwd record carries a placeholder while password hash and aging fields live in protected shadow data."}
:::

## Recognizing Service Accounts

Many records represent services rather than people. Separate service identities help confine files and processes to the authority required by one daemon. Their home paths can be nonstandard or nonexistent, and their login program may be `/usr/sbin/nologin`, `/bin/false`, or another restricted program.

Do not infer account purpose from UID range alone without checking the distribution's policy. Allocation ranges vary, and centrally managed accounts may follow different conventions.

:::single-choice{#passwd-nologin-shell}
What is a common purpose of a login program such as `/usr/sbin/nologin` in field 7?

::option[Delete the account's files whenever a service stops.]{#passwd-nologin-delete explanation="The login program does not automatically remove owned data or manage service shutdown files."}
::option[Prevent an ordinary interactive shell through login paths that honor the field.]{#passwd-nologin-purpose .correct explanation="A non-login program is commonly used for service accounts that should not receive an interactive shell through normal login."}
::option[Grant the account the same privileges as UID 0.]{#passwd-nologin-root explanation="Restricting interactive login does not elevate the account or change its numeric UID."}
:::

## Modifying Account Records Safely

Prefer account-management tools such as `useradd`, `usermod`, and `userdel` because they coordinate related records and apply system defaults. Their exact behavior is distribution-configurable, so review options before changing an account.

If a local passwd database truly requires manual repair, use `vipw` rather than an ordinary editor. It applies locking intended to avoid concurrent edits. Validate databases with tools such as `pwck` and maintain a recovery session before changing authentication files remotely.

To practice user and group records in a controlled environment, try these hands-on labs:

1. **[Manage Linux User Accounts with useradd, usermod, and userdel](https://labex.io/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Practice the complete lifecycle of user administration, from creating and securing new accounts to modifying and deleting them.
2. **[Manage Linux Groups with groupadd, usermod, and groupdel](https://labex.io/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Gain hands-on experience with core command-line utilities for group administration, including creating new groups and modifying user memberships.
## Summary

You can now interpret local passwd records without mistaking them for the complete identity database.

1. Query NSS-resolved accounts with `getent passwd`.
2. Read the seven colon-separated passwd fields.
3. Locate the UID and primary GID fields.
4. Interpret password placeholders without overclaiming login state.
5. Use account tools or `vipw` instead of an ordinary editor.
