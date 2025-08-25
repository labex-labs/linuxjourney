---
index: 4
lang: "en"
title: "Kernel Installation"
meta_title: "Kernel Installation - Kernel"
meta_description: "Learn how to install and manage Linux kernels. Discover kernel versions, use `uname -r`, and apt commands. Start your Linux kernel journey!"
meta_keywords: "Linux kernel, install kernel, uname -r, apt dist-upgrade, kernel management, Linux tutorial, beginner Linux, Linux guide"
---

## Lesson Content

Okay, now that we've got all that boring stuff out of the way, let's talk about actually installing and modifying kernels. You can install multiple kernels on your system; remember in our lesson on the boot process? In our GRUB menu, we can choose which kernel to boot to.

To see what kernel version you have on your system, use the following command:

```bash
$ uname -r
3.19.0-43-generic
```

The `uname` command prints system information; the `-r` option will print out the kernel release version.

You can install the Linux kernel in different ways: you can download the source package and compile from source, or you can install it using package management tools.

```bash
sudo apt install linux-generic-lts-vivid
```

And then just reboot into the kernel you installed. Simple, right? Kind of. You'll need to also install other Linux packages such as `linux-headers`, `linux-image-generic`, etc. You can also specify the version number, so the above command can look like: **`sudo apt install 3.19.0-43-generic`**

Alternatively, if you just want the updated kernel version, just use `dist-upgrade`; it performs upgrades to all packages on your system:

```bash
sudo apt dist-upgrade
```

There are many different kernel versions. Some are used as LTS (Long Term Support), some are the latest and greatest. The compatibility may be very different between kernel versions, so you may want to try out different kernels.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of Linux kernel management and related system administration tasks:

1. **[Customize the GRUB2 Boot Menu in Linux](https://labex.io/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)** - Practice modifying the GRUB2 boot menu, which is essential when managing multiple kernel versions and selecting which one to boot into.
2. **[Manage Kernel Modules in Linux](https://labex.io/labs/comptia-manage-kernel-modules-in-linux-590865)** - Learn to list, inspect, load, and unload kernel modules, a fundamental aspect of kernel management and understanding how hardware interacts with your system.
3. **[Software Installation on Linux](https://labex.io/labs/linux-software-installation-on-linux-18005)** - Gain practical experience with various methods to install and manage software, including using package managers, which is a common way to install and update kernels.

These labs will help you apply the concepts of kernel management, boot processes, and package management in real scenarios, building confidence with system administration.

## Quiz Question

How do you see the kernel version of your system?

## Quiz Answer

uname -r
