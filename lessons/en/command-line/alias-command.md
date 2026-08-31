---
lesson_id: "alias-command"
course_id: "command-line"
lang: "en"
order_index: 18
title: "alias"
description: "Learn how to create, inspect, persist, bypass, and remove command aliases in Bash."
meta_title: "alias - Command Line"
meta_description: "Learn the Linux alias command with examples for creating temporary aliases, saving aliases in .bashrc, listing aliases, and removing them with unalias."
meta_keywords: "linux alias command, alias command, bash alias, .bashrc alias, unalias command, command shortcut linux, shell alias"
---

An alias tells an interactive shell to replace one command word with another string before executing the line. This can shorten a frequent command or provide a preferred set of options.

## Creating an Alias in the Current Shell

In Bash, define an alias with `alias NAME='REPLACEMENT'`. Do not put spaces around the equals sign:

```bash
$ alias ll='ls -la'
```

After this definition, entering `ll` as a command expands to `ls -la`. The quotes keep the replacement together while the alias is being defined.

Aliases are best for simple command-prefix substitutions. Use a shell function when you need to process arguments in a more structured way.

:::single-choice{#define-ll-alias}
Which Bash command defines `ll` as an alias for `ls -la` in the current shell?

::option[`alias ll = 'ls -la'`]{#alias-spaces explanation="Spaces around `=` split the definition into separate shell words, so Bash does not receive a valid alias assignment."}
::option[`alias ll='ls -la'`]{#alias-ll .correct explanation="This uses the required `NAME=REPLACEMENT` form and quotes the replacement containing a space."}
::option[`unalias ll='ls -la'`]{#unalias-definition explanation="`unalias` removes existing alias names. It does not create a replacement."}
:::

## Loading an Alias in Future Bash Sessions

An alias defined at the prompt belongs to the current shell and disappears when that shell exits. Interactive non-login Bash sessions normally read `~/.bashrc`, so that file is the usual place for personal Bash aliases:

```bash
alias ll='ls -la'
```

After editing the file, start a new interactive Bash session or reload it in the current shell:

```bash
$ source ~/.bashrc
```

Shell startup behavior can vary by shell, login mode, and distribution configuration. A Zsh user, for example, would normally use Zsh configuration rather than Bash's `.bashrc`.

:::single-choice{#persist-bash-alias}
Where should a personal alias normally be defined so future interactive non-login Bash sessions load it?

::option[In the user's `~/.bashrc` file.]{#bashrc-alias .correct explanation="Interactive non-login Bash normally reads `~/.bashrc`, making it the conventional location for personal Bash aliases."}
::option[In the executable file used by the aliased command.]{#edit-executable explanation="Changing an installed executable is unrelated to shell alias expansion and can damage managed system files."}
::option[In the current terminal's scrollback history.]{#terminal-scrollback explanation="Scrollback only records displayed text. Bash does not execute it as startup configuration."}
:::

## Inspecting Aliases and Name Resolution

Run `alias` without arguments to list aliases in the current shell:

```bash
$ alias
alias ll='ls -la'
alias grep='grep --color=auto'
```

Use `type NAME` to inspect how Bash resolves a particular name:

```bash
$ type ll
ll is aliased to 'ls -la'
```

:::single-choice{#inspect-command-alias}
Which command shows whether Bash currently resolves `ll` as an alias, function, builtin, or executable?

::option[`file ll`]{#file-ll explanation="`file` classifies a filesystem pathname. An alias exists in shell state and need not correspond to a file named `ll`."}
::option[`type ll`]{#type-ll .correct explanation="The `type` builtin reports how the current Bash session resolves the name `ll`."}
::option[`whatis ll`]{#whatis-ll explanation="`whatis` queries manual-page descriptions. Personal aliases normally have no manual database entry."}
:::

## Bypassing and Removing an Alias

To bypass an alias for one command line, prefix the command name with a backslash or put it after Bash's `command` builtin:

```bash
$ \ls
$ command ls
```

This is useful when you need the underlying command's normal behavior. Keep aliases short and predictable, and avoid hiding surprising or destructive behavior behind familiar command names.

:::single-choice{#bypass-ls-alias}
The current Bash session has an alias named `ls`. Which command bypasses that alias for one invocation?

::option[`alias ls`]{#show-ls-alias explanation="This prints the definition of the `ls` alias. It does not invoke the underlying command."}
::option[`command ls`]{#command-ls .correct explanation="Because `command` is the command word, Bash does not expand the following `ls` as an alias and invokes normal command resolution."}
::option[`source ls`]{#source-ls explanation="`source` reads a file as shell code in the current shell. It is not a safe or appropriate way to bypass an alias."}
:::

Remove an alias from the current shell with `unalias`:

```bash
$ unalias ll
```

If the definition remains in `~/.bashrc`, a future shell can create it again. Remove or change that configuration line as well when you want the alias gone permanently.

:::single-choice{#remove-current-alias}
Which command removes the alias `ll` from the current Bash session?

::option[`unalias ll`]{#unalias-ll .correct explanation="`unalias` deletes the named alias from the current shell's alias table."}
::option[`alias ll=''`]{#empty-ll explanation="This replaces the alias with an empty expansion rather than removing its definition."}
::option[`command ll`]{#command-ll explanation="`command` can bypass alias expansion on that line, but it does not delete the alias from shell state."}
:::

## Summary

You can now customize Bash with simple, inspectable aliases.

1. Define a temporary alias with correct quoting.
2. Load personal aliases from `~/.bashrc` in future sessions.
3. Inspect aliases and command resolution.
4. Bypass an alias for one invocation.
5. Remove both the active and saved definition when required.
