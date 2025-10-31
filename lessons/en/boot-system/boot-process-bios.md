---
index: 2
lang: "en"
title: "Boot Process: BIOS"
meta_title: "Boot Process: BIOS - Boot the System"
meta_description: "Discover the first step of the Linux boot process: the BIOS. Learn how it finds the bootloader via MBR or GPT, and understand the role of UEFI. This guide explains system startup and touches on how to boot into BIOS for configuration."
meta_keywords: "Linux boot process, BIOS, MBR, UEFI, bios in linux, bios linux, how to boot into bios, bootloader, system startup"
---

## Lesson Content

The first step in the Linux boot process is the BIOS (Basic Input/Output System), which performs crucial system integrity checks upon startup. The BIOS is firmware commonly found in IBM PC-compatible computers, which represent the majority of computers in use today.

### The Role of BIOS in Linux

When you power on your computer, the **BIOS in Linux** systems is the first software to run. Its primary function is to initialize and test the system hardware, such as the CPU, memory, and hard drives. You have likely interacted with the BIOS firmware before to change the boot order, check the system time, or view your machine's MAC address. After the hardware checks are complete, the main goal of the **bios linux** process is to locate and hand off control to the system bootloader.

### How BIOS Finds the Bootloader

Once the BIOS initializes the hard drive, it searches for a boot block to determine how to start the operating system. The location it checks depends on the disk's partitioning scheme: Master Boot Record (MBR) or GUID Partition Table (GPT).

The MBR is located in the first 512 bytes of the hard drive. This small section contains the initial boot code and the partition table. The MBR's code is responsible for loading another program, which in turn loads our actual bootloader. If you are using a GPT-partitioned disk, the process is slightly different.

### How to Boot into BIOS

Many users need to know **how to boot into BIOS** to configure hardware settings. The method for this typically involves pressing a specific key (such as F2, F10, DEL, or ESC) immediately after powering on the computer. Learning **how to boot to bios** is essential for tasks like changing the boot device priority or enabling virtualization technology. The exact key varies by manufacturer, so you may need to consult your computer's documentation.

### The Rise of UEFI

An alternative to the traditional BIOS is UEFI (Unified Extensible Firmware Interface). Designed as the successor to BIOS, UEFI is now standard on most modern hardware. It stores all startup information in an `.efi` file located on a dedicated EFI System Partition (ESP). This partition contains the bootloader for the installed operating system.

UEFI offers many improvements over BIOS, including faster boot times and support for larger hard drives. While the GPT format was designed for UEFI, a "protective MBR" on GPT disks ensures backward compatibility, making it possible to boot from them on older BIOS-based machines. Although many Linux systems now use UEFI, this guide will focus on the traditional BIOS boot process for foundational understanding.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of Linux user and group management:

1. **[Manage Linux User Accounts with useradd, usermod, and userdel](https://labex.io/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Practice the complete lifecycle of user administration, from creating and securing new accounts to modifying and deleting them.
2. **[Manage Linux Groups with groupadd, usermod, and groupdel](https://labex.io/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Gain hands-on experience with command-line utilities for group administration, including creating new groups, modifying user memberships, and removing groups.
3. **[Configure User Accounts and Sudo Privileges in Linux](https://labex.io/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Learn essential techniques for managing user accounts and sudo privileges to enhance the security of a Linux system.

These labs will help you apply the concepts in real scenarios and build confidence with user and group management in Linux.

## Quiz Question

What does the BIOS load? Please answer in a single word, in English, and in lowercase.

## Quiz Answer

bootloader
