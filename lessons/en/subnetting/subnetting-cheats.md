---
lesson_id: "subnetting-cheats"
course_id: "subnetting"
lang: "en"
order_index: 4
title: "Subnetting Cheats"
description: "Learn compact binary and block-size methods for checking IPv4 subnet calculations."
meta_title: "Subnetting Cheats - Subnetting"
meta_description: "Master subnetting with our guide on binary conversion cheats. Learn to use the 128+64+32+16+8+4+2+1 chart to quickly convert IP addresses from decimal to binary and back. Essential for networking interviews and certifications."
meta_keywords: "subnetting, binary conversion, IP address, network, Linux networking, 128+64+32+16+8+4+2+1, 128 64 32 16 8 4 2 1, decimal to binary, subnet math, tutorial, guide"
---

Subnet calculators are useful, but a small set of binary patterns makes their output easier to verify. These methods are checks, not substitutes for confirming the real allocation and routing policy.

## Octet Bit Values

An IPv4 octet uses these place values:

```text
bit:    1   1   1   1   1  1  1  1
value: 128  64  32  16   8  4  2  1
```

Adding all eight values produces 255. Decimal 192 is `128 + 64`, so its binary representation is `11000000`.

:::single-choice{#subnet-cheats-binary-192}
What is decimal 192 in eight-bit binary?

::option[`11000000`]{#subnet-cheats-192-correct .correct explanation="The 128 and 64 positions are set and the remaining positions are zero."}
::option[`10101000`]{#subnet-cheats-168 explanation="This pattern equals 168."}
::option[`11111111`]{#subnet-cheats-255 explanation="All eight positions set equal 255."}
:::

## Common Partial-Octet Masks

Contiguous prefix bits produce a short mask sequence:

```text
bits set: 0    1    2    3    4    5    6    7    8
decimal:  0  128  192  224  240  248  252  254  255
```

For example, `/19` contains 16 full prefix bits plus three bits in the third octet, so its mask is `255.255.224.0`.

:::single-choice{#subnet-cheats-prefix-19}
Which mask corresponds to IPv4 `/19`?

::option[`255.255.224.0`]{#subnet-cheats-mask-19 .correct explanation="Sixteen full bits plus three more yield 255, 255, and 224."}
::option[`255.255.19.0`]{#subnet-cheats-literal-19 explanation="A prefix length is a bit count, not a decimal mask octet."}
::option[`255.255.255.19`]{#subnet-cheats-tail-19 explanation="This is not a contiguous 19-bit mask."}
:::

## Block Sizes

In the first mask octet that is not 255, subtract the mask value from 256 to get the subnet increment. A `/27` mask ends in 224, giving block size `256 - 224 = 32`. Boundaries in the final octet are therefore 0, 32, 64, 96, 128, 160, 192, and 224.

Address `198.51.100.77/27` lies in the 64-through-95 block.

:::single-choice{#subnet-cheats-77-network}
What is the network address for `198.51.100.77/27`?

::option[`198.51.100.32`]{#subnet-cheats-network-32 explanation="That block covers final-octet values 32 through 63."}
::option[`198.51.100.77`]{#subnet-cheats-network-77 explanation="The address includes host bits and is not the block boundary."}
::option[`198.51.100.64`]{#subnet-cheats-network-64 .correct explanation="The `/27` block beginning at 64 covers 64 through 95."}
:::

## Converting an Arbitrary Octet

To convert decimal 123, select the largest remaining values without exceeding it:

```text
123 = 64 + 32 + 16 + 8 + 2 + 1
    = 01111011
```

Convert back by adding only the place values whose bits are one. Always keep all eight positions when working inside an IPv4 octet.

:::single-choice{#subnet-cheats-binary-123}
Which eight-bit value equals decimal 123?

::option[`1111011`]{#subnet-cheats-123-seven-bit explanation="The numeric value is similar, but the octet representation must retain eight positions."}
::option[`01111011`]{#subnet-cheats-123-correct .correct explanation="The set positions add to 64 + 32 + 16 + 8 + 2 + 1."}
::option[`01111100`]{#subnet-cheats-124 explanation="This pattern sets the 4 position instead of 2 and 1, producing 124."}
:::

## Summary

You can now check common IPv4 calculations with compact binary patterns.

1. Use the eight octet place values from 128 through 1.
2. Recall the sequence of contiguous partial-octet masks.
3. Derive block size by subtracting the partial mask from 256.
4. Keep eight bits when converting individual octets.
