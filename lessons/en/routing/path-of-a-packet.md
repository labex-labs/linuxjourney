---
index: 3
lang: "en"
title: "Path of a Packet"
meta_title: "Path of a Packet - Routing"
meta_description: "Learn how a packet travels within and outside a network. Understand IP, MAC, ARP, and routing tables for network communication. Start your Linux networking journey!"
meta_keywords: "packet travel, network communication, ARP, IP address, MAC address, routing table, Linux networking, beginner guide"
---

## Lesson Content

### Let's look at how a packet travels within its local network

1. First, the local machine will compare the destination IP address to see if it's in the same subnet by looking at its subnet mask.
2. When packets are sent, they need to have a source MAC address, destination MAC address, source IP address, and destination IP address. At this point, we do not know the destination MAC address.
3. To get to the destination host, we use ARP to broadcast a request on the local network to find the MAC address of the destination host.
4. Now the packet can be successfully sent!

### Let's see how a packet travels outside its network

1. First, the local machine will compare the destination IP address. Since it's outside of our network, it does not see the MAC address of the destination host. And we can't use ARP because the ARP request is a broadcast to locally connected hosts.
2. So our packet now looks at the routing table. It doesn't know the address of the destination IP, so it sends it out to the default gateway (another router). So now our packet contains our source IP, destination IP, and source MAC; however, we don't have a destination MAC. Remember, MAC addresses are only reached through the same network. So what does it do? It sends an ARP request to get the MAC address of the default gateway.
3. The router looks at the packet and confirms the destination MAC address, but it's not the final destination IP address, so it keeps looking at the routing table to forward the packet to another IP address that can help the packet move along to its destination. Every time the packet moves, it strips the old source and destination MAC addresses and updates the packet with the new source and destination MAC addresses.
4. Once the packet gets forwarded to the same network, we use ARP to find the final destination MAC address.
5. During this process, our packet doesn't change the source or destination IP address.

## Exercise

No exercises for this lesson.

## Quiz Question

How do we find the MAC address of an IP address?

## Quiz Answer

ARP
