---
lesson_id: "dev-directory"
course_id: "devices"
lang: "en"
order_index: 1
title: "/dev directory"
description: "Learn how Linux exposes device interfaces and pseudo-devices through nodes under `/dev`."
meta_title: "/dev directory - Devices"
meta_description: "Discover the purpose of the /dev directory in Linux. This guide explains what the dev folder is, how to explore it with `ls /dev`, and the role of device files for system hardware."
meta_keywords: "dev in linux, /dev directory in linux, dev folder linux, ls /dev, dev command in linux, device files, device nodes, linux devices"
---

Linux exposes many kernel device interfaces through special filesystem objects called device nodes. They normally appear under `/dev`, alongside useful symbolic links and communication endpoints. Opening a device node connects an application to a kernel driver rather than to bytes stored in an ordinary file.

## Exploring `/dev`

List the directory without dereferencing or reading devices:

```bash
$ ls -l /dev
```

Entries can represent physical storage, terminals, input interfaces, logical devices, or kernel-provided pseudo-devices. Not every hardware component needs its own user-visible node, and one device can be represented through several links or interfaces.

The first character of a long listing identifies the filesystem object type. Character and block device nodes appear as `c` and `b`; later lessons examine these types and their major and minor numbers.

:::single-choice{#dev-directory-device-node-purpose}
What happens when a program opens a device node under `/dev`?

::option[It always reads an ordinary disk file containing a hardware copy.]{#dev-directory-ordinary-copy explanation="A device node is a special object and does not store a copy of the device's data as a regular file."}
::option[It accesses an interface implemented by a kernel driver.]{#dev-directory-kernel-interface .correct explanation="Device-node operations are routed through the node's device identity to kernel driver behavior."}
::option[It recompiles the driver source code for that device.]{#dev-directory-recompile-driver explanation="Opening an interface does not invoke a compiler or rebuild kernel modules."}
:::

## Pseudo-Devices

Some nodes provide kernel services without corresponding to physical hardware. `/dev/null` accepts and discards written data:

```bash
$ command > /dev/null
```

Other familiar examples include `/dev/zero`, which produces zero bytes, and `/dev/urandom`, which provides random bytes through the kernel random subsystem. Each has specific semantics; do not infer behavior only from its filename.

:::single-choice{#dev-directory-null-behavior}
What does `/dev/null` do with data written to it?

::option[It stores the data until the next reboot.]{#dev-directory-null-temporary-storage explanation="The null device is a sink and does not act as temporary storage."}
::option[It sends the data to every logged-in terminal.]{#dev-directory-null-broadcast explanation="Terminal broadcasting is unrelated to the null pseudo-device."}
::option[It discards the data.]{#dev-directory-null-discards .correct explanation="The null device accepts writes without preserving their contents."}
:::

## Dynamic Device Management

On modern Linux systems, the kernel-backed `devtmpfs` can populate basic device nodes as devices appear. A user-space device manager such as `udev` processes events, applies permissions and ownership, and creates useful symbolic links or policy-driven names. Exact responsibilities vary by system.

Stable links such as entries under `/dev/disk/by-id/` or `/dev/disk/by-uuid/` can be safer in configuration than detection-order names such as `/dev/sda`, which can change when hardware topology or discovery order changes.

:::single-choice{#dev-directory-persistent-link}
Why might an administrator prefer `/dev/disk/by-id/...` over `/dev/sda` in configuration?

::option[The identifier-based link is less dependent on device discovery order.]{#dev-directory-stable-identifier .correct explanation="Persistent links are derived from device properties instead of a letter assigned by enumeration order."}
::option[The link automatically backs up every block on the device.]{#dev-directory-link-backup explanation="A symbolic link names the same device and does not create backup data."}
::option[The link bypasses all permissions on the target device.]{#dev-directory-link-permissions explanation="Opening through a symbolic link still reaches the target device and its access controls."}
:::

## Interacting Safely

Standard tools can open device nodes, but that does not make arbitrary reads and writes safe. Reading can expose sensitive input or storage; writing to a disk, terminal, or firmware interface can corrupt data or disrupt users. Device-node permissions, groups, ACLs, capabilities, and service mediation restrict access for this reason.

Use read-only discovery tools first, confirm the exact node and device identity, and follow device-specific documentation. Never experiment by redirecting data into an unfamiliar `/dev` entry on a system you care about.

:::single-choice{#dev-directory-direct-write-risk}
Why should you avoid writing arbitrary data to an unfamiliar device node?

::option[Every device node is guaranteed to be a harmless text file.]{#dev-directory-harmless-text explanation="Device nodes are specifically not ordinary text files."}
::option[The operation can directly affect hardware, storage, or another kernel interface.]{#dev-directory-write-impact .correct explanation="Device writes invoke driver-defined operations and can cause destructive or disruptive effects."}
::option[Linux converts every device write into a read-only listing.]{#dev-directory-write-listing explanation="The driver decides write semantics; the kernel does not universally convert writes to listings."}
:::

Use [Explore Hardware Devices in Linux](https://labex.io/labs/comptia-explore-hardware-devices-in-linux-590861) for read-only inspection in a controlled environment.

## Summary

You can now describe `/dev` as a set of live kernel-facing interfaces.

1. Distinguish device nodes from ordinary files.
2. Recognize pseudo-devices such as `/dev/null`.
3. Relate dynamic nodes and persistent links to device management.
4. Treat direct device access as interface-specific and potentially destructive.
