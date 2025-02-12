# What is a router?

## Lesson Content

We've used this term router before, hopefully you know what one is, since you probably have one in your home. A router enables machines on a network to communicate with each other as well as other networks. On a typical router, you will have LAN ports, that allow your machines to connect to the same local area network and you will also have an Internet uplink port that connects you to the Internet, sometimes you'll see this port being labelled as WAN, because it is essentially connecting you to a wider network. When we do any sort of networking activity, it has to go through the router. The router decides where our network packets go and which ones come in. It routes our packets between multiple networks to get from it's source host to it's destination host. 

<b>How does a router work?</b>

Think about routing the same way as mail delivery, we have an address we want to send a letter to, when we send it off to the post office, they get the letter and see, oh this is going to California, I'll put it on the truck going to California (I honestly have no idea how the postal system works). The letter then gets sent to San Francisco, inside San Francisco there are different zip codes, and then in those zip codes there are smaller address codes, until finally someone is able to deliver your letter to the address you wanted. On the other hand, if you already lived in San Francisco and in the same zipcode, the mail deliverer will probably know exactly where the letter has to go to without handing it off to anyone else. 

When we route packets, they use similar address "routes", such as to get to network A, send these packets to network B. When we don't have a route set for that, we have a default route that our packets will use. These routes are set on a routing table that our system uses to navigate us across networks.

<b>Hops</b>

As packets move across networks, they travel in hops, a hop is how we roughly measure the distance that the packet must travel to get from the source to the destination. Let's say to I have two routers connecting host A to host B, so therefore we say there are two hops between host A and host B. Each hop is a intermediate device like the routers that we must pass through.

<b>Understanding the basic difference between Switching, Routing & Flooding?</b>
Packet SWITCHING is basically receiving, processing and forwarding data to the destination device.
ROUTING is a process of creating the routing table, so that we can do SWITCHING better.
Before routing, FLOODING was used. If a router don't know which way to send a packet than every incoming packet is sent through every outgoing link except the one it arrived on.

## Exercise

No exercises for this lesson.

## Quiz Question

How do packets measure distance?

## Quiz Answer

hops
