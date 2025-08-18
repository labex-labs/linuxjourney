---
lang: "en"
title: "Subnetting Cheats"
meta_description: "Learn subnetting basics and binary conversion for networking. Understand IP addresses and subnet masks with this beginner-friendly guide. Start learning now!"
meta_keywords: "subnetting, binary conversion, IP address, network, Linux networking, beginner, tutorial, guide"
---

## Lesson Content

I hate to have to add this section. In the real world, you would most likely never have to do subnet math by hand. However, if you were getting interviewed on this, you'll have to know how to convert to and from binary form for subnetting. Luckily, there are some arithmetic cheats you can memorize.

First, memorize your base-2 calculations; just do it:

- 2^1 = 2
- 2^2 = 4
- 2^3 = 8
- 2^4 = 16
- 2^5 = 32
- 2^6 = 64
- 2^7 = 128
- 2^8 = 256
- 2^9 = 512
- 2^10 = 1024
- 2^11 = 2048
- 2^12 = 4096

### Decimal to Binary Chart

```plaintext
1   1  1  1  1 1 1 1
128 64 32 16 8 4 2 1
```

There are lots of reasons why the following chart looks the way it does. If you're curious how it works, there are lots of resources online.

Okay, got these memorized? Let's do a quick decimal to binary conversion:

### Convert 192.168.23.43 to Binary

Remember: 128 / 64 / 32 / 16 / 8 / 4 / 2 / 1

Let's walk through converting the first octet to binary, and you'll understand how the rest works.

1. Can you subtract 192 - 128? Yes, so the first bit is 1.
2. 192 - 128 = 64. The next number in the chart is 64. Can you subtract 64 - 64? Yes, so the second bit is 1.
3. We've run out of numbers to subtract from, so our binary form of 192 is 11000000.

### Convert Binary 11000000 to Decimal

For binary to decimal conversion, you add up the numbers that have a 1, so:

128 + 64 + 0 + 0 + 0 + 0 + 0 + 0 = 192!

## Exercise

Look at your IP address and subnet mask and see how many hosts you can have on your subnet.

## Quiz Question

What is the binary conversion of 123?

## Quiz Answer

1111011
