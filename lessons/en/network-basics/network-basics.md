---
lesson_id: "network-basics"
course_id: "network-basics"
lang: "en"
order_index: 1
title: "Network Basics"
description: "Learn how hosts, links, switches, routers, and packets form local and wide-area networks."
meta_title: "Network Basics - Network Basics"
meta_description: "Discover the best way to learn Linux by starting with network basics. This guide covers the basics of network components like WAN, LAN, routers, and hosts for beginners."
meta_keywords: "basics network, basics linux, best way to learn linux, basics of linux, WAN, LAN, WLAN, network tutorial, networking guide"
---

A network connects interfaces so applications on different hosts can exchange data. Understanding which device, address, and link handles each part of the path makes later Linux commands easier to interpret.

## Hosts and Interfaces

A host is an endpoint or networked system, such as a laptop, server, phone, or virtual machine. One host can have several interfaces: Ethernet, Wi-Fi, loopback, tunnels, bridges, or virtual adapters. Each interface can have link-layer and network-layer configuration appropriate to its technology.

Inspect a Linux host's interfaces and addresses with:

```bash
$ ip address show
```

An interface being present or administratively up does not prove end-to-end connectivity.

:::single-choice{#network-basics-host-interface} What is a network interface?

::option[A permanent copy of every packet on the Internet.]{#network-basics-interface-copy explanation="An interface transmits and receives traffic; it is not a global packet archive."}
::option[A host's attachment point to a network or virtual link.]{#network-basics-interface-attachment .correct explanation="A host can have multiple physical or virtual interfaces with separate configuration."}
::option[A human-readable alias for an ISP invoice.]{#network-basics-interface-invoice explanation="Billing labels are unrelated to host network attachments."}
:::

## Local Networks

A local area network, or LAN, covers a limited environment such as a home, office, or data center segment. Ethernet switches forward frames between ports on a local link. A wireless LAN, or WLAN, uses wireless link technology. Wired and wireless interfaces can still belong to the same IP subnet when a bridge or access point joins them.

:::single-choice{#network-basics-wlan-relationship} How does a WLAN relate to a LAN?

::option[A WLAN is always a separate global Internet.]{#network-basics-wlan-global explanation="It is a local network using wireless link technology."}
::option[A WLAN is a disk partition used by routers.]{#network-basics-wlan-disk explanation="The term describes networking, not storage layout."}
::option[A WLAN is a wireless form of local area network.]{#network-basics-wlan-local .correct explanation="Wireless and wired links can even be bridged into one local broadcast domain."}
:::

## Routers and Wider Networks

A router forwards network-layer packets between IP networks according to its routing table. A home device often combines routing, switching, Wi-Fi access, firewalling, NAT, and DHCP, but those remain distinct functions.

A wide area network, or WAN, spans larger geographic or administrative boundaries. An Internet service provider can connect a customer network to other networks, but “WAN” does not simply mean every device outside one house.

:::single-choice{#network-basics-router-role} What is a router's defining role?

::option[Forward packets between network-layer networks.]{#network-basics-forward-networks .correct explanation="Routing selects next hops across IP network boundaries."}
::option[Store every user's files as a mandatory backup.]{#network-basics-router-backup explanation="File retention is not the defining routing function."}
::option[Translate every hostname without consulting DNS.]{#network-basics-router-hostnames explanation="Name resolution and packet forwarding are separate functions."}
:::

## Packets, Frames, and Flows

Applications produce data that protocol layers divide and encapsulate for transmission. IP carries packets across networks; a local link carries each packet inside a technology-specific frame. Routers normally replace link-layer framing at each hop while forwarding the IP packet onward.

A conversation can involve many packets in both directions. Loss, reordering, fragmentation, retransmission, and path changes mean one captured packet rarely describes the whole application transaction.

:::single-choice{#network-basics-router-frame} What normally happens to link-layer framing at a router hop?

::option[The router removes incoming framing and creates framing for the next link.]{#network-basics-reframe .correct explanation="The forwarded IP packet is carried in a new link-layer frame appropriate to the outgoing interface."}
::option[The same Ethernet frame crosses the entire Internet unchanged.]{#network-basics-same-frame explanation="Frames are scoped to their links and are replaced at routed hops."}
::option[The application deletes the IP addresses permanently.]{#network-basics-delete-ip explanation="Routing depends on network-layer addresses."}
:::

## Summary

You can now describe the main components of a basic network path.

1. Distinguish hosts from their physical and virtual interfaces.
2. Recognize wired and wireless forms of local networks.
3. Separate routing from other functions in a combined home device.
4. Distinguish link frames from routed IP packets.
