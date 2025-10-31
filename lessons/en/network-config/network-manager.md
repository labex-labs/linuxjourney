---
index: 4
lang: "en"
title: "Network Manager"
meta_title: "Network Manager - Network Config"
meta_description: "Discover the role of the NetworkManager daemon in modern Linux network management. Learn how this tool automates network configuration and how to interact with it using nm-tool and the powerful nmcli command-line utility."
meta_keywords: "NetworkManager, nm-tool, nmcli, network manager linux, networkmanager linux, linux network manager, linux network management, network configuration, Linux networking"
---

## Lesson Content

For a system's networking to be configured automatically, a service is typically already in place. Most modern Linux distributions utilize the NetworkManager daemon for this purpose, making it a cornerstone of **linux network management**.

### What is Network Manager in Linux?

If you are using a graphical user interface (GUI), you will likely notice the **Network Manager Linux** service as an applet on your desktop's taskbar. This tool manages your network hardware and connection information. For example, upon startup, NetworkManager gathers information about network hardware, searches for available connections (such as wireless or wired networks), and then activates them to get you online.

### Command-Line Interaction

While the GUI applet is convenient, there are also powerful command-line tools to interact with the **networkmanager linux** service. These are essential for server administration and scripting.

### Using nm-tool

The `nm-tool` command reports NetworkManager's current state and a list of its managed devices. Note that `nm-tool` is considered deprecated on many modern systems in favor of `nmcli`.

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

### The Modern nmcli Tool

The `nmcli` command is the primary command-line utility for controlling and modifying the **Linux Network Manager**. It allows you to view status, manage connections, and configure network devices directly from the terminal. For a complete list of its capabilities, refer to its man page (`man nmcli`).

## Exercise

Practice makes perfect! While NetworkManager automates much of the network configuration, understanding the underlying commands and concepts it manages is crucial for troubleshooting and advanced administration. Here are some hands-on labs to reinforce your understanding of network identification and management in Linux:

1. **[Identify MAC and IP Addresses in Linux](https://labex.io/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Practice using the `ip a` command to identify network addressing information, including MAC and IP addresses, on a Linux system.
2. **[Manage IP Addressing in Linux](https://labex.io/labs/comptia-manage-ip-addressing-in-linux-592736)** - Learn to configure static and dynamic IP addresses, set default gateways, and verify network configurations using the `ip` command and `dhclient`.
3. **[Explore Network Layer Interaction with ping and arp in Linux](https://labex.io/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Use `ping` and `arp` to understand how network and data link layers interact, observing ARP in action and how default gateways handle traffic.

These labs will help you apply the concepts of network identification and configuration in real scenarios and build confidence with Linux networking fundamentals.

## Quiz Question

What is the command to view a summary of NetworkManager's state and devices as shown in the lesson? Please answer using only the English command name in lowercase.

## Quiz Answer

nm-tool
