---
index: 2
lang: "en"
title: "Routing Table"
meta_title: "Routing Table - Routing"
meta_description: "A guide to understanding the Linux routing table. Learn how to interpret the output of the route command, including destination, gateway, genmask, and the eth0 interface. Master the basics of your Linux route table."
meta_keywords: "linux routing table, linux route table, genmask, eth0, route command, network routing, IP routing, destination, gateway, subnet mask, linux networking"
---

## Lesson Content

The **Linux routing table** holds the rules that determine where network packets are sent. Every time your system needs to send a packet to an IP address, it consults this table to find the appropriate path. To view your machine's **Linux route table**, you can use the `route` command.

```plaintext
pete@icebox:~$ sudo route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.224.2   0.0.0.0         UG    0      0        0 eth0
192.168.224.0   0.0.0.0         255.255.255.0   U     1      0        0 eth0
```

### Understanding the Columns

The output of the `route` command is organized into several columns, each providing specific information about a network route.

### Destination

The Destination column specifies a network or a host. The entry `192.168.224.0` directs all packets intended for that specific network. If a packet's destination is within this network (e.g., from 192.168.224.5 to 192.168.224.7), it is sent directly through the specified interface, such as `eth0`.

The destination `0.0.0.0` is the default route. If the routing table does not have a more specific entry for a packet's destination, it uses this route.

### Gateway

The Gateway column shows the router to which packets are sent. If a packet is not on the same local network, it is forwarded to this gateway address. For the default route, this is the IP address of the router that connects your local network to other networks, like the internet.

### Genmask

The `genmask`, or generation mask, is the subnet mask for the destination network. It is used with the destination IP to determine if a packet belongs to that network. For example, a `genmask` of `255.255.255.0` means the first three octets of the IP address must match the destination's first three octets.

### Flags

These flags provide additional information about the route:

- **U**: Indicates the route is up and active.
- **G**: Signifies that the route is to a gateway (router).
- **UG**: Means the route is active and points to a gateway.

### Iface

This column indicates the network interface, like `eth0`, that packets for this route will be sent through. `eth0` typically represents the first Ethernet adapter on your system.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of network routing and IP addressing:

1. **[Identify MAC and IP Addresses in Linux](https://labex.io/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Practice using the `ip a` command to identify network addressing information, including IP addresses and network interfaces, which are key components of a routing table.
2. **[Manage IP Addressing in Linux](https://labex.io/labs/comptia-manage-ip-addressing-in-linux-592736)** - Learn to manage IP addressing, configure static IPs, set default gateways, and verify network configurations, directly relating to the entries found in a routing table.
3. **[Explore IP Address Types and Reachability in Linux](https://labex.io/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Explore IP addressing and network reachability using `ping` and `ip a`, helping you understand how different IP types interact and how network reachability is determined, which is reflected in routing decisions.

These labs will help you apply the concepts in real scenarios and build confidence with network configuration and troubleshooting.

## Quiz Question

If a destination is not found in the routing table, where are the packets sent? Please answer with a single English word, paying attention to capitalization.

## Quiz Answer

Gateway
