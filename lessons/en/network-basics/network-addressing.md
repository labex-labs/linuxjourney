---
lesson_id: "network-addressing"
course_id: "network-basics"
lang: "en"
order_index: 4
title: "Network Addressing"
description: "Learn how link addresses, IP addresses, and hostnames identify different parts of network communication."
meta_title: "Network Addressing - Network Basics"
meta_description: "Discover the fundamentals of network addressing. This guide explains MAC addresses, IP addresses, and hostnames, key concepts for understanding how devices communicate in Linux networking."
meta_keywords: "network addressing, MAC address, IP address, hostname, network identifiers, Linux networking, network basics, beginner, tutorial, guide"
---

Network communication uses different identifiers at different scopes. Link-layer addresses deliver frames on a local link, IP addresses support routed delivery, and names help applications and people select services.

## Link-Layer Addresses

An Ethernet MAC address is 48 bits, commonly written as six hexadecimal octets such as `00:c4:b5:45:b2:43`. A source address identifies an interface on the current link, while a destination can be unicast, multicast, or broadcast.

MAC addresses are not guaranteed permanent or globally unique. Software can assign a locally administered address, virtual interfaces generate addresses, and Wi-Fi privacy features can randomize them. Routers normally replace Ethernet framing at each hop, so a remote server does not receive the original local Ethernet source address.

:::single-choice{#network-addressing-mac-scope}
What is the normal scope of an Ethernet MAC address in packet delivery?

::option[The current local link.]{#network-addressing-local-link .correct explanation="Routers create new link-layer framing for subsequent hops."}
::option[Every routed hop to the final Internet server.]{#network-addressing-all-hops explanation="The original frame does not cross routers unchanged."}
::option[Only the application's text encoding.]{#network-addressing-text-encoding explanation="A MAC address belongs to link-layer framing."}
:::

## IP Addresses and Prefixes

IPv4 addresses are 32 bits, or four octets, while IPv6 addresses are 128 bits. An IP address is normally assigned to an interface and interpreted with a prefix length such as `192.0.2.10/24` or `2001:db8::10/64`. The prefix identifies which leading bits describe the network.

One interface can have several IP addresses, and an address can change through DHCP, privacy addressing, failover, or administration. Private IPv4 addresses can be reused in separate networks; public routing and NAT policies determine external reachability.

:::single-choice{#network-addressing-ipv4-size}
How large is an IPv4 address?

::option[32 bits in four octets.]{#network-addressing-thirty-two .correct explanation="Each displayed decimal component represents eight bits."}
::option[4 bits in a single hexadecimal digit.]{#network-addressing-four-bits explanation="Four bits represent only one hexadecimal digit."}
::option[128 bits in sixteen octets.]{#network-addressing-128-octets explanation="IPv6 is 128 bits, not 128 octets."}
:::

## Hostnames and Name Resolution

A hostname is a name, not an address. Name resolution can consult `/etc/hosts`, DNS, multicast systems, or other sources according to the host's name-service configuration. One name can resolve to multiple addresses, and several names can refer to one service.

Use the system resolver path when testing what an application is likely to see:

```bash
$ getent ahosts example.com
```

DNS answers can change or be cached, and successful resolution does not prove that the service is reachable.

:::single-choice{#network-addressing-getent-purpose}
Why use `getent ahosts` during a name-resolution check?

::option[It permanently assigns the returned address to every interface.]{#network-addressing-getent-assign explanation="The command queries databases and does not configure interfaces."}
::option[It asks the system's configured name-service path for addresses.]{#network-addressing-system-resolver .correct explanation="This can include local files and DNS according to host policy."}
::option[It guarantees that an application is healthy on every returned host.]{#network-addressing-getent-health explanation="Name lookup and application health are separate tests."}
:::

## Inspecting a Linux Host

View link and IP configuration separately:

```bash
$ ip -brief link
$ ip -brief address
```

Then inspect routes and neighbor state when diagnosing reachability. Never infer the correct source interface or address from naming alone; route selection, policy rules, namespaces, and tunnels can change the path.

:::single-choice{#network-addressing-ip-link-versus-address}
Which command view focuses on assigned IP addresses?

::option[`ip -brief address`]{#network-addressing-address-view .correct explanation="The address object displays IPv4 and IPv6 assignments on interfaces."}
::option[`ip -brief link` only.]{#network-addressing-link-only explanation="The link view focuses on interface and link-layer state."}
::option[`pwd`]{#network-addressing-pwd explanation="Pwd prints the shell's working directory."}
:::

## Summary

You can now distinguish names and addresses by their networking scope.

1. Treat MAC addresses as local-link identifiers that may change.
2. Read IPv4 and IPv6 addresses with their prefix lengths.
3. Recognize that interfaces can hold several logical addresses.
4. Query hostnames through the configured system resolver.
