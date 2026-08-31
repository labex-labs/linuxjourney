---
lesson_id: "list-directories-ls-command"
course_id: "command-line"
lang: "en"
order_index: 4
title: "ls (List Directories)"
description: "Learn how to use ls options to inspect files, hidden entries, details, sizes, and sort order."
meta_title: "ls (List Directories) - Command Line"
meta_description: "Learn the Linux ls command with examples for listing files, hidden files, long format output, human-readable sizes, sorting, and combining options."
meta_keywords: "ls command, linux ls, list files linux, list directories, ls -a, ls -l, ls -lh, ls -r, hidden files"
---

Now that we know how to move around the filesystem, how do we figure out what is available to us? The `ls` command lists files and directories so you can inspect your current location or another path.

## Basic Usage of the ls Command

By default, the `ls` command will list the directories and files in your current directory. However, you can also specify a path to list the contents of a different directory.

```bash
$ ls
$ ls /home/pete
```

You can list a specific file too:

```bash
$ ls /etc/hosts
/etc/hosts
```

:::single-choice{#list-another-directory}
Which command lists the contents of `/home/pete` without changing into it?

::option[`ls /home/pete`]{#ls-target-path .correct explanation="Passing a directory path to `ls` lists that directory's contents. The shell remains in its current working directory."}
::option[`cd /home/pete`]{#cd-target-path explanation="`cd` changes the shell's working directory. It does not perform the requested listing by itself."}
::option[`pwd /home/pete`]{#pwd-target-path explanation="`pwd` reports the current working directory and does not take a destination to list. Use `ls` with the path instead."}
:::

## Viewing Hidden Files

Not all files in a directory are visible by default. In Linux, filenames that start with a dot (`.`) are hidden. You can view them with the `-a` option, which stands for all.

```bash
$ ls -a
.  ..  .bashrc  Documents  Pictures
```

Dotfiles are hidden by default and often store configuration, such as `.bashrc`.

:::single-choice{#show-hidden-files}
Which command includes hidden files in the listing?

::option[`ls -l`]{#long-format explanation="The `-l` option adds detailed columns but does not include hidden names by itself."}
::option[`ls -r`]{#reverse-order explanation="The `-r` option reverses the sort order. It does not change whether hidden files are included."}
::option[`ls -a`]{#all-files .correct explanation="The `-a` option means all, so `ls` includes names that begin with a dot."}
:::

## Getting Detailed Information

Another essential `ls` option is `-l` for long format. It shows file permissions, number of links, owner, group, size, modification time, and name.

```bash
$ ls -l
```

Here is an example of the output:

```plaintext
pete@icebox:~$ ls -l
total 80
drwxr-x--- 7 pete penguingroup   4096 Nov 20 16:37 Desktop
drwxr-x--- 2 pete penguingroup   4096 Oct 19 10:46  Documents
drwxr-x--- 4 pete penguingroup   4096 Nov 20 09:30 Downloads
drwxr-x--- 2 pete penguingroup   4096 Oct  7 13:13   Music
drwxr-x--- 2 pete penguingroup   4096 Sep 21 14:02 Pictures
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Public
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Templates
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Videos
```

For easier file sizes, add `-h` for human-readable output:

```bash
$ ls -lh
```

:::single-choice{#show-readable-file-details}
Which command shows long-format details with human-readable sizes?

::option[`ls -la`]{#long-all explanation="This combines long format with hidden files. It does not request human-readable size units."}
::option[`ls -lh`]{#long-human-readable .correct explanation="`-l` selects long format and `-h` makes sizes easier to read. The flags can be combined in one command."}
::option[`ls -ltr`]{#long-time-reverse explanation="This combines long format, modification-time sorting, and reverse order. It does not include the `-h` size option."}
:::

## Sorting in Reverse Order

Sometimes you may want to change the sort order. The `-r` option lists files and directories in reverse order.

```bash
$ ls -r
```

You can sort by modification time with `-t`, then reverse it with `-r`:

```bash
$ ls -lt
$ ls -ltr
```

:::single-choice{#show-newest-files-last}
Which command sorts by modification time and then places the newest entries last?

::option[`ls -ltr`]{#time-reversed .correct explanation="`-t` sorts by modification time, while `-r` reverses that order. Together they place older entries before newer ones."}
::option[`ls -lt`]{#time-default explanation="This sorts by modification time but keeps the default newest-first direction. It does not place the newest entries last."}
::option[`ls -lr`]{#reverse-name-order explanation="This uses long format and reverses the default name sort. Without `-t`, modification time does not control the order."}
:::

## Combining Command Flags

Commands have flags, also called options, to add more functionality. As we saw with `-a` and `-l`, you can combine them into a single command like `ls -la`. The order of the flags often does not matter, so `ls -al` works the same way.

```bash
$ ls -la
```

Useful combinations include:

```bash
$ ls -lh
$ ls -la
$ ls -ltr
```

## Common ls Options

- `-a`: Show all files, including hidden files.
- `-l`: Use long format.
- `-h`: Show human-readable sizes with `-l`.
- `-r`: Reverse the sort order.
- `-t`: Sort by modification time.
- `-S`: Sort by file size.
- `-d`: List the directory itself instead of its contents.

:::single-choice{#list-directory-entry-itself}
Which command lists the `projects/` directory entry instead of its contents?

::option[`ls -d projects/`]{#directory-entry .correct explanation="The `-d` option tells `ls` to show the directory entry itself rather than opening it for a content listing."}
::option[`ls projects/`]{#directory-contents explanation="Without `-d`, passing a directory path makes `ls` display the entries inside that directory."}
::option[`cd projects/`]{#change-to-directory explanation="`cd` changes the working directory. It does not list the directory entry requested here."}
:::

Some systems display `ls` output in different colors for different file types. This behavior commonly comes from an alias or environment setting, so colors may vary between systems.

To reinforce your understanding of the `ls` command, try this hands-on lab:

- **[Linux ls Command: Content Listing](https://labex.io/labs/linux-linux-ls-command-content-listing-219205)** - Practice using the `ls` command to efficiently list and analyze file and directory contents. You'll learn various options for detailed listings, hidden file display, human-readable sizes, and sorting techniques to enhance your command-line skills.

This lab will help you apply the concepts in a real scenario and build confidence with directory listing in Linux.

## Summary

You can now use `ls` to inspect directory contents and control how entries are displayed.

1. List the current directory or another path.
2. Include hidden files in a listing.
3. Show detailed information with readable sizes.
4. Sort entries by modification time in reverse order.
5. List a directory entry without listing its contents.
