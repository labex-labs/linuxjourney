---
lesson_id: "kernel-installation"
course_id: "kernel"
lang: "en"
order_index: 4
title: "Kernel Installation"
description: "Learn how to install, boot, verify, and retain a distribution kernel with a tested fallback."
meta_title: "Kernel Installation - Kernel"
meta_description: "Learn how to install and manage Linux kernels. Discover kernel versions, use `uname -r`, and apt commands. Start your Linux kernel journey!"
meta_keywords: "Linux kernel, install kernel, uname -r, apt dist-upgrade, kernel management, Linux tutorial, beginner Linux, Linux guide"
---

Distributions package kernels together with modules, initramfs integration, boot-loader updates, signatures, and support policy. Use that managed workflow unless you are deliberately developing or testing a custom kernel and can recover the machine.

## Running and Installed Kernels

Show the release of the kernel currently running:

```bash
$ uname -r
6.8.0-00-generic
```

This does not list every installed kernel and does not change immediately when a newer package is installed. The system must boot the new image before `uname -r` reports it. Query installed packages and boot entries with the distribution's own tools.

:::single-choice{#kernel-installation-uname-release}
What does `uname -r` display?

::option[The release string of the currently running kernel.]{#kernel-installation-running-release .correct explanation="It reports live kernel state, not merely the newest image stored on disk."}
::option[Every kernel package available in all repositories.]{#kernel-installation-all-packages explanation="Repository inventory belongs to the package manager."}
::option[The firmware version of every attached device.]{#kernel-installation-device-firmware explanation="Kernel release and device firmware inventories are different data."}
:::

## Prefer the Distribution Tracking Package

Install or retain the distribution's supported kernel tracking or meta-package so future security updates continue to arrive. Package names depend on release, architecture, hardware class, and kernel flavor. For example, Ubuntu commonly offers `linux-generic`, but cloud, low-latency, HWE, OEM, real-time, and architecture-specific systems use other packages.

Do not turn a version string from `uname -r` directly into an `apt install` operand and assume it is valid. Consult the current distribution documentation and inspect candidates with the package manager before installation.

:::single-choice{#kernel-installation-meta-package}
Why is a supported kernel meta-package useful?

::option[It guarantees that no reboot is ever required.]{#kernel-installation-no-reboot explanation="A newly installed kernel becomes active only after a boot into it, barring specialized live-patching scope."}
::option[It converts every out-of-tree driver into built-in code.]{#kernel-installation-convert-drivers explanation="External modules still require compatible builds and signing."}
::option[It tracks the distribution's intended sequence of kernel updates.]{#kernel-installation-update-tracking .correct explanation="Dependencies move the system to newer supported image and module packages as updates are published."}
:::

## Preflight the Change

Before a kernel transaction:

1. Confirm supported repositories, package signatures, release lifecycle, and the intended kernel flavor.
2. Ensure `/boot` or the EFI System Partition has enough space.
3. Preserve at least one known-good installed kernel and a selectable boot entry.
4. Verify console, remote-management, rescue-media, encryption-recovery, and rollback access.
5. Check out-of-tree modules, storage and network drivers, Secure Boot signing, hibernation, and virtualization compatibility.

The package transaction should generate a matching initramfs and update boot entries through distribution hooks. Read every error; a package marked installed is not sufficient if initramfs or loader generation failed.

:::single-choice{#kernel-installation-initramfs-error}
Why must an initramfs-generation error block an assumed-success conclusion?

::option[Initramfs generation changes the user's shell password.]{#kernel-installation-initramfs-password explanation="The boot archive workflow is unrelated to account authentication secrets."}
::option[The new kernel may lack early modules or tools needed to reach root storage.]{#kernel-installation-missing-early-tools .correct explanation="An image can be installed while its required early user-space artifact is absent or stale."}
::option[The error proves the currently running kernel has already stopped.]{#kernel-installation-current-stopped explanation="Package hooks run while the old kernel can remain active."}
:::

## Boot and Validate

Schedule a controlled reboot with stakeholders and active workloads accounted for. Ensure the console can select the older entry if the default fails. After boot:

```bash
$ uname -r
$ journalctl -k -b
$ systemctl --failed
```

Use equivalent tools on non-systemd systems. Validate storage, filesystems, networking, graphics, input, security modules, external modules, containers, virtual machines, and application health. A login prompt alone is not complete validation.

:::single-choice{#kernel-installation-activation}
When does a newly installed ordinary kernel package become the running kernel?

::option[As soon as `uname -r` is typed.]{#kernel-installation-uname-activates explanation="Uname is read-only and cannot switch kernels."}
::option[After the machine boots that kernel image.]{#kernel-installation-after-boot .correct explanation="Installing files does not replace the kernel already executing in memory."}
::option[When the package archive is downloaded but before installation.]{#kernel-installation-download-activates explanation="A downloaded archive has no effect on live execution."}
:::

## Removing Older Kernels

Use the package manager's supported cleanup workflow only after the new kernel has passed validation. Never remove the currently running kernel, the only known-good fallback, or packages required by the active tracking package. Review the exact proposed removal and resulting boot entries.

Manual deletion from `/boot` leaves package and loader state inconsistent. If space is already exhausted, create a recovery plan before changing files rather than deleting arbitrary images.

:::single-choice{#kernel-installation-old-kernel-removal}
Which kernel should remain installed during initial validation of a new one?

::option[Only the untested new kernel.]{#kernel-installation-only-new explanation="Removing all fallbacks before testing converts a compatibility issue into a recovery incident."}
::option[No kernel files at all under the boot path.]{#kernel-installation-no-kernels explanation="The machine needs a loadable kernel artifact to boot Linux."}
::option[A known-good fallback selectable by the boot loader.]{#kernel-installation-known-good-fallback .correct explanation="The fallback provides a recovery path when the new kernel fails on hardware or workloads."}
:::

The [Customize the GRUB2 Boot Menu](https://labex.io/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859) lab provides a recovery-safe environment for understanding multiple entries.

## Summary

You can now treat a kernel update as a boot-chain and compatibility change.

1. Distinguish the running release from installed images.
2. Track supported updates through the correct distribution package.
3. Preflight storage, initramfs, signatures, modules, and recovery access.
4. Boot and validate hardware and application behavior.
5. Retain a known-good fallback until the new kernel is proven.
