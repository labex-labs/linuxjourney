---
lesson_id: "network-file-sharing"
course_id: "network-sharing"
lang: "en"
order_index: 1
title: "File Sharing Overview"
description: "Learn how to choose and safely perform an SSH-based file transfer with scp."
meta_title: "File Sharing Overview - Network Sharing"
meta_description: "Explore Linux file sharing with our free online course. Learn one of the best ways to learn Linux commands like scp for secure network file transfers. A key resource for coding in Linux."
meta_keywords: "linux file sharing, scp command, secure copy, learn linux commands, best linux course online free, coding in linux, network file transfer, best resources to learn linux"
---

Network file movement ranges from one-time copies to continuously mounted shares and synchronized directory trees. Choose a method based on direction, data size, update frequency, identity model, network trust, metadata requirements, and whether clients need live shared access.

## Choosing a Transfer Method

- `scp` or SFTP provides an SSH-authenticated copy or interactive transfer.
- `rsync` efficiently reconciles directory trees locally or over a transport such as SSH.
- NFS presents server exports as mounted filesystems, commonly between Unix-like hosts.
- SMB, implemented by Samba on Linux, supports shared access across many operating systems.
- HTTP can provide simple downloads but is not a general mounted filesystem.

A copy is not automatically a backup. A backup design also needs independent retention, restore testing, integrity checks, and protection from the same deletion or compromise.

:::single-choice{#file-sharing-one-time-ssh-copy} Which tool is suitable for a one-time file copy through SSH?

::option[`scp`]{#file-sharing-scp .correct explanation="SCP uses SSH authentication and transport for file copies."}
::option[`uptime`]{#file-sharing-uptime explanation="Uptime reports host runtime and load rather than transferring files."}
::option[`logrotate`]{#file-sharing-logrotate explanation="Logrotate manages file-log generations on a host."}
:::

## Understanding scp Paths

The general form is `scp SOURCE DESTINATION`. A remote operand commonly uses `user@host:path`:

```bash
$ scp -- report.txt alice@example.net:/srv/incoming/
$ scp -- alice@example.net:/srv/outgoing/result.txt ./result.txt
```

The first command pushes a local file; the second pulls a remote file. A colon distinguishes the remote host from its path. Quote paths that contain shell-sensitive characters and avoid ambiguous untrusted filenames.

:::single-choice{#file-sharing-scp-pull-source} In an `scp` pull, where does the remote specification appear?

::option[As the source before the local destination.]{#file-sharing-pull-source .correct explanation="Copy direction follows the source-to-destination operand order."}
::option[As the local destination after every option.]{#file-sharing-pull-destination explanation="The remote object being retrieved is the source operand."}
::option[Only inside the user's SSH configuration file.]{#file-sharing-pull-config explanation="SSH configuration can provide defaults, but the copied remote path is still an operand."}
:::

## Copying a Directory

Use recursive mode for a directory tree:

```bash
$ scp -r -- project/ alice@example.net:/srv/incoming/
```

Before copying, inspect data size, symlinks, permissions, ownership requirements, free space, and destination naming. SCP is not a synchronization policy; repeated directory copies can leave files at the destination that no longer exist at the source.

:::single-choice{#file-sharing-scp-recursive} What does `scp -r` request?

::option[Removal of the remote destination before copying.]{#file-sharing-scp-remove explanation="Recursive mode traverses directories and does not define cleanup policy."}
::option[Recursive copying of a directory tree.]{#file-sharing-scp-tree .correct explanation="The flag is required when the selected source is a directory."}
::option[Read-only access to the SSH configuration.]{#file-sharing-scp-readonly explanation="The option concerns directory traversal, not configuration access."}
:::

## Verifying Identity and Results

SSH host-key verification protects against connecting to the wrong server. Treat a changed host key as an event to verify through a trusted channel rather than bypassing the warning. Use least-privilege accounts and key handling appropriate to the environment.

After transfer, verify exit status, expected files, sizes, metadata, and—when integrity requirements demand it—independently calculated hashes at both ends. Confirm that the destination application can actually read the data.

:::single-choice{#file-sharing-host-key-change} What should you do when SSH reports an unexpected changed host key?

::option[Disable host-key checking for every future transfer.]{#file-sharing-disable-checking explanation="This removes an important server-identity control."}
::option[Verify the new key through a trusted source before continuing.]{#file-sharing-verify-key .correct explanation="The warning can indicate a rebuilt host, wrong destination, or interception and should be investigated."}
::option[Publish the private authentication key in the command output.]{#file-sharing-publish-key explanation="Private credentials must not be exposed."}
:::

## Summary

You can now select and verify a secure one-time network file copy.

1. Match the sharing method to access and retention needs.
2. Read local and remote `scp` operands by source and destination.
3. Use recursive mode deliberately for directory trees.
4. Verify server identity, transfer results, and destination usability.
