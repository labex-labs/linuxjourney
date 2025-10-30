---
index: 3
lang: "en"
title: "dhclient"
meta_title: "dhclient - Network Config"
meta_description: "Learn about dhclient, how it obtains IP addresses using DHCP, and manages network leases. Understand dhclient.conf and dhclient.leases files. Linux beginner guide."
meta_keywords: "dhclient, DHCP, Linux networking, IP address, network configuration, Linux tutorial, beginner guide"
---

## Lesson Content

We've discussed DHCP before, and most often you will never need to statically set your IP addresses, subnet masks, etc. Instead, you'll be using DHCP! The `dhclient` starts up on boot and gets a list of network interfaces from the `dhclient.conf` file. For each interface listed, it tries to configure the interface using the DHCP protocol.

In the `dhclient.leases` file, `dhclient` keeps track of a list of leases across system reboots. After reading `dhclient.conf`, the `dhclient.leases` file is read to let it know what leases it's already assigned.

### To obtain a fresh IP

```bash
sudo dhclient
```

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of dynamic IP addressing and network configuration:

1. **[Manage IP Addressing in Linux](https://labex.io/labs/comptia-manage-ip-addressing-in-linux-592736)** - Practice using `dhclient` to obtain a dynamic IP address and verify network configuration in a real Linux environment.
2. **[Identify MAC and IP Addresses in Linux](https://labex.io/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Learn to inspect network interfaces and identify MAC and IP addresses, which are fundamental to understanding how DHCP assigns addresses.
3. **[Explore IP Address Types and Reachability in Linux](https://labex.io/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Test network reachability and explore different IP address types, building on your understanding of how IP addresses function in a network.

These labs will help you apply the concepts of DHCP and IP addressing in real scenarios and build confidence with network configuration in Linux.

## Quiz Question

What tries to assign IP addresses with the DHCP protocol?

## Quiz Answer

dhclient
