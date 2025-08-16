# ICMP

## Lesson Content

The Internet Control Message Protocol (ICMP) is part of the TCP/IP protocol suite. It is used to send updates and error messages and is an extremely useful protocol for debugging network issues, such as failed packet delivery.

Each ICMP message contains a type, code, and checksum field. The type field indicates the type of ICMP message, the code is a subtype that provides more information about the message, and the checksum is used to detect any issues with the integrity of the message.

Let's look at some common ICMP Types:

- Type 0 - Echo Reply
- Type 3 - Destination Unreachable
- Type 8 - Echo Request
- Type 11 - Time Exceeded

When a packet cannot reach a destination, a Type 3 ICMP message is generated. Within Type 3, there are 16 code values that further describe why it cannot reach the destination:

- Code 0 - Network Unreachable
- Code 1 - Host Unreachable
  etc...etc...

These messages will make more sense as we use some network troubleshooting tools.

## Exercise

No exercises for this lesson.

## Quiz Question

What is the ICMP type for an echo request?

## Quiz Answer

8
