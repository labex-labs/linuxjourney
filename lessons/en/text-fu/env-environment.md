---
index: 5
lang: "en"
title: "env (Environment)"
meta_title: "env (Environment) - Text-Fu"
meta_description: "Learn about Linux environment variables with 'env' command. Understand PATH, HOME, and USER variables. Get a beginner's guide to managing your Linux environment."
meta_keywords: "env command, Linux environment variables, PATH variable, Linux tutorial, beginner Linux, shell variables, Linux guide"
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

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of Linux environment variables:

1. **[Manage Shell Environment and Configuration in Linux](https://labex.io/labs/comptia-manage-shell-environment-and-configuration-in-linux-590838)** - Practice creating and managing local and environment variables, understanding inheritance, and making configurations persistent by modifying the `.bashrc` file.
2. **[Environment Variables in Linux](https://labex.io/labs/linux-environment-variables-in-linux-385274)** - Learn the concept and usage of environment variables, how to create, modify, and manage them, and their role in system configuration.
3. **[Configure Linux Environment Variables](https://labex.io/labs/linux-configure-linux-environment-variables-437861)** - Get hands-on experience creating, setting, and managing environment variables in a Linux system.

These labs will help you apply the concepts in real scenarios and build confidence with managing your Linux shell environment.

## Quiz Question

How do you see your environment variables?

## Quiz Answer

env
