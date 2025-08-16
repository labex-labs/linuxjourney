# Boot Process: Bootloader

## Lesson Content

The bootloader's main responsibilities are:

<ul>
<li>Booting into an operating system, it can also be used to boot to non-Linux operating systems</li>
<li>Select a kernel to use</li>
<li>Specify kernel parameters</li>
</ul>

The most common bootloader for Linux is GRUB, you are most likely using it on your system. There are many other bootloaders that you can use such as LILO, efilinux, coreboot, SYSLINUX and more. However, we will just be working with GRUB as our bootloader.

So we know that the bootloader's main goal is to load up the kernel, but where does it find the kernel? To find it, we will need to look at our kernel parameters. The parameters can be found by going into the GRUB menu on startup using the 'e' key. If you don't have GRUB no worries, we'll go through the boot parameters that you will see:

<ul>
<li>initrd - Specifies the location of initial RAM disk (we'll talk more about this in the next lesson).
<li>BOOT_IMAGE  - This is where the kernel image is located</li>
<li>root - The location of the root filesystem, the kernel searches inside this location to find init. It is often represented by it's UUID or the device name such as /dev/sda1.</li>
<li>ro - This parameter is pretty standard, it mounts the fileystem as read-only mode.</li>
<li>quiet - This is added so that you don't see display messages that are going on in the background during boot.</li>
<li>splash - This lets the splash screen be shown.</li>
</ul>

## Exercise

If you have GRUB as your bootloader, go into the GRUB menu with 'e' and take a look at the settings.

## Quiz Question

What kernel parameter makes it so you don't see bootup messages?

## Quiz Answer

quiet
