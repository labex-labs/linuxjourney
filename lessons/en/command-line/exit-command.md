---
lesson_id: "exit-command"
course_id: "command-line"
lang: "en"
order_index: 19
title: "exit"
description: "Learn how to leave the current shell and choose the status it returns to its caller."
meta_title: "exit - Command Line"
meta_description: "Learn the Linux exit command, how to close a shell session, how logout differs from exit, and how exit status values work."
meta_keywords: "exit command, linux exit, logout command, shell session, terminal exit, exit status, bash exit"
---

Shells can be nested: a graphical terminal starts a shell, an SSH connection starts a remote shell, and a shell can start another shell. Leaving one normally returns control to whatever started that current shell.

## Leaving the Current Shell

The `exit` command asks the current shell to terminate:

```bash
$ exit
```

If that shell is the main process in a graphical terminal tab, the tab may close according to the terminal's settings. In an SSH session, leaving the remote shell normally returns you to the local shell. If you started a nested shell, `exit` returns to its parent shell.

:::single-choice{#leave-current-shell} You started Bash inside another shell and now want to return to the parent shell. Which command should you run in the nested Bash session?

::option[`clear`]{#clear-nested explanation="`clear` refreshes the visible terminal area but leaves the current shell running."}
::option[`exit`]{#exit-nested .correct explanation="`exit` terminates the current shell, allowing its parent shell to resume."}
::option[`history -c`]{#clear-nested-history explanation="This clears Bash's in-memory history list. It does not terminate the current shell."}
:::

## Returning an Exit Status

An optional numeric argument sets the status returned to the shell's caller:

```bash
$ exit 0
```

By convention, `0` means success and a nonzero value represents failure or another condition defined by the program. If Bash receives no numeric argument, it exits with the status of the last command executed before `exit`.

:::single-choice{#return-success-status} Which command terminates the current shell and explicitly reports success to its caller?

::option[`exit 0`]{#exit-zero .correct explanation="Status `0` conventionally reports successful completion to the caller."}
::option[`exit 1`]{#exit-one explanation="A nonzero status conventionally indicates failure or another exceptional result rather than success."}
::option[`logout 0`]{#logout-zero explanation="Bash `logout` is for a login shell and does not use this form to set the requested status."}
:::

:::single-choice{#exit-without-number} In Bash, what status does `exit` return when you do not provide a number?

::option[It always returns a successful status of `0`.]{#always-zero explanation="A successful convention does not force a bare `exit` to return zero. Bash preserves a previous status in this case."}
::option[It always returns a failure status of `1`.]{#always-one explanation="Bash does not assign failure status `1` to every bare `exit`. The preceding command determines the value."}
::option[It returns the previous command's exit status.]{#last-command-status .correct explanation="Without an explicit numeric argument, Bash exits using the most recent command status."}
:::

## Using logout in a Login Shell

The Bash `logout` builtin exits a login shell:

```bash
$ logout
```

In a non-login Bash shell, `logout` reports that it is not a login shell; use `exit` instead.

:::single-choice{#leave-login-shell} Which Bash builtin is specifically intended to leave a login shell?

::option[`logout`]{#logout-login .correct explanation="Bash provides `logout` for terminating a login shell."}
::option[`unalias`]{#unalias-login explanation="`unalias` removes alias definitions from the current shell. It does not end the session."}
::option[`source`]{#source-login explanation="`source` reads commands from a file into the current shell. It does not terminate that shell."}
:::

## Using Ctrl+D or Closing a Terminal

At an empty interactive prompt, pressing `Ctrl+D` normally supplies the terminal's end-of-file input character. Bash commonly interprets that condition as a request to exit. It is not a signal, and shell settings such as Bash's `ignoreeof` can change the behavior.

Closing a graphical terminal window asks the terminal application to close its processes and can affect running jobs. Prefer an orderly `exit` when practical, and check for active work before closing a session.

## Summary

You can now leave the current shell and communicate its completion status.

1. Use `exit` to return to the current shell's caller.
2. Supply `0` for success or a defined nonzero status otherwise.
3. Understand the status used by a bare `exit`.
4. Use `logout` only for a login shell.
5. Recognize `Ctrl+D` as end-of-file input rather than a signal.
