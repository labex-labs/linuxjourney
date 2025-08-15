# Boot Process: BIOS

## Lesson Content

<b>BIOS</b>

The first step in the Linux boot process is the BIOS which performs system integrity checks. The BIOS is a firmware that comes most common in IBM PC compatible computers, the dominant type of computers out there today. You've probably used the BIOS firmware to change the boot order of your harddisks, check system time, your machine's mac address, etc. The BIOS's main goal is to find the system bootloader.

So once the BIOS boots up the hard drive, it searches for the boot block to figure out how to boot up the system. Depending on how you partition your disk, it will look to the master boot record (MBR) or GPT. The MBR is located in the first sector of the hard drive, the first 512 bytes. The MBR contains the code to load another program somewhere on the disk, this program in turn actually loads up our bootloader.

Now if you partitioned your disk with GPT, the location of the bootloader changes a bit.

<b>UEFI</b>

There is another way to boot up your system instead of using BIOS and that is with UEFI (stands for "Unified extensible firmware interface"). UEFI was designed to be successor to BIOS, most hardware out there today comes with UEFI firmware built in. Macintosh machines have been using EFI booting for years now and Windows has mostly moved all of their stuff over to UEFI booting. The GPT format was intended for use with EFI. You don't necessarily need EFI if you are booting a GPT disk. The first sector of a GPT disk is reserved for a "protective MBR" to make it possible to boot a BIOS-based machine.

UEFI stores all the information about startup in an .efi file. This file is stored on a special partition called EFI system partition on the hardware. Inside this partition it will contain the bootloader. UEFI comes with many improvements from the traditional BIOS firmware. However, since we are using Linux, the majority of us are using BIOS. So all of these lessons will be going along with that pretense.

## Exercise

Go into your BIOS menu and see if you have UEFI booting enabled.

## Quiz Question

What does the BIOS load?

## Quiz Answer

bootloader
