---
lesson_id: "boot-process-bootloader"
course_id: "boot-system"
lang: "en"
order_index: 3
title: "Boot Process: Bootloader"
description: "Learn how a boot loader selects Linux artifacts, constructs the kernel command line, and transfers control."
meta_title: "Boot Process: Bootloader - Boot the System"
meta_description: "A guide to the bootloader in Linux. Learn what a Linux boot loader is, its primary functions, and how GRUB uses kernel parameters like initrd and root to start the system."
meta_keywords: "linux boot loader, bootloader in linux, linux bootloader, grub, what is bootloader in linux, kernel parameters, initrd, root filesystem, linux boot process"
---

A boot loader bridges firmware discovery and kernel execution. GRUB is common on Linux PCs, but systemd-boot, U-Boot, firmware loading of an EFI-stub kernel, and other designs implement different parts of this role.

## Selecting Boot Artifacts

A loader entry can identify:

- a Linux kernel image
- an optional initramfs or legacy initrd image
- a kernel command line
- platform-specific metadata or another operating system's loader

GRUB can present multiple kernels and recovery entries. A fallback kernel is useful only when its matching modules and initramfs remain available and tested. The loader reads files through its supported storage and filesystem modules; it does not rely on the not-yet-running Linux VFS.

:::single-choice{#bootloader-primary-handoff}
What does a Linux boot loader normally transfer control to?

::option[An interactive user shell with every service already running.]{#bootloader-user-shell explanation="User-space shells appear only after the kernel and init system start."}
::option[The selected kernel image after loading required boot artifacts.]{#bootloader-selected-kernel .correct explanation="The loader prepares the kernel, parameters, and often an initramfs before executing the kernel entry point."}
::option[The filesystem package manager for dependency resolution.]{#bootloader-package-manager explanation="Package management is not the next processor-control stage in boot."}
:::

## Kernel Command-Line Parameters

The loader passes a text command line that the kernel and early user space parse. Common examples include:

- `root=...` to identify the intended root filesystem or early-user-space source specification
- `ro` or `rw` to request an initial root mount mode
- `quiet` to reduce kernel console messages
- `init=...` to request a different first user-space program for specialized recovery
- distribution-specific `rd.*` parameters interpreted by initramfs tooling

`initrd` is normally a loader directive naming an image, not a generic kernel parameter. `BOOT_IMAGE=` can appear in a command line produced by some GRUB configurations, but it is not the mechanism that loads the kernel.

Inspect the command line used for the current boot with:

```bash
$ cat /proc/cmdline
```

:::single-choice{#bootloader-root-parameter}
What is the purpose of the `root=` kernel command-line parameter?

::option[Identify the root filesystem that boot must eventually use.]{#bootloader-root-filesystem .correct explanation="The kernel or initramfs interprets the value as part of locating and assembling the real root."}
::option[Set the login password for the root account.]{#bootloader-root-password explanation="Authentication secrets must not be passed as ordinary kernel command-line text."}
::option[Rename PID 1 to the word `root`.]{#bootloader-root-pid explanation="Process naming is unrelated to this storage parameter."}
:::

:::single-choice{#bootloader-quiet-parameter}
What does the `quiet` parameter normally request?

::option[Read-only access to every mounted filesystem.]{#bootloader-quiet-readonly explanation="Initial root write policy uses parameters such as `ro`, not `quiet`."}
::option[Reduce kernel messages printed during boot.]{#bootloader-quiet-console .correct explanation="It suppresses many informational messages but does not guarantee silence from every boot component."}
::option[Disabling every hardware cooling fan.]{#bootloader-quiet-fans explanation="The parameter concerns message verbosity rather than acoustic hardware control."}
:::

## Temporary Editing and Recovery

GRUB commonly lets an authorized console user edit an entry for one boot, often through an edit key shown by the menu. This is useful for removing `quiet`, selecting recovery parameters, or correcting a bad root identifier. Interface and authorization vary, especially with Secure Boot and password-protected GRUB configurations.

Command-line parameters can expose sensitive text through `/proc/cmdline`, boot logs, and crash reports. They can also weaken security or make the system unbootable. Never place secrets there, and preserve a known-good entry and console recovery path.

:::single-choice{#bootloader-temporary-edit}
What is a typical property of editing a GRUB menu entry interactively for one boot?

::option[It automatically rewrites every installed kernel image.]{#bootloader-rewrites-kernels explanation="Changing command text does not modify kernel binaries."}
::option[It permanently disables firmware verification on all disks.]{#bootloader-disables-firmware explanation="Firmware policy is separate and is not universally changed by a one-entry edit."}
::option[The change applies to that boot unless separately saved in configuration.]{#bootloader-one-boot-change .correct explanation="Menu editing normally alters the in-memory entry rather than persistent source configuration."}
:::

## Persistent GRUB Configuration

Distributions commonly generate the final GRUB configuration from templates, defaults, scripts, and discovered kernels. Do not edit the generated `grub.cfg` directly unless the distribution explicitly documents that workflow; regeneration can overwrite it.

Make a scoped source change, run the distribution's documented regeneration command, inspect its output, and test while retaining an older known-good entry and bootable recovery media. The command and output path differ between Debian, Fedora, UEFI, and BIOS installations.

:::single-choice{#bootloader-generated-config}
Why is directly editing a generated `grub.cfg` usually unreliable?

::option[The file can never contain readable text.]{#bootloader-config-binary explanation="GRUB configuration is text, but generated ownership still matters."}
::option[GRUB reads only files in each user's home directory.]{#bootloader-grub-home explanation="Boot configuration is system-level and must be available before user home sessions."}
::option[A later regeneration can overwrite the manual change.]{#bootloader-regeneration-overwrites .correct explanation="Persistent settings generally belong in the distribution's configuration sources and generation workflow."}
:::

Use [Customize the GRUB2 Boot Menu](https://labex.io/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859) only in its recovery-capable lab environment.

## Summary

You can now separate loader directives from kernel command-line parameters.

1. Identify kernel, initramfs, command line, and alternate entries.
2. Use `root=`, `ro`, and `quiet` according to their actual roles.
3. Inspect the running boot's parameters through `/proc/cmdline`.
4. Treat interactive edits as temporary and security-sensitive.
5. Change persistent generated configuration through the distribution workflow.
