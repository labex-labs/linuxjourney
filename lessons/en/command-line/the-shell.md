---
lesson_id: "the-shell"
course_id: "command-line"
lang: "en"
order_index: 1
title: "The Shell"
description: "Learn what the Linux shell is and how commands are executed."
meta_title: "The Shell - Command Line"
meta_description: "Learn what the Linux shell is, how the Bash prompt works, and how to run your first command with beginner-friendly command line examples."
meta_keywords: "linux shell, bash shell, command line, linux terminal, shell prompt, echo command, basic linux commands"
---

## What is the Linux Shell

Welcome to your Linux journey! The first step is understanding the Linux shell. A shell is a program that accepts commands you type, asks the operating system to run them, and then prints the result back to your terminal.

If you have used a graphical user interface, you are used to clicking windows, menus, and buttons. In the command line, you type precise instructions instead. Applications named "Terminal", "Console", or "Konsole" usually open a shell session for you.

The terminal is the window or app you type into, while the shell is the program running inside it.

The shell is useful because it is fast, scriptable, and available on almost every Linux system. As you learn more commands, you can combine them to inspect files, manage directories, search text, install software, and automate repeated work.

:::single-choice{#distinguish-shell-and-terminal} Which statement correctly describes the relationship between a terminal and a shell?

::option[The terminal provides the window, while the shell runs inside it.]{#shell-runs-in-terminal .correct explanation="The terminal is the interface you use, and the shell is the command-processing program running inside it."}
::option[The terminal accepts commands, while the shell only displays their output.]{#terminal-accepts-commands explanation="This reverses their roles. The terminal provides the interface, while the shell accepts and runs commands."}
::option[The terminal and the shell are two names for the same program.]{#terminal-equals-shell explanation="They work together, but they are not the same program. A terminal opens a session in which a shell runs."}
:::

## Interacting with the Bash Shell

For this course, we will focus on Bash, short for Bourne Again Shell. Bash is one of the most common Linux shells and is a good foundation even if you later use `zsh`, `fish`, or another shell.

When you open a terminal, you will be greeted by the shell prompt. Its appearance can vary, but it often shows your username, host name, and current directory.

```plaintext
pete@icebox:/home/pete $
```

The `$` symbol indicates that the shell is ready to accept your input as a normal user. You do not type this symbol when entering commands; it is shown by the shell. If you see `#` instead, you are usually working as the root user, which has more power and more risk.

:::single-choice{#interpret-dollar-prompt} What does the `$` at the end of the example prompt indicate?

::option[The shell is running with the privileges of the root user.]{#root-user-ready explanation="A root prompt usually ends with `#`, not `$`. Root access carries additional power and risk."}
::option[The shell is waiting for input from a normal user.]{#normal-user-ready .correct explanation="The `$` marks a normal user prompt and shows that the shell is ready for a command."}
::option[The next command must begin with a dollar sign.]{#type-dollar-first explanation="The `$` belongs to the prompt. You type the command that follows it, without copying the symbol."}
:::

Commands often follow this pattern:

```bash
command options arguments
```

For example, in `echo Hello World`, `echo` is the command and `Hello World` is the text passed to it.

:::single-choice{#identify-command-name} In `echo Hello World`, which part is the command name?

::option[`Hello`]{#hello-command explanation="`Hello` comes after the command name, so it is part of the text passed to `echo`."}
::option[`World`]{#world-command explanation="`World` is also text passed to `echo`, not the name of the command being run."}
::option[`echo`]{#echo-command .correct explanation="`echo` names the program the shell should run. The words after it are passed to that program as arguments."}
:::

## Your First Linux Command

Let's start with one of the most basic Linux commands for beginners: `echo`. This command displays the text you provide back to the terminal.

```bash
$ echo Hello World
Hello World
```

Try a few more examples:

```bash
$ echo Linux is fun
Linux is fun
$ echo "Hello from Bash"
Hello from Bash
```

Quotes are useful when you want the shell to treat several words as one piece of text.

:::single-choice{#group-words-with-quotes} Which command makes the shell treat `Hello from Bash` as one quoted piece of text?

::option[`echo "Hello from Bash"`]{#quoted-words .correct explanation="The quotation marks group the three words into one argument passed to `echo`."}
::option[`echo Hello from Bash`]{#unquoted-words explanation="This prints the same visible words, but the shell treats them as separate arguments because they are not quoted."}
::option[`"echo Hello from Bash"`]{#quoted-command explanation="Quoting the entire line makes the shell look for a command with that full name instead of running `echo` with text."}
:::

To practice these skills, explore the comprehensive [Shell Learning Path](https://labex.io/learn/shell).

## Common Beginner Tips

- Press `Enter` to run a command.
- Use the `Up Arrow` key to recall a previous command.
- Commands and filenames are case-sensitive in Linux.
- Spaces matter. `echo hello` and `echohello` are different.
- If a command seems stuck, `Ctrl-C` often cancels it.

## Summary

You can now explain the role of a shell and interact with a basic shell prompt.

1. Distinguish between a terminal and a shell.
2. Identify a command prompt.
3. Run a simple command with `echo`.
