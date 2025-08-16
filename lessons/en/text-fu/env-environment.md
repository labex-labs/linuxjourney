---
lang: "en"
title: "env (Environment)"
description: "Learn about Linux environment variables with 'env' command. Understand PATH, HOME, and USER variables. Get a beginner's guide to managing your Linux environment."
keywords: "env command, Linux environment variables, PATH variable, Linux tutorial, beginner Linux, shell variables, Linux guide"
---

## Lesson Content

Run the following command:

```bash
echo $HOME
```

You should see the path to your home directory; mine looks like /home/pete.

What about this command?

```bash
echo $USER
```

You should see your username!

Where is this information coming from? It's coming from your environment variables. You can view these by typing:

```bash
env
```

This outputs a whole lot of information about the environment variables you currently have set. These variables contain useful information that the shell and other processes can use.

Here is a short example:

```plaintext
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/bin
PWD=/home/user
USER=pete
```

One particularly important variable is the PATH variable. You can access these variables by sticking a `$` in front of the variable name like so:

```bash
$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/bin
```

This returns a list of paths separated by a colon that your system searches when it runs a command. Let's say you manually download and install a package from the internet and put it into a non-standard directory, and you want to run that command. You type `$ coolcommand`, and the prompt says "command not found." Well, that's silly; you are looking at the binary in a folder and know it exists. What is happening is that the `$PATH` variable doesn't check that directory for this binary, so it's throwing an error.

Let's say you had tons of binaries you wanted to run out of that directory; you can just modify the PATH variable to include that directory in your PATH environment variable.

## Exercise

What does the following output? Why?

```bash
echo $HOME
```

## Quiz Question

How do you see your environment variables?

## Quiz Answer

env
