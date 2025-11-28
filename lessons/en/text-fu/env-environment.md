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

### Setting an Environment Variable for the Current Session

Running the following command in your terminal sets the environment variable `TEST` for the current session only:

```bash
export TEST=test
```

After this, if you run:

```bash
echo $TEST
```

The output will be:

```
test
```

This variable will be available as long as the terminal session remains open. Once you close and reopen the terminal, the variable will no longer exist.

### Making the Environment Variable Persistent Across Sessions

If you want the environment variable to be available in every terminal session (even after closing and reopening the terminal), you need to add it to your shell’s startup file. In the case of Bash (the default shell for many Linux distributions and macOS), this file is usually `.bashrc` in your home directory.

Here's how you do it:

1. Open `.bashrc` in your preferred text editor. For example:

    ```bash
    nano ~/.bashrc
    ```

2. Add the `export` line to the end of the file:

    ```bash
    export TEST=test
    ```

3. Save and exit the editor (in Nano, this would be `Ctrl+X`, then `Y` to confirm, and `Enter`).

4. To apply the changes immediately without reopening the terminal, run:

    ```bash
    source ~/.bashrc
    ```

After this, the `TEST` variable will be available in all future terminal sessions, and running `echo $TEST` will print `test` even after you close and reopen the terminal.

### A Note on Shell Configuration Files

- For **Bash** (the default on many systems), the relevant file is `~/.bashrc` for non-login interactive shells.
- For **Zsh**, the equivalent file is usually `~/.zshrc`.
- For **Fish**, you'd typically use `~/.config/fish/config.fish`.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of Linux environment variables:

1. **[Manage Shell Environment and Configuration in Linux](https://labex.io/labs/comptia-manage-shell-environment-and-configuration-in-linux-590838)** - Practice creating and managing local and environment variables, understanding inheritance, and making configurations persistent by modifying the `.bashrc` file.
2. **[Environment Variables in Linux](https://labex.io/labs/linux-environment-variables-in-linux-385274)** - Learn the concept and usage of environment variables, how to create, modify, and manage them, and their role in system configuration.
3. **[Configure Linux Environment Variables](https://labex.io/labs/linux-configure-linux-environment-variables-437861)** - Get hands-on experience creating, setting, and managing environment variables in a Linux system.

These labs will help you apply the concepts in real scenarios and build confidence with managing your Linux shell environment.

## Quiz Question

Which command displays all of your current environment variables? (Please answer in English, using only the lowercase command name).

## Quiz Answer

env
