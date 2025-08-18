---
lang: "en"
title: "Distance Vector Protocols"
meta_description: "Learn about distance vector protocols like RIP, how they work, and their limitations for network routing. Understand hop count and network efficiency."
meta_keywords: "distance vector protocols, RIP, routing information protocol, hop count, network routing, Linux networking, beginner guide, tutorial"
---

## Lesson Content

Distance vector protocols determine the path to other networks using the hop count a packet takes across the network. For example, if network A is 3 hops away and network B is next to network A, then we assume network B must be 4 hops away. In distance vector protocols, the next route would be the one with the least number of hops.

Distance vector protocols are great for small networks. However, when networks start to scale, it takes longer for the routers to converge because they periodically send the entire routing table out to every router. Another downside to distance vector protocols is efficiency; they choose routes that are closer in hops, but this may not always be the most efficient route.

One of the common distance vector protocols is RIP (Routing Information Protocol). It broadcasts the routing table to every router in the network every 30 seconds. For a large network, this can consume significant resources. Because of this, RIP limits its hop count to 15.

## Exercise

No exercises for this lesson.

## Quiz Question

True or false: Distance vector protocols use the route with the least amount of bandwidth?

## Quiz Answer

False
