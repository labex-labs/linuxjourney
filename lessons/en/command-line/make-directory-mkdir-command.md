---
lesson_id: "make-directory-mkdir-command"
course_id: "command-line"
lang: "en"
order_index: 12
title: "mkdir (Make Directory)"
description: "Learn how to create single, multiple, and nested directories with mkdir options."
meta_title: "mkdir (Make Directory) - Command Line"
meta_description: "Learn the Linux mkdir command with examples for creating one directory, multiple directories, nested parent directories, and setting permissions."
meta_keywords: "mkdir command, linux mkdir, create directory linux, make directory linux, mkdir -p, mkdir -m, create folder linux"
---

The `mkdir` command, short for make directory, creates directories for organizing files and other directories.

The basic syntax is:

```bash
mkdir [OPTIONS] DIRECTORY...
```

## Creating One Directory

Pass a pathname to create one directory. This example creates `documents` in the current working directory:

```bash
$ mkdir documents
```

If an entry named `documents` already exists, `mkdir` reports an error rather than replacing it. Use `ls -ld documents` to inspect the existing entry.

:::single-choice{#create-one-directory}
Which command creates a directory named `documents` in the current working directory?

::option[`mkdir documents`]{#mkdir-documents .correct explanation="`mkdir` creates the requested directory at the relative pathname `documents`."}
::option[`touch documents`]{#touch-documents explanation="`touch` creates an empty regular file when the pathname is missing. It does not create a directory."}
::option[`cd documents`]{#cd-documents explanation="`cd` attempts to enter an existing directory. It does not create a missing one."}
:::

## Creating Multiple Directories

List several pathnames to create several directories in one command:

```bash
$ mkdir books paintings
```

:::single-choice{#create-separate-directories}
Which command creates two sibling directories named `books` and `paintings`?

::option[`mkdir books/paintings`]{#nested-paintings explanation="This pathname describes `paintings` inside `books`, not two sibling directories. It also fails if `books` is missing."}
::option[`mkdir "books paintings"`]{#spaced-directory explanation="Quoting combines the words into one pathname, so this requests a single directory whose name contains a space."}
::option[`mkdir books paintings`]{#two-directories .correct explanation="Separate operands tell `mkdir` to create `books` and `paintings` as two directories."}
:::

## Creating Missing Parent Directories

Without an option, `mkdir books/hemingway/favorites` fails if an intermediate directory is missing. Add `-p` to create missing parent directories along the path:

```bash
$ mkdir -p books/hemingway/favorites
```

This creates the missing parts of the path. It also does not report an error merely because the final directory already exists, although other errors such as insufficient permissions can still occur.

:::single-choice{#create-nested-path}
None of `projects/app/src` exists yet. Which command creates the complete directory path?

::option[`mkdir -p projects/app/src`]{#mkdir-parents .correct explanation="The `-p` option creates each missing parent directory before creating the final directory."}
::option[`mkdir projects/app/src`]{#mkdir-no-parents explanation="Without `-p`, `mkdir` cannot create `src` when the intermediate directories do not exist."}
::option[`mkdir -m projects/app/src`]{#mkdir-mode-missing explanation="The `-m` option requires a mode argument and does not request creation of missing parents."}
:::

## Setting the Initial Mode

Use `-m MODE` to specify permissions for a newly created directory:

```bash
$ mkdir -m 755 public
```

You will study permission modes later. In this example, mode `755` gives the owner read, write, and search permissions, while the group and others receive read and search permissions.

Add `-v` to print a message for each directory as it is created:

```bash
$ mkdir -pv projects/app/src
mkdir: created directory 'projects'
mkdir: created directory 'projects/app'
mkdir: created directory 'projects/app/src'
```

:::single-choice{#set-directory-mode}
Which command creates `public` with permission mode `755`?

::option[`mkdir -p 755 public`]{#parents-755 explanation="The `-p` option treats the remaining words as directory pathnames, so this would not set permission mode `755`."}
::option[`mkdir -v 755 public`]{#verbose-755 explanation="The `-v` option prints creation messages. It does not interpret `755` as a permission mode."}
::option[`mkdir -m 755 public`]{#mode-public .correct explanation="The `-m` option takes the requested mode, and `public` is the directory pathname to create."}
:::

To practice creating and organizing directories, try these hands-on labs:

1. **[Linux mkdir Command: Directory Creating](https://labex.io/labs/linux-linux-mkdir-command-directory-creating-209739)** - Learn how to use the `mkdir` command in Linux to create directories, set permissions, and organize your file system. This lab covers basic and advanced usage, including creating nested directories.
2. **[Setting Up a New Project Structure](https://labex.io/labs/linux-setting-up-a-new-project-structure-387859)** - Practice your Linux directory management skills by creating a specific project structure and navigating through it using essential commands like `mkdir` and `cd`.

## Summary

You can now create directory structures with deliberate names, parents, and modes.

1. Create one or more directories in a single command.
2. Recognize an error caused by an existing pathname.
3. Build missing parent directories with `-p`.
4. Set a new directory's mode with `-m`.
