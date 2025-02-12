# Kernel Installation

## Lesson Content

Ok, now that we've got all that boring stuff out of the way, let's talk about actually installing and modifying kernels. You can install multiple kernels on your system, remember in our lesson on the boot process? In our GRUB menu we can choose which kernel to boot to. 

To see what kernel version you have on your system, use the following command:

<pre>$ uname -r
3.19.0-43-generic</pre>

The uname command prints system information, the -r command will print out all of the kernel release version.

You can install the Linux kernel in different ways, you can download the source package and compile from source or you can install it using package management tools.

<pre>$ sudo apt install linux-generic-lts-vivid</pre>

and then just reboot into the kernel you installed. Simple right? Kind of, you'll need to also install other linux packages such as the linux-headers, linux-image-generic, etc). You can also specify the version number, so the above command can look like, <b>sudo apt install 3.19.0-43-generic</b>

Alternatively, if you just want the updated kernel version, just use dist-upgrade, it performs upgrades to all package on your system:

<pre>$ sudo apt dist-upgrade</pre>

There are many different kernel versions, some are used as LTS (long term support), some are the latest and greatest, the compatibility may be very different between kernel versions so you may want to try out different kernels.

## Exercise

<ol>
<li>Find out what kernel version you have.</li>
<li>Research the different versions of kernels available</li>
</ol>

## Quiz Question

How do you see the kernel version of your system?

## Quiz Answer

uname -r
