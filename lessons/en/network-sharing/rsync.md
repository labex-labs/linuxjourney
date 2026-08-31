---
lesson_id: "rsync"
course_id: "network-sharing"
lang: "en"
order_index: 2
title: "rsync"
description: "Learn how to preview, run, and verify safe local or SSH-based directory synchronization with rsync."
meta_title: "rsync - Network Sharing"
meta_description: "Discover how to use the powerful rsync command in Linux for efficient file synchronization, remote data transfer, and reliable backups. This guide covers key rsync commands and options."
meta_keywords: "rsync, linux rsync, file synchronization, data backup, remote sync, rsync command, linux file transfer, rsync tutorial"
---

`rsync` reconciles files and directory trees while avoiding unnecessary transfer of unchanged data. Its efficiency does not make every invocation safe: source syntax, trailing slashes, metadata, exclusions, and deletion policy determine the result.

## Reading Source and Destination

Synchronize the contents of `source/` into `destination/` locally:

```bash
$ rsync -a -- source/ destination/
```

The trailing slash on `source/` means “copy this directory's contents.” Without it, `rsync -a source destination/` creates or updates `destination/source`. Always preview the resulting paths when changing slash placement.

:::single-choice{#rsync-source-trailing-slash}
What does the trailing slash in `rsync -a source/ destination/` signify?

::option[Delete the source after a successful transfer.]{#rsync-delete-source explanation="Source removal requires a separate explicit option and policy."}
::option[Copy the contents of `source` into the destination.]{#rsync-copy-contents .correct explanation="Removing the source slash changes the top-level destination layout."}
::option[Interpret the destination as a remote Windows share.]{#rsync-windows-share explanation="The slash controls directory contents, not transport type."}
:::

## Understanding Archive Mode

Archive mode, `-a`, is equivalent to a collection of recursive and metadata-preserving options commonly summarized as `-rlptgoD`. It preserves symlinks, permissions, modification times, groups, owners, and device or special files where permissions and platform support allow.

Archive mode does not include preservation of hard links, ACLs, or extended attributes; those commonly require `-H`, `-A`, and `-X`. It also does not create historical versions by itself.

:::single-choice{#rsync-archive-limit}
Which metadata is not included in `-a` by itself?

::option[Hard-link relationships.]{#rsync-hard-links .correct explanation="Preserving hard links requires the separate `-H` option."}
::option[Directory recursion.]{#rsync-archive-recursion explanation="Archive mode includes recursive traversal."}
::option[Modification times.]{#rsync-archive-times explanation="Archive mode includes time preservation."}
:::

## Previewing a Transfer

Use a dry run with itemized changes before a consequential sync:

```bash
$ rsync -a --dry-run --itemize-changes -- source/ destination/
```

A dry run predicts actions using the current scan; it cannot guarantee that files will not change before the real command. Save and review the exact command, then run it without `--dry-run` only after confirming both endpoints.

:::single-choice{#rsync-dry-run-purpose}
What does `--dry-run --itemize-changes` provide?

::option[A permanent snapshot retained on another device.]{#rsync-dry-backup explanation="No data copy or independent retention is created by a dry run."}
::option[A guarantee that source files cannot change later.]{#rsync-dry-lock explanation="Previewing does not lock the source tree."}
::option[A preview of the changes rsync currently plans.]{#rsync-dry-preview .correct explanation="Itemized dry-run output exposes path and metadata decisions before mutation."}
:::

## Synchronizing over SSH

Push to or pull from a remote host using the familiar remote operand:

```bash
$ rsync -a -- source/ alice@example.net:/srv/data/
$ rsync -a -- alice@example.net:/srv/data/ destination/
```

Modern rsync commonly uses SSH for this form, but confirm the configured remote shell, host key, account privileges, and remote rsync availability. Compression with `-z` can help compressible data on a constrained link but can waste CPU for data already compressed.

:::single-choice{#rsync-pull-direction}
Which operand order pulls remote data into a local directory?

::option[`rsync -a local/ host:/data/`]{#rsync-local-first explanation="This order pushes local content to the remote destination."}
::option[`rsync --delete host local`]{#rsync-missing-path explanation="This does not express the shown remote-path syntax and adds an unrelated destructive option."}
::option[`rsync -a host:/data/ local/`]{#rsync-remote-first .correct explanation="The remote tree is the source and the local tree is the destination."}
:::

## Treating Deletion as Destructive

`--delete` removes destination entries that are absent from the source within the synchronized scope. A reversed endpoint, wrong slash, or bad exclusion can therefore erase valid data. Preview against a test destination, ensure recoverable backups, review mount state, and consider maximum-delete limits before authorization.

After the real run, inspect exit status and logs, compare expected file counts and metadata, and test representative content or restoration. Rsync synchronization alone mirrors unwanted deletion or corruption and is not a complete backup strategy.

:::single-choice{#rsync-delete-effect}
What can `--delete` do during synchronization?

::option[Encrypt every transferred file with the SSH host key.]{#rsync-delete-encrypt explanation="Deletion policy is unrelated to file encryption."}
::option[Prevent all destination filesystem changes.]{#rsync-delete-readonly explanation="It explicitly authorizes additional destination changes."}
::option[Remove destination entries missing from the selected source scope.]{#rsync-delete-destination .correct explanation="The option makes destination membership mirror the source and requires a reviewed preview and recovery plan."}
:::

## Summary

You can now preview and verify an `rsync` operation without hiding its destructive edge cases.

1. Use trailing slashes to express the intended directory layout.
2. Add metadata options not covered by archive mode when required.
3. Review itemized dry-run output before the real sync.
4. Verify SSH identity and endpoint direction.
5. Treat deletion and backup retention as explicit policies.
