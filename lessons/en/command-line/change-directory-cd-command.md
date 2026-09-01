---
lesson_id: "change-directory-cd-command"
course_id: "command-line"
lang: "en"
order_index: 3
title: "cd (Change Directory)"
description: "Learn how to use cd with paths and shortcuts to move through the Linux filesystem."
meta_title: "cd (Change Directory) - Command Line"
meta_description: "Learn the Linux cd command with examples for absolute paths, relative paths, home directory shortcuts, parent directories, and previous directory navigation."
meta_keywords: "cd command, linux cd command, change directory, cd parent directory, cd home, cd previous directory, absolute path, relative path"
---

To move around the Linux filesystem, you use paths to specify your destination. The primary tool for this is the `cd` command, short for change directory. It changes the shell's current working directory.

The destination must be a directory rather than a regular file. If the directory does not exist, its name is typed incorrectly, or you lack permission to enter it, `cd` reports an error instead of changing location.

The basic syntax is:

```bash
cd [DIRECTORY]
```

## Understanding Paths

There are two ways to specify a path: absolute and relative.

- **Absolute path**: The full path starting from the root directory (`/`). For example: `/home/pete/Desktop`.

- **Relative path**: A path based on your current location. If you are in `/home/pete/Documents` and want to access a subdirectory named `taxes`, you can use `taxes/`.

:::single-choice{#recognize-absolute-cd-path} Which statement correctly describes an absolute path?

::option[It begins at whichever directory the shell currently uses]{#begins-at-current-directory explanation="A path that depends on the shell's current location is relative. It does not necessarily begin at the root."}
::option[It contains only the final directory name without parents]{#contains-final-name-only explanation="A single destination name is normally interpreted relative to the current directory. An absolute path includes its route from `/`."}
::option[It begins at the root directory, represented by `/`]{#begins-at-root .correct explanation="An absolute path starts at the filesystem root. The leading `/` makes its starting point independent of the current directory."}
:::

## Using the cd Command

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

:::single-choice{#verify-changed-directory} Which command confirms the shell's current location after `cd`?

::option[`cd`]{#cd-command explanation="`cd` changes the current directory but does not normally print the resulting full path. Use `pwd` to confirm it."}
::option[`ls`]{#ls-command explanation="`ls` displays directory contents. It can help you inspect a location, but `pwd` reports the location itself."}
::option[`pwd`]{#pwd-command .correct explanation="`pwd` prints the current working directory. It lets you verify where `cd` moved the shell."}
:::

## Navigating to a Subdirectory

If you are already in a directory and want to move to a subdirectory, use a relative path. For instance, if your current location is `/home/pete/Pictures` and it contains a folder named `Hawaii`, you can navigate into it with:

```bash
$ cd Hawaii
```

Notice we only used the folder's name. This is because we were already in its parent directory, `/home/pete/Pictures`.

## Essential Navigation Shortcuts

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

:::single-choice{#move-to-parent-directory} From `/home/pete/Pictures`, which command moves to `/home/pete`?

::option[`cd .`]{#cd-current explanation="`.` represents the current directory. This command leaves the shell in `/home/pete/Pictures`."}
::option[`cd -`]{#cd-previous explanation="`-` returns to the previous working directory, which is not necessarily the parent. Use `..` when the destination is one level up."}
::option[`cd ..`]{#cd-parent .correct explanation="`..` represents the parent of the current directory. From `Pictures`, its parent is `/home/pete`."}
:::

:::single-choice{#return-to-previous-directory} Which command returns to the directory used immediately before the current one?

::option[`cd -`]{#previous-directory .correct explanation="`cd -` switches to the previous working directory. That directory can be anywhere in the filesystem."}
::option[`cd ..`]{#parent-directory explanation="`cd ..` moves to the parent directory. The parent and previous directory are not always the same place."}
::option[`cd ~`]{#home-directory explanation="`cd ~` moves to your home directory. It does not track the directory you visited immediately before."}
:::

Experiment with these shortcuts to become more efficient on the command line.

## Practical cd Examples

Go to your home directory:

```bash
$ cd
```

Running `cd` with no directory argument also takes you to your home directory.

Go up two levels:

```bash
$ cd ../..
```

Go to a directory whose name contains spaces by quoting it:

```bash
$ cd "Vacation Photos"
```

:::single-choice{#enter-directory-with-spaces} Which command treats `Vacation Photos` as one directory name?

::option[`cd Vacation Photos`]{#unquoted-directory-name explanation="Without quotes, the shell passes `Vacation` and `Photos` as separate arguments rather than one directory name."}
::option[`"cd Vacation Photos"`]{#quote-entire-command explanation="Quoting the entire line makes the shell treat it as one command name. The command itself must remain outside the path quotes."}
::option[`cd "Vacation Photos"`]{#quote-directory-name .correct explanation="The quotation marks group both words into one path argument for `cd`."}
:::

Go back to the previous directory:

```bash
$ cd -
/home/pete/Documents
```

To reinforce your understanding of Linux directory navigation, try these hands-on labs:

1. **[Linux cd Command: Directory Changing](https://labex.io/labs/linux-linux-cd-command-directory-changing-209733)** - Learn the Linux `cd` command to efficiently navigate your file system, including various techniques for changing directories, understanding paths, and exploring the file structure.
2. **[Linux Directory Navigation](https://labex.io/labs/linux-directory-navigation-387844)** - Put your basic Linux command-line skills to the test by navigating through directories using essential commands.
3. **[Setting Up a New Project Structure](https://labex.io/labs/linux-setting-up-a-new-project-structure-387859)** - Practice your Linux directory management skills by creating a specific project structure and navigating through it using essential commands like `mkdir` and `cd`.

## Summary

You can now use `cd` to move between directories with full paths and shell shortcuts.

1. Distinguish absolute paths from relative paths.
2. Change directories and verify the result with `pwd`.
3. Move to parent, home, and previous directories.
4. Enter directory names that contain spaces.
5. Recognize common path and permission errors.
