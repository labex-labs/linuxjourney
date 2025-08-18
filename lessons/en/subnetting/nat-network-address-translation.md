---
index: 6
lang: "en"
title: "NAT"
meta_title: "NAT - Subnetting"
meta_description: "Learn about NAT (Network Address Translation) in Linux, how it works, and its role in network security. Understand private vs. public IPs. Linux networking guide."
meta_keywords: "NAT, Network Address Translation, Linux networking, private IP, public IP, Linux tutorial, beginner guide"
---

## Lesson Content

We've brought up NAT (Network Address Translation) before but didn't touch upon it. When we are working on our network, does that mean the internet can see our IP address? Not quite.

NAT makes a device like our router act as an intermediary between the internet and a private network. So, only a single, unique IP address is required to represent an entire group of computers.

Think of NAT as a receptionist in a large office. If someone wants to contact you, they only know the number to the whole office. The receptionist would then have to look for your extension number and forward the call to you.

### How does it work?

A simple case would look like this:

1. Patty wants to connect to <www.google.com>, so her machine sends this request through the router.
2. The router takes that request and opens its own connection to google.com, then it sends Patty's request once it makes a connection.
3. The router is the intermediary between Patty and <www.google.com>. Google doesn't know about Patty; instead, all it can see is the router.

NAT and packet routing in general can get pretty ugly, but we won't dive into the specifics.

## Exercise

No exercises for this lesson.

## Quiz Question

What is used to represent a single private address to the internet?

## Quiz Answer

NAT
