---
lesson_id: "file-command"
course_id: "command-line"
lang: "en"
order_index: 6
title: "file"
description: "Learn how to identify a file's likely content type without relying on its name or extension."
meta_title: "file - Command Line"
meta_description: "Learn the Linux file command with examples for identifying text files, images, scripts, compressed archives, binaries, and MIME types."
meta_keywords: "linux file command, file command, identify file type linux, mime type linux, text file, binary file, archive file"
---

In the previous lesson, you used `touch` to create a file without adding an extension. Linux filenames do not have to describe what a file contains: a file named `funny.gif` is not necessarily a GIF image.

Use the `file` command to inspect a file and report its likely type:

```bash
$ file banana.jpg
banana.jpg: JPEG image data
```

## Why File Extensions Are Not Enough

Linux tools usually do not require a file extension to determine a file's type. A shell script can be named `backup`, a text file can be named `README`, and an image can have a misleading extension. The `file` command examines properties such as filesystem metadata and recognizable patterns in the content.

```bash
$ file README
README: ASCII text
$ file /bin/ls
/bin/ls: ELF 64-bit LSB executable
```

Its result is a classification, not a guarantee. An unusual, incomplete, or damaged file may receive a broad description such as `data` instead of a precise type.

:::single-choice{#identify-misleading-extension} A file named `report.jpg` may not contain an image. Which command checks its likely content type?

::option[`ls report.jpg`]{#list-report explanation="`ls` confirms that the name exists and can show metadata, but it does not classify the file's contents."}
::option[`file report.jpg`]{#inspect-report .correct explanation="The `file` command examines the file and reports a likely type. It does not rely only on the `.jpg` suffix."}
::option[`touch report.jpg`]{#touch-report explanation="`touch` updates timestamps or creates a missing file. It does not identify the content type."}
:::

## Checking Multiple Files

You can check several files at once:

```bash
$ file notes.txt image.png archive.tar.gz
notes.txt: ASCII text
image.png: PNG image data
archive.tar.gz: gzip compressed data
```

You can also pass a shell wildcard. The shell expands `*` into matching names before `file` examines them:

```bash
$ file *
```

:::single-choice{#inspect-multiple-files} Which command asks `file` to inspect every non-hidden name matched by `*` in the current directory?

::option[`file *`]{#file-wildcard .correct explanation="The shell expands `*` to matching non-hidden names, and `file` inspects each resulting operand."}
::option[`file .`]{#file-current-directory explanation="A single dot names the current directory itself. This command classifies that directory rather than each entry inside it."}
::option[`file -b`]{#file-brief-no-operand explanation="The `-b` option changes output formatting, but this command does not supply the files to inspect."}
:::

## Showing MIME Information

The `-i` option prints MIME-style information, including a media type and, when available, a character set. This form is useful when another program expects values such as `text/html`.

```bash
$ file -i index.html
index.html: text/html; charset=us-ascii
```

:::single-choice{#show-mime-information} Which command reports MIME-style information for `index.html`?

::option[`file -b index.html`]{#brief-index explanation="The `-b` option omits the filename from the usual description. It does not specifically request MIME-style output."}
::option[`file -i index.html`]{#mime-index .correct explanation="The `-i` option requests MIME-style output, such as `text/html` plus character-set information."}
::option[`file -L index.html`]{#follow-index explanation="The `-L` option controls symbolic-link handling. It does not select the MIME output format."}
:::

## Useful file Options

- `-i`: Show MIME-style information.
- `-b`: Use brief mode and omit the filename from the output.
- `-L`: Follow symbolic links and classify their targets.
- `-z`: Try to examine the contents of compressed files.

For example:

```bash
$ file -b notes.txt
ASCII text
```

:::single-choice{#omit-filename-from-output} Which command classifies `notes.txt` but omits its filename from the output?

::option[`file -i notes.txt`]{#mime-notes explanation="The `-i` option requests MIME-style information. The output still normally includes the filename."}
::option[`file -z notes.txt`]{#compressed-notes explanation="The `-z` option asks `file` to look inside compressed data when possible. It does not enable brief output."}
::option[`file -b notes.txt`]{#brief-notes .correct explanation="Brief mode, selected with `-b`, prints the classification without the filename prefix."}
:::

## Summary

You can now use `file` to investigate what a file is likely to contain.

1. Classify a file without trusting its extension.
2. Inspect multiple pathnames in one command.
3. Request MIME-style information.
4. Adjust how links, compressed data, and output labels are handled.
