---
lesson_id: "what-is-a-router"
course_id: "routing"
lang: "en"
order_index: 1
title: "What is a router?"
description: "Learn how routers select next hops and forward IP packets between networks."
meta_title: "What is a router? - Routing"
meta_description: "A beginner's guide to understanding what a router is in networking. Learn about routing, packet switching, hops, and how routers use routing tables to forward data across networks. This network guide is essential for learning Linux networking."
meta_keywords: "router, networking, routing, hops, packet switching, Linux networking, beginner tutorial, network guide"
---

A router connects network-layer domains and forwards IP packets between them. A Linux host can act as a router when forwarding is enabled and its interfaces, routes, neighbor discovery, and filtering policy are configured appropriately.

## Routing and Forwarding

Routing builds or selects information about reachable prefixes. Forwarding applies that information to each packet: examine the destination, choose an eligible route and next hop, decrement the hop limit, and transmit through an outgoing interface.

These are separate control-plane and data-plane concerns. A route can exist while firewall policy blocks forwarding, or a forwarding interface can be up while no valid route exists.

:::single-choice{#router-forwarding-role} What does packet forwarding do?

::option[Applies routing information to send a packet toward its next hop.]{#router-apply-route .correct explanation="Forwarding is the per-packet action based on the selected route and policy."}
::option[Creates a permanent application login for every destination.]{#router-create-login explanation="Routing does not manage remote application accounts."}
::option[Copies every packet to all interfaces when no route exists.]{#router-flood-no-route explanation="Ordinary IP forwarding drops an unroutable packet rather than using Ethernet-style flooding as a fallback."}
:::

## Routing Tables and Defaults

A route associates a destination prefix with an outgoing interface, next hop, metric, source preference, or other attributes. Longest-prefix matching favors a more-specific eligible route. A default route, IPv4 `/0` or IPv6 `::/0`, is the least-specific match and is used only when no more-specific route wins.

If no eligible route exists, the router drops the packet and may generate an ICMP unreachable message. A default route is optional and need not point directly to the public Internet.

:::single-choice{#router-default-route} When is a default route selected?

::option[Before checking any destination-specific prefixes.]{#router-default-first explanation="More-specific eligible prefixes take precedence."}
::option[Only when the packet is an Ethernet broadcast.]{#router-default-broadcast explanation="IP route selection is based on network-layer destinations."}
::option[When no more-specific eligible route matches.]{#router-default-fallback .correct explanation="The zero-length prefix is the least-specific route."}
:::

## Local and Routed Traffic

Two hosts on the same on-link subnet normally exchange frames without sending the IP packet through a router. A router becomes involved when route selection chooses it as a next hop or when topology and policy deliberately force routed traversal.

A home “router” commonly combines an IP router, Ethernet switch, Wi-Fi access point, DHCP service, NAT, and firewall. Each function should be diagnosed separately.

:::single-choice{#router-same-subnet-path} Must traffic between two on-link hosts pass through their default router?

::option[Yes, because every packet must reach a WAN port.]{#router-always-wan explanation="Local on-link delivery can occur directly through the link."}
::option[Yes, unless both hosts have public addresses.]{#router-public-required explanation="Public versus private scope does not determine basic on-link forwarding."}
::option[No; the sender can address the destination directly on the local link.]{#router-direct-on-link .correct explanation="The routing table identifies the connected prefix as on-link."}
:::

## Hops and Loop Prevention

A routed hop is a network-layer forwarding step. IPv4 TTL and IPv6 Hop Limit are decremented at each router, bounding loops. Hop count is not a complete distance or quality metric: links differ in bandwidth, latency, loss, policy, and congestion.

:::single-choice{#router-hop-count-limit} What does a smaller hop count fail to guarantee?

::option[That at least one routed step exists.]{#router-hop-exists explanation="A positive hop count directly indicates routed traversal."}
::option[A faster or better application path.]{#router-hop-not-quality .correct explanation="Fewer routers can still traverse slower, congested, or policy-constrained links."}
::option[That hop-limit fields are finite.]{#router-hop-limit-finite explanation="Those fields are finite by protocol design."}
:::

## Summary

You can now separate a router's route selection from its forwarding action.

1. Define routers by forwarding between IP networks.
2. Distinguish control-plane routing from data-plane forwarding.
3. Treat the default route as the least-specific fallback.
4. Recognize that hop count alone does not measure path quality.
