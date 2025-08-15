# Kernel Location

## Lesson Content

What happens when you install a new kernel? Well it actually adds a couple of files to your system, these files are usually added to the /boot directory.

You will see multiple files for different kernel versions:

<ul>
<li>vmlinuz - this is the actual linux kernel</li>
<li>initrd - as we've discussed before, the initrd is used as a temporary file system, used before loading the kernel</li>
<li>System.map - symbolic lookup table</li>
<li>config - kernel configuration settings, if you are compiling your own kernel, you can set which modules can be loaded</li>
</ul>

If your /boot directory runs out of space, you can always delete old versions of these files or just use a package manager, but be careful when doing maintenance in this directory and don't accidentally delete the kernel you are using.

## Exercise

Go into your boot directory and see what files are in there.

## Quiz Question

What is the kernel image called in /boot?

## Quiz Answer

vmlinuz
