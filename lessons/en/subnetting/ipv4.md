---
index: 1
lang: "en"
title: "IPv4"
meta_title: "IPv4 - Subnetting"
meta_description: "Discover the best way to learn Linux networking by understanding IPv4 addresses. This guide for beginners covers IP structure and how to find your IP using the command line."
meta_keywords: "IPv4, IP address, beginner linux, best way to learn linux, linux command line for beginners, ifconfig, ip addr, network basics"
---

## Lesson Content

Every device connected to a network has a unique address, known as an IP (Internet Protocol) address. For this course, we will focus on IPv4 addresses, which are the most common type you will encounter. Understanding them is a core part of learning networking on Linux.

An IPv4 address is a 32-bit number typically represented in a human-readable format, like this:

```
204.23.124.23
```

This address contains two distinct parts: the **network portion**, which identifies the specific network the device is on, and the **host portion**, which identifies the specific device on that network.

### The Structure of an IP Address

An IPv4 address is divided into four sections separated by periods. Each section is called an **octet**. In computer science, an octet is a group of 8 bits, and since 8 bits equal 1 byte, an IPv4 address is 4 bytes long. This structure is fundamental, and mastering it is one of the `best resources to learn linux command line for beginners` in networking.

### Finding Your IP Address on Linux

For any `beginner linux` user, one of the first tasks is to find the system's IP address. You can do this using command-line tools.

The traditional command for this is `ifconfig`. While it is still found on many systems, it is considered a legacy tool.

```bash
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
```

In the output above, the IPv4 address is `192.168.1.129`.

### The Modern Approach with ip addr

The `best way to learn linux` networking today involves using the modern `ip` command. The `ip addr` command has replaced `ifconfig` and is the standard on most current Linux distributions.

```bash
pete@icebox:~$ ip addr show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 1d:3a:32:24:4d:ce brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.129/24 brd 192.168.1.255 scope global dynamic eth0
       valid_lft 85646sec preferred_lft 85646sec
```

Here, you can find the same IPv4 address, `192.168.1.129`, listed next to `inet` for the `eth0` interface.

## Exercise

Practice your skills with these hands-on labs to reinforce your understanding of IP addressing and network identification in Linux:

1. **[Identify MAC and IP Addresses in Linux](https://labex.io/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Practice using the `ip a` command to identify network addressing information, including IPv4 and IPv6 addresses, on a Linux system.
2. **[Explore IP Address Types and Reachability in Linux](https://labex.io/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Explore different IP address types and test network reachability using commands like `ping` and `ip a`.
3. **[Perform IP Subnetting and Binary Conversion in the Linux Terminal](https://labex.io/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Master IP subnetting and binary conversion, essential for a deeper understanding of how IP addresses and networks are structured at the bit level.

These labs will help you apply the concepts of IP addressing in real scenarios and build confidence with network configuration and troubleshooting in Linux.

## Quiz Question

How many bytes are in an IPv4 address?

## Quiz Answer

4
