---
index: 19
lang: "en"
title: "exit"
meta_title: "exit - Command Line"
meta_description: "Learn the Linux exit command, how to close a shell session, how logout differs from exit, and how exit status values work."
meta_keywords: "exit command, linux exit, logout command, shell session, terminal exit, exit status, bash exit"
---

## Lesson Content

Congratulations on completing the foundational lessons of your Linux journey! You have covered essential Linux basics, and now it is time to learn how to properly end your session. Exiting the Linux shell is a simple but important final step.

### The Exit Command

The most common way to end a shell session is with the `exit` command. When you type `exit` and press Enter, the current shell process terminates. This command works in virtually any shell environment.

```bash
$ exit
```

If you opened a terminal window, `exit` usually closes the shell running inside it. If you connected through SSH, `exit` ends the remote shell session and returns you to your local prompt.

### Exit Status Values

The `exit` command can also return a status code. A status of `0` usually means success, and a nonzero status usually means an error or special condition.

```bash
$ exit 0
```

You will see exit statuses more often when writing shell scripts. For interactive use, simply typing `exit` is enough.

### The Logout Command

Another command you can use for a terminal exit is `logout`. This command is specifically designed to terminate a login shell. While in many modern systems it behaves similarly to `exit`, it's good practice to know both commands.

```bash
$ logout
```

### Closing the Terminal Window

If you are working within a graphical user interface, you also have the option to simply close the terminal window. This action typically sends a signal that terminates the shell session running inside it.

### Common Ways to Leave a Shell

- Type `exit` to end the current shell.
- Press `Ctrl-D` on an empty prompt to send end-of-file, which often exits the shell.
- Type `logout` when you are in a login shell.
- Close the terminal window when using a graphical terminal.

### Common Questions

**Is exit the same as closing the terminal window?** Often the result is similar, but `exit` cleanly tells the shell to terminate.

**What is Ctrl-D?** It sends an end-of-file signal to the shell. At an empty prompt, this usually exits.

**What does exit 1 mean?** It exits with status code `1`, commonly used to indicate failure in scripts.

You have successfully learned how to navigate, work with files, get help, and exit the shell.

## Exercise

While there are no specific labs for this topic, we recommend exploring the comprehensive [Linux Learning Path](https://labex.io/learn/linux) to practice related Linux skills and concepts.

## Quiz Question

What is the most common command to exit from the Linux shell? Please answer using only a single lowercase English word.

## Quiz Answer

exit
