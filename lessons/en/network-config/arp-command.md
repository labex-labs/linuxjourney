---
lesson_id: "arp-command"
course_id: "network-config"
lang: "en"
order_index: 5
title: "arp"
description: "Learn how to inspect and interpret Linux IPv4 ARP and IPv6 neighbor-cache state."
meta_title: "arp - Network Config"
meta_description: "Learn about the Linux ARP command and how to view your ARP cache. Understand ARP's role in network communication. A beginner's guide to ARP."
meta_keywords: "Linux ARP, ARP cache, ip neighbour show, network commands, Linux networking, beginner Linux, Linux tutorial"
---

Linux stores recently resolved next-hop link addresses in the neighbor table. For IPv4 over Ethernet, entries are learned through ARP; IPv6 uses Neighbor Discovery. The legacy `arp` command shows only part of this state, while `ip neighbor` handles both families.

## Viewing Neighbor Entries

Inspect all entries or one interface:

```bash
$ ip neighbor show
$ ip neighbor show dev enp1s0
```

An entry includes an IP address, link-layer address, device, and reachability state. The table can be empty after boot and populate as traffic needs local next hops.

:::single-choice{#arp-command-modern-view}
Which command displays modern Linux neighbor-table state?

::option[`pwd neighbor`]{#arp-command-pwd explanation="Pwd reports the shell working directory."}
::option[`ip neighbor show`]{#arp-command-ip-neighbor .correct explanation="It reports both IPv4 ARP-derived and IPv6 Neighbor Discovery entries."}
::option[`route --passwords`]{#arp-command-route-passwords explanation="No such route inspection should expose credentials."}
:::

## Resolving an IPv4 Neighbor

When an on-link IPv4 mapping is absent, a host broadcasts an ARP request asking who owns the target address. The target, or a router explicitly performing proxy ARP, replies. The sender caches the mapping and transmits the waiting frame.

For a remote IP destination, the host resolves the selected gateway's address rather than the remote host's MAC.

:::single-choice{#arp-command-remote-target}
Which IPv4 neighbor does a host resolve for an off-link destination?

::option[The final remote server across all routers.]{#arp-command-final-server explanation="Its MAC address has no meaning on the source link."}
::option[Every DNS server listed in resolver configuration.]{#arp-command-all-dns explanation="Neighbor resolution follows the selected route, not the resolver list."}
::option[The selected on-link gateway.]{#arp-command-gateway .correct explanation="The local Ethernet frame is addressed to the router that forwards the IP packet."}
:::

## Interpreting States

Common states include `REACHABLE`, `STALE`, `DELAY`, `PROBE`, `INCOMPLETE`, and `FAILED`. `STALE` means recent reachability confirmation has expired; the cached address can still be used while the stack probes as needed. `FAILED` indicates resolution or reachability detection did not succeed, but causes can include link, VLAN, address, route, filtering, or the peer being down.

:::single-choice{#arp-command-stale-state}
Does `STALE` mean the neighbor is known to be unreachable?

::option[No; it lacks recent confirmation and can be probed on use.]{#arp-command-stale-probe .correct explanation="The state is not equivalent to `FAILED`."}
::option[Yes, and the entry can never be used again.]{#arp-command-stale-dead explanation="Stale entries remain candidates and can transition after reachability checks."}
::option[Yes, because its DNS record expired.]{#arp-command-stale-dns explanation="Neighbor state and DNS caching are separate."}
:::

## Changing Neighbor State Carefully

Static entries and cache flushes are state-changing and can disrupt active traffic or hide the original evidence. Capture current routes, packet counters, and neighbor state first. Prefer a targeted probe and packet capture on an authorized test network before flushing an entire interface.

ARP has no built-in authentication, so duplicate addresses or spoofed replies can poison mappings. Switch protections, segmentation, monitoring, and higher-layer authentication help reduce impact.

:::single-choice{#arp-command-flush-first}
Why avoid flushing the whole neighbor table as the first diagnostic step?

::option[Neighbor entries are stored only in DNS root servers.]{#arp-command-neighbors-dns explanation="They are maintained by the local network stack."}
::option[A flush permanently removes the interface hardware.]{#arp-command-flush-hardware explanation="It removes cache entries, not physical devices."}
::option[It changes evidence and can interrupt otherwise working next hops.]{#arp-command-flush-disrupts .correct explanation="Read-only inspection and targeted tests preserve the state needed to diagnose the cause."}
:::

## Summary

You can now inspect neighbor resolution without treating every cache state as failure.

1. Use `ip neighbor` for IPv4 and IPv6 state.
2. Resolve the destination only when it is on-link.
3. Resolve a gateway for off-link IP traffic.
4. Preserve cache evidence before targeted state changes.
