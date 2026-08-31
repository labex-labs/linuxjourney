---
lesson_id: "symlinks"
course_id: "filesystem"
lang: "en"
order_index: 12
title: "symlinks"
description: "Learn how symbolic and hard links differ in pathname resolution, inode identity, and filesystem scope."
meta_title: "symlinks - The Filesystem"
meta_description: "Explore Linux symlinks (symbolic links) and hard links. Learn how to create them with the ln command, check the link count in linux with ls, and understand the difference when you ls symlink and hard link outputs."
meta_keywords: "Linux symlinks, hard links, ln command, symbolic links, ls symlink, link count in linux, ls symlinks, ls links, Linux file system, Linux tutorial"
---

A directory entry gives an inode a name. A hard link creates another directory entry for the same inode, while a symbolic link creates a different inode whose content is a pathname to resolve. This difference controls identity, lifetime, and cross-filesystem behavior.

## Creating and Inspecting a Symbolic Link

Create a symlink with `ln -s TARGET LINK_NAME`:

```bash
$ printf '%s\n' 'example' > myfile
$ ln -s -- myfile myfilelink
$ ls -li myfile myfilelink
151   -rw-r--r-- 1 user user 8 ... myfile
93403 lrwxrwxrwx 1 user user 6 ... myfilelink -> myfile
```

The symlink has its own inode and stores the text `myfile`. When a program follows `myfilelink`, pathname resolution continues to the target. Display the stored text without following it with:

```bash
$ readlink myfilelink
```

:::single-choice{#symlinks-create-symbolic}
Which command creates symbolic link `myfilelink` with target text `myfile`?

::option[`ln -s -- myfile myfilelink`]{#symlinks-ln-s .correct explanation="The `-s` option requests a symbolic link, followed by target and new link name."}
::option[`ln -- myfile myfilelink`]{#symlinks-ln-hard explanation="Without `-s`, `ln` requests a hard link to the existing inode."}
::option[`readlink myfile myfilelink`]{#symlinks-readlink-create explanation="Readlink inspects a symlink and does not create one."}
:::

## Relative and Absolute Symlink Targets

An absolute target starts at `/`. A relative target is resolved relative to the directory containing the symlink—not relative to the shell's current directory at the moment someone later opens it.

```bash
$ mkdir -p tree/data tree/current
$ printf '%s\n' 'value' > tree/data/item
$ ln -s ../data/item tree/current/item
```

Moving the entire `tree` hierarchy preserves this relative relationship. Moving only the link or target can break it. A symlink is allowed to contain a nonexistent target and is then called dangling or broken.

:::single-choice{#symlinks-relative-resolution}
From where is a relative symlink target resolved?

::option[The home directory of the user who created it.]{#symlinks-creator-home explanation="Creator identity does not become a permanent resolution base."}
::option[The current directory of whichever shell first lists it.]{#symlinks-listing-shell explanation="Listing context does not rewrite the stored target relationship."}
::option[The directory that contains the symlink.]{#symlinks-containing-directory .correct explanation="Path traversal substitutes the stored relative text at the symlink's location."}
:::

## Creating a Hard Link

Create another name for an existing regular file without `-s`:

```bash
$ ln -- myfile myhardlink
$ ls -li myfile myhardlink
151 -rw-r--r-- 2 user user 8 ... myfile
151 -rw-r--r-- 2 user user 8 ... myhardlink
```

Both names map to the same filesystem and inode number. The link count becomes 2. Neither name is inherently the “original”; changing content through one name changes the shared object, and removing one name leaves the other.

Hard links cannot cross filesystem boundaries because an inode number is meaningful only within its filesystem. Linux also restricts ordinary users from hard-linking directories and can restrict links to files they do not own, preventing cycles and security problems.

:::single-choice{#symlinks-hard-link-inode}
What do two hard links to one regular file share?

::option[Only similar filenames but separate file data.]{#symlinks-separate-data explanation="That would describe independent copies, not hard links."}
::option[A pathname stored inside a separate symlink inode.]{#symlinks-stored-path explanation="Path text is the defining mechanism of a symbolic link."}
::option[The same inode and file content.]{#symlinks-same-inode .correct explanation="Each directory entry names the identical filesystem object."}
:::

## Lifetime and Deletion

Removing a symlink removes that link object, not its target:

```bash
$ rm -- myfilelink
```

Removing a hard-link name decrements the shared inode's link count. The filesystem can reclaim the object only after the count reaches zero and no open file descriptions or other filesystem references keep it alive.

Avoid a trailing slash when removing a symlink to a directory, because trailing-slash path resolution can follow directory semantics depending on the command. Inspect with `ls -ld -- LINK` and remove the link name deliberately.

:::single-choice{#symlinks-remove-symbolic}
What normally happens when you remove a symlink itself?

::option[The symlink inode and name are removed while the target remains.]{#symlinks-remove-link-only .correct explanation="Unlinking the symbolic link does not operate on the object named by its stored target text."}
::option[The target and every hard link to it are erased automatically.]{#symlinks-remove-target explanation="The symlink is a separate filesystem object and does not own its target."}
::option[The target is copied into the symlink before removal.]{#symlinks-copy-target explanation="Removal does not preserve target content inside the link."}
:::

## Following Links Safely

Symlinks can redirect a privileged program outside an expected directory or change between validation and use. Secure programs should avoid check-then-open pathname races and use directory-relative, no-follow, or constrained-resolution interfaces appropriate to their language and operating system.

For routine inspection:

- `ls -ld LINK` shows the link itself.
- `readlink LINK` prints its stored target text.
- `stat LINK` commonly reports link metadata, while `stat -L LINK` follows it in GNU coreutils.
- `find -L` follows links and can encounter cycles; use it only intentionally.

Permissions displayed as `lrwxrwxrwx` are not a general access grant. Access is decided through directory traversal, link-following policy, and target permissions; symlink ownership also matters for some protected-directory rules.

:::single-choice{#symlinks-readlink-output}
What does `readlink LINK` print by default?

::option[The pathname text stored in the symbolic link.]{#symlinks-readlink-target-text .correct explanation="It inspects the link object without reading the target file's contents."}
::option[The complete byte content of the target regular file.]{#symlinks-readlink-file-content explanation="Use a file-reading command after intentional resolution for target content."}
::option[Every hard link anywhere on the filesystem.]{#symlinks-readlink-all-hard explanation="Hard-link discovery requires inode-aware filesystem searches and is unrelated to symlink target text."}
:::

Use [Manage Files and Directories in Linux](https://labex.io/labs/comptia-manage-files-and-directories-in-linux-590835) to practice links on disposable files and compare inode numbers.

## Summary

You can now choose and inspect the correct kind of filesystem link.

1. Use `ln -s TARGET LINK` for a pathname-based symbolic link.
2. Resolve relative targets from the link's containing directory.
3. Use `ln EXISTING LINK` for another same-filesystem inode name.
4. Distinguish unlinking a symlink from unlinking a hard link.
5. Avoid unsafe link following in privileged or recursive operations.
