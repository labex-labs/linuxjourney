# Subnets

## Lesson Content

How can I tell if I'm on the same network as Patty? Well we can just look at the subnet short for subnetwork. A subnet is a group of hosts with IP addresses that are similar in a certain way. These hosts usually are in a proximate location from each other and you can easily send data to and from hosts on the same subnet. Think about it as sending mail in the same zip code, it's a lot easier than sending mail to a different state. 

For example, all hosts with an IP address that starts with 123.45.67 would be on the same subnet. My host has an IP of 123.45.67.8 and Patty's has an IP of 123.45.67.9. The common numbers are my network prefix and the 8 and 9 are our hosts, therefore my network is the same as Patty's. A subnet is divided into a network prefix, such as 123.45.67.0 and a subnet mask.

<b>Subnet Masks</b>

Subnet masks determine what part of your IP address is the network portion and what part is the host portion. 

A typical subnet mask can look something like this:

<pre>255.255.255.0</pre>

The 255 portion is actually our mask. To make this a little easier to understand, remember how we refer to each octet as 8 bits? In computer science a bit is denoted by a 0 or a 1 in binary form. When binary numbers are used, 1 means on and 0 means off. So what does 8 0's or 1's equal?

Punch into Google "binary to decimal calculator" and convert 11111111 into a decimal form. What do you get? 255! So an octet ranges from 0 to 255. So if we had a subnet mask of 255.255.255.0, and an IP address of 192.168.1.0, how many hosts are on that subnet? We'll find out the answer to that in our subnet math lesson.

Also when we talk about our subnet, we commonly denote it by the network prefix followed by the subnet mask:

<pre>123.234.0.0/255.255.0.0</pre>

<b>Why?</b>

Why on earth do we make subnets? Subnetting is used to segment networks and control the flow of traffic within that network. So a host on one subnet can’t interact with another host on a different subnet. 

But wait a minute, what if I want to connect to other hosts like yahoo.com? Then you need to connect subnets together. To connect subnets you just need to find the hosts that are connected to more than one subnet. For example, if my host at 192.168.1.129 is connected to a local network of 192.168.1.129/24 it can reach any hosts on that network. To reach hosts on the rest of the Internet, it needs to communicate through the router. Traditionally, on most networks with a subnet mask of 255.255.255.0, the router is usually at address 1 of the subnet, so 192.168.1.1. Now that router will have a port that connects it to another subnet (more in the Routing course). Certain IP addresses (private networks) are not visible to the internet, and we have things like NAT in place (more on this later).

## Exercise

Use ifconfig to view your subnet mask.

## Quiz Question

True or false, a subnet consists of a subnet mask and network prefix.

## Quiz Answer

True