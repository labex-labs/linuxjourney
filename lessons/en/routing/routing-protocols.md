---
index: 4
lang: "en"
title: "Routing Protocols"
meta_title: "Routing Protocols - Routing"
meta_description: "Learn about routing protocols like distance vector and link state. Understand network convergence and how routers adapt to changes. Start your Linux networking journey!"
meta_keywords: "routing protocols, network convergence, distance vector, link state, Linux networking, beginner guide, network tutorial"
---

## Lesson Content

It would be a pain to have to manually configure routes on a routing table for every device on your network. Instead, we use what are known as routing protocols. Routing protocols help our system adapt to network changes; they learn different routes, build them into the routing table, and then route our packets that way. There are two primary routing protocol types: distance vector protocols and link state protocols.

### Convergence

Before we talk about the protocols, we should go over a term used in routing known as convergence. When using routing protocols, routers communicate with other routers to collect and exchange information about the network. When they agree on how a network should look, every routing table maps out the complete topology of the network, thus "converging." When something occurs in the network topology, the convergence will temporarily break until all routers are aware of this change.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of network routing and IP addressing:

1. **[Manage IP Addressing in Linux](https://labex.io/labs/linux-manage-ip-addressing-in-linux-592736)** - Practice configuring static and dynamic IP addresses, setting a default gateway, and verifying network configurations, which are crucial for understanding how routing tables are built and utilized.
2. **[Explore Network Layer Interaction with ping and arp in Linux](https://labex.io/labs/linux-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Learn how devices interact at the network layer, observing ARP and how the default gateway handles remote traffic, providing insight into the mechanisms routing protocols manage.
3. **[Simulate Network Layer Connectivity in Linux](https://labex.io/labs/linux-simulate-network-layer-connectivity-in-linux-592752)** - Use Docker to simulate network nodes, assign IP addresses, and test connectivity across subnets, directly applying concepts related to network changes and routing decisions.

These labs will help you apply the concepts of network configuration and connectivity in real scenarios, building confidence with the foundational elements that routing protocols automate.

## Quiz Question

What is the term used when all routing tables know the network topology?

## Quiz Answer

Convergence
