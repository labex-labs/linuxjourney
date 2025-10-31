---
index: 6
lang: "en"
title: "Kernel Modules"
meta_title: "Kernel Modules - Kernel"
meta_description: "Discover what kernel modules are in Linux and how they extend kernel functionality. This lesson covers using lsmod and modprobe to list, load, and unload modules on demand."
meta_keywords: "what are kernel modules, Linux kernel modules, modprobe, lsmod, kernel management, Linux tutorial, beginner Linux, Linux guide"
---

## Lesson Content

Think of the Linux kernel as the core engine of a car. You can add accessories like a roof rack or a new sound system without changing the engine itself. These accessories can be added or removed as needed. The Linux kernel uses a similar concept with kernel modules.

### What are Kernel Modules

So, **what are kernel modules**? They are pieces of code that can be loaded into and unloaded from the kernel on demand. They extend the functionality of the kernel without requiring you to recompile the core kernel or reboot the system. This modular approach allows support for new hardware (like a new Wi-Fi card) or new software features (like a new filesystem) to be added dynamically. This keeps the core kernel lean while allowing for immense flexibility.

### Listing Loaded Modules

To see a list of all kernel modules currently loaded into memory, you can use the `lsmod` command. This gives you a snapshot of the active modules and their dependencies.

```bash
lsmod
```

### Loading a Kernel Module

To load a kernel module, we use the `modprobe` command. For example, to load the `bluetooth` module, you would run:

```bash
sudo modprobe bluetooth
```

The `modprobe` command is intelligent; it searches for the module in the standard directory (`/lib/modules/$(uname -r)/`) and also loads any other modules that the target module depends on.

### Unloading a Kernel Module

If a module is no longer needed, you can unload it to free up system resources. Use the `-r` flag with `modprobe` to remove a module:

```bash
sudo modprobe -r bluetooth
```

### Managing Modules at Boot

Modules loaded with `modprobe` are temporary and will be gone after a reboot. To make module configurations permanent, you can create configuration files in the `/etc/modprobe.d/` directory.

To automatically load a module at boot with specific options, create a `.conf` file. For instance, if you had a hypothetical module named `peanut_butter` and wanted to set its `type` parameter to `almond`, your file would look like this:

```plaintext
# /etc/modprobe.d/peanutbutter.conf

options peanut_butter type=almond
```

Conversely, to prevent a module from loading at boot (a process called blacklisting), you can use the `blacklist` keyword in a configuration file:

```plaintext
# /etc/modprobe.d/peanutbutter.conf

blacklist peanut_butter
```

These configuration files allow for fine-grained control over which modules are available when your system starts.

## Exercise

Practice makes perfect! Here's a hands-on lab to reinforce your understanding of Linux kernel modules:

1. **[Manage Kernel Modules in Linux](https://labex.io/labs/comptia-manage-kernel-modules-in-linux-590865)** - Practice listing, inspecting, loading, and unloading kernel modules, and configuring them to load automatically at boot. This lab will help you apply the concepts in a real scenario and build confidence with kernel module management.

## Quiz Question

What command is used to unload a module?

## Quiz Answer

modprobe -r
