---
index: 5
lang: "en"
title: "Kernel Location"
meta_title: "Kernel Location - Kernel"
meta_description: "Learn about Linux kernel location in the /boot directory, understanding vmlinuz, initrd, and System.map. Explore kernel files and manage space effectively."
meta_keywords: "Linux kernel, /boot directory, vmlinuz, initrd, System.map, Linux beginner, kernel tutorial, Linux guide"
---

## Lesson Content

What happens when you install a new kernel? Well, it actually adds a couple of files to your system; these files are usually added to the `/boot` directory.

You will see multiple files for different kernel versions:

- `vmlinuz` - this is the actual Linux kernel
- `initrd` - as we've discussed before, the `initrd` is used as a temporary file system, used before loading the kernel
- `System.map` - symbolic lookup table
- `config` - kernel configuration settings; if you are compiling your own kernel, you can set which modules can be loaded

If your `/boot` directory runs out of space, you can always delete old versions of these files or just use a package manager. But be careful when doing maintenance in this directory, and don't accidentally delete the kernel you are currently using.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of the Linux boot process and kernel management:

1. **[Customize the GRUB2 Boot Menu in Linux](https://labex.io/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)** - Practice modifying the GRUB2 configuration, which directly impacts how your Linux system boots and selects kernel versions. This lab will help you understand the practical implications of the files discussed in the `/boot` directory.

This lab will help you apply the concepts in real scenarios and build confidence with Linux kernel and boot management.

## Quiz Question

What is the kernel image called in `/boot`?

## Quiz Answer

vmlinuz
