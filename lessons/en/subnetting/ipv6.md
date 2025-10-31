---
index: 7
lang: "en"
title: "IPv6"
meta_title: "IPv6 - Subnetting"
meta_description: "A beginner's guide to the IPv6 protocol. Learn why IPv6 was created, how it differs from IPv4, and understand the basics of its addressing scheme for modern Linux networking."
meta_keywords: "IPv6, IPv4, IP address, Linux networking, network protocols, internet protocol, address exhaustion, beginner, tutorial, guide"
---

## Lesson Content

Every device that connects to the internet, from your server to your smartphone, requires a unique IP address to communicate. The most widely used version, IPv4, provides a finite number of addresses, a limit we are rapidly approaching in our increasingly connected world. This issue is known as IPv4 address exhaustion.

### What is IPv6?

To solve this problem, the Internet Engineering Task Force (IETF) developed a new version of the Internet Protocol: IPv6. The primary purpose of IPv6 is to dramatically expand the available pool of IP addresses, ensuring the internet can continue to grow and accommodate billions of new devices. It also includes other improvements to the network protocol.

### IPv4 vs IPv6

While IPv6 was created to address the limitations of IPv4, its adoption has been gradual. It is not intended to immediately replace IPv4. Instead, the two network protocols are designed to coexist and complement each other. Many networks today run in a "dual-stack" mode, supporting both IPv4 and IPv6 simultaneously. If you are familiar with IPv4, the core concepts of IPv6 will be easy to grasp.

### Understanding IPv6 Addresses

The most significant difference you will notice is the address format. An IPv4 address is a 32-bit number typically written as four decimal numbers separated by periods (e.g., `192.168.1.1`). In contrast, an IPv6 address is a 128-bit number written in hexadecimal and separated by colons.

Here is what a typical IPv6 address looks like:

```plaintext
2dde:1235:1256:3:200:f8ed:fe23:59cf
```

This longer format allows for a vastly larger number of unique IP addresses, securing the future of internet connectivity.

## Exercise

To master the concepts of IPv6, practice is essential. Here are some hands-on labs to reinforce your understanding of IPv6 addressing and its interaction with IPv4 in a Linux environment:

1. **[Configure and Verify IPv6 Addresses in Linux](https://labex.io/labs/comptia-configure-and-verify-ipv6-addresses-in-linux-592858)** - Practice assigning static IPv6 addresses and testing connectivity using `ip` and `ping6` commands.
2. **[Perform IPv6 DNS Lookups in Linux](https://labex.io/labs/comptia-perform-ipv6-dns-lookups-in-linux-592862)** - Learn to query for AAAA records and verify IPv6 DNS resolution using `dig`, `nslookup`, and `ping6`.
3. **[Configure an IPv4-to-IPv6 6to4 Tunnel in Linux](https://labex.io/labs/comptia-configure-an-ipv4-to-ipv6-6to4-tunnel-in-linux-592867)** - Gain hands-on experience setting up a 6to4 tunnel to enable IPv6 connectivity over an existing IPv4 network.

These labs will help you apply the concepts of IPv6 in real scenarios and build confidence with network configuration and troubleshooting.

## Quiz Question

What is the name of the IP protocol designed to increase the number of available addresses for hosts on the Internet? Please answer in English using the protocol's common name, paying attention to capitalization.

## Quiz Answer

IPv6
