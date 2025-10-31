---
index: 4
lang: "en"
title: "netstat"
meta_title: "netstat - Troubleshooting"
meta_description: "Master the linux netstat command to analyze network connections, ports, and sockets. This guide covers common states like SYN_SENT and netstat close_wait for effective troubleshooting."
meta_keywords: "linux netstat, netstat, netstat command, syn_sent netstat, netstat close_wait, network connections, linux networking, network analysis, linux tutorial"
---

## Lesson Content

### Well-Known Ports

We've discussed how data is transmitted through ports on our machine. Let's look at some common, well-known ports. You can find a list of these ports in the **/etc/services** file:

```plaintext
ftp             21/tcp
ssh             22/tcp
smtp            25/tcp
domain          53/tcp  # DNS
http            80/tcp
https           443/tcp
..etc..
```

The first column shows the service name, followed by its assigned port number and the transport layer protocol it uses.

### Introduction to linux netstat

An extremely useful tool for gathering detailed network information is **netstat**. The `linux netstat` command displays a wide range of network-related data, including active network connections, routing tables, and interface statistics. It is often called the Swiss Army knife of networking tools.

This lesson will focus on using `netstat` to check the status of network connections. Before we dive into an example, let's clarify the difference between sockets and ports. A **port** is a numerical identifier used to direct data to a specific application. A **socket** is an endpoint for communication, allowing programs to send and receive data. The socket address is the unique combination of an IP address and a port number. Every connection between a host and a destination requires a unique socket. For example, while the HTTP service runs on port 80, multiple HTTP connections can exist simultaneously, and a unique socket is created for each one.

Let's examine the output of `netstat -at`:

```bash
pete@icebox:~$ netstat -at
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State
tcp        0      0 icebox:domain           *:*                     LISTEN
tcp        0      0 localhost:ipp           *:*                     LISTEN
tcp        0      0 icebox.lan:44468        124.28.28.50:http       TIME_WAIT
tcp        0      0 icebox.lan:34751        124.28.29.50:http       TIME_WAIT
tcp        0      0 icebox.lan:34604        economy.canonical.:http TIME_WAIT
tcp6       0      0 ip6-localhost:ipp       [::]:*                  LISTEN
tcp6       1      0 ip6-localhost:35094     ip6-localhost:ipp       CLOSE_WAIT
tcp6       0      0 ip6-localhost:ipp       ip6-localhost:35094     FIN_WAIT2
```

The `netstat -a` command displays all listening and non-listening sockets, while the `-t` flag filters the output to show only TCP connections.

The columns are as follows:

- **Proto**: The protocol used (e.g., TCP or UDP).
- **Recv-Q**: The queue of data waiting to be received.
- **Send-Q**: The queue of data waiting to be sent.
- **Local Address**: The address of the local host.
- **Foreign Address**: The address of the remote host.
- **State**: The current state of the socket.

### Understanding Connection States

The **State** column provides crucial information about the status of a connection. Here are a few common states you will encounter:

- **LISTENING**: The socket is waiting for incoming connections. For a TCP connection to be made, the destination must be listening.
- **SYN_SENT**: When using `netstat`, a `SYN_SENT` state indicates the socket is actively attempting to establish a connection.
- **ESTABLISHED**: The socket has a fully established connection.
- **CLOSE_WAIT**: The `netstat close_wait` state means the remote host has shut down, and the local system is waiting for the application to close the socket.
- **TIME_WAIT**: The socket is waiting after closing to handle any packets that might still be in the network.

You can see a full list of socket states in the `netstat` man page.

## Exercise

Practice makes perfect! Here is a hands-on lab to reinforce your understanding of network interface settings:

1. **[Examine Network Interface Settings with ethtool in Linux](https://labex.io/labs/comptia-examine-network-interface-settings-with-ethtool-in-linux-592759)** - Learn to use the `ethtool` command to examine and manage network interface settings, including viewing and setting interface speed and duplex, and analyzing link modes to troubleshoot physical layer network issues.

This lab will help you apply the concepts in real scenarios and build confidence with managing network interfaces.

## Quiz Question

What port is used for HTTPS?

## Quiz Answer

443
