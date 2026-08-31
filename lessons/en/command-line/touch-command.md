---
lesson_id: "touch-command"
course_id: "command-line"
lang: "en"
order_index: 5
title: "touch"
description: "Learn how to create empty files and manage file timestamps with the touch command."
meta_title: "touch - Command Line"
meta_description: "Learn the Linux touch command with examples for creating empty files, updating timestamps, setting dates, using reference files, and avoiding overwrites."
meta_keywords: "linux touch command, touch command, create file linux, update timestamp linux, touch -d, touch -r, touch -c"
---

The `touch` command changes file timestamps. It is also commonly used to create one or more empty files.

The basic syntax is:

```bash
touch [OPTIONS] FILE...
```

## Creating Empty Files

If the named file does not exist, `touch` creates it as an empty file:

```bash
$ touch mysuperduperfile
```

You can create several files in one command by listing each name:

```bash
$ touch file1.txt file2.txt file3.log
```

This is useful for creating placeholders, but `touch` does not add text to a file. Use a text editor or another command designed to write content when you need a nonempty file.

:::single-choice{#create-several-empty-files}
Which command creates three empty files named `one`, `two`, and `three` if they do not already exist?

::option[`touch "one two three"`]{#touch-one-spaced explanation="The quotation marks make this a single filename containing spaces. This command addresses one file rather than three."}
::option[`mkdir one two three`]{#mkdir-three explanation="`mkdir` creates directories rather than empty regular files. Use `touch` for the files requested here."}
::option[`touch one two three`]{#touch-three .correct explanation="`touch` accepts multiple file operands. It creates each missing file without adding content."}
:::

## Updating File Timestamps

Files track several timestamps. By default, running `touch` on an existing file changes both its access time and modification time to the current time. It leaves the file's contents unchanged.

You can compare the displayed modification time before and after running the command:

```bash
$ ls -l mysuperduperfile
$ touch mysuperduperfile
$ ls -l mysuperduperfile
```

The `ls -l` output normally displays the modification time, not the access time.

:::single-choice{#touch-existing-file}
What happens when you run `touch report.txt` and `report.txt` already exists?

::option[Its timestamps are updated without replacing its contents.]{#timestamps-only .correct explanation="By default, `touch` updates the access and modification times of an existing file. It does not overwrite the file's data."}
::option[Its contents are deleted and the file becomes empty.]{#contents-deleted explanation="Creating an empty file is the missing-file behavior. An existing file keeps its contents when `touch` updates its timestamps."}
::option[The command fails because the filename is already in use.]{#existing-error explanation="`touch` is designed to operate on existing files as well as missing ones. An existing name is not itself an error."}
:::

## Controlling Which Timestamp Changes

Use `-a` to change only the access time or `-m` to change only the modification time:

```bash
$ touch -a notes.txt
$ touch -m notes.txt
```

:::single-choice{#change-modification-time-only}
Which command updates only the modification time of `notes.txt`?

::option[`touch -a notes.txt`]{#access-only explanation="The `-a` option changes only the access time. It does not select the modification time requested here."}
::option[`touch -m notes.txt`]{#modification-only .correct explanation="The `-m` option limits the change to the modification time. The access time is left unchanged."}
::option[`touch -c notes.txt`]{#no-create explanation="The `-c` option controls whether a missing file is created. It does not limit the update to one timestamp."}
:::

## Setting or Copying a Time

The `-d` option accepts a date string instead of using the current time:

```bash
$ touch -d "2026-06-23 12:30:00" mysuperduperfile
```

To give a file the same access and modification times as a reference file, use `-r`:

```bash
$ touch -r file1.txt file2.txt
```

Here, `file1.txt` supplies the timestamps and `file2.txt` is the file that changes. The `-t` option is another way to provide a time, using a compact numeric format.

:::single-choice{#copy-reference-timestamps}
Which command copies the timestamps of `source.txt` to `target.txt`?

::option[`touch -r source.txt target.txt`]{#reference-source .correct explanation="With `-r`, the next operand is the reference file and the final operand is the file whose timestamps are updated."}
::option[`touch -r target.txt source.txt`]{#reference-target explanation="This reverses the roles of the files. It would use `target.txt` as the reference and update `source.txt`."}
::option[`touch -d source.txt target.txt`]{#date-source explanation="The `-d` option expects a date string, not a reference filename. Use `-r` to copy another file's timestamps."}
:::

## Avoiding File Creation

Normally, `touch` creates a file when the named path does not exist. Add `-c` when you want to update a file only if it already exists:

```bash
$ touch -c existing-file.txt
```

If `existing-file.txt` is missing, this command does not create it. This behavior can be useful in scripts that should update a timestamp without introducing a new file.

:::single-choice{#update-without-creating}
Which command updates `status.log` if it exists but does not create it if it is missing?

::option[`touch -a status.log`]{#touch-access explanation="The `-a` option selects the access time, but a missing file can still be created. It does not provide the required no-create behavior."}
::option[`touch -m status.log`]{#touch-modification explanation="The `-m` option selects the modification time, but it does not prevent creation of a missing file. Use `-c` for that condition."}
::option[`touch -c status.log`]{#touch-no-create .correct explanation="The `-c` option suppresses creation of a missing file. An existing file can still have its timestamps updated."}
:::

## Summary

You can now use `touch` to create empty files and control file timestamps.

1. Create one or more empty files.
2. Update timestamps without changing file contents.
3. Select the access time or modification time.
4. Set a specific time or copy a reference file's timestamps.
5. Prevent creation of a missing file.
