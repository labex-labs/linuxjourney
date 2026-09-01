---
lesson_id: "device-names"
course_id: "devices"
lang: "en"
order_index: 3
title: "Device Names"
description: "Learn how Linux names common storage devices, partitions, logical devices, and persistent device links."
meta_title: "Device Names - Devices"
meta_description: "Explore common Linux device names for storage and peripherals. This guide explains the naming convention for SCSI disks (like sda), what sda stands for, and pseudo-devices like /dev/null."
meta_keywords: "linux device names, linux device name, what does sda stand for, sd element name, what would commonly be the device name for the first partition on the second scsi disk, /dev, SCSI devices, pseudo devices, PATA devices"
---

Linux device names reflect the kernel subsystem and driver presenting an interface, not always the physical connector printed on the hardware. Learn the common patterns, but discover the actual mapping on the current system before making storage changes.

## SCSI-Layer Disk Names

Disks presented through the SCSI disk layer commonly use `sd` names. This includes many SCSI, SATA, USB-storage, and virtual disks:

- `/dev/sda`: one whole disk
- `/dev/sdb`: another whole disk
- `/dev/sda3`: partition 3 on `/dev/sda`
- `/dev/sdb1`: partition 1 on `/dev/sdb`

Letters reflect enumeration, not a durable identity. Adding a controller, changing firmware order, or attaching a device can change which disk receives a particular letter.

:::single-choice{#device-names-sdb-first-partition} Under the `sd` naming pattern, which path denotes partition 1 on `/dev/sdb`?

::option[`/dev/sda2`]{#device-names-sda-two explanation="This denotes partition 2 on the disk currently named `/dev/sda`."}
::option[`/dev/sdbp1`]{#device-names-sdb-p-one explanation="The `p` separator is used by patterns whose base name already ends in a digit, not ordinary `sd` names."}
::option[`/dev/sdb1`]{#device-names-sdb-one .correct explanation="For `sd` disks, the partition number is appended directly to the whole-disk name."}
:::

## Names That End in Digits

Some whole-device names already contain digits, so their partition names use `p` as a separator:

- `/dev/nvme0n1`: NVMe namespace 1 on controller 0
- `/dev/nvme0n1p2`: partition 2 on that namespace
- `/dev/mmcblk0`: an MMC block device
- `/dev/mmcblk0p1`: partition 1 on that device

NVMe devices are not normally named `/dev/sdX`; they use the NVMe subsystem's naming convention.

:::single-choice{#device-names-nvme-partition} Which path denotes partition 2 of `/dev/nvme0n1`?

::option[`/dev/nvme0n1p2`]{#device-names-nvme-p-two .correct explanation="NVMe partition names insert `p` before the partition number."}
::option[`/dev/nvme0n12`]{#device-names-nvme-no-p explanation="Without a separator, the trailing digits would be ambiguous with the namespace number."}
::option[`/dev/sda2`]{#device-names-nvme-sda explanation="That is an `sd`-layer disk partition and does not name the specified NVMe namespace."}
:::

## Logical and Virtual Block Devices

Linux also creates block devices that do not map one-to-one to a physical disk:

- `/dev/dm-N` for device-mapper devices, often accompanied by descriptive links under `/dev/mapper/`
- `/dev/mdN` for Linux software RAID arrays
- `/dev/loopN` for regular files attached as loop block devices

Partitions, encryption layers, RAID, logical volumes, and filesystems form a stack. Use tools such as `lsblk` to see parent-child relationships instead of inferring the stack from a name alone.

:::single-choice{#device-names-device-mapper-link} Which location commonly provides descriptive links for device-mapper devices?

::option[`/dev/mapper/`]{#device-names-mapper-directory .correct explanation="Device-mapper users such as LVM and disk encryption commonly expose named links in this directory."}
::option[`/dev/null/`]{#device-names-null-directory explanation="`/dev/null` is a character device, not a directory of mapped block devices."}
::option[`/proc/partitions/mapper/`]{#device-names-proc-mapper explanation="This is not the normal path for device-mapper name links."}
:::

## Persistent Storage Links

User-space device management creates links under `/dev/disk/`, commonly grouped as:

- `by-id` for hardware or transport identifiers
- `by-uuid` for filesystem UUIDs
- `by-label` for filesystem labels
- `by-partuuid` for partition-table UUIDs
- `by-path` for topology-dependent paths

Choose an identifier that matches what must remain stable. A filesystem UUID identifies a filesystem, not necessarily the physical disk beneath it. Cloning a filesystem can duplicate its UUID, so verify uniqueness before relying on it.

:::single-choice{#device-names-persistent-config} Why are `/dev/disk/by-id/` links often preferable to `/dev/sdX` in device-specific configuration?

::option[They make destructive writes automatically reversible.]{#device-names-by-id-reversible explanation="A stable name does not provide snapshots, backups, or write protection."}
::option[They convert a block device into a regular file.]{#device-names-by-id-regular explanation="The entry is a symbolic link that still resolves to a block device node."}
::option[They are derived from device identity rather than current enumeration order.]{#device-names-by-id-stable .correct explanation="The link target can change while the identity-based link remains associated with the same recognized device."}
:::

## Pseudo-Device Names

Names such as `/dev/null`, `/dev/zero`, and `/dev/urandom` describe kernel pseudo-devices rather than physical storage. `/dev/null` discards writes and returns end-of-file on reads; `/dev/zero` supplies zero bytes; `/dev/urandom` supplies bytes from the kernel random-number generator.

:::single-choice{#device-names-zero-read} What does reading from `/dev/zero` produce?

::option[A listing of unused storage devices.]{#device-names-zero-storage-list explanation="It is a byte-producing character device, not a discovery command."}
::option[A stream of zero-valued bytes.]{#device-names-zero-bytes .correct explanation="The zero pseudo-device returns null bytes for requested reads."}
::option[End-of-file immediately, like reading `/dev/null`.]{#device-names-zero-eof explanation="`/dev/zero` continues producing bytes, while `/dev/null` reads return end-of-file."}
:::

Use [Explore Hardware Devices in Linux](https://labex.io/labs/comptia-explore-hardware-devices-in-linux-590861) to compare names, persistent links, and `lsblk` relationships before attempting partition work.

## Summary

You can now decode common Linux storage names without treating them as permanent identity.

1. Read `sdXNUMBER` as an `sd` disk partition.
2. Use `pNUMBER` when the whole-device name already ends in a digit.
3. Recognize logical devices such as device mapper, RAID, and loop devices.
4. Prefer persistent links chosen for the identity you need.
5. Distinguish storage names from kernel pseudo-devices.
