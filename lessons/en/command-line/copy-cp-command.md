---
lesson_id: "copy-cp-command"
course_id: "command-line"
lang: "en"
order_index: 10
title: "cp (Copy)"
description: "Learn how to copy files and directory trees while controlling overwrites and preserved attributes."
meta_title: "cp (Copy) - Command Line"
meta_description: "Learn the Linux cp command with examples for copying files, directories, multiple files, wildcards, backups, and options like cp -r, cp -i, and cp -p."
meta_keywords: "linux cp command, cp command, copy files linux, cp -r, cp -i, cp -p, cp -a, cp -u, recursive copy, linux wildcards"
---

The `cp` command copies files and directories while leaving the source in place. Its basic syntax is:

```bash
cp [OPTIONS] SOURCE DESTINATION
```

You can copy one file to another path, copy several files into a directory, or recursively copy a directory tree.

## Copying One File

Place the source first and the destination second:

```bash
$ cp mycoolfile /home/pete/Documents/cooldocs
```

If `/home/pete/Documents/cooldocs` is an existing directory, the copy is created inside it as `mycoolfile`. You can instead provide a new destination filename:

```bash
$ cp mycoolfile /home/pete/Documents/mycoolfile_backup
```

In the second example, the copied data receives the name `mycoolfile_backup`.

:::single-choice{#copy-file-under-new-name} Which command copies `draft.txt` to a file named `final.txt` while keeping `draft.txt`?

::option[`mv draft.txt final.txt`]{#move-draft explanation="`mv` renames or moves the original pathname. It does not leave the requested source copy in place."}
::option[`cp final.txt draft.txt`]{#copy-reversed explanation="Source and destination are reversed here. This would copy from `final.txt` to `draft.txt`."}
::option[`cp draft.txt final.txt`]{#copy-draft .correct explanation="`cp` reads `draft.txt` and creates or replaces `final.txt`, while the source remains available."}
:::

## Copying Multiple Files into a Directory

List every source first and put the destination directory last:

```bash
$ cp report.txt notes.txt summary.txt /home/pete/Documents/
```

The final argument must be a directory when you provide more than one source.

:::single-choice{#copy-multiple-files} Which command copies `a.txt` and `b.txt` into the existing `archive/` directory?

::option[`cp archive/ a.txt b.txt`]{#destination-first explanation="For this form of `cp`, the destination directory belongs at the end. Placing it first changes how the operands are interpreted."}
::option[`cp a.txt b.txt archive/`]{#destination-last .correct explanation="With multiple sources, `cp` treats the final existing directory as the destination for every preceding file."}
::option[`cp a.txt archive/ b.txt`]{#destination-middle explanation="All source operands must come before the destination. The existing directory should be the final operand."}
:::

## Selecting Files with Wildcards

The shell can expand wildcard patterns into several source pathnames:

- `*`: Matches any sequence of characters.
- `?`: Matches any single character.
- `[]`: Matches any one of the characters enclosed in the brackets.

For example, copy names ending in `.jpg` from the current directory to `Pictures`:

```bash
$ cp *.jpg /home/pete/Pictures
```

Preview the matches before a bulk copy, especially when the destination contains important data:

```bash
$ ls *.jpg
beach.jpg  lunch.jpg  profile.jpg
$ cp *.jpg /home/pete/Pictures
```

:::single-choice{#preview-copy-pattern} Before copying `*.jpg`, which command shows the non-hidden names that the pattern currently matches?

::option[`cp *.jpg`]{#copy-no-destination explanation="This attempts a copy without a clear destination when several names match. It is not a preview operation."}
::option[`ls *.jpg`]{#list-jpg-matches .correct explanation="The shell expands the same pattern for `ls`, letting you inspect the matching names before copying them."}
::option[`file '*.jpg'`]{#quoted-jpg-pattern explanation="The quotes prevent wildcard expansion, so `file` receives the literal characters `*.jpg`. This does not preview the normal matches."}
:::

## Copying Directory Trees

Copying a directory and everything below it requires recursive operation. Use `-r` or `-R`:

```bash
$ cp -r Pumpkin/ /home/pete/Documents
```

This copies the `Pumpkin` directory and its descendants into `Documents`.

Uppercase `-R` also requests recursive copying:

```bash
$ cp -R website /home/pete/backups/
```

Archive mode, `-a`, is useful for backup-style copies. It copies recursively while preserving links and many file attributes:

```bash
$ cp -a project/ project-backup/
```

:::single-choice{#archive-directory-tree} You want a recursive backup-style copy of `project/` that preserves links and many attributes. Which command fits that goal?

::option[`cp -p project/ project-backup/`]{#preserve-directory-only explanation="`-p` preserves selected attributes, but it does not by itself make a directory copy recursive."}
::option[`cp -u project/ project-backup/`]{#update-directory-only explanation="`-u` controls when files are copied based on destination state. It does not by itself enable recursive directory copying."}
::option[`cp -a project/ project-backup/`]{#archive-project .correct explanation="Archive mode includes recursive copying and preserves links and a broad set of attributes for a backup-style result."}
:::

## Controlling Overwrites

By default, `cp` can replace an existing destination file. Use `-i` to request confirmation before an overwrite:

```bash
$ cp -i mycoolfile /home/pete/Pictures
cp: overwrite '/home/pete/Pictures/mycoolfile'? n
```

Use `-n` when an existing destination should not be overwritten:

```bash
$ cp -n mycoolfile /home/pete/Pictures
```

The `-f` option tells GNU `cp` to try removing an existing destination if it cannot open that file for writing, then retry the copy. It is not a substitute for checking targets carefully. Shell aliases can also add options such as `-i`, so inspect an unexpected prompt rather than assuming a particular configuration.

:::single-choice{#skip-existing-destination} Which command copies `report.txt` into `backup/` but skips an existing destination of the same name?

::option[`cp -n report.txt backup/`]{#no-clobber-report .correct explanation="The `-n` option prevents `cp` from overwriting an existing destination file."}
::option[`cp -i report.txt backup/`]{#interactive-report explanation="`-i` asks before an overwrite, so the result depends on the response. It does not automatically skip every existing destination."}
::option[`cp -f report.txt backup/`]{#force-report explanation="`-f` can help replace a destination that cannot initially be opened. It does not provide no-clobber behavior."}
:::

## Preserving or Refreshing Files

Use `-p` to preserve the source file's mode, ownership when permitted, and timestamps:

```bash
$ cp -p mycoolfile /home/pete/backups/
```

Use `-u` to copy a source only when the destination is missing or the source is newer:

```bash
$ cp -u *.txt /home/pete/Documents/
```

Other common options include:

- `-f`: Force overwriting by removing the destination first if needed.
- `-v`: Show each file as it is copied.

To practice copying files and directory trees, try these hands-on labs:

1. **[Linux cp Command: File Copying](https://labex.io/labs/linux-linux-cp-command-file-copying-209744)** - Practice basic usage, advanced options like recursive copying, preserving attributes, and using wildcards to efficiently copy files and directories.
2. **[Organizing Files and Directories](https://labex.io/labs/linux-organizing-files-and-directories-387877)** - Practice essential Linux file management skills by using `cp`, `mv`, and `rm` commands to organize a project structure, move files, and clean up unnecessary directories.

## Summary

You can now copy files and directory trees while controlling how destinations are handled.

1. Place source operands before the destination.
2. Preview wildcard matches before a bulk copy.
3. Copy directory trees recursively or in archive mode.
4. Confirm, skip, or deliberately replace existing destinations.
5. Preserve attributes or copy only newer sources when needed.
