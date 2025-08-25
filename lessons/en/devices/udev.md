---
index: 5
lang: "en"
title: "udev"
meta_title: "udev - Devices"
meta_description: "Learn about udev, how it dynamically manages Linux device files, and use udevadm. Understand device node creation for beginners."
meta_keywords: "udev, udevadm, Linux device management, device files, Linux tutorial, beginner Linux, udev rules, Linux guide"
---

## Lesson Content

Back in the old days, and actually today if you really wanted to, you would create device nodes using a command such as:

```bash
mknod /dev/sdb1 b 8 3
```

This command will make a device node `/dev/sdb1` and it will make it a block device (b) with a major number of 8 and a minor number of 3.

To remove a device, you would simply **rm** the device file in the `/dev` directory.

Luckily, we really don't need to do this anymore because of udev. The udev system dynamically creates and removes device files for us depending on whether or not they are connected. There is a `udevd` daemon that is running on the system, and it listens for messages from the kernel about devices connected to the system. `Udevd` will parse that information and match the data with the rules that are specified in `/etc/udev/rules.d`. Depending on those rules, it will most likely create device nodes and symbolic links for the devices. You can write your own udev rules, but that is a little out of scope for this lesson. Fortunately, your system already comes with lots of udev rules, so you may never need to write your own.

You can also view the udev database and sysfs using the **udevadm** command. This tool is very useful, but sometimes can get very convoluted. A simple command to view information for a device would be:

```bash
udevadm info --query=all --name=/dev/sda
```

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of hardware interaction and device management in Linux:

1. **[Explore Hardware Devices in Linux](https://labex.io/labs/comptia-explore-hardware-devices-in-linux-590861)** - In this lab, you will learn the essential skills to explore, identify, and inspect hardware devices within a Linux environment. You will gain hands-on experience with powerful command-line utilities to understand how the operating system interacts with physical components, which is crucial for understanding device nodes and udev's role.

This lab will help you apply the concepts in real scenarios and build confidence with Linux hardware management.

## Quiz Question

What dynamically adds and removes devices?

## Quiz Answer

udev
