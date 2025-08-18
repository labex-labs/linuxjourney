---
lang: "en"
title: "TCP/IP Model"
meta_description: "Learn about the TCP/IP model layers: Application, Transport, Network, and Link. Understand how data travels across networks. Start your Linux networking journey!"
meta_keywords: "TCP/IP model, networking basics, Linux networking, TCP, IP, beginner tutorial, network layers, guide"
---

## Lesson Content

The OSI model gave birth to what eventually became the TCP/IP model, and this model is actually what the Internet is based on. It is the actual implementation of networking. The TCP/IP model uses the TCP/IP protocol suite, which we commonly refer to as TCP/IP. These protocols work together to specify how data should be gathered, addressed, transmitted, and routed through a network. Using the TCP/IP model, we can see how these protocols are used to show the breakdown of how a packet travels through the network.

### Application Layer

The top layer of the TCP/IP model. It determines how your computer's programs (such as your web browser) interface with the transport layer services to view the data that gets sent or received.

This layer uses:

- HTTP (Hypertext Transfer Protocol) - used for webpages on the Internet.
- SMTP (Simple Mail Transfer Protocol) - electronic mail (email) transmission

### Transport Layer

How data will be transmitted, includes checking the correct ports, the integrity of the data, and basically delivering our packets.

This layer uses:

- TCP (Transmission Control Protocol) - reliable data delivery
- UDP (User Datagram Protocol) - unreliable data delivery

### Network Layer

This layer specifies how to move packets between hosts and across networks.

This layer uses:

- IP (Internet Protocol) - Helps route packets from one machine to another.
- ICMP (Internet Control Message Protocol) - Helps tell us what is going on, such as error messages and debugging information.

### Link Layer

This layer specifies how to send data across a physical piece of hardware, such as data traveling through Ethernet, fiber, etc.

The lists above of protocols each layer uses are not extensive, and you'll encounter many other protocols that come into play.

In the following lessons, we will dive through each of these layers and discuss how our packet traverses through the network in the eyes of the TCP/IP model (there are many perspectives on how a packet travels across networks; we won't look at them all, but be aware that they exist).

## Exercise

No exercises for this lesson.

## Quiz Question

What is the top layer of the TCP/IP model?

## Quiz Answer

Application
