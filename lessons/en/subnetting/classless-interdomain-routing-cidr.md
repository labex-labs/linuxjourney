---
index: 5
lang: "en"
title: "CIDR"
meta_title: "CIDR - Subnetting"
meta_description: "Learn CIDR notation for Linux networking. Understand subnet masks, IP addressing, and host calculation with this beginner-friendly guide. Improve your network skills!"
meta_keywords: "CIDR, subnet mask, IP addressing, network prefix, Linux networking, beginner, tutorial, guide"
---

## Lesson Content

CIDR (Classless Inter-Domain Routing) is used to represent a subnet mask in a more compact way. You may see subnets notated in CIDR notation, where a subnet such as 10.42.3.0/255.255.255.0 is written as 10.42.3.0/24. This notation includes both the subnet prefix and the subnet mask.

Remember, an IP address consists of 4 bytes or 32 bits. CIDR indicates the number of bits used as the network prefix. So, 123.12.24.0/23 means that the first 23 bits are used. What does that mean? How many hosts is that?

A simple trick is to subtract the CIDR address (23) from the total number of bits an IP address can have (32). This leaves 9 bits. Therefore, 2^9 = 512. However, we must remove 2 addresses (the subnet address and the broadcast address), so we have 510 usable hosts.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of CIDR, IP addressing, and subnetting:

1. **[Perform IP Subnetting and Binary Conversion in the Linux Terminal](https://labex.io/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Master IP subnetting and binary conversion, including translating CIDR masks and calculating usable hosts.
2. **[Simulate Network Layer Connectivity in Linux](https://labex.io/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Learn to assign static IP addresses and observe how IP subnets govern direct network communication in a simulated environment.
3. **[Explore IP Address Types and Reachability in Linux](https://labex.io/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Explore IP addressing and network reachability using commands like `ping` and `ip a` to test various IP types and connectivity.

These labs will help you apply the concepts of CIDR and IP addressing in real scenarios and build confidence with network configuration.

## Quiz Question

No questions, move along!

## Quiz Answer
