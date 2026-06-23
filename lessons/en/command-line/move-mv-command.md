---
index: 11
lang: "en"
title: "mv (Move)"
meta_title: "mv (Move) - Command Line"
meta_description: "Learn the Linux mv command with examples for moving files, renaming files and directories, moving multiple files, and avoiding overwrites."
meta_keywords: "linux mv command, mv command, move files linux, rename file linux, rename directory linux, mv -i, mv -n, mv -t"
---

## Lesson Content

The `mv` command, short for "move," is a fundamental utility in any Linux environment. It serves two primary purposes: renaming files or directories and moving them to a different location.

The basic syntax is:

```bash
mv [OPTIONS] SOURCE DESTINATION
```

Unlike `cp`, which creates a copy, `mv` changes where the original item lives or what it is called.

### Renaming Files and Directories

One of the most common uses of `mv` is renaming. The syntax is straightforward: specify the old name and the new name.

To rename a file:

```bash
$ mv oldfile newfile
```

This same logic applies to renaming directories:

```bash
$ mv old_directory_name new_directory_name
```

### Moving Files and Directories

The other core function of the `mv` command is to move items from one location to another.

To move a single file into a different directory:

```bash
$ mv file2 /home/pete/Documents
```

You can also move multiple files at once. Simply list all the source files followed by the target directory:

```bash
$ mv file_1 file_2 somedirectory/
```

On GNU/Linux systems, a useful option for this is `-t`, which allows you to specify the target directory first. This can be clearer when moving many files.

```bash
$ mv -t somedirectory/ file_1 file_2
```

Unlike the `cp` command, you do not need a recursive option to move a directory. `mv` handles directories by default.

### Important Options for the mv Command

By default, if you move a file to a destination where a file with the same name already exists, `mv` will overwrite it without warning. To prevent accidental data loss, you can use the following options:

- **-i (interactive)**: This is a crucial safety feature. It will prompt you for confirmation before overwriting any existing file.

  ```bash
  $ mv -i source_file destination_directory
  ```

- **-b (backup)**: If you intend to overwrite a file but want to keep the old version, this option creates a backup of the destination file. The backup is typically renamed with a tilde (`~`) suffix.

  ```bash
  $ mv -b file1 directory_with_file1
  ```

- **-v (verbose)**: This option makes the `mv` command print out what it is doing, showing each file being moved or renamed.

  ```bash
  $ mv -v file1 file2 somedirectory/
  ```

Another useful option is `-n`, which means no clobber. It prevents overwriting an existing destination file.

```bash
$ mv -n source_file destination_directory
```

### Common mv Examples

Rename a file:

```bash
$ mv draft.txt final.txt
```

Move a directory:

```bash
$ mv project /home/pete/Documents/
```

Move all text files into a folder:

```bash
$ mv *.txt notes/
```

Preview wildcard matches with `ls` before moving many files.

### Common Questions

**Does mv copy files?** No. `mv` moves or renames the original item.

**Can mv overwrite files?** Yes. Use `mv -i` to ask first or `mv -n` to avoid overwriting.

**Do I need mv -r for directories?** No. `mv` moves directories without `-r`.

## Exercise

Practice makes perfect! Hands-on experience is crucial for mastering Linux commands like `mv`. These labs will help you solidify your understanding of moving and renaming files and directories in a real environment:

1. **[Linux mv Command: File Moving and Renaming](https://labex.io/labs/linux-linux-mv-command-file-moving-and-renaming-209743)** - Practice using the `mv` command to move and rename files and directories, including understanding its various options and behaviors.
2. **[Organizing Files and Directories](https://labex.io/labs/linux-organizing-files-and-directories-387877)** - Apply your knowledge of `mv` (along with `cp` and `rm`) in a practical challenge to organize a project structure, move files, and clean up directories.

These labs will help you apply the concepts in real scenarios and build confidence with file and directory management using the `mv` command.

## Quiz Question

Using the `mv` command, how would you rename a file named `cat` to `dog`? Please provide the full command. Note: The answer is case-sensitive and should be entered in lowercase English.

## Quiz Answer

mv cat dog
