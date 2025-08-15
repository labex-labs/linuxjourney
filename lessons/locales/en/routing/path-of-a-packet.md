# Path of a Packet

## Lesson Content

<b>Let's look at how a packet travels within it's local network</b>

<ol>
<li>First the local machine will compare the destination IP address to see if it's in the same subnet by looking at its subnet mask.</li>
<li>When packets are sent they need to have a source MAC address, destination MAC address, source IP address and destination IP address, at this point we do not know the destination MAC address.</li>
<li>To get to the destination host, we use ARP to broadcast a request on the local network to find the MAC address of the destination host.</li>
<li>Now the packet can be successfully sent!</li>
</ol>

<b>Let's see how a packet travels outside it's network</b>

<ol>
<li>First the local machine will compare the destination IP address, since it's outside of our network, it does not see the MAC address of the destination host. And we can't use ARP because the ARP request is a broadcast to locally connected hosts.</li>
<li>So our packet now looks at the routing table, it doesn't know the address of the destination IP, so it sends it out to the default gateway (another router). So now our packet contains our source IP, destination IP and source MAC, however we don't have a destination MAC. Remember MAC addresses are only reached through the same network. So what does it do? It sends an ARP request to get the MAC address of the default gateway.</li>
<li>The router looks at the packet and confirms the destination MAC address, but it's not the final destination IP address, so it keeps looking at the routing table to forward the packet to another IP address that can help the packet move along to its destination. Everytime the packet moves, it strips the old source and destination MAC address and updates the packet with the new source and destination MAC addresses.</li>
<li>Once the packet gets forwarded to the same network, we use ARP to find the final destination MAC address</li>
<li>During this process, our packet doesn't change the source or destination IP address.</li>
</ol>

## Exercise

No exercises for this lesson.

## Quiz Question

How do we find the MAC address of an IP address?

## Quiz Answer

ARP
