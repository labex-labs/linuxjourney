---
index: 3
lang: "en"
title: "tar and gzip"
meta_title: "tar and gzip - Packages"
meta_description: "Learn to use tar and gzip for file archiving and compression in Linux. Understand commands for creating, extracting, and compressing files. Get started with this beginner guide!"
meta_keywords: "tar, gzip, Linux archiving, file compression, tar command, gzip command, Linux tutorial, beginner Linux"
---

## Lesson Content

Before we get into package installation and the different managers, we need to discuss archiving and compressing files, because you will most likely encounter these when you hunt for software on the internet.

You probably already know what a file archive is; you've most likely encountered file types such as .rar and .zip. These are archives of files; they contain many files inside of them, but they come in this very neat single file known as an archive.

### Compressing files with gzip

gzip is a program used to compress files in Linux; they end in a .gz extension.

To compress a file:

```bash
gzip mycoolfile
```

To decompress the file:

```bash
gunzip mycoolfile.gz
```

### Creating archives with tar

Unfortunately, gzip can't add multiple files into one archive for us. Luckily, we have the tar program which does. When you create an archive using tar, it will have a .tar extension.

```bash
tar cvf mytarfile.tar mycoolfile1 mycoolfile2
```

- `c` - create
- `v` - tell the program to be verbose and let us see what it's doing
- `f` - the filename of the tar file has to come after this option; if you are creating a tar file, you'll have to come up with a name

### Unpacking archives with tar

To extract the contents of a tar file, use:

```bash
tar xvf mytarfile.tar
```

- `x` - extract
- `v` - tell the program to be verbose and let us see what it's doing
- `f` - the file you want to extract

### Compressing/uncompressing archives with tar and gzip

Many times you'll see a tar file that has been compressed, such as: `mycompressedarchive.tar.gz`. All you need to do is work outside in, so first remove the compression with `gunzip` and then you can unpack the tar file. Or you can alternatively use the **z** option with tar, which just tells it to use the gzip or gunzip utility.

Create a compressed tar file:

```bash
tar czf myfile.tar.gz
```

Uncompress and unpack:

```bash
tar xzf file.tar
```

If you need help remembering this: e**X**tract all **Z**ee **F**iles!

tar is one of those commands that is so important and yet you never really remember it. Relevant xkcd: `https://xkcd.com/1168`

### Other Utilities

Throughout your journey with Linux, you'll encounter other archive and compression types such as: bzip2, compress, zip, unzip, etc. They are a little less common, but just keep in mind that different utilities will call for different commands.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of file archiving and compression:

1. **[File Packaging and Compression](https://labex.io/labs/linux-file-packaging-and-compression-385413)** - Learn essential Linux file compression and packaging techniques using tools like tar, gzip, and zip.
2. **[Create and Restore a Backup with tar in Linux](https://labex.io/labs/comptia-create-and-restore-a-backup-with-tar-in-linux-590843)** - Gain hands-on experience creating and restoring file system backups using the tar command.
3. **[Backup System Log](https://labex.io/labs/linux-backup-system-log-17989)** - Learn the essential skill of backing up system log files using the tar command and date formatting.

These labs will help you apply the concepts of archiving and compression in real scenarios and build confidence with managing files in Linux.

## Quiz Question

What tar flag is used to create archives?

## Quiz Answer

c
