# traceroute

## Lesson Content

The traceroute command is used to see how packets are getting routed. It works by sending packets with increasing TTL values, starting with 1. So the first router gets the packet, and it decrements the TTL value by one, thus dropping the packet. The router sends back an ICMP Time Exceeded message back to us. And then the next packet gets a TTL of 2, so it makes it past the first router, but when it gets to the second router the TTL is 0 and it returns another ICMP Time Exceeded message. Traceroute works this way because as it sends and drops packets it is build a list of routers that the packets traverse, until it finally gets to its destination and gets an ICMP Echo Reply message. 

Here's a little snippet of a traceroute: 

<pre>
$ traceroute google.com                                                                          
traceroute to google.com (216.58.216.174), 30 hops max, 60 byte packets                          
 1  192.168.4.254 (192.168.4.254)  0.028 ms  0.009 ms  0.008 ms                                  
 2  100.64.1.113 (100.64.1.113)  1.227 ms  1.226 ms 0.920 ms
 3  100.64.0.20 (100.64.0.20)  1.501 ms 1.556 ms  0.855 ms                                                                                 
</pre>

Each line is a router or machine that is between me and my target. It shows the name of the target and its IP address and the last three columns correspond to the round-trip time of a packet to get to that router. By default, we send three packets along the route.

## Exercise

Run the traceroute command on your machine and observe the output.

## Quiz Question

What gets decremented by one when making hops across the network?

## Quiz Answer

ttl
