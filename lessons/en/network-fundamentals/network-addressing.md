---
index: 4
lang: "en"
title: "Network Addressing"
meta_title: "Network Addressing - Network Basics"
meta_description: "Learn network addressing basics: MAC vs. IP addresses, and hostnames. Understand how devices communicate on a network. Start your Linux networking journey!"
meta_keywords: "network addressing, MAC address, IP address, hostname, Linux networking, beginner, tutorial, guide"
---

## Lesson Content

Before we jump into seeing how a packet moves across a network, we have to familiarize ourselves with some terminology. When you mail a letter, you must know who it is being sent to and where it is coming from. Packets need the same information. Our hosts and other hosts are identified using MAC (Media Access Control) addresses and IP addresses. To make it easier on us humans, we use hostnames to identify a host.

### MAC Addresses

A MAC address is a unique identifier used as a hardware address. This address will never change. When you want to get access to the Internet, your machine needs to have a device called a network interface card. This network adapter has its own hardware address that's used to identify your machine. A MAC address for an Ethernet device looks something like this: `00:C4:B5:45:B2:43`. MAC addresses are given to network adapters when they are manufactured. Each manufacturer has an Organizationally Unique Identifier (OUI) to identify them as the manufacturer. This OUI is denoted by the first 3 bytes of the MAC address. For example, Dell has `00-14-22`, so a network adapter from Dell could have a MAC address like: `00-14-22-34-B2-C2`.

### IP Addresses

An IP address is used to identify a device on a network. They are hardware independent and can vary in syntax depending on if you are using IPv4 or IPv6 (more on this later). For now, we'll assume you are using IPv4, so a typical IP address would look like: `10.24.12.4`. IP addresses are used with the software side of networking. Anytime a system is connected to the Internet, it should have an IP address. They can also change if your network changes and are unique to the entire Internet (this isn't always the case once we learn about NAT).

Remember, it takes both software and hardware to move packets across networks, so we have two identifiers for each: MAC (hardware) and IP (software).

### Hostnames

One last way to identify your machines is through hostnames. Hostnames take your IP address and allow you to tie that address to a human-readable name. Instead of remembering `192.12.41.4`, you can just remember `myhost.com`.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of network identifiers like MAC addresses, IP addresses, and hostnames:

1. **[Identify MAC and IP Addresses in Linux](https://labex.io/labs/linux-identify-mac-and-ip-addresses-in-linux-592731)** - Practice using the `ip a` command to identify network addressing information, including MAC and IP addresses, on a Linux system.
2. **[Explore IP Address Types and Reachability in Linux](https://labex.io/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** - Explore different IP address types and test network reachability using `ping` and `ip a`.
3. **[Manage Local Hostname Resolution in Linux](https://labex.io/labs/linux-manage-local-hostname-resolution-in-linux-592792)** - Learn to manage local hostname resolution by editing the `/etc/hosts` file and testing your changes.

These labs will help you apply the concepts in real scenarios and build confidence with fundamental Linux networking.

## Quiz Question

How many bytes are in an IPv4 address?

## Quiz Answer

4
