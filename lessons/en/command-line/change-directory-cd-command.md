---
index: 3
lang: "en"
title: "cd (Change Directory)"
meta_title: "cd (Change Directory) - Command Line"
meta_description: "Learn the essential cd linux command to change directories. This guide covers using the cd command in a command prompt, navigating to any cd folder with absolute and relative paths, and using helpful shortcuts."
meta_keywords: "cd command, cd linux command, cd folder, cd command prompt, cd command cmd, change directory, linux navigation, absolute path, relative path"
---

## Lesson Content

To move around the Linux filesystem, you'll use paths to specify your destination. The primary tool for this is the `cd` (change directory) command. Understanding how to use this `cd linux command` is a fundamental skill for working in the terminal or `cd command prompt`.

### Understanding Paths

There are two ways to specify a path: absolute and relative.

- **Absolute Path**: This is the full path starting from the root directory (`/`). The root is the top-level directory in the filesystem. Any path that begins with `/` is an absolute path. For example: `/home/pete/Desktop`.

- **Relative Path**: This path is relative to your current location in the filesystem. If you are in `/home/pete/Documents` and want to access a subdirectory named `taxes`, you don't need the full path. You can simply use the relative path: `taxes/`.

### Using the cd Command

Once you understand paths, you can use the `cd command` to change your current directory. Whether you're in a Linux terminal or a Windows `cd command cmd` prompt, the concept of changing directories is universal, though the syntax may differ slightly.

To change to a specific directory using an absolute path, you would type:

```bash
cd /home/pete/Pictures
```

This command moves you directly to the `Pictures` directory.

### Navigating to a cd folder

If you are already in a directory and want to move to a sub-directory, you can use a relative path. For instance, if your current location is `/home/pete/Pictures` and it contains a `cd folder` named `Hawaii`, you can navigate into it with:

```bash
cd Hawaii
```

Notice we only used the folder's name. This is because we were already in its parent directory, `/home/pete/Pictures`.

### Essential Navigation Shortcuts

Navigating with full paths can be tedious. Fortunately, the shell provides several shortcuts to make moving around much faster.

- `.` (current directory): Represents the directory you are currently in.
- `..` (parent directory): Moves you one level up to the directory containing your current one.
- `~` (home directory): A shortcut to your personal home directory, like `/home/pete`.
- `-` (previous directory): Takes you back to the last directory you were in.

You can use these shortcuts with the `cd command`:

```bash
cd .
cd ..
cd ~
cd -
```

Experiment with these shortcuts to become more efficient on the command line.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of Linux directory navigation:

1. **[Linux cd Command: Directory Changing](https://labex.io/labs/linux-linux-cd-command-directory-changing-209733)** - Learn the Linux `cd` command to efficiently navigate your file system, including various techniques for changing directories, understanding paths, and exploring the file structure.
2. **[Linux Directory Navigation](https://labex.io/labs/linux-directory-navigation-387844)** - Put your basic Linux command-line skills to the test by navigating through directories using essential commands.
3. **[Setting Up a New Project Structure](https://labex.io/labs/linux-setting-up-a-new-project-structure-387859)** - Practice your Linux directory management skills by creating a specific project structure and navigating through it using essential commands like `mkdir` and `cd`.

These labs will help you apply the concepts in real scenarios and build confidence with navigating the Linux filesystem.

## Quiz Question

If you are in `/home/pete/Pictures` and want to navigate to the parent directory (`/home/pete`), what is the full command you should use? Please answer in English, paying attention to case and spacing.

## Quiz Answer

cd ..
