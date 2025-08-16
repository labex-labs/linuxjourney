---
lang: "en"
title: "Boot Process: Bootloader"
description: "Learn about the Linux bootloader, its functions, and common kernel parameters like initrd and root. Understand GRUB and optimize your Linux boot process."
keywords: "Linux bootloader, GRUB, kernel parameters, initrd, root filesystem, Linux boot process, Linux tutorial, beginner Linux"
---

## Lesson Content

The bootloader's main responsibilities are:

- Booting into an operating system; it can also be used to boot to non-Linux operating systems.
- Select a kernel to use.
- Specify kernel parameters.

The most common bootloader for Linux is GRUB; you are most likely using it on your system. There are many other bootloaders that you can use, such as LILO, EFILINUX, Coreboot, SYSLINUX, and more. However, we will just be working with GRUB as our bootloader.

So, we know that the bootloader's main goal is to load the kernel, but where does it find the kernel? To find it, we will need to look at our kernel parameters. The parameters can be found by going into the GRUB menu on startup using the 'e' key. If you don't have GRUB, no worries, we'll go through the boot parameters that you will see:

- `initrd` - Specifies the location of the initial RAM disk (we'll talk more about this in the next lesson).
- `BOOT_IMAGE` - This is where the kernel image is located.
- `root` - The location of the root filesystem; the kernel searches inside this location to find `init`. It is often represented by its UUID or the device name, such as `/dev/sda1`.
- `ro` - This parameter is pretty standard; it mounts the filesystem in read-only mode.
- `quiet` - This is added so that you don't see display messages that are going on in the background during boot.
- `splash` - This lets the splash screen be shown.

## Exercise

If you have GRUB as your bootloader, go into the GRUB menu with 'e' and take a look at the settings.

## Quiz Question

What kernel parameter makes it so you don't see bootup messages?

## Quiz Answer

quiet
