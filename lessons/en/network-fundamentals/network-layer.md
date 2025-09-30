---
index: 7
lang: "en"
title: "Network Layer"
meta_title: "Network Layer - Network Basics"
meta_description: "Learn about the Network layer in Linux, how IP addresses route packets across subnets, and its role in data transmission. Start your Linux networking journey!"
meta_keywords: "Network layer, IP addresses, subnets, Linux networking, packet routing, beginner, tutorial, guide"
---

## Lesson Content

The Network layer determines the routing of our packets from our source host to a destination host. Fortunately, in our example, our packet is only traveling within the same network, but the Internet is made up of many networks. These smaller networks that make up the Internet are known as subnets. All subnets connect to each other in some way, which is why we are able to get to `https://www.google.com` even though it's on its own network. I won't go into detail as we have a whole course dedicated to subnets, but for now, in regards to our Network layer, know that the IP addresses define the rules to travel to different subnets.

In the Network layer, it receives the segment coming from the Transport layer and encapsulates this segment in an IP packet, then attaches the IP address of the source host and the IP address of the destination host to the packet header. So at this point, our packet has information about where it is going and where it came from. Now it sends our packet to the physical hardware layer.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of the Network layer, IP addressing, and subnets:

1. **[Simulate Network Layer Connectivity in Linux](https://labex.io/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Practice assigning static IP addresses and testing connectivity within and across different subnets using Docker containers.
2. **[Perform IP Subnetting and Binary Conversion in the Linux Terminal](https://labex.io/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Master IP subnetting and binary conversion, including calculating usable hosts and subnets, directly in the Linux terminal.
3. **[Explore IP Address Types and Reachability in Linux](https://labex.io/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Explore various IP address types (private, public, multicast) and test network reachability using `ping` and `ip a`.

These labs will help you apply the concepts of IP addressing and subnetting in real scenarios and build confidence with Network layer fundamentals.

## Quiz Question

What are smaller networks that make up the Internet called?

## Quiz Answer

subnets
