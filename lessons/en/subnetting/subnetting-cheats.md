---
index: 4
lang: "en"
title: "Subnetting Cheats"
meta_title: "Subnetting Cheats - Subnetting"
meta_description: "Master subnetting with our guide on binary conversion cheats. Learn to use the 128+64+32+16+8+4+2+1 chart to quickly convert IP addresses from decimal to binary and back. Essential for networking interviews and certifications."
meta_keywords: "subnetting, binary conversion, IP address, network, Linux networking, 128+64+32+16+8+4+2+1, 128 64 32 16 8 4 2 1, decimal to binary, subnet math, tutorial, guide"
---

## Lesson Content

In modern networking, you will rarely perform subnet math by hand, as tools and calculators automate the process. However, understanding the manual conversion between decimal and binary is crucial for networking interviews, certification exams, and gaining a deeper understanding of how IP addressing works. This lesson provides some simple cheats to help you master it.

First, it's highly beneficial to memorize the base-2 calculations, as they form the foundation of binary math.

- 2^1 = 2
- 2^2 = 4
- 2^3 = 8
- 2^4 = 16
- 2^5 = 32
- 2^6 = 64
- 2^7 = 128
- 2^8 = 256

### The Binary Conversion Chart

To easily convert numbers, we use a chart that represents the value of each bit in an 8-bit octet of an IP address.

```plaintext
1   1  1  1  1 1 1 1
128 64 32 16 8 4 2 1
```

This chart is your primary tool. Each number corresponds to a bit's position. The full sum, `128+64+32+16+8+4+2+1`, equals 255, which is the highest possible value in an octet.

### Decimal to Binary Conversion

Let's convert the IP address `192.168.23.43` to binary. We'll walk through the first octet, `192`, to demonstrate the process. We use the values from our chart: `128 64 32 16 8 4 2 1`.

1. Start with the number `192`. Can you subtract 128 from it? Yes (192 - 128 = 64). So, the first bit is **1**.
2. Our new number is `64`. Can you subtract the next value, 64, from it? Yes (64 - 64 = 0). The second bit is **1**.
3. Our remainder is now `0`. We cannot subtract 32, 16, 8, 4, 2, or 1. Therefore, the remaining bits are all **0**.

The binary form of 192 is `11000000`. You can apply this same subtraction method to the other octets.

### Binary to Decimal Conversion

To convert from binary back to decimal, you simply add the values from the chart where a `1` appears in the binary number. Let's convert `11000000` back to decimal.

Looking at the chart `128 64 32 16 8 4 2 1`, the first two bits are `1`. This means we add the first two values:

`128 + 64 = 192`

Since all other bits are `0`, we don't add any other values. The formula `128 + 64 + 0 + 0 + 0 + 0 + 0 + 0` gives us 192. It's that simple!

## Exercise

Practice makes perfect! While subnet math is often automated in the real world, understanding the underlying binary conversions is crucial for interviews and a deeper grasp of networking. Here's a hands-on lab to reinforce your understanding:

1. **[Perform IP Subnetting and Binary Conversion in the Linux Terminal](https://labex.io/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Master IP subnetting and binary conversion by using Python in a Linux terminal to convert IP addresses, translate CIDR masks, and calculate network details.

This lab will help you apply the concepts of binary conversion and subnetting in a practical scenario and build confidence with network addressing fundamentals.

## Quiz Question

What is the binary conversion of 123? Please provide the answer in English characters (numbers).

## Quiz Answer

01111011
