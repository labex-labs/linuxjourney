---
lesson_id: "move-mv-command"
course_id: "command-line"
lang: "en"
order_index: 11
title: "mv (Move)"
description: "Learn how to rename and move files or directories while avoiding unintended overwrites."
meta_title: "mv (Move) - Command Line"
meta_description: "Learn the Linux mv command with examples for moving files, renaming files and directories, moving multiple files, and avoiding overwrites."
meta_keywords: "linux mv command, mv command, move files linux, rename file linux, rename directory linux, mv -i, mv -n, mv -t"
---

The `mv` command renames a file or directory, or moves it to another location. Unlike `cp`, it does not leave the original pathname in place after a successful move.

The basic syntax is:

```bash
mv [OPTIONS] SOURCE DESTINATION
```

## Renaming Files and Directories

To rename an item, put its current pathname first and its new pathname second.

To rename a file:

```bash
$ mv oldfile newfile
```

The same operand order renames a directory:

```bash
$ mv old_directory_name new_directory_name
```

:::single-choice{#rename-file-with-mv} Which command renames `cat` to `dog` in the current directory?

::option[`mv cat dog`]{#rename-cat .correct explanation="`mv` treats `cat` as the source pathname and `dog` as its new destination pathname."}
::option[`mv dog cat`]{#rename-dog explanation="The operand order is reversed. This would try to rename an existing `dog` to `cat`."}
::option[`cp cat dog`]{#copy-cat explanation="`cp` would create a copy named `dog` while keeping `cat`. It would not perform the requested rename."}
:::

## Moving Items to a Directory

When the final operand is an existing directory, `mv` places the source inside it:

```bash
$ mv file2 /home/pete/Documents
```

To move several sources, list them first and put the target directory last:

```bash
$ mv file_1 file_2 somedirectory/
```

GNU `mv` also provides `-t` for placing the target directory before the sources:

```bash
$ mv -t somedirectory/ file_1 file_2
```

Unlike `cp`, `mv` does not need a recursive option for a directory.

:::single-choice{#move-multiple-files} Which command moves both `file_1` and `file_2` into the existing `archive/` directory?

::option[`mv archive/ file_1 file_2`]{#target-first-without-option explanation="Without GNU `-t`, a multi-source move expects the target directory last. This operand order is not the standard multi-source form."}
::option[`mv -r file_1 file_2 archive/`]{#recursive-move explanation="`mv` does not use `-r` to move files or directories. The normal multi-source form already handles the requested move."}
::option[`mv file_1 file_2 archive/`]{#target-last .correct explanation="With multiple sources, the existing target directory is the final operand and receives both files."}
:::

## Controlling Existing Destinations

By default, `mv` can replace an existing destination. Inspect source and destination pathnames before running a move, then choose an overwrite policy when necessary:

- `-i`: Ask for confirmation before replacing an existing destination.

  ```bash
  $ mv -i source_file destination_directory
  ```

- `-n`: Do not overwrite an existing destination.

  ```bash
  $ mv -n source_file destination_directory
  ```

- `-b`: On GNU/Linux, make a backup of a destination that would otherwise be replaced. The default backup suffix is usually `~`.

  ```bash
  $ mv -b file1 directory_with_file1
  ```

- `-v`: Print each move as it happens.

```bash
$ mv -v file1 file2 somedirectory/
```

:::single-choice{#move-without-overwriting} Which command moves `draft.txt` into `finished/` only when it will not overwrite an existing destination?

::option[`mv -i draft.txt finished/`]{#interactive-draft explanation="The `-i` option asks what to do when a destination exists. An overwrite can still occur if the user confirms it."}
::option[`mv -b draft.txt finished/`]{#backup-draft explanation="The `-b` option permits replacement while keeping a backup of the previous destination. It does not prevent overwriting."}
::option[`mv -n draft.txt finished/`]{#no-clobber-draft .correct explanation="The `-n` option skips a move that would overwrite an existing destination."}
:::

## Moving Directories and Wildcard Matches

A directory can be moved without `-r`:

```bash
$ mv project /home/pete/Documents/
```

Shell wildcards can select multiple sources:

```bash
$ ls *.txt
$ mv *.txt notes/
```

Previewing the matches with `ls` helps you catch an overly broad pattern before changing several pathnames.

:::single-choice{#move-directory-without-recursion} Which command moves the `project/` directory into `/srv/archive/`?

::option[`mv -r project/ /srv/archive/`]{#recursive-project explanation="`mv` does not need or support `-r` for this purpose. Directories are handled by the ordinary move operation."}
::option[`mv project/ /srv/archive/`]{#move-project .correct explanation="The ordinary `mv` syntax moves a directory to an existing target directory without a recursive flag."}
::option[`cp project/ /srv/archive/`]{#copy-project explanation="A plain `cp` does not move the directory and would require a recursive option to copy it. The original would also remain."}
:::

:::single-choice{#preview-text-file-move} You plan to run `mv *.txt notes/`. Which command previews the pathnames selected by the same wildcard?

::option[`ls '*.txt'`]{#literal-text-pattern explanation="Quotes keep the shell from expanding `*`, so this looks for a literal name containing an asterisk rather than previewing the move set."}
::option[`ls *.txt`]{#list-text-matches .correct explanation="The shell expands `*.txt` for `ls` just as it would for `mv`, allowing you to inspect the selected non-hidden names first."}
::option[`mv -v *.txt notes/`]{#verbose-text-move explanation="Verbose mode reports moves while they happen. It performs the operation instead of providing a read-only preview."}
:::

To practice moving and renaming items, try these hands-on labs:

1. **[Linux mv Command: File Moving and Renaming](https://labex.io/labs/linux-linux-mv-command-file-moving-and-renaming-209743)** - Practice using the `mv` command to move and rename files and directories, including understanding its various options and behaviors.
2. **[Organizing Files and Directories](https://labex.io/labs/linux-organizing-files-and-directories-387877)** - Apply your knowledge of `mv` (along with `cp` and `rm`) in a practical challenge to organize a project structure, move files, and clean up directories.

## Summary

You can now rename and move files or directories while protecting existing destinations.

1. Put the source before its new pathname.
2. Place a target directory after multiple sources.
3. Ask, skip, or back up before replacing a destination.
4. Move directories without a recursive option.
5. Preview wildcard matches before a bulk move.
