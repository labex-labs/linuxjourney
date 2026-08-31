---
lesson_id: "ipv6"
course_id: "subnetting"
lang: "en"
order_index: 7
title: "IPv6"
description: "Learn how to read IPv6 addresses, prefixes, scopes, autoconfiguration, and Linux routing state."
meta_title: "IPv6 - Subnetting"
meta_description: "A beginner's guide to the IPv6 protocol. Learn why IPv6 was created, how it differs from IPv4, and understand the basics of its addressing scheme for modern Linux networking."
meta_keywords: "IPv6, IPv4, IP address, Linux networking, network protocols, internet protocol, address exhaustion, beginner, tutorial, guide"
---

IPv6 uses 128-bit addresses and was designed to support a much larger address space along with updated packet and neighbor-discovery behavior. IPv4 and IPv6 are separate protocols; dual-stack hosts can run both while networks transition.

## Reading IPv6 Notation

An IPv6 address is written as eight 16-bit hexadecimal groups:

```text
2001:0db8:0000:0000:0000:0000:0000:0025
```

Leading zeros in each group can be omitted, and one consecutive run of zero groups can be compressed with `::`:

```text
2001:db8::25
```

Only one `::` may appear because otherwise the number of omitted groups would be ambiguous. `2001:db8::/32` is reserved for documentation examples.

:::single-choice{#ipv6-double-colon-rule}
Why can `::` appear at most once in an IPv6 address?

::option[Multiple `::` markers would make expansion ambiguous.]{#ipv6-compression-ambiguity .correct explanation="One compression marker can be expanded to the exact number of groups needed to reach eight."}
::option[IPv6 addresses contain only one zero bit.]{#ipv6-one-zero explanation="An address can contain many zero bits and zero groups."}
::option[The marker selects TCP port zero.]{#ipv6-port-zero explanation="Address compression is unrelated to transport ports."}
:::

## Address Types and Scope

Important addresses and ranges include:

- `::1/128`: loopback on the local host.
- `fe80::/10`: link-local unicast; normally present on IPv6 interfaces.
- `2000::/3`: currently allocated global unicast space.
- `ff00::/8`: multicast.

IPv6 has no broadcast address; multicast and Neighbor Discovery serve use cases that IPv4 often handles with broadcast. A link-local destination can require an interface zone such as `fe80::1%eth0` because the same prefix exists on every link.

:::single-choice{#ipv6-link-local-scope}
What is the normal scope of an `fe80::/10` address?

::option[Every host on the global Internet.]{#ipv6-global-link-local explanation="Global unicast addresses serve routed global scope."}
::option[Only a DNS zone file.]{#ipv6-dns-only explanation="Link-local addresses are assigned to interfaces and used on networks."}
::option[One local link.]{#ipv6-one-link .correct explanation="Routers do not forward ordinary link-local traffic between links."}
:::

## Prefixes and Interface Addresses

IPv6 CIDR notation uses a prefix length from `/0` through `/128`. A `/64` is the standard size for most LAN subnets and supports Stateless Address Autoconfiguration. An interface can hold link-local, stable global, temporary privacy, and other addresses simultaneously, each with preferred and valid lifetimes.

:::single-choice{#ipv6-address-multiplicity}
Why might one interface show several IPv6 addresses?

::option[IPv6 requires one address for each hexadecimal digit.]{#ipv6-one-per-digit explanation="Digits are representation, not separate interface assignments."}
::option[Different scopes and privacy or lifetime roles can coexist.]{#ipv6-several-roles .correct explanation="Link-local and one or more global or temporary addresses are normal."}
::option[Every address identifies a separate physical network card.]{#ipv6-separate-card explanation="One interface can own multiple addresses."}
:::

## Neighbor and Router Discovery

IPv6 Neighbor Discovery uses ICMPv6 for address resolution, duplicate-address detection, router discovery, and reachability information. Router Advertisements can provide prefixes and default-router information. Hosts may combine SLAAC with DHCPv6 for other configuration; DHCPv6 normally does not supply the default router.

Blocking all ICMPv6 breaks essential protocol behavior. Firewall policy should permit the required message types with appropriate scope rather than treating ICMPv6 as optional.

:::single-choice{#ipv6-default-router-source}
How does an IPv6 host normally learn a default router dynamically?

::option[Through Router Advertisements.]{#ipv6-router-advertisements .correct explanation="Router Discovery is part of ICMPv6 Neighbor Discovery."}
::option[From an Ethernet broadcast address.]{#ipv6-ethernet-broadcast explanation="IPv6 does not use an IP broadcast address."}
::option[From the TCP three-way handshake.]{#ipv6-tcp-handshake explanation="TCP establishes transport state after routing is already available."}
:::

## Inspecting and Testing IPv6

Inspect addresses, routes, and neighbors independently:

```bash
$ ip -6 address show
$ ip -6 route show
$ ip -6 neighbor show
$ ping -6 -c 3 2001:db8::25
```

Use a real assigned test address rather than the documentation address shown. A dual-stack application can succeed over IPv4 while IPv6 is broken, or the reverse, so test each family and its DNS `A` or `AAAA` records explicitly.

:::single-choice{#ipv6-dual-stack-test}
Why test IPv4 and IPv6 separately on a dual-stack service?

::option[Every IPv6 packet must first become an IPv4 broadcast.]{#ipv6-becomes-ipv4 explanation="Native IPv6 and IPv4 are distinct protocol paths."}
::option[The two families can have different DNS, routes, filters, and failures.]{#ipv6-independent-paths .correct explanation="A successful fallback can hide a broken preferred address family."}
::option[IPv6 tools cannot display interface state.]{#ipv6-tools-cannot explanation="The `ip -6` commands expose address, route, and neighbor state."}
:::

## Summary

You can now read and test common IPv6 interface and routing state.

1. Expand or compress eight hexadecimal address groups correctly.
2. Distinguish loopback, link-local, global, and multicast scope.
3. Expect several IPv6 addresses and lifetimes on one interface.
4. Preserve required Neighbor Discovery and Router Advertisement traffic.
5. Test IPv4 and IPv6 paths independently on dual-stack services.
