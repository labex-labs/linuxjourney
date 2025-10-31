---
index: 6
lang: "en"
title: "Transport Layer"
meta_title: "Transport Layer - Network Basics"
meta_description: "Explore the Transport Layer in Linux networking. This lesson covers key protocols like TCP and UDP, the function of network ports, data segmentation, and the TCP handshake for reliable data transfer."
meta_keywords: "Linux Transport Layer, TCP, UDP, TCP handshake, network ports, data segmentation, Linux networking, network protocols, reliable data transfer"
---

## Lesson Content

The transport layer is a fundamental part of Linux networking responsible for end-to-end communication and reliable data transfer between applications on different hosts. It prepares data for transport across the network in a structured and manageable way.

### Data Segmentation

One of the primary functions of the transport layer is data segmentation. It breaks down large amounts of data into smaller, more manageable chunks called segments. This process makes data transfer more efficient and resilient. If a segment is lost or corrupted during transmission, only that small piece needs to be re-sent, not the entire data set. Once the segments arrive at their destination, the transport layer reassembles them in the correct order.

### Understanding Network Ports

While IP addresses identify the correct host on a network, they don't specify which application or service should receive the data. This is where network ports come in. Services like HTTP (web traffic) or SMTP (email) listen on specific, well-known ports. For example, HTTP typically uses port 80. The transport layer attaches source and destination port numbers to each segment, ensuring that the data is delivered to the correct process on the receiving host.

### Core Transport Protocols TCP and UDP

There are two main transport protocols used in modern networks: TCP (Transmission Control Protocol) and UDP (User Datagram Protocol). We will briefly cover UDP and then focus on TCP, as it is the most widely used for reliable communication.

### UDP (User Datagram Protocol)

UDP is a connectionless protocol that offers a fast but unreliable method of transporting data. It does not guarantee that all segments will arrive or that they will arrive in the correct order. While this may seem like a disadvantage, UDP is highly effective for applications where speed is more critical than perfect accuracy, such as live video streaming or online gaming. Losing a few frames of video is often an acceptable trade-off for a smoother, faster stream.

### TCP (Transmission Control Protocol)

TCP provides a reliable, connection-oriented stream of data. Before any data is exchanged, TCP establishes a formal connection between the two hosts to ensure both are ready to communicate.

### The TCP Handshake

To establish a connection, TCP uses a process called the three-way handshake:

1.  **SYN**: The client sends a SYN (synchronize) segment to the server to initiate a connection.
2.  **SYN-ACK**: The server responds with a SYN-ACK (synchronize-acknowledge) segment to acknowledge the client's request.
3.  **ACK**: The client sends an ACK (acknowledge) segment back to the server, confirming the connection is established.

Once the handshake is complete, data can be exchanged reliably. TCP uses sequence numbers to track each segment, allowing the receiving host to reassemble them in the correct order and request re-transmission of any missing segments. In our email example, the transport layer would attach the destination port for SMTP (port 25) and a source port from the client host to each segment.

## Exercise

While there are no specific labs for this topic, we recommend exploring the comprehensive [Linux Learning Path](https://labex.io/learn/linux) to practice related Linux skills and concepts.

## Quiz Question

What is a reliable transport protocol? (Your answer should be in English and is case-sensitive).

## Quiz Answer

TCP
