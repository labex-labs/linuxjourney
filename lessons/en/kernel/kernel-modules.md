---
lang: "en"
title: "Kernel Modules"
meta_title: "Kernel Modules - Kernel"
meta_description: "Learn about Linux kernel modules: how to load, unload, and manage them. Understand `modprobe` and `lsmod` commands for extending kernel functionality. Start your Linux journey!"
meta_keywords: "Linux kernel modules, modprobe, lsmod, kernel management, Linux tutorial, beginner Linux, Linux guide"
---

## Lesson Content

Let's say I have a sweet ride; I invest a lot of time and money into it. I add a spoiler, hitch, bike rack, and other random things. These components don't actually change the core functionality of the car, and I can remove and add them very easily. The kernel uses the same concept with kernel modules.

The kernel in itself is a monolithic piece of software. When we want to add support for a new type of keyboard, we don't write this code directly into the kernel code. Just as we wouldn't meld a bike rack to our car (well, maybe some people would do that). Kernel modules are pieces of code that can be loaded and unloaded into the kernel on demand. They allow us to extend the functionality of the kernel without actually adding to the core kernel code. We can also add modules and not have to reboot the system (in most cases).

### View a list of currently loaded modules

```bash
lsmod
```

### Load a module

```bash
sudo modprobe bluetooth
```

`modprobe` loads the module from `/lib/modules/(kernel version)/kernel/drivers`. Kernel modules may also have dependencies; `modprobe` loads our module dependencies if they are not already loaded.

### Remove a module

```bash
sudo modprobe -r bluetooth
```

### Load on bootup

You can also load modules during system boot, instead of temporarily loading them with `modprobe` (which will be unloaded when you reboot). Just modify the `/etc/modprobe.d` directory and add a configuration file in it like so:

```plaintext
pete@icebox:~$ /etc/modprobe.d/peanutbutter.conf

options peanut_butter type=almond
```

A bit of an outlandish example, but if you had a module named `peanut_butter` and you wanted to add a kernel parameter for `type=almond`, you can have it load on startup using this configuration file. Also, note that kernel modules have their own kernel parameters, so you'll want to read about the module specifically to find out more.

### Do not load on bootup

You can also make sure a module does not load on bootup by adding a configuration file like so:

```plaintext
pete@icebox:~$ /etc/modprobe.d/peanutbutter.conf

blacklist peanut_butter
```

## Exercise

Unload your Bluetooth module with `modprobe` and see what happens. How will you fix this?

## Quiz Question

What command is used to unload a module?

## Quiz Answer

modprobe -r
