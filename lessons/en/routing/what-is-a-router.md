---
title: "What is a router?"
description: "Learn what a router is, how it works, and its role in networking. Understand routing, hops, and packet delivery for beginners."
keywords: "router, networking, routing, hops, packet switching, Linux networking, beginner tutorial, network guide"
---

## Lesson Content

We've used this term router before; hopefully, you know what one is, since you probably have one in your home. A router enables machines on a network to communicate with each other as well as with other networks. On a typical router, you will have LAN ports that allow your machines to connect to the same local area network, and you will also have an internet uplink port that connects you to the internet. Sometimes you'll see this port labeled as WAN because it is essentially connecting you to a wider network. When we do any sort of networking activity, it has to go through the router. The router decides where our network packets go and which ones come in. It routes our packets between multiple networks to get from their source host to their destination host.

### How does a router work?

Think about routing the same way as mail delivery. We have an address we want to send a letter to. When we send it off to the post office, they get the letter and see, "Oh, this is going to California." I'll put it on the truck going to California (I honestly have no idea how the postal system works). The letter then gets sent to San Francisco. Inside San Francisco, there are different zip codes, and then in those zip codes, there are smaller address codes until finally, someone is able to deliver your letter to the address you wanted. On the other hand, if you already lived in San Francisco and in the same zip code, the mail deliverer will probably know exactly where the letter has to go without handing it off to anyone else.

When we route packets, they use similar address "routes," such as "to get to network A, send these packets to network B." When we don't have a route set for that, we have a default route that our packets will use. These routes are set on a routing table that our system uses to navigate us across networks.

### Hops

As packets move across networks, they travel in hops. A hop is how we roughly measure the distance that the packet must travel to get from the source to the destination. Let's say I have two routers connecting host A to host B; therefore, we say there are two hops between host A and host B. Each hop is an intermediate device, like the routers, that we must pass through.

### Understanding the basic difference between Switching, Routing & Flooding?

- **Packet SWITCHING** is basically receiving, processing, and forwarding data to the destination device.
- **ROUTING** is a process of creating the routing table so that we can do SWITCHING better.
- Before routing, **FLOODING** was used. If a router doesn't know which way to send a packet, then every incoming packet is sent through every outgoing link except the one it arrived on.

## Exercise

No exercises for this lesson.

## Quiz Question

How do packets measure distance?

## Quiz Answer

Hops
