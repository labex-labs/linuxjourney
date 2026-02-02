---
index: 6
lang: "en"
title: "lsusb, lspci, lsscsi"
meta_title: "lsusb, lspci, lsscsi - Devices"
meta_description: "Discover how to list and inspect USB, PCI, and SCSI hardware on your Linux system. This guide covers the lsusb, lspci, and lsscsi commands, including options like lsusb -t to view device trees."
meta_keywords: "lsusb, lspci, lsscsi, lsusb -t, list usb devices, list pci devices, list scsi devices, linux hardware, device information"
---

## Lesson Content

Just as you use the `ls` command to list files, Linux provides similar tools for listing hardware devices. These commands are essential for identifying the hardware connected to your system.

### Listing USB Devices with lsusb

To see all the USB devices connected to your system, you can use the `lsusb` command. This command scans the USB hubs and reports information about the devices it finds, such as webcams, keyboards, and external drives.

```bash
lsusb
```

For a more structured view, you can use the `lsusb -t` command. This option displays the USB devices in a tree-like structure, which is helpful for understanding how devices are physically connected to the USB controllers and hubs.

### Listing PCI Devices with lspci

The `lspci` command is used to list all PCI (Peripheral Component Interconnect) devices. These are typically internal components connected to the motherboard, such as graphics cards, network adapters, and sound cards. This command provides a quick overview of your system's core hardware.

```bash
lspci
```

### Listing SCSI and SATA Devices with lsscsi

For storage devices, the `lsscsi` command is particularly useful. It lists all connected SCSI and SATA devices, which commonly include hard drives, SSDs, and optical drives (CD/DVD/Blu-ray). While other commands might show the storage controller, `lsscsi` provides direct information about the storage devices themselves, making it a valuable tool for system administrators and users managing storage.

```bash
lsscsi
```

## Exercise

To reinforce your understanding of exploring hardware devices in Linux, try the following hands-on lab:

1. **[Explore Hardware Devices in Linux](https://labex.io/labs/comptia-explore-hardware-devices-in-linux-590861)** - In this lab, you will learn the essential skills to explore, identify, and inspect hardware devices within a Linux environment. You will gain hands-on experience with powerful command-line utilities to understand how the operating system interacts with physical components.

This lab will help you apply these concepts in a real-world scenario and build confidence in managing device information.

## Quiz Question

What command is used to view a list of connected USB devices? (Please answer in lowercase English characters only.)

## Quiz Answer

lsusb
