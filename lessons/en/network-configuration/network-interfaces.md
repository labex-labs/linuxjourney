---
index: 1
lang: "en"
title: "Network Interfaces"
meta_title: "Network Interfaces - Network Config"
meta_description: "Learn about Linux network interfaces, ifconfig, and ip commands. Understand how to configure and manage network settings. Start your Linux networking journey!"
meta_keywords: "Linux network interfaces, ifconfig, ip command, network configuration, Linux networking, beginner, tutorial, guide"
---

## Lesson Content

A network interface is how the kernel links the software side of networking to the hardware side. We've already seen an example of this:

```plaintext
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
```

### The ifconfig command

The **ifconfig** tool allows us to configure our network interfaces. If we don't have any network interfaces set up, the kernel's device drivers and the network won't know how to talk to each other. Ifconfig runs on boot-up and configures our interfaces through config files, but we can also manually modify them. The output of ifconfig shows the interface name on the left side, and the right side shows detailed information. You'll most commonly see interfaces named eth0 (first Ethernet card in the machine), wlan0 (wireless interface), and lo (loopback interface). The loopback interface is used to represent your computer; it just loops you back to yourself. This is good for debugging or connecting to servers running locally.

The status of interfaces can be up or down. As you can guess, if you wanted to "turn off" an interface, you can set it to go down. The fields you'll probably look at the most in the ifconfig output are the HWaddr (MAC address of the interface), inet address (IPv4 address), and inet6 (IPv6 address). Of course, you can see that the subnet mask and broadcast address are there as well. You can also view interface information at /etc/network/interfaces.

### To create an interface and bring it up

```bash
ifconfig eth0 192.168.2.1 netmask 255.255.255.0 up
```

This assigns an IP address and netmask to the eth0 interface and also brings it up.

### To bring up or down an interface

```bash
ifup eth0
ifdown eth0
```

### The ip command

The **ip** command also allows us to manipulate the networking stack of a system. Depending on the distribution you are using, it may be the preferred method of manipulating your network settings.

Here are some examples of its use:

### To show interface information for all interfaces

```bash
ip link show
```

### To show the statistics of an interface

```bash
ip -s link show eth0
```

### To show IP addresses allocated to interfaces

```bash
ip address show
```

### To bring interfaces up and down

```bash
ip link set eth0 up
ip link set eth0 down
```

### To add an IP address to an interface

```bash
ip address add 192.168.1.1/24 dev eth0
```

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of network interfaces and IP addressing:

1. **[Identify MAC and IP Addresses in Linux](https://labex.io/labs/linux-identify-mac-and-ip-addresses-in-linux-592731)** - Practice using the `ip a` command to identify network addressing information, including MAC, IPv4, and IPv6 addresses on a Linux system.
2. **[Manage IP Addressing in Linux](https://labex.io/labs/linux-manage-ip-addressing-in-linux-592736)** - Learn to configure static and dynamic IP addresses, set a default gateway, and verify network configurations using the `ip` command.
3. **[Explore IP Address Types and Reachability in Linux](https://labex.io/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** - Explore different IP address types (private, public, multicast) and test network reachability using `ping` and `ip a`.

These labs will help you apply the concepts of network interface identification and IP addressing in real scenarios and build confidence with Linux networking.

## Quiz Question

What is the command to configure our network interfaces?

## Quiz Answer

ifconfig
