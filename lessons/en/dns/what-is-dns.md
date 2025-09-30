---
index: 1
lang: "en"
title: "What is DNS?"
meta_title: "What is DNS? - DNS"
meta_description: "Learn what DNS is and how it translates domain names to IP addresses. Understand this core internet concept with our beginner-friendly Linux guide."
meta_keywords: "DNS, Domain Name System, IP address, hostname, Linux networking, beginner, tutorial, guide"
---

## Lesson Content

Imagine if every time you wanted to do a search on Google you had to type in `http://192.78.12.4` instead of `www.google.com`. Well, without DNS ("Domain Name System"), that's exactly what would happen. Low-level networking only understands the raw IP address to identify a host. DNS allows us humans to keep track of websites and hosts by name instead of an IP address. It's like a contact list for the Internet. If you know someone's name but don’t know their phone number, you can simply look it up in your contacts list.

DNS is fundamentally a distributed database of hostnames to IP addresses. We manage our database so people know how to get to our site/domain, and somewhere else another person is managing their database so others can get to their domain. These domains are then able to talk to each other and build a massive contact list of the Internet.

In this course, we will go over some basics of DNS, but be wary that DNS is an exhaustive topic, and if you really want to get down and dirty with it, you'll need to do some additional research.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of DNS and hostname resolution:

1. **[Query DNS Records in Linux with dig and nslookup](https://labex.io/labs/comptia-query-dns-records-in-linux-with-dig-and-nslookup-592796)** - Learn to use essential Linux tools like `dig` and `nslookup` to query various DNS record types, helping you understand how hostnames are resolved to IP addresses.
2. **[Manage Local Hostname Resolution in Linux](https://labex.io/labs/comptia-manage-local-hostname-resolution-in-linux-592792)** - Practice editing the `/etc/hosts` file to manage local hostname resolution, a fundamental skill for controlling how your Linux system resolves names without relying on external DNS servers.
3. **[Set Up a Local Authoritative DNS Server on Linux](https://labex.io/labs/comptia-set-up-a-local-authoritative-dns-server-on-linux-592803)** - Gain hands-on experience by setting up and configuring your own local authoritative DNS server using `bind9`, allowing you to delve deeper into how DNS zones and records are managed.

These labs will help you apply the concepts in real scenarios and build confidence with DNS and hostname resolution in a Linux environment.

## Quiz Question

True or false: DNS helps us find MAC addresses for hostnames?

## Quiz Answer

False
