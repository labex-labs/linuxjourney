---
title: "The Shell"
description: "Learn about the Linux shell, Bash, and basic commands like 'echo'. Understand shell prompts and start your Linux journey with this beginner-friendly guide."
keywords: "Linux shell, Bash, echo command, Linux tutorial, command line, beginner Linux, shell prompt, Linux guide"
---

## Lesson Content

The world is your oyster, or rather, the shell is your oyster. What is the shell? The shell is basically a program that takes your commands from the keyboard and sends them to the operating system to perform. If you’ve ever used a GUI, you’ve probably seen programs such as "Terminal" or "Console"; these are just programs that launch a shell for you. Throughout this entire course, we will be learning about the wonders of the shell.

In this course, we will use the shell program Bash (Bourne Again Shell). Almost all Linux distributions will default to the Bash shell. There are other shells available, such as `ksh`, `zsh`, and `tsch`, but we won’t get into any of those.

Let’s jump right in! Depending on the distribution, your shell prompt might change, but for the most part, it should adhere to the following format:

```plaintext
username@hostname:current_directory
pete@icebox:/home/pete $
```

Notice the `$` at the end of the prompt? Different shells will have different prompts. In our case, the `$` is for a normal user using Bash, Bourne, or Korn shell. You don't add the prompt symbol when you type the command; just know that it's there.

Let’s start with a simple command, `echo`. The `echo` command just prints out the text arguments to the display.

```bash
echo Hello World
```

## Exercise

Try some other Linux commands and see what they output:

1. `$ date`
2. `$ whoami`

## Quiz Question

What should be outputted to the display when you type `echo Hello World`?

## Quiz Answer

Hello World
