---
lesson_id: "boot-process-bios"
course_id: "boot-system"
lang: "en"
order_index: 2
title: "Boot Process: BIOS"
description: "Learn how legacy BIOS and modern UEFI firmware locate and authorize the next boot stage."
meta_title: "Boot Process: BIOS - Boot the System"
meta_description: "Discover the first step of the Linux boot process: the BIOS. Learn how it finds the bootloader via MBR or GPT, and understand the role of UEFI. This guide explains system startup and touches on how to boot into BIOS for configuration."
meta_keywords: "Linux boot process, BIOS, MBR, UEFI, bios in linux, bios linux, how to boot into bios, bootloader, system startup"
---

Firmware runs before the Linux kernel. On PC-class hardware, the two major interfaces are legacy BIOS and UEFI. They use different boot discovery models, so “the BIOS reads the bootloader” is only a description of one path.

## Legacy BIOS Boot

After early platform initialization and boot-device selection, a legacy BIOS commonly reads the first 512-byte sector from the chosen disk and transfers control to its boot code if the sector has the expected signature.

In an MBR layout, that sector contains a small boot-code region, four partition entries, and a signature. The code is too small for a feature-rich loader, so it often locates another stage elsewhere on disk or in a filesystem.

BIOS boot from a GPT disk is possible, but the protective MBR alone does not provide the loader's later stages. GRUB commonly uses a small BIOS Boot Partition on GPT for embedded core code. The exact arrangement belongs to the installed loader.

:::single-choice{#boot-bios-legacy-first-sector} What does legacy BIOS commonly load from the selected boot disk first?

::option[The initial boot sector containing small boot code.]{#boot-bios-boot-sector .correct explanation="The firmware's legacy disk path transfers control to code in the selected disk's first sector."}
::option[The entire Linux root filesystem into firmware memory.]{#boot-bios-entire-root explanation="The first-stage sector is tiny and later software locates the kernel and root storage."}
::option[Every user service configuration under `/etc`.]{#boot-bios-etc-config explanation="Firmware does not parse the installed system's full service configuration."}
:::

## UEFI Boot

UEFI firmware can understand a defined filesystem on an EFI System Partition, or ESP, and load EFI executable files. Firmware boot entries stored in nonvolatile variables normally identify a disk, partition, and executable path. A standardized fallback path can be used for removable media or recovery scenarios.

The ESP contains boot applications and supporting files, not “all startup information.” Kernel images, initramfs files, and loader configuration can reside there or elsewhere depending on the boot design. GPT is conventional for UEFI systems, though the firmware interface and partition-table scheme remain distinct layers.

:::single-choice{#boot-bios-uefi-esp} What does UEFI commonly load from an EFI System Partition?

::option[An EFI executable selected by a firmware boot entry.]{#boot-bios-efi-executable .correct explanation="UEFI boot management points the firmware to an executable file on a supported system partition."}
::option[A POSIX shell script from any arbitrary ext4 home directory.]{#boot-bios-shell-script explanation="Firmware loads defined executable formats from supported boot paths rather than running a normal user shell."}
::option[An MBR extended partition containing user accounts.]{#boot-bios-extended-users explanation="Account data is unrelated to UEFI executable discovery."}
:::

## Secure Boot and Trust

With Secure Boot enabled, UEFI verifies signatures in the boot chain according to enrolled platform keys and policy. A Linux distribution can use a signed shim, boot loader, kernel, and kernel-module policy to extend this chain.

Secure Boot does not encrypt the disk and does not prove that every user-space program is safe. It helps prevent unauthorized pre-boot code from being accepted under the configured trust policy.

:::single-choice{#boot-bios-secure-boot-purpose} What does UEFI Secure Boot primarily enforce?

::option[Automatic encryption of every file on every disk.]{#boot-bios-secure-encryption explanation="Disk confidentiality requires a separate encryption system."}
::option[Signature-based authorization of boot-chain executables.]{#boot-bios-secure-signatures .correct explanation="Firmware and later verified components accept code according to enrolled keys and policy."}
::option[Guaranteed absence of vulnerabilities in signed software.]{#boot-bios-secure-no-vulnerabilities explanation="A valid signature proves authorization and integrity, not flawless code."}
:::

## Entering Firmware Setup

Firmware setup keys vary by manufacturer and model, commonly including keys such as Delete, Escape, or a function key during early startup. Consult the device documentation rather than trying random changes. Some UEFI systems also expose an operating-system request to reboot into firmware setup.

Record existing values and recovery keys before changing Secure Boot, storage-controller mode, TPM, virtualization, or boot order. A firmware change can make encrypted volumes or the installed operating system temporarily inaccessible.

:::single-choice{#boot-bios-setup-key} Why is there no universal key for entering firmware setup?

::option[Linux assigns a new random key after every boot.]{#boot-bios-random-key explanation="The operating system does not randomly define the firmware's early startup key."}
::option[The key and timing are chosen by the system manufacturer.]{#boot-bios-vendor-key .correct explanation="Firmware interfaces differ across models, so authoritative device documentation is required."}
::option[Setup can be entered only by deleting the bootloader.]{#boot-bios-delete-loader explanation="Firmware setup is independent of destroying installed boot files."}
:::

## Summary

You can now distinguish the legacy BIOS and UEFI boot discovery models.

1. Relate legacy BIOS to first-sector boot code and later loader stages.
2. Relate UEFI boot entries to EFI executables on an ESP.
3. Treat GPT, firmware interface, and bootloader layout as separate choices.
4. Change firmware trust and storage settings only with a recovery path.
