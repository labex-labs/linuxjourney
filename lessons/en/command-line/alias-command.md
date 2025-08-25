---
index: 18
lang: "en"
title: "alias"
meta_title: "alias - Command Line"
meta_description: "Learn how to create and manage Linux aliases for common commands. Discover temporary and permanent alias setup in .bashrc. Improve your command-line efficiency!"
meta_keywords: "Linux alias, bash alias, unalias command, .bashrc, Linux tutorial, command line, beginner Linux, Linux guide"
---

## Lesson Content

Sometimes typing commands can get really repetitive, or if you need to type a long command many times, it's best to have an alias you can use for that. To create an alias for a command, you simply specify an alias name and set it to the command.

```bash
alias foobar='ls -la'
```

Now, instead of typing `ls -la`, you can type `foobar`, and it will execute that command—pretty neat stuff. Keep in mind that this command won't save your alias after reboot, so you'll need to add a permanent alias in:

```plaintext
~/.bashrc
```

or similar files if you want to have it persist after reboot.

You can remove aliases with the `unalias` command:

```bash
unalias foobar
```

## Exercise

While there are no specific labs for this topic, we recommend exploring the comprehensive [Linux Learning Path](https://labex.io/learn/linux) to practice related Linux skills and concepts.

## Quiz Question

What command is used to make an alias?

## Quiz Answer

alias
