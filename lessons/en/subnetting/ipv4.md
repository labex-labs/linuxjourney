---
index: 1
lang: "en"
title: "IPv4"
meta_title: "IPv4 - Subnetting"
meta_description: "Start your journey with our complete linux tutorial on IPv4 addresses. This guide for beginner linux users is the best way to learn linux networking, covering IP structure and essential command-line tools like ip addr."
meta_keywords: "IPv4, IP address, beginner linux, best way to learn linux, complete linux tutorial, best linux course online free, free linux certification courses, linux networking, ifconfig, ip addr"
---

## Lesson Content

Every device on a network has a unique identifier called an IP (Internet Protocol) address. This lesson, a key part of our `complete linux tutorial`, focuses on IPv4 addresses—the most common type you'll encounter. For any `beginner linux` user, understanding IPv4 is a critical first step into the world of networking.

### Why IPv4 is Essential

Learning about IPv4 is fundamental for anyone serious about system administration or network management. It forms the backbone of most network communication. This guide offers the `best way to learn linux` networking from the ground up. While this isn't one of those `free linux certification courses`, mastering these basics is a key step toward professional certification.

### IPv4 Address Structure

An IPv4 address is a 32-bit number, but it's usually shown in a human-readable format like this:

```
204.23.124.23
```

This address has two main parts: the **network portion**, which identifies the network, and the **host portion**, which identifies the specific device on that network. The address is divided into four sections separated by periods, with each section called an **octet**. An octet is a group of 8 bits, meaning an IPv4 address is 4 bytes (32 bits) long. Understanding this structure is crucial for network configuration and troubleshooting.

### Finding Your IP Address

One of the first tasks for any Linux user is to find their system's IP address. You can do this using simple command-line tools. The traditional command for this is `ifconfig`. While it is still found on many systems, it is considered a legacy tool.

```bash
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
```

In the output above, the IPv4 address is `192.168.1.129`.

### Using the ip addr Command

The modern and recommended method uses the `ip` command. The `ip addr` command has replaced `ifconfig` and is the standard on most current Linux distributions. It provides more detailed information and is the tool you should focus on learning.

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
