---
index: 2
lang: "en"
title: "ping"
meta_title: "ping - Troubleshooting"
meta_description: "Learn how to use the Linux ping command to test network connectivity and troubleshoot issues. Understand ICMP, TTL, and roundtrip time for effective network diagnostics."
meta_keywords: "Linux ping, network connectivity, ICMP, TTL, Linux networking, beginner Linux, Linux tutorial, ping command"
---

## Lesson Content

One of the simplest networking tools, **ping**, is used to test whether or not a packet can reach a host. It works by sending ICMP echo request (Type 8) packets to the destination host and waits for an ICMP echo reply (Type 0). Ping is successful when a host sends out the request packet and receives a response from the target. Let's look at an example:

```plaintext
pete@icebox:~$ ping -c 3 www.google.com
PING www.google.com (74.125.239.112) 56(84) bytes of data.
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=1 ttl=128 time=29.0 ms
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=2 ttl=128 time=23.7 ms
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=3 ttl=128 time=15.1 ms
```

In this example, we are using ping to check if we can get to `www.google.com`. The `-c` flag (count) is used to stop sending echo request packets after the count has been reached.

The first part says that we are sending 64-byte packets to 74.125.239.112 (google.com), and the rest show us the details of the trip. By default, it sends a packet per second.

### icmp_seq

The `icmp_seq` field is used to show the sequence number of packets sent. In this case, I sent out 3 packets, and we can see that 3 packets made it back. If you do a ping and you get some sequence numbers missing, that means some connectivity issue is happening, and not all your packets are getting through. If the sequence number is out of order, your connection is probably very slow, as your packets are exceeding the one-second default.

### ttl

The Time To Live (TTL) field is used as a hop counter. As you make hops, it decrements the counter by one, and once the hop counter reaches 0, our packet dies. This is meant to give the packet a lifespan; we don't want our packets traveling around forever.

### time

The roundtrip time it took from you sending the echo request packet to getting an echo reply.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of network connectivity and the `ping` command:

1. **[Explore Network Layer Interaction with ping and arp in Linux](https://labex.io/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Use `ping` and `arp` to explore network and data link layer interactions and observe how the default gateway handles remote traffic.
2. **[Explore IP Address Types and Reachability in Linux](https://labex.io/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Utilize `ping` and `ip a` to test the local TCP/IP stack, verify public internet connectivity, and explore network reachability.
3. **[Simulate Network Layer Connectivity in Linux](https://labex.io/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Learn to assign static IP addresses with `ip addr` and test connectivity with `ping` on the same and different subnets.

These labs will help you apply the concepts of network reachability and the `ping` command in real scenarios and build confidence with network diagnostics in Linux.

## Quiz Question

What is the roundtrip time unit of measurement?

## Quiz Answer

ms
