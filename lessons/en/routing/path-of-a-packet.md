---
lesson_id: "path-of-a-packet"
course_id: "routing"
lang: "en"
order_index: 3
title: "Path of a Packet"
description: "Learn how routes, neighbor discovery, frames, and routers carry an IP packet across a path."
meta_title: "Path of a Packet - Routing"
meta_description: "Explore the complete packet path for data traveling within a local network and across the internet. Learn how IP addresses, MAC addresses, ARP, and routing tables work together to ensure successful network communication in Linux."
meta_keywords: "packet path, network communication, ARP, IP address, MAC address, routing table, default gateway, Linux networking, packet travel"
---

A packet path is a sequence of local decisions. The source host, each router, and the destination apply their own routing, neighbor, filtering, and protocol state; no endpoint normally knows every internal decision in advance.

## Sending to an On-Link Destination

For a destination covered by a connected route, the source selects an interface and source IP. It then resolves the destination's link address—ARP for IPv4 over Ethernet or Neighbor Discovery for IPv6—and sends a frame carrying the IP packet. A switch can forward the frame without becoming an IP hop.

:::single-choice{#packet-path-switch-hop}
Does an ordinary Ethernet switch count as an IP routing hop?

::option[No; it forwards local frames without decrementing the IP hop field.]{#packet-path-switch-not-hop .correct explanation="A routed hop occurs when a router processes and forwards the IP packet."}
::option[Yes; every switch replaces the IP destination.]{#packet-path-switch-replaces-ip explanation="Layer-2 forwarding does not normally rewrite IP destinations."}
::option[Yes; every cable connector is also an IP hop.]{#packet-path-cable-hop explanation="Physical components do not perform IP routing."}
:::

## Sending Through a Gateway

For an off-link destination, the selected route identifies a next-hop router. The IP destination remains the remote endpoint, while the local frame destination is the gateway's link address. The host resolves the gateway, not the remote server, on its local link.

:::single-choice{#packet-path-gateway-mac}
Whose MAC address is used in the first Ethernet frame to an off-link server?

::option[The remote server's address across all intervening networks.]{#packet-path-remote-mac explanation="The remote link address is not meaningful on the source LAN."}
::option[A value calculated from the server's DNS name.]{#packet-path-dns-mac explanation="DNS names do not encode the local next-hop MAC."}
::option[The selected local gateway's address.]{#packet-path-local-gateway .correct explanation="The frame is delivered to the next hop while the IP header targets the final endpoint."}
:::

## Processing at Each Router

A router removes incoming link framing, validates and processes the IP header, decrements TTL or Hop Limit, looks up the destination, applies policy, and creates new framing for the outgoing link. For IPv4, header checksum processing reflects the changed TTL. If the hop field reaches zero, the router drops the packet and can return an ICMP time-exceeded message.

:::single-choice{#packet-path-router-change}
Which IP field is changed by every normal routed hop?

::option[The application username.]{#packet-path-username explanation="Routers do not need application account data for basic forwarding."}
::option[IPv4 TTL or IPv6 Hop Limit.]{#packet-path-hop-field .correct explanation="Each router decrements the field to bound routing loops."}
::option[The transport destination port in all cases.]{#packet-path-port explanation="Ordinary routing preserves transport endpoints; NAT can be a separate transformation."}
:::

## Accounting for Middleboxes and MTU

Ordinary routing preserves source and destination IP addresses, but NAT can rewrite them and tunnels can wrap the original packet. Firewalls can drop traffic silently or reject it. Link MTUs also differ; IPv4 routers can sometimes fragment packets, while IPv6 routers do not fragment forwarded packets and rely on Path MTU Discovery.

:::single-choice{#packet-path-address-change-exception}
When might end-to-end IP addresses change along a path?

::option[Whenever an Ethernet switch learns a source MAC.]{#packet-path-switch-learning-ip explanation="Switch learning affects a link forwarding table, not IP endpoint addresses."}
::option[When a NAT policy translates packet headers.]{#packet-path-nat-change .correct explanation="Translation is a middlebox function beyond ordinary route forwarding."}
::option[Whenever a DNS cache entry expires.]{#packet-path-dns-expiry explanation="Existing packets already contain numeric addresses."}
:::

## Following the Return Path

The destination performs its own route lookup for the response. The return path can use different routers due to routing policy, load balancing, or failures. Stateful firewalls and NAT must account for the observed flow, so asymmetry can matter operationally even when IP permits it.

:::single-choice{#packet-path-return-symmetry}
Must a reply traverse the same routers in reverse order?

::option[Yes, because IP records the complete outbound route in every packet.]{#packet-path-records-route explanation="Ordinary IP packets do not carry a mandatory full reverse route."}
::option[Yes, unless the source and destination share a hostname.]{#packet-path-hostname-symmetry explanation="Names do not enforce path symmetry."}
::option[No; each direction is routed independently.]{#packet-path-independent-return .correct explanation="Policies and topology can produce an asymmetric but valid path."}
:::

## Summary

You can now trace the changing link state around a routed IP packet.

1. Resolve the final host only when it is on-link.
2. Frame off-link traffic to the selected local gateway.
3. Follow route lookup and hop-limit processing at each router.
4. Account for NAT, filtering, tunnels, and MTU constraints.
5. Treat the return direction as an independent route.
