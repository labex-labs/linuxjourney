---
lesson_id: "listing-devices"
course_id: "devices"
lang: "en"
order_index: 6
title: "lsusb, lspci, lsscsi"
description: "Learn how to inspect USB topology, PCI functions, SCSI-layer devices, and their active drivers."
meta_title: "lsusb, lspci, lsscsi - Devices"
meta_description: "Discover how to list and inspect USB, PCI, and SCSI hardware on your Linux system. This guide covers the lsusb, lspci, and lsscsi commands, including options like lsusb -t to view device trees."
meta_keywords: "lsusb, lspci, lsscsi, lsusb -t, list usb devices, list pci devices, list scsi devices, linux hardware, device information"
---

Linux offers bus- and subsystem-specific inventory tools. Each command shows a different view, so combine their identifiers, topology, drivers, sysfs paths, and logs instead of expecting one complete hardware list.

## Inspecting USB Devices

`lsusb` lists USB devices visible through the USB subsystem:

```bash
$ lsusb
```

Output normally includes bus and device numbers, a vendor and product ID pair, and a description from the local USB ID database. The numeric bus/device address can change after reconnecting or rebooting and should not be treated as a persistent identity.

Display controller, hub, port, interface, driver, and speed relationships with:

```bash
$ lsusb -t
```

Verbose descriptor output is available, but some details require elevated read access. Do not grant broad USB-device permissions merely to make an inspection command quieter.

:::single-choice{#listing-devices-usb-tree}
Which command displays USB devices as a topology tree?

::option[`lspci -k`]{#listing-devices-lspci-tree explanation="This lists PCI functions and kernel-driver information rather than USB topology."}
::option[`lsscsi -t`]{#listing-devices-lsscsi-tree explanation="This is not the introduced USB tree command."}
::option[`lsusb -t`]{#listing-devices-lsusb-tree .correct explanation="The tree option shows devices below controllers and hubs with port and interface relationships."}
:::

## Inspecting PCI Functions

`lspci` lists functions discovered on PCI and PCI Express buses:

```bash
$ lspci
```

Internal and externally attached PCIe devices can include graphics, network, storage, USB, audio, and bridge controllers. Show the kernel driver in use and candidate modules with:

```bash
$ lspci -k
```

A PCI controller appearing in this list does not prove that every device behind it is initialized or healthy. Check the driver binding and kernel logs when troubleshooting.

:::single-choice{#listing-devices-pci-driver}
Which command adds kernel-driver information to a PCI listing?

::option[`lspci -k`]{#listing-devices-lspci-k .correct explanation="The `-k` option displays the active kernel driver and modules capable of handling each PCI device."}
::option[`lsusb -t`]{#listing-devices-usb-not-pci explanation="This describes USB hierarchy and interface drivers."}
::option[`lsblk -f`]{#listing-devices-lsblk-filesystem explanation="This reports block-device and filesystem fields, not PCI driver binding."}
:::

## Inspecting SCSI-Layer Devices

`lsscsi` lists devices represented through the Linux SCSI mid-layer:

```bash
$ lsscsi
```

This can include native SCSI devices and SATA, USB-storage, or virtual disks presented through SCSI-compatible layers. NVMe namespaces normally belong to a different subsystem and are not comprehensively inventoried by `lsscsi`.

For a storage-oriented hierarchy that includes many block-device types, use `lsblk` as well:

```bash
$ lsblk -o NAME,TYPE,SIZE,MODEL,SERIAL,TRAN,FSTYPE,MOUNTPOINTS
```

:::single-choice{#listing-devices-lsscsi-scope}
What does `lsscsi` primarily list?

::option[Every NVMe namespace and controller exclusively.]{#listing-devices-only-nvme explanation="NVMe uses its own subsystem and tools, although related block views can appear elsewhere."}
::option[Only files whose names end in `.scsi`.]{#listing-devices-scsi-extension explanation="The command queries kernel device interfaces rather than filename extensions."}
::option[Devices represented through the Linux SCSI mid-layer.]{#listing-devices-scsi-mid-layer .correct explanation="The command reports SCSI hosts, targets, logical units, and corresponding device nodes where available."}
:::

## Interpreting Inventory Results

Descriptions often come from local ID databases and can be generic or stale. A listed device can lack a working driver, and a virtualized environment can present emulated or paravirtual hardware. Correlate results with `udevadm info`, sysfs, `lsblk`, network tools, and `journalctl -k` or `dmesg` according to permissions and the problem being investigated.

The utilities may be packaged separately, commonly through packages such as `usbutils`, `pciutils`, and `lsscsi`. Use the distribution package manager rather than downloading unknown replacements when a command is absent.

:::single-choice{#listing-devices-listed-not-working}
Does seeing a device in `lspci` prove its driver is active and functioning correctly?

::option[No; inspect driver binding and relevant kernel messages too.]{#listing-devices-needs-correlation .correct explanation="Enumeration establishes that a PCI function is visible, not that higher-level initialization succeeded."}
::option[Yes; PCI enumeration performs a complete functional test.]{#listing-devices-complete-test explanation="The listing does not exercise every hardware function or validate service behavior."}
::option[Yes; `lspci` installs a suitable driver automatically.]{#listing-devices-installs-driver explanation="The command is an inventory tool and does not install driver packages."}
:::

Use [Explore Hardware Devices in Linux](https://labex.io/labs/comptia-explore-hardware-devices-in-linux-590861) to compare these subsystem views on one controlled host.

## Summary

You can now select an inventory command for the device subsystem in question.

1. Use `lsusb` and `lsusb -t` for USB identity and topology.
2. Use `lspci -k` for PCI functions and driver binding.
3. Use `lsscsi` for SCSI-layer devices and `lsblk` for block topology.
4. Correlate enumeration with drivers, sysfs, and kernel messages.
