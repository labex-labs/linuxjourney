---
lesson_id: "kernel-location"
course_id: "kernel"
lang: "en"
order_index: 5
title: "Kernel Location"
description: "Learn where distributions place kernel images, initramfs files, configuration, symbols, and versioned modules."
meta_title: "Kernel Location - Kernel"
meta_description: "Discover where the kernel is stored in Linux. This guide explains the Linux kernel location in the /boot directory, detailing key files like vmlinuz and initrd."
meta_keywords: "linux kernel location, where is the kernel, kernel location, where is the kernel located, where is the kernel stored in linux, vmlinuz, /boot directory"
---

Linux distributions commonly store bootable kernel artifacts under `/boot`, but UEFI and Boot Loader Specification layouts can also place artifacts on an EFI System Partition or extended boot partition mounted at paths such as `/boot`, `/boot/efi`, or `/efi`. Inspect mounts and loader configuration rather than assuming one universal path.

## Versioned Files under `/boot`

A traditional distribution layout can contain:

- `vmlinuz-KERNEL_RELEASE`: a bootable Linux kernel image
- `initrd.img-KERNEL_RELEASE` or `initramfs-KERNEL_RELEASE.img`: early user-space image
- `config-KERNEL_RELEASE`: configuration used for that packaged kernel build
- `System.map-KERNEL_RELEASE`: symbol-address map from the kernel build

Names vary. An `initrd`-named file on a modern distribution often contains an initramfs archive. The `vmlinuz` naming convention does not tell you the exact internal compression or platform boot format; inspect it with distribution tooling.

:::single-choice{#kernel-location-vmlinuz} What does a versioned `vmlinuz-*` file normally contain?

::option[A bootable Linux kernel image.]{#kernel-location-kernel-image .correct explanation="The boot loader or firmware loads this architecture-specific kernel artifact."}
::option[Every loadable module for all installed kernels.]{#kernel-location-all-modules explanation="Modules are stored separately in a release-specific module tree."}
::option[The user's shell history from the previous boot.]{#kernel-location-shell-history explanation="Boot kernel images do not contain personal command history."}
:::

## Initial RAM Filesystem and Build Metadata

The initramfs must contain the early modules and tools required by its matching kernel and root-storage design. A filename match is not enough; stale or failed generation can still produce an unusable boot entry.

`config-*` helps explain which features were built in, modular, or omitted. `System.map-*` can help symbolization and debugging, but address randomization, split debug information, and distribution tooling affect how it is used. These files are supporting artifacts, not alternate kernels.

:::single-choice{#kernel-location-initramfs-match} Why is an initramfs tied to a particular kernel release and system configuration?

::option[It stores the permanent contents of every mounted filesystem.]{#kernel-location-all-filesystems explanation="An initramfs is a small early boot environment, not a full system backup."}
::option[It assigns new UIDs to users during every boot.]{#kernel-location-user-ids explanation="Account identity management is outside its normal role."}
::option[It contains early modules and tools needed by that boot path.]{#kernel-location-early-modules .correct explanation="Module ABI and required storage assembly components must agree with the selected kernel."}
:::

## Versioned Kernel Modules

Loadable modules for the running release commonly reside below:

```bash
$ printf '/lib/modules/%s\n' "$(uname -r)"
```

On merged filesystem layouts this can resolve into `/usr/lib/modules/KERNEL_RELEASE`. Each installed kernel needs a compatible module tree and dependency indexes. `modprobe` uses release-specific metadata rather than searching arbitrary `.ko` files across the disk.

:::single-choice{#kernel-location-module-tree} Which directory conventionally holds modules for the running kernel release?

::option[`/home/modules/current/`]{#kernel-location-home-modules explanation="User home directories are not the standard system module tree."}
::option[`/lib/modules/$(uname -r)/`]{#kernel-location-lib-modules .correct explanation="The release component separates module ABI and dependency data for each installed kernel."}
::option[`/proc/modules/files/`]{#kernel-location-proc-files explanation="`/proc/modules` reports loaded modules and is not a directory of module binaries."}
:::

## Unified Kernel Images and Firmware Paths

A Unified Kernel Image, or UKI, is one signed EFI executable that can bundle a kernel, initrd, command line, and metadata. UKIs are commonly stored in an EFI-accessible boot location rather than represented by separate `vmlinuz` and initramfs files.

Therefore, an empty-looking traditional `/boot` layout does not prove that no kernel is installed. Use `findmnt`, the package database, boot-manager tools, and the loader's configuration to map the active artifacts.

:::single-choice{#kernel-location-uki} What can a Unified Kernel Image combine?

::option[All user home directories in a GPT header.]{#kernel-location-uki-homes explanation="A UKI is a boot executable, not a user-data container or partition table."}
::option[Every installed package into one shell script.]{#kernel-location-uki-packages explanation="It packages boot components rather than the complete operating system repository."}
::option[Kernel, initrd, command line, and metadata in an EFI executable.]{#kernel-location-uki-components .correct explanation="The combined artifact can participate in a signed UEFI boot workflow."}
:::

## Managing Space Safely

If the boot filesystem is full, first map mounted boot paths and query which package owns every artifact. Use the package manager's kernel cleanup workflow, preserve the running kernel and a known-good fallback, regenerate or inspect boot entries, and verify free space afterward.

Do not manually delete `vmlinuz`, initramfs, UKI, or module trees merely by age. A file can be the only bootable recovery entry even when it is not currently running.

## Summary

You can now map a kernel package to its boot and module artifacts.

1. Inspect actual `/boot` and EFI-related mounts.
2. Distinguish kernel image, initramfs, config, and symbol map.
3. Match module trees to the exact kernel release.
4. Account for Unified Kernel Images and distribution-specific layouts.
5. Reclaim boot space only through a verified package and fallback plan.
