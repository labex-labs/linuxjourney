---
index: 18
lang: "en"
title: "alias"
meta_title: "alias - Command Line"
meta_description: "Learn how to create and manage a command alias in Linux to streamline your workflow. This guide covers creating temporary and permanent aliases using the alias command and the .bashrc file."
meta_keywords: "linux alias, alias command linux, command alias in linux, linux command alias, bash alias, unalias command, .bashrc, command line, Linux tutorial"
---

## Lesson Content

Typing long or repetitive commands can be tedious. Fortunately, you can create a shortcut, or a **Linux alias**, to make your command-line experience more efficient. The `alias` command lets you define a custom name for any command or sequence of commands.

### Creating a Temporary Alias

To create a temporary alias that lasts for your current terminal session, you simply specify a name and set it equal to the command string.

For example, to create an alias named `ll` for the `ls -la` command, you would use the `alias command linux` syntax like this:

```bash
alias ll='ls -la'
```

Now, instead of typing `ls -la`, you can just type `ll`, and it will execute the same command. This is a simple yet powerful way to customize your shell.

### Making an Alias Permanent

A temporary alias will disappear once you close your terminal or reboot your system. To make a `command alias in linux` permanent, you need to add it to your shell's configuration file. For the Bash shell, this file is typically `~/.bashrc`.

1.  Open the file in a text editor: `nano ~/.bashrc`
2.  Add your alias definition to the file, just as you typed it on the command line:

```bash
alias ll='ls -la'
alias update='sudo apt update && sudo apt upgrade'
```

3.  Save the file and exit the editor.

For the changes to take effect, you must either close and reopen your terminal or tell the shell to reload the configuration file using the `source` command:

```bash
source ~/.bashrc
```

Your **Linux command alias** will now be available every time you start a new terminal session.

### Removing an Alias

If you no longer need an alias, you can remove it with the `unalias` command. This will remove it from your current session.

```bash
unalias ll
```

To remove a permanent alias, you must also delete its definition from your `~/.bashrc` file.

## Exercise

While there are no specific labs for this topic, we recommend exploring the comprehensive [Linux Learning Path](https://labex.io/learn/linux) to practice related Linux skills and concepts.

## Quiz Question

What command is used to create an alias? Please answer in lowercase English.

## Quiz Answer

alias
