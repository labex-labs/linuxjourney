---
title: "Border Gateway Protocol"
description: "Learn about BGP, the Border Gateway Protocol, and how it enables internet routing between autonomous systems. Understand BGP basics for beginners."
keywords: "BGP, Border Gateway Protocol, internet routing, autonomous systems, Linux networking, BGP tutorial, network protocols, beginner guide"
---

## Lesson Content

The last important protocol we'll discuss is BGP. BGP is basically how the internet runs. It's used to collect and exchange routing information among autonomous systems. Think of an autonomous system as an internet service provider, a company, a university, any organization, etc. Without BGP, these systems would not know how to talk to each other; they would just be siloed off. Instead of routing inside these autonomous systems, BGP routes between them.

Let's say you were on your home network and I'm working from Starbucks. I want to be able to communicate with you, so I send an email. The network packet travels through Starbucks' network, bounces around there, and goes through the routing tables in Starbucks' network until it finally reaches a point at the border of the Starbucks network and passes it to a Border Gateway router. This router contains the information for my packet to leave the Starbucks network and traverse other networks.

## Exercise

No exercises for this lesson.

## Quiz Question

What protocol basically makes the internet work?

## Quiz Answer

BGP
