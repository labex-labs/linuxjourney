---
index: 2
lang: "en"
title: "route"
meta_title: "route - Network Config"
meta_description: "Learn to manage your Linux routing table. This guide covers adding and deleting network routes using the modern 'ip route command in linux' and the legacy 'route' command."
meta_keywords: "ip route command in linux, linux ip route command, add route, delete route, routing table, network routing, linux networking, ip route"
---

## Lesson Content

In Linux, the routing table directs network traffic to its correct destination. While we've previously discussed viewing this table, you can also manually add or remove routes to control how data packets are forwarded. This is essential for configuring complex network setups or troubleshooting connectivity issues.

### Using the Legacy route Command

The `route` command is a traditional tool for managing the routing table. While still functional, it is considered legacy, and the `ip` command is now preferred.

To add a new network route, you specify the network address, subnet mask, and the gateway (`gw`):

```bash
sudo route add -net 192.168.2.1/23 gw 10.11.12.3
```

To delete a route, use the `del` flag with the network address:

```bash
sudo route del -net 192.168.2.1/23
```

### Modern Route Management with ip route

The `ip route` command is the modern and more powerful tool for network configuration in Linux. It offers a more consistent and extensive set of options for managing network interfaces and routes. Using the **linux ip route command** is the recommended practice for current systems.

To add a route with the **ip route command in linux**, you use the `add` action, specifying the destination network and the next hop via the gateway:

```bash
ip route add 192.168.2.1/23 via 10.11.12.3
```

To delete a route, you can use the `delete` action. You can specify the route in full or just the destination network if it's unique:

```bash
# Delete by specifying the full route
ip route delete 192.168.2.1/23 via 10.11.12.3

# Or, delete by specifying only the destination
ip route delete 192.168.2.1/23
```

Mastering the `ip route` command is a key skill for any Linux administrator responsible for network management.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of network routing and IP addressing:

1.  **[Manage IP Addressing in Linux](https://labex.io/labs/comptia-manage-ip-addressing-in-linux-592736)** - Practice configuring a static IP, setting a default gateway, and verifying network configuration using the `ip` command.
2.  **[Explore Network Layer Interaction with ping and arp in Linux](https://labex.io/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Learn how the default gateway handles remote traffic and observe network layer interactions.

These labs will help you apply the concepts of IP addressing and routing in real scenarios and build confidence with Linux networking.

## Quiz Question

When using the legacy `route` command, what is the flag used to delete a route? Please answer in English, paying attention to case.

## Quiz Answer

del
