---
index: 17
lang: "en"
title: "whatis"
meta_title: "whatis - Command Line"
meta_description: "Learn the Linux whatis command with examples for getting one-line command descriptions from man pages and understanding multiple manual sections."
meta_keywords: "whatis command, linux whatis, command description linux, man page summary, command line help, apropos"
---

## Lesson Content

As you explore the Linux command line, you'll encounter a vast number of commands. It's natural to forget what a specific command does. Fortunately, there's a simple utility to help you out.

### What is the whatis Command

The `whatis` command displays a concise, one-line description of a command directly from its manual page. It is a quick way to get a reminder of a command's primary function without reading the entire man page.

### How to Use the whatis Command

Using `whatis` is straightforward. Type `whatis` followed by the command you want to know about.

```bash
$ whatis cat
cat (1)              - concatenate files and print on the standard output
```

### Understanding the Output

The description provided by `whatis` comes from the `NAME` section of the command's manual page. If a name has multiple manual pages in different sections, `whatis` may display more than one line.

```bash
$ whatis passwd
passwd (1)           - change user password
passwd (5)           - the password file
```

The number in parentheses is the man page section.

### Whatis vs Man vs Apropos

- `whatis ls`: Show a one-line description for an exact command name.
- `man ls`: Open the full manual page.
- `apropos keyword`: Search man page descriptions for a keyword.

For example:

```bash
$ apropos password
```

Use `whatis` when you know the command name but forgot what it does.

### Common Questions

**Why does whatis say "nothing appropriate"?** The command may not have a man page installed, or the man database may need updating.

**Does whatis show command options?** No. Use `man COMMAND` or `COMMAND --help` for options.

**Is whatis the same as which?** No. `whatis` describes a command. `which` shows the executable path.

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
