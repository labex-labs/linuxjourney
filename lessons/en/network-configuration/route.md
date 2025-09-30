---
index: 2
lang: "en"
title: "route"
meta_title: "route - Network Config"
meta_description: "Learn how to add and delete network routes using the Linux route and ip commands. Understand routing table management for beginners and intermediate users."
meta_keywords: "route command, ip route, add route, delete route, Linux networking, routing table, Linux tutorial, beginner guide"
---

## Lesson Content

We've already discussed viewing our routing tables with the `route` command. If you want to add or remove routes, you can do so manually.

### Add a new route

```bash
sudo route add -net 192.168.2.1/23 gw 10.11.12.3
```

### Delete a route

```bash
sudo route del -net 192.168.2.1/23
```

You can also perform these changes with the **ip** command:

### To add a route

```bash
ip route add 192.168.2.1/23 via 10.11.12.3
```

### To delete a route

```bash
$ ip route delete 192.168.2.1/23 via 10.11.12.3
or
$ ip route delete 192.168.2.1/23
```

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of network routing and IP addressing:

1. **[Manage IP Addressing in Linux](https://labex.io/labs/comptia-manage-ip-addressing-in-linux-592736)** - Practice configuring a static IP, setting a default gateway, and verifying network configuration using the `ip` command.
2. **[Explore Network Layer Interaction with ping and arp in Linux](https://labex.io/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Learn how the default gateway handles remote traffic and observe network layer interactions.

These labs will help you apply the concepts of IP addressing and routing in real scenarios and build confidence with Linux networking.

## Quiz Question

What is the command flag to delete a route?

## Quiz Answer

del
