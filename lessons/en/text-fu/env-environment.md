---
lesson_id: "env-environment"
course_id: "text-fu"
lang: "en"
order_index: 5
title: "env (Environment)"
description: "Learn how Bash expands, exports, inspects, and temporarily overrides environment variables."
meta_title: "env (Environment) - Text-Fu"
meta_description: "Explore what the env command does in Linux. This guide explains how to view and use Linux environment variables like PATH, HOME, and USER with the env linux command."
meta_keywords: "env, linux env, env linux, env command linux, linux env command, what does env do in linux, environment variables, PATH variable, shell variables"
---

Every process has an environment: a collection of name-value strings inherited from its parent process. Shells use environment variables to pass configuration such as language settings and executable search paths to the programs they start.

## Expanding Variable Values in Bash

Bash expands `$NAME` or `${NAME}` to a variable's value before it runs a command. Quote the expansion to preserve the value as one argument:

```bash
$ printf '%s\n' "$HOME"
/home/pete
```

Common environment variables include:

- `HOME`: The current user's home-directory path.
- `USER`: A username supplied by the login environment on many systems.
- `PWD`: The shell's current working directory.
- `PATH`: Directories searched for command names.

Values depend on the current process environment; they are not universal constants. An unset variable expands to an empty string unless stricter shell behavior is enabled.

:::single-choice{#env-print-home-value} Which Bash command prints the value of `HOME` while preserving it as one argument?

::option[`printf '%s\n' '$HOME'`]{#env-literal-home explanation="Single quotes prevent parameter expansion, so this prints the literal characters `$HOME`."}
::option[`printf '%s\n' "$HOME"`]{#env-quoted-home .correct explanation="Bash expands `$HOME` inside double quotes, and `printf` receives the complete value as one argument."}
::option[`printf '%s\n' HOME`]{#env-name-home explanation="Without a dollar sign or parameter syntax, `HOME` is ordinary text rather than a variable expansion."}
:::

## Inspecting the Current Environment

Run `env` without operands to print the environment inherited by that `env` process:

```bash
$ env
```

The output contains `NAME=value` records, for example:

```plaintext
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/bin
PWD=/home/user
USER=pete
```

Environment variables can contain credentials, tokens, internal paths, or other sensitive data. Do not paste complete `env` output into public issues or logs without reviewing and redacting it.

:::single-choice{#env-list-exported-values} Which command prints the environment visible to a newly started process?

::option[`env`]{#env-print-all .correct explanation="With no command or assignments, `env` prints the name-value environment it received."}
::option[`alias`]{#env-alias-list explanation="`alias` lists shell alias definitions, which are shell state rather than exported environment records."}
::option[`history`]{#env-history-list explanation="`history` displays the shell's remembered command lines. It does not enumerate exported variables."}
:::

## Finding Commands through PATH

`PATH` is a colon-separated list of directories that Bash searches when a command name contains no slash:

```bash
$ printf '%s\n' "$PATH"
```

The order matters: Bash uses the first suitable command it finds according to its resolution rules. Use `type -a NAME` to inspect how the current shell resolves a name.

To add `/opt/coolapp/bin` for the current shell and its future children while retaining the existing search path:

```bash
$ export PATH="/opt/coolapp/bin:$PATH"
```

Do not replace `PATH` accidentally with only the new directory, and do not add untrusted writable directories. Either mistake can prevent normal commands from resolving or cause an unexpected executable to run.

:::single-choice{#env-prepend-path-directory} Which command adds `/opt/coolapp/bin` before the existing `PATH` for the current Bash process and its future children?

::option[`export PATH="/opt/coolapp/bin"`]{#env-replace-path explanation="This discards every existing search directory, which can make ordinary commands difficult to find."}
::option[`export PATH="/opt/coolapp/bin:$PATH"`]{#env-export-path .correct explanation="This prepends the new directory, retains the previous value, and exports the result for child processes."}
::option[`PATH='$PATH:/opt/coolapp/bin'`]{#env-literal-path explanation="Single quotes preserve the literal text `$PATH`, and the assignment is not exported to future child processes."}
:::

## Exporting a Variable to Child Processes

Bash variables are not automatically part of the environment given to child processes. Mark a name for export with `export`:

```bash
$ export TEST=test
```

The current Bash process now has a variable named `TEST`, and commands it starts inherit `TEST=test`. A child process cannot use this mechanism to change its parent's environment.

```bash
$ printenv TEST
test
```

The assignment normally lasts until you unset it or the shell exits. It does not modify a system-wide environment.

:::single-choice{#env-export-inheritance} What is the main effect of `export TEST=test` in Bash?

::option[It writes `TEST` into every user's system configuration.]{#env-system-wide explanation="The assignment affects the current shell and inheritance by its children, not every user or the whole operating system."}
::option[It marks `TEST=test` for inheritance by future child processes.]{#env-child-inheritance .correct explanation="`export` adds the shell variable to the environment Bash passes to commands it starts."}
::option[It changes the environment of processes that are already running.]{#env-existing-processes explanation="Existing unrelated or child processes keep their own environments. Export affects processes started afterward."}
:::

## Setting a Value for One Command

Place assignments before a command to supply values only to that command's environment:

```bash
$ LANG=C sort names.txt
```

The current shell's `LANG` value is not permanently changed. The `env` utility provides another explicit form:

```bash
$ env LANG=C sort names.txt
```

Use `env -i COMMAND` to start a command with an initially empty environment, then add any required assignments. Many programs rely on environment values, so use that option deliberately.

:::single-choice{#env-one-command-value} Which command runs `sort names.txt` with `LANG=C` without permanently changing the current shell's `LANG`?

::option[`env LANG=C sort names.txt`]{#env-lang-sort .correct explanation="`env` adds the assignment to the environment of the command it starts, while the parent shell keeps its prior value."}
::option[`export LANG=C; sort names.txt`]{#env-export-lang explanation="This exports `LANG=C` in the current shell and leaves it changed after `sort` finishes."}
::option[`env -i sort names.txt`]{#env-empty-sort explanation="This starts with an empty environment but does not set the requested `LANG=C` value."}
:::

## Loading Personal Values in Future Sessions

To recreate an exported variable in future interactive Bash sessions, place a suitable `export` line in the startup file those sessions actually read, commonly `~/.bashrc` for interactive non-login Bash:

```bash
export TEST=test
```

Zsh commonly uses `~/.zshrc`, while Fish uses different syntax and configuration. Login and non-interactive shells can read other files, so identify the shell and session type instead of assuming one file configures every process.

To practice environment inheritance and shell configuration, try these hands-on labs:

1. **[Manage Shell Environment and Configuration in Linux](https://labex.io/labs/comptia-manage-shell-environment-and-configuration-in-linux-590838)** - Practice creating and managing local and environment variables, understanding inheritance, and making configurations persistent by modifying the `.bashrc` file.
2. **[Environment Variables in Linux](https://labex.io/labs/linux-environment-variables-in-linux-385274)** - Learn the concept and usage of environment variables, how to create, modify, and manage them, and their role in system configuration.
## Summary

You can now inspect and control the environment passed from Bash to child processes.

1. Expand variable values with deliberate quoting.
2. Review exported values without exposing secrets.
3. Preserve and order command directories in `PATH`.
4. Export a shell variable for future child processes.
5. Override a value for one command without changing the parent shell.
