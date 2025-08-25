---
index: 5
lang: "en"
title: "arp"
meta_title: "arp - Network Config"
meta_description: "Learn about the Linux ARP command and how to view your ARP cache. Understand ARP's role in network communication. A beginner's guide to ARP."
meta_keywords: "Linux ARP, ARP cache, ip neighbour show, network commands, Linux networking, beginner Linux, Linux tutorial"
---

## Lesson Content

Remember when we look up a MAC address with ARP, it first checks the locally stored ARP cache on our system. You can actually view this cache:

```
pete@icebox:~$ arp
Address                  HWtype  HWaddress           Flags Mask            Iface
192.168.22.1            ether   00:12:24:fc:12:cc   C                     eth0
192.168.22.254          ether   00:12:45:f2:84:64   C                     eth0
```

The ARP cache is actually empty when a machine boots up; it gets populated as packets are being sent to other hosts. If we send a packet to a destination that isn't in the ARP cache, the following happens:

1. The source host creates the Ethernet frame with an ARP request packet.
2. The source host broadcasts this frame to the entire network.
3. If one of the hosts on the network knows the correct MAC address, it will send a reply packet and frame containing the MAC address.
4. The source host adds the IP to MAC address mapping to the ARP cache and then proceeds with sending the packet.

You can also view your ARP cache via the `ip` command:

```bash
ip neighbour show
```

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of ARP and network layer interaction:

1. **[Explore Network Layer Interaction with ping and arp in Linux](https://labex.io/labs/linux-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Use `ping` and `arp` commands to observe how IP addresses are resolved to MAC addresses and how the default gateway handles traffic.
2. **[Identify MAC and IP Addresses in Linux](https://labex.io/labs/linux-identify-mac-and-ip-addresses-in-linux-592731)** - Learn to use the `ip a` command to identify network addressing information, including MAC and IP addresses, which are fundamental to understanding ARP.
3. **[Manage IP Addressing in Linux](https://labex.io/labs/linux-manage-ip-addressing-in-linux-592736)** - Practice managing IP addressing using the `ip` command and verify network configuration with `arp` and `traceroute`.

These labs will help you apply the concepts of ARP and network addressing in real scenarios and build confidence with Linux networking.

## Quiz Question

What command can you use to view your ARP cache?

## Quiz Answer

arp
