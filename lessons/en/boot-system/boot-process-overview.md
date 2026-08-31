---
lesson_id: "boot-process-overview"
course_id: "boot-system"
lang: "en"
order_index: 1
title: "Boot Process Overview"
description: "Learn the major handoffs from platform firmware through the kernel to the first user-space process."
meta_title: "Boot Process Overview - Boot the System"
meta_description: "A clear overview of the Linux boot process, detailing the four key stages: BIOS, bootloader, kernel, and init. Learn about the complete booting process of the Linux operating system, from power-on to the login prompt."
meta_keywords: "Linux boot process, boot process linux, booting process linux, booting process of linux operating system, BIOS, bootloader, kernel, init, Linux tutorial, Linux guide, beginner"
---

Boot is a chain of trust and control transfers that turns platform reset into a running user-space environment. A common PC path can be summarized as firmware, boot manager or loader, kernel with optional early user space, and the PID 1 init system. Architectures, virtual machines, embedded systems, and containers can use different paths.

## Firmware Initialization

Platform firmware initializes enough CPU, memory, and device state to choose a boot target. Traditional PCs use BIOS conventions; current PCs commonly use UEFI. Firmware settings, boot order, platform verification, and Secure Boot policy can determine which next-stage executable is allowed to run.

Firmware does not necessarily understand the installed Linux root filesystem. It locates a boot path according to its interface—for example, BIOS boot code on a selected disk or a UEFI boot entry pointing to an EFI executable on an EFI System Partition.

:::single-choice{#boot-overview-first-stage}
Which component begins platform initialization after reset on a typical PC?

::option[The user's interactive shell.]{#boot-overview-shell explanation="A shell is started much later by user-space services or login processing."}
::option[Platform firmware such as BIOS or UEFI.]{#boot-overview-firmware .correct explanation="Firmware establishes early hardware state and selects the next boot target before Linux runs."}
::option[The filesystem repair utility.]{#boot-overview-fsck explanation="A checker can participate later under boot policy but is not the initial firmware stage."}
:::

## Boot Loader or Boot Manager

A loader such as GRUB can present entries, load a selected Linux kernel and initial RAM filesystem into memory, construct the kernel command line, and transfer control. UEFI can also load a kernel built as an EFI executable directly, so a separate multi-stage loader is common rather than universal.

The selected artifacts must agree: kernel version, initramfs content, root identifier, security signatures, and command-line options all affect whether the next handoff succeeds.

:::single-choice{#boot-overview-loader-role}
What is a common responsibility of a Linux boot loader?

::option[Load a selected kernel and pass its command line.]{#boot-overview-load-kernel .correct explanation="The loader prepares the kernel image and parameters, often together with an initramfs."}
::option[Create all user accounts from scratch on every boot.]{#boot-overview-create-users explanation="Persistent account databases are user-space configuration and not recreated by the loader."}
::option[Schedule every application process after login.]{#boot-overview-schedule-apps explanation="CPU scheduling is a running-kernel responsibility."}
:::

## Kernel and Early User Space

The kernel decompresses or relocates as required, initializes core subsystems, parses its command line, and discovers available hardware. An initramfs can supply modules and early tools needed for storage discovery, RAID, encryption, LVM, networking, or other work required to assemble the real root filesystem.

After the intended root is available, early user space switches to it and the kernel executes the configured first user-space program. Details such as who performs filesystem checks or read-write remounting belong to the distribution's boot design rather than one universal sequence.

:::single-choice{#boot-overview-initramfs-purpose}
Why might a system use an initramfs?

::option[To preserve every user's desktop session permanently in firmware.]{#boot-overview-desktop-firmware explanation="An initramfs is a boot-time filesystem image, not firmware session storage."}
::option[To provide early tools and drivers needed to reach the real root filesystem.]{#boot-overview-early-root-tools .correct explanation="Early user space can assemble encrypted, logical, networked, or driver-dependent root storage."}
::option[To replace the kernel's process scheduler after login.]{#boot-overview-replace-scheduler explanation="The kernel retains scheduling responsibility throughout operation."}
:::

## PID 1 and System Readiness

The first user-space process receives PID 1. On many distributions it is systemd; other systems use sysvinit, OpenRC, runit, BusyBox init, or a specialized program. PID 1 establishes the user-space service environment, reaps orphaned children, and handles shutdown responsibilities.

Reaching PID 1 does not mean the system is fully ready. Services can still be starting, storage can be mounting, network configuration can be pending, and a graphical or console login is only one possible target state.

:::single-choice{#boot-overview-final-stage}
What begins the main user-space initialization stage?

::option[Creation of the disk's protective MBR on every boot.]{#boot-overview-create-mbr explanation="Partition-table creation is not a normal recurring boot stage."}
::option[Deletion of all kernel command-line parameters.]{#boot-overview-delete-command-line explanation="The kernel parses and exposes its command line rather than requiring such deletion."}
::option[Execution of the PID 1 init program.]{#boot-overview-pid-one .correct explanation="After root setup, the first user-space process starts or supervises the services needed for the configured system state."}
:::

The [Customize the GRUB2 Boot Menu](https://labex.io/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859) lab demonstrates one loader configuration path. Apply changes only in a recovery-capable lab system.

## Summary

You can now trace the major Linux boot handoffs without treating them as universal implementation details.

1. Start with firmware initialization and target selection.
2. Relate the loader to kernel, initramfs, and command-line selection.
3. Use early user space to understand complex root assembly.
4. Treat PID 1 as the beginning of service initialization, not proof of readiness.
