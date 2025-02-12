# Network Addressing

## Lesson Content

Before we jump into seeing how a packet moves across a network, we have to familiarize ourselves with some terminology. When you mail a letter, you must know who it is being sent to and where it is coming from. Packets need the same information, our hosts and other hosts are identified using MAC (media access control) addresses and IP addresses, to make it easier on us humans we use hostnames to identify a host.

<b>MAC Addresses</b>

A MAC address is a unique identifier used as a hardware address. This address will never change. When you want to get access to the Internet, your machine needs to have a device called a network interface card. This network adapter has its own hardware address that's used to identify your machine. A MAC address for an Ethernet device looks something like this 00:C4:B5:45:B2:43. MAC addresses are given to network adapters when they are manufactured. Each manufacturer has an organizationally unique identifier (OUI) to identify them as the manufacturer. This OUI is denoted by the first 3 bytes of the MAC address. For example, Dell has 00-14-22, so a network adapter from Dell could have a MAC address like: 00-14-22-34-B2-C2. 

<b>IP Addresses</b>

An IP Address is used to identify a device on a network, they are hardware independent and can vary in syntax depending on if you are using IPv4 or IPv6 (more on this later). For now we'll assume you are using IPv4, so a typical IP address would look like: 10.24.12.4. IP addresses are used with the software side of networking. Anytime a system is connected to the Internet it should have an IP address. They can also change if your network changes and are unique to the entire Internet (this isn't always the case once we learn about NAT). 

Remember it takes both software and hardware to move packets across networks, so we have two identifiers for each, MAC (hardware) and IP (software).

<b>Hostnames</b>

One last way to identify your machines is through hostname. Hostnames take your IP address and allow you to tie that address to a human readable name. Instead of remembering 192.12.41.4 you can just remember myhost.com.

## Exercise

No exercises for this lesson.

## Quiz Question

How many bytes are in an IPv4 address?

## Quiz Answer

4
