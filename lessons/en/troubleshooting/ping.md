---
index: 2
lang: "en"
title: "ping"
meta_title: "ping - Troubleshooting"
meta_description: "Learn to use the Linux ping command to test network connectivity. This guide explains the ping output, including the meaning of icmp_seq, TTL, and roundtrip time. Understand how to interpret the ping seq to diagnose network issues."
meta_keywords: "Linux ping, network connectivity, ICMP, TTL, ping command, icmp_seq, ping seq, icmp seq, icmp_seq meaning, ping icmp_seq, Linux networking"
---

## Lesson Content

The **ping** command is one of the most fundamental networking utilities, used to test if a remote host is reachable across an IP network. It operates by sending ICMP (Internet Control Message Protocol) "echo request" packets to the target host and waiting for an ICMP "echo reply". A successful ping occurs when the request packet is sent and a response is received.

Let's examine a typical `ping` command in action:

```plaintext
pete@icebox:~$ ping -c 3 www.google.com
PING www.google.com (74.125.239.112) 56(84) bytes of data.
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=1 ttl=128 time=29.0 ms
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=2 ttl=128 time=23.7 ms
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=3 ttl=128 time=15.1 ms
```

In this example, we use `ping` to check connectivity to `www.google.com`. The `-c 3` option tells `ping` to send exactly three echo request packets and then stop. By default, `ping` sends one packet per second.

### Understanding the Ping Output

The output of the `ping icmp_seq` command provides valuable diagnostic information. Let's break down the key components.

### ICMP Sequence (icmp_seq)

The `icmp_seq` field displays the sequence number of each ICMP packet. In our example, we sent three packets, and the output shows that all three (`icmp_seq=1`, `icmp_seq=2`, `icmp_seq=3`) were successfully returned. The `ping seq` is crucial for diagnosing packet loss. If you notice missing sequence numbers, it indicates a connectivity issue where some packets are not reaching their destination or returning. If the `icmp seq` numbers appear out of order, it might suggest network congestion or latency, as packets are taking longer than the one-second default interval to complete the roundtrip. Understanding the `icmp_seq meaning` is key to troubleshooting.

### Time To Live (TTL)

The Time To Live (TTL) field acts as a hop counter for the packet. Each time the packet passes through a router (a "hop"), the TTL value is decremented by one. If the counter reaches zero before the packet arrives at its destination, the packet is discarded. This mechanism prevents packets from circulating endlessly on the network.

### Time

The `time` field measures the roundtrip time—the duration it took for the packet to travel from your machine to the target host and for the echo reply to return. This value is typically measured in milliseconds (ms) and is a primary indicator of network latency.

## Exercise

Practice is essential for mastering network diagnostics. These hands-on labs will help reinforce your understanding of the `ping` command:

1.  **[Explore Network Layer Interaction with ping and arp in Linux](https://labex.io/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Use `ping` and `arp` to explore network and data link layer interactions and observe how the default gateway handles remote traffic.
2.  **[Explore IP Address Types and Reachability in Linux](https://labex.io/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Utilize `ping` and `ip a` to test the local TCP/IP stack, verify public internet connectivity, and explore network reachability.
3.  **[Simulate Network Layer Connectivity in Linux](https://labex.io/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Learn to assign static IP addresses with `ip addr` and test connectivity with `ping` on the same and different subnets.

These labs will help you apply the concepts of network reachability and the `ping` command in real-world scenarios, building your confidence with network diagnostics in Linux.

## Quiz Question

What is the roundtrip time unit of measurement? Please answer in English, paying attention to case sensitivity.

## Quiz Answer

ms
