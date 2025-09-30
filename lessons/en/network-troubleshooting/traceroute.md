---
index: 3
lang: "en"
title: "traceroute"
meta_title: "traceroute - Troubleshooting"
meta_description: "Learn how to use the Linux traceroute command to trace network routes and troubleshoot connectivity. Understand TTL and packet routing for beginners."
meta_keywords: "traceroute, Linux networking, network troubleshooting, TTL, Linux commands, beginner, tutorial"
---

## Lesson Content

The `traceroute` command is used to see how packets are routed. It works by sending packets with increasing TTL (Time To Live) values, starting with 1. So, the first router receives the packet and decrements the TTL value by one, thus dropping the packet. The router sends back an ICMP Time Exceeded message to us. Then, the next packet gets a TTL of 2, so it makes it past the first router, but when it gets to the second router, the TTL is 0, and it returns another ICMP Time Exceeded message. Traceroute works this way because as it sends and drops packets, it builds a list of routers that the packets traverse until it finally gets to its destination and receives an ICMP Echo Reply message.

Here's a little snippet of a traceroute:

```bash
$ traceroute google.com
traceroute to google.com (216.58.216.174), 30 hops max, 60 byte packets
 1  192.168.4.254 (192.168.4.254)  0.028 ms  0.009 ms  0.008 ms
 2  100.64.1.113 (100.64.1.113)  1.227 ms  1.226 ms 0.920 ms
 3  100.64.0.20 (100.64.0.20)  1.501 ms 1.556 ms  0.855 ms
```

Each line represents a router or machine that is between you and your target. It shows the name of the target and its IP address, and the last three columns correspond to the round-trip time of a packet to reach that router. By default, three packets are sent along the route.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of network path discovery and troubleshooting:

1. **[Manage IP Addressing in Linux](https://labex.io/labs/comptia-manage-ip-addressing-in-linux-592736)** - Practice using the `ip` command to configure network settings and verify connectivity with `traceroute`.
2. **[Explore Network Layer Interaction with ping and arp in Linux](https://labex.io/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Learn how `ping` and `arp` work to understand network layer interactions, which are foundational to how `traceroute` operates.

These labs will help you apply the concepts of network diagnostics in real scenarios and build confidence with Linux networking tools.

## Quiz Question

What gets decremented by one when making hops across the network?

## Quiz Answer

TTL
