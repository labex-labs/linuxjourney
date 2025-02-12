# Transport Layer

## Lesson Content

The transports layer helps us transfer our data in a way networks can read it. It breaks our data into chunks that will be transported and put back together in the correct order. These chunks are known as segments. Segments make it easier to transport data across networks. 

<b>Ports</b>

Even though we know where we are sending our data via IP addresses, they aren't specific enough to send our data to a certain processes or services. Services such as HTTP use a communication channel via ports. If we want to send webpage data, we need to send it over the HTTP port (port 80). In addition to forming segments, the transport layer will also attach the source and destination ports to the segment, so when the receiver gets the final packet it will know what port to use. 

<b>UDP</b>

There are two popular transport protocols UDP and TCP. We'll briefly discuss UDP and spend most of our time on TCP, since it's the most commonly used.

UDP is not a reliable method of transporting data, in fact it doesn't really care if you get all of your original data. This may sound terrible, but it does have its uses, such as for media streaming, it's ok if you lose some frames in return you get your data a little faster. 

<b>TCP</b>

TCP provides a reliable connection-oriented stream of data. TCP uses ports to send data to and from hosts. An application opens up a connection from one port on its host to another port on a remote host. In order to establish the connection, we use the TCP handshake. 

<ul>
<li>The client (connecting process) sends a SYN segment to the server to request a connection</li>
<li>Server sends the client a SYN-ACK segment to acknowledge the client's connection request</li>
<li>Client sends an ACK to the server to acknowledge the server's connection request</li>
</ul>

Once this connection is established, data can be exchanged over a TCP connection. The data is sent over in different segments and are tracked with TCP sequence numbers so they can be arranged in the correct order when they are delivered. In our email example, the transport layer attaches the destination port (25) to the source port of the source host.

## Exercise

No exercises for this lesson.

## Quiz Question

What is a reliable transport protocol?

## Quiz Answer

TCP
