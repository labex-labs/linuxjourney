---
lesson_id: "sysfs"
course_id: "devices"
lang: "en"
order_index: 4
title: "sysfs"
description: "Learn how sysfs exposes the Linux kernel's live device, driver, bus, and class model under `/sys`."
meta_title: "sysfs - Devices"
meta_description: "Explore what sysfs is and its role in the Linux sys system. This guide explains the linux /sys directory, a virtual filesystem for device information, and contrasts it with /dev."
meta_keywords: "sysfs, what is sysfs, /sys, linux /sys, linux sys, sys system, virtual filesystem, linux devices, /dev"
---

`sysfs` is a virtual filesystem normally mounted at `/sys`. It represents kernel objects and their relationships through directories, symbolic links, and small attribute files. Device-discovery tools and managers use it to understand the kernel's current device model.

## Navigating the Device Model

Important top-level views include:

- `/sys/devices/`: the physical and logical device hierarchy
- `/sys/class/`: devices grouped by functional class, such as block or network
- `/sys/bus/`: buses, their devices, and drivers
- `/sys/block/`: a convenient view of block devices
- `/sys/dev/`: links indexed by character or block major and minor numbers

Many entries outside `/sys/devices` are symbolic links into the canonical hierarchy. Resolve a link with `readlink -f` when you need the actual parent path:

```bash
$ readlink -f /sys/class/block/sda
```

The example name may not exist on systems using other storage interfaces.

:::single-choice{#sysfs-canonical-device-tree}
Which sysfs subtree contains the kernel's primary device hierarchy?

::option[`/sys/passwords/`]{#sysfs-passwords-tree explanation="Sysfs is not a repository for user authentication secrets."}
::option[`/sys/devices/`]{#sysfs-devices-tree .correct explanation="The devices subtree represents device parent-child topology; class and bus views link into it."}
::option[`/sys/packages/`]{#sysfs-packages-tree explanation="Installed package state is maintained by distribution package tools, not this sysfs path."}
:::

## Reading Attributes

Attribute files expose individual values or controls. For a block device, examples can include:

```bash
$ cat /sys/class/block/sda/dev
8:0
$ cat /sys/class/block/sda/ro
0
$ cat /sys/class/block/sda/size
1953525168
```

`dev` reports the major and minor device numbers. `ro` reports the block device's read-only flag. For Linux block devices, `size` is conventionally expressed in 512-byte sectors, regardless of the device's physical sector size. Always consult the kernel ABI documentation for a specific attribute's units and meaning.

:::single-choice{#sysfs-dev-attribute}
What does a block device's sysfs `dev` attribute normally contain?

::option[Every file currently stored on the device.]{#sysfs-file-list explanation="A filesystem directory tree is not embedded in this small device attribute."}
::option[The package name that installed the hardware.]{#sysfs-package-name explanation="Hardware is not installed as a package identified by the `dev` attribute."}
::option[Its major and minor device numbers.]{#sysfs-major-minor .correct explanation="The attribute connects the sysfs object to the corresponding block device identity."}
:::

## Relating `/sys` and `/dev`

`/dev` contains nodes applications open for device I/O. `/sys` exposes object relationships, properties, status, and selected controls. A block node such as `/dev/sda` can be matched to `/sys/dev/block/8:0`, which resolves to the relevant sysfs object.

The two interfaces complement each other. Neither contains a complete standalone inventory of all hardware facts, and a device can disappear while it is being inspected.

:::single-choice{#sysfs-versus-dev}
Which statement correctly distinguishes `/sys` from `/dev`?

::option[`/sys` stores user documents; `/dev` stores package archives.]{#sysfs-dev-user-files explanation="Neither directory has those ordinary data-storage roles."}
::option[`/sys` exposes kernel-object attributes; `/dev` provides device nodes for I/O.]{#sysfs-dev-distinction .correct explanation="Sysfs models objects and controls, while device nodes route operations to character or block drivers."}
::option[Both are static lists created once during installation.]{#sysfs-dev-static explanation="Their visible state changes as devices and kernel objects appear or disappear."}
:::

## Writing Attributes Safely

Some sysfs attributes are writable and can change power state, driver binding, queue behavior, device authorization, LEDs, or other live controls. A successful text write can have immediate hardware or service effects; it is not equivalent to editing a persistent configuration file.

Read the documented ABI and current value, identify how the setting should be made persistent, and test only on an authorized system. Never recursively edit permissions or write guessed values across `/sys`.

:::single-choice{#sysfs-write-risk}
Why can writing to a sysfs attribute be operationally significant?

::option[Every write creates an ordinary backup copy on disk.]{#sysfs-backup-copy explanation="Sysfs is virtual and does not provide automatic backups of control changes."}
::option[Sysfs ignores all writes even when an attribute is writable.]{#sysfs-ignore-writes explanation="Writable attributes exist specifically to accept supported control values."}
::option[The write can invoke a live kernel or driver control.]{#sysfs-live-control .correct explanation="Writable attributes are active interfaces and may alter device behavior immediately."}
:::

Use [Explore Hardware Devices in Linux](https://labex.io/labs/comptia-explore-hardware-devices-in-linux-590861) to navigate sysfs read-only and correlate it with device nodes.

## Summary

You can now use sysfs as a structured view of live kernel objects.

1. Navigate device, class, bus, block, and device-number views.
2. Read one documented attribute at a time with correct units.
3. Correlate sysfs objects with `/dev` nodes.
4. Treat writable attributes as live control interfaces.
