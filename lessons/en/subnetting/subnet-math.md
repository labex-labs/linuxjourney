---
lesson_id: "subnet-math"
course_id: "subnetting"
lang: "en"
order_index: 3
title: "Subnet Math"
description: "Learn how to calculate IPv4 network, broadcast, range, and address counts from a prefix."
meta_title: "Subnet Math - Subnetting"
meta_description: "Master the fundamentals of subnet math. This guide explains how to perform subnet mask math to calculate the number of available hosts on your network. Learn essential IP addressing and binary concepts for Linux networking."
meta_keywords: "subnet math, subnet mask math, IP address, subnet mask, network hosts, binary, Linux networking, host calculation, beginner tutorial"
---

Subnet math applies a prefix length to the 32 bits of an IPv4 address. Binary reasoning prevents mistakes at prefix boundaries that do not align with decimal octets.

## Finding the Network Address

Use address `192.168.1.165/24`:

```text
address  11000000.10101000.00000001.10100101
mask     11111111.11111111.11111111.00000000
network  11000000.10101000.00000001.00000000
```

A bitwise AND keeps address bits where the mask is one and clears host bits. The result is `192.168.1.0/24`.

:::single-choice{#subnet-math-network-operation}
Which operation finds an IPv4 network address from an address and mask?

::option[Decimal string concatenation.]{#subnet-math-concatenation explanation="Joining printed octets does not apply prefix bits."}
::option[Transport-port subtraction.]{#subnet-math-port-subtraction explanation="Ports are unrelated to the network prefix."}
::option[Bitwise AND.]{#subnet-math-bitwise-and .correct explanation="Network bits remain while host positions masked by zeros are cleared."}
:::

## Counting Addresses

For prefix `/p`, the host portion contains `32 - p` bits. The total address count is:

```text
2^(32 - p)
```

A `/24` therefore contains `2^8 = 256` addresses. In a traditional broadcast subnet, the all-zero host value is the network address and the all-one value is the directed broadcast, leaving 254 ordinary unicast host addresses.

:::single-choice{#subnet-math-24-total}
How many total addresses are in an IPv4 `/24`?

::option[24]{#subnet-math-total-24 explanation="The prefix length counts network bits, not addresses."}
::option[256]{#subnet-math-total-256 .correct explanation="Eight host bits produce 2^8 distinct address values."}
::option[254]{#subnet-math-total-254 explanation="That is the traditional usable-host count after two special addresses, not the total."}
:::

## Finding a Block Boundary

For `/26`, the mask is `255.255.255.192`. The final-octet block size is `256 - 192 = 64`, so subnet boundaries are 0, 64, 128, and 192. Address `192.168.1.165/26` lies in:

```text
network:   192.168.1.128
broadcast: 192.168.1.191
range:     192.168.1.129 through 192.168.1.190
```

:::single-choice{#subnet-math-165-network}
What is the network address for `192.168.1.165/26`?

::option[`192.168.1.0`]{#subnet-math-network-zero explanation="That is the first `/26` block, covering 0 through 63."}
::option[`192.168.1.165`]{#subnet-math-network-self explanation="The supplied address has nonzero host bits within the `/26`."}
::option[`192.168.1.128`]{#subnet-math-network-128 .correct explanation="The value 165 falls in the 128-through-191 block."}
:::

## Accounting for Prefix Exceptions

The shortcut `2^host_bits - 2` is not universal. IPv4 `/31` prefixes are defined for point-to-point links where both addresses can be endpoints and no directed broadcast is needed. A `/32` identifies one host route or interface address. Network technology and protocol use determine which addresses are assignable.

:::single-choice{#subnet-math-31-exception}
Why should you not subtract two addresses from every IPv4 prefix?

::option[IPv4 addresses contain no host bits at any prefix.]{#subnet-math-no-host-bits explanation="Most prefixes leave one or more host bits."}
::option[`/31` point-to-point links can use both addresses as endpoints.]{#subnet-math-31-both .correct explanation="The point-to-point model does not need traditional network and directed-broadcast reservations."}
::option[All IPv4 networks use multicast instead of unicast.]{#subnet-math-all-multicast explanation="Ordinary unicast addressing remains fundamental."}
:::

## Verifying Calculations

Use an independent tool or library to check manual work, then compare with the real interface and route configuration. A mathematically valid prefix can still conflict with another subnet or violate an allocation plan.

:::single-choice{#subnet-math-valid-not-safe}
What does a correct subnet calculation fail to prove?

::option[That the address plan has no overlap or policy conflict.]{#subnet-math-no-conflict .correct explanation="Operational allocation and routing evidence are still required."}
::option[That IPv4 addresses contain 32 bits.]{#subnet-math-proves-size explanation="The calculation is based on that fixed size."}
::option[That powers of two determine block counts.]{#subnet-math-powers explanation="Binary address combinations inherently use powers of two."}
:::

## Summary

You can now calculate IPv4 subnet boundaries and recognize common exceptions.

1. Find a network address with bitwise AND.
2. Count total addresses from the number of host bits.
3. Use block sizes to locate network and broadcast boundaries.
4. Handle `/31` and `/32` according to their intended use.
5. Verify mathematical results against the actual address plan.
