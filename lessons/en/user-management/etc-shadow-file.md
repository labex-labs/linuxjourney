---
lesson_id: "etc-shadow-file"
course_id: "user-management"
lang: "en"
order_index: 4
title: "/etc/shadow"
description: "Learn how local shadow records represent password hashes and aging policy without exposing sensitive data."
meta_title: "/etc/shadow - User Management"
meta_description: "Explore the /etc/shadow file in Linux, a critical component for user authentication. Learn how to view it with 'cat /etc/shadow' and understand the structure of the etc shadow file, which stores encrypted passwords and policy information."
meta_keywords: "etc shadow, etc/shadow file in linux, cat /etc/shadow, etc shadow in linux, /etc/shadow, user authentication, password security, Linux system administration"
---

`/etc/shadow` stores protected local password-hash and password-aging fields. Separating these values from the generally readable `/etc/passwd` database reduces exposure to offline password-guessing attacks.

## Protecting Shadow Data

Passwords are not stored reversibly “encrypted” for later display. A local password entry normally contains a one-way password hash encoded with an algorithm identifier, salt, and parameters. An attacker who obtains hashes can guess candidate passwords offline, so the database should remain restricted.

Exact ownership and permission details vary, but access is commonly limited to root and narrowly authorized system components. Do not print, copy, log, or share shadow contents merely to inspect account status.

:::single-choice{#shadow-restricted-reason} Why is local shadow data normally protected from general read access?

::option[The file contains every user's unencrypted current password.]{#shadow-plaintext-passwords explanation="Proper shadow entries store one-way password hashes or special markers, not retrievable plaintext passwords."}
::option[Password hashes can be attacked offline if they are disclosed.]{#shadow-offline-guessing .correct explanation="An attacker can test password guesses against stolen hashes without interacting with the login service."}
::option[Reading it automatically changes all password-expiration dates.]{#shadow-read-changes explanation="A read does not inherently update policy fields; the concern is disclosure of sensitive authentication material."}
:::

## Reading the Nine-Field Format

A local shadow record contains nine colon-separated fields. A schematic record looks like this, with the hash deliberately omitted:

```text
alice:<password-field>:20000:0:90:7:14:20500:
```

The fields are:

1. **Login name**.
2. **Password hash or special password marker**.
3. **Last password change**, in days since 1970-01-01; `0` requests a change at the next password-authenticated login in typical tooling.
4. **Minimum password age**, in days.
5. **Maximum password age**, in days.
6. **Warning period** before password expiration, in days.
7. **Inactivity period** after password expiration, in days.
8. **Account expiration date**, in days since 1970-01-01.
9. **Reserved field**.

Empty fields and special numeric values have defined meanings that can vary by field and tooling. Use account-management commands instead of editing values by sight.

:::single-choice{#shadow-account-expiration-field} Which shadow field stores the account expiration date as days since 1970-01-01?

::option[Field 3]{#shadow-field-three explanation="Field 3 records the last password-change date rather than account expiration."}
::option[Field 8]{#shadow-field-eight .correct explanation="The eighth field is the absolute account-expiration day count."}
::option[Field 5]{#shadow-field-five explanation="Field 5 records the maximum password age."}
:::

## Interpreting the Password Field Carefully

A valid hash in field 2 supports local Unix-password verification. A value beginning with `!` commonly locks that password hash, while `*` or another invalid hash marker prevents successful password verification through that field. An empty value is security-sensitive and can allow passwordless behavior depending on PAM policy.

These markers describe the local password path, not every possible authentication method. SSH public keys, certificates, tokens, and application-specific credentials can remain usable unless separately restricted. Account expiration in field 8 is also distinct from password locking.

:::single-choice{#shadow-password-lock-scope} What can you safely conclude from a shadow password field that begins with `!`?

::option[The stored Unix password hash has been made unusable for normal password verification.]{#shadow-password-locked .correct explanation="Prefixing the hash with `!` prevents it from matching a supplied password through the shadow password path."}
::option[Every possible login method for the account is disabled.]{#shadow-all-login-disabled explanation="Other authentication methods can be independent, so the password marker alone does not prove a complete account lockout."}
::option[The account has been deleted from all identity databases.]{#shadow-account-deleted explanation="A shadow record still exists, and deletion is a separate account-management operation."}
:::

## Distinguishing Password and Account Dates

Fields 3 through 7 concern password aging: when the password last changed, when another change is allowed, when it expires, when warnings begin, and how long after expiration password login remains available. Field 8 expires the account on an absolute day regardless of the password's age.

For example, a 90-day maximum password age is not the same as an account expiration date. The former moves relative to the last password change; the latter is a fixed date until an administrator changes it.

:::single-choice{#shadow-max-age-versus-expire} What is the difference between shadow fields 5 and 8?

::option[Field 5 stores the username; field 8 stores the login shell.]{#shadow-username-shell explanation="Username is field 1, and the login shell is recorded in `/etc/passwd`, not the shadow record."}
::option[Field 5 stores a password hash; field 8 stores its salt.]{#shadow-hash-salt explanation="The password hash encoding belongs in field 2, and aging fields do not separately store its salt."}
::option[Field 5 is maximum password age; field 8 is an absolute account expiration date.]{#shadow-password-vs-account-expiry .correct explanation="Password age is relative to the last change, while account expiration is stored as an absolute day count."}
:::

## Inspecting and Changing Policy through Tools

Administrators should query only the information required for the task:

```bash
$ sudo passwd -S alice
$ sudo chage -l alice
```

`passwd -S` summarizes local password status, while `chage -l` lists aging information in a readable form. Output formats and authorization requirements can vary by distribution.

Use `passwd`, `chage`, `usermod`, and related account tools for changes. If manual repair of the local shadow database is unavoidable, `vipw -s` provides locking; validate account databases with `pwck`. Maintain a recovery session before remote authentication changes.

:::single-choice{#shadow-list-aging-policy} Which command is designed to list readable password-aging information for the local account `alice`?

::option[`cat /etc/shadow`]{#shadow-cat-entire-file explanation="This exposes every local shadow record and more sensitive information than the task requires."}
::option[`passwd -d alice`]{#shadow-passwd-delete explanation="The `-d` operation removes the password hash and is a state-changing, security-sensitive action rather than a listing command."}
::option[`chage -l alice`]{#shadow-chage-list .correct explanation="The lowercase `-l` option asks `chage` to display the account's password-aging fields in readable form."}
:::

PAM and NSS can integrate authentication and identity sources beyond local shadow files. A system account may therefore have no local shadow record or may authenticate through additional services.

To practice account status and aging policy in a controlled environment, try these hands-on labs:

1. **[Manage Linux User Accounts with useradd, usermod, and userdel](https://labex.io/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Practice the complete lifecycle of user administration, from creating and securing new accounts with `useradd` and `passwd` to modifying and deleting them.
2. **[Configure User Accounts and Sudo Privileges in Linux](https://labex.io/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Learn essential techniques for managing user accounts and sudo privileges, including enforcing password policies and securing accounts.

## Summary

You can now interpret shadow policy without exposing the complete password database.

1. Treat password hashes as restricted authentication material.
2. Read the nine shadow fields by purpose.
3. Distinguish password locking from disabling every login method.
4. Separate password aging from absolute account expiration.
5. Inspect and change policy through focused account tools.
