---
index: 18
lang: "en"
title: "alias"
meta_title: "alias - Command Line"
meta_description: "Learn the Linux alias command with examples for creating temporary aliases, saving aliases in .bashrc, listing aliases, and removing them with unalias."
meta_keywords: "linux alias command, alias command, bash alias, .bashrc alias, unalias command, command shortcut linux, shell alias"
---

## Lesson Content

Typing long or repetitive commands can be tedious. An alias is a shell shortcut that lets you define a custom name for a command or sequence of commands.

### Creating a Temporary Alias

To create a temporary alias that lasts for your current terminal session, you simply specify a name and set it equal to the command string.

For example, create an alias named `ll` for `ls -la`:

```bash
$ alias ll='ls -la'
```

Now, instead of typing `ls -la`, you can just type `ll`, and it will execute the same command. This is a simple yet powerful way to customize your shell.

### Making an Alias Permanent

A temporary alias will disappear once you close your terminal or reboot your system. To make a `command alias in linux` permanent, you need to add it to your shell's configuration file. For the Bash shell, this file is typically `~/.bashrc`.

1. Open the file in a text editor: `nano ~/.bashrc`
2. Add your alias definition to the file, just as you typed it on the command line:

```bash
alias ll='ls -la'
alias update='sudo apt update && sudo apt upgrade'
```

3. Save the file and exit the editor.

For the changes to take effect, you must either close and reopen your terminal or tell the shell to reload the configuration file using the `source` command:

```bash
$ source ~/.bashrc
```

Your alias will now be available every time you start a new Bash session.

### Removing an Alias

If you no longer need an alias, you can remove it with the `unalias` command. This will remove it from your current session.

```bash
$ unalias ll
```

To remove a permanent alias, you must also delete its definition from your `~/.bashrc` file.

### Listing Existing Aliases

Run `alias` with no arguments to list aliases in your current shell.

```bash
$ alias
alias ll='ls -la'
alias grep='grep --color=auto'
```

Use `type` to see what will run when you enter a command:

```bash
$ type ll
ll is aliased to 'ls -la'
```

### Useful Alias Examples

```bash
$ alias la='ls -la'
$ alias ..='cd ..'
$ alias grep='grep --color=auto'
```

Keep aliases short and predictable. Avoid replacing destructive commands with surprising behavior unless you are very sure.

### Common Questions

**Do aliases work in scripts?** Usually no, not by default. Scripts should use full commands or functions.

**Where should Bash aliases go?** Put them in `~/.bashrc` for interactive Bash sessions.

**What if an alias conflicts with a real command?** The alias usually takes priority in interactive shell use. Use `command name` or `\name` to bypass an alias.

## Exercise

While there are no specific labs for this topic, we recommend exploring the comprehensive [Linux Learning Path](https://labex.io/learn/linux) to practice related Linux skills and concepts.

## Quiz Question

What command is used to create an alias? Please answer in lowercase English.

## Quiz Answer

alias
