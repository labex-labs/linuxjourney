---
index: 9
lang: "en"
title: "DHCP Overview"
meta_title: "DHCP Overview - Network Basics"
meta_description: "Learn about DHCP (Dynamic Host Configuration Protocol) in Linux. Understand how DHCP assigns IP addresses and its four-step process. Start your Linux networking journey!"
meta_keywords: "DHCP, Dynamic Host Configuration Protocol, Linux networking, IP address, DHCP tutorial, beginner, guide"
---

## Lesson Content

An important networking concept that we did not go over yet is DHCP (Dynamic Host Configuration Protocol).

DHCP assigns IP addresses, subnet masks, and gateways to our machines. For example, let's say you have a cell phone and you want to get a cell phone number to start talking to people. You have to call up your phone carrier, and they will give you a number. As long as you pay your bills, you can keep using your phone. DHCP is the phone carrier in this case; it gives you an IP address so that you can talk to other IP addresses. You are also leased an IP address; these last for a certain period of time, then will get renewed depending on how you have your lease settings.

DHCP is great for many reasons: it allows a network administrator to not worry about assigning IP addresses, and it also prevents them from setting up duplicate IP addresses. Every physical network should have its own DHCP server so that a host can request an IP address. In a regular home setting, the router usually acts as the DHCP server.

The way DHCP gets all your dynamic host information is:

1. DHCP DISCOVER - This message is broadcasted to search for a DHCP server.
2. DHCP OFFER - The DHCP server in the network replies with an offer message. The offer contains a packet with DHCP lease time, subnet mask, IP address, etc.
3. DHCP REQUEST - The client sends out another broadcast to let all DHCP servers know which offer it accepted.
4. DHCP ACK - Acknowledgment is sent by the server.

DHCP gets more involved than this, but this is the gist of it.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of dynamic IP addressing and network configuration:

1. **[Manage IP Addressing in Linux](https://labex.io/labs/comptia-manage-ip-addressing-in-linux-592736)** - Practice using the `ip` command to inspect interfaces and specifically use `dhclient` to obtain a dynamic IP address, directly applying your knowledge of DHCP.
2. **[Identify MAC and IP Addresses in Linux](https://labex.io/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Learn to use the `ip a` command to identify network addressing information, including the IP addresses assigned by DHCP, and inspect network interfaces.
3. **[Explore IP Address Types and Reachability in Linux](https://labex.io/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Explore IP addressing and network reachability using `ping` and `ip a`, helping you understand how dynamically assigned IPs function within a network.

These labs will help you apply the concepts of dynamic IP assignment and network configuration in real scenarios and build confidence with Linux networking.

## Quiz Question

What are the steps in a DHCP request?

## Quiz Answer

DISCOVER, OFFER, REQUEST, ACK
