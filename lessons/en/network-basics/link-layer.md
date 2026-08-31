---
lesson_id: "link-layer"
course_id: "network-basics"
lang: "en"
order_index: 8
title: "Link Layer"
description: "Learn how Ethernet frames, neighbor discovery, switches, and routers deliver packets on a local link."
meta_title: "Link Layer - Network Basics"
meta_description: "Explore the fundamentals of the TCP/IP link layer. Learn how the link layer header is constructed, how ARP resolves IP addresses to MAC addresses, and the process of packet traversal on a local network."
meta_keywords: "link layer, link layer header, ARP, TCP/IP, MAC address, network fundamentals, Linux networking, packet traversal, address resolution protocol"
---

The link layer carries network-layer packets across one local medium or virtual link. Ethernet and Wi-Fi use different framing details, but both provide local delivery beneath IP.

## Ethernet Frames

An Ethernet frame contains destination and source MAC addresses, an EtherType or length field, payload, and a frame check sequence trailer. Physical transmission also uses a preamble and start delimiter. The frame check sequence detects corruption on the link; it does not repair a damaged frame or protect it cryptographically.

:::single-choice{#link-layer-fcs-purpose}
What is the Ethernet frame check sequence used for?

::option[Detecting frame corruption on the link.]{#link-layer-detect-corruption .correct explanation="A receiver can discard a frame that fails the integrity check."}
::option[Encrypting the payload for all routed hops.]{#link-layer-fcs-encryption explanation="FCS is an error-detection code, not encryption or authentication."}
::option[Selecting an application by TCP port.]{#link-layer-fcs-port explanation="Transport ports are carried inside the IP payload."}
:::

## Switches and Local Delivery

An Ethernet switch learns which source MAC addresses appear on its ports and forwards known unicast frames toward the learned destination port. Broadcast and some unknown-destination traffic is flooded within the broadcast domain. VLANs can divide one switching system into separate logical link domains.

:::single-choice{#link-layer-switch-learning}
What information does an Ethernet switch normally learn from frames?

::option[Application passwords and HTTP cookies.]{#link-layer-switch-passwords explanation="A basic forwarding table uses link addresses, not application credentials."}
::option[Every router's complete Internet routing table.]{#link-layer-switch-routing-table explanation="Layer-2 switching and global route exchange are different functions."}
::option[Source MAC addresses associated with switch ports.]{#link-layer-switch-source .correct explanation="This learning builds the forwarding table used for later known unicast traffic."}
:::

## Resolving the Next-Hop Address

For IPv4 on Ethernet, Address Resolution Protocol maps an on-link IPv4 next-hop address to a MAC address. The host first checks its neighbor cache. If needed, it broadcasts an ARP request, and the owner or an authorized proxy replies.

For an off-link IP destination, the host resolves the default or selected gateway's MAC address—not the remote destination's MAC. IPv6 uses Neighbor Discovery over ICMPv6 rather than ARP.

:::single-choice{#link-layer-remote-destination-mac}
Which MAC address does a host use for an off-link IPv4 destination?

::option[The selected next-hop router's MAC address.]{#link-layer-gateway-mac .correct explanation="The IP packet remains addressed to the remote host while the local frame goes to the router."}
::option[The remote server's MAC address across every router.]{#link-layer-remote-mac explanation="MAC addresses are local-link identifiers and are not carried end to end."}
::option[A MAC address derived from the TCP destination port.]{#link-layer-port-mac explanation="Transport ports do not determine link addresses."}
:::

## Inspecting Neighbor State

View IPv4 ARP and IPv6 Neighbor Discovery entries with:

```bash
$ ip neighbor show
```

States such as `REACHABLE`, `STALE`, `DELAY`, `PROBE`, and `FAILED` describe the neighbor-unreachability process. `STALE` does not mean broken; it means the cached reachability confirmation is no longer recent and can be tested on use.

:::single-choice{#link-layer-stale-neighbor}
What does a `STALE` neighbor entry indicate?

::option[The neighbor is permanently blocked by the firewall.]{#link-layer-stale-blocked explanation="The state does not describe firewall policy."}
::option[The MAC address has been written to disk as a backup.]{#link-layer-stale-backup explanation="Neighbor state is operational cache information."}
::option[The cached mapping lacks recent reachability confirmation.]{#link-layer-stale-confirmation .correct explanation="The stack can still use it and perform reachability detection as needed."}
:::

## Encapsulation Across a Router

The sender places an IP packet inside a frame addressed to its next hop. The router validates and removes the incoming frame, processes the IP header, selects an outgoing route, and builds a new frame for that link. The receiver reverses encapsulation and delivers the transport payload to the appropriate socket.

:::single-choice{#link-layer-router-reframing}
What remains the same in ordinary forwarding while Ethernet framing changes at a router?

::option[The IP destination, unless a middlebox such as NAT changes it.]{#link-layer-ip-destination .correct explanation="Ordinary routers forward toward the end IP destination while replacing hop-local frames."}
::option[The incoming frame check sequence.]{#link-layer-same-fcs explanation="A new outgoing frame receives its own link integrity value."}
::option[The destination MAC address on every link.]{#link-layer-same-mac explanation="Each link uses the appropriate next-hop link address."}
:::

## Summary

You can now follow an IP packet through one local-link delivery step.

1. Identify the main Ethernet frame fields and integrity trailer.
2. Explain how a switch learns local forwarding locations.
3. Resolve an IPv4 next hop with ARP and IPv6 neighbors with NDP.
4. Interpret neighbor-cache state without overclaiming failure.
5. Recognize that routers rebuild frames for each outgoing link.
