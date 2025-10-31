---
index: 5
lang: "en"
title: "Kernel Location"
meta_title: "Kernel Location - Kernel"
meta_description: "Discover where the kernel is stored in Linux. This guide explains the Linux kernel location in the /boot directory, detailing key files like vmlinuz and initrd."
meta_keywords: "linux kernel location, where is the kernel, kernel location, where is the kernel located, where is the kernel stored in linux, vmlinuz, /boot directory"
---

## Lesson Content

When you install a new kernel, your system adds several important files to a specific directory. If you've ever wondered **where is the kernel stored in Linux**, the answer is typically the `/boot` directory. This directory is the standard **Linux kernel location** on most systems.

### The /boot Directory

The `/boot` directory contains all the files needed to start the boot process. When you look inside, you'll often see files corresponding to different kernel versions, allowing you to boot into an older kernel if a new one causes issues. Understanding this **kernel location** is crucial for system maintenance.

### Key Kernel Files

So, **where is the kernel located** within this directory? It's accompanied by a few other critical files. Here are the main ones you will encounter:

- `vmlinuz`: This is the compressed, executable Linux kernel itself. The 'z' at the end indicates that it is compressed.
- `initrd`: This is the initial RAM disk. As we've discussed, the `initrd` is a temporary root filesystem loaded into memory during startup to mount the real root filesystem.
- `System.map`: This file holds a symbol table, which maps kernel function names to their memory addresses. It's primarily used for debugging kernel panics and oopses.
- `config`: This file stores the configuration settings that were used to compile that specific kernel version. It details which drivers and features were included.

### Managing Kernel Files

Over time, your `/boot` directory can fill up with files from old kernels. If you run out of space, you can remove the files for older, unused versions. The safest way to do this is by using your distribution's package manager (like `apt` or `dnf`). Manually deleting files can be risky, so be extremely careful not to remove the files for the kernel you are currently using.

## Exercise

Apply your knowledge with this hands-on lab to reinforce your understanding of the Linux boot process and kernel management:

1. **[Customize the GRUB2 Boot Menu in Linux](https://labex.io/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)** - Practice modifying the GRUB2 configuration, which directly impacts how your Linux system boots and selects kernel versions. This lab will help you understand the practical implications of the files discussed in the `/boot` directory.

This lab will help you apply these concepts in a real-world scenario and build confidence with Linux kernel and boot management.

## Quiz Question

In the `/boot` directory, what is the typical name for the compressed Linux kernel image file? Please answer in English, paying attention to case sensitivity.

## Quiz Answer

vmlinuz
