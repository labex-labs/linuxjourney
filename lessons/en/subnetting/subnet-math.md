---
index: 3
lang: "en"
title: "Subnet Math"
meta_title: "Subnet Math - Subnetting"
meta_description: "Learn subnet math basics and how to calculate available hosts on a network. Understand IP addressing and subnet masks for beginners. Start your Linux journey!"
meta_keywords: "subnet math, IP address, subnet mask, network hosts, binary, Linux networking, beginner tutorial, guide"
---

## Lesson Content

Okay, we know that subnet masks are important to figure out how many hosts we can have on our subnet. So how many hosts would that be?

Let's say I have an IP address of **192.168.1.0** and a subnet mask of **255.255.255.0**. Now, let's line up these numbers in binary form. For now, use an online calculator to convert these values from decimal to binary.

```
192.168.1.165  = 11000000.10101000.00000001.10100101
255.255.255.0  = 11111111.11111111.11111111.00000000
```

The IP address is masked by our subnet mask. When you see a 1, it is masked, and we pretend like we don't see it. So the only possible hosts we can have are from the `00000000` region. Remember, `11111111` in binary form equals 255. We also account for 0 as a host number, so there are 256 possible options. However, it may look like we have 256 possible options, but we actually subtract 2 hosts because we have to account for the broadcast address and the subnet address, leaving us with 254 possible hosts on our subnet. So we know that we can have hosts with IP addresses ranging from 192.168.1.1 - 192.168.1.254.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of IP addressing and subnetting:

1. **[Perform IP Subnetting and Binary Conversion in the Linux Terminal](https://labex.io/labs/linux-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Master IP subnetting and binary conversion, essential skills for network configuration and planning.
2. **[Explore IP Address Types and Reachability in Linux](https://labex.io/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** - Deepen your understanding of various IP address types and how to verify network reachability using Linux commands.
3. **[Simulate Network Layer Connectivity in Linux](https://labex.io/labs/linux-simulate-network-layer-connectivity-in-linux-592752)** - Apply your knowledge by simulating network configurations and testing connectivity between different IP subnets in a practical environment.

These labs will help you apply the concepts of IP addressing, subnet masks, and host calculation in real scenarios and build confidence with network fundamentals.

## Quiz Question

What is the binary equivalent of 255?

## Quiz Answer

11111111
