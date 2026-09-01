---
lesson_id: "kernel-modules"
course_id: "kernel"
lang: "en"
order_index: 6
title: "Kernel Modules"
description: "Learn how to inspect, load, configure, and safely remove release-specific Linux kernel modules."
meta_title: "Kernel Modules - Kernel"
meta_description: "Discover what kernel modules are in Linux and how they extend kernel functionality. This lesson covers using lsmod and modprobe to list, load, and unload modules on demand."
meta_keywords: "what are kernel modules, Linux kernel modules, modprobe, lsmod, kernel management, Linux tutorial, beginner Linux, Linux guide"
---

A loadable kernel module is privileged code that can extend the running kernel with a driver, filesystem, network feature, or other subsystem. Modules avoid building every optional feature into one kernel image, but loading one expands the trusted kernel attack surface.

## Listing and Inspecting Modules

List modules currently loaded:

```bash
$ lsmod
```

The output is derived from kernel state such as `/proc/modules` and includes module name, size, and a use count or dependencies. A zero-looking count is not complete proof that removal is safe; a driver can still own active devices or participate in subsystem state.

Inspect a module available for the running kernel with:

```bash
$ modinfo MODULE_NAME
```

`modinfo` can show filename, aliases, parameters, license, description, and signature information. Treat metadata as descriptive, not proof that the module is trustworthy or compatible with the workload.

:::single-choice{#kernel-modules-lsmod-purpose} What does `lsmod` display?

::option[Every module package available in remote repositories.]{#kernel-modules-repository-list explanation="Package-manager queries are needed for repository inventory."}
::option[Only drivers compiled directly into the kernel image.]{#kernel-modules-builtins explanation="Built-in features are not loadable modules and normally do not appear in lsmod."}
::option[Modules currently loaded in the running kernel.]{#kernel-modules-loaded-list .correct explanation="The listing reflects live module state and dependency/use information."}
:::

## Loading with `modprobe`

Load a module by name:

```bash
$ sudo modprobe MODULE_NAME
```

`modprobe` consults dependency indexes, aliases, and configuration for the running kernel under `/lib/modules/$(uname -r)/`. It loads required dependencies and passes configured parameters. `insmod` instead inserts one specified module file directly and does not provide the same dependency-resolution workflow.

Before loading, confirm module provenance, signature policy, kernel release compatibility, parameters, expected hardware binding, and rollback. Secure Boot or kernel lockdown can reject unsigned modules; forcing incompatible code risks a crash or compromise.

:::single-choice{#kernel-modules-modprobe-dependencies} Why is `modprobe` normally preferred over direct `insmod`?

::option[It runs the module entirely in unprivileged user space.]{#kernel-modules-modprobe-userspace explanation="The inserted module executes as privileged kernel code."}
::option[It guarantees that every third-party module is signed and safe.]{#kernel-modules-modprobe-guarantee explanation="Enforcement depends on policy, and a valid signature does not prove absence of defects."}
::option[It resolves module aliases, dependencies, and configuration.]{#kernel-modules-modprobe-resolves .correct explanation="Modprobe uses the indexed module tree for the exact running release."}
:::

## Module Parameters and Boot-Time Loading

Persistent parameter and alias policy belongs in a `.conf` file under `/etc/modprobe.d/`:

```text
options example_module mode=careful
```

This line affects how modprobe loads the module; it does not by itself request that the module load at boot. A simple boot-time load list commonly belongs under `/etc/modules-load.d/`:

```text
example_module
```

Hardware aliases often trigger automatic loading without an explicit list. For modules needed inside early boot, update the initramfs through the distribution's documented process after configuration changes.

:::single-choice{#kernel-modules-options-versus-load} What does an `options` line in `/etc/modprobe.d/` do?

::option[Guarantees the module is loaded at every boot by that line alone.]{#kernel-modules-options-autoload explanation="Boot-time load requests use another mechanism such as modules-load configuration or device aliases."}
::option[Sets parameters used when the named module is loaded.]{#kernel-modules-options-parameters .correct explanation="Modprobe applies configured key-value arguments during insertion."}
::option[Compiles the module for every installed kernel release.]{#kernel-modules-options-compiles explanation="Configuration does not build binary modules."}
:::

## Blacklisting and Its Limits

A modprobe configuration can contain:

```text
blacklist example_module
```

Blacklisting normally suppresses automatic loading through the module's aliases. It does not unload an already loaded module, remove it from an initramfs, or necessarily prevent an explicit load by exact name or loading as a dependency. Security hardening requires a threat-specific combination of module availability, signature enforcement, initramfs content, boot parameters, and policy.

:::single-choice{#kernel-modules-blacklist-effect} What does a basic modprobe `blacklist` line primarily suppress?

::option[Automatic loading through the module's aliases.]{#kernel-modules-blacklist-aliases .correct explanation="The directive is not a universal prohibition on every route by which code can already be or become loaded."}
::option[Execution of every user-space program with a similar name.]{#kernel-modules-blacklist-user-programs explanation="Modprobe configuration applies to kernel module resolution."}
::option[All kernel code compiled into the image.]{#kernel-modules-blacklist-builtins explanation="Built-in functionality cannot be unloaded or blocked as a module."}
:::

## Removing a Module Safely

Request removal with:

```bash
$ sudo modprobe -r MODULE_NAME
```

Modprobe can remove now-unused dependencies as appropriate. The kernel refuses removal when ordinary reference tracking shows the module is busy, but do not rely on that as the only safety check. Stop services, unmount filesystems, detach devices, quiesce networking, and confirm another driver or recovery path before removing code that supports active hardware.

Never force-unload a module on a system you need to preserve. Removal bugs or outstanding activity can crash the kernel or corrupt data.

:::single-choice{#kernel-modules-remove-command} Which command requests dependency-aware removal of a module by name?

::option[`lsmod -r MODULE_NAME`]{#kernel-modules-lsmod-remove explanation="Lsmod is a read-only listing tool and has no removal role."}
::option[`uname -r MODULE_NAME`]{#kernel-modules-uname-remove explanation="Uname reports kernel information and does not manage modules."}
::option[`modprobe -r MODULE_NAME`]{#kernel-modules-modprobe-remove .correct explanation="The remove mode considers the indexed dependency relationships around the requested module."}
:::

Use [Manage Kernel Modules in Linux](https://labex.io/labs/comptia-manage-kernel-modules-in-linux-590865) to practice with modules designated safe by the lab.

## Summary

You can now manage modules while respecting their kernel-level risk.

1. Use `lsmod` for live state and `modinfo` for available metadata.
2. Use `modprobe` for alias and dependency-aware loading.
3. Separate modprobe parameters from boot-time load requests.
4. Treat blacklisting as limited policy rather than an absolute block.
5. Quiesce every consumer before `modprobe -r`.
