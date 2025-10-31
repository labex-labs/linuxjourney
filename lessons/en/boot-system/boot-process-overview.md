---
index: 1
lang: "en"
title: "Boot Process Overview"
meta_title: "Boot Process Overview - Boot the System"
meta_description: "A clear overview of the Linux boot process, detailing the four key stages: BIOS, bootloader, kernel, and init. Learn about the complete booting process of the Linux operating system, from power-on to the login prompt."
meta_keywords: "Linux boot process, boot process linux, booting process linux, booting process of linux operating system, BIOS, bootloader, kernel, init, Linux tutorial, Linux guide, beginner"
---

## Lesson Content

Having explored some key components of Linux, let's now see how they all come together during system startup. The entire sequence, from pressing the power button to reaching a login prompt, is known as the **Linux boot process**. It's a fascinating journey that transforms a powered-off machine into a fully functional operating system.

The **booting process of the Linux operating system** can be simplified into four main stages.

### Stage 1 BIOS

The BIOS (Basic Input/Output System) or its modern successor, UEFI (Unified Extensible Firmware Interface), is the first software to run when you power on your computer. It performs a Power-On Self-Test (POST) to initialize and verify the system's hardware, such as the CPU, memory, and storage devices. Once the hardware checks out, the BIOS's primary job is to locate and load the bootloader from a storage device.

### Stage 2 Bootloader

The bootloader takes over from the BIOS. Its main responsibility is to load the Linux kernel into memory. A common bootloader for Linux is GRUB (GRand Unified Bootloader). GRUB often presents a menu, allowing you to choose which operating system or kernel version to boot. After you make a selection (or after a timeout), it loads the selected kernel and an initial RAM disk (initrd) into memory, then passes control to the kernel.

### Stage 3 Kernel

Once the kernel is loaded into memory, it takes control of the system. It starts by decompressing itself and initializing core hardware and memory management. The kernel then mounts the root filesystem, which contains all the system files. Its final and most critical task in the **boot process linux** relies on is to execute the first user-space program: the `init` process.

### Stage 4 Init

The `init` process is the first process started by the kernel and is the ancestor of all other processes on the system. Its primary job is to bring the system to a usable state by starting essential services and background processes (daemons) according to its configuration. There are several implementations of `init`, such as the traditional System V init, Upstart, and the now widely-adopted systemd.

This provides a high-level overview of the **booting process linux** follows. We will delve deeper into each of these stages in the upcoming lessons.

## Exercise

To solidify your understanding, we recommend trying this hands-on lab. It provides a practical environment to apply what you've learned about the Linux boot process.

1.  **[Customize the GRUB2 Boot Menu in Linux](https://labex.io/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)** - Practice modifying the GRUB2 boot menu, a critical component in the Linux boot sequence.

## Quiz Question

What is the last stage in the Linux boot process? (Please answer in English, paying attention to case sensitivity).

## Quiz Answer

init
