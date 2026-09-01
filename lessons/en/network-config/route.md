---
lesson_id: "route"
course_id: "network-config"
lang: "en"
order_index: 2
title: "route"
description: "Learn how to inspect, add, replace, delete, and safely verify Linux routes with ip."
meta_title: "route - Network Config"
meta_description: "Learn to manage your Linux routing table. This guide covers adding and deleting network routes using the modern 'ip route command in linux' and the legacy 'route' command."
meta_keywords: "ip route command in linux, linux ip route command, add route, delete route, routing table, network routing, linux networking, ip route"
---

Manual routes alter how the kernel selects an outgoing interface and next hop. A mistake can disconnect the host or redirect sensitive traffic, so inspect the effective route, configuration owner, and recovery path before changing state.

## Inspecting the Current Decision

Record relevant routes and ask the kernel how it currently reaches the destination:

```bash
$ ip -4 route show
$ ip route get 192.168.2.25
```

Also inspect policy rules and alternate tables when present. The route lookup is local evidence; it does not send traffic.

:::single-choice{#route-get-before-change} Why run `ip route get DESTINATION` before a route change?

::option[It records the current local decision for comparison and rollback.]{#route-get-baseline .correct explanation="The selected interface, next hop, and source help define the intended change."}
::option[It permanently reserves the destination on every router.]{#route-get-reserves explanation="The command performs a local lookup and changes no remote state."}
::option[It disables all policy-routing rules.]{#route-get-disables-policy explanation="The lookup evaluates policy rather than removing it."}
:::

## Adding or Replacing a Route

Add a route to the canonical prefix through a reachable next hop:

```bash
$ sudo ip route add 192.168.2.0/23 via 10.11.12.3 dev enp1s0
```

The gateway must be reachable according to the relevant link or an explicit valid on-link design. `add` fails when an equivalent route already exists. `replace` creates or changes a route, which is useful for idempotent configuration but can overwrite working state; preview the exact target first.

:::single-choice{#route-add-existing} What commonly happens if `ip route add` targets a route that already exists?

::option[It silently deletes the old destination prefix.]{#route-add-deletes explanation="Add normally reports an existing-object error rather than replacing it."}
::option[It fails instead of replacing the existing route.]{#route-add-fails .correct explanation="Use a deliberate `replace` only after reviewing which entry will change."}
::option[It reboots the selected gateway.]{#route-add-reboots explanation="Local route configuration cannot request a remote reboot in this way."}
:::

## Deleting Precisely

Delete the exact route attributes when more than one candidate or table could exist:

```bash
$ sudo ip route del 192.168.2.0/23 via 10.11.12.3 dev enp1s0
```

A destination-only deletion can match more broadly than intended or be ambiguous. Capture the original command needed to restore the route before removing it.

:::single-choice{#route-delete-precision} Why include next hop and device when deleting a route?

::option[To identify the intended entry more precisely.]{#route-delete-exact .correct explanation="Explicit attributes reduce the chance of removing a different route with the same prefix."}
::option[To delete the physical network adapter as well.]{#route-delete-adapter explanation="Route deletion does not remove the kernel link object."}
::option[To erase the destination's DNS zone.]{#route-delete-dns explanation="Routing and authoritative DNS data are separate systems."}
:::

## Persistence and Remote Safety

An `ip route` command changes current kernel state only. NetworkManager, systemd-networkd, netplan, ifupdown, DHCP, routing daemons, or orchestration may later replace it. Store the route in the active owner only after testing runtime behavior.

For a remote host, preserve an independent console and use a rollback that does not depend on the route being changed. Then verify route lookup, neighbor state, both traffic directions, and the real service.

:::single-choice{#route-runtime-persistence} What can happen to a manually added route after a network-manager reload?

::option[It becomes an immutable kernel feature forever.]{#route-manual-immutable explanation="Runtime routes can be removed or replaced."}
::option[It automatically appears on every host in the subnet.]{#route-manual-all-hosts explanation="The command changes only the current network namespace."}
::option[It can disappear if it is absent from persistent policy.]{#route-manual-disappears .correct explanation="The manager reconciles kernel state from its configured profiles."}
:::

## Summary

You can now make a scoped Linux route change with a recoverable workflow.

1. Capture current routes, rules, and effective lookup.
2. Use a canonical prefix and reachable next hop.
3. Distinguish add from deliberate replacement.
4. Delete the exact route and preserve a restore command.
5. Persist through the active manager and verify both directions.
