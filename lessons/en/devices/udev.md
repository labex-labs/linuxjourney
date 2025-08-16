# udev

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

Run the `udevadm` command given and check out the output.

## Quiz Question

What dynamically adds and removes devices?

## Quiz Answer

udev
