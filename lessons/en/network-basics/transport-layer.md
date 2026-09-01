---
lesson_id: "transport-layer"
course_id: "network-basics"
lang: "en"
order_index: 6
title: "Transport Layer"
description: "Learn how TCP and UDP use ports and different delivery semantics between application endpoints."
meta_title: "Transport Layer - Network Basics"
meta_description: "Explore the Transport Layer in Linux networking. This lesson covers key protocols like TCP and UDP, the function of network ports, data segmentation, and the TCP handshake for reliable data transfer."
meta_keywords: "Linux Transport Layer, TCP, UDP, TCP handshake, network ports, data segmentation, Linux networking, network protocols, reliable data transfer"
---

The transport layer connects application endpoints across an IP network. TCP and UDP both use 16-bit port numbers, but they expose different communication models and guarantees to applications.

## Ports and Sockets

A destination port helps the operating system deliver traffic to a listening socket. A connection or flow is identified by more than one port: protocol, source and destination addresses, and source and destination ports all matter. The same server port can therefore support many simultaneous clients.

:::single-choice{#transport-layer-many-clients} How can one TCP server port handle several clients at once?

::option[Each connection has a distinct combination of endpoint addresses and ports.]{#transport-layer-connection-tuple .correct explanation="The complete transport tuple distinguishes concurrent connections sharing a listening port."}
::option[The server permanently renames its port after each packet.]{#transport-layer-renames-port explanation="The listening port can remain stable while accepted connections have distinct peer tuples."}
::option[IP removes all source addresses before delivery.]{#transport-layer-removes-source explanation="Source addresses are part of identifying the peer and path."}
:::

## TCP Byte Streams

TCP provides an ordered, reliable byte stream while a connection remains viable. It uses sequence numbers, acknowledgements, retransmission, flow control, and congestion control. TCP does not preserve application message boundaries: one write can arrive through several reads, or several writes can be returned by one read. Applications define their own framing.

Reliability is not absolute delivery. A connection can time out, reset, or fail, and an acknowledgement does not prove that an application durably committed the data.

:::single-choice{#transport-layer-tcp-boundaries} What happens to application message boundaries in TCP?

::option[TCP exposes an ordered byte stream without preserving write boundaries.]{#transport-layer-byte-stream .correct explanation="The application protocol must define how messages are delimited or sized."}
::option[Every write becomes exactly one IP packet and one read.]{#transport-layer-one-write-packet explanation="Segmentation, buffering, and receiving APIs do not preserve that mapping."}
::option[TCP converts each message into a DNS record.]{#transport-layer-tcp-dns explanation="DNS is a separate application protocol."}
:::

## The TCP Handshake

A normal TCP connection begins with a three-way handshake:

1. The initiator sends `SYN` with its initial sequence information.
2. The listener replies `SYN-ACK` with its own sequence information and acknowledgement.
3. The initiator returns `ACK`.

This establishes transport state in both endpoints. It does not authenticate the application server or prove that the requested application operation will succeed.

:::single-choice{#transport-layer-handshake-order} What is the normal TCP three-way handshake order?

::option[SYN, SYN-ACK, ACK.]{#transport-layer-syn-order .correct explanation="The exchange synchronizes and acknowledges initial connection state in both directions."}
::option[ACK, ACK, SYN.]{#transport-layer-ack-ack-syn explanation="The initiator first requests synchronization."}
::option[SYN, FIN, RST.]{#transport-layer-syn-fin-rst explanation="FIN and RST close or abort state rather than form a normal handshake."}
:::

## UDP Datagrams

UDP preserves datagram boundaries and provides checksum-based error detection, but it does not provide TCP-style connection state, ordering, retransmission, flow control, or congestion control. An application can add any needed reliability or congestion behavior itself. UDP is not automatically faster; performance depends on protocol design, workload, path, and implementation.

:::single-choice{#transport-layer-udp-boundaries} Which property does UDP provide to applications?

::option[An automatically retransmitted ordered byte stream.]{#transport-layer-udp-stream explanation="That describes TCP-like services, not base UDP."}
::option[Preserved boundaries between submitted datagrams.]{#transport-layer-udp-datagrams .correct explanation="A received UDP datagram corresponds to one sent datagram, unless it is lost."}
::option[Guaranteed delivery before a fixed deadline.]{#transport-layer-udp-deadline explanation="UDP provides no delivery deadline guarantee."}
:::

## Inspecting Transport Endpoints

Use `ss` to inspect listening and connected sockets without changing them:

```bash
$ ss -lntup
$ ss -tn state established
```

Process details can require privileges. A listening socket proves local readiness only at the transport boundary; firewall, routing, address family, TLS, and application health still need appropriate tests.

:::single-choice{#transport-layer-listener-proof} What does a listening TCP socket establish?

::option[Every remote firewall permits the connection.]{#transport-layer-all-firewalls explanation="Local socket state does not reveal all path policy."}
::option[The application has passed every health check.]{#transport-layer-all-health explanation="Listening is weaker evidence than a successful application transaction."}
::option[A local process is prepared to accept matching TCP connections.]{#transport-layer-local-listener .correct explanation="Remote reachability and correct application responses remain separate questions."}
:::

## Summary

You can now distinguish TCP stream behavior from UDP datagram behavior.

1. Identify a flow using protocol, addresses, and ports.
2. Treat TCP as a reliable ordered byte stream without message boundaries.
3. Recognize what the TCP handshake does and does not prove.
4. Treat UDP reliability and congestion behavior as application design choices.
5. Verify application health beyond local socket state.
