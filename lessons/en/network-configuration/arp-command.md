---
lang: "en"
title: "arp"
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

Observe what happens to your ARP cache when you reboot your machine and then do something on the network.

## Quiz Question

What command can you use to view your ARP cache?

## Quiz Answer

arp
