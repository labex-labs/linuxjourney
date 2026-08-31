---
lesson_id: "classless-interdomain-routing-cidr"
course_id: "subnetting"
lang: "en"
order_index: 5
title: "CIDR"
description: "Learn how CIDR prefixes represent address ranges, subnet boundaries, and aggregated routes."
meta_title: "CIDR - Subnetting"
meta_description: "A guide to CIDR notation. Learn about the CIDR format, cidr subnetting, and how to calculate hosts for your network, including on an Ubuntu server. Master IP addressing with CIDR."
meta_keywords: "CIDR, cidr subnetting, cidr format, subnet mask, IP addressing, ubuntu server subnet cidr, ubuntu subnet cidr, network prefix, Linux networking"
---

Classless Inter-Domain Routing represents an address range with a prefix length instead of relying on historical address classes. CIDR supports variable-sized allocations, subnetting, and route aggregation for IPv4 and IPv6.

## Reading Prefix Notation

In `10.42.3.17/24`, the first 24 bits are the network prefix and eight bits remain for positions within the range. The canonical network is `10.42.3.0/24`; the supplied host address can still be written with the prefix when configuring an interface.

:::single-choice{#cidr-prefix-meaning}
What does `/24` specify in an IPv4 CIDR value?

::option[Twenty-four leading network-prefix bits.]{#cidr-24-prefix-bits .correct explanation="The remaining eight of the 32 IPv4 bits vary within the prefix."}
::option[Twenty-four usable addresses in every subnet.]{#cidr-24-addresses explanation="A `/24` contains 256 total address values."}
::option[The TCP destination port for the network.]{#cidr-24-port explanation="CIDR and transport ports are independent."}
:::

## Calculating Range Size

IPv4 prefix `/23` leaves nine host bits and therefore covers `2^9 = 512` total addresses. The aligned prefix `123.12.24.0/23` spans:

```text
first: 123.12.24.0
last:  123.12.25.255
```

In traditional broadcast use, the first is the network address and the last the directed broadcast. Do not apply the “minus two” usable-host shortcut blindly to `/31` point-to-point or `/32` host routes.

:::single-choice{#cidr-23-total}
How many total IPv4 addresses does a `/23` contain?

::option[512]{#cidr-total-512 .correct explanation="Nine variable bits create 2^9 combinations."}
::option[23]{#cidr-total-23 explanation="The prefix number counts fixed bits, not addresses."}
::option[510]{#cidr-total-510 explanation="That is a traditional usable count after special endpoints, not the total range size."}
:::

## Checking Alignment

A prefix must begin on its binary boundary. A `/23` advances in blocks of two in the third octet when earlier octets are fixed, so `123.12.24.0/23` is aligned but `123.12.25.0/23` canonicalizes to the same `123.12.24.0/23` range.

:::single-choice{#cidr-canonical-25}
What is the canonical `/23` network containing `123.12.25.0`?

::option[`123.12.25.0/23` only, beginning at 25.]{#cidr-25-unaligned explanation="The final prefix bit groups third-octet values in aligned pairs."}
::option[`123.12.0.0/23`]{#cidr-third-zero explanation="This describes a different `/23` range."}
::option[`123.12.24.0/23`]{#cidr-24-canonical .correct explanation="Third-octet values 24 and 25 share the same aligned 23-bit prefix."}
:::

## Aggregating Routes

CIDR can advertise one aggregate for several contiguous, equally sized, correctly aligned prefixes. For example, `192.0.2.0/25` and `192.0.2.128/25` combine into `192.0.2.0/24`. Aggregation is safe only when the advertising router can correctly reach the complete aggregate or has policy to prevent loops and black holes.

:::single-choice{#cidr-aggregate-two-25s}
Which aggregate covers both halves of `192.0.2.0/24`?

::option[`192.0.2.0/26`]{#cidr-aggregate-26 explanation="A `/26` covers only 64 addresses, smaller than either half."}
::option[`192.0.3.0/25`]{#cidr-aggregate-other explanation="This is outside the stated address range."}
::option[`192.0.2.0/24`]{#cidr-aggregate-24 .correct explanation="The two contiguous aligned `/25` ranges differ only in the next bit and share the `/24` prefix."}
:::

## Longest-Prefix Routing

When routes overlap, forwarding normally selects the eligible route with the longest matching prefix. A `/24` route is more specific than a covering `/16`, while a default route `/0` matches only when no more-specific eligible route wins.

:::single-choice{#cidr-route-specificity}
For destination `10.42.3.8`, which eligible route is more specific?

::option[`10.42.3.0/24`]{#cidr-route-24 .correct explanation="The 24-bit match is longer and therefore more specific than `/8`."}
::option[`10.0.0.0/8`]{#cidr-route-8 explanation="This matches, but fixes fewer destination bits."}
::option[`0.0.0.0/0`]{#cidr-default explanation="The default route is the least specific possible IPv4 prefix."}
:::

## Summary

You can now use CIDR notation for both address ranges and route selection.

1. Interpret the slash value as a leading prefix-bit count.
2. Calculate total range size from remaining bits.
3. Canonicalize a prefix to its aligned network boundary.
4. Aggregate only contiguous aligned ranges with valid reachability.
5. Prefer the longest eligible prefix during route lookup.
