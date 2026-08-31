---
lesson_id: "dhcp-overview"
course_id: "network-basics"
lang: "en"
order_index: 9
title: "DHCP Overview"
description: "Learn how DHCPv4 leases addresses and network options through discovery, selection, and renewal."
meta_title: "DHCP Overview - Network Basics"
meta_description: "Learn the fundamentals of DHCP (Dynamic Host Configuration Protocol). This guide covers how DHCP assigns IP addresses, its four-step process (DORA), and its role in the network's DHCP layer. Perfect for Linux networking beginners."
meta_keywords: "DHCP, Dynamic Host Configuration Protocol, dhcp layer, IP address, Linux networking, DHCP process, DORA, network configuration"
---

Dynamic Host Configuration Protocol supplies clients with leased network configuration. In DHCPv4, this can include an IPv4 address, subnet mask, default routers, DNS servers, lease time, and other options selected by local policy.

## Clients, Servers, and Relays

A DHCP server manages scopes or address pools and lease state. The server does not need to reside on every physical segment: a DHCP relay can forward client exchanges between a subnet and a centralized server. Networks using only static configuration may not provide DHCP at all.

DHCP is an application-layer protocol carried over UDP. DHCPv4 servers normally use UDP port 67 and clients port 68.

:::single-choice{#dhcp-relay-purpose}
What does a DHCP relay enable?

::option[Every client to choose an address without any policy.]{#dhcp-client-any-address explanation="The server still applies scope and lease policy."}
::option[Clients on another subnet to reach a centralized DHCP server.]{#dhcp-central-server .correct explanation="The relay forwards DHCP exchanges across a routing boundary and identifies the client network."}
::option[Ethernet switches to replace all IP routers.]{#dhcp-switch-router explanation="Relaying DHCP does not eliminate routed network boundaries."}
:::

## Initial DHCPv4 Exchange

The common initial process is remembered as DORA:

1. `DHCPDISCOVER`: a client searches for available servers.
2. `DHCPOFFER`: a server proposes an address and options.
3. `DHCPREQUEST`: the client selects and requests an offered lease.
4. `DHCPACK`: the selected server confirms the lease and options.

Broadcast and unicast details vary with client state, relay use, and server capabilities. An offer is not yet the final usable lease; the acknowledgement completes the normal selection exchange.

:::single-choice{#dhcp-dora-order}
What is the normal initial DHCPv4 order?

::option[OFFER, DISCOVER, ACK, REQUEST.]{#dhcp-wrong-order-one explanation="A client discovers before a server offers, and it requests before acknowledgement."}
::option[DISCOVER, OFFER, REQUEST, ACK.]{#dhcp-correct-order .correct explanation="The sequence searches, proposes, selects, and confirms."}
::option[REQUEST, ACK, DISCOVER, OFFER.]{#dhcp-wrong-order-two explanation="A new client normally needs discovery and an offer before selecting a lease."}
:::

## Lease Renewal

A lease expires unless renewed. A client normally begins renewal before expiry, often first contacting the original server directly. If renewal does not succeed, it later broadens the rebinding attempt. Exact timers are supplied or derived under the protocol.

An address shown as dynamically assigned does not prove that its lease will remain forever. Record the active lease, lifetime, server, and options when troubleshooting changes.

:::single-choice{#dhcp-lease-expiration}
What happens to a DHCP address lease without successful renewal?

::option[It becomes a permanent hardware MAC address.]{#dhcp-lease-mac explanation="An IP lease does not change link-layer identity."}
::option[It eventually expires and the client must stop treating it as valid.]{#dhcp-lease-expires .correct explanation="Leasing permits addresses and options to be reclaimed or changed under server policy."}
::option[It converts the client into the authoritative DNS root.]{#dhcp-lease-dns-root explanation="DHCP leasing does not grant DNS authority."}
:::

## Inspecting the Result

After a client configures DHCP, verify all required state rather than only the address:

```bash
$ ip address show
$ ip route show
$ resolvectl status
```

The resolver command varies by system. Also inspect the active network manager's lease data and logs. Duplicate addresses can still occur through rogue servers, static assignments inside a pool, stale state, or manual configuration; DHCP reduces mistakes but cannot prevent every conflict by itself.

:::single-choice{#dhcp-result-verification}
What should be checked after a DHCP lease is accepted?

::option[Only the interface's displayed name.]{#dhcp-interface-name-only explanation="An interface name does not establish addressing, routing, or resolution."}
::option[Only whether the keyboard responds.]{#dhcp-keyboard explanation="Keyboard input is unrelated to network lease configuration."}
::option[Address, routes, DNS, and lease details.]{#dhcp-check-complete-state .correct explanation="A usable configuration depends on several options and their applied system state."}
:::

## DHCPv6 and IPv6 Configuration

IPv6 hosts can use Stateless Address Autoconfiguration, DHCPv6, static configuration, or combinations. DHCPv6 does not use the IPv4 DORA exchange, and the default-router information normally comes from IPv6 Router Advertisements rather than DHCPv6.

:::single-choice{#dhcp-ipv6-default-router}
Where does an IPv6 host normally learn its default-router information?

::option[From IPv6 Router Advertisements.]{#dhcp-router-advertisement .correct explanation="DHCPv6 can provide other configuration, but routers announce themselves through Neighbor Discovery."}
::option[From an Ethernet FCS trailer.]{#dhcp-ipv6-fcs explanation="The FCS detects link corruption and carries no router configuration."}
::option[From IPv4 DHCPACK only.]{#dhcp-ipv4-ack explanation="IPv4 DHCP messages do not configure IPv6 routing."}
:::

## Summary

You can now explain how DHCPv4 leases and renews a host's network configuration.

1. Distinguish DHCP servers from relays and client subnets.
2. Follow the DISCOVER, OFFER, REQUEST, and ACK exchange.
3. Treat addresses and options as time-limited lease state.
4. Verify address, routes, DNS, and lease metadata together.
5. Keep DHCPv4 behavior distinct from IPv6 autoconfiguration.
