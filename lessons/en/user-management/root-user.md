---
lesson_id: "root-user"
course_id: "user-management"
lang: "en"
order_index: 2
title: "root"
description: "Learn how su, sudo, and sudoers policy provide controlled access to privileged identities."
meta_title: "root - User Management"
meta_description: "Explore the role of the root user in Linux. This lesson covers the differences between su and sudo for gaining superuser privileges and explains how the /etc/sudoers file manages access."
meta_keywords: "root user in linux, linux root user, su, sudo, sudoers, visudo, superuser, user management, linux permissions"
---

The account traditionally named `root` has UID 0 and broad authority in its security context. Use an unprivileged account for routine work and elevate only for a specific administrative purpose you understand.

## Starting a Shell as Another User with su

`su`, meaning substitute user, starts a shell or command with another account's identity. With no username, the target defaults to root:

```bash
$ su
```

Authentication is controlled by PAM and local policy. A system may ask for the target account's password, restrict who can use `su`, or keep the root password locked. Do not assume knowledge of a password is the only condition.

Plain `su` changes identity while preserving more of the current environment. `su - USER`, also written `su --login USER`, starts a login-style shell and initializes an environment closer to a fresh login for the target account:

```bash
$ su - operator
```

Exit the subshell when the target-specific work is complete.

:::single-choice{#root-su-login-shell}
Which command requests a login-style shell as the user `operator`?

::option[`su - operator`]{#root-su-login-operator .correct explanation="The hyphen requests login-shell behavior and a target-oriented environment for `operator`."}
::option[`su operator`]{#root-su-preserve-environment explanation="This changes to the target identity but does not request the full login-style initialization introduced here."}
::option[`sudo -l operator`]{#root-sudo-list-operator explanation="`sudo -l` lists allowed commands under policy; it does not start the requested login shell."}
:::

## Running a Specific Command with sudo

`sudo COMMAND` requests policy authorization to run one command as a target user, usually root by default. Use `-u USER` to request another target:

```bash
$ sudo -u postgres id
```

This does not mean the request will be permitted. Sudo policy controls the invoking user, host, target identity, command, and other conditions. Authentication may use the invoking user's password, another mechanism, or no prompt depending on configuration.

Prefer one narrowly scoped administrative command over a long-lived privileged shell when practical. The smaller scope makes accidental commands less likely to run with elevated authority.

:::single-choice{#root-sudo-target-user}
What does `sudo -u postgres id` request?

::option[Permanently rename the current account to `postgres`.]{#root-sudo-rename explanation="`sudo` runs a command with target credentials; it does not rename account records."}
::option[Run `id` with `postgres` as the target user, subject to policy.]{#root-sudo-postgres-id .correct explanation="The `-u` option selects the target identity, while sudoers policy decides whether the request is allowed."}
::option[List every user whose UID is greater than the current user's.]{#root-sudo-list-uids explanation="The `id` command reports identity information for its process; this syntax does not enumerate account UIDs."}
:::

## Avoiding Persistent Privileged Shells

Commands such as `su -`, `sudo -s`, or `sudo -i` can create a privileged shell when policy permits. Every later command in that shell can have elevated impact until you exit it. Path mistakes, unreviewed scripts, and shell expansions become more dangerous.

Audit behavior is configuration-dependent. `sudo` commonly records invocations, but a single logged shell launch does not automatically provide a complete record of every command typed inside that shell. Shell history, system audit, and sudo I/O logging are separate mechanisms with their own policies.

:::single-choice{#root-persistent-shell-risk}
Why is a long-lived root shell riskier than elevating one understood command at a time?

::option[Root shells automatically delete every command from all audit systems.]{#root-shell-no-audit explanation="Logging varies by configuration; it is inaccurate to claim that all audit records are automatically erased."}
::option[The shell disables filesystem pathnames longer than one component.]{#root-shell-path-limit explanation="Privilege does not impose this pathname restriction; the concern is the authority applied to ordinary operations."}
::option[Later commands can retain elevated impact until the shell exits.]{#root-shell-elevated-scope .correct explanation="A persistent privileged identity expands the window in which a typo or untrusted command can modify protected resources."}
:::

## Reviewing sudo Authorization

Run `sudo -l` to list what the current account may request under the active policy:

```bash
$ sudo -l
```

Review command paths, permitted target users, and argument restrictions. A broad-looking rule should not be treated as permission to perform unrelated work.

:::single-choice{#root-list-sudo-rules}
Which command lists sudo privileges available to the current invoking user?

::option[`sudo -i`]{#root-sudo-login explanation="This requests a target login-style shell and can increase privilege scope; it is not a read-only policy listing."}
::option[`sudo -l`]{#root-sudo-list .correct explanation="The lowercase `-l` option asks sudo to list the commands allowed by its current policy."}
::option[`su -l`]{#root-su-login-default explanation="This invokes login-shell behavior for `su` rather than listing sudo authorization."}
:::

## Editing sudoers Policy Safely

The default sudo policy commonly reads `/etc/sudoers` and may include files under `/etc/sudoers.d/`. Other policy sources are possible. Syntax controls much more than a simple list of users and groups.

Use `visudo` for policy changes because it locks the file and validates syntax before installation:

```bash
$ sudo visudo
```

For a drop-in file, specify its exact path:

```bash
$ sudo visudo -f /etc/sudoers.d/application-admins
```

Do not edit sudoers with an ordinary redirection or unvalidated editor workflow. A syntax or permission mistake can remove administrative access. Keep another verified recovery path available when changing remote authorization.

:::single-choice{#root-edit-sudoers-safely}
Which tool should be used to edit and syntax-check the main sudoers policy?

::option[`cat`]{#root-cat-sudoers explanation="`cat` can display readable text but does not safely edit, lock, or validate sudoers syntax."}
::option[`visudo`]{#root-visudo .correct explanation="`visudo` provides locking and syntax validation designed for sudoers policy changes."}
::option[`echo` with `>`]{#root-echo-sudoers explanation="Shell redirection can truncate policy immediately and offers no sudoers syntax validation."}
:::

To practice delegated administration in a controlled environment, try this hands-on lab:

1. **[Configure User Accounts and Sudo Privileges in Linux](https://labex.io/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Practice enforcing password policies, locking and unlocking user accounts, securing the root account, and granting administrative permissions, directly relating to the management of superuser access.

## Summary

You can now distinguish identity switching from policy-controlled command delegation.

1. Use `su - USER` only when a target login shell is intended.
2. Request a specific sudo target with `-u USER`.
3. Minimize time spent in a privileged shell.
4. Review effective sudo rules with `sudo -l`.
5. Edit sudoers policy only through `visudo`.
