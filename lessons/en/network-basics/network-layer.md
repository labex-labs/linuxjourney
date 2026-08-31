---
lesson_id: "network-layer"
course_id: "network-basics"
lang: "en"
order_index: 7
title: "Network Layer"
description: "Learn how IP addressing, prefixes, routing tables, and hop limits move packets between networks."
meta_title: "Network Layer - Network Basics"
meta_description: "Explore the Network layer in Linux networking. This guide explains how IP addresses and subnets enable packet routing for data transmission across networks."
meta_keywords: "Network layer, IP addresses, subnets, Linux networking, packet routing, data transmission, OSI model, IP packet"
---

The network layer provides logical addressing and best-effort packet delivery across interconnected networks. In the Internet protocol suite, IPv4 and IPv6 carry packets while routers choose the next hop toward each destination.

## IP Packets

An IP header includes source and destination addresses plus fields needed for forwarding and protocol processing. The payload commonly contains a TCP segment, UDP datagram, or ICMP message. IP does not guarantee arrival, order, or absence of duplicates.

:::single-choice{#network-layer-ip-service}
What delivery service does IP provide by itself?

::option[Guaranteed application transaction commits.]{#network-layer-guaranteed-commit explanation="An IP delivery outcome cannot prove application persistence."}
::option[Best-effort packet delivery.]{#network-layer-best-effort .correct explanation="Higher layers or applications add any required recovery or ordering."}
::option[Permanent reservation of one physical cable.]{#network-layer-cable-reservation explanation="Packet forwarding does not reserve a dedicated physical path."}
:::

## Prefixes and Subnets

An address and prefix length define which leading bits form a network prefix. Hosts use this information and their routes to decide whether a destination is on-link or requires a next-hop router. A subnet is an address range under a prefix and policy; subnets are not automatically connected to every other subnet.

:::single-choice{#network-layer-prefix-decision}
What helps a host decide whether an IPv4 destination is on-link?

::option[The destination's application password.]{#network-layer-password explanation="Authentication data does not define network prefixes."}
::option[The color of the Ethernet cable.]{#network-layer-cable-color explanation="Cable appearance has no addressing semantics."}
::option[Its configured prefixes and routing table.]{#network-layer-prefix-routes .correct explanation="The host compares destinations against routes, including connected prefixes."}
:::

## Routing Decisions

Linux consults routing policy and tables to select an outgoing interface, next hop, and preferred source information. Among otherwise eligible routes, the most specific matching prefix is normally preferred. Inspect the actual decision for a destination with:

```bash
$ ip route get 203.0.113.10
```

This is a local route lookup, not proof that every downstream router has a working route or that the destination accepts traffic.

:::single-choice{#network-layer-longest-prefix}
Which route normally wins among eligible routes to the same destination?

::option[The route whose interface name is alphabetically first.]{#network-layer-alphabetical explanation="Interface spelling is not the selection rule."}
::option[The oldest route regardless of its prefix.]{#network-layer-oldest explanation="Age alone does not override prefix matching."}
::option[The route with the most specific matching prefix.]{#network-layer-most-specific .correct explanation="Longest-prefix matching chooses the route covering the narrowest matching address range."}
:::

## Hop Limits and Forwarding Changes

Each IPv4 packet has a TTL and each IPv6 packet a Hop Limit. A router decrements it; when it reaches zero, the router drops the packet and can send an ICMP error. This prevents forwarding loops from circulating indefinitely.

Routers normally preserve end-to-end IP addresses, but NAT, tunnels, proxies, and other middleboxes can transform or wrap packets. Link-layer headers change at each routed hop regardless.

:::single-choice{#network-layer-hop-limit}
Why is TTL or Hop Limit decremented by routers?

::option[To increase the application's file permissions.]{#network-layer-hop-permissions explanation="Hop count is unrelated to filesystem authorization."}
::option[To convert every packet from IPv4 to IPv6.]{#network-layer-hop-convert explanation="Protocol translation is not the purpose of the field."}
::option[To prevent packets from looping forever.]{#network-layer-prevent-loop .correct explanation="A finite hop count ensures a persistent routing loop eventually discards the packet."}
:::

## Summary

You can now explain how an IP host selects the next step toward a destination.

1. Treat IP delivery as best effort.
2. Use prefixes and routes to distinguish on-link and routed destinations.
3. Apply longest-prefix matching to route selection.
4. Recognize how hop limits bound forwarding loops.
