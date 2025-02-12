# DHCP Overview

## Lesson Content

An important networking concept that we did not go over yet is DHCP (Dynamic Host Configuration Protocol)

DHCP assigns IP addresses, subnet masks and gateways to our machines. For example, let's say you have a cell phone and you want to get a cell phone number to start talking to people. You have to call up your phone carrier and they will give you a number. As long as your pay your bills you can keep using your phone. DHCP is the phone carrier in this case, it gives you an IP address so that you can talk to other IP addresses. You are also leased an IP address, these last for a certain period of time, then will get renewed depending on how you have your lease settings. 

DHCP is great for many reasons, it allows a network administrator to not worry about assigning IP addresses and it also prevents them from setting up duplicate IP addresses. Every physical network should have its own DHCP server so that a host can request an IP address. In a regular home setting, the router usually acts as the DHCP server.

The way DHCP gets all your dynamic host information is:

<ol>
<li>DHCP DISCOVER - This message is broadcasted to search for a DHCP server.</li>
<li>DHCP OFFER - The DHCP server in the network replies with an offer message. The offer contains a packet with DHCP lease time, subnet mask, IP address, etc.</li>
<li>DHCP REQUEST - The client sends out another broadcast to let all DHCP servers know which offer it accepted.</li>
<li>DHCP ACK - Acknowledgement is sent by the server.</li>
</ol>

DHCP gets more involved than this, but this is the gist of it.

## Exercise

No exercises for this lesson.

## Quiz Question

What are the steps in a DHCP request? 

## Quiz Answer

DISCOVER, OFFER, REQUEST, ACK
