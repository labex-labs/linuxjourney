---
lesson_id: "subnets"
course_id: "subnetting"
lang: "en"
order_index: 2
title: "Subnets"
description: "Learn how prefixes define IPv4 subnets and influence on-link delivery, routing, and policy."
meta_title: "Subnets - Subnetting"
meta_description: "Master the fundamentals of the Linux subnet and subnet mask. This guide explains subnetting subnets, network prefixes, and how to manage network segmentation in a subnet linux environment."
meta_keywords: "subnet linux, linux subnet, linux subnet mask, subnetting subnets, subnets, subnet mask, network prefix, Linux networking, IP address"
---

A subnet is an IP address range defined by a network prefix. Hosts in one subnet are often on the same local link, but physical proximity is not the definition: VLANs, tunnels, overlays, and routed links can change topology.

## Prefixes and Masks

IPv4 can express a 24-bit prefix as either `/24` or mask `255.255.255.0`. In binary, a valid conventional subnet mask has contiguous ones followed by zeros:

```text
11111111.11111111.11111111.00000000
```

For address `192.168.1.8/24`, the network prefix is `192.168.1.0/24`. Writing `192.168.1.0/255.255.255.0` is understood by some contexts, but CIDR prefix notation is the standard compact form.

:::single-choice{#subnets-mask-24} Which dotted-decimal mask corresponds to `/24`?

::option[`255.255.255.0`]{#subnets-mask-correct .correct explanation="Three full octets contain 24 leading one bits."}
::option[`255.255.0.255`]{#subnets-noncontiguous explanation="This has noncontiguous network bits and is not the conventional `/24` mask."}
::option[`0.0.0.24`]{#subnets-prefix-as-octet explanation="A prefix length is not placed into the last mask octet."}
:::

## Deciding Whether a Destination Is On-Link

Linux installs connected routes from interface addresses and prefixes. It compares a destination with eligible routes rather than merely comparing the first three decimal octets. For non-octet boundaries such as `/20`, the split occurs inside an octet.

Inspect connected routes and the decision for one address:

```bash
$ ip route show
$ ip route get 192.168.1.50
```

:::single-choice{#subnets-on-link-decision} How does a Linux host determine whether to send directly or through a router?

::option[It always assumes addresses ending in `.1` are local.]{#subnets-dot-one explanation="Host-number conventions do not replace configured prefixes and routes."}
::option[It consults prefixes and the routing policy.]{#subnets-route-policy .correct explanation="The selected route identifies whether the destination is on-link and which interface or next hop to use."}
::option[It asks the destination application for a subnet mask after connecting.]{#subnets-ask-application explanation="Route selection must occur before that application exchange."}
:::

## Routing Between Subnets

A router with suitable interfaces and routes can forward traffic between subnets. A default gateway is simply a next hop selected by a default route; it need not use the first usable address or end in `.1`.

Subnet separation creates a place to apply routing and filtering policy, but it is not automatically a security boundary. If forwarding is allowed without restrictive policy, hosts in different subnets can still communicate.

:::single-choice{#subnets-security-boundary} Does creating two subnets automatically block traffic between them?

::option[Yes, because routers cannot connect different prefixes.]{#subnets-never-route explanation="Connecting prefixes is the primary job of routing."}
::option[No; routing and filtering policy determine permitted traffic.]{#subnets-policy-required .correct explanation="Segmentation enables policy enforcement but does not define that policy by itself."}
::option[Yes, unless both use host address `.1`.]{#subnets-dot-one-security explanation="A host-number convention does not control forwarding."}
:::

## Reasons to Subnet

Subnetting can organize address allocation, limit link-layer broadcast scope, separate failure domains, and provide policy boundaries. It can also add routing, firewall, DHCP, monitoring, and documentation complexity. Design prefixes around actual scale, growth, redundancy, and security requirements rather than assuming smaller always means faster.

:::single-choice{#subnets-design-tradeoff} What is a real subnetting trade-off?

::option[Smaller broadcast domains require no routing or documentation.]{#subnets-no-complexity explanation="More boundaries usually require more route, policy, address, and service management."}
::option[Segmentation can improve organization while increasing policy complexity.]{#subnets-tradeoff .correct explanation="Subnet boundaries can aid control but add operational state that must be maintained."}
::option[Every subnet guarantees equal latency to the Internet.]{#subnets-equal-latency explanation="Path and workload conditions determine latency."}
:::

## Summary

You can now relate an IPv4 prefix to local delivery and routed policy.

1. Express contiguous masks with CIDR prefix lengths.
2. Calculate the network prefix from address bits and mask.
3. Use routes to determine on-link versus next-hop delivery.
4. Treat subnet isolation as a policy opportunity, not a guarantee.
