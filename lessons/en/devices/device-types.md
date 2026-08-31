---
lesson_id: "device-types"
course_id: "devices"
lang: "en"
order_index: 2
title: "device types"
description: "Learn to distinguish character and block device nodes from pipes, sockets, and regular filesystem objects."
meta_title: "device types - Devices"
meta_description: "Explore the different Linux device types, including character, block, pipe, and socket devices. Learn how Linux manages devices, how to identify a device file using `ls -l /dev`, and understand the role of major and minor device numbers."
meta_keywords: "linux devices, linux device types, device file, character device, block device, major minor numbers, linux for devices, /dev directory"
---

The first character in an `ls -l` mode identifies an object's filesystem type. Under `/dev`, character and block special files are device nodes. Pipes and Unix-domain socket nodes can also appear there, but they are interprocess communication objects rather than hardware device nodes.

```text
$ ls -l /dev/null /dev/sda /run/systemd/journal/dev-log /tmp/example-fifo
crw-rw-rw- 1 root root 1, 3 ... /dev/null
brw-rw---- 1 root disk 8, 0 ... /dev/sda
srw-rw-rw- 1 root root      ... /run/systemd/journal/dev-log
prw------- 1 user user      ... /tmp/example-fifo
```

Entries and permissions vary by system; the example illustrates type characters only.

## Character Device Nodes

A `c` identifies a character device. It usually exposes a stream-oriented or device-specific interface rather than addressable fixed-size storage blocks. Examples include terminals and pseudo-devices such as `/dev/null`.

“Character” does not require each system call to transfer exactly one character. Applications can read or write buffers, while the driver defines blocking, framing, and control behavior.

:::single-choice{#device-types-character-marker}
Which first mode character identifies a character device node?

::option[`b`]{#device-types-marker-block explanation="The `b` marker identifies a block device node."}
::option[`p`]{#device-types-marker-pipe explanation="The `p` marker identifies a FIFO, or named pipe."}
::option[`c`]{#device-types-marker-character .correct explanation="Character special files appear with `c` at the start of a long-listing mode."}
:::

## Block Device Nodes

A `b` identifies a block device. Block devices provide addressable storage in blocks through the kernel's block layer and can support operations such as buffered I/O, partitioning, and filesystems. Disks, partitions, and logical volumes commonly have block nodes.

A block node is not a mounted filesystem. It represents a storage device or logical region; a filesystem can be created on it and mounted separately. Writing raw data to the wrong block node can destroy partition tables, filesystems, or user data.

:::single-choice{#device-types-block-marker}
What does first mode character `b` indicate?

::option[A background shell job.]{#device-types-background-job explanation="Shell job state is not encoded as a filesystem type character."}
::option[A block device interface.]{#device-types-block-device .correct explanation="Block special files expose addressable storage through the kernel block subsystem."}
::option[A broken symbolic link.]{#device-types-broken-link explanation="Symbolic links use `l`, whether or not their target currently exists."}
:::

## FIFOs and Socket Nodes

A `p` identifies a FIFO, also called a named pipe. It provides a named byte stream through which processes can communicate. The data is not persistently stored in the FIFO node after being consumed.

An `s` identifies a Unix-domain socket node. It names a local socket endpoint and can support connection-oriented or datagram communication, descriptor passing, and peer credential features. Network sockets using Internet addresses do not necessarily have filesystem nodes.

Neither a FIFO nor a Unix socket node uses device major and minor numbers to select a hardware driver.

:::single-choice{#device-types-pipe-socket-distinction}
Which statement correctly distinguishes these IPC object types?

::option[`p` marks a disk partition, while `s` marks solid-state storage.]{#device-types-storage-letters explanation="Partitions are normally block devices, and the letters do not encode storage technology."}
::option[`p` marks a FIFO, while `s` marks a Unix-domain socket node.]{#device-types-p-and-s .correct explanation="These are separate filesystem object types used for local interprocess communication."}
::option[Both types identify kernel block drivers through major numbers.]{#device-types-ipc-major explanation="FIFO and socket nodes are not character or block device nodes."}
:::

## Major and Minor Device Numbers

Character and block device nodes store a device number split into major and minor components. In a long listing they replace the ordinary file-size column:

```text
brw-rw---- 1 root disk 8, 0 ... /dev/sda
```

The pair tells the kernel which registered device interface and instance the node addresses. A major number is associated with a driver or device class, while the driver interprets the minor number. Do not hard-code assumptions such as “minor zero always means the first drive”; mappings depend on the subsystem and kernel interfaces.

Display type and device numbers explicitly with:

```bash
$ stat -c 'type=%F major=%t minor=%T path=%n' /dev/null
```

The `%t` and `%T` values are shown in hexadecimal by GNU `stat`.

:::single-choice{#device-types-major-minor-scope}
Which objects use major and minor numbers to identify a kernel device interface?

::option[Every regular file and directory.]{#device-types-all-files explanation="Regular files use size and filesystem metadata rather than a device-node major/minor pair."}
::option[Only symbolic links whose targets are missing.]{#device-types-broken-symlinks explanation="Symbolic links store path text and do not become device nodes when a target is absent."}
::option[Character and block device nodes.]{#device-types-device-number-nodes .correct explanation="Their special inode metadata contains the device number routed to a driver interface."}
:::

## Summary

You can now interpret special filesystem types without treating all of them as hardware devices.

1. Read `c` as character and `b` as block device nodes.
2. Read `p` as FIFO and `s` as Unix-domain socket node.
3. Associate major and minor numbers only with device nodes.
4. Treat raw block-device access as potentially destructive.
