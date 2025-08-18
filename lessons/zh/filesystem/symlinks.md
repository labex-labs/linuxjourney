---
lang: "zh"
title: "符号链接"
meta_description: "了解 Linux 符号链接和硬链接，包括如何创建和管理它们。通过这份适合初学者的指南，理解它们之间的区别和用例。"
meta_keywords: "Linux 符号链接，硬链接，ln 命令，符号链接，Linux 文件系统，Linux 教程，Linux 初学者"
---

## Lesson Content

让我们使用之前的一个 inode 信息示例：

```plaintext
pete@icebox:~$ ls -li
140 drwxr-xr-x 2 pete pete 6 Jan 20 20:13 Desktop
141 drwxr-xr-x 2 pete pete 6 Jan 20 20:01 Documents
```

您可能已经注意到，我们一直忽略了 `ls` 命令的第三个字段；该字段是链接计数。链接计数是文件拥有的硬链接总数。嗯，这现在对您来说毫无意义，所以我们先来讨论链接。

### Symlinks

在 Windows 操作系统中，有一种叫做快捷方式的东西。快捷方式只是其他文件的别名。如果您对原始文件进行某些操作，可能会破坏快捷方式。在 Linux 中，快捷方式的等效物是符号链接（或软链接或 symlinks）。符号链接允许我们通过文件名链接到另一个文件。Linux 中发现的另一种链接类型是硬链接；这些实际上是另一个链接到 inode 的文件。让我们从符号链接开始，看看我在实践中是什么意思。

```bash
pete@icebox:~/Desktop$ echo 'myfile' > myfile
pete@icebox:~/Desktop$ echo 'myfile2' > myfile2
pete@icebox:~/Desktop$ echo 'myfile3' > myfile3

pete@icebox:~/Desktop$ ln -s myfile myfilelink
pete@icebox:~/Desktop$ ls -li
total 12
  151 -rw-rw-r-- 1 pete pete 7 Jan 21 21:36 myfile
93401 -rw-rw-r-- 1 pete pete 8 Jan 21 21:36 myfile2
93402 -rw-rw-r-- 1 pete pete 8 Jan 21 21:36 myfile3
93403 lrwxrwxrwx 1 pete pete 6 Jan 21 21:39 myfilelink -> myfile
```

您可以看到我创建了一个名为 `myfilelink` 的符号链接，它指向 `myfile`。符号链接用 `->` 表示。请注意，我确实获得了一个新的 inode 号；符号链接只是指向文件名的文件。当您修改符号链接时，文件也会被修改。Inode 号对于文件系统是唯一的；您不能在单个文件系统中拥有两个相同的 inode 号，这意味着您不能通过其 inode 号引用不同文件系统中的文件。但是，如果您使用符号链接，它们不使用 inode 号；它们使用文件名，因此可以在不同的文件系统之间引用。

### Hardlinks

让我们看一个硬链接的例子：

```bash
pete@icebox:~/Desktop$ ln myfile2 myhardlink
pete@icebox:~/Desktop$ ls -li
total 16
  151 -rw-rw-r-- 1 pete pete 7 Jan 21 21:36 myfile
93401 -rw-rw-r-- 2 pete pete 8 Jan 21 21:36 myfile2
93402 -rw-rw-r-- 1 pete pete 8 Jan 21 21:36 myfile3
93403 lrwxrwxrwx 1 pete pete 6 Jan 21 21:39 myfilelink -> myfile
93401 -rw-rw-r-- 2 pete pete 8 Jan 21 21:36 myhardlink
```

硬链接只是创建另一个链接到相同 inode 的文件。因此，如果我修改 `myfile2` 或 `myhardlink` 的内容，更改将在两者上都可见。但是，如果我删除了 `myfile2`，文件仍然可以通过 `myhardlink` 访问。这就是 `ls` 命令中的链接计数发挥作用的地方。链接计数是 inode 拥有的硬链接数量。当您删除文件时，它将减少该链接计数。只有当指向 inode 的所有硬链接都被删除时，inode 才会被删除。当您创建文件时，其链接计数为 1，因为它是唯一指向该 inode 的文件。与符号链接不同，硬链接不跨文件系统，因为 inode 对于文件系统是唯一的。

### Creating a symlink

```bash
ln -s myfile mylink
```

要创建符号链接，您使用 `ln` 命令，带 `-s` 表示符号链接，然后指定目标文件和链接名称。

### Creating a hardlink

```bash
ln somefile somelink
```

类似于符号链接的创建，只是这次您省略了 `-s`。

## Exercise

尝试创建符号链接和硬链接。删除几个并看看会发生什么。

## Quiz Question

用于创建符号链接的命令是什么？

## Quiz Answer

ln -s
