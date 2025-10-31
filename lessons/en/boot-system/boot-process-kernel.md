---
index: 4
lang: "en"
title: "Boot Process: Kernel"
meta_title: "Boot Process: Kernel - Boot the System"
meta_description: "Explore the Linux kernel boot process. Learn how initramfs loads drivers from a temporary filesystem to mount the final boot root partition. Understand the steps from kernel loading to executing init."
meta_keywords: "boot root, initramfs, kernel boot, boot partition, initramfs ubuntu, /etc/default/grub, Linux boot process, root filesystem, kernel initialization"
---

## Lesson Content

Once the bootloader has loaded the kernel into memory and passed the necessary parameters, the kernel takes control of the system. Let's explore what happens next.

### Kernel Initialization and the Initramfs

A classic challenge during boot-up is that the kernel needs drivers to access hardware devices, but those drivers often reside on a storage device that the kernel can't access yet. To solve this, Linux uses a temporary root filesystem.

In older systems, this was handled by an `initrd` (initial RAM disk). The kernel would load this disk image, find the necessary drivers, and then switch to the real root filesystem. Modern systems, including distributions like Ubuntu, use `initramfs` (initial RAM filesystem). Unlike `initrd`, `initramfs` is a `cpio` archive that is unpacked into a temporary filesystem directly in memory. This approach is more efficient as it avoids the overhead of creating and mounting a block device. The `initramfs` contains just the essential modules the kernel needs to access the actual `boot partition` and other hardware.

### Mounting the Boot Root Filesystem

With the drivers loaded from `initramfs`, the kernel can now locate and mount the main `boot root` filesystem. The location of this filesystem is typically passed as a parameter by the bootloader, which can be configured in files like `/etc/default/grub`.

First, the kernel mounts the `boot root` partition in read-only mode. This is a safety measure that allows the `fsck` (file system check) utility to run and verify the integrity of the filesystem without risking data corruption. After the check completes successfully, the kernel remounts the filesystem in read-write mode.

Finally, with the root filesystem fully available, the kernel starts the very first user-space program: `init`. This program is responsible for bringing the rest of the system online.

## Exercise

Practice makes perfect! Here is a hands-on lab to reinforce your understanding of the Linux boot process:

- **[Customize the GRUB2 Boot Menu in Linux](https://labex.io/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)** - Learn to modify the GRUB2 boot menu, including changing the timeout and default entry, and applying these changes. This lab will help you understand how the bootloader can be configured.

This lab will help you apply the concepts in a real scenario and build confidence with Linux boot configuration.

## Quiz Question

What is used in modern systems to load a temporary root filesystem? Please answer in English, using only lowercase letters.

## Quiz Answer

initramfs
