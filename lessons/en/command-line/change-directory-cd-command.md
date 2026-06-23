---
index: 3
lang: "en"
title: "cd (Change Directory)"
meta_title: "cd (Change Directory) - Command Line"
meta_description: "Learn the Linux cd command with examples for absolute paths, relative paths, home directory shortcuts, parent directories, and previous directory navigation."
meta_keywords: "cd command, linux cd command, change directory, cd parent directory, cd home, cd previous directory, absolute path, relative path"
---

## Lesson Content

To move around the Linux filesystem, you use paths to specify your destination. The primary tool for this is the `cd` command, short for change directory. It changes the shell's current working directory.

The basic syntax is:

```bash
cd [DIRECTORY]
```

### Understanding Paths

There are two ways to specify a path: absolute and relative.

- **Absolute path**: The full path starting from the root directory (`/`). For example: `/home/pete/Desktop`.

- **Relative path**: A path based on your current location. If you are in `/home/pete/Documents` and want to access a subdirectory named `taxes`, you can use `taxes/`.

### Using the cd Command

To change to a specific directory using an absolute path, type:

```bash
$ cd /home/pete/Pictures
```

This command moves you directly to the `Pictures` directory.

You can confirm your location with `pwd`:

```bash
$ pwd
/home/pete/Pictures
```

### Navigating to a Subdirectory

If you are already in a directory and want to move to a subdirectory, use a relative path. For instance, if your current location is `/home/pete/Pictures` and it contains a folder named `Hawaii`, you can navigate into it with:

```bash
$ cd Hawaii
```

Notice we only used the folder's name. This is because we were already in its parent directory, `/home/pete/Pictures`.

### Essential Navigation Shortcuts

Navigating with full paths can be tedious. Fortunately, the shell provides several shortcuts to make moving around much faster.

- `.` (current directory): Represents the directory you are currently in.
- `..` (parent directory): Moves you one level up to the directory containing your current one.
- `~` (home directory): A shortcut to your personal home directory, like `/home/pete`.
- `-` (previous directory): Takes you back to the last directory you were in.

You can use these shortcuts with `cd`:

```bash
$ cd .
$ cd ..
$ cd ~
$ cd -
```

Experiment with these shortcuts to become more efficient on the command line.

### Practical cd Examples

Go to your home directory:

```bash
$ cd
```

Go up two levels:

```bash
$ cd ../..
```

Go to a directory whose name contains spaces by quoting it:

```bash
$ cd "Vacation Photos"
```

Go back to the previous directory:

```bash
$ cd -
/home/pete/Documents
```

### Common Questions

**Why does cd say "No such file or directory"?** The path does not exist from your current location, or the name was typed incorrectly. Use `ls` to list available directories.

**Why does cd say "Permission denied"?** You do not have permission to enter that directory.

**What happens when I run cd with no arguments?** It takes you to your home directory.

**Does cd work on files?** No. `cd` changes into directories, not regular files.

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
