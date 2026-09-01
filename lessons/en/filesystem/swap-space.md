---
lesson_id: "swap-space"
course_id: "filesystem"
lang: "en"
order_index: 8
title: "swap"
description: "Learn how Linux uses, initializes, activates, sizes, and safely deactivates swap space."
meta_title: "swap - The Filesystem"
meta_description: "Learn about Linux swap space, how it works, and how to create and manage swap partitions. Optimize your system's memory usage with this guide!"
meta_keywords: "Linux swap, mkswap, swapon, swapoff, /etc/fstab, virtual memory, Linux beginner, Linux tutorial"
---

Linux can move selected anonymous memory pages between RAM and swap-backed storage. This can retain inactive memory while freeing RAM for active workloads and filesystem cache, but storage is much slower than RAM. Swap is a capacity and memory-management tool, not a substitute for sufficient memory or an application memory limit.

## How Swap Participates in Memory Management

The kernel can use swap before RAM is completely exhausted, depending on workload, memory pressure, cgroups, and tunables such as swappiness. File-backed clean pages can often be discarded and reread from their files, while anonymous pages need swap or must remain in RAM.

Heavy sustained swapping can cause severe latency or thrashing. Diagnose memory demand, working sets, pressure, and application limits rather than treating a larger swap area as a universal performance fix.

:::single-choice{#swap-space-anonymous-pages} Which memory is a primary candidate for storage in swap?

::option[Every executable file installed under `/usr`.]{#swap-space-installed-files explanation="Installed files remain in their filesystems; clean mapped pages can be reread from there."}
::option[Inactive anonymous memory pages.]{#swap-space-anonymous-memory .correct explanation="Anonymous pages lack an ordinary backing file from which they can simply be reread."}
::option[The disk's partition table entries.]{#swap-space-partition-table explanation="Partition metadata remains on the block device and is not process memory swapped from RAM."}
:::

## Inspecting Active Swap

Use read-only commands first:

```bash
$ swapon --show
$ cat /proc/swaps
$ free -h
```

These show configured active swap and aggregate memory figures. A nonzero “used” value is not automatically a problem; correlate it with swap-in/out rates, memory pressure, latency, and workload behavior.

:::single-choice{#swap-space-show-active} Which command lists active swap areas in a structured view?

::option[`swapon --show`]{#swap-space-swapon-show .correct explanation="The show mode reports active swap files or devices and their size, use, and priority where available."}
::option[`mkswap --all`]{#swap-space-mkswap-all explanation="Mkswap initializes swap signatures and is not the read-only active listing command."}
::option[`mkfs -t swap`]{#swap-space-mkfs-swap explanation="The standard initialization tool is `mkswap`, and formatting is not a status query."}
:::

## Initializing and Activating a Swap Device

`mkswap` writes a swap signature and destroys the target's previous usable metadata. Practice only on a verified disposable target:

```bash
$ sudo mkswap /dev/VERIFIED-SWAP-TARGET
$ sudo swapon /dev/VERIFIED-SWAP-TARGET
```

Before `mkswap`, verify model, serial, size, persistent identity, existing signatures, mounts, RAID, LVM, encryption, and backups just as you would before `mkfs`. After activation, confirm the exact source with `swapon --show`.

For persistence, use the swap UUID in `/etc/fstab` with type and options appropriate to local policy:

```text
UUID=VERIFIED-SWAP-UUID none swap sw 0 0
```

:::single-choice{#swap-space-enable-command} Which command activates an initialized swap area?

::option[`swapon`]{#swap-space-command-swapon .correct explanation="Swapon adds a valid swap device or file to the kernel's active swap set."}
::option[`mkswap`]{#swap-space-command-mkswap explanation="Mkswap initializes the signature but does not itself activate the area."}
::option[`mount`]{#swap-space-command-mount explanation="Swap is activated through the swap subsystem rather than mounted as a directory filesystem."}
:::

## Swap Files and Other Back Ends

A swap file can provide flexible capacity without repartitioning, but creation requirements are filesystem-specific. The file must have restrictive permissions, suitable allocation with no unsupported holes or copy-on-write behavior, a swap signature, and activation. Follow the filesystem and distribution documentation instead of copying a generic `fallocate` recipe everywhere.

Compressed RAM devices such as zram can provide another swap tier with different CPU and capacity tradeoffs. Encrypted swap can protect pages at rest, while hibernation requires a resume configuration and sufficient suitable storage. These goals affect sizing and design.

There is no universal rule that swap must equal twice RAM. Size it from workload peaks, desired failure behavior, hibernation needs, storage latency and endurance, crash-dump design, and operational monitoring.

:::single-choice{#swap-space-sizing-rule} Which is the best basis for swap sizing?

::option[Always exactly twice the installed RAM.]{#swap-space-twice-ram explanation="That historical heuristic is not suitable for every workload or modern memory size."}
::option[Measured workload needs, hibernation goals, and failure policy.]{#swap-space-sizing-requirements .correct explanation="System purpose and observed memory behavior matter more than a fixed RAM multiplier."}
::option[Always zero whenever the system has an SSD.]{#swap-space-zero-ssd explanation="Storage type alone does not determine memory-pressure or hibernation requirements."}
:::

## Deactivating Swap Safely

Deactivate a specific verified area with:

```bash
$ sudo swapoff /dev/VERIFIED-SWAP-TARGET
```

The kernel must move its resident swapped pages elsewhere. If RAM and remaining swap cannot accommodate them, the operation can fail or create dangerous memory pressure. Stop or constrain workloads first, monitor memory, remove the persistent fstab entry only after verifying the correct target, and confirm deactivation with `swapon --show` before repurposing storage.

:::single-choice{#swap-space-swapoff-capacity} Why can `swapoff` fail or endanger a heavily loaded system?

::option[Swapoff always reformats every RAM module.]{#swap-space-formats-ram explanation="It changes active swap configuration and does not format physical memory hardware."}
::option[Pages in that area need capacity in RAM or other swap.]{#swap-space-pages-need-capacity .correct explanation="Deactivation requires relocating live swapped pages while the system continues operating."}
::option[An inactive swap area must remain mounted at `/swap`.]{#swap-space-mounted-path explanation="Swap areas are not directory-mounted filesystems."}
:::

Use [Create and Activate a Swap File in Linux](https://labex.io/labs/comptia-create-and-activate-a-swap-file-in-linux-590858) in a controlled environment to practice file permissions, activation, and persistence.

## Summary

You can now treat swap as an explicit memory-management resource.

1. Relate swap primarily to anonymous memory under pressure.
2. Inspect active swap and workload behavior before changing capacity.
3. Initialize only a verified disposable target, then activate with `swapon`.
4. Size and secure swap according to workload and hibernation requirements.
5. Ensure relocation capacity before using `swapoff`.
