---
index: 14
lang: "en"
title: "find"
meta_title: "find - Command Line"
meta_description: "Learn the Linux find command with examples for searching by name, type, size, modification time, and running actions on matching files."
meta_keywords: "linux find command, find command, find files linux, find by name, find by type, find by size, find mtime, find exec"
---

## Lesson Content

With countless files on a system, it can be challenging to locate a specific one. The `find` command searches directory trees using criteria such as name, type, size, and modification time.

### Using the find Command

The basic syntax is:

```bash
find [PATH] [EXPRESSION]
```

You specify the directory to search in and the criteria for what you are looking for.

For example, to search for a file named `puppies.jpg` within the `/home` directory and all its subdirectories, you would use:

```bash
$ find /home -name puppies.jpg
```

Searches are recursive by default, so `find /home` looks inside `/home` and its subdirectories.

### Searching by Name and Type

One of the most common uses of `find` is searching by filename. The `-name` option matches names exactly or by shell-style patterns.

```bash
$ find . -name "*.txt"
```

You can also specify the type of item you are searching for. The `-type` option is used for this purpose. For instance, if you want to find a directory instead of a file, you can use `d`.

```bash
$ find /home -type d -name MyFolder
```

In this command, we set the type to `d` for directory and are searching for an item named `MyFolder`. To search specifically for regular files, you would use `-type f`.

### Searching by Size and Time

You can search by file size:

```bash
$ find . -type f -size +10M
$ find . -type f -size -1k
```

The first command finds files larger than 10 megabytes. The second finds files smaller than 1 kilobyte.

You can also search by modification time:

```bash
$ find . -type f -mtime -7
$ find . -type f -mtime +30
```

`-mtime -7` means modified within the last 7 days. `-mtime +30` means modified more than 30 days ago.

### Running Actions on Results

By default, `find` prints matching paths. You can add actions such as `-print`, `-delete`, or `-exec`.

Print matches explicitly:

```bash
$ find . -name "*.log" -print
```

Run `ls -l` on each match:

```bash
$ find . -name "*.log" -exec ls -l {} \;
```

The `{}` placeholder is replaced by each matching path. The escaped semicolon marks the end of the command.

Be careful with destructive actions such as `-delete`. First run the same search without `-delete` to confirm the matches.

### Common find Options

- `-name PATTERN`: Match by filename.
- `-iname PATTERN`: Match by filename, ignoring case.
- `-type f`: Match regular files.
- `-type d`: Match directories.
- `-size +10M`: Match files larger than 10 megabytes.
- `-mtime -7`: Match files modified within the last 7 days.
- `-maxdepth N`: Limit how deep `find` searches.

### Common Questions

**Why does find show "Permission denied"?** Your user cannot read some directories. Search a narrower path or use appropriate privileges.

**Why should I quote patterns like "*.txt"?** Quoting prevents the shell from expanding the wildcard before `find` receives it.

**Is find recursive?** Yes. It searches subdirectories by default.

## Exercise

Practice is key to mastering the `find command in linux`. These hands-on labs will help you reinforce your understanding of finding files and directories:

1. **[Linux find Command: File Searching](https://labex.io/labs/linux-linux-find-command-file-searching-219191)** - This lab provides an introduction to the `find` command, a versatile utility for searching and locating files and directories based on various criteria. You'll practice using `find` to locate specific files.
2. **[Discover Critical System Resources](https://labex.io/labs/linux-discover-critical-system-resources-388032)** - Learn essential Linux commands for locating files and executables, including `find`. You'll practice efficiently navigating the file system and discovering critical system resources.

These labs will help you apply the concepts in real scenarios and build confidence with using the `find` command effectively.

## Quiz Question

What option should you specify for the `find` command to search by name? Please answer using only the English option, paying attention to the required format (e.g., -option).

## Quiz Answer

-name
