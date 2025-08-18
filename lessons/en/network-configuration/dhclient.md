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

No exercises for this lesson.

## Quiz Question

What tries to assign IP addresses with the DHCP protocol?

## Quiz Answer

dhclient
