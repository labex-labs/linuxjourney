---
lang: "en"
title: "netstat"
meta_title: "netstat - Troubleshooting"
meta_description: "Learn netstat command for Linux network analysis. Understand network connections, ports, and sockets with this beginner-friendly guide."
meta_keywords: "netstat, netstat command, Linux networking, network connections, Linux tutorial, beginner, guide"
---

## Lesson Content

### Well-Known Ports

We've discussed data transmission through ports on our machine; let's look at some well-known ports.

You can get a list of well-known ports by looking at the file **/etc/services**:

```plaintext
ftp             21/tcp
ssh             22/tcp
smtp            25/tcp
domain          53/tcp  # DNS
http            80/tcp
https           443/tcp
..etc..
```

The first column is the name of the service, then the port number, and the transport layer protocol it uses.

### netstat

An extremely useful tool to get detailed information about your network is **netstat**. Netstat displays various network-related information such as network connections, routing tables, information about network interfaces, and more; it's the Swiss Army knife of networking tools. We will focus mostly on one feature netstat has, and that's the status of network connections. Before we look at an example, let's talk about sockets and ports first. A socket is an interface that allows programs to send and receive data, while a port is used to identify which application should send or receive data. The socket address is the combination of the IP address and port. Every connection between a host and destination requires a unique socket. For example, HTTP is a service that runs on port 80; however, we can have many HTTP connections, and to maintain each connection, a socket gets created per connection.

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

The `netstat -a` command shows the listening and non-listening sockets for network connections; the `-t` flag shows only TCP connections.

The columns are as follows from left to right:

- **Proto**: Protocol used, TCP or UDP.
- **Recv-Q**: Data that is queued to be received.
- **Send-Q**: Data that is queued to be sent.
- **Local Address**: Locally connected host.
- **Foreign Address**: Remotely connected host.
- **State**: The state of the socket.

See the manpage for a list of socket states, but here are a few:

- **LISTENING**: The socket is listening for incoming connections. Remember, when we make a TCP connection, our destination has to be listening for us before we can connect.
- **SYN_SENT**: The socket is actively attempting to establish a connection.
- **ESTABLISHED**: The socket has an established connection.
- **CLOSE_WAIT**: The remote host has shut down, and we're waiting for the socket to close.
- **TIME_WAIT**: The socket is waiting after close to handle packets still in the network.

## Exercise

Look at the manpage for `netstat` and learn all the features it has to offer.

## Quiz Question

What port is used for HTTPS?

## Quiz Answer

443
