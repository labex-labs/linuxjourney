---
index: 2
lang: "en"
title: "Boot Process: BIOS"
meta_title: "Boot Process: BIOS - Boot the System"
meta_description: "Learn about the Linux boot process, BIOS, and MBR. Understand how your system starts up with this beginner-friendly guide. Explore UEFI concepts!"
meta_keywords: "Linux boot process, BIOS, MBR, UEFI, Linux tutorial, bootloader, beginner Linux, system startup"
---

## Lesson Content

### BIOS

The first step in the Linux boot process is the BIOS, which performs system integrity checks. The BIOS is firmware that is most common in IBM PC-compatible computers, the dominant type of computers out there today. You've probably used the BIOS firmware to change the boot order of your hard drives, check system time, your machine's MAC address, etc. The BIOS's main goal is to find the system bootloader.

So, once the BIOS boots up the hard drive, it searches for the boot block to figure out how to boot up the system. Depending on how you partition your disk, it will look to the Master Boot Record (MBR) or GPT. The MBR is located in the first sector of the hard drive, the first 512 bytes. The MBR contains the code to load another program somewhere on the disk; this program in turn actually loads up our bootloader.

Now, if you partitioned your disk with GPT, the location of the bootloader changes a bit.

### UEFI

There is another way to boot up your system instead of using BIOS, and that is with UEFI (stands for "Unified Extensible Firmware Interface"). UEFI was designed to be the successor to BIOS; most hardware out there today comes with UEFI firmware built in. Macintosh machines have been using EFI booting for years now, and Windows has mostly moved all of their stuff over to UEFI booting. The GPT format was intended for use with EFI. You don't necessarily need EFI if you are booting a GPT disk. The first sector of a GPT disk is reserved for a "protective MBR" to make it possible to boot a BIOS-based machine.

UEFI stores all the information about startup in an `.efi` file. This file is stored on a special partition called the EFI System Partition on the hardware. Inside this partition, it will contain the bootloader. UEFI comes with many improvements from the traditional BIOS firmware. However, since we are using Linux, the majority of us are using BIOS. So all of these lessons will be going along with that premise.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of Linux user and group management:

1. **[Manage Linux User Accounts with useradd, usermod, and userdel](https://labex.io/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Practice the complete lifecycle of user administration, from creating and securing new accounts to modifying and deleting them.
2. **[Manage Linux Groups with groupadd, usermod, and groupdel](https://labex.io/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Gain hands-on experience with command-line utilities for group administration, including creating new groups, modifying user memberships, and removing groups.
3. **[Configure User Accounts and Sudo Privileges in Linux](https://labex.io/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Learn essential techniques for managing user accounts and sudo privileges to enhance the security of a Linux system.

These labs will help you apply the concepts in real scenarios and build confidence with user and group management in Linux.

## Quiz Question

What does the BIOS load?

## Quiz Answer

bootloader
