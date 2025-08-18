---
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

No exercises for this lesson.

## Quiz Question

No questions, move along!

## Quiz Answer
