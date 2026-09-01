---
lesson_id: "filesystem-hierarchy"
course_id: "filesystem"
lang: "en"
order_index: 1
title: "Filesystem Hierarchy"
description: "Learn the intended roles of major Linux directories and how modern merged layouts can differ."
meta_title: "Filesystem Hierarchy - The Filesystem"
meta_description: "Explore the standard Linux file system hierarchy (FSH). This guide explains the purpose of key directories like /bin, /etc, /home, and /var, providing a clear overview of the file system hierarchy in Linux."
meta_keywords: "linux file system hierarchy, file system hierarchy in linux, linux file hierarchy structure, linux file hierarchy, FSH, linux directory structure"
---

Linux presents mounted filesystems as one directory tree rooted at `/`. The Filesystem Hierarchy Standard, or FHS, gives many directories conventional roles, but distributions, containers, immutable systems, and local policy can differ. Inspect the actual host before relying on a path.

```bash
$ ls -ld /*
```

## Root and Essential System Paths

- `/` is the root of the visible filesystem tree.
- `/etc` holds host-specific system configuration. It can contain executable helper or startup scripts, so it is inaccurate to say it never contains executable content.
- `/boot` holds boot-related files such as boot-loader data and, on many systems, kernels and initial RAM filesystem images.
- `/bin` and `/sbin` traditionally contain essential user and system-administration commands.
- `/lib` and architecture-specific variants traditionally contain essential shared libraries and loader components.

Many current distributions use a merged `/usr` layout in which `/bin`, `/sbin`, and `/lib` are symbolic links into corresponding `/usr` directories. Use command discovery and package records rather than assuming whether a path is a physical directory or link.

:::single-choice{#filesystem-hierarchy-configuration-directory} Which directory conventionally contains host-specific system configuration?

::option[`/proc`]{#filesystem-hierarchy-proc-config explanation="Procfs presents live process and kernel interfaces rather than persistent host configuration files."}
::option[`/etc`]{#filesystem-hierarchy-etc .correct explanation="System and service configuration is conventionally organized under `/etc`."}
::option[`/dev`]{#filesystem-hierarchy-dev-config explanation="`/dev` contains runtime device-facing objects, not the general configuration hierarchy."}
:::

## Distribution and Local Software

- `/usr` contains the main shareable, largely read-only operating-system and application hierarchy, including commands, libraries, and architecture-independent data.
- `/usr/local` is reserved for software and data installed by the local administrator outside the distribution's normal `/usr` management.
- `/opt` can hold add-on application packages in self-contained subtrees.

Despite its name, `/usr` is not where individual users' personal files normally live. Distribution package managers commonly own large parts of it, so copying locally compiled files into `/usr/bin` can conflict with managed packages.

:::single-choice{#filesystem-hierarchy-local-software} Which prefix is conventionally reserved for software installed locally outside distribution-managed `/usr` content?

::option[`/usr/local`]{#filesystem-hierarchy-usr-local .correct explanation="The local hierarchy separates administrator-installed software from the distribution's main `/usr` tree."}
::option[`/proc/local`]{#filesystem-hierarchy-proc-local explanation="Procfs is a virtual kernel interface and not a persistent software prefix."}
::option[`/dev/local`]{#filesystem-hierarchy-dev-local explanation="Device-node storage is not the conventional location for local applications."}
:::

## User and Service Data

- `/home` conventionally contains non-root users' home directories, though directory services and local policy can place them elsewhere.
- `/root` is the root account's conventional home directory.
- `/srv` is intended for site-specific data served by this system.

A home path comes from account information, not merely from joining `/home` with a username. Use `getent passwd USER` or the shell's resolved home rather than hard-coding assumptions.

:::single-choice{#filesystem-hierarchy-root-home} What is the root account's conventional home directory?

::option[`/home/root`]{#filesystem-hierarchy-home-root explanation="Ordinary home directories often appear below `/home`, but root has a distinct conventional path."}
::option[`/root`]{#filesystem-hierarchy-root .correct explanation="The privileged account's home is conventionally located directly under the filesystem root."}
::option[`/usr/root`]{#filesystem-hierarchy-usr-root explanation="`/usr` is the software and shared-data hierarchy, not root's home."}
:::

## Variable, Runtime, and Temporary Data

- `/var` contains variable data such as logs, caches, spools, and application state. System logs commonly appear under `/var/log`, though some systems rely primarily on a journal interface.
- `/run` contains volatile runtime state for the current boot, such as sockets, service state, and PID files. It is normally recreated at boot.
- `/tmp` is for temporary files and is commonly writable by all users with sticky-bit protection.
- `/var/tmp` is intended for temporary files that should survive longer than files in `/tmp`.

Cleanup policy for `/tmp` varies; do not assume files persist until reboot or are always deleted at reboot. Applications should use secure temporary-file creation rather than predictable names.

:::single-choice{#filesystem-hierarchy-log-path} Which path conventionally stores system log files?

::option[`/etc/log`]{#filesystem-hierarchy-etc-log explanation="`/etc` is for configuration rather than ordinary accumulating log data."}
::option[`/var/log`]{#filesystem-hierarchy-var-log .correct explanation="Logs are a category of changing system data organized under the variable-data hierarchy."}
::option[`/boot/log`]{#filesystem-hierarchy-boot-log explanation="`/boot` is reserved for boot-related artifacts, not general service logs."}
:::

## Devices, Kernel Interfaces, and Mount Points

- `/dev` contains device nodes and related runtime links.
- `/proc` exposes process and kernel interfaces through procfs.
- `/sys` exposes kernel objects, devices, drivers, and attributes through sysfs.
- `/media` is commonly used for automatically mounted removable media.
- `/mnt` is a conventional location for temporary administrator mounts.

These are conventions, not permission grants. Mounting another filesystem on a nonempty directory temporarily hides the directory's previous contents until unmounted.

:::single-choice{#filesystem-hierarchy-sysfs-path} Which path normally exposes the kernel device model through sysfs?

::option[`/srv`]{#filesystem-hierarchy-srv explanation="`/srv` is intended for data served by the system."}
::option[`/sys`]{#filesystem-hierarchy-sys .correct explanation="Sysfs is conventionally mounted at `/sys` and presents devices, drivers, buses, and attributes."}
::option[`/opt`]{#filesystem-hierarchy-opt explanation="`/opt` holds optional add-on application trees."}
:::

Use [Navigate the Filesystem in Linux](https://labex.io/labs/comptia-navigate-the-filesystem-in-linux-590971) to inspect these paths, and [Find Files and Commands in Linux](https://labex.io/labs/comptia-find-files-and-commands-in-linux-590834) to avoid relying on guessed locations.

## Summary

You can now relate major Linux paths to their intended roles while allowing for real system variation.

1. Start from the unified tree rooted at `/`.
2. Separate configuration, managed software, local software, and variable data.
3. Distinguish homes and service data from runtime state.
4. Recognize `/dev`, `/proc`, and `/sys` as special runtime interfaces.
5. Inspect symlinks, mounts, account data, and distribution policy before assuming a layout.
