---
lesson_id: "compressed-archives-tar"
course_id: "packages"
lang: "en"
order_index: 3
title: "tar and gzip"
description: "Learn how to archive files with `tar`, compress streams with `gzip`, and inspect archives before safe extraction."
meta_title: "tar and gzip - Packages"
meta_description: "A comprehensive guide to using tar and gzip in Linux. Learn about tar compression, how to create and extract archives, and the difference between gzip and tar. Master commands to compress tar gz files and manage your software packages effectively."
meta_keywords: "tar and gzip, tar compression, gzip tar, compress tar gz, gzip and tar, Linux archiving, file compression, tar command, gzip command, Linux tutorial"
---

Archiving and compression solve different problems. An archive combines a directory tree and its metadata into one stream. Compression encodes a stream to reduce its size. A `.tar.gz` file is conventionally a tar archive whose stream has been compressed with gzip.

## Compressing One Stream with `gzip`

By default, `gzip` compresses a file and replaces the original name with a `.gz` file:

```bash
$ gzip report.txt
```

This normally removes `report.txt` after successfully creating `report.txt.gz`. Decompress it with:

```bash
$ gunzip report.txt.gz
```

Use `gzip -k report.txt` where supported to keep the input file, or use standard streams when you need explicit control. A filename extension is a convention, not proof of the actual format; tools such as `file` can inspect content.

:::single-choice{#tar-gzip-gzip-role}
What is the primary role of `gzip` in this lesson?

::option[Combining a directory tree into an archive with file metadata.]{#tar-gzip-directory-archive explanation="Tar performs that archiving role before gzip compression is applied."}
::option[Compressing a single input stream.]{#tar-gzip-compress-stream .correct explanation="Gzip transforms one byte stream and does not itself encode a directory hierarchy."}
::option[Installing dependency metadata into a package database.]{#tar-gzip-package-install explanation="Compression is separate from native package installation and dependency tracking."}
:::

## Creating a Tar Archive

Create an uncompressed archive with:

```bash
$ tar -cvf project.tar file1 file2 directory1
```

- `-c` creates a new archive.
- `-v` lists members while processing and is optional.
- `-f project.tar` names the archive file; because `-f` consumes an argument, keep the filename beside it.

Paths are stored as archive member names. Create archives from a deliberate working directory and avoid unintentionally capturing secrets, caches, sockets, or broad absolute paths.

:::single-choice{#tar-gzip-create-option}
Which `tar` option creates a new archive?

::option[`-x`]{#tar-gzip-option-extract explanation="The `-x` operation extracts archive members."}
::option[`-c`]{#tar-gzip-option-create .correct explanation="The create operation writes a new archive from the named inputs."}
::option[`-t`]{#tar-gzip-option-list explanation="The `-t` operation lists archive members without extracting them."}
:::

## Creating a Gzip-Compressed Tar Archive

GNU tar and many other implementations can invoke gzip with `-z`:

```bash
$ tar -czvf project.tar.gz file1 file2 directory1
```

The result is one gzip-compressed tar stream. Compression does not encrypt the archive or hide its contents from someone who can read and decompress it. If confidentiality is required, use an appropriate authenticated-encryption workflow and manage keys separately.

:::single-choice{#tar-gzip-z-option}
What does `-z` request in the shown `tar` command?

::option[Encrypt the archive using a zero-knowledge key.]{#tar-gzip-z-encrypt explanation="Neither tar nor gzip provides encryption through this option."}
::option[Discard every zero-length member.]{#tar-gzip-z-zero explanation="The option selects gzip and does not filter archive members by size."}
::option[Process the archive stream through gzip.]{#tar-gzip-z-gzip .correct explanation="The `z` option connects tar's archive operation with gzip compression or decompression."}
:::

## Listing Before Extracting

Treat an archive from another party as untrusted input. List its member names first:

```bash
$ tar -tzf download.tar.gz
```

Look for unexpected absolute paths, `..` traversal components, surprising symbolic or hard links, device files, and names that would overwrite important files. Modern tar implementations apply protections, but behavior and options vary, and extracting still creates attacker-chosen names and content.

Extract into a newly created, nonprivileged staging directory:

```bash
$ mkdir extraction-stage
$ tar -xzf download.tar.gz -C extraction-stage
```

Do not extract an unreviewed archive as root. Verify what was created before moving selected files to their final locations.

:::single-choice{#tar-gzip-list-before-extract}
Which operation lists archive members without extracting them?

::option[`tar -czf download.tar.gz .`]{#tar-gzip-create-download explanation="This creates or replaces an archive from the current directory."}
::option[`tar -xzf download.tar.gz`]{#tar-gzip-extract-download explanation="The `-x` operation writes members into the target directory."}
::option[`tar -tzf download.tar.gz`]{#tar-gzip-list-members .correct explanation="The `-t` operation reads and displays the member table while `-z` handles gzip."}
:::

## Other Compression Formats

Tar implementations can work with compressors such as bzip2 and xz, commonly selected with `-j` and `-J` respectively in GNU tar. Format support and automatic detection differ, so consult `tar --help` or the local manual. ZIP is a separate archive format operated with tools such as `zip` and `unzip`.

:::single-choice{#tar-gzip-archive-confidentiality}
Does gzip compression make a tar archive confidential?

::option[No; anyone who can read it can ordinarily decompress it.]{#tar-gzip-not-encryption .correct explanation="Compression changes representation and size but does not provide access control or cryptographic secrecy."}
::option[Yes; gzip derives an encryption key from the filename.]{#tar-gzip-filename-key explanation="Gzip does not implement such an encryption mechanism."}
::option[Yes; tar encrypts every member before gzip sees it.]{#tar-gzip-tar-encrypt explanation="Tar archives members but does not automatically encrypt their contents."}
:::

Practice with disposable files in [File Packaging and Compression](https://labex.io/labs/linux-file-packaging-and-compression-385413), then apply inspection and staging in [Create and Restore a Backup with tar](https://labex.io/labs/comptia-create-and-restore-a-backup-with-tar-in-linux-590843).

## Summary

You can now combine tar archiving with gzip compression safely.

1. Distinguish a tar archive from gzip compression.
2. Create archives with `-c` and gzip streams with `-z`.
3. List members with `-t` before extracting with `-x`.
4. Extract untrusted content into a nonprivileged staging directory.
5. Treat compression as separate from encryption.
