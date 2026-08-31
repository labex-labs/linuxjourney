---
lesson_id: "setuid-set-user-id"
course_id: "permissions"
lang: "en"
order_index: 5
title: "Setuid"
description: "Learn how the set-user-ID mode bit affects executable programs and why it requires careful security review."
meta_title: "Setuid - Permissions"
meta_description: "Learn about Linux Setuid (SUID) permissions, how they work, and how to modify them. Understand SUID for secure file access in Linux."
meta_keywords: "Linux Setuid, SUID, Linux permissions, chmod, passwd command, Linux security, beginner Linux, Linux tutorial"
---

Some programs need narrowly controlled access that their callers do not ordinarily have. On an executable regular file, the set-user-ID bit can cause a new process to receive the file owner's user ID as its effective user ID. The program can then perform operations authorized for that identity while retaining information about the caller.

Setuid is not a general instruction to “run as root.” Its effect depends on the executable's owner, the operating system, the filesystem and mount options, and the way the program manages its credentials.

## Recognizing Setuid

On systems that use a setuid `passwd` executable, a long listing may resemble:

```bash
$ ls -l /usr/bin/passwd
-rwsr-xr-x 1 root root 68248 Jan 10 09:30 /usr/bin/passwd
```

The lowercase `s` in the owner's execute position means both setuid and owner execute are set. If setuid is present but owner execute is absent, `ls -l` displays an uppercase `S` in that position.

Do not assume every distribution has the same mode or authentication design. Inspect the actual system rather than relying on the example.

:::single-choice{#setuid-lowercase-s}
What does lowercase `s` in the owner's execute position indicate?

::option[Setuid is set but owner execute is absent.]{#setuid-s-without-execute explanation="That combination is displayed as uppercase `S`, not lowercase `s`."}
::option[The file has a sticky bit and group execute.]{#setuid-sticky-group explanation="The sticky bit appears in the other execute position, while setuid appears in the owner position."}
::option[Setuid is set and owner execute is also set.]{#setuid-s-with-execute .correct explanation="Lowercase `s` represents the setuid bit together with the ordinary owner execute bit."}
:::

## Understanding the Credential Change

When the kernel honors setuid during execution, the new process normally gets an effective user ID based on the executable's owner. For a root-owned program, that can provide root-authorized access, but only while the program runs and only through the operations its code performs.

This mechanism can allow a carefully written program to validate a request and make a restricted change to protected state. For example, a local password-changing utility may need controlled access to authentication data that ordinary users cannot edit directly. Modern implementations also rely on PAM, file locking, policy, and other safeguards; setuid alone does not explain the complete workflow.

:::single-choice{#setuid-effective-identity}
When a setuid executable is honored, which identity is primarily taken from the file owner?

::option[The login name stored in `/etc/passwd`.]{#setuid-login-name explanation="Executing a file does not rewrite the caller's account record or login name."}
::option[The process's effective user ID.]{#setuid-effective-user .correct explanation="The set-user-ID execution mechanism changes the effective user identity used for many authorization checks."}
::option[The group owner of every opened file.]{#setuid-opened-file-group explanation="Setuid affects process credentials, not ownership metadata on unrelated files."}
:::

## Setting and Removing the Bit

Set setuid symbolically with:

```bash
$ sudo chmod u+s myfile
```

In octal notation, setuid contributes `4` in a leading special-bits digit:

```bash
$ sudo chmod 4755 myfile
```

Here, the leading `4` sets setuid and `755` sets the ordinary owner, group, and other bits. Remove setuid without otherwise changing the mode with `chmod u-s myfile`.

:::single-choice{#setuid-octal-value}
Which leading octal value represents the setuid special bit?

::option[`4`]{#setuid-octal-four .correct explanation="Setuid contributes value `4` in the leading special-bits digit."}
::option[`1`]{#setuid-octal-one explanation="A leading `1` represents the sticky bit."}
::option[`2`]{#setuid-octal-two explanation="A leading `2` represents the setgid bit."}
:::

## Treating Setuid as Security-Sensitive

A flaw in a privileged setuid program can become a privilege-escalation path. Such programs must validate input, control the environment and file paths they trust, avoid unsafe subprocess behavior, minimize privileged code, and drop elevated credentials as soon as possible.

Linux normally does not honor setuid on interpreted scripts because doing so safely has race and interpreter-related problems. Filesystems mounted with `nosuid` also suppress setuid and setgid effects. Prefer narrower mechanisms such as service-mediated operations, carefully scoped `sudo` policy, or capabilities when they fit the requirement.

Never add setuid to an arbitrary shell, interpreter, or copied program as an experiment on a shared system. Audit existing setuid files and practice only in an isolated disposable environment.

:::single-choice{#setuid-nosuid-mount}
What is the purpose of mounting a filesystem with `nosuid`?

::option[Remove every execute bit stored on files in that filesystem.]{#setuid-nosuid-remove-execute explanation="The option does not rewrite ordinary execute bits in file metadata."}
::option[Suppress setuid and setgid execution effects on that filesystem.]{#setuid-nosuid-suppress .correct explanation="The `nosuid` mount option prevents those special mode bits from granting their normal credential-changing execution behavior."}
::option[Make all files on the filesystem owned by root.]{#setuid-nosuid-root-owner explanation="Mounting with `nosuid` does not change user or group ownership fields."}
:::

## Summary

You can now recognize setuid and explain its credential and security implications.

1. Find `s` or `S` in the owner's execute position.
2. Relate setuid execution to the executable owner's effective user identity.
3. Set or remove the bit with symbolic or octal `chmod` modes.
4. Treat every privileged executable as security-sensitive code.
