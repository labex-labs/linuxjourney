---
lesson_id: "tcp-ip-model"
course_id: "network-basics"
lang: "en"
order_index: 3
title: "TCP/IP Model"
description: "Learn how the application, transport, Internet, and link layers cooperate in the TCP/IP model."
meta_title: "TCP/IP Model - Network Basics"
meta_description: "Explore the fundamental layers in the TCP/IP model, the cornerstone of modern networking. Learn about the Application, Transport, Network, and Link layers for effective networking with TCP/IP."
meta_keywords: "TCP/IP model, layers in the tcp ip model, networking with tcp ip, layers of tcp protocol, network layers, TCP, IP, Linux networking, real world protocol project"
---

The TCP/IP model organizes the protocols used by Internet hosts into functional layers. A common four-layer form uses Application, Transport, Internet, and Link. Some teaching models split the physical medium from the link layer and therefore show five layers.

## Application Layer

Application protocols define messages and behavior for services such as HTTP, DNS, SSH, and SMTP. This layer also includes many representation and session responsibilities that the OSI model discusses separately.

:::single-choice{#tcpip-http-layer} At which TCP/IP layer is HTTP normally classified?

::option[Internet.]{#tcpip-http-internet explanation="The Internet layer handles IP addressing and packet forwarding."}
::option[Link.]{#tcpip-http-link explanation="The link layer carries traffic on a local medium."}
::option[Application.]{#tcpip-http-application .correct explanation="HTTP defines application request and response semantics."}
:::

## Transport Layer

Transport protocols provide communication between application endpoints. TCP offers a reliable ordered byte stream with congestion and flow control. UDP provides independent datagrams without TCP's connection, ordering, or retransmission guarantees. Port numbers help identify transport endpoints, but a port number alone does not prove which application is listening.

:::single-choice{#tcpip-udp-property} Which property belongs to UDP rather than TCP?

::option[Independent datagrams without built-in retransmission guarantees.]{#tcpip-udp-datagrams .correct explanation="Applications using UDP decide whether and how to add reliability."}
::option[Guaranteed in-order delivery of one byte stream.]{#tcpip-udp-ordered explanation="That is a TCP service property, subject to connection success."}
::option[Routing packets between different IP networks.]{#tcpip-udp-routing explanation="Inter-network routing is an Internet-layer function."}
:::

## Internet Layer

Internet Protocol carries packets using source and destination IP addresses. Routers examine routing information and decrement hop limits while forwarding packets toward the destination. ICMP communicates control and error information for IP operation. Delivery remains best effort; higher layers or applications handle any required recovery.

:::single-choice{#tcpip-router-layer} Which layer supplies the IP destination used by routers?

::option[Internet.]{#tcpip-router-internet .correct explanation="The IP header contains the network-layer destination used for routed forwarding."}
::option[Application.]{#tcpip-router-application explanation="Application messages are carried inside lower-layer protocol data."}
::option[Link.]{#tcpip-router-link explanation="Link addresses select the next local-hop frame destination."}
:::

## Link Layer and Encapsulation

The link layer sends an IP packet across one local link using Ethernet, Wi-Fi, a point-to-point protocol, or another technology. As application data moves downward, each layer adds information needed for its scope. At the receiver, layers validate and remove their own encapsulation before delivering data upward.

Link headers normally change at each routed hop; transport and application conversations are end-to-end unless a middlebox terminates or transforms them.

:::single-choice{#tcpip-link-scope} What is the normal scope of a link-layer frame?

::option[One local link or hop.]{#tcpip-one-link .correct explanation="A router removes incoming framing and creates framing for the next link."}
::option[Every application session on the global Internet.]{#tcpip-global-frame explanation="Frames do not remain unchanged across routed networks."}
::option[Only the source process's memory.]{#tcpip-process-memory explanation="Frames are transmitted over a network link."}
:::

## Summary

You can now place common Internet functions in the TCP/IP model.

1. Associate service protocols with the application layer.
2. Distinguish TCP streams from UDP datagrams.
3. Place IP addressing and routing at the Internet layer.
4. Treat link framing as local-hop encapsulation.
