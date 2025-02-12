# Application Layer

## Lesson Content

Let's say I wanted to send an email to Patty. We'll go through each of the TCP/IP layers to see this in action. 

Remember that packets are used to transmit data across networks, a packet consists of a header and payload. The header contains information about where the packet is going and where it came from. The payload is the actual data that is being transferred. As our packet traverses the network, each layer adds a bit of information to the header of the packet. Also keep in mind that different layers use a different term for our "packet". In the transport layer we essentially encapsulate our data in a segment and in the link layer we refer to this as a frame, but just know that packet can be used in regards to the same thing.

First we start off in the application layer. When we send our email through our email client, the application layer will encapsulate this data. The application layer talks to the transport layer through a specified port and through this port it sends its data. We want to send an email through the application layer protocol SMTP (simple mail transfer protocol). The data is sent through our transport protocol which opens a connection to this port (port 25 is used for SMTP), so we get this data sent through this port and that data is sent to the Transport layer to be encapsulated into segments.

## Exercise

No exercises for this lesson.

## Quiz Question

What layer is used to present the packet data in a user friendly format?

## Quiz Answer

Application
