---
lang: "en"
title: "Controlling Terminal"
meta_title: "Controlling Terminal - Processes"
meta_description: "Learn about controlling terminals in Linux, including TTY vs. PTS, and how processes are bound to them. Understand daemon processes. Start your Linux journey!"
meta_keywords: "controlling terminal, TTY, PTS, Linux terminal, daemon processes, Linux beginner, Linux tutorial, Linux guide"
---

## Lesson Content

We discussed how there is a TTY field in the `ps` output. The TTY is the terminal that executed the command.

There are two types of terminals: regular **terminal devices** and **pseudoterminal devices**. A regular terminal device is a native terminal device that you can type into and send output to your system. This sounds like the terminal application you've been launching to get to your shell, but it's not.

We're going to segue so you can see this in action. Go ahead and type Ctrl-Alt-F1 to get into TTY1 (the first virtual console). You'll notice how you don't have anything except the terminal—no graphics, etc. This is considered a regular terminal device. You can exit this with Ctrl-Alt-F7.

A pseudoterminal is what you've been used to working in. They emulate terminals with the shell terminal window and are denoted by PTS. If you look at `ps` again, you'll see your shell process under `pts/*`.

Okay, now circling back to the controlling terminal: processes are usually bound to a controlling terminal. For example, if you were running a program in your shell window, such as `find`, and you closed the window, your process would also terminate with it.

There are processes such as daemon processes, which are special processes that are essentially keeping the system running. They often start at system boot and usually get terminated when the system is shut down. They run in the background, and since we don't want these special processes to get terminated, they are not bound to a controlling terminal. In the `ps` output, the TTY is listed as a **?**, meaning it does not have a controlling terminal.

## Exercise

Look at your `ps` output and list all the unique TTY values.

## Quiz Question

What value is given for a process that does not have a controlling terminal?

## Quiz Answer

?
