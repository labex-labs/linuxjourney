---
index: 1
lang: "en"
title: "What is a router?"
meta_title: "What is a router? - Routing"
meta_description: "A beginner's guide to understanding what a router is in networking. Learn about routing, packet switching, hops, and how routers use routing tables to forward data across networks. This network guide is essential for learning Linux networking."
meta_keywords: "router, networking, routing, hops, packet switching, Linux networking, beginner tutorial, network guide"
---

## Lesson Content

A router is a fundamental device in computer networking. You likely have one in your home connecting you to the internet. Its primary job is to enable machines on a network to communicate with each other and with other networks. This process is a core part of what makes the internet and local networks function.

### The Core Function of a Router

A typical home router has LAN (Local Area Network) ports for connecting your devices to a local network and a WAN (Wide Area Network) port that provides an internet connection. Every piece of data, or "packet," that you send or receive during any networking activity must pass through the router. The router inspects these network packets and decides where they should go. It effectively routes traffic between multiple networks, ensuring each packet travels from its source to its final destination.

### The Routing Process

Think of the routing process like mail delivery. When you send a letter, the post office determines the general destination (e.g., a state or city) and sends it there. From that point, it's sorted into smaller regions like zip codes until it finally reaches the specific street address.

In networking, a router uses a **routing table** to make these decisions. This table contains a set of rules, or routes, that tell the router how to forward packets to a particular network destination. For example, a rule might say, "To reach Network A, send packets to Router B." If there's no specific rule for a destination, the router uses a **default route**, which typically directs traffic toward the internet. This system is crucial in both simple home setups and complex **Linux networking** environments.

### Hops

As packets travel across networks, their journey is measured in **hops**. A hop represents one step of the journey where a packet passes through an intermediate device, like a router. For example, if a packet must go through two routers to get from Host A to Host B, we say the path is two hops long. Hops provide a simple metric for measuring the distance between a source and a destination in a network.

### Packet Switching, Routing, and Flooding

To understand how data moves, it's helpful to know these related terms:

- **Packet Switching** is the fundamental method of receiving, processing, and forwarding data packets to their destination. It's what routers do continuously.
- **Routing** is the intelligent process of building and maintaining the routing table. Effective routing allows for more efficient and reliable packet switching.
- **Flooding** is an older, less efficient method used when a router doesn't know where to send a packet. It sends the incoming packet out on every connection except the one it arrived on, hoping one will reach the destination. Modern networking relies on routing to avoid this kind of inefficiency.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of network connectivity and routing:

1. **[Explore IP Address Types and Reachability in Linux](https://labex.io/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Practice testing the local TCP/IP stack, identifying private and public IPs, and verifying network reachability, which are key to understanding how a router facilitates communication.
2. **[Explore Network Layer Interaction with ping and arp in Linux](https://labex.io/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Learn how `ping` and `arp` commands help you observe how the network and data link layers interact, and how the default gateway (router) handles remote traffic.
3. **[Simulate Network Layer Connectivity in Linux](https://labex.io/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Use Docker to simulate network nodes and assign IP addresses, then test connectivity to understand how IP subnets and routing govern network communication.

These labs will help you apply the concepts of network communication, IP addressing, and the role of routing in real scenarios, building confidence with network fundamentals.

## Quiz Question

How do packets measure distance? (Please answer in English. The answer is case-sensitive.)

## Quiz Answer

Hops
