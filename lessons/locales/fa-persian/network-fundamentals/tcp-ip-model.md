# TCP/IP Model

## Lesson Content

The OSI model gave birth to what eventually became the TCP/IP model and this model is actually what the Internet is based off of. It is the actual implementation of networking. The TCP/IP model uses the TCP/IP protocol suite, which we just commonly refer to as TCP/IP. These protocols work together to specify how data should be gathered, addressed, transmitted and routed through a network. Using the TCP/IP model, we can see how these protocols are used to show the breakdown of how a packet travels through the network.

<b>Application Layer</b>

The top layer of the TCP/IP model. It determines how your computer's programs (such as your web browser) interface with the transport layer services to view the data that gets sent or received.

This layer uses:
<ul>
<li>HTTP (Hypertext Transfer Protocol) - used for the webpages on the Internet.</li>
<li>SMTP (Simple Mail Transfer Protocol) - electronic mail (email) transmission</li>
</ul>

<b>Transport Layer</b>

How data will be transmitted, includes checking the correct ports, the integrity of the data, and basically delivering our packets.

This layer uses:
<ul>
<li>TCP (Transmission Control Protocol) - reliable data delivery</li>
<li>UDP (User Datagram Protocol) - unreliable data delivery</li>
</ul>

<b>Network Layer</b>

This layers specifies how to move packets between hosts and across networks.

This layer uses:
<ul>
<li>IP (Internet Protocol) - Helps route packets from one machine to another.</li>
<li>ICMP (Internet Control Message Protocol) - Helps tell us what is going on, such as error messages and debugging information.</li>
</ul>

<b>Link Layer</b>

This layer specifies how to send data across a physical piece of hardware. Such as data travelling through Ethernet, fiber, etc.

The lists above of protocols each layer uses is not extensive and you'll encounter many other protocols that come into play.

In the following lessons, we will dive through each of these layers and discuss how our packet traverses through the network in the eyes of the TCP/IP model (there are many perspectives on how a packet travels across networks, we won't look at them all, but be aware that they exist).

## Exercise

No exercises for this lesson.

## Quiz Question

What is the top layer of the TCP/IP model?

## Quiz Answer

Application