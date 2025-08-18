---
lang: "en"
title: "mount and umount"
meta_description: "Learn how to use the Linux mount and umount commands to manage filesystems. Understand device mounting, unmounting, and UUIDs for beginners."
meta_keywords: "Linux mount, umount command, mount filesystem, Linux UUID, beginner Linux, Linux tutorial, mount point, Linux guide"
---

## Lesson Content

Before you can view the contents of your filesystem, you will have to mount it. To do that, I'll need the device location, the filesystem type, and a mount point. The mount point is a directory on the system where the filesystem is going to be attached. So, we basically want to mount our device to a mount point.

First, create the mount point; in our case, **mkdir /mydrive**.

```bash
sudo mount -t ext4 /dev/sdb2 /mydrive
```

Simple as that! Now, when we go to /mydrive, we can see our filesystem contents. The **-t** specifies the type of filesystem, then we have the device location, then the mount point.

To unmount a device from a mount point:

```bash
sudo umount /mydrive
```

or

```bash
sudo umount /dev/sdb2
```

Remember that the kernel names devices in the order it finds them. What if our device name changes for some reason after we mount it? Well, fortunately, you can use a device's universally unique ID (UUID) instead of a name.

To view the UUIDs on your system for block devices:

```bash
pete@icebox:~$ sudo blkid
/dev/sda1: UUID="130b882f-7d79-436d-a096-1e594c92bb76" TYPE="ext4"
/dev/sda5: UUID="22c3d34b-467e-467c-b44d-f03803c2c526" TYPE="swap"
/dev/sda6: UUID="78d203a0-7c18-49bd-9e07-54f44cdb5726" TYPE="xfs"
```

We can see our device names, their corresponding filesystem types, and their UUIDs. Now, when we want to mount something, we can use:

```bash
sudo mount UUID=130b882f-7d79-436d-a096-1e594c92bb76 /mydrive
```

Most of the time, you won't need to mount devices via their UUIDs; it's much easier to use the device name, and often times the operating system will know to mount common devices like USB drives. If you need to automatically mount a filesystem at startup, though, like if you added a secondary hard drive, you'll want to use the UUID, and we'll go over that in the next lesson.

## Exercise

Look at the manpage for `mount` and `umount` and see what other options you can use.

## Quiz Question

What command is used to attach a filesystem?

## Quiz Answer

mount
