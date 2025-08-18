---
lang: "en"
title: "Network Layer"
meta_description: "Learn about the Network layer in Linux, how IP addresses route packets across subnets, and its role in data transmission. Start your Linux networking journey!"
meta_keywords: "Network layer, IP addresses, subnets, Linux networking, packet routing, beginner, tutorial, guide"
---

## Lesson Content

The Network layer determines the routing of our packets from our source host to a destination host. Fortunately, in our example, our packet is only traveling within the same network, but the Internet is made up of many networks. These smaller networks that make up the Internet are known as subnets. All subnets connect to each other in some way, which is why we are able to get to <https://www.google.com> even though it's on its own network. I won't go into detail as we have a whole course dedicated to subnets, but for now, in regards to our Network layer, know that the IP addresses define the rules to travel to different subnets.

In the Network layer, it receives the segment coming from the Transport layer and encapsulates this segment in an IP packet, then attaches the IP address of the source host and the IP address of the destination host to the packet header. So at this point, our packet has information about where it is going and where it came from. Now it sends our packet to the physical hardware layer.

## Exercise

No exercises for this lesson.

## Quiz Question

What are smaller networks that make up the Internet called?

## Quiz Answer

subnets
