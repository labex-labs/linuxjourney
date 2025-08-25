---
index: 8
lang: "en"
title: "swap"
meta_title: "swap - The Filesystem"
meta_description: "Learn about Linux swap space, how it works, and how to create and manage swap partitions. Optimize your system's memory usage with this guide!"
meta_keywords: "Linux swap, mkswap, swapon, swapoff, /etc/fstab, virtual memory, Linux beginner, Linux tutorial"
---

## Lesson Content

In our previous example, I showed you how to see your partition table. Let's revisit that example, more specifically this line:

```
Number  Start   End     Size    Type      File system     Flags
 5      6861MB  7380MB  519MB   logical   linux-swap(v1)
```

What is this swap partition? Well, swap is what we use to allocate virtual memory to our system. If you are low on memory, the system uses this partition to "swap" pieces of memory of idle processes to the disk, so you're not bogged down for memory.

### Using a partition for swap space

Let's say we wanted to set our partition `/dev/sdb2` to be used for swap space.

1. First, make sure we don't have anything on the partition.
2. Run: `mkswap /dev/sdb2` to initialize swap areas.
3. Run: `swapon /dev/sdb2`. This will enable the swap device.
4. If you want the swap partition to persist on bootup, you need to add an entry to the `/etc/fstab` file. `sw` is the filesystem type that you'll use.
5. To remove swap: `swapoff /dev/sdb2`.

Generally, you should allocate about twice as much swap space as you have memory. However, modern systems today are usually powerful enough and have enough RAM as it is.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of Linux swap space and virtual memory management:

1. **[Create and Activate a Swap File in Linux](https://labex.io/labs/comptia-create-and-activate-a-swap-file-in-linux-590858)** - Practice creating and activating a swap file, a crucial skill for managing your system's virtual memory.

This lab will help you apply the concepts of swap partitions in real scenarios and build confidence with system resource management.

## Quiz Question

What is the command to enable swap space on a device?

## Quiz Answer

swapon
