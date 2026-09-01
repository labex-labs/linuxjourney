---
lesson_id: "mounting-and-unmounting-filesystems"
course_id: "filesystem"
lang: "en"
order_index: 6
title: "mount and umount"
description: "Learn how to attach, inspect, and safely detach filesystems using verified sources and mount points."
meta_title: "mount and umount - The Filesystem"
meta_description: "Learn how to use the mount and umount commands in Linux to attach and detach filesystems. This guide covers mounting devices, the sudo umount process for a safe linux unmount, and using UUIDs."
meta_keywords: "mount, umount, sudo umount, umount linux, linux unmount, debian umount, mount filesystem, unmount device, Linux UUID, mount point"
---

Mounting attaches a filesystem to a directory in the visible namespace. The source can be a block device, network export, virtual filesystem, bind source, or another implementation-specific object. The target directory is called the mount point.

## Preparing and Inspecting a Mount Point

Create a deliberately named directory when local policy calls for it:

```bash
$ sudo mkdir -p /mnt/mydrive
```

Inspect it before mounting:

```bash
$ findmnt --target /mnt/mydrive
$ sudo ls -la /mnt/mydrive
```

Mounting on a nonempty directory hides its existing entries behind the new filesystem until unmounted; it does not delete them. This can confuse applications and consume disk space invisibly, so use an empty, dedicated mount point.

:::single-choice{#mount-umount-nonempty-target} What happens to existing files in a directory when another filesystem is mounted there?

::option[They are automatically copied into the new filesystem.]{#mount-umount-copied-files explanation="Mounting changes namespace attachment and does not migrate directory contents."}
::option[They are permanently erased by the kernel.]{#mount-umount-erased-files explanation="The files normally reappear after unmounting because they were obscured, not deleted."}
::option[They are hidden by the mount until it is detached.]{#mount-umount-hidden-files .correct explanation="The underlying directory remains, but pathname lookup crosses into the mounted filesystem."}
:::

## Mounting a Verified Filesystem

After confirming source identity, detected type, and expected contents, mount explicitly:

```bash
$ sudo mount -t ext4 /dev/VERIFIED-PARTITION /mnt/mydrive
```

The `-t` option specifies the filesystem implementation. Mount can often detect the type, but explicit type and reviewed options make intent clearer. For untrusted or removable content, consider restrictive options such as `ro`, `nosuid`, `nodev`, and `noexec` where they match the workload; each has limits and must not be treated as a complete sandbox.

Verify what is actually mounted:

```bash
$ findmnt --target /mnt/mydrive -o TARGET,SOURCE,FSTYPE,OPTIONS
```

Mounts are namespace-scoped. A mount created in a container or private service namespace might not appear in another process's view.

:::single-choice{#mount-umount-mount-role} What does the `mount` command do in the shown workflow?

::option[Creates a new filesystem and erases the source.]{#mount-umount-format-source explanation="Filesystem creation is a separate destructive `mkfs` operation."}
::option[Attaches a filesystem source to a directory in a mount namespace.]{#mount-umount-attach-filesystem .correct explanation="Path lookup beneath the target then enters the attached filesystem."}
::option[Changes the disk's partition boundaries.]{#mount-umount-change-partitions explanation="Partition-table editing is separate from namespace mounting."}
:::

## Using Filesystem UUIDs

Enumeration names such as `/dev/sdb2` can change. Discover filesystem identifiers with:

```bash
$ lsblk -f
$ sudo blkid
```

Then mount a verified filesystem by UUID:

```bash
$ sudo mount UUID=130b882f-7d79-436d-a096-1e594c92bb76 /mnt/mydrive
```

A UUID identifies the filesystem, not necessarily the physical disk. Reformatting changes it, while cloning can duplicate it. Verify uniqueness before attaching original and clone to the same system.

:::single-choice{#mount-umount-uuid-benefit} Why is a filesystem UUID often preferable to `/dev/sdX` for persistent configuration?

::option[It prevents all storage devices from ever failing.]{#mount-umount-uuid-no-failure explanation="An identifier does not provide redundancy, integrity repair, or backup."}
::option[It guarantees cloned filesystems have different identifiers.]{#mount-umount-uuid-clone-unique explanation="A block-level clone can copy the UUID and create a collision."}
::option[It is tied to filesystem identity rather than current enumeration order.]{#mount-umount-uuid-identity .correct explanation="The block-device path can change while the filesystem metadata retains its UUID."}
:::

## Unmounting Safely

Detach by the exact mount point:

```bash
$ sudo umount /mnt/mydrive
```

The command is spelled `umount`, without the first `n`. Successful unmount detaches the filesystem after the kernel completes required writeback and references permit it. Confirm afterward with `findmnt` before disconnecting storage.

A successful unmount is not always the final safe-removal operation for removable media. Desktop storage stacks may offer an eject or power-off action that flushes device caches and disables a USB device. Follow the platform and hardware workflow.

:::single-choice{#mount-umount-command-name} Which command detaches `/mnt/mydrive`?

::option[`umount /mnt/mydrive`]{#mount-umount-umount-correct .correct explanation="`umount` detaches the filesystem mounted at the specified target."}
::option[`unmount /mnt/mydrive`]{#mount-umount-unmount-spelling explanation="The standard command name omits the first `n`."}
::option[`mkfs /mnt/mydrive`]{#mount-umount-mkfs-target explanation="Mkfs creates filesystem structures and must not be used for detachment."}
:::

## Diagnosing a Busy Filesystem

Unmounting fails when the namespace still has active references, such as open files, a process working directory, nested mounts, swap, or other storage layers. Investigate rather than immediately forcing it:

```bash
$ findmnt --submounts /mnt/mydrive
$ sudo fuser -vm /mnt/mydrive
```

Move shells out of the tree, stop the responsible application cleanly, and unmount child mounts before the parent. Lazy unmount and force options have specialized semantics and can leave active references or risk data loss; use them only with documented recovery reasoning.

:::single-choice{#mount-umount-busy-cause} Which condition can make `umount` report that a filesystem is busy?

::option[The mount point directory name contains lowercase letters.]{#mount-umount-lowercase explanation="Path casing alone does not create an active filesystem reference."}
::option[A process has its current working directory inside the mount.]{#mount-umount-cwd-busy .correct explanation="The process retains a reference into the mounted filesystem, preventing ordinary detachment."}
::option[The filesystem UUID is longer than the device name.]{#mount-umount-uuid-length explanation="Identifier string length is unrelated to busy-state checks."}
:::

Use [Manage Linux Partitions and Filesystems](https://labex.io/labs/comptia-manage-linux-partitions-and-filesystems-590845) to practice on designated disposable storage.

## Summary

You can now attach and detach filesystems with verifiable scope.

1. Use an empty, dedicated mount point.
2. Verify source, type, options, and resulting mount.
3. Prefer a unique filesystem identifier for persistent references.
4. Unmount by target and confirm detachment before removal.
5. Diagnose active references instead of forcing a busy unmount.
