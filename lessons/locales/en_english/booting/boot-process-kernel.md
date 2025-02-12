# Boot Process: Kernel

## Lesson Content

So now that our bootloader has passed on the necessary parameters, let's see how it get's started:

<b>Initrd vs Initramfs</b>

There is a bit of a chicken and egg problem when we talk about the kernel bootup. The kernel manages our systems hardware, however not all drivers are available to the kernel during bootup. So we depend on a temporary root filesystem that contains just the essential modules that the kernel needs to get to the rest of the hardware. In older versions of Linux, this job was given to the initrd (initial ram disk). The kernel would mount the initrd, get the necessary bootup drivers, then when it was done loading everything it needed, it would replace the initrd with the actual root filesystem. These days, we have something called the initramfs, this is a temporary root filesystem that is built into the kernel itself to load all the necessary drivers for the real root filesystem, so no more locating the initrd file. 

<b>Mounting the root filesystem</b>

Now the kernel has all the modules it needs to create a root device and mount the root partition. Before you go any further though, the root partition is actually mounted in read-only mode first so that fsck can run safely and check for system integrity. Afterwards it remounts the root filesystem in read-write mode. Then the kernel locates the init program and executes it. 

## Exercise

No exercises for this lesson.

## Quiz Question

What is used in modern systems to load up a temporary root filesystem?

## Quiz Answer

initramfs
