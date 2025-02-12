# Routing Table

## Lesson Content

Look at your machine's routing table:

<pre>
pete@icebox:~$ sudo route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.224.2   0.0.0.0         UG    0      0        0 eth0
192.168.224.0   0.0.0.0         255.255.255.0   U     1      0        0 eth0
</pre>

<b>Destination</b>

In the first field, we have a destination IP address of 192.168.224.0, this says that any packet that tries to go to this network, goes out through my Ethernet cable (eth0). If I was 192.168.224.5 and wanted to get to 192.168.224.7, I would just use the network interface eth0 directly. 

Notice that we have addresses of <b>0.0.0.0</b> this means that no address is specified or it's unknown. So if for example, I wanted to send a packet to IP address 151.123.43.6, our routing table doesn't know where that goes, so it denotes it as 0.0.0.0 and therefore routes our packet to the Gateway.

<b>Gateway</b>

If we are sending a packet that is not on the same network, it will be sent to this Gateway address. Which is aptly named as being a Gateway to another network.

<b>Genmask</b>

This is the subnet mask, used to figure out what IP addresses match what destination. 

<b>Flags</b>

<ul>
<li>UG - Network is Up and is a Gateway</li>
<li>U - Network is Up</li>
</ul>

<b>Iface</b>

This is the interface that our packet will be going out of, eth0 usually stands for the first Ethernet device on your system. 

## Exercise

Look at your routing table and see where your packets can go.

## Quiz Question

Where are packets routed to if our routing table doesn't know?

## Quiz Answer

Gateway