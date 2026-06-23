---
index: 13
lang: "en"
title: "rm (Remove)"
meta_title: "rm (Remove) - Command Line"
meta_description: "Learn the Linux rm command with safe examples for deleting files, removing directories, using rm -r, rm -i, and avoiding rm -rf mistakes."
meta_keywords: "linux rm command, rm command, rm -r, rm -i, rm -f, rm -rf, delete files linux, remove directory linux, rmdir"
---

## Lesson Content

In Linux, it's common to accumulate files that are no longer needed. To delete them, you use the `rm` (remove) command, a fundamental utility for managing your filesystem. The basic syntax is:

```bash
rm [OPTIONS] FILE...
```

The `rm` command removes directory entries from the filesystem. In normal terms, it deletes files. Unlike many desktop environments, command-line deletion usually does not move files to a trash folder, so you should check your command before pressing Enter.

### Remove a Single File

To remove one file, pass the filename to `rm`.

```bash
$ rm file1
```

You can remove several files at once by listing them one after another.

```bash
$ rm notes.txt old-report.txt draft.md
```

This is useful for quick cleanup, but it also means a typo can delete more than you intended.

### Remove Files with Wildcards

Shell wildcards let you match multiple files. For example, this removes every `.tmp` file in the current directory:

```bash
$ rm *.tmp
```

Before using `rm` with a wildcard, it is safer to preview the match with `ls`.

```bash
$ ls *.tmp
cache.tmp  test.tmp
$ rm *.tmp
```

Remember that the shell expands `*.tmp` before `rm` runs. If the pattern matches more files than expected, `rm` will still receive all of them.

### Interactive Deletion with -i

For a safer approach, use the `-i` option. It prompts you before deleting each file.

```bash
$ rm -i important.txt
rm: remove regular file 'important.txt'? y
```

Use `rm -i` when deleting files from a shared directory, cleaning up many files, or learning the command for the first time.

### Forceful Deletion with -f

The `-f` option means "force." It ignores nonexistent files and does not prompt for confirmation.

```bash
$ rm -f old-cache.txt
```

This is useful in scripts where cleanup should continue even if a file is already gone.

```bash
$ rm -f build.log
```

Be careful: `-f` also suppresses some safety prompts, so it can hide mistakes.

### Removing Directories with -r

By default, `rm` cannot delete a directory.

```bash
$ rm projects
rm: cannot remove 'projects': Is a directory
```

To remove a directory and everything inside it, use `-r` or `-R` for recursive removal.

```bash
$ rm -r old-project
```

Recursive removal walks through the directory tree and removes files, subdirectories, and their contents.

### The Dangers of rm -rf

The command `rm -rf` combines recursive deletion with forceful deletion.

```bash
$ rm -rf old-project
```

This command can be appropriate for removing generated folders such as build outputs, but it is dangerous because it removes a whole tree without asking questions. Always check:

- Are you in the directory you think you are in? Use `pwd`.
- Did your wildcard expand correctly? Preview with `ls`.
- Is the path absolute or relative? `/tmp/cache` and `tmp/cache` are very different.
- Is there an accidental space? `rm -rf old-project` and `rm -rf old project` target different paths.

### Using rmdir for Empty Directories

As a safer alternative, remove an empty directory with `rmdir`.

```bash
$ rmdir empty-directory
```

The `rmdir` command will only succeed if the directory is completely empty, making it a safer choice than `rm -r` for cleanup tasks.

### Common rm Options

Here are the options you will see most often:

- `-i`: Prompt before every removal.
- `-I`: Prompt once before removing more than three files or removing recursively.
- `-f`: Force removal and ignore nonexistent files.
- `-r` or `-R`: Remove directories and their contents recursively.
- `-v`: Show what was removed.

For example, you can combine options:

```bash
$ rm -rv old-project
removed 'old-project/notes.txt'
removed directory 'old-project'
```

### Common Questions

**Can I undo rm?** Usually, no. Once a file is removed with `rm`, there is no built-in undo command. Backups, version control, and filesystem recovery tools are the real safety net.

**Why does rm say "Permission denied"?** You do not have permission to remove that file or to modify the directory containing it. Check ownership and permissions with `ls -l`.

**Why does rm say "No such file or directory"?** The file does not exist at that path, or you are in a different directory than you expected. Use `pwd` and `ls` to confirm.

**Should I use sudo with rm?** Only when you fully understand the path you are deleting. `sudo rm -r` can remove system files that your normal user account is not allowed to touch.

## Exercise

Practice is key. Here are some hands-on exercises to solidify your understanding of file and directory removal in Linux:

1. **[Linux rm Command: File Removing](https://labex.io/labs/linux-linux-rm-command-file-removing-209741)** - Learn how to use the `rm` command for removing files and directories, including various options like `-r` and `-i`, and practice safe and effective file deletion.
2. **[Organizing Files and Directories](https://labex.io/labs/linux-organizing-files-and-directories-387877)** - Practice essential Linux file management skills, including using the `rm` command to clean up unnecessary directories, in a practical challenge.

These labs will help you apply these concepts in real-world scenarios and build confidence with the `linux rm command`.

## Quiz Question

How do you remove a file named `myfile`? Your answer must be in English and use the exact, case-sensitive command.

## Quiz Answer

rm myfile
