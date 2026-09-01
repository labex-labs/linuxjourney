---
lesson_id: "remove-rm-command"
course_id: "command-line"
lang: "en"
order_index: 13
title: "rm (Remove)"
description: "Learn how to remove files and directories while checking targets and choosing safer rm options."
meta_title: "rm (Remove) - Command Line"
meta_description: "Learn the Linux rm command with safe examples for deleting files, removing directories, using rm -r, rm -i, and avoiding rm -rf mistakes."
meta_keywords: "linux rm command, rm command, rm -r, rm -i, rm -f, rm -rf, delete files linux, remove directory linux, rmdir"
---

The `rm` command removes filesystem entries. Command-line removal normally does not send items to a desktop trash folder, and `rm` has no built-in undo, so confirm every target before you run it.

The basic syntax is:

```bash
rm [OPTIONS] FILE...
```

## Removing Files

Pass one or more file pathnames to `rm`:

```bash
$ rm file1
```

```bash
$ rm notes.txt old-report.txt draft.md
```

Check spelling and location before pressing Enter. A backup or version-control copy is a more dependable recovery plan than filesystem-recovery tools after deletion.

:::single-choice{#remove-one-file} After confirming the target, which command removes the file `old-report.txt`?

::option[`rm old-report.txt`]{#rm-report .correct explanation="`rm` removes the named file entry. The operation normally does not place the file in a trash folder."}
::option[`rmdir old-report.txt`]{#rmdir-report explanation="`rmdir` operates on empty directories, not regular files. It is not the command for this target."}
::option[`mv old-report.txt`]{#mv-report explanation="`mv` needs a destination and changes a pathname rather than deleting it. This incomplete command does not perform the requested removal."}
:::

## Previewing Wildcard Targets

The shell can expand a wildcard into several operands. For example, `*.tmp` selects matching non-hidden names in the current directory:

```bash
$ rm *.tmp
```

Preview the same unquoted pattern with `ls` before removing anything:

```bash
$ ls *.tmp
cache.tmp  test.tmp
$ rm *.tmp
```

The shell expands the pattern before `rm` starts. If the preview includes an unexpected file, correct the pattern instead of proceeding.

:::single-choice{#preview-removal-pattern} You plan to remove `*.tmp`. Which command first shows the non-hidden pathnames selected by that pattern without deleting them?

::option[`rm -v *.tmp`]{#verbose-remove explanation="Verbose mode reports removals as they happen. It still deletes the matched files and is not a read-only preview."}
::option[`ls '*.tmp'`]{#quoted-pattern explanation="Quotes prevent wildcard expansion, so this looks for a literal name containing `*` rather than previewing the intended targets."}
::option[`ls *.tmp`]{#list-temp-matches .correct explanation="The shell expands `*.tmp` for `ls`, allowing you to inspect the same set of non-hidden matches before removal."}
:::

## Requesting Confirmation

The `-i` option asks before each removal:

```bash
$ rm -i important.txt
rm: remove regular file 'important.txt'? y
```

The `-I` option is a less intrusive safeguard in GNU `rm`: it prompts once when a command would remove more than three files or operate recursively.

:::single-choice{#confirm-each-removal} Which command asks for confirmation before removing each named file?

::option[`rm -i important.txt`]{#interactive-important .correct explanation="The `-i` option prompts before each removal, giving you a chance to reject the operation."}
::option[`rm -f important.txt`]{#force-important explanation="The `-f` option suppresses prompts and ignores a missing operand. It removes rather than adds confirmation."}
::option[`rm -v important.txt`]{#verbose-important explanation="The `-v` option reports what was removed, but it does not ask for approval first."}
:::

## Ignoring Missing Files with -f

The `-f` option ignores missing operands and suppresses prompts:

```bash
$ rm -f old-cache.txt
```

This can make scripted cleanup idempotent when a generated file may already be absent. Because it removes confirmation, do not add `-f` merely to silence an error you have not understood.

## Removing Directories

Plain `rm` does not remove a directory:

```bash
$ rm projects
rm: cannot remove 'projects': Is a directory
```

Use `-r` or `-R` only when you intend to remove a directory tree and all of its contents:

```bash
$ rm -r old-project
```

For an empty directory, `rmdir` is a narrower alternative:

```bash
$ rmdir empty-directory
```

`rmdir` fails when the directory is not empty, which protects its contents from recursive deletion.

:::single-choice{#remove-empty-directory-only} Which command removes `old-cache/` only if that directory is empty?

::option[`rm -r old-cache/`]{#recursive-cache explanation="Recursive `rm` removes the directory and its contents. It does not enforce the empty-directory condition."}
::option[`rmdir old-cache/`]{#rmdir-cache .correct explanation="`rmdir` succeeds only for an empty directory, so it does not recursively delete contained files."}
::option[`rm -f old-cache/`]{#force-cache explanation="The `-f` option does not make plain `rm` remove a directory. It also suppresses safeguards rather than checking emptiness."}
:::

## Checking a Recursive Removal

Recursive removal can erase a complete tree. Combining `-r` with `-f` also removes prompts, so `rm -rf` deserves especially careful target validation. Before any recursive removal, check:

- Are you in the directory you think you are in? Use `pwd`.
- Does `ls -ld -- TARGET` show the intended top-level path?
- If a wildcard is involved, did a read-only preview match exactly what you expect?
- Is the path absolute or relative? `/tmp/cache` and `tmp/cache` are very different.
- Is there an accidental space? `rm -rf old-project` and `rm -rf old project` target different paths.

Use `--` before a target that could begin with a hyphen so it is not interpreted as an option:

```bash
$ rm -- -old-name
```

Do not reach for `sudo` simply because `rm` reports a permissions error. First verify the target and determine why your account cannot modify its containing directory. Elevated recursive removal can damage the operating system or other users' data.

Use `-v` when you want `rm` to report each successful removal:

```bash
$ rm -rv old-project
removed 'old-project/notes.txt'
removed directory 'old-project'
```

:::single-choice{#remove-nonempty-tree} After verifying the complete target, which command removes `old-project/` and everything below it while still allowing normal prompts?

::option[`rm old-project/`]{#plain-rm-project explanation="Plain `rm` does not descend into a directory. It cannot remove a nonempty tree."}
::option[`rm -r old-project/`]{#recursive-old-project .correct explanation="The `-r` option recursively removes the directory tree. Unlike `-rf`, this form does not add `-f` to suppress prompts."}
::option[`rmdir old-project/`]{#rmdir-project explanation="`rmdir` requires an empty directory. It fails when the project still contains entries."}
:::

To practice removal in a controlled environment, try these hands-on labs:

1. **[Linux rm Command: File Removing](https://labex.io/labs/linux-linux-rm-command-file-removing-209741)** - Learn how to use the `rm` command for removing files and directories, including various options like `-r` and `-i`, and practice safe and effective file deletion.
2. **[Organizing Files and Directories](https://labex.io/labs/linux-organizing-files-and-directories-387877)** - Practice essential Linux file management skills, including using the `rm` command to clean up unnecessary directories, in a practical challenge.

## Summary

You can now remove filesystem entries while treating every target as irreversible.

1. Confirm file pathnames before removal.
2. Preview wildcard expansions with a read-only command.
3. Ask for confirmation with `-i` or `-I`.
4. Prefer `rmdir` when a directory must be empty.
5. Validate an entire target before using recursive removal.
