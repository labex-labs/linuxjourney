---
index: 8
lang: "en"
title: "Link Layer"
meta_title: "Link Layer - Network Basics"
meta_description: "Explore the fundamentals of the TCP/IP link layer. Learn how the link layer header is constructed, how ARP resolves IP addresses to MAC addresses, and the process of packet traversal on a local network."
meta_keywords: "link layer, link layer header, ARP, TCP/IP, MAC address, network fundamentals, Linux networking, packet traversal, address resolution protocol"
---

## Lesson Content

The **Link Layer** is the foundational layer of the TCP/IP model, responsible for communications on the local network segment. This layer is hardware-specific, dealing directly with network interface cards and physical addressing.

### Frames and the Link Layer Header

At the **link layer**, the packet from the network layer is encapsulated into a structure called a frame. A crucial part of this process is adding the **link layer header**. This header contains the source and destination MAC addresses of the hosts, checksums for error detection, and packet separators, which allow the receiving device to identify where one frame ends and the next begins.

To construct the **link layer header**, the system needs both the source and destination MAC addresses. While the source MAC address is known, the destination MAC address for an IP on the same local network must be discovered. This is where the Address Resolution Protocol (ARP) comes into play.

### ARP (Address Resolution Protocol)

ARP is a **link layer** protocol used to find the MAC address associated with a specific IP address within the same network. If the destination host were on a different network, the packet would be sent to a default gateway (router), and ARP would be used to find the router's MAC address.

Systems first consult their ARP lookup table, which caches known IP-to-MAC address mappings. If the required address is not in the cache, the system broadcasts an ARP request to the entire network. This special message asks which host has a specific IP address, for example, 10.10.1.4. The host with that IP address will send an ARP reply containing its IP and MAC address.

With all the necessary IP and MAC addresses, the **link layer** can now forward the frame through the network interface card. The journey of a packet is a multi-step process of encapsulation and de-encapsulation as it moves up and down the TCP/IP stack on both the sending and receiving ends.

### Packet Traversal

Here is a step-by-step breakdown of how a packet travels from a sender (Pete) to a receiver (Patty):

1. Pete sends Patty an email. This data is sent to the transport layer.
2. The transport layer encapsulates the data into a TCP or UDP header to form a segment. It attaches the destination and source ports, then sends the segment to the network layer.
3. The network layer encapsulates the segment inside an IP packet and attaches the source and destination IP addresses. It then routes the packet to the **link layer**.
4. The packet reaches the **link layer**, where it is encapsulated into a frame. The **link layer header**, containing the source and destination MAC addresses, is added.
5. Patty receives this data frame through her physical layer, checks the frame for data integrity, then de-encapsulates it and sends the IP packet to her network layer.
6. The network layer reads the packet to find the source and destination IP addresses. It confirms the destination IP matches its own, de-encapsulates the packet, and sends the segment to the transport layer.
7. The transport layer de-encapsulates the segment, checks the TCP or UDP port numbers, and makes a connection to the application layer based on those ports.
8. The application layer receives the data from the transport layer on the specified port and presents it to Patty as the final email message.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of the Link Layer, MAC addresses, and ARP:

1. **[Identify MAC and IP Addresses in Linux](https://labex.io/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Practice using the `ip a` command to identify network addressing information, including MAC addresses, on a Linux system.
2. **[Explore Network Layer Interaction with ping and arp in Linux](https://labex.io/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Learn how `ping` and `arp` commands work together to resolve IP addresses to MAC addresses and understand network layer interactions.
3. **[Analyze Ethernet Frames with tcpdump in Linux](https://labex.io/labs/comptia-analyze-ethernet-frames-with-tcpdump-in-linux-592765)** - Gain hands-on experience capturing and inspecting Ethernet frames, including MAC addresses, to understand low-level network communications.

These labs will help you apply the concepts in real scenarios and build confidence with network fundamentals at the Link Layer.

## Quiz Question

What protocol is used to find the MAC address of a host on the same local network? (Please answer with the English acronym in uppercase letters).

## Quiz Answer

ARP
