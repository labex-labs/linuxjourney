---
index: 5
lang: "en"
title: "CIDR"
meta_title: "CIDR - Subnetting"
meta_description: "A guide to CIDR notation. Learn about the CIDR format, cidr subnetting, and how to calculate hosts for your network, including on an Ubuntu server. Master IP addressing with CIDR."
meta_keywords: "CIDR, cidr subnetting, cidr format, subnet mask, IP addressing, ubuntu server subnet cidr, ubuntu subnet cidr, network prefix, Linux networking"
---

## Lesson Content

CIDR (Classless Inter-Domain Routing) is a method for allocating IP addresses and routing Internet Protocol packets. It offers a more compact and efficient way to represent a subnet mask, replacing the older classful network design. Understanding CIDR is essential for modern network administration.

### The CIDR Format

You will often see networks notated using the **CIDR format**, where an IP address is followed by a slash and a number. For example, a subnet like `10.42.3.0` with a subnet mask of `255.255.255.0` is written as `10.42.3.0/24`. This single notation includes both the network address and the prefix length.

The number after the slash indicates how many bits of the IP address are used for the network prefix. This is a common task when configuring networking on a system like an **Ubuntu server**, where you might define an interface with an `ubuntu subnet cidr` address.

### CIDR Subnetting and Host Calculation

An IPv4 address consists of 4 bytes, which is a total of 32 bits. The CIDR prefix determines the split between the network portion and the host portion of the address. For effective **cidr subnetting**, you need to know how to calculate the number of available hosts.

Let's take the example `123.12.24.0/23`. This means the first 23 bits are the network prefix. To find the number of available hosts:

1. Subtract the CIDR prefix from the total number of bits (32): `32 - 23 = 9`. This leaves 9 bits for the host portion.
2. Calculate the total number of addresses in the subnet: `2^9 = 512`.
3. Subtract 2 from the total. One address is reserved for the network itself, and one is for the broadcast address. This leaves `512 - 2 = 510` usable host addresses.

Another common example is a `/30` network, which provides `32 - 30 = 2` host bits. This results in `2^2 = 4` total addresses, leaving just 2 usable addresses, making it ideal for point-to-point links.

## Exercise

To master these concepts, practice with some hands-on labs that reinforce your understanding of CIDR, IP addressing, and **cidr subnetting**:

1. **[Perform IP Subnetting and Binary Conversion in the Linux Terminal](https://labex.io/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Master IP subnetting and binary conversion, including translating CIDR masks and calculating usable hosts.
2. **[Simulate Network Layer Connectivity in Linux](https://labex.io/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Learn to assign static IP addresses and observe how IP subnets govern direct network communication in a simulated environment.
3. **[Explore IP Address Types and Reachability in Linux](https://labex.io/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Explore IP addressing and network reachability using commands like `ping` and `ip a` to test various IP types and connectivity.

These labs will help you apply the concepts of CIDR and IP addressing in real-world scenarios and build confidence with network configuration.

## Quiz Question

## Quiz Answer
