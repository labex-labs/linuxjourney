---
lesson_id: "boot-process-kernel"
course_id: "boot-system"
lang: "en"
order_index: 4
title: "Boot Process: Kernel"
description: "Learn how the kernel initializes hardware, runs initramfs early user space, reaches the real root, and starts PID 1."
meta_title: "Boot Process: Kernel - Boot the System"
meta_description: "Explore the Linux kernel boot process. Learn how initramfs loads drivers from a temporary filesystem to mount the final boot root partition. Understand the steps from kernel loading to executing init."
meta_keywords: "boot root, initramfs, kernel boot, boot partition, initramfs ubuntu, /etc/default/grub, Linux boot process, root filesystem, kernel initialization"
---

After control reaches the Linux kernel, it initializes memory management, scheduling, interrupts, built-in drivers, security frameworks, and other core subsystems. It parses the command line and prepares to start the first user-space process.

## Why Early User Space Exists

A simple root filesystem can sometimes be mounted using drivers built into the kernel. More complex systems need modules and tools before the real root can be reached. Examples include:

- storage-controller or filesystem modules
- encrypted root unlocking
- LVM or RAID assembly
- network configuration for a network root
- device discovery and persistent identifier resolution

An initramfs packages these components into an early user-space environment supplied alongside the kernel.

:::single-choice{#boot-kernel-initramfs-purpose} What problem does an initramfs commonly solve?

::option[It supplies early tools and modules needed before the real root is available.]{#boot-kernel-early-tools .correct explanation="Early user space can discover and assemble storage that the kernel cannot access using built-in support alone."}
::option[It stores every user's permanent home directory in firmware.]{#boot-kernel-home-firmware explanation="The archive is a boot artifact and not permanent user-data storage."}
::option[It replaces the Linux kernel after the first login.]{#boot-kernel-replace-kernel explanation="The kernel remains active while initramfs code runs in user space."}
:::

## Initramfs and Legacy Initrd

A modern initramfs is usually one or more cpio archives, often compressed, that the kernel unpacks into its initial root filesystem. The kernel executes an early `/init` program from that environment.

A legacy initrd is conceptually a filesystem image loaded into a RAM-backed block device and mounted. The terms are often used loosely in filenames and boot-loader commands, so inspect the actual tooling rather than inferring format from the word alone.

The initramfs must match the kernel and boot design. Missing modules, stale device identifiers, or omitted cryptographic and LVM tooling can make a newly installed kernel unbootable even when the kernel image itself is valid.

:::single-choice{#boot-kernel-initramfs-format} How is a modern initramfs commonly presented to the kernel?

::option[As an interactive package repository over HTTP only.]{#boot-kernel-http-repository explanation="Network access can be configured in early user space, but it is not the defining initramfs format."}
::option[As a cpio-based archive unpacked into the initial root.]{#boot-kernel-cpio-archive .correct explanation="The kernel expands the archive and executes its early user-space initialization program."}
::option[As the disk's GPT backup header.]{#boot-kernel-gpt-header explanation="Partition-table redundancy is independent of the early user-space archive."}
:::

## Reaching the Real Root

Early user space interprets parameters such as `root=`, waits for the necessary devices, activates storage layers, and mounts the intended root filesystem. It then uses a root-switch operation to make that filesystem the new `/` and release the temporary early environment where possible.

The initial `ro` command-line request can support consistency checks and controlled startup, but the exact sequence is distribution-specific. Filesystem checks are user-space operations, and the initramfs or later init system can remount the root read-write when policy permits.

:::single-choice{#boot-kernel-root-switch} What happens after early user space successfully mounts the intended real root?

::option[The partition table is recreated on every disk.]{#boot-kernel-recreate-tables explanation="Root switching does not repartition storage."}
::option[The kernel exits and firmware resumes normal process scheduling.]{#boot-kernel-firmware-schedules explanation="The Linux kernel remains responsible for processes and hardware after the handoff."}
::option[Boot switches the root view to that filesystem and continues user-space startup.]{#boot-kernel-switch-root .correct explanation="The temporary early root hands off to the installed system's root hierarchy."}
:::

## Starting PID 1

The kernel executes the configured init program, normally reached through a path such as `/sbin/init` or selected with `init=`. That process receives PID 1 and takes responsibility for the main user-space service environment.

If no usable init program can be executed, the kernel cannot proceed to a normal user-space system and typically reports a boot failure or panic. Debug the earliest failing layer: kernel and command line, initramfs content, root discovery, root mount, or PID 1 execution.

:::single-choice{#boot-kernel-pid-one} What is the kernel's final major handoff in this simplified boot stage?

::option[Execute the first user-space program as PID 1.]{#boot-kernel-exec-init .correct explanation="PID 1 then brings up services and the configured system state."}
::option[Turn `/proc` into a persistent package database.]{#boot-kernel-proc-package explanation="Procfs remains a runtime kernel interface."}
::option[Assign every later process the same PID.]{#boot-kernel-same-pid explanation="Each live process receives its own PID within a namespace."}
:::

## Summary

You can now trace kernel boot through early user space to PID 1.

1. Separate built-in kernel initialization from loadable early modules.
2. Relate initramfs to a cpio-based temporary root and `/init`.
3. Follow storage assembly and the switch to the real root.
4. Identify execution of PID 1 as the user-space handoff.
