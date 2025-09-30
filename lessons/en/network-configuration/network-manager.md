---
index: 4
lang: "en"
title: "Network Manager"
meta_title: "Network Manager - Network Config"
meta_description: "Learn about NetworkManager in Linux, how it automates network configuration, and use nm-tool & nmcli commands. Get started with this beginner guide!"
meta_keywords: "NetworkManager, nm-tool, nmcli, Linux networking, network configuration, Linux tutorial, beginner guide"
---

## Lesson Content

Of course, if you want your system's networking up and running automatically, there is something already in place for that. Most distributions utilize the NetworkManager daemon to configure their networks automatically.

You'll notice NetworkManager in the form of an applet somewhere on your desktop taskbar if you are using a GUI. As you can see, it manages your network's hardware and connection information. For instance, on startup, NetworkManager will gather network hardware information, search for connections (wireless, wired, etc.), and then activate them.

There are also command-line tools to interact with NetworkManager:

### nm-tool

`nm-tool` reports NetworkManager's state and its devices.

```plaintext
pete@icebox:/$ nm-tool
NetworkManager Tool

State: connected (global)

- Device: eth0  [Wired connection 1] -------------------------------------------
  Type:              Wired
  Driver:            pcnet32
  State:             connected
  Default:           yes
  HW Address:        12:3D:45:56:7D:CC

  Capabilities:
    Carrier Detect:  yes

  Wired Properties
    Carrier:         on

  IPv4 Settings:
    Address:         192.168.22.1
    Prefix:          24 (255.255.255.0)
    Gateway:         192.168.22.2

    DNS:             192.168.22.2
```

### nmcli

The `nmcli` command allows you to control and modify NetworkManager. See the man page for more details.

## Exercise

Practice makes perfect! While NetworkManager automates much of the network configuration, understanding the underlying commands and concepts it manages is crucial for troubleshooting and advanced administration. Here are some hands-on labs to reinforce your understanding of network identification and management in Linux:

1. **[Identify MAC and IP Addresses in Linux](https://labex.io/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Practice using the `ip a` command to identify network addressing information, including MAC and IP addresses, on a Linux system.
2. **[Manage IP Addressing in Linux](https://labex.io/labs/comptia-manage-ip-addressing-in-linux-592736)** - Learn to configure static and dynamic IP addresses, set default gateways, and verify network configurations using the `ip` command and `dhclient`.
3. **[Explore Network Layer Interaction with ping and arp in Linux](https://labex.io/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Use `ping` and `arp` to understand how network and data link layers interact, observing ARP in action and how default gateways handle traffic.

These labs will help you apply the concepts of network identification and configuration in real scenarios and build confidence with Linux networking fundamentals.

## Quiz Question

What is the command to view NetworkManager information?

## Quiz Answer

nm-tool
