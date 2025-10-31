---
index: 17
lang: "en"
title: "whatis"
meta_title: "whatis - Command Line"
meta_description: "Discover the whatis command in Linux. Learn how the linux whatis command provides one-line descriptions of other commands, making it a vital tool for navigating the command line."
meta_keywords: "whatis command in linux, whatis linux, linux whatis command, whatis command linux, linux whatis, command line, linux commands"
---

## Lesson Content

As you explore the Linux command line, you'll encounter a vast number of commands. It's natural to forget what a specific command does. Fortunately, there's a simple utility to help you out.

### What is the whatis Command in Linux

The `whatis` command in Linux displays a concise, one-line description of a command directly from its manual (man) page. It's a quick way to get a reminder of a command's primary function without reading the entire man page. Think of the **linux whatis** command as a quick dictionary for your terminal.

### How to Use the whatis Command

Using the **whatis command linux** is straightforward. Simply type `whatis` followed by the name of the command you want to know about. For example, if you're unsure about the `cat` command, you can run:

```bash
whatis cat
```

This will return a short description, such as "cat - concatenate files and print on the standard output".

### Understanding the Output

The description provided by the **linux whatis command** is sourced directly from the NAME section of the command's manual page. This ensures the information is accurate and consistent with the system's documentation. If a command has multiple manual pages in different sections, `whatis` may display a line for each, helping you understand its various contexts.

## Exercise

Practice makes perfect! While there isn't a specific lab for the `whatis` command, understanding how to find information about commands and files is crucial. Here are some hands-on labs to reinforce your understanding of locating commands and files in Linux:

1. **[Linux which Command: Command Locating](https://labex.io/labs/linux-linux-which-command-command-locating-215210)** - Practice using the `which` command to locate executable files and understand command priority in your system's PATH.
2. **[Linux whereis Command: File and Command Finding](https://labex.io/labs/linux-linux-whereis-command-file-and-command-finding-215211)** - Learn to use `whereis` to find the binary, source, and manual pages for commands, deepening your understanding of how commands are structured.
3. **[Discover Critical System Resources](https://labex.io/labs/linux-discover-critical-system-resources-388032)** - This challenge combines `which`, `whereis`, and `find` to help you efficiently navigate the file system and discover important system resources.

These labs will help you apply the concepts of command and file discovery in real scenarios and build confidence with essential Linux utilities.

## Quiz Question

What command can you use to see a small description of a command? Please answer in English, paying attention to lowercase.

## Quiz Answer

whatis
