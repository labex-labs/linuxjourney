# ICMP

## Lesson Content

The Internet Control Message Protocol (ICMP) is part of the TCP/IP protocol suite, it used to send updates and error messages and is an extremely useful protocol used for debugging network issues such as a failed packet delivery.

Each ICMP message contains a type, code and checksum field. The type field is the type of ICMP message, the code is a sub-type and describes more information about the message and the checksum is used to detect any issues with the integrity of the message.

Let's look at some common ICMP Types:

<ul>
<li>Type 0 - Echo Reply</li>
<li>Type 3 - Destination Unreachable</li>
<li>Type 8 - Echo Request</li>
<li>Type 11 - Time Exceeded</li>
</ul>

When a packet can't get to a destination, Type 3 ICMP message is generated, within Type 3 there are 16 code values that will further describe why it can't get to the destination: 

<ul>
<li>Code 0 - Network Unreachable</li>
<li>Code 1 - Host Unreachable</li>
etc..etc..
</ul>

These messages will make more sense as we use some network troubleshooting tools.

## Exercise

No exercises for this lesson.

## Quiz Question

What is the ICMP type for echo request?

## Quiz Answer

8