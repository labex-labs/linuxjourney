# Kernel Installation

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

1. Find out what kernel version you have.
2. Research the different versions of kernels available.

## Quiz Question

How do you see the kernel version of your system?

## Quiz Answer

uname -r
