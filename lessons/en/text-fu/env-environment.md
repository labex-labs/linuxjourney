---
index: 5
lang: "en"
title: "env (Environment)"
meta_title: "env (Environment) - Text-Fu"
meta_description: "Explore what the env command does in Linux. This guide explains how to view and use Linux environment variables like PATH, HOME, and USER with the env linux command."
meta_keywords: "env, linux env, env linux, env command linux, linux env command, what does env do in linux, environment variables, PATH variable, shell variables"
---

## Lesson Content

Your Linux system uses environment variables to store information that the shell and other processes can access. These variables contain useful data about your user session and system configuration.

### Exploring Basic Environment Variables

You can view the value of a specific variable by prefixing its name with a `$` symbol. For example, run the following command:

```bash
echo $HOME
```

This command will display the path to your home directory, which might look something like `/home/pete`.

Now, try another one:

```bash
echo $USER
```

This will output your current username. But where does this information come from? It's stored in your shell's environment.

### What Does env Do in Linux

To see all the environment variables currently set for your session, you can use the `env` command. The `linux env command` is a fundamental tool for inspecting your shell's configuration.

```bash
env
```

Running the `env` command will output a list of key-value pairs. Here is a short example of what you might see:

```plaintext
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/bin
PWD=/home/user
USER=pete
```

Understanding the `linux env` is crucial for managing your system effectively.

### The Importance of the PATH Variable

One of the most important variables in your `env linux` output is `PATH`. You can view its contents specifically with:

```bash
echo $PATH
```

This command returns a colon-separated list of directories. When you type a command, your system searches through these directories to find the corresponding executable file.

Imagine you manually install a program in a non-standard directory like `/opt/coolapp/bin`. If you try to run it by typing `coolcommand`, you might get a "command not found" error. This happens because the directory containing your program is not listed in the `PATH` variable, so the shell doesn't know where to look for it.

To fix this, you can modify the `PATH` variable to include the new directory. By adding your custom directory to `PATH`, you enable the shell to find and execute your programs from anywhere in the terminal.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of Linux environment variables:

1.  **[Manage Shell Environment and Configuration in Linux](https://labex.io/labs/comptia-manage-shell-environment-and-configuration-in-linux-590838)** - Practice creating and managing local and environment variables, understanding inheritance, and making configurations persistent by modifying the `.bashrc` file.
2.  **[Environment Variables in Linux](https://labex.io/labs/linux-environment-variables-in-linux-385274)** - Learn the concept and usage of environment variables, how to create, modify, and manage them, and their role in system configuration.
3.  **[Configure Linux Environment Variables](https://labex.io/labs/linux-configure-linux-environment-variables-437861)** - Get hands-on experience creating, setting, and managing environment variables in a Linux system.

These labs will help you apply the concepts in real scenarios and build confidence with managing your Linux shell environment.

## Quiz Question

Which command displays all of your current environment variables? (Please answer in English, using only the lowercase command name).

## Quiz Answer

env
