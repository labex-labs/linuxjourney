# Link Layer

## Lesson Content

At the bottom of the TCP/IP model sits the Link Layer. This layer is the hardware specific layer.

In the link layer, our packet is encapsulated once more into something called a frame. The frame header attaches the source and destination MAC addresses of our hosts, checksums and packet separators so that the receiver can tell when a packet ends. 

Fortunately we are on the same network, so our packet won't have to travel too far. First, the link layer attaches my source MAC address to the frame header, but it needs to know Patty's MAC address as well. How does it know that and how do I find it since it's not on the Internet? We use ARP!

<b>ARP (Address Resolution Protocol)</b>

ARP finds the MAC address associated with an IP address. ARP is used within the same network. If Patty was not on the same network, we would use a routing system to determine the next router that would receive the packet and once we were on the same network, we could use ARP. 

Once we are on the same network, systems first use the ARP look-up table that stores information about what IP addresses are associated with what MAC address. If the value is not there, then ARP is used. Then the system will send a broadcast message to the network using the ARP protocol to find out which host has IP 10.10.1.4. A broadcast message is a special message that is sent to all hosts on a network (aptly named for sending a broadcast). Any machine with the requested IP address will reply with an ARP packet containing the IP address and the MAC address.

Now that we have all the necessary data we need, IP address and MAC addresses, our link layer forwards this frame through our network interface card, out to the next device and finds Patty's network. This step is a little more complex than how I just explained it, but we will discuss more details in the Routing course.

And there it is a simple (or not so simple) packet traversal down the TCP/IP layer. Keep in mind that packets don't travel in a one way fashion like this. We haven't even gotten to Patty's network yet! When travelling through networks, it requires going through the TCP/IP model at least twice before any data is sent or received. In reality, the way this packet looks would be something like this: 

<b>Packet Traversal</b>

<ol>
<li>Pete sends Patty an email: this data gets sent to the transport layer.</li>
<li>The transport layer encapsulates the data into a TCP or UDP header to form a segment, the segment attaches the destination and source TCP or UDP port, then the segment is sent to the network layer.</li>
<li>The network layer encapsulates the TCP segment inside an IP packet, it attaches the source and destination IP address. Then routes the packet to the link layer.</li>
<li>The packet then reaches Pete's physical hardware and gets encapsulated in a frame. The source and destination MAC address get added to the frame.</li>
<li>Patty's receives this data frame through her physical layer and checks each frame for data integrity, then de-encapsulates the frame contents and sends the IP packet to the network layer.</li>
<li>The network layer reads the packet to find the source and destination IP that was previously attached. It checks if its IP is the same as the destination IP, which it is! It de-encapsulates the packet and sends the segment to the transport layer.</li>
<li>The transport layer de-encapsulates the segments, checks the TCP or UDP port numbers and makes a connection to the application layer based on those port numbers.</li>
<li>The application layer receives the data from the transport layer on the port that was specified and presents it to Patty in the form of the final email message</li>
</ol>

## Exercise

No exercises for this lesson.

## Quiz Question

What is used to find the MAC address on the same network?

## Quiz Answer

ARP
