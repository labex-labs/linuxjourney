# CIDR

## Lesson Content

CIDR (classless inter-domain routing) is used to represent a subnet mask in a more compact way. You may see subnets notated in CIDR notation, where a subnet such as the 10.42.3.0/255.255.255.0 is written as 10.42.3.0/24 which just means it includes both the subnet prefix and the subnet mask.

Remember an IP address consists of 4 bytes or 32 bits, CIDR indicates the amount of bits used as the network prefix. So 123.12.24.0/23 means that the first 23 bits are used. Well what does that mean? How many hosts is that? 

A simple trick is to subtract the total of bits an IP address can have (32) from the CIDR address (23), so that leaves 9 bits, 2^9 = 512, but we have to remove 2 addresses (subnet address and broadcast address) so we have 510 usable hosts.

## Exercise

No exercises for this lesson.

## Quiz Question

No questions move along!

## Quiz Answer