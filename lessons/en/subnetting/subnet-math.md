---
title: "Subnet Math"
description: "Learn subnet math basics and how to calculate available hosts on a network. Understand IP addressing and subnet masks for beginners. Start your Linux journey!"
keywords: "subnet math, IP address, subnet mask, network hosts, binary, Linux networking, beginner tutorial, guide"
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

No exercises for this lesson.

## Quiz Question

What is the binary equivalent of 255?

## Quiz Answer

11111111
