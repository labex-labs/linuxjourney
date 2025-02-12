# ping

## Lesson Content

One of the most simplest networking tools <b>ping</b>, it's used to test whether or not a packet can reach a host. It works by sending ICMP echo request (Type 8) packets to the destination host and waits for an ICMP echo reply (Type 0). Ping is successful when a host sends out the request packet and receives a response from the target. Let's look at an example: 

<pre>
pete@icebox:~$ ping -c 3 www.google.com
PING www.google.com (74.125.239.112) 56(84) bytes of data.
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=1 ttl=128 time=29.0 ms
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=2 ttl=128 time=23.7 ms
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=3 ttl=128 time=15.1 ms
</pre>

In this example, we are using ping to check if we can get to www.google.com. The -c flag (count) is used to stop sending echo request packets after the count has been reached. 

The first part says that we are sending 64-byte packets to 74.125.239.112 (google.com) and the rest show us the details of the trip. By default it sends a packet per second.

<b>icmp_seq</b>

The icmp_seq field is used to show the sequence number of packets sent, so in this case, I sent out 3 packets and we can see that 3 packets made it back. If you do a ping and you get some sequence numbers missing, that means that some connectivity issue is happening and not all your packets are getting through. If the sequence number is out of order, your connection is probably very slow as your packets are exceeding the one second default. 

<b>ttl</b>

The Time To Live (ttl) field is used as a hop counter, as you make hops, it decrements the counter by one and once the hop counter reaches 0, our packet dies. This is meant to give the packet a lifespan, we don't want our packets travelling around forever.

<b>time</b>

The roundtrip time it took from you sending the echo request packet to getting an echo reply. 

## Exercise

Do a ping on a website and look at the output you receive.

## Quiz Question

What is the roundtrip time unit of measurement?

## Quiz Answer

ms