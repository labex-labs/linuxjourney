---
lesson_id: "routing-table"
course_id: "routing"
lang: "en"
order_index: 2
title: "Routing Table"
description: "Learn how to read Linux routes and inspect the route selected for a destination."
meta_title: "Routing Table - Routing"
meta_description: "A guide to understanding the Linux routing table. Learn how to interpret the output of the route command, including destination, gateway, genmask, and the eth0 interface. Master the basics of your Linux route table."
meta_keywords: "linux routing table, linux route table, genmask, eth0, route command, network routing, IP routing, destination, gateway, subnet mask, linux networking"
---

Linux routing state determines which next hop, interface, and source are eligible for an IP destination. The legacy `route -n` view is still encountered, but `ip route` exposes modern kernel routing concepts more directly.

## Reading IPv4 Routes

Example output can look like:

```text
$ ip -4 route show
default via 192.168.224.2 dev eth0 proto dhcp src 192.168.224.10 metric 100
192.168.224.0/24 dev eth0 proto kernel scope link src 192.168.224.10 metric 100
```

The connected `/24` route sends matching destinations directly through `eth0`. The default uses next-hop gateway `192.168.224.2`. `proto` describes how the route was installed, `src` is a preferred source for matching traffic, and a metric helps rank otherwise comparable routes.

:::single-choice{#routing-table-via-meaning} What does `via 192.168.224.2` indicate?

::option[The only application allowed to use the route.]{#routing-table-application explanation="Application authorization is not encoded by the `via` keyword."}
::option[The next-hop gateway for the route.]{#routing-table-next-hop .correct explanation="The packet is framed to that on-link router while retaining its IP destination."}
::option[The route's filesystem mount point.]{#routing-table-mount explanation="Routing entries concern network forwarding, not filesystems."}
:::

## Connected and Default Routes

A route with `scope link` and no `via` next hop treats the prefix as directly reachable on the interface. A default route matches every address but loses to any eligible more-specific route.

:::single-choice{#routing-table-connected-route} How is a connected `scope link` destination normally reached?

::option[Through the default gateway even when a connected route matches.]{#routing-table-connected-default explanation="The connected prefix is more specific and has no gateway operand."}
::option[By converting the destination into a DNS server.]{#routing-table-connected-dns explanation="Name service is not part of an already selected IP route."}
::option[Directly through the named interface after neighbor resolution.]{#routing-table-direct .correct explanation="The host resolves the destination's on-link address and frames traffic locally."}
:::

## Prefix Length and Metric

Route selection considers policy rules and chooses the longest eligible prefix. Metrics rank routes within appropriate comparable sets; a low-metric default does not override a matching `/24` merely because its number is lower.

:::single-choice{#routing-table-prefix-before-default} Which route normally matches `192.168.224.50` more specifically?

::option[`192.168.224.0/24 dev eth0`]{#routing-table-twenty-four .correct explanation="The 24-bit matching prefix is longest among the listed routes."}
::option[`default via 192.168.224.2`]{#routing-table-default-less-specific explanation="The default has prefix length zero."}
::option[`192.168.0.0/16 via 192.168.224.3`]{#routing-table-sixteen explanation="This covers the address but fixes fewer bits than `/24`."}
:::

## Policy Rules and Multiple Tables

Linux can consult several routing tables according to `ip rule` policy based on source, mark, interface, or other selectors. Viewing only the main table can therefore miss the actual path:

```bash
$ ip rule show
$ ip route show table all
```

Network namespaces and VRFs can hold separate state as well. Run inspection in the same context as the affected process.

:::single-choice{#routing-table-policy-limit} Why might `ip route show` alone not explain an application's path?

::option[Policy rules or another network namespace can select different routing state.]{#routing-table-policy-context .correct explanation="The effective lookup depends on packet attributes and the process's network context."}
::option[Linux routing tables contain no destination prefixes.]{#routing-table-no-prefixes explanation="Destination prefixes are fundamental route keys."}
::option[Applications never send IP packets.]{#routing-table-apps-never explanation="Application traffic is carried through network and transport protocols."}
:::

## Querying an Effective Route

Ask the kernel to evaluate a destination and optional source:

```bash
$ ip route get 203.0.113.10
$ ip route get 203.0.113.10 from 192.168.224.10
```

The result predicts the local lookup at that moment. It does not send a probe or prove neighbor, downstream, firewall, or application reachability.

:::single-choice{#routing-table-route-get-limit} What does `ip route get` not do?

::option[Display the chosen local interface and next hop.]{#routing-table-get-does-interface explanation="Those are primary fields in the lookup result."}
::option[Evaluate current local route policy for a destination.]{#routing-table-get-does-policy explanation="The command performs a kernel route lookup."}
::option[Prove successful delivery through every downstream hop.]{#routing-table-get-not-probe .correct explanation="It is a local decision query rather than an end-to-end network probe."}
:::

## Summary

You can now read Linux routing entries and query the effective local decision.

1. Distinguish connected routes from routes through a gateway.
2. Read prefix, interface, protocol, source, and metric fields.
3. Apply longest-prefix matching before comparing relevant metrics.
4. Account for policy tables, namespaces, and VRFs.
5. Treat `ip route get` as a lookup, not a reachability test.
