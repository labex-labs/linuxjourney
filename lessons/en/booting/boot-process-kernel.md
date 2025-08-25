---
index: 4
lang: "en"
title: "Boot Process: Kernel"
meta_title: "Boot Process: Kernel - Boot the System"
meta_description: "Learn about the Linux boot process, kernel initialization, and the role of initramfs. Understand how the kernel mounts the root filesystem. Linux boot process guide."
meta_keywords: "Linux boot process, kernel boot, initramfs, initrd, root filesystem, Linux tutorial, beginner Linux, Linux guide"
---

## Lesson Content

So now that our bootloader has passed on the necessary parameters, let's see how it gets started:

### Initrd vs Initramfs

There is a bit of a chicken-and-egg problem when we talk about the kernel boot-up. The kernel manages our system's hardware; however, not all drivers are available to the kernel during boot-up. So we depend on a temporary root filesystem that contains just the essential modules the kernel needs to access the rest of the hardware. In older versions of Linux, this job was given to the initrd (initial ramdisk). The kernel would mount the initrd, get the necessary boot-up drivers, then when it was done loading everything it needed, it would replace the initrd with the actual root filesystem. These days, we have something called the initramfs; this is a temporary root filesystem that is built into the kernel itself to load all the necessary drivers for the real root filesystem, so there's no more locating the initrd file.

### Mounting the root filesystem

Now the kernel has all the modules it needs to create a root device and mount the root partition. Before going any further, the root partition is actually mounted in read-only mode first so that fsck can run safely and check for system integrity. Afterwards, it remounts the root filesystem in read-write mode. Then the kernel locates the init program and executes it.

## Exercise

Practice makes perfect! Here is a hands-on lab to reinforce your understanding of the Linux boot process:

- **[Customize the GRUB2 Boot Menu in Linux](https://labex.io/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)** - Learn to modify the GRUB2 boot menu, including changing the timeout and default entry, and applying these changes. This lab will help you understand how the bootloader can be configured.

This lab will help you apply the concepts in a real scenario and build confidence with Linux boot configuration.

## Quiz Question

What is used in modern systems to load a temporary root filesystem?

## Quiz Answer

initramfs
