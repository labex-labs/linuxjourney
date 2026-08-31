---
lesson_id: "ipv4"
course_id: "subnetting"
lang: "en"
order_index: 1
title: "IPv4"
description: "Learn how IPv4 addresses, prefixes, scopes, and Linux interface output fit together."
meta_title: "IPv4 - Subnetting"
meta_description: "Start your journey with our complete linux tutorial on IPv4 addresses. This guide for beginner linux users is the best way to learn linux networking, covering IP structure and essential command-line tools like ip addr."
meta_keywords: "IPv4, IP address, beginner linux, best way to learn linux, complete linux tutorial, best linux course online free, free linux certification courses, linux networking, ifconfig, ip addr"
---

IPv4 provides 32-bit source and destination addresses for routed packets. An address is meaningful together with its prefix, interface, scope, route policy, and lifetime—not as a permanent identifier for an entire device.

## Dotted-Decimal Notation

IPv4 is displayed as four eight-bit octets separated by dots:

```text
192.0.2.165
```

Each octet ranges from 0 through 255, so the complete address contains four bytes. The prefix length identifies how many leading bits belong to the network prefix, as in `192.0.2.165/24`.

:::single-choice{#ipv4-address-size}
How large is an IPv4 address?

::option[32 bits in four octets.]{#ipv4-thirty-two-bits .correct explanation="Four groups of eight bits produce the dotted-decimal representation."}
::option[24 bits in every network.]{#ipv4-always-twenty-four explanation="A `/24` is one prefix length, not the size of every IPv4 address."}
::option[128 bytes separated by colons.]{#ipv4-128-bytes explanation="IPv6 is 128 bits and uses colon-separated hexadecimal notation."}
:::

## Address Scope and Purpose

Not every IPv4 address is globally routable. Examples include loopback `127.0.0.0/8`, link-local `169.254.0.0/16`, private ranges such as `10.0.0.0/8`, and documentation ranges such as `192.0.2.0/24`. Multicast and limited broadcast addresses have other semantics.

Private addresses can be reused in separate networks. NAT may translate them for external communication, but NAT is not required for communication within the private routed domain.

:::single-choice{#ipv4-private-reuse}
Why can `10.0.0.1` appear in many organizations?

::option[Every instance identifies the same physical router.]{#ipv4-same-router explanation="The address has meaning within each network and is not globally unique."}
::option[IPv4 routers ignore the first octet.]{#ipv4-ignore-octet explanation="All address bits participate in route matching."}
::option[It is in an address range intended for private-network reuse.]{#ipv4-private-range .correct explanation="Separate private networks can use the same addresses without advertising them globally."}
:::

## Inspecting Linux IPv4 Addresses

Display IPv4 assignments with:

```bash
$ ip -4 address show
```

A line such as this reports more than the address:

```text
inet 192.0.2.165/24 brd 192.0.2.255 scope global dynamic eth0
```

It shows prefix, broadcast, scope, dynamic origin marker, and interface. Additional lines can show valid and preferred lifetimes. An interface can hold several IPv4 addresses.

:::single-choice{#ipv4-ip-output-prefix}
What does `/24` mean in `192.0.2.165/24`?

::option[The address expires after 24 seconds.]{#ipv4-prefix-seconds explanation="Lifetime is reported separately."}
::option[The first 24 address bits form the network prefix.]{#ipv4-prefix-bits .correct explanation="The remaining eight bits identify positions within that prefix."}
::option[The interface is TCP port 24.]{#ipv4-prefix-port explanation="CIDR prefix notation is independent of transport ports."}
:::

## Determining the Selected Source

The presence of an address does not prove Linux will use it for a destination. Routes, policy rules, metrics, and application binding influence source selection. Query the current routing decision:

```bash
$ ip route get 198.51.100.20
```

Read the selected next hop, interface, and source, then test the real application path. Do not alter addresses on a remote host without console access and a rollback plan.

:::single-choice{#ipv4-route-get-purpose}
What can `ip route get DESTINATION` show?

::option[Every router's configuration along the complete Internet path.]{#ipv4-all-router-config explanation="A local lookup does not query downstream device configurations."}
::option[The local route decision, including interface and preferred source.]{#ipv4-route-decision .correct explanation="It evaluates current host routing policy for the supplied destination."}
::option[The destination user's password.]{#ipv4-password explanation="Routing commands do not expose application credentials."}
:::

## Summary

You can now read an IPv4 address as part of interface and routing state.

1. Recognize IPv4 as four octets totaling 32 bits.
2. Interpret an address together with its prefix.
3. Distinguish private, loopback, link-local, and other scopes.
4. Inspect assignments and the source selected for a destination.
