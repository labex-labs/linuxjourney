# Network Interfaces

## Lesson Content

A network interface is how the kernel links up the software side of networking to the hardware side. We've already seen an example of this:

<pre>
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce  
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
</pre>

<b> The ifconfig command</b>

The <b>ifconfig</b> tool allows us to configure our network interfaces, if we don't have any network interfaces set up, the kernel's device drivers and the network won't know how to talk to each other. Ifconfig runs on bootup and configures our interfaces through config files, but we can also manually modify them. The output of ifconfig shows the interface name on the left side and the right side shows detailed information. You'll most commonly see interfaces named eth0 (first Ethernet card in the machine), wlan0 (wireless interface), lo (loopback interface). The loopback interface is used to represent your computer, it just loops you back to yourself. This is good for debugging or connecting to servers running locally.

The status of interfaces, can be up or down, as you can guess if you wanted to "turn off" an interface you can set it to go down. The fields you'll probably look at the most in the ifconfig output is the HWaddr (MAC address of the interface), inet address (IPv4 address) and inet6 (IPv6 address). Of course you can see that the subnet mask and broadcast address are there as well. You can also view interface information at /etc/network/interfaces.

<b>To create an interface and bring it up</b>

<pre>$ ifconfig eth0 192.168.2.1 netmask 255.255.255.0 up</pre>

This assigns an IP address and netmask to the eth0 interface and also turns it up.

<b>To bring up or down an interface</b>

<pre>
$ ifup eth0
$ ifdown eth0
</pre>

<b> The ip command </b>

The <b>ip</b> command also allows us to manipulate the networking stack of a system. Depending on the distribution you are using it may be the preferred method of manipulating your network settings.

Here are some examples of its use:

<b>To show interface information for all interfaces </b>
<pre>
$ ip link show
</pre>

<b>To show the statistics of an interface</b>
<pre>
$ ip -s link show eth0
</pre>

<b>To show ip addresses allocated to interfaces</b>
<pre>
$ ip address show
</pre>

<b>To bring interfaces up and down</b>
<pre>
$ ip link set eth0 up
$ ip link set eth0 down
</pre>

<b>To add an IP address to an interface</b>
<pre>
$ ip address add 192.168.1.1/24 dev eth0
</pre>

## Exercise

Try changing the state of your network interfaces to either up or down and observe what happens.

Can you change your network interface's with both the ifconfig and ip commands ?

## Quiz Question

What is the command to configure our network interfaces?

## Quiz Answer

ifconfig
