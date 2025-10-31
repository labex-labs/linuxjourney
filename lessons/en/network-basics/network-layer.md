---
index: 7
lang: "en"
title: "Network Layer"
meta_title: "Network Layer - Network Basics"
meta_description: "Explore the Network layer in Linux networking. This guide explains how IP addresses and subnets enable packet routing for data transmission across networks."
meta_keywords: "Network layer, IP addresses, subnets, Linux networking, packet routing, data transmission, OSI model, IP packet"
---

## Lesson Content

The Network layer is responsible for the logical addressing and routing of data packets from a source host to a destination host. While a packet might sometimes travel within a single local network, the internet is a vast collection of interconnected networks.

### The Role of Packet Routing

The primary function of the Network layer is to determine the optimal path for data to travel. This process, known as **packet routing**, ensures that information reaches its intended destination efficiently, even if it needs to cross multiple network boundaries. In **Linux networking**, this layer is fundamental for all internet communication.

### Understanding Subnets and IP Addresses

The smaller networks that constitute the internet are called **subnets**. All subnets are connected, which allows a device on one network to communicate with a device on another, such as accessing a website like `google.com`. The rules for traveling between these different subnets are defined by **IP addresses**. An IP address provides a unique identifier for a device on a network, much like a street address for a house.

### Encapsulation at the Network Layer

At the Network layer, the data segment received from the Transport layer is encapsulated into a new unit called an IP packet. During this process, a header is added to the packet, which includes the source IP address (where the packet came from) and the destination IP address (where it is going). With this crucial addressing information attached, the packet now has everything it needs for its journey and is passed down to the Data Link layer to be prepared for physical transmission.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of the Network layer, IP addressing, and subnets:

1. **[Simulate Network Layer Connectivity in Linux](https://labex.io/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Practice assigning static IP addresses and testing connectivity within and across different subnets using Docker containers.
2. **[Perform IP Subnetting and Binary Conversion in the Linux Terminal](https://labex.io/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Master IP subnetting and binary conversion, including calculating usable hosts and subnets, directly in the Linux terminal.
3. **[Explore IP Address Types and Reachability in Linux](https://labex.io/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Explore various IP address types (private, public, multicast) and test network reachability using `ping` and `ip a`.

These labs will help you apply the concepts of IP addressing and subnetting in real scenarios and build confidence with Network layer fundamentals.

## Quiz Question

What are the smaller networks that make up the Internet called? Please answer using a single, lowercase English word.

## Quiz Answer

subnets
